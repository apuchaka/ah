#!/usr/bin/env python3
"""positional_refs.py — surface positional references whose target may no longer exist.

The problem this exists for
---------------------------
`citation_audit.py` validates `[[File]]` wikilink targets. It cannot see a
reference made with a **positional word** — "the UK figures below", "the table
above", "the note that follows" — because there is no link to resolve. Those
references are silently invalidated by any edit that removes what they point at.

The specific defect that produced this scan (found in the N7 pass, 2026-08-28):

    08_08 chlamydia:  "...genuinely different from the UK figures below."
                      The UK figures had been deleted by a localisation pass.
                      The box pointed at nothing. Said it three times.

That is a **localisation-pass hazard**: a verification box is written to contrast
AU practice against the UK content it is replacing, then the UK content is
removed and the box is left comparing against a void. It reads as authoritative
and sends the reader looking for something that is not there.

What it does
------------
Finds positional references and tries to resolve them in the direction indicated.
Two tiers, reported separately:

  TIER A — QUALIFIED reference. The phrase names a qualifier the target must
           contain ("the **UK** figures below", "the **NICE** table above").
           This is checkable: does that qualifier token actually appear in the
           indicated direction? Scoped outward in three steps, because scope is
           what separates a genuine strand from a false positive:
               1. same '##' section, in the indicated direction, OUTSIDE the
                  callout block the reference sits in   <- the real target
               2. the remainder of the same callout block
                  (legitimate when the box quotes the figures itself)
               3. elsewhere in the file, in the indicated direction
           Nothing found at any scope -> STRANDED.

  TIER B — STRUCTURAL reference ("the table below", "the note above", "the list
           below", "the algorithm below"). Checks for the named structure in
           that direction within the section. Over-surfaces heavily by design;
           reported as informational, not as findings.

KNOWN LIMITATIONS — read before treating a hit as a gap
-------------------------------------------------------
  * **Candidate generator, not a finding list.** Tuned to over-surface. Every
    hit needs reading against the file before it is called a defect.
  * **Prose references are invisible to it.** "as described earlier", "the
    approach set out previously", "see the discussion of this in the preceding
    section" carry no positional keyword this matches. This is the same class of
    blind spot the scan exists to fix, one level up.
  * **Tier C can mistake a SIBLING REFERENCE for the referent.** `02_Respiratory`
    line 114 says "per the COPD-X framework above"; the COPD-X box really is
    above, at line 103, but the literal phrase "COPD-X framework" next occurs
    at line 143 — another reference, not the target. The scan reports
    MISDIRECTED. Read every hit: the question is where the CONTENT is, not
    where the phrase recurs.
  * **Tier A depends on the qualifier being a word.** "the figures below" with
    no qualifier is unresolvable mechanically — it lands in Tier B, where the
    check is weak.
  * **A resolved reference is not a correct one.** Finding "UK" below proves a
    token is present, not that it is the content the sentence promises.
  * **Section scoping is by '##' only.** A reference pointing across a '##'
    boundary resolves at scope 3 and is reported as WEAK rather than clean.

Usage
-----
  scripts/positional_refs.py                 # tier A findings + tier B summary
  scripts/positional_refs.py --all           # include the full tier B listing
  scripts/positional_refs.py --file 08_08*   # one file
  scripts/positional_refs.py --self-test     # regression cases from the N7 pass

Exit status: 0 always — this reports, it does not gate.
"""

import argparse
import glob
import os
import re
import sys

META_FILES = {
    "CLAUDE.md", "CLAUDE_CODE_PROMPT.md", "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md", "PENDING_GUIDELINE_CHECKS.md",
    "PHASE_EXECUTION_WORKFLOW.md", "RECOMMENDED_WORKFLOW.md",
}

# Qualifier tokens a positional reference can name, which are then checkable.
# Deliberately weighted to the localisation hazard this scan was built for.
QUALIFIERS = [
    "UK", "NICE", "NHS", "BNF", "British", "DVLA", "BASHH", "RCOG", "SIGN",
    "Australian", "Australia", "AU", "RACGP", "RANZCOG", "ANZCA", "eTG", "AMH",
    "Austroads", "ANZCOR", "ASCIA", "NHMRC", "TGA", "AIHW", "US", "American",
]

POSITIONAL = r"(?:below|above)"

# TIER A: a qualifier inside the noun phrase immediately preceding below/above.
#   "...from the UK figures below"      "...the NICE table above"
QUALIFIED_RE = re.compile(
    r"\b(?P<qual>%s)\b(?P<mid>[^.;:!?\n]{0,40}?)\s(?P<pos>%s)\b"
    % ("|".join(QUALIFIERS), POSITIONAL)
)

# TIER B: a structural noun immediately preceding below/above.
STRUCTURES = {
    "table": r"^\s*\|.*\|",
    "list": r"^\s*(?:[-*+]|\d+\.)\s",
    "note": r"^>\s*\[!",
    "box": r"^>\s*\[!",
    "callout": r"^>\s*\[!",
    "warning": r"^>\s*\[!",
    "algorithm": r"^\s*(?:[-*+]|\d+\.)\s",
    "criteria": r"^\s*(?:[-*+]|\d+\.)\s",
    "figures": r"\d",
    "regimen": r"\d",
    "doses": r"\d",
    "schedule": r"\d",
    "section": r"^#{2,6}\s",
    "entry": r"^#{2,6}\s",
}
STRUCTURAL_RE = re.compile(
    r"\b(?P<struct>%s)\s+(?P<pos>%s)\b" % ("|".join(STRUCTURES), POSITIONAL), re.I
)

# TIER C: a NAMED referent — "See Kellgren-Lawrence grading above".
#
# Added 2026-08-29 (G14) after this scan MISSED the simplest possible instance
# of the class it exists for: 12_01 said "See Kellgren-Lawrence grading above"
# while the K-L grading box sat 21 lines BELOW. Tier A needs an AU/UK
# qualifier and there is none; Tier B needs a structural noun and "grading" is
# not one. So a named, checkable, wrong reference fell through both.
#
# The resolution here is stronger than either other tier, because a proper
# name can simply be searched for: the direction is checkable, not guessed.
#   MISDIRECTED  the name appears ONLY in the opposite direction. A defect.
#   OK           the name appears in the direction claimed.
#   UNRESOLVED   the name appears nowhere else in the file.
NAMED_RE = re.compile(
    r"\b(?:[Ss]ee|[Pp]er|[Ff]rom|[Ii]n)\s+(?P<name>(?:the\s+)?[A-Z][\w'’-]*"
    r"(?:[- ][A-Za-z][\w'’-]*){0,3})\s+(?P<pos>%s)\b" % POSITIONAL
)
# Words that start a sentence but are not a referent name.
NAMED_STOP = {"the", "this", "that", "these", "those", "it", "there", "note",
              "table", "list", "box", "section", "entry", "figures", "doses"}


def resolve_named(lines, idx, name, pos):
    """Does `name` actually appear in the direction the sentence claims?"""
    key = re.sub(r"^the\s+", "", name, flags=re.I).strip()
    head = key.split()[0]
    if head.lower() in NAMED_STOP or len(head) < 4:
        return None
    # Match the FULL name, not just its head word.
    #
    # The first version matched on the head alone, so "see Anterior Uveitis
    # above" resolved OK against an unrelated "Anterior ischaemic optic
    # neuropathy" 19 lines up, while the real Anterior Uveitis section sat 242
    # lines BELOW. A false OK is the one outcome this scan must not produce, so
    # the full name decides; the head is used only to detect that SOME related
    # text exists, which downgrades to UNRESOLVED rather than claiming OK.
    # Allow a parenthetical gloss between the words of the name, so
    # "Kellgren-Lawrence grading" still matches "Kellgren-Lawrence (K-L)
    # grading" — the corpus routinely introduces an acronym mid-name.
    sep = r"[\s\-]+(?:\([^)]{0,24}\)[\s\-]*)?(?:\*\*)?"
    full = re.compile(r"\b" + sep.join(re.escape(w) for w in key.split()), re.I)
    before = any(full.search(l) for l in lines[:idx])
    after = any(full.search(l) for l in lines[idx + 1:])
    if not before and not after:
        hx = re.compile(re.escape(head), re.I)
        if any(hx.search(l) for l in lines[:idx] + lines[idx + 1:]):
            return "UNRESOLVED", key
    claimed_before = pos.lower() == "above"
    if (claimed_before and before) or (not claimed_before and after):
        return "OK", key
    if (claimed_before and after) or (not claimed_before and before):
        return "MISDIRECTED", key
    return "UNRESOLVED", key


def nearest_qualifiers(line):
    """Yield one match per positional word, using the NEAREST qualifier to it.

    re.finditer scans left to right and so returns the *leftmost* qualifier,
    which is wrong: in "Australian choices differ from the UK NICE regimen
    below" the referent is the UK regimen, not anything Australian. Resolving
    against the wrong qualifier produced both spurious strands and missed ones
    in this scan's first corpus run.
    """
    best = {}
    for m in QUALIFIED_RE.finditer(line):
        key = m.span("pos")
        if key not in best or m.start("qual") > best[key].start("qual"):
            best[key] = m
    return [best[k] for k in sorted(best)]


def load_files(pattern=None):
    out = []
    for path in sorted(glob.glob(pattern or "*.md")):
        name = os.path.basename(path)
        if name in META_FILES:
            continue
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        out.append({"name": name, "lines": lines})
    return out


def section_bounds(lines, idx):
    """Return (start, end) line indices of the '##' section containing idx."""
    start = 0
    for i in range(idx, -1, -1):
        if re.match(r"^##\s", lines[i]):
            start = i
            break
    end = len(lines)
    for i in range(idx + 1, len(lines)):
        if re.match(r"^##\s", lines[i]):
            end = i
            break
    return start, end


def callout_bounds(lines, idx):
    """Return (start, end) of the contiguous '>' block containing idx, else None."""
    if not lines[idx].lstrip().startswith(">"):
        return None
    start = idx
    while start > 0 and lines[start - 1].lstrip().startswith(">"):
        start -= 1
    end = idx
    while end + 1 < len(lines) and lines[end + 1].lstrip().startswith(">"):
        end += 1
    return start, end


# A line that merely COMMENTS on the qualifier is not the referent. This filter
# exists because the first version of this scan graded three genuine strands OK:
# e.g. 02_Respiratory said "...differ materially from the UK NICE regimen below",
# and "UK" did appear below — inside a further sentence saying the AU regimen is
# "not the UK one". Commentary about the absent content was being counted as the
# absent content. Evidence has to be the thing, not a second mention of the thing.
COMMENTARY_RE = re.compile(
    r"(?:\bdiffer|\bunlike\b|rather than|no longer|not the\b|not in the\b|"
    r"not part of\b|not mentioned\b|should not be\b|-sourced\b|-style\b|"
    r"-derived\b|\bpreviously carried\b|\bwritten against\b)", re.I)


def _search(lines, rng, rx, skip=None, exclude_commentary=False):
    """True if rx matches any line in rng, excluding the skip range.

    With exclude_commentary, lines that only *talk about* the qualifier are not
    accepted as evidence that the referent is present.
    """
    for i in rng:
        if skip and skip[0] <= i <= skip[1]:
            continue
        if not (0 <= i < len(lines)):
            continue
        if not rx.search(lines[i]):
            continue
        if exclude_commentary and COMMENTARY_RE.search(lines[i]):
            continue
        return True
    return False


def resolve_qualified(lines, idx, qual, pos):
    """Resolve a qualified positional reference. Returns (verdict, scope)."""
    rx = re.compile(r"\b%s\b" % re.escape(qual))
    sec_start, sec_end = section_bounds(lines, idx)
    call = callout_bounds(lines, idx)

    if pos == "below":
        sec_rng = range(idx + 1, sec_end)
        file_rng = range(sec_end, len(lines))
        call_rng = range(idx + 1, call[1] + 1) if call else range(0)
    else:
        sec_rng = range(sec_start, idx)
        file_rng = range(0, sec_start)
        call_rng = range(call[0], idx) if call else range(0)

    if _search(lines, sec_rng, rx, skip=call, exclude_commentary=True):
        return "OK", "same section, outside the callout"
    if call and _search(lines, call_rng, rx, exclude_commentary=True):
        return "SELF", "only inside the same callout block"
    if _search(lines, file_rng, rx, exclude_commentary=True):
        return "WEAK", "only across a '##' boundary elsewhere in the file"
    if _search(lines, sec_rng, rx, skip=call) or _search(lines, file_rng, rx):
        return "COMMENT-ONLY", "qualifier appears only in commentary about it, not as the referent"
    return "STRANDED", "not found in the indicated direction at any scope"


def resolve_structural(lines, idx, struct, pos):
    rx = re.compile(STRUCTURES[struct.lower()], re.I | re.M)
    sec_start, sec_end = section_bounds(lines, idx)
    rng = range(idx + 1, sec_end) if pos == "below" else range(sec_start, idx)
    return ("OK", "structure present in section") if _search(lines, rng, rx) \
        else ("STRANDED", "no matching structure in the indicated direction")


def scan(files):
    tier_a, tier_b, tier_c = [], [], []
    for f in files:
        lines = f["lines"]
        for i, line in enumerate(lines):
            for m in nearest_qualifiers(line):
                qual, pos = m.group("qual"), m.group("pos")
                # "differs from X below" where X is the *source of truth*
                # verified against is a different sentence shape; keep it, the
                # resolver decides.
                verdict, scope = resolve_qualified(lines, i, qual, pos)
                tier_a.append((f["name"], i + 1, qual, pos, verdict, scope, line.strip()))
            for m in STRUCTURAL_RE.finditer(line):
                struct, pos = m.group("struct"), m.group("pos")
                if QUALIFIED_RE.search(line):
                    continue  # already covered, more precisely, by tier A
                verdict, scope = resolve_structural(lines, i, struct, pos)
                tier_b.append((f["name"], i + 1, struct, pos, verdict, scope, line.strip()))
            for m in NAMED_RE.finditer(line):
                if QUALIFIED_RE.search(line) or STRUCTURAL_RE.search(line):
                    continue  # covered more precisely by tier A or B
                r = resolve_named(lines, i, m.group("name"), m.group("pos"))
                if r:
                    tier_c.append((f["name"], i + 1, r[1], m.group("pos"),
                                   r[0], None, line.strip()))
    return tier_a, tier_b, tier_c


# ---------------------------------------------------------------------------
# SELF-TEST
#
# These run against inline FIXTURES, not against the live corpus. The first
# version ran against real lines in real files — and every one of its cases
# evaporated the moment those lines were fixed, which is the opposite of what a
# regression suite is for. Fixtures reproduce the shape of each defect so the
# suite still means something after the corpus is clean.
#
# The property asserted is NOT the exact verdict. The non-OK verdicts only grade
# how hard a hit is to dismiss, and a genuine strand can land in any of them.
# The one thing this scan can actually guarantee is that **no genuine defect is
# graded OK** — that is what is tested.
# ---------------------------------------------------------------------------

FIXTURES = [
    ("strand-below: AU content replaced the UK content it points at",
     """## Colorectal Cancer
> [!info] Verified against the NBCSP — Australia's program differs materially from the UK figures below.
> **Screening:** iFOBT, free, every 2 years, ages 45-74.

**Ix:** bloods — FBC.
""", 2, False),

    ("strand-above: no UK regimen anywhere above",
     """## Hypertension
### Treatment threshold
Treat if <80yo AND target organ damage.

> [!info] Verified against AMH — Australian approach differs from the UK NICE stepwise regimen above.
> Australian decisions are driven by absolute CVD risk.
""", 5, False),

    ("comment-only: qualifier below is commentary ABOUT the absent content",
     """## Pneumonia
> [!info] Australian choices differ materially from the UK NICE regimen below; use the AU regimen.
> - Low severity: amoxicillin.
> Note the AU regimen is built around amoxicillin, not the UK's co-amoxiclav.
""", 2, False),

    ("contradiction: the content below now says the OPPOSITE of the reference",
     """## Osteoporosis
> [!info] Strontium should not be offered the way the UK-style note below suggests.

- **Mx:**
  - Alendronate first-line. Strontium ranelate is no longer recommended in Australia.
""", 2, False),

    ("legitimate: the box quotes the figures it refers to, on its own next line",
     """## OGD
> [!warning] Could not confirm an Australian timing to replace the UK figures below.
> **Stopping medications before OGD (illustrative):** PPI — 2 weeks; H2RA — 3 days.
""", 2, True),

    ("legitimate: a real UK block does exist further down the same section",
     """## Pneumonia
> [!info] Australian choices differ from the UK NICE regimen below; use the AU regimen.
> - Low severity: amoxicillin.

**Mx:** as per the AU regimen above.

> UK figures (unverified for AU use): co-amoxiclav 500/125mg tds x 5 days.
""", 2, True),
]


# Tier C fixtures: (label, text, lineno, expected verdict).
# The first is THE case this scan missed in the live corpus on 2026-08-29 —
# a scan must carry the instance that defeated it.
NAMED_FIXTURES = [
    ("K-L: 'see X above' where X is 21 lines BELOW — the missed case",
     """## Osteoarthritis (OA)
### OA of the knee
- See Kellgren-Lawrence grading above (not repeated here) for the scale.

### OA of the hand
> [!note] **Kellgren-Lawrence (K-L) grading** is the standard radiographic scale:
> - Grade 1: doubtful narrowing.
""", 3, "MISDIRECTED"),
    ("correct: 'see X above' and X really is above",
     """> [!note] **Kellgren-Lawrence (K-L) grading** is the standard scale.
- See Kellgren-Lawrence grading above for the scale.
""", 2, "OK"),
    ("Anterior Uveitis: head word matches an UNRELATED entry above",
     """## Sudden Vision Loss
| Anterior ischaemic optic neuropathy | Acute glaucoma |
- See Anterior Uveitis above for the detail.

## Anterior Uveitis
- **D:** inflammation of the uveal tract.
""", 3, "MISDIRECTED"),
    ("named referent absent from the file entirely",
     """## Ankle
- See Ottawa rules above for the imaging decision.
""", 2, "UNRESOLVED"),
    ("must not fire on a structural noun — that is tier B's job",
     """## Thing
- See the table above for the doses.
""", 2, None),
]


def self_test(_files=None):
    passed = failed = 0
    print("SELF-TEST — inline fixtures (see note in source)")
    print("Asserting only that no genuine defect is graded OK.\n")
    for label, text, lineno, is_legit in FIXTURES:
        lines = text.split("\n")
        idx = lineno - 1
        verdicts = []
        for m in nearest_qualifiers(lines[idx]):
            verdicts.append(resolve_qualified(lines, idx, m.group("qual"), m.group("pos"))[0])
        if not verdicts:
            print("  FAIL  %-58s no reference detected" % label[:58])
            failed += 1
            continue
        v = verdicts[0]
        if is_legit:
            # A legitimate reference SHOULD resolve. It is not a failure if it
            # over-surfaces — that is the design — so this is reported, not failed.
            note = "resolves" if v == "OK" else "over-surfaced (acceptable: %s)" % v
            print("  ok    %-58s %s" % (label[:58], note))
            passed += 1
        elif v == "OK":
            print("  FAIL  %-58s graded OK — would be missed" % label[:58])
            failed += 1
        else:
            print("  ok    %-58s %s" % (label[:58], v))
            passed += 1
    print("\n  TIER C — named referents")
    for label, text, lineno, expect in NAMED_FIXTURES:
        lines = text.split("\n")
        idx = lineno - 1
        got = None
        for m in NAMED_RE.finditer(lines[idx]):
            if QUALIFIED_RE.search(lines[idx]) or STRUCTURAL_RE.search(lines[idx]):
                continue
            r = resolve_named(lines, idx, m.group("name"), m.group("pos"))
            if r:
                got = r[0]
                break
        ok = got == expect
        print("  %-5s %-58s %s" % ("ok" if ok else "FAIL", label[:58], got))
        passed, failed = passed + ok, failed + (not ok)

    print("\n  %d passed, %d failed" % (passed, failed))
    return failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="glob for files to scan (default: *.md)")
    ap.add_argument("--all", action="store_true", help="show the full tier B listing")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(1 if self_test() else 0)
    files = load_files(args.file)

    tier_a, tier_b, tier_c = scan(files)

    print("=" * 78)
    print(" positional_refs.py — %d content files" % len(files))
    print("=" * 78)

    stranded = [r for r in tier_a if r[4] in ("STRANDED", "COMMENT-ONLY")]
    selfref = [r for r in tier_a if r[4] == "SELF"]
    weak = [r for r in tier_a if r[4] == "WEAK"]
    ok = [r for r in tier_a if r[4] == "OK"]

    print("\nTIER A — qualified positional references (%d found)\n" % len(tier_a))
    for label, rows in (("STRANDED / COMMENT-ONLY — no referent found", stranded),
                        ("WEAK — resolves only across a '##' boundary", weak),
                        ("SELF — resolves only inside the same callout", selfref)):
        print("  %s: %d" % (label, len(rows)))
        for r in rows:
            print("     %s:%d  '%s ... %s'" % (r[0], r[1], r[2], r[3]))
            print("        %s" % (r[6][:150]))
        if rows:
            print()
    print("  OK — resolves in the same section, outside the callout: %d" % len(ok))

    b_str = [r for r in tier_b if r[4] == "STRANDED"]
    print("\nTIER B — structural positional references (%d found, %d unresolved)"
          % (len(tier_b), len(b_str)))
    print("  Weak check by design; informational, not findings.")
    if args.all:
        for r in b_str:
            print("     %s:%d  '%s %s' — %s" % (r[0], r[1], r[2], r[3], r[5]))
            print("        %s" % (r[6][:150]))
    elif b_str:
        print("  Re-run with --all to list the %d unresolved." % len(b_str))

    c_bad = [r for r in tier_c if r[4] == "MISDIRECTED"]
    c_unres = [r for r in tier_c if r[4] == "UNRESOLVED"]
    print("\nTIER C — named referents (%d found)" % len(tier_c))
    print("  MISDIRECTED — the name appears ONLY in the opposite direction: %d" % len(c_bad))
    for r in c_bad:
        print("     %s:%d  '%s ... %s'" % (r[0], r[1], r[2], r[3]))
        print("        %s" % (r[6][:150]))
    print("  UNRESOLVED — the name appears nowhere else in the file: %d" % len(c_unres))
    if args.all:
        for r in c_unres:
            print("     %s:%d  '%s ... %s'" % (r[0], r[1], r[2], r[3]))
            print("        %s" % (r[6][:150]))
    elif c_unres:
        print("  Re-run with --all to list them.")

    print("\n" + "-" * 78)
    print("Reminder: STRANDED is a candidate, not a finding. Read the file before")
    print("editing. And see KNOWN LIMITATIONS in the header — prose references")
    print("carrying no positional keyword are invisible to this scan entirely.")
    print("-" * 78)


if __name__ == "__main__":
    main()
