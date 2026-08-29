# Project Rules — Grind Time Intern Exam Notes

## What this project is
Intern-level medical exam notes for Australian AMC-standard exams (MCQ 27 Sept 2026, OSCE 1 Nov, second MCQ 8 Nov). 148 content .md files, checklist.csv (872-row master topic checklist, 24 categories), **checklist_scales.csv** (Phase 5 — named clinical scales and reporting systems, with a verdict per system), and MASTER_VERIFICATION_WORKFLOW.md (the 26-step method and work queue). **All future work checks both CSVs.** A third, `checklist_external.csv`, was specified for Phase 5 Part A and **deliberately not created** — see the Phase 5 note in the workflow: the primary sources were egress-blocked and a snippet-and-recall baseline would have made a fabricated standard permanent.

Read MASTER_VERIFICATION_WORKFLOW.md before any work. Read checklist.csv with `encoding='utf-8-sig'` — plain utf-8 breaks the first column header.

## Target standard
Intern/RMO level. The test for any content: would a newly-graduated intern need this to recognise, explain, or act on something clinically? Not subspecialist depth. The workflow document's "Target standard" section has the full definition — follow it.

## Non-negotiable working rules

1. **Verify before writing any cross-reference.** Check the target file's exact header text first. Never write a plausible-sounding section name and assume it exists.

2. **Zero grep hits is not proof of absence.** Check case-sensitivity, Unicode characters (α, β, ₂ subscripts), hyphenation variants, **markdown emphasis inside a word**, and alternate medical terminology before concluding content is missing. Historically most "missing" results have been search artifacts.
   - **The markdown case specifically:** this corpus bolds acronym expansions letter by letter — `**H**aemolysis, **E**levated **L**iver enzymes, **L**ow **P**latelets`. A search for `Haemolysis` finds nothing, because the literal text is `**H**aemolysis`. **Whenever a search for an acronym expansion returns zero hits, search again for a distinctive letter-run from the middle of the word** (`aemolysis`) before concluding the expansion is absent. The construction most likely to be searched for is the one least likely to be found.
   - Also never conclude absence from **truncated** output: a hit that was returned and cut off by a `cut`/`head` limit looks identical to no hit at all. View the full line.

3. **Every automated scan produces false positives.** Verify each hit manually against actual file content before treating it as a gap. Report dismissed artifacts alongside confirmed gaps — the ratio is the main signal of whether the run was careful.

4. **Scans also produce false negatives.** A template-completeness scan keyed on the presence of an S/Smx line cannot detect entries that lack one entirely. Build scans defensively and assume blind spots exist. If you find one, fix the scan and re-run affected items before continuing.

5. **In any paediatric entry, treat every absolute quantity as suspect.** Confirmed four times (2026-08-29): DKA maintenance fluid, DKA dextrose rate, paediatric nephrotic proteinuria, and the adrenaline band that stopped at 7.5kg. For any `g`, `mg`, `mL`, `mL/h` or `g/24h` figure in a paediatric file, **ask what it does at 10kg and at 50kg.** The correct paediatric forms are per-kg, per-m², per-age-band, or per-kg with an absolute cap — the corpus does this well where it does it at all (`40mg/kg (≤2g)`, `60mg/m²/day (max 80mg)`, the ASCIA and ANZCOR bands). **The defect is always an absolute figure standing alone**, because a number that is right for an adult survives being copied — nothing about it looks wrong in isolation. This applies to every round, not only paediatric ones: adult files carry paediatric content too.

6. **One fix at a time, one commit each.** After each fix: confirm no duplicate headers introduced, confirm all cross-references resolve. Commit with a descriptive message before moving on. Never batch unverified edits.

7. **Stop and report if you discover a limitation in your own method mid-run.** Do not continue applying a scan you've realised is flawed. This is more important than completing the phase.

8. **Report honestly.** "Clean against everything currently known to check for" — never "verified complete." This project's history is that every completeness claim was later disproven by a new technique.

## Reporting format
For each queue item: what was checked · scan hits produced · genuine gaps vs dismissed artifacts (with reasons) · fixes made with commit hashes · any limitation noticed in the method itself.

## Content builds (Phase 2 of the queue) work differently
One topic per unit of work, not one category. Require a cited Australian source per topic (RACGP, Therapeutic Guidelines, state health guidelines, relevant college). Depth should match the existing notes, not be uniformly shallow.
