#!/usr/bin/env python3
"""export_obsidian.py — the tracker as an Obsidian vault folder.

Same data and same logic as `export_checks.py`, which it imports rather than
reimplements: one open tracker row is one task, routed to the same 26 source
groups, flagged dose-or-threshold by the same test. If the routing changes
there, it changes here.

Shape
-----
  Guideline_Checks_Index.md   links every source file, priority order
  <Source>.md                 one file per source group

Each row is a native task checkbox so Obsidian's task tracking, Tasks queries
and Dataview all see it:

  - [ ] **B24** — row text… #dose-threshold #src/racgp

THE MULTI-SOURCE PROBLEM, AND HOW IT IS SOLVED
-----------------------------------------------
15 of the 64 rows name more than one source that could settle them. The HTML
export lists such a row under every source, which is right for reading (79
cards from 64 rows) and **wrong for task tracking**: two checkboxes for one
piece of work double-counts, and ticking one leaves the other stale.

So each row gets exactly **one canonical checkbox**, in its highest-priority
source file. Every other source that could settle it carries a **non-task
pointer line** naming the row and linking to the file that owns it:

  → **B43** also settles from here — tracked in [[ASCIA]]

Consequences worth knowing:
  * Ticking a box is unambiguous; the total of all checkboxes is exactly 64.
  * A row is still discoverable from every source it belongs to.
  * Tags live on the canonical checkbox only, so a tag search returns each row
    once. The pointer lines are deliberately untagged.

Usage
-----
  scripts/export_obsidian.py                 # writes ./obsidian_export/
  scripts/export_obsidian.py --out DIR
"""

import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import export_checks as E  # noqa: E402  — shared routing/flagging, single source of truth


def slug_file(name):
    """Source name -> Obsidian filename stem. 'RACGP — Red Book / HANDI' -> RACGP_Red_Book_HANDI"""
    s = name.replace("—", " ").replace("/", " ").replace("'", "")
    s = re.sub(r"[^\w\s-]", " ", s)
    return re.sub(r"\s+", "_", s.strip())


def slug_tag(name):
    """Source name -> nested tag leaf. 'RCH Melbourne / Qld Children's' -> rch-melbourne-qld-childrens"""
    s = name.lower().replace("—", " ").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def clean(t):
    """Tracker markdown -> a single-line task body. Bold and code survive; pipes do not."""
    t = t.replace("|", "·").strip()
    return re.sub(r"\s+", " ", t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="obsidian_export")
    args = ap.parse_args()

    rows = E.load_rows()
    groups = E.group_rows(rows)
    order = E.priority_order(groups)          # same order the HTML export uses
    rank = {name: i for i, name in enumerate(order)}

    # canonical owner = the row's highest-priority source
    owner = {}
    for r in rows:
        owner[r["id"]] = min(r["src"], key=lambda s: rank[s])

    os.makedirs(args.out, exist_ok=True)
    written, tasks, pointers = [], 0, 0

    for name in order:
        rs = groups[name]
        mine = [r for r in rs if owner[r["id"]] == name]
        elsewhere = [r for r in rs if owner[r["id"]] != name]
        hi = sum(1 for r in mine if r["hi"])
        stem = slug_file(name)
        tag = slug_tag(name)

        L = []
        L.append("---")
        L.append("source: \"%s\"" % name.replace('"', "'"))
        L.append("tasks_here: %d" % len(mine))
        L.append("dose_or_threshold: %d" % hi)
        L.append("also_relevant: %d" % len(elsewhere))
        L.append("tags:")
        L.append("  - guideline-check")
        L.append("  - src/%s" % tag)
        L.append("---")
        L.append("")
        L.append("# %s" % name)
        L.append("")
        L.append("%d open check%s owned here%s. Back to [[Guideline_Checks_Index]]."
                 % (len(mine), "" if len(mine) == 1 else "s",
                    ", **%d touching a dose or threshold**" % hi if hi else ""))
        L.append("")
        for r in sorted(mine, key=lambda r: (not r["hi"], r["id"])):
            t = "#dose-threshold" if r["hi"] else "#provenance"
            L.append("- [ ] **%s** — %s %s #src/%s" % (r["id"], clean(r["body"]), t, tag))
            L.append("      *Files:* %s" % clean(r["files"]))
            L.append("")
            tasks += 1
        if elsewhere:
            L.append("## Also settles from this source")
            L.append("")
            L.append("*Tracked elsewhere so one row is one checkbox — tick it there, not here.*")
            L.append("")
            for r in sorted(elsewhere, key=lambda r: r["id"]):
                L.append("→ **%s** — tracked in [[%s]]" % (r["id"], slug_file(owner[r["id"]])))
                pointers += 1
            L.append("")
        io.open(os.path.join(args.out, stem + ".md"), "w", encoding="utf-8").write("\n".join(L))
        written.append((name, stem, len(mine), hi, len(elsewhere)))

    # index
    nhi = sum(1 for r in rows if r["hi"])
    I = ["---", "tags:", "  - guideline-check", "  - moc", "---", "",
         "# Guideline Checks — Index", "",
         "%d open rows from `PENDING_GUIDELINE_CHECKS.md`, grouped by the Australian "
         "primary source that settles each one. **%d touch a dose or threshold** "
         "(`#dose-threshold`); the rest are provenance checks (`#provenance`)." % (len(rows), nhi),
         "",
         "Each row has **one** checkbox, in its highest-priority source file, so the "
         "checkboxes across this folder total exactly %d. Where a row could also be settled "
         "from another source, that file carries a pointer to the file that owns it." % len(rows),
         "",
         "## Useful searches", "",
         "- `tag:#dose-threshold` — everything that changes what a patient receives",
         "- `tag:#provenance` — sourcing checks where the content is likely right",
         "- `tag:#src/rch-melbourne-qld-childrens` — one source group, wherever its rows sit",
         "- Obsidian Tasks: ``` tasks / not done / tags include #dose-threshold ```",
         "",
         "## Sources", "",
         "| Source | Checks | Dose/threshold | Also relevant |",
         "|---|---|---|---|"]
    for name, stem, n, hi, el in written:
        I.append("| [[%s\\|%s]] | %d | %s | %s |"
                 % (stem, name, n, hi if hi else "—", el if el else "—"))
    I += ["", "---", "",
          "Regenerate with `python3 scripts/export_obsidian.py` after editing the tracker. "
          "The tracker is the source of truth; ticking a box here does not write back to it."]
    io.open(os.path.join(args.out, "Guideline_Checks_Index.md"), "w", encoding="utf-8").write("\n".join(I))

    print("wrote %d files to %s/" % (len(written) + 1, args.out))
    print("  %d task checkboxes (one per open row: %d)" % (tasks, len(rows)))
    print("  %d cross-source pointer lines" % pointers)
    print("  %d dose-or-threshold, %d provenance" % (nhi, len(rows) - nhi))
    if tasks != len(rows):
        print("  WARNING: checkbox count %d != row count %d" % (tasks, len(rows)))


if __name__ == "__main__":
    main()
