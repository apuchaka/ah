---
name: phase-execution-workflow
description: Phase-level execution setup for Claude Code, starting from a clean slate. Reduces ~80 batch prompts to ~8 phase prompts while keeping the self-interrupt safety mechanism. Includes the CLAUDE.md standing-rules file and each phase prompt.
---

# Phase-Level Execution — Full Setup (Clean Start)

Reduces the work from ~60–80 batch prompts down to **~8 phase prompts**.

**How it stays safe without manual batching**: the standing rules move into a `CLAUDE.md` file that Claude Code reads automatically, and each phase prompt carries a **self-interrupt clause** — stop and report on discovering a flaw in your own method, rather than continuing with a broken scan. That replaces human-imposed batching with automatic batching triggered by actual problems.

**This assumes a clean start** — no prior verification work exists in the repo. The 146 content files are as they were at handoff.

---

## STEP 0 — Repo setup

1. Get all files into the repo: 146 content `.md` files, `checklist.csv`, and the workflow documents (`MASTER_VERIFICATION_WORKFLOW.md`, `RECOMMENDED_WORKFLOW.md`, `COWORK_HANDOFF.md`, this file).
2. Confirm filenames are exactly intact — the cross-reference system depends on ~112 wikilink targets matching filenames precisely. A bad extraction (spaces converted, `(1)` suffixes) will produce a flood of false "broken link" reports.
3. Commit the baseline before any changes.

---

## STEP 1 — Create `CLAUDE.md` in the repo root

Read automatically by Claude Code, so these rules never need repeating in a prompt. Paste as file contents:

```markdown
# Project Rules — Grind Time Intern Exam Notes

## What this project is
Intern-level medical exam notes for Australian AMC-standard exams (MCQ 27 Sept 2026, OSCE 1 Nov, second MCQ 8 Nov). 146 content .md files, checklist.csv (872-row master topic checklist, 24 categories), and MASTER_VERIFICATION_WORKFLOW.md (the 26-step method and work queue).

Read MASTER_VERIFICATION_WORKFLOW.md before any work. Read checklist.csv with `encoding='utf-8-sig'` — plain utf-8 breaks the first column header.

## Target standard
Intern/RMO level. The test for any content: would a newly-graduated intern need this to recognise, explain, or act on something clinically? Not subspecialist depth. The workflow document's "Target standard" section has the full definition — follow it.

## Non-negotiable working rules

1. **Verify before writing any cross-reference.** Check the target file's exact header text first. Never write a plausible-sounding section name and assume it exists.

2. **Zero grep hits is not proof of absence.** Check case-sensitivity, Unicode characters (α, β, ₂ subscripts), hyphenation variants, and alternate medical terminology before concluding content is missing. Historically most "missing" results have been search artifacts.

3. **Every automated scan produces false positives.** Verify each hit manually against actual file content before treating it as a gap. Report dismissed artifacts alongside confirmed gaps — the ratio is the main signal of whether the run was careful.

4. **Scans also produce false negatives.** A template-completeness scan keyed on the presence of an S/Smx line cannot detect entries that lack one entirely. Build scans defensively and assume blind spots exist. If you find one, fix the scan and re-run affected items before continuing.

5. **One fix at a time, one commit each.** After each fix: confirm no duplicate headers introduced, confirm all cross-references resolve. Commit with a descriptive message before moving on. Never batch unverified edits.

6. **Stop and report if you discover a limitation in your own method mid-run.** Do not continue applying a scan you've realised is flawed. This is more important than completing the phase.

7. **Report honestly.** "Clean against everything currently known to check for" — never "verified complete." This project's history is that every completeness claim was later disproven by a new technique.

## Reporting format
For each queue item: what was checked · scan hits produced · genuine gaps vs dismissed artifacts (with reasons) · fixes made with commit hashes · any limitation noticed in the method itself.

## Content builds (Phase 2 of the queue) work differently
One topic per unit of work, not one category. Require a cited Australian source per topic (RACGP, Therapeutic Guidelines, state health guidelines, relevant college). Depth should match the existing notes, not be uniformly shallow.
```

---

## STEP 2 — Run the phases

Eight prompts, in order. Read each report before starting the next.

### Prompt A — Build and validate the tooling
> Read MASTER_VERIFICATION_WORKFLOW.md and CLAUDE.md in full.
>
> Convert the inline scan snippets in the workflow document into four saved, reusable scripts:
> - `check_structure.sh` — duplicate headers, wikilink resolution, file sync, file count (Steps 0, 1, final sweep)
> - `csv_crosscheck.py` — full category row pull + presence check. Must handle case-insensitive matching, Unicode characters (α, β, ₂ subscripts), and hyphenation variants.
> - `citation_audit.py` — bidirectional cross-reference accuracy (Step 8): does the named section in each `[[File]] Section Name` citation actually exist in the target?
> - `completeness_scan.py` — granular Ix/Mx and template completeness (Steps 2, 13). **Include a complementary check** flagging any entry over ~15 lines with no recognisable template markers at all (no D, S/Smx, Ix, or Mx) — a scan keyed only on S/Smx presence cannot see entries lacking one, which is a real blind spot.
>
> **Validate before trusting them**: run `csv_crosscheck.py` against the Neurology category. It must NOT flag Multiple Sclerosis, Trigeminal Neuralgia, or α-/β-thalassaemia as missing — all three exist and all three produce false positives with naive search patterns. If yours flags them, fix the script before proceeding.
>
> Then run `check_structure.sh` across all 146 files and report the baseline (expected: zero duplicate headers, ~112 wikilinks all resolving, 146 content files). Report anything unexpected before making any changes. Commit the scripts. Stop and report.

### Prompt B — Phase 1 (the full exhaustive CSV sweep)
> Run queue items P1–P6 (ENT, Immunology/Allergy/ID, Psychiatry & Mental Health, Paediatrics, Gynaecology & Breast, Ophthalmology) per CLAUDE.md, using the saved scripts.
>
> This is the highest-value phase — every major gap found in this project came from this exact technique. For each category: pull the full CSV row list, check presence, then verify depth (not just presence) for anything found, and verify genuine absence (not a search artifact) for anything missing. Fix confirmed gaps in place where the fix is contained; flag anything Geriatrics-sized as needing its own build round.
>
> Update queue status markers. Stop and report.

### Prompt C — Phase 2, the largest build
> Build queue item N1 (Geriatrics/Older Persons Health) per CLAUDE.md — 11 CSV topics, 9 High-yield, essentially nothing currently exists. **One topic per unit of work**, each with a cited Australian source. Check each topic against existing files first (e.g. cognitive screening tools already exist in Investigation-Interpretation.md — cross-reference, don't duplicate). Decide and state where content should live: new file(s) versus additions to existing files. Stop and report.

### Prompt D — Phase 2, second build
> Build queue item N6 (GP/Preventive Med/Ethics/Communication) per CLAUDE.md — 29 CSV rows, roughly half already covered. **Verify what exists before building**: breaking bad news, polypharmacy, end-of-life discussions, ICE, and SNAP were previously confirmed present. Confirmed absent: motivational interviewing/stages-of-change, giving/receiving handover, continuity of care, mandatory reporting as a general skill. Build only genuine gaps. Stop and report.

### Prompt E — Phase 2, remainder
> Build queue items N3 (Injury/Poisoning/Envenomation/Environmental — Shock is High-yield), N2 (Public Health/Epidemiology), N4 (Australian Context of Health), and run N5 (Clinical-Process-EBM-Consent-Capacity.md confirmation pass) per CLAUDE.md. Check existing coverage before building — several may be partially covered already. Stop and report.

### Prompt F — Phase 3, mega files
> Run queue items M1–M10 (04_Neurology, 01_Cardiovascular, 03_Gastrointestinal, 06_Metabolic_Medicine_and_Endocrinology, 07_Renal_Medicine_and_Urology, Examination.md, History-Taking.md, 02_Respiratory, 05_Ophthalmology, Investigation-Interpretation.md) per CLAUDE.md.
>
> These are the ten largest files in the project — apply the full step set, not a subset. This is a large phase; report progress at roughly M5 even if nothing is wrong, so the run doesn't go dark for its entire duration. Stop and report.

### Prompt G — Phase 4, large files
> Run queue items L1–L10 per CLAUDE.md, using the grouping table in MASTER_VERIFICATION_WORKFLOW.md for exact file lists. Stop and report.

### Prompt H — Phase 4, medium/small groups
> Run queue items G1–G39 per CLAUDE.md, using the grouping table in MASTER_VERIFICATION_WORKFLOW.md. This is the largest single phase — report progress at roughly G13 and G26 even if nothing is wrong. Per rule 6, stop immediately if you discover any method limitation rather than continuing. Stop and report.

---

## STEP 3 — Between phases

**Review by diff, not by reading files**: `git log --oneline` for the phase, then spot-check 3–5 diffs.

**Watch the artifact ratio.** "Found 14 hits, 11 artifacts, 3 real gaps fixed" is a run verifying properly. "Found 14 gaps, fixed 14" means it probably isn't — and that's the failure mode that damages good content. If you see the second pattern, say so before the next phase.

**After Phase 2 (Prompt E) and again after Phase 3 (Prompt F)**, do a deep review in a **fresh chat session** (not Claude Code): hand it MASTER_VERIFICATION_WORKFLOW.md, the most-modified files, and the git diff. Ask for the intern/RMO depth-ceiling audit (Step 18), readability check (Step 15), and a spot-audit of 5 sampled guideline citations (Step 22). These need judgment rather than pattern-matching, and a clean-context session does them better.

---

## What this trades away, honestly

Batching at 2–4 items exists so a systematic error surfaces after 3 items rather than 20. Phase-level running means an error could affect a whole phase before surfacing. Rule 6 (self-interrupt on discovering a method limitation) is the mitigation — and it's a real one, but not equivalent.

Prompt A exists specifically to reduce this risk: build and validate the tooling *before* any content work, against known false-positive cases, so the scans are trustworthy before they're applied at phase scale.

It's a genuine trade, not a free efficiency gain. Worth it for the ~10x prompt reduction — worth knowing you've made it.
