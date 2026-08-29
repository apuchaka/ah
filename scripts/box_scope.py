#!/usr/bin/env python3
"""box_scope.py — verification boxes sitting above figures they never name.

The defect
----------
The partial-verification-box pattern, confirmed seven times: a box accurate
about the dimension it explicitly checked, and silent about content in its
scope that it did not name. The worst instances:

  * paediatric DKA — box verified the protocol structure; the fluid table
    beneath carried a five-fold unit error.
  * latent TB — box verified active-TB RIPE; the latent regimen beneath was
    the UK 3HR.
  * anti-D — box stated the corrected doses; a block eighteen lines below
    still carried the superseded ones.

This was recorded early as "explicitly not scannable", and that was too
strong. What is *not* scannable is whether a box's prose covers a claim.
What IS scannable is the cheap proxy below.

The proxy
---------
For each verification/localisation box, collect the numeric figures the box
itself names, then collect the figures in the block immediately beneath it.
Report any figure present beneath and absent above. A box that verifies doses
and sits above a different dose is exactly the shape that keeps failing.

KNOWN LIMITATIONS — this over-surfaces by design
------------------------------------------------
  * **A box need not name every figure it covers.** "Verified against ASCIA"
    legitimately covers a table it does not quote. Most hits are this. The
    output is a reading queue, not a defect list.
  * **Non-numeric claims are invisible.** The RCOG placenta accreta finding
    (a UK attribution under an Australian localisation heading) carries no
    uncovered figure and would not appear here.
  * **Only the block immediately beneath is examined** (to the next header or
    callout, max 14 lines). A defect further down the entry is missed — the
    anti-D case was 18 lines below and is at the edge of this window.
  * Figures are matched as literal strings, so "500 units" and "500units"
    match but "0.5g" and "500mg" do not.

RESULT OF THE FIRST FULL READ (2026-08-29) — read this before using it
----------------------------------------------------------------------
All 55 hits were read and **all 55 were dismissed as scope-legitimate.** Zero
genuine defects. The flagged figures were durations, intervals, ages and
thresholds sitting under boxes that name a guideline, a drug class or a
pathway rather than quoting each number — which is how a verification box
normally and correctly works.

**The proxy does not capture the defect.** Every genuine partial-verification-box
instance found this session turned on a NON-numeric claim:
  * a UK latent-TB regimen under a box verifying active-TB RIPE;
  * a UK screening position under a box verifying the screening *structure*;
  * a UK college attribution under a file-level "Localised for Australia";
  * adult hyperkalaemia doses under a box claiming *paediatric* validity —
    found by the CLAUDE.md rule 5 sweep, not by this script.

Keep it as a cheap re-runnable guard against the one shape it can see (a box
that quotes doses sitting above different doses), and do not read a clean run
as evidence the pattern is absent. The manual substitute is the only thing
that has ever worked: read what a box claims, then read what sits beneath it,
and ask what the box did NOT say.

Usage:  scripts/box_scope.py [--all]
Exit status: 0 always — this reports, it does not gate.
"""
import argparse, glob, io, os, re, sys

META_FILES = {"CLAUDE.md","CLAUDE_CODE_PROMPT.md","COWORK_HANDOFF.md",
 "MASTER_VERIFICATION_WORKFLOW.md","PENDING_GUIDELINE_CHECKS.md",
 "PHASE_EXECUTION_WORKFLOW.md","RECOMMENDED_WORKFLOW.md"}
BOX = re.compile(r">\s*\[!\w+\]")
# "Localis" alone matches "localising sign" — an explanatory box making no
# verification claim at all (04_Neurology Bell's palsy). Require the
# localisation *status* wording the corpus actually uses.
VERIFIED = re.compile(r"\bVerified\b|\bverified\b|Localis(?:ed|ation) (?:for|status)", re.I)
NUM = re.compile(r"\b\d+(?:\.\d+)?\s*(?:mg|mcg|g|mL|L|IU|units?|%|mmol|mmHg|"
                 r"g/L|mmol/L|hours?|h|days?|weeks?|months?|years?|min)\b", re.I)

def figures(lines):
    return {m.group(0).lower().replace(" ", "") for m in NUM.finditer(" ".join(lines))}

def scan(paths):
    out, total = [], 0
    for p in paths:
        L = io.open(p, encoding="utf-8").read().split("\n")
        for i, l in enumerate(L):
            if not (BOX.match(l) and VERIFIED.search(l)):
                continue
            total += 1
            j = i; box = []
            while j < len(L) and L[j].startswith(">"):
                box.append(L[j]); j += 1
            k = j; blk = []
            while k < len(L) and len(blk) < 14:
                if re.match(r"#{2,4}\s", L[k]) or (L[k].startswith(">") and BOX.match(L[k])):
                    break
                blk.append(L[k]); k += 1
            un = figures(blk) - figures(box)
            if un:
                out.append((os.path.basename(p), i + 1, sorted(un)))
    return out, total

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="list every uncovered figure, not the first four")
    a = ap.parse_args()
    paths = [p for p in sorted(glob.glob("*.md")) if os.path.basename(p) not in META_FILES]
    rows, total = scan(paths)
    print("=" * 78)
    print(" box_scope.py — %d verification boxes across %d files" % (total, len(paths)))
    print("=" * 78)
    print("\nBoxes sitting above a figure the box itself never names: %d\n" % len(rows))
    for f, ln, un in rows:
        print("   %s:%d" % (f[:48], ln))
        print("       uncovered: %s" % ", ".join(un if a.all else un[:4]))
    print("\n" + "-" * 78)
    print("A reading queue, not a defect list — most hits are legitimate.")
    print("See KNOWN LIMITATIONS: non-numeric claims are invisible to this.")
    print("-" * 78)

if __name__ == "__main__":
    main()
