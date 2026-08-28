#!/usr/bin/env python3
"""citation_audit.py — bidirectional cross-reference accuracy (Step 8).

Step 1 (check_structure.sh) proves a `[[Target]]` link RESOLVES — the file
exists. This script asks the harder question: does the SECTION NAME written
beside the link still exist inside that file? A target file restructured in a
later round leaves every citing file's section name silently stale, and nothing
else in the pipeline detects it.

Bidirectional, per Step 8:
  OUTGOING  citations made BY the files in --range
  INCOMING  citations from ANYWHERE in the project pointing INTO --range
Run with no --range and it audits every citation in the project, both ways.

What counts as a citation
-------------------------
A `[[Target]]` (or `[[Target|alias]]`) followed by candidate section text, cut
at the first terminator. Terminators are the punctuation and connective words
that in this corpus reliably end a citation:
    )  ]  ;  :  .  ,  --  em/en dash  newline
    for | not repeated | not duplicated | given | see | and the | which | where
This directly targets the documented parsing artifact where the regex ran past
a citation's closing parenthesis and swallowed an unrelated following clause
("...Idiopathic Intracranial Hypertension); nystagmus").

What counts as a match
----------------------
The cited name is compared against the target file's headers AND, deliberately,
against its BOLD LIST-ITEM LABELS and CALLOUT TITLES (`**Text**`, `> [!info] Text`).
Step 8 records that a genuine false positive came from citing an `[!info]` box
title rather than a markdown header ("Kocher criteria for diagnosis of septic
arthritis"). A header-only scan reports those as broken when they are correct.

Matching is case-insensitive and Unicode-folded, and accepts exact / substring /
containing / high-similarity (>=0.86) forms. The matched anchor and how it
matched are always printed, so a loose match can be audited rather than trusted.

KNOWN LIMITATIONS — read before trusting a BROKEN line
------------------------------------------------------
  * BROKEN is a candidate, not a verdict. Open the target file and look.
  * Free-prose citations ("see the stroke section of [[04_Neurology]]") are not
    modelled; the extracted name may be prose, not a claimed section.
  * Citations where the section name PRECEDES the link are not detected at all.
    This is a known blind spot, reported in the summary as un-audited context.
  * A citation naming no section is counted as bare and skipped, not passed.
  * Links inside fenced code blocks are skipped, but inline-code links are not.

Usage
-----
  scripts/citation_audit.py                          # whole project, both directions
  scripts/citation_audit.py --range '04_*.md'        # outgoing + incoming for a range
  scripts/citation_audit.py --range 'Examination.md' --show-ok
  scripts/citation_audit.py --target 04_Neurology    # everything citing one file
  scripts/citation_audit.py --list-anchors 04_Neurology

Exit status: 0 = no broken candidates, 1 = broken candidates found, 2 = usage error.
"""

import argparse
import difflib
import glob
import os
import re
import sys
import unicodedata

META_FILES = {
    "CLAUDE.md", "CLAUDE_CODE_PROMPT.md", "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md", "PHASE_EXECUTION_WORKFLOW.md",
    "RECOMMENDED_WORKFLOW.md",
}

SIMILARITY = 0.86
MIN_NAME = 4          # a cited "name" shorter than this is treated as bare
MAX_NAME = 90

PUNCT = {"’": "'", "‘": "'", "“": '"', "”": '"',
         "–": "-", "—": "-", "‒": "-", "−": "-", "‐": "-", "‑": "-",
         " ": " ", " ": " "}

# Words/phrases that end a citation's section name.
STOP_PHRASES = [
    "not repeated here", "not repeated", "not duplicated here", "not duplicated",
    " for ", " given ", " see ", " and the ", " which ", " where ", " because ",
    " unless ", " rather than ", " instead of ", " as well as ", " covers ",
    " covered ", " has ", " have ", " includes ", " including ",
]

HEADER_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
BOLD_RE = re.compile(r"\*\*([^*\n]{3,90}?)\*\*")
CALLOUT_RE = re.compile(r"^>\s*\[![a-zA-Z]+\]\s*(.+?)\s*$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
LINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def fold(text):
    for a, b in PUNCT.items():
        text = text.replace(a, b)
    text = unicodedata.normalize("NFKC", text)
    text = "".join(c for c in unicodedata.normalize("NFD", text)
                   if not unicodedata.combining(c))
    text = text.lower().replace("'", "")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def content_files(root):
    return sorted(p for p in glob.glob(os.path.join(root, "*.md"))
                  if os.path.basename(p) not in META_FILES)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def anchors_of(text):
    """Every string a citation could legitimately be naming, with its kind."""
    out = []
    for m in HEADER_RE.finditer(text):
        out.append((m.group(1).strip(), "header"))
    for m in CALLOUT_RE.finditer(text):
        out.append((m.group(1).strip(), "callout"))
    for m in BOLD_RE.finditer(text):
        t = m.group(1).strip().rstrip(":").strip()
        if len(t) >= MIN_NAME:
            out.append((t, "bold"))
    seen, uniq = set(), []
    for name, kind in out:
        key = (fold(name), kind)
        if key not in seen:
            seen.add(key)
            uniq.append((name, kind))
    return uniq


def trim_name(raw):
    """Cut the text following a link into CANDIDATE cited section names.

    Returns a list, longest first. A single truncation rule cannot be right for
    every citation in this corpus: section names here legitimately contain em
    dashes and parentheses ("Abdominal Pain - Regional Anatomy and DDx",
    "Upper GI Bleed (UGIB)"), so cutting at those characters produces false
    BROKEN hits, while NOT cutting there lets a citation run on into unrelated
    prose. Generating progressively shorter candidates and accepting the first
    that matches an anchor handles both, and the accepted candidate is printed
    so the decision stays auditable.
    """
    name = raw
    # Hard terminators — these never appear inside a section name in this corpus.
    for ch in ["\n", ")", "]", ";", "|", "**"]:
        i = name.find(ch)
        if i != -1:
            name = name[:i]
    low = name.lower()
    for sp in STOP_PHRASES:
        i = low.find(sp)
        if i != -1:
            name = name[:i]
            low = name.lower()
    m = re.search(r"\.(\s|$)", name)
    if m:
        name = name[:m.start()]

    def tidy(t):
        return t.strip(" \t.,;:-–—'\"")

    cands = [tidy(name)]
    # Soft terminators — legitimate INSIDE a section name, so only ever offered
    # as an additional, shorter candidate.
    for cut in [",", " — ", " – ", " - ", "—", "–", ":", "("]:
        nxt = []
        for c in cands:
            i = c.find(cut)
            if i > 0:
                nxt.append(tidy(c[:i]))
        cands.extend(nxt)

    out, seen = [], set()
    for c in sorted(cands, key=len, reverse=True):
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def extract_citations(text):
    """Yield (target, cited_name_or_None, line_no, context)."""
    clean = FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    for m in LINK_RE.finditer(clean):
        target = m.group(1).strip()
        after = clean[m.end():m.end() + 160]
        cands = [c for c in trim_name(after)
                 if MIN_NAME <= len(c) <= MAX_NAME and c[0].isupper()]
        line = clean.count("\n", 0, m.start()) + 1
        ctx = clean[m.start():m.start() + 110].replace("\n", " ")
        yield target, cands, line, ctx


def match_anchor(name, anchors):
    """Return (anchor_text, kind, how) or None."""
    f = fold(name)
    if not f:
        return None
    folded = [(fold(a), a, k) for a, k in anchors]
    for fa, a, k in folded:
        if fa == f:
            return a, k, "exact"
    for fa, a, k in folded:
        if f and fa and (f in fa or fa in f):
            return a, k, "substring"
    # Ordered token-subset: every word of the cited name appears in the anchor,
    # in order. Catches legitimate abbreviated citations of a long header, e.g.
    # 'Discussing DNACPR' -> 'Discussing "Do Not Attempt Cardiopulmonary
    # Resuscitation" (DNACPR / Not-for-Resuscitation)'.
    ftoks = f.split()
    if len(ftoks) >= 2:
        for fa, a, k in folded:
            atoks = fa.split()
            i = 0
            for t in atoks:
                if i < len(ftoks) and t == ftoks[i]:
                    i += 1
            if i == len(ftoks):
                return a, k, "token-subset"

    pool = [fa for fa, _, _ in folded]
    near = difflib.get_close_matches(f, pool, n=1, cutoff=SIMILARITY)
    if near:
        for fa, a, k in folded:
            if fa == near[0]:
                ratio = difflib.SequenceMatcher(None, f, fa).ratio()
                return a, k, "similar %.2f" % ratio
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=None)
    ap.add_argument("--range", dest="rng", default=None,
                    help="glob of files under audit (default: whole project)")
    ap.add_argument("--target", default=None,
                    help="audit every citation pointing at this file (no .md)")
    ap.add_argument("--list-anchors", default=None,
                    help="print every citable anchor in a file and exit")
    ap.add_argument("--show-ok", action="store_true")
    args = ap.parse_args()

    root = args.dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = content_files(root)
    if not paths:
        sys.stderr.write("no content files in %s\n" % root)
        return 2

    texts = {os.path.basename(p)[:-3]: read(p) for p in paths}
    anchors = {k: anchors_of(v) for k, v in texts.items()}

    if args.list_anchors:
        key = args.list_anchors[:-3] if args.list_anchors.endswith(".md") else args.list_anchors
        if key not in anchors:
            sys.stderr.write("unknown file: %s\n" % key); return 2
        for name, kind in anchors[key]:
            print("%-9s %s" % (kind, name))
        return 0

    if args.rng:
        in_range = set(os.path.basename(p)[:-3]
                       for p in glob.glob(os.path.join(root, args.rng))
                       if os.path.basename(p) not in META_FILES)
    elif args.target:
        in_range = {args.target[:-3] if args.target.endswith(".md") else args.target}
    else:
        in_range = set(texts)

    unknown = in_range - set(texts)
    if unknown:
        sys.stderr.write("not content files: %s\n" % ", ".join(sorted(unknown)))
        return 2

    print("=" * 78)
    print(" citation_audit.py — Step 8 bidirectional cross-reference accuracy")
    print(" corpus: %d content files   |   range: %d file(s)" % (len(texts), len(in_range)))
    print("=" * 78)

    broken, ok, bare, offsite = [], [], 0, 0
    for src in sorted(texts):
        for target, cands, line, ctx in extract_citations(texts[src]):
            direction = None
            if src in in_range:
                direction = "OUT"
            if target in in_range:
                direction = "IN" if direction is None else "BOTH"
            if direction is None:
                continue
            if target not in anchors:
                offsite += 1          # unresolved target: check_structure.sh's job
                continue
            if not cands:
                bare += 1
                continue
            hit, used = None, cands[0]
            for c in cands:
                hit = match_anchor(c, anchors[target])
                if hit:
                    used = c
                    break
            rec = (src, line, target, used, hit, direction, ctx)
            (ok if hit else broken).append(rec)

    if args.show_ok and ok:
        print("\nRESOLVED (%d)" % len(ok))
        for src, line, target, name, hit, d, _ in sorted(ok):
            print("  [%-4s] %s:%d" % (d, src, line))
            print("         cites [[%s]] %r" % (target, name))
            print("         -> %s %r (%s)" % (hit[1], hit[0], hit[2]))

    print("\nBROKEN CANDIDATES (%d) — hand-verify each before editing" % len(broken))
    if not broken:
        print("  none")
    for src, line, target, name, _, d, ctx in sorted(broken):
        print("\n  [%-4s] %s:%d" % (d, src, line))
        print("         cites [[%s]] %r" % (target, name))
        print("         context: ...%s..." % ctx.strip())
        near = difflib.get_close_matches(fold(name),
                                         [fold(a) for a, _ in anchors[target]],
                                         n=3, cutoff=0.4)
        if near:
            print("         nearest anchors in %s.md:" % target)
            shown = set()
            for nf in near:
                for a, k in anchors[target]:
                    if fold(a) == nf and a not in shown:
                        shown.add(a)
                        print("           %-9s %s" % (k, a))
                        break
        else:
            print("         no similar anchor found in %s.md" % target)

    print("\n" + "-" * 78)
    print("citations checked : %d  (%d resolved, %d broken candidates)"
          % (len(ok) + len(broken), len(ok), len(broken)))
    print("bare links        : %d  (no section name written beside the link —" % bare)
    print("                       NOT audited, and NOT evidence of correctness)")
    print("off-range/unresolved targets skipped : %d" % offsite)
    print("BLIND SPOT: citations that name the section BEFORE the link are not")
    print("            detected by this scan at all. See LIMITATIONS in the header.")
    print("-" * 78)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
