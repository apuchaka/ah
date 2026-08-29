#!/usr/bin/env python3
"""header_refs.py — check cited section names against EXACT header text.

The gap this fills
------------------
`citation_audit.py` answers "does this `[[File]]` exist, and does a header
roughly matching the cited name exist in it?" That question cannot catch the
defect found in the L9 round (2026-08-29):

    [[15_24a_Paeds_-_Non-Accidental_Injury…]] Non-accidental injury
                                       real header: Non-accidental injury (NAI)

**A truncated header is a valid prefix and resolves fine.** The reference is
navigable, so nothing flags it — and yet it is wrong: it names a section that
does not exist under that name, and a reader searching the target file for the
literal string will not find it. ~20 of these were found in two files, all from
one habit: **dropping a header's parenthetical suffix.**

Worse, the same blind spot hides genuinely broken references. Two citations to
`[[03a_Anaesthetics_Primer]] Consent` sat in the corpus while 03a has no
Consent section at all — consent there is a bold sub-item inside
Pre-Operative Assessment.

What it does
------------
For every `[[File]] Section Name` citation it takes the text after the link and
resolves it against the target file's **exact, complete** header text:

  EXACT       the citation text starts with a real header, verbatim.
  TRUNCATED   no header matches, but a real header STARTS WITH the cited words —
              the cited name is a strict prefix of the real one. This is the
              class citation_audit.py is structurally blind to.
  NO-MATCH    no header matches and none starts with the cited words.
  NO-FILE     the [[target]] itself does not exist.

KNOWN LIMITATIONS — read before treating a hit as a defect
----------------------------------------------------------
  * **Where the name ends and prose begins is a guess.** "…]] Frailty for the
    reserve assessment" is a correct citation followed by prose. The resolver
    takes the LONGEST real header the text starts with, which handles this, but
    a citation followed by prose that happens to continue a different header
    name can mis-resolve. Read every hit.
  * **Bare `[[File]]` links carry no section name** and are not checked here.
    citation_audit.py counts them; neither script can validate them.
  * **A resolved name is not a correct citation.** It proves the section exists,
    not that it contains what the sentence claims.
  * **Sub-headers are indexed at every level (## to ####)**, so a citation to a
    `###` inside a `##` resolves. That is deliberate — the corpus cites both.
  * TRUNCATED is not always wrong. A file can hold both `Cervical cancer` and
    `Cervical cancer screening`; citing the former is exact, not truncated.
    The resolver prefers an exact match and only reports truncation when there
    is none.

Usage
-----
  scripts/header_refs.py                 # corpus sweep
  scripts/header_refs.py --file X.md     # one file's outgoing citations
  scripts/header_refs.py --all           # include EXACT matches in the listing
  scripts/header_refs.py --self-test     # fixtures, incl. the L9 cases

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

HEADER_RE = re.compile(r"^#{2,4}\s+(.*?)\s*$")
# A citation: [[Target]] followed by capitalised text that could be a section name.
CITE_RE = re.compile(r"\[\[([^\]|]+?)\]\]\s+(?=[A-Z0-9\"“])(.{3,140})")


def build_index(paths):
    """filename-stem -> ordered list of exact header strings."""
    idx = {}
    for p in paths:
        stem = os.path.basename(p)[:-3]
        hs = []
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                m = HEADER_RE.match(line)
                if m and m.group(1).strip():
                    hs.append(m.group(1).strip())
        idx[stem] = hs
    return idx


def _norm(w):
    """Strip trailing punctuation a citation may carry that a header will not.

    The first version stripped only ",.;:" — so a citation reading
    "…]] Small Bowel Obstruction), visible masses" failed to match the header
    "Small Bowel Obstruction (SBO)" at the third word, because "Obstruction),"
    kept its bracket. It then resolved to the two-word run shared with an
    unrelated "Small Bowel Bacterial Overgrowth" header and reported the
    citation as ambiguous rather than as the clean truncation it is.
    """
    return w.strip(",.;:)(]['\"").rstrip("—-–")


def _words(s):
    return [w for w in re.split(r"\s+", s.strip()) if w]


def resolve(cited_text, headers):
    """Classify a citation's trailing text against a file's exact headers.

    Returns (verdict, matched_or_suggested, cited_name).
    """
    t = cited_text.strip()
    # Headers in the numbered files carry a section number ("## 0.27 Chronic
    # Heart Failure") which citations routinely and legitimately omit. Index
    # each header under both forms; the first corpus run reported 40 such
    # citations as NO-MATCH before this was added, all of them correct.
    variants = {}
    numkeys = {}
    for h in headers:
        variants.setdefault(h, h)
        m = re.match(r"^(\d+(?:\.\d+)*[a-z]?)\s+", h)
        if m:
            variants.setdefault(h[m.end():], h)
            # The corpus also cites by BARE section number — "[[01_Cardiovascular]]
            # 0.34.5 for the Austroads timing". The first version indexed only the
            # full header and the number-stripped name, so every bare-number
            # citation fell through to NO-MATCH: 20 of the 33 reported by the
            # first corpus run were this artifact, all of them correct citations.
            numkeys.setdefault(m.group(1), h)

    # 1. EXACT — longest key the text starts with. Longest wins so that
    #    "Cervical cancer screening" is not mis-resolved to "Cervical cancer".
    exact = [k for k in variants if t == k or t.startswith(k)]
    # Bare-number keys must not swallow a longer number: "0.4" is not a match
    # for a citation reading "0.40)". Require a non-numeric boundary after it.
    for k, h in numkeys.items():
        if t == k or (t.startswith(k) and not t[len(k)].isdigit() and t[len(k)] != "."):
            exact.append(k)
            variants.setdefault(k, h)
    if exact:
        best = max(exact, key=len)
        return "EXACT", variants[best], best
    headers = list(variants)

    # 2. TRUNCATED — a real header starts with the leading words of the text.
    #    Walk the text word by word and keep the longest run that is a strict
    #    prefix of some header.
    tw = _words(t)
    best_run, best_hdr = 0, None
    for h in headers:
        hw = _words(h)
        n = 0
        while n < len(tw) and n < len(hw) and _norm(tw[n]) == _norm(hw[n]):
            n += 1
        # require the run to cover the whole header start and stop short of it
        if n >= 2 and n < len(hw) and n > best_run:
            best_run, best_hdr = n, h
    if best_hdr:
        return "TRUNCATED", best_hdr, " ".join(tw[:best_run])

    return "NO-MATCH", None, " ".join(tw[:6])


# ---------------------------------------------------------------------------
# CONTAINMENT CLAIMS — "the **Kellgren-Lawrence (K-L) grading** box under
# Investigations below".
#
# Added 2026-08-29, after the L9 rule was broken again in the G14 round by a
# claim no scan could see. The first version of this check tested whether the
# named section EXISTS — and would NOT have caught that error, because "OA of
# the knee" is a real header in that file. The claim was about CONTAINMENT:
# which section the box actually sits under. That is the thing to check.
#
# So: find the callout that contains the named thing, walk up to its enclosing
# header, and compare that against the section the sentence claims. Unlike a
# reminder to "grep the target first", this runs whether or not anyone
# remembers the rule.
CONTAIN_RE = re.compile(
    r"\*\*(?P<thing>[^*]{3,60}?)\*\*\s+(?:box|table|note|entry)\s+"
    r"(?:under|in|within)\s+(?:the\s+)?"
    r"(?P<sect>[A-Z][\w'’\-()/]*(?:\s+[A-Za-z][\w'’\-()/]*){0,5}?)"
    r"(?=\s+(?:below|above|section|entry|$|[,.;(]))"
)


def enclosing_header(lines, idx):
    for j in range(idx, -1, -1):
        m = HEADER_RE.match(lines[j])
        if m and m.group(1).strip():
            return m.group(1).strip()
    return None


def scan_bare(paths, index):
    """Does the named thing actually sit under the section claimed?"""
    out = []
    for p in paths:
        lines = open(p, encoding="utf-8").read().split("\n")
        for i, line in enumerate(lines):
            for m in CONTAIN_RE.finditer(line):
                thing, sect = m.group("thing").strip(), m.group("sect").strip()
                key = re.sub(r"\s+", " ", thing).lower()
                # where does the thing itself live? (a callout line, not this one)
                homes = [j for j, l in enumerate(lines)
                         if j != i and l.lstrip().startswith(">") and key in l.lower()]
                if not homes:
                    out.append((os.path.basename(p), i + 1, thing, sect, "NOT-FOUND"))
                    continue
                actual = enclosing_header(lines, homes[0])
                a = re.sub(r"^\d+(?:\.\d+)*[a-z]?\s+", "", actual or "").lower()
                if a != sect.lower() and not a.startswith(sect.lower()):
                    out.append((os.path.basename(p), i + 1, thing, sect, actual))
    return out


def scan(paths, index):
    out = []
    for p in paths:
        name = os.path.basename(p)
        for i, line in enumerate(open(p, encoding="utf-8").read().split("\n")):
            for m in CITE_RE.finditer(line):
                tgt, rest = m.group(1).strip(), m.group(2)
                if tgt not in index:
                    out.append((name, i + 1, "NO-FILE", tgt, rest[:60], None))
                    continue
                verdict, hdr, cited = resolve(rest, index[tgt])
                out.append((name, i + 1, verdict, tgt, cited, hdr))
    return out


# ---------------------------------------------------------------------------
# SELF-TEST — inline fixtures.
#
# The L9 instances that motivated this script are all FIXED in the corpus, so
# testing against live files would produce a suite that passes for the wrong
# reason and silently rots. positional_refs.py learned this the hard way; this
# script is built with fixtures from the start.
# ---------------------------------------------------------------------------

FIXTURES = [
    # (headers in target, citation trailing text, expected verdict, note)
    (["Non-accidental injury (NAI)", "Sexual abuse"], "Non-accidental injury for the SA framework",
     "TRUNCATED", "L9: dropped parenthetical — the commonest form"),
    (["Abuse of Older People (Elder Abuse) and Carer Stress"], "Abuse of Older People and the",
     "TRUNCATED", "L9: dropped a parenthetical AND a trailing clause"),
    (["Human immunodeficiency virus (HIV)", "Measles"], "Human Immunodeficiency Virus for the detail",
     "NO-MATCH", "L9: wrong CASE as well as truncated — must not silently pass"),
    (["General Anaesthesia", "Pre-Operative Assessment", "Airway Adjuncts"], "Consent for the anaesthetic-specific",
     "NO-MATCH", "L9: cited a section that does not exist at all"),
    (["Frailty", "Falls in Older People"], "Frailty for the reserve assessment that should inform it",
     "EXACT", "correct citation followed by prose — must NOT be flagged"),
    (["Cervical cancer", "Cervical cancer screening"], "Cervical cancer screening and the pathway after",
     "EXACT", "longest-wins: must resolve to the screening header, not the shorter one"),
    (["Cervical cancer", "Cervical cancer screening"], "Cervical cancer for the disease-level detail",
     "EXACT", "the shorter header is itself real — exact, not truncated"),
    (["Continuity of Care, and What Makes General Practice Different"], "Continuity of Care for the",
     "TRUNCATED", "L9: header contains a comma; truncation at the comma"),
    (["0.34.5 Austroads cardiovascular driving rules (private vehicle standards)", "0.34.4 Antiplatelets"],
     "0.34.5 for the Austroads timing", "EXACT",
     "BARE SECTION NUMBER — 20 of the first run's 33 NO-MATCHes were this artifact"),
    (["0.4 Atrial Fibrillation", "0.40 Something Else"], "0.40), more concerning ventricular",
     "EXACT", "bare number must not let 0.4 swallow a citation to 0.40"),
    (["0.4 Atrial Fibrillation"], "0.40), more concerning ventricular", "NO-MATCH",
     "and with no 0.40 header, 0.4 must NOT claim it either"),
]


def self_test():
    print("SELF-TEST — inline fixtures (L9 cases + the false positives to avoid)\n")
    p = f = 0
    for headers, cited, expect, note in FIXTURES:
        got, hdr, name = resolve(cited, headers)
        ok = got == expect
        print("  %-4s %-11s expected %-10s :: %s" % ("ok" if ok else "FAIL", got, expect, note))
        if not ok:
            print("        cited=%r -> matched=%r" % (cited[:60], hdr))
        p, f = p + ok, f + (not ok)
    print("\n  %d passed, %d failed" % (p, f))
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--all", action="store_true", help="list EXACT matches too")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(1 if self_test() else 0)

    paths = [p for p in sorted(glob.glob("*.md")) if os.path.basename(p) not in META_FILES]
    index = build_index(paths)
    targets = [p for p in paths if not args.file or os.path.basename(p) == args.file]
    rows = scan(targets, index)

    print("=" * 78)
    print(" header_refs.py — %d files indexed, %d named-section citations checked"
          % (len(index), len(rows)))
    print("=" * 78)
    for verdict, label in (("NO-FILE", "NO-FILE — the [[target]] does not exist"),
                           ("NO-MATCH", "NO-MATCH — no header matches, none starts with the cited words"),
                           ("TRUNCATED", "TRUNCATED — cited name is a strict PREFIX of the real header")):
        hits = [r for r in rows if r[2] == verdict]
        print("\n%s: %d" % (label, len(hits)))
        for r in hits:
            print("   %s:%d  [[%s]]" % (r[0][:44], r[1], r[3][:44]))
            print("       cited: %s" % r[4])
            if r[5]:
                print("       real : %s" % r[5])
    bare = scan_bare(targets, index)
    print("\nCONTAINMENT CLAIMS — '**X** box under Y' where X does not sit"
          "\n  under Y: %d" % len(bare))
    for b in bare:
        print("   %s:%d  %r claimed under %r — actually under %r"
              % (b[0][:40], b[1], b[2][:40], b[3], b[4]))

    ok = [r for r in rows if r[2] == "EXACT"]
    print("\nEXACT: %d" % len(ok))
    if args.all:
        for r in ok:
            print("   %s:%d -> %s" % (r[0][:40], r[1], r[5]))
    print("\n" + "-" * 78)
    print("TRUNCATED is the class citation_audit.py cannot see: a truncated header")
    print("is a valid prefix and resolves. Read every hit — see KNOWN LIMITATIONS.")
    print("-" * 78)


if __name__ == "__main__":
    main()
