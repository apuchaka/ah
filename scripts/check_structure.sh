#!/usr/bin/env bash
# check_structure.sh — Structural integrity for the Grind Time intern exam notes.
#
# Covers MASTER_VERIFICATION_WORKFLOW.md:
#   Step 0  — setup / re-sync + naming-pattern (narrow-vs-broad glob) check
#   Step 1  — within-file duplicate headers, cross-file duplicate headers,
#             full wikilink resolution
#   Step 25 — final comprehensive sweep (same checks + total file count)
#
# Usage:
#   scripts/check_structure.sh                 # run from anywhere; repo root auto-detected
#   scripts/check_structure.sh --dir /path     # explicit notes directory
#   scripts/check_structure.sh --mirror DIR    # also diff every content file against DIR
#                                              #   (the original /mnt/user-data/outputs sync check)
#   scripts/check_structure.sh --quiet         # summary lines only, no detail listings
#
# Exit status: 0 = clean, 1 = something needs a human look, 2 = usage/setup error.
#
# ---------------------------------------------------------------------------
# KNOWN LIMITATIONS — read before trusting a clean result (CLAUDE.md rule 7)
#
#  * "Duplicate header" is checked on `## ` (headline metric, expected zero
#    within-file) and `### ` (reported separately as INFO — repeated `###`
#    subsection names inside one file are frequently legitimate).
#  * Cross-file `##` duplicates are EXPECTED (~13 known, already cross-referenced
#    pairs). This script prints the count and the list; a change in the list is
#    the signal, not the existence of duplicates.
#  * Wikilink resolution only proves the TARGET FILE exists. It says nothing
#    about whether the section named beside the link exists — that is
#    citation_audit.py (Step 8). A clean run here is not a clean run there.
#  * Links inside fenced code blocks are not excluded; a `[[Example]]` written
#    as documentation would be reported as unresolved. Verify each hit.
#  * The original Step 0 sync check compared against /mnt/user-data/outputs.
#    That path does not exist in the git-repo layout, so the default sync check
#    is "working tree vs git HEAD" (uncommitted/untracked content files).
#    Use --mirror to run the original directory-diff form.
# ---------------------------------------------------------------------------

set -uo pipefail

DIR=""
MIRROR=""
QUIET=0

while [ $# -gt 0 ]; do
  case "$1" in
    --dir)    DIR="${2:-}"; shift 2 ;;
    --mirror) MIRROR="${2:-}"; shift 2 ;;
    --quiet)  QUIET=1; shift ;;
    -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [ -z "$DIR" ]; then
  DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi
cd "$DIR" || { echo "cannot cd to $DIR" >&2; exit 2; }

# Meta/process files that are not exam content. Everything else matching *.md is content.
META_RE='^(CLAUDE|CLAUDE_CODE_PROMPT|COWORK_HANDOFF|MASTER_VERIFICATION_WORKFLOW|PENDING_GUIDELINE_CHECKS|PHASE_EXECUTION_WORKFLOW|RECOMMENDED_WORKFLOW)\.md$'
EXPECTED_CONTENT=148

mapfile -t CONTENT < <(ls -1 *.md 2>/dev/null | grep -vE "$META_RE" | sort)
if [ "${#CONTENT[@]}" -eq 0 ]; then
  echo "no .md files found in $DIR" >&2; exit 2
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

STATUS=0
flag() { STATUS=1; }
say()  { [ "$QUIET" -eq 1 ] || echo "$@"; }

echo "=========================================================="
echo " check_structure.sh — $(date '+%Y-%m-%d %H:%M:%S')"
echo " directory: $DIR"
echo "=========================================================="

# ---------------------------------------------------------------------------
# Step 0a — file counts
# ---------------------------------------------------------------------------
echo
echo "--- Step 0a: file count ---"
TOTAL_MD=$(ls -1 *.md 2>/dev/null | wc -l | tr -d ' ')
N_CONTENT=${#CONTENT[@]}
N_META=$((TOTAL_MD - N_CONTENT))
echo "total .md files      : $TOTAL_MD"
echo "meta/process files   : $N_META"
echo "content files        : $N_CONTENT (expected $EXPECTED_CONTENT)"
if [ "$N_CONTENT" -ne "$EXPECTED_CONTENT" ]; then
  echo "MISMATCH: content file count is $N_CONTENT, expected $EXPECTED_CONTENT."
  echo "          Either files were added/removed, or the META_RE list in this"
  echo "          script is stale. Resolve before trusting anything below."
  flag
else
  echo "OK"
fi

# ---------------------------------------------------------------------------
# Step 0b — naming-pattern check (narrow glob vs broad grep)
# A narrow glob like 14_*.md silently excluded 14a-*.md for many rounds.
# Run this every round, not once.
# ---------------------------------------------------------------------------
echo
echo "--- Step 0b: naming-pattern check (narrow glob vs broad prefix) ---"
NAMING_ISSUES=0
for prefix in $(printf '%s\n' "${CONTENT[@]}" | grep -oE '^[0-9]+' | sort -u); do
  narrow=$(ls -1 "${prefix}_"*.md 2>/dev/null | wc -l | tr -d ' ')
  broad=$(printf '%s\n' "${CONTENT[@]}" | grep -cE "^${prefix}[^0-9]" )
  if [ "$narrow" -ne "$broad" ]; then
    NAMING_ISSUES=$((NAMING_ISSUES+1))
    echo "prefix ${prefix}: narrow '${prefix}_*.md'=$narrow  broad '^${prefix}'=$broad  <-- DIFFER"
    echo "  broad-only files:"
    printf '%s\n' "${CONTENT[@]}" | grep -E "^${prefix}[^0-9]" | grep -v "^${prefix}_" | sed 's/^/    /' 
  fi
done
if [ "$NAMING_ISSUES" -eq 0 ]; then
  echo "OK — every numeric prefix's narrow glob matches its broad pattern"
else
  echo
  echo "WARN (standing property of this corpus, not a regression):"
  echo "  $NAMING_ISSUES prefix(es) differ. Any per-range work MUST use the broad"
  echo "  pattern, or the listed files are silently skipped. Known cases:"
  echo "    03a_Anaesthetics_Primer.md"
  echo "    14a-1_Psych_-_Substance_Misuse__Recreational_Drug_Profiles_.md"
  echo "    14a-2_Psych_-_Overdose_and_Poisoning_Management.md"
  echo "  A file listed above that is NOT one of these three is new — investigate."
  echo "  Not treated as a failure: it is permanent, and failing every run would"
  echo "  make the exit code meaningless."
fi

# ---------------------------------------------------------------------------
# Step 0c — sync check
# ---------------------------------------------------------------------------
echo
echo "--- Step 0c: sync check ---"
if [ -n "$MIRROR" ]; then
  if [ ! -d "$MIRROR" ]; then
    echo "mirror directory does not exist: $MIRROR"; flag
  else
    OUT=0
    for f in "${CONTENT[@]}"; do
      if [ ! -f "$MIRROR/$f" ]; then
        echo "$f: MISSING IN MIRROR"; OUT=$((OUT+1))
      elif ! diff -q "$f" "$MIRROR/$f" >/dev/null 2>&1; then
        echo "$f: OUTOFSYNC"; OUT=$((OUT+1))
      fi
    done
    for f in "$MIRROR"/*.md; do
      b="$(basename "$f")"
      [ -f "./$b" ] || { echo "$b: IN MIRROR ONLY"; OUT=$((OUT+1)); }
    done
    if [ "$OUT" -eq 0 ]; then echo "OK — all content files in sync with $MIRROR"
    else echo "$OUT file(s) out of sync with $MIRROR"; flag; fi
  fi
elif git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  DIRTY=$(git status --porcelain -- '*.md' | grep -vE "$(printf '%s' "$META_RE" | sed 's/[$^]//g')" || true)
  if [ -z "$DIRTY" ]; then
    echo "OK — no uncommitted changes to content files (working tree == HEAD)"
  else
    echo "uncommitted/untracked content files (this is expected mid-edit,"
    echo "but must be empty before reporting a round complete):"
    echo "$DIRTY" | sed 's/^/  /'
  fi
  echo "branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null)  HEAD: $(git rev-parse --short HEAD 2>/dev/null)"
else
  echo "SKIPPED — not a git repo and no --mirror given. Sync was NOT checked."
fi

# ---------------------------------------------------------------------------
# Step 1a — within-file duplicate headers
# ---------------------------------------------------------------------------
echo
echo "--- Step 1a: within-file duplicate '## ' headers (expected: zero) ---"
DUP2_FILES=0; DUP2_TOTAL=0
for f in "${CONTENT[@]}"; do
  dups=$(grep '^## ' "$f" | sed 's/[[:space:]]*$//' | sort | uniq -d)
  if [ -n "$dups" ]; then
    DUP2_FILES=$((DUP2_FILES+1))
    DUP2_TOTAL=$((DUP2_TOTAL + $(printf '%s\n' "$dups" | wc -l | tr -d ' ')))
    echo "$f:"; printf '%s\n' "$dups" | sed 's/^/    /'
  fi
done
if [ "$DUP2_FILES" -eq 0 ]; then echo "OK — 0 duplicate '## ' headers across $N_CONTENT files"
else echo "$DUP2_TOTAL duplicate '## ' header(s) in $DUP2_FILES file(s) — FIX THESE"; flag; fi

echo
echo "--- Step 1b: within-file duplicate '### ' headers (INFO, not a failure) ---"
echo "    Repeated '### ' names inside one file are often legitimate."
echo "    Listed so a NEW one is visible; verify each against the file."
DUP3_TOTAL=0
for f in "${CONTENT[@]}"; do
  dups=$(grep '^### ' "$f" | sed 's/[[:space:]]*$//' | sort | uniq -d)
  if [ -n "$dups" ]; then
    DUP3_TOTAL=$((DUP3_TOTAL + $(printf '%s\n' "$dups" | wc -l | tr -d ' ')))
    say "$f:"; say "$(printf '%s\n' "$dups" | sed 's/^/    /')"
  fi
done
echo "total repeated '### ' header names: $DUP3_TOTAL (informational)"

# ---------------------------------------------------------------------------
# Step 1c — cross-file duplicate headers
# ---------------------------------------------------------------------------
echo
echo "--- Step 1c: cross-file duplicate '## ' headers ---"
echo "    ~13 known, already cross-referenced pairs are EXPECTED."
echo "    Investigate anything not already known."
grep -h '^## ' "${CONTENT[@]}" | sed 's/^## //; s/[[:space:]]*$//' | sort | uniq -d > "$TMP/xdup.txt"
XDUP=$(wc -l < "$TMP/xdup.txt" | tr -d ' ')
echo "cross-file duplicate header names: $XDUP"
if [ "$XDUP" -gt 0 ] && [ "$QUIET" -eq 0 ]; then
  while IFS= read -r h; do
    echo "  \"$h\""
    grep -l "^## ${h}[[:space:]]*$" "${CONTENT[@]}" 2>/dev/null | sed 's/^/      /'
  done < "$TMP/xdup.txt"
fi

# ---------------------------------------------------------------------------
# Step 1c-bis — cross-file duplicates that Step 1c cannot see
#
# Added 2026-08-29 (G10-G17). Step 1c matches `^## ` exactly and
# case-sensitively, so it missed a full duplicate pair:
#
#   04_Neurology.md      ### Cauda Equina Syndrome
#   11_01_Ortho_...md    ### Cauda equina syndrome
#
# Two complete entries for one surgical emergency, in two files, neither
# pointing at the other — invisible on two counts at once: the header level
# (### not ##) and the letter case. CLAUDE.md rule 2 says to check
# case-sensitivity before concluding something is absent; that applies to the
# scans themselves, not only to manual greps.
# ---------------------------------------------------------------------------
echo
echo "--- Step 1c-bis: cross-file duplicate '##'/'###' headers, case-insensitive ---"
echo "    INFO. Catches pairs Step 1c misses on header level or letter case."
grep -h '^###\{0,1\} ' "${CONTENT[@]}" \
  | sed 's/^#\{2,3\} //; s/[[:space:]]*$//' \
  | tr '[:upper:]' '[:lower:]' | sort | uniq -d > "$TMP/xdup_ci.txt"
comm -13 <(sed 's/.*/\L&/' "$TMP/xdup.txt" | sort) "$TMP/xdup_ci.txt" > "$TMP/xdup_all.txt"
# Generic STRUCTURAL sub-headers repeat across files by design — every entry
# has a Management section. They are not topic duplicates and drown the signal.
grep -vxE 'management|complications|investigation|investigations|investigation and management|screening|causes|ix|mx|dx|prevention|prognosis|preparation|epidemiology|aetiology|pathophysiology|ddx by location|risk factors|examination|history|treatment|follow-up|referral' \
  "$TMP/xdup_all.txt" > "$TMP/xdup_new.txt" || true
XDUPCI=$(wc -l < "$TMP/xdup_new.txt" | tr -d ' ')
echo "additional TOPIC pairs not already reported by Step 1c: $XDUPCI"
echo "    (generic structural sub-headers such as Management/Complications filtered out)"
if [ "$XDUPCI" -gt 0 ] && [ "$QUIET" -eq 0 ]; then
  while IFS= read -r h; do
    echo "  \"$h\""
    grep -il "^#\{2,3\} ${h}[[:space:]]*$" "${CONTENT[@]}" 2>/dev/null | sed 's/^/      /'
  done < "$TMP/xdup_new.txt"
fi

# ---------------------------------------------------------------------------
# Step 1d — wikilink resolution
# ---------------------------------------------------------------------------
echo
echo "--- Step 1d: wikilink resolution ---"
printf '%s\n' "${CONTENT[@]}" | sed 's/\.md$//' | sort > "$TMP/files.txt"
# Strip any |alias, trim surrounding whitespace, drop #anchors from the target.
grep -oh '\[\[[^]]*\]\]' "${CONTENT[@]}" 2>/dev/null \
  | sed 's/^\[\[//; s/\]\]$//' > "$TMP/raw_links.txt"
TOTAL_LINKS=$(wc -l < "$TMP/raw_links.txt" | tr -d ' ')
sed 's/|.*$//; s/#.*$//; s/^[[:space:]]*//; s/[[:space:]]*$//' "$TMP/raw_links.txt" \
  | grep -v '^$' | sort -u > "$TMP/links.txt"
UNIQ_LINKS=$(wc -l < "$TMP/links.txt" | tr -d ' ')
comm -23 "$TMP/links.txt" "$TMP/files.txt" > "$TMP/unresolved.txt"
UNRESOLVED=$(wc -l < "$TMP/unresolved.txt" | tr -d ' ')

echo "total [[...]] occurrences in content files : $TOTAL_LINKS"
echo "unique link targets                        : $UNIQ_LINKS"
echo "unresolved targets                         : $UNRESOLVED"
if [ "$UNRESOLVED" -eq 0 ]; then
  echo "OK — every wikilink target resolves to an existing content file"
else
  echo "UNRESOLVED targets (and the files citing them):"
  while IFS= read -r link; do
    echo "  [[$link]]"
    grep -l -F "[[$link]]" "${CONTENT[@]}" 2>/dev/null | sed 's/^/      cited by: /'
  done < "$TMP/unresolved.txt"
  flag
fi

# Orphan check (Step 19 adjunct): content files nothing links to.
echo
echo "--- Step 1e: content files with zero incoming wikilinks (INFO) ---"
echo "    Step 19 adjunct — a file nothing points to may be undiscoverable."
ORPHANS=0
while IFS= read -r base; do
  if ! grep -q -F "[[$base]]" "${CONTENT[@]}" 2>/dev/null; then
    ORPHANS=$((ORPHANS+1)); say "  $base.md"
  fi
done < "$TMP/files.txt"
echo "files with no incoming wikilink: $ORPHANS (informational)"

# ---------------------------------------------------------------------------
echo
echo "=========================================================="
if [ "$STATUS" -eq 0 ]; then
  echo " RESULT: clean against everything this script checks for."
  echo " That is not the same as verified complete — see KNOWN"
  echo " LIMITATIONS in the header, and run the Python scans."
else
  echo " RESULT: issues found above. Resolve before proceeding."
fi
echo "=========================================================="
exit "$STATUS"
