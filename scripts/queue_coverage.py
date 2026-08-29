#!/usr/bin/env python3
"""queue_coverage.py — reconcile the corpus on disk against the queue.

Why this exists
---------------
On 2026-08-29, resuming G1–G39, **nine content files were found to be named
nowhere in MASTER_VERIFICATION_WORKFLOW.md** — no queue row, no grouping-table
entry, no prose. The M-tier is by definition the ten largest files and reached
none of them; G1–G39 skipped 08_01–08_06 and 08_09–08_10, 10_11a, 10_12, and
11_02. Two of them (43 KB and 42 KB) are larger than most files the queue does
cover.

**Every prior completeness claim about the queue was made by reading the
queue.** That cannot find a file the queue never mentions. This script starts
from the filesystem instead and subtracts, which is the only direction that
can see an omission.

It is the same lesson as `undefined_terms.py` (start from the corpus, not the
checklist) applied to the queue itself, and the same shape as N7, which was
"structurally unreachable from the queue until you added it."

What it reports
---------------
  UNQUEUED   a content file matched by no P/N/M/L/G queue row. This is the
             defect class. The M-tier is resolved by size, not by name, so
             the ten largest files are treated as covered by M1-M10.
  BY-TOPIC   reachable only through a row that names a TOPIC, not a filename
             (N1 "Geriatrics build" -> 18_...). Reachable, but through a
             *build* row rather than a verify row, so the file has never had
             a file-level audit pass. Listed, never silently cleared: naming
             by topic instead of filename is exactly how the nine hid.
  UNNAMED    a content file whose name appears nowhere in the document at all,
             queue row or prose. A subset of UNQUEUED, and the worse case.
  GHOST      a filename the queue names that does not exist on disk.

KNOWN LIMITATIONS
-----------------
  * **A file being in a queue row does not mean it was audited** — only that
    it is reachable. This checks addressability, nothing else.
  * Status markers are not read. A row with no tick still counts as covered.
  * Only `.md` files in the repo root are treated as corpus.

Usage:  scripts/queue_coverage.py        Exit 1 if anything is UNQUEUED.
"""

import glob
import os
import re
import sys

META_FILES = {
    "CLAUDE.md", "CLAUDE_CODE_PROMPT.md", "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md", "PENDING_GUIDELINE_CHECKS.md",
    "PHASE_EXECUTION_WORKFLOW.md", "RECOMMENDED_WORKFLOW.md",
}
WF = "MASTER_VERIFICATION_WORKFLOW.md"

# Hand-maintained. Every entry here is a file the automated check CANNOT see
# and a human has vouched for, so every entry weakens this script. Keep it
# short, and prefer fixing the queue row to naming the file.
# Deliberately EMPTY. The two files that would have gone here (18_, 19_ —
# reachable only through the topic-named build rows N1 and N6) were given real
# verify rows G44/G45 instead. Fixing the queue beats vouching for it.
BY_TOPIC = {}


def main():
    files = sorted(os.path.basename(p)[:-3] for p in glob.glob("*.md")
                   if os.path.basename(p) not in META_FILES)
    doc = open(WF, encoding="utf-8").read()
    rows = [l for l in doc.split("\n")
            if re.match(r"\|\s*(P\d+|N\d+|M\d+|L\d+|G\d+)\s*\|", l.strip())]
    queue = " ".join(rows)

    # The M-tier is defined by size, not by name; honour that definition.
    largest = {os.path.basename(p)[:-3] for p in
               sorted((p for p in glob.glob("*.md")
                       if os.path.basename(p) not in META_FILES),
                      key=os.path.getsize, reverse=True)[:10]}

    unqueued = [f for f in files if f not in queue and f not in largest
                and f not in BY_TOPIC]
    by_topic = [f for f in files if f in BY_TOPIC and f not in queue]
    unnamed = [f for f in files if f not in doc]
    # Strip fenced blocks and inline code first: the document quotes script
    # source, and "filepath.replace('.md'" was being read as a filename.
    prose = re.sub(r"`[^`]*`", " ", re.sub(r"```.*?```", " ", doc, flags=re.S))
    ghosts = sorted({m[:-3].lstrip("(`'\"") for m in
                     re.findall(r"[\w\-'’,\.\(\)]+\.md", prose)}
                    - set(files) - {m[:-3] for m in META_FILES})

    print("=" * 74)
    print(" queue_coverage.py — %d content files on disk, %d queue rows"
          % (len(files), len(rows)))
    print("=" * 74)
    for label, items in (("UNQUEUED — in no P/N/M/L/G row", unqueued),
                         ("UNNAMED  — absent from the document entirely", unnamed),
                         ("BY-TOPIC — reachable only via a topic-named build row", by_topic),
                         ("GHOST    — named by the queue, absent from disk", ghosts)):
        print("\n%s: %d" % (label, len(items)))
        for i in items:
            size = ("%.0f KB" % (os.path.getsize(i + ".md") / 1024)
                    if os.path.exists(i + ".md") else "missing")
            note = BY_TOPIC.get(i)
            print("   %s (%s)%s" % (i, size, " -> " + note if note else ""))
    print("\n" + "-" * 74)
    print("Covered here means ADDRESSABLE, not audited. See KNOWN LIMITATIONS.")
    print("-" * 74)
    return 1 if unqueued else 0


if __name__ == "__main__":
    sys.exit(main())
