#!/usr/bin/env python3
"""dose_tables.py — unit-and-progression check for banded dose tables.

The gap this fills
------------------
Every other scan in scripts/ checks a claim against something external: a
header, a checklist row, a citation target. This one checks a table against
**itself**. It asks whether a dose that varies by weight or age behaves
sensibly on its own terms *before* anyone opens a source:

  * does the dose move monotonically as the banding variable moves?
  * do all the bands share a unit, or does one jump scale?

It was written after the paediatric DKA find (2026-08-29), where maintenance
fluid read:

    <10kg — 4 mL/kg/h; 10–40kg — 2 mL/kg/h; >40kg — 4 mL/kg/h

The last band should be **40 mL/h as a fixed rate**, not 4 mL/kg/h — 200 mL/h
instead of 40 for a 50kg adolescent, in the one condition where fluid overload
drives cerebral oedema. No source was needed to see it: the rate *fell* with
weight and then *rose again*, which inverts the relationship every maintenance
formula has. Arithmetic alone convicted it.

RULE 4 DISCLOSURE — this detector's own blind spot, found and fixed
-------------------------------------------------------------------
The first version required the band and its dose on **separate lines**. The
DKA table is inline, three bands on one line — **so the first detector would
not have found the table that motivated it.** That is the exact failure
CLAUDE.md rule 4 describes, and it was fixed before any result was trusted.
The DKA line is fixture 1 below so the blind spot cannot silently return.

KNOWN LIMITATIONS — read before treating a hit as a defect
-----------------------------------------------------------
  * **NON-MONOTONIC is not a defect by itself.** Two different drugs on one
    line produce a false flag (benzylpenicillin 300/600/1200mg followed by
    cefotaxime 1000mg reads as a fall). So does any non-dose number in mg or
    mL — haemoglobin thresholds in g/L flagged this way.
  * **MIXED-UNITS is not a defect by itself.** A deliberate per-kg-to-absolute
    transition is correct paediatric practice: levothyroxine goes 8-10 mcg/kg
    (neonate) -> 5 mcg/kg (<2y) -> 50 mcg absolute (>2y). That is the same
    *shape* as the DKA error and is entirely right. The unit change is the
    thing to read, not the thing to report.
  * **Falling doses are sometimes correct** — weaning and tapering regimens,
    and per-kg doses that legitimately fall as weight rises. The check is
    whether the direction matches the clinical expectation, which is a
    judgement, not a rule.
  * Only banded tables are found. A single dose stated once has no
    progression to check and is invisible here.

Every hit needs reading. This script narrows 148 files to a handful of blocks;
it does not decide anything.

Usage
-----
  scripts/dose_tables.py               # corpus sweep
  scripts/dose_tables.py --self-test   # fixtures, incl. the DKA line
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

# A band: a weight or age qualifier. Covers "<10kg", "10-40kg", ">40kg",
# "10 to 40 kg", "<6mo", ">=12 years", "5-12y".
BAND_RE = re.compile(
    r"(?:[<>≤≥]\s*=?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?\s*(?:[-–—]|to)\s*\d+(?:\.\d+)?)"
    r"\s*(?:kg|g|mo|months?|y|yrs?|years?|weeks?|w)\b",
    re.I,
)
# A dose with its unit. /kg and /kg/h are captured so a scale change is visible.
DOSE_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(mcg|microgram|µg|mg|g|mL|ml|units?|IU)"
    r"((?:\s*/\s*kg)?(?:\s*/\s*(?:h|hr|hour|day|dose|min))?)",
    re.I,
)


def _unit(u, per):
    per = re.sub(r"\s+", "", per or "").lower()
    return (u.lower().replace("microgram", "mcg").replace("µg", "mcg")
            .replace("ml", "mL") + per)


def analyse(text):
    """Return (bands, doses) for one candidate block, or None if not banded."""
    bands = BAND_RE.findall(text)
    doses = [(float(m.group(1)), _unit(m.group(2), m.group(3)))
             for m in DOSE_RE.finditer(text)]
    if len(bands) < 2 or len(doses) < 2:
        return None
    return bands, doses


def flags(doses):
    out = []
    units = {u for _, u in doses}
    # A per-kg unit sitting beside an absolute one is the DKA/levothyroxine
    # shape: the scale of the number changes meaning between bands.
    perkg = {u for u in units if "/kg" in u}
    if perkg and perkg != units:
        out.append("MIXED-UNITS " + "|".join(sorted(units)))
    vals = [v for v, u in doses if u == doses[0][1]]
    if len(vals) >= 3 and vals != sorted(vals) and vals != sorted(vals, reverse=True):
        out.append("NON-MONOTONIC %s" % vals)
    return out


def scan(paths):
    rows = []
    for p in paths:
        for i, line in enumerate(open(p, encoding="utf-8").read().split("\n")):
            r = analyse(line)
            if r and flags(r[1]):
                rows.append((os.path.basename(p), i + 1, flags(r[1]), line.strip()))
            elif r:
                rows.append((os.path.basename(p), i + 1, [], line.strip()))
    return rows


FIXTURES = [
    # (text, must-flag substring or None, note)
    ("<10kg — 4 mL/kg/h; 10–40kg — 2 mL/kg/h; >40kg — 4 mL/kg/h",
     "NON-MONOTONIC", "THE DKA LINE — inline bands. The first detector missed this."),
    ("Neonates 8-10 mcg/kg/day; <2y 5 mcg/kg/day; >2y 50 mcg/day",
     "MIXED-UNITS", "levothyroxine — same shape as DKA and entirely correct; flag, then read"),
    ("20mg SC OD if <50kg; 40mg if 50–90kg; 60mg if 91–130kg; 80mg if 131–170kg",
     None, "enoxaparin — clean monotonic ladder, one unit, must NOT flag"),
    ("Give 500 mg PO TDS for 7 days",
     None, "single dose, no bands — nothing to check, must not appear at all"),
]


def self_test():
    print("SELF-TEST — inline fixtures\n")
    p = f = 0
    for text, expect, note in FIXTURES:
        r = analyse(text)
        got = flags(r[1]) if r else []
        if expect is None:
            ok = not got
        else:
            ok = any(expect in g for g in got)
        print("  %-4s %-28s :: %s" % ("ok" if ok else "FAIL", ";".join(got) or "-", note))
        p, f = p + ok, f + (not ok)
    print("\n  %d passed, %d failed" % (p, f))
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(1 if self_test() else 0)

    paths = [p for p in sorted(glob.glob("*.md")) if os.path.basename(p) not in META_FILES]
    rows = scan(paths)
    print("=" * 78)
    print(" dose_tables.py — %d files, %d banded dose blocks found" % (len(paths), len(rows)))
    print("=" * 78)
    for name, ln, fl, text in rows:
        print("\n%s:%d  %s" % (name[:52], ln, ";".join(fl) or "(no flag)"))
        print("   %s" % text[:150])
    print("\n" + "-" * 78)
    print("Neither flag is a defect by itself — see KNOWN LIMITATIONS. Read each.")
    print("-" * 78)


if __name__ == "__main__":
    main()
