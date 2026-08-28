#!/usr/bin/env python3
"""completeness_scan.py — granular Ix/Mx and template completeness (Steps 2, 13)
plus the un-templated-entry blind-spot check.

Three scans, run together because each one's blind spot is another's coverage.

  CHECK A (Step 2)  — granular Ix/Mx completeness
      Sections are split at BOTH `##` and `###`. A `##`-only split hides gaps in
      `###` subsections sitting under a sibling that has its own Mx — this is
      exactly how Cauda Equina and Spinal Cord Compression stayed hidden for
      several rounds. Flags: has S/Smx, lacks Mx, and is substantial.

  CHECK B (Step 13) — template completeness
      Step 2 only fires when S/Smx is present AND Mx is absent. It cannot see an
      entry missing D or Ix outright. Flags: has S/Smx, lacks D and/or Ix.

  CHECK C (blind spot) — un-templated entries          *** THE POINT OF THIS ***
      Checks A and B are BOTH keyed on the presence of an S/Smx line. Neither
      can, even in principle, detect an entry that has no S/Smx line at all —
      a section can be long, substantive, and completely untemplated, and both
      scans will pass over it in silence. CLAUDE.md rule 4 names this directly.
      CHECK C is keyed on the opposite condition: any section longer than
      --min-lines (default 15) carrying NONE of the four markers (no D, no
      S/Smx, no Ix, no Mx). It is deliberately independent of the S/Smx line so
      that it cannot inherit A and B's blind spot.

Marker detection
----------------
Every marker regex accepts the BARE BOLD form with no colon (`**Mx**`) as well
as `**Mx:**` and `Mx:`. Some file ranges (Obstetrics/Gynaecology) use the bare
form throughout, and the plain `Mx[:\\s]` pattern misses those entries entirely.
Run --show-markers to print the exact patterns in use.

KNOWN LIMITATIONS — read before treating any hit as a gap
---------------------------------------------------------
  * Every hit is a CANDIDATE. Open the file. The documented false positives are
    real and common:
      - a sibling `###` subsection whose Mx sits just outside the split boundary
      - deliberately compressed reference-table entries
      - cross-reference stubs that legitimately skip most of the template
      - CHECK C fires on legitimately non-disease sections: reference tables,
        DDx charts, examination sequences, index/overview sections. These are
        NOT gaps. The signal in CHECK C is a DISEASE entry appearing in the list.
  * Sections whose first 400 chars say "not repeated here" / "not duplicated
    here" are skipped as deliberate cross-reference stubs. If that phrasing
    changes, the skip silently stops working — grep the corpus for new phrasings
    when adding content.
  * The cross-cutting files (History-Taking, Examination, Investigation-
    Interpretation, Communication, Clinical-Process) do NOT follow the
    D/S-Smx/Ix/Mx template, so A and B do not apply to them and they are
    excluded by default (--include-crosscutting to override). Per Step 2 they
    need a different check: every Hx/exam entry a COMPLETE systematic question
    or technique list, every investigation entry both the *why* and the *what*.
    That check is judgement-driven and is NOT automated here — this script
    cannot tell you those files are fine.

Usage
-----
  scripts/completeness_scan.py                          # whole corpus
  scripts/completeness_scan.py --files '04_*.md'
  scripts/completeness_scan.py --files '16_*.md' --check A
  scripts/completeness_scan.py --check C --min-lines 20
  scripts/completeness_scan.py --show-markers
  scripts/completeness_scan.py --summary

Exit status: 0 = no candidates, 1 = candidates found, 2 = usage error.
"""

import argparse
import glob
import os
import re
import sys

META_FILES = {
    "CLAUDE.md", "CLAUDE_CODE_PROMPT.md", "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md", "PHASE_EXECUTION_WORKFLOW.md",
    "RECOMMENDED_WORKFLOW.md",
}

CROSSCUTTING = {
    "History-Taking.md", "Examination.md", "Investigation-Interpretation.md",
    "Communication.md", "Clinical-Process-EBM-Consent-Capacity.md",
}

SKIP_PHRASES = ("not repeated here", "not duplicated here", "not repeated",
                "not duplicated", "see above", "covered above")
SKIP_WINDOW = 400

# Each marker accepts: **X:**  |  **X**  |  X:  — the bare bold form matters.
MARKERS = {
    "D": re.compile(
        r"\*\*\s*D\s*[:\s]*\*\*|\*\*\s*D\s*:|(?<![A-Za-z])D:\s|"
        r"\*\*\s*(?:Definition|Dx)\b|(?<![A-Za-z])Definition\s*:",
        re.IGNORECASE),
    "S/Smx": re.compile(
        r"S\s*/\s*S(?:mx|ymptoms)|\*\*\s*S(?:mx)?\s*[:\s]*\*\*|"
        r"(?<![A-Za-z])Smx\s*:|Features\s*:|Clinical features|"
        r"Signs?\s+and\s+symptoms|Presentation\s*:",
        re.IGNORECASE),
    "Ix": re.compile(
        r"\*\*\s*Ix\b[^*]{0,24}\*\*|\*\*\s*Ix\s*:|(?<![A-Za-z])Ix\s*[:\s]|"
        r"\*\*\s*Investigations?\b|(?<![A-Za-z])Investigations?\s*:",
        re.IGNORECASE),
    "Mx": re.compile(
        r"\*\*\s*Mx\b[^*]{0,24}\*\*|\*\*\s*Mx\s*:|(?<![A-Za-z])Mx\s*[:\s]|"
        r"\*\*\s*(?:Management|Treatment)\b|(?<![A-Za-z])Management\s*:|"
        r"(?<![A-Za-z])Treatment\s*:|treat(?:ed|ment|s)?\b|watch and wait|"
        r"self-resolv|supportive|reassur|resolves spontaneously|conservative",
        re.IGNORECASE),
}

HEAD_RE = re.compile(r"^(#{2,3}) ([^\n]+)$", re.MULTILINE)


def content_files(root, pattern, include_cc):
    out = []
    for p in sorted(glob.glob(os.path.join(root, pattern))):
        b = os.path.basename(p)
        if b in META_FILES:
            continue
        if b in CROSSCUTTING and not include_cc:
            continue
        out.append(p)
    return out


def sections(path):
    """Yield (title, level, own_text, full_text) for every `##` and `###` section.

    Two scopes, deliberately:

      own   text down to the NEXT header of any level (## or ###)
      full  text down to the next header of the SAME OR HIGHER level, i.e. a
            `##` section's full text includes all its `###` children

    A `##` parent is judged on `full`, a `###` child on `own`. This keeps both
    halves of the Step 2 requirement at once:

      * judging a `##` on `own` alone produces a false positive on every parent
        whose Mx lives in a `###` child (ACS, Tuberculosis, Crohn's all flagged
        this way on the first run of this script — none was a real gap);
      * judging only at `##` level hides a genuine gap inside a `###` sitting
        under a sibling that has its own Mx — how Cauda Equina and Spinal Cord
        Compression stayed hidden for rounds.

    Checking children independently on `own` preserves the second, while
    judging parents on `full` removes the first. Nothing is lost: every `###`
    is still examined in its own right.
    """
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    heads = [(m.start(), len(m.group(1)), m.group(2).strip())
             for m in HEAD_RE.finditer(content)]
    for i, (pos, level, title) in enumerate(heads):
        own_end = heads[i + 1][0] if i + 1 < len(heads) else len(content)
        full_end = len(content)
        for j in range(i + 1, len(heads)):
            if heads[j][1] <= level:
                full_end = heads[j][0]
                break
        own = content[pos:own_end]
        full = content[pos:full_end]
        if any(sp in full[:SKIP_WINDOW].lower() for sp in SKIP_PHRASES):
            continue
        yield title, level, own, full


def markers_in(sec):
    return {k: bool(rx.search(sec)) for k, rx in MARKERS.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=None)
    ap.add_argument("--files", default="*.md")
    ap.add_argument("--check", default="ABC", help="subset of A, B, C (default ABC)")
    ap.add_argument("--min-lines", type=int, default=15,
                    help="CHECK C: minimum section length in lines (default 15)")
    ap.add_argument("--min-chars", type=int, default=200,
                    help="CHECK A/B: minimum section length in chars (default 200)")
    ap.add_argument("--include-crosscutting", action="store_true")
    ap.add_argument("--summary", action="store_true", help="counts only")
    ap.add_argument("--show-markers", action="store_true")
    args = ap.parse_args()

    if args.show_markers:
        for k, rx in MARKERS.items():
            print("%-6s %s" % (k, rx.pattern))
        return 0

    root = args.dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = content_files(root, args.files, args.include_crosscutting)
    if not paths:
        sys.stderr.write("no content files matched %r in %s\n" % (args.files, root))
        return 2

    checks = args.check.upper()
    a_hits, b_hits, c_hits = [], [], []
    n_sections = 0

    for p in paths:
        name = os.path.basename(p)
        for title, level, own, full in sections(p):
            n_sections += 1
            # A `##` parent is judged including its `###` children; a `###` on
            # its own content. See the docstring in sections().
            scope = full if level == 2 else own
            mk = markers_in(scope)
            nlines = own.count("\n") + 1
            nchars = len(scope)
            tag = "##" if level == 2 else "###"

            if "A" in checks and mk["S/Smx"] and not mk["Mx"] and nchars > args.min_chars:
                a_hits.append((name, title, tag, nlines, mk))

            if "B" in checks and mk["S/Smx"] and not (mk["D"] and mk["Ix"]):
                missing = [k for k in ("D", "Ix") if not mk[k]]
                b_hits.append((name, title, tag, nlines, missing))

            if "C" in checks and nlines >= args.min_lines and not any(mk.values()):
                c_hits.append((name, title, tag, nlines, own))

    print("=" * 78)
    print(" completeness_scan.py")
    print(" files: %d   sections examined: %d   (cross-cutting %s)"
          % (len(paths), n_sections,
             "included" if args.include_crosscutting else "excluded"))
    print("=" * 78)

    if "A" in checks:
        print("\n" + "-" * 78)
        print("CHECK A (Step 2) — has S/Smx, NO Mx, >%d chars   [%d candidate(s)]"
              % (args.min_chars, len(a_hits)))
        print("-" * 78)
        if not a_hits:
            print("  none")
        elif not args.summary:
            for name, title, tag, nlines, mk in a_hits:
                present = ",".join(k for k in ("D", "S/Smx", "Ix", "Mx") if mk[k])
                print("  %s :: %s %s" % (name, tag, title))
                print("      %d lines | markers present: %s" % (nlines, present or "none"))

    if "B" in checks:
        print("\n" + "-" * 78)
        print("CHECK B (Step 13) — has S/Smx, missing D and/or Ix   [%d candidate(s)]"
              % len(b_hits))
        print("-" * 78)
        if not b_hits:
            print("  none")
        elif not args.summary:
            for name, title, tag, nlines, missing in b_hits:
                label = "%s :: %s %s" % (name, tag, title)
                print("  %-62s missing %s" % (label[:62], " and ".join(missing)))

    if "C" in checks:
        print("\n" + "-" * 78)
        print("CHECK C (blind spot) — >=%d lines, NO D / S-Smx / Ix / Mx marker at all"
              % args.min_lines)
        print("                       [%d candidate(s)]" % len(c_hits))
        print("-" * 78)
        print("  Checks A and B are both keyed on an S/Smx line and are STRUCTURALLY")
        print("  incapable of seeing these. Most hits are legitimately untemplated")
        print("  (reference tables, DDx charts, exam sequences, overviews) — the")
        print("  signal is a DISEASE entry appearing here.")
        if not c_hits:
            print("\n  none")
        elif not args.summary:
            print("")
            for name, title, tag, nlines, sec in c_hits:
                body = re.sub(r"\s+", " ", sec[len(title) + 4:]).strip()[:88]
                print("  %s :: %s %s" % (name, tag, title))
                print("      %d lines | opens: %s..." % (nlines, body))

    print("\n" + "-" * 78)
    print("TOTALS   CHECK A: %d   CHECK B: %d   CHECK C: %d"
          % (len(a_hits), len(b_hits), len(c_hits)))
    print("Every one is a CANDIDATE. Manually verify against the file before")
    print("treating it as a gap, and report dismissed artifacts alongside real")
    print("gaps — the ratio is the signal that the run was careful.")
    print("-" * 78)
    return 1 if (a_hits or b_hits or c_hits) else 0


if __name__ == "__main__":
    sys.exit(main())
