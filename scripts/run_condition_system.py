#!/usr/bin/env python3
"""Run condition_scan over one organ-system file and write it into the CSV.

IDEMPOTENT BY CONSTRUCTION. The first version appended. A stale background
run of the same system then landed after a foreground re-run and the CSV
silently carried 444 rows for 222 conditions - every neurology verdict
duplicated, with nothing in the file to show it. Appending is only safe if
nothing ever runs twice, which is not a property a scan can have. This
version reads the CSV, drops every existing row for the system being run,
and writes the file back, so re-running a system replaces its rows instead
of doubling them.
"""
import sys, os, csv, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import condition_scan as cs

FIELDS = ["system","condition","verdict","occurrences","first_location","scope_judgement"]
CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "checklist_external.csv")

def main(path, system):
    names = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
    corpus = cs.load()
    keep = []
    if os.path.exists(CSV):
        keep = [r for r in csv.DictReader(open(CSV, encoding="utf-8"))
                if r["system"] != system]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS); counts, rows = cs.run(system, names, corpus, w)
    with open(CSV, "w", newline="", encoding="utf-8") as fh:
        out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
        out.writerows(keep)
        fh.write(buf.getvalue())
    assert sum(1 for _ in csv.DictReader(open(CSV, encoding="utf-8"))) == len(keep) + len(names)
    print(f"{system}: {len(names)} conditions ->", dict(counts))
    for v in ("ABSENT","MENTIONED"):
        sel = [r[1] for r in rows if r[2] == v]
        print(f"\n--- {v} ({len(sel)}) ---")
        print(" · ".join(sel))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
