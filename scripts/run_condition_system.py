#!/usr/bin/env python3
"""Run condition_scan over one organ-system file and append to the CSV."""
import sys, os, csv, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import condition_scan as cs

FIELDS = ["system","condition","verdict","occurrences","first_location","scope_judgement"]
CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "checklist_external.csv")

def main(path, system):
    names = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
    corpus = cs.load()
    new = not os.path.exists(CSV)
    with open(CSV, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new: w.writeheader()
        counts, rows = cs.run(system, names, corpus, w)
    print(f"{system}: {len(names)} conditions ->", dict(counts))
    for v in ("ABSENT","MENTIONED"):
        sel = [r[1] for r in rows if r[2] == v]
        print(f"\n--- {v} ({len(sel)}) ---")
        print(" · ".join(sel))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
