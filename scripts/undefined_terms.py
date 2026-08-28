#!/usr/bin/env python3
"""undefined_terms.py — surface terms the corpus USES often but never DEFINES.

The other four scans in this suite all start from the checklist: they ask whether
a CSV row is built. This one starts from the corpus itself and asks a different
question — **is there a term appearing repeatedly in procedural positions that no
entry ever explains?**

Why this exists
---------------
Six times in this project, content has been found that the corpus *referenced*
enough to look covered while never actually containing it:

  SNAP                  mentioned as a risk factor across many entries; the
                        framework itself had zero hits
  sensitivity/specificity   applied to eight named tests; never defined, and
                        PPV/NPV absent entirely
  documentation         instructed in ~a dozen entries ("document the refusal");
                        never specified anywhere
  "chaperone"           appeared 8x in Examination.md, every instance a
                        procedural line inside an examination sequence;
                        professional boundaries never taught
  "raise a safeguarding concern"   instructed in four entries; the conversation
                        never taught
  "refer to X"          instructed in 100+ entries; how to refer never taught

The first five were found by auditing a CSV row. The **"chaperone" case was found
by noticing that a word recurred and asking what it meant** — a different route
in, and one that does not depend on the checklist being complete. This script
makes that route mechanical instead of opportunistic.

What it does
------------
For each candidate term appearing more than --min-uses times across the content
files, it checks whether the corpus contains a **definitional site** for it:

  * a markdown header containing the term            (## Frailty)
  * a bold label containing the term                 (**Frailty**)
  * a callout/admonition line containing the term    (> [!info] Frailty is …)
  * a definitional line                              ("Frailty is a state of …",
    "D:" / "Definition:" lines, "X — a …", "X (also called …)")

A term used many times with **no definitional site anywhere** is a candidate for
the referenced-but-never-taught pattern.

KNOWN LIMITATIONS — read before treating a hit as a gap
-------------------------------------------------------
  * **This is a candidate generator, not a finding list.** Expect a high false
    positive rate by design — it is tuned to over-surface rather than miss.
  * Common clinical words that need no definition at intern level (patient, dose,
    pain, risk) are excluded by a stoplist, but the stoplist is incomplete and
    hand-maintained. Anything obviously general is noise.
  * A term may be adequately defined **in prose that this scan cannot recognise**
    as definitional. Read the hits before acting.
  * A term genuinely defined *outside* this corpus (a drug name, an anatomical
    term) will surface and is not a gap.
  * It only sees terms it looks for: multi-word phrases are matched literally,
    so a concept named inconsistently across the corpus can slip through — the
    same blind spot csv_crosscheck.py exists to handle for checklist rows.

Usage
-----
  scripts/undefined_terms.py                    # default sweep
  scripts/undefined_terms.py --min-uses 8
  scripts/undefined_terms.py --term "ISBAR"     # check one term
  scripts/undefined_terms.py --show-sites       # show why a term was dismissed

Exit status: 0 always — this reports, it does not gate.
"""

import argparse
import glob
import os
import re
import sys
from collections import Counter

META_FILES = {
    "CLAUDE.md", "CLAUDE_CODE_PROMPT.md", "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md", "PENDING_GUIDELINE_CHECKS.md",
    "PHASE_EXECUTION_WORKFLOW.md", "RECOMMENDED_WORKFLOW.md",
}

# Words that recur constantly and need no definition at intern level.
STOP = set("""
patient patients doctor doctors clinician clinicians nurse child children adult adults
dose doses dosing drug drugs medicine medicines medication medications treatment treat
pain risk risks care history examination assessment management diagnosis diagnostic
blood test tests result results level levels normal abnormal acute chronic severe mild
moderate cause causes symptom symptoms sign signs disease conditions condition therapy
first second third early late high low increased decreased common rare features
australian australia state national guideline guidelines evidence review referral refer
consider considered including include includes given specific particular general
""".split())

# Definitional patterns, checked against the whole corpus for each term.
def definitional_sites(term, files):
    """Return list of (filename, kind, line) where `term` looks defined."""
    t = re.escape(term)
    pats = [
        ("header",      re.compile(r"^#{1,6}[^\n]*\b%s\b" % t, re.I | re.M)),
        ("bold",        re.compile(r"\*\*[^*\n]{0,60}\b%s\b[^*\n]{0,60}\*\*" % t, re.I)),
        ("callout",     re.compile(r"^>\s*\[![a-z]+\][^\n]{0,80}\b%s\b" % t, re.I | re.M)),
        ("definition",  re.compile(r"\b%s\b\s*(?:\([^)]{0,60}\))?\s*(?:is|are|means|refers to|=)\s" % t, re.I)),
        ("D-line",      re.compile(r"\*\*D[:\s*]{1,4}\*{0,2}[^\n]{0,120}\b%s\b" % t, re.I)),
        ("gloss",       re.compile(r"\b%s\b\s*[—–-]\s*(?:a|an|the)\s" % t, re.I)),
    ]
    sites = []
    for f in files:
        for kind, rx in pats:
            m = rx.search(f["raw"])
            if m:
                line = f["raw"].count("\n", 0, m.start()) + 1
                sites.append((f["name"], kind, line))
                break
    return sites


def candidate_terms(files, min_uses):
    """Acronyms and capitalised multi-word phrases that recur across the corpus."""
    counts = Counter()
    acro = re.compile(r"\b([A-Z][A-Za-z]{1,6}(?:-[A-Z][A-Za-z]{1,6})?)\b")
    phrase = re.compile(r"\b((?:[a-z]+ ){0,2}(?:chaperone|observer|referral|handover|"
                        r"screening|safety[- ]net(?:ting)?|escalation|consent|capacity|"
                        r"debrief|audit|governance|stewardship|triage|formulation))\b", re.I)
    for f in files:
        text = f["raw"]
        for m in acro.finditer(text):
            w = m.group(1)
            if len(w) >= 3 and w.upper() == w and w.lower() not in STOP:
                counts[w] += 1
        for m in phrase.finditer(text):
            w = m.group(1).strip().lower()
            if w and w not in STOP and len(w.split()) <= 3:
                counts[w] += 1
    return {t: n for t, n in counts.items() if n >= min_uses}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=None)
    ap.add_argument("--min-uses", type=int, default=5)
    ap.add_argument("--term", default=None, help="check one specific term")
    ap.add_argument("--show-sites", action="store_true",
                    help="also list where defined terms were found (audit the dismissals)")
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    root = args.dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = []
    for p in sorted(glob.glob(os.path.join(root, "*.md"))):
        if os.path.basename(p) in META_FILES:
            continue
        with open(p, encoding="utf-8") as fh:
            files.append({"name": os.path.basename(p), "raw": fh.read()})
    if not files:
        sys.stderr.write("no content files found\n")
        return 0

    print("=" * 78)
    print(" undefined_terms.py — terms USED often but never DEFINED")
    print(" corpus: %d content files | threshold: >%d uses" % (len(files), args.min_uses))
    print("=" * 78)

    if args.term:
        terms = {args.term: sum(f["raw"].lower().count(args.term.lower()) for f in files)}
    else:
        terms = candidate_terms(files, args.min_uses)

    undefined, defined = [], []
    for t, n in sorted(terms.items(), key=lambda kv: -kv[1]):
        sites = definitional_sites(t, files)
        (defined if sites else undefined).append((t, n, sites))

    print("\nUNDEFINED CANDIDATES (%d) — used often, no definitional site found" % len(undefined))
    print("-" * 78)
    if not undefined:
        print("  none")
    for t, n, _ in undefined[:args.limit]:
        holders = sorted({f["name"] for f in files if re.search(r"\b%s\b" % re.escape(t), f["raw"], re.I)})
        print("  %-28s %4d uses across %2d files" % (t, n, len(holders)))
        print("      e.g. %s" % ", ".join(holders[:3]))

    print("\nDEFINED (%d) — dismissed, a definitional site exists" % len(defined))
    print("-" * 78)
    if args.show_sites:
        for t, n, sites in defined[:args.limit]:
            f, kind, line = sites[0]
            print("  %-28s %4d uses — %s at %s:%d" % (t, n, kind, f, line))
    else:
        print("  " + ", ".join(t for t, _, _ in defined[:60]))
        print("  (--show-sites to audit these dismissals)")

    print("\n" + "-" * 78)
    print("Every line above is a CANDIDATE. This scan over-surfaces by design and")
    print("has a high false-positive rate — read the term in context before acting.")
    print("The signal is a term used procedurally many times that no entry teaches.")
    print("-" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
