---
name: claude-code-prompt
description: The exact prompt to paste into Claude Code to set up and run the Grind Time intern exam notes project. Includes setup instructions, working rules, and the per-batch prompt to reuse thereafter.
---

# Claude Code — Prompts

Two prompts below. **Prompt 1** is the one-time setup, used once. **Prompt 2** is what you reuse for every batch of work after that.

---

## PROMPT 1 — First session (setup + validation + first batch)

Paste this whole block:

---

I'm continuing an existing project: building intern-level medical exam notes for Australian AMC-standard exams (MCQ 27 Sept 2026, OSCE 1 Nov, second MCQ 8 Nov). Everything is in this folder.

**Read these three files in full before doing anything else:**
1. `MASTER_VERIFICATION_WORKFLOW.md` — the complete 26-step verification method, the prioritised work queue, lists of already-confirmed findings (so you don't rediscover them), documented false-positive patterns for each automated check, and the target standard.
2. `RECOMMENDED_WORKFLOW.md` — how this work should be structured and why.
3. `COWORK_HANDOFF.md` — project state and context.

Also present: 146 content `.md` files (the notes themselves) and `checklist.csv` (872-row master topic checklist, 24 categories). **Read the CSV with `encoding='utf-8-sig'`** — plain utf-8 breaks the first column header.

### Step 1 — Set up version control

`git init` if needed, then commit all current files as a baseline before making any changes. From here on, commit each individual fix as its own commit with a descriptive message. This matters: it's what makes your changes reviewable and individually revertable.

### Step 2 — Build the scan scripts

Convert the inline scan snippets scattered through `MASTER_VERIFICATION_WORKFLOW.md` into four saved, reusable scripts:

- `check_structure.sh` — duplicate headers, wikilink resolution, file sync, file count (Steps 0, 1, final sweep)
- `csv_crosscheck.py` — full category row pull + presence check. **Must handle: case-insensitive matching, Unicode characters (α, β, ₂ subscripts), and hyphenation variants.** These three specifically have caused false "missing content" results before.
- `citation_audit.py` — bidirectional cross-reference accuracy (Step 8): does the *named section* in each `[[File]] Section Name` citation actually exist in the target file?
- `completeness_scan.py` — granular Ix/Mx and template completeness scans (Steps 2, 13)

Each script should print its own known false-positive patterns (documented per-step in the workflow file) alongside its results, as a reminder not to trust raw output.

### Step 3 — Validate the scripts before trusting them

Run `csv_crosscheck.py` against the Neurology category. It must **not** flag Multiple Sclerosis, Trigeminal Neuralgia, or α-/β-thalassaemia as missing — all three are present and all three produced false positives with naive search patterns previously. If your script flags any of them, it has the same bug; fix it before proceeding.

Run `check_structure.sh` across all 146 files. Expected baseline: zero duplicate headers, all wikilinks resolving (~112 unique targets), 146 content files. Anything else is a pre-existing issue worth reporting before you start changing things.

### Step 4 — Run the first batch

Work queue items **P1, P2, and P3 only** (ENT, Immunology/Allergy/ID, Psychiatry & Mental Health), then stop and report. Do not continue past P3 in this session.

### Working rules — all learned the hard way, please follow them

- **Verify before writing any cross-reference.** Check the target file's exact header text first. Don't write a plausible-sounding section name and assume it exists — this produced three separate errors previously.
- **Zero grep hits is not proof of absence.** Check case-sensitivity, Unicode characters, hyphenation variants, and alternate medical terminology before concluding content is missing. Most "missing" results have historically been search artifacts, not real gaps.
- **Every automated scan produces real false positives.** Verify each hit manually against actual file content before treating it as a gap. A report saying "found 14 hits, 11 were artifacts, fixed 3" is more trustworthy than "found 14 gaps, fixed 14."
- **One fix at a time.** After each: confirm no duplicate headers introduced, confirm cross-references resolve, commit, then move on. Never batch unverified edits.
- **Match depth to the intern/RMO ceiling** defined in the workflow document — the test is whether a newly-graduated intern would need this to recognise, explain, or act on something. Not subspecialist depth.
- **Report honestly.** "Clean against everything currently known to check for" — not "verified complete." This project's history is that every completeness claim was later disproven by a new technique.

### What to report back

For each queue item: what you checked, what hits the scans produced, which were genuine gaps versus dismissed artifacts (with reasons), what you fixed, and the commit hashes. Then update the queue status markers in `MASTER_VERIFICATION_WORKFLOW.md`.

---

## PROMPT 2 — Every batch after the first

Reuse this, changing only the item numbers:

---

Run queue items **[P4, P5, P6]** from `MASTER_VERIFICATION_WORKFLOW.md`, then stop and report.

Use the saved scripts rather than retyping scans. Verify every scan hit manually before treating it as a real gap — the documented false-positive patterns still apply. Fix confirmed gaps, verify each fix (no duplicate headers, all cross-references resolve against actual header text), commit each fix separately, and update the queue status markers.

Report: what you checked, hits produced, genuine gaps versus dismissed artifacts with reasons, fixes made, commit hashes.

---

## Notes on using these

**Batch size**: 2–4 items per run. Large enough for real efficiency, small enough that a systematic error gets caught after 3 items rather than 20.

**Content builds are different.** When you reach Phase 2 of the queue (Geriatrics, GP/Ethics/Communication, etc.), switch to **one topic per run, not one category per run**. Geriatrics has 11 topics; building all 11 in one autonomous run produces uniform, shallow output rather than the depth the rest of the project has. Also require a cited Australian source (RACGP, Therapeutic Guidelines, state health guidelines, relevant college) per topic.

**Every 10–15 items**, do a deep review in a **fresh chat session** (not Claude Code) — hand it the workflow document, the most-modified files, and the git diff, and ask specifically for the intern/RMO depth-ceiling audit (Step 18), readability check (Step 15), and a spot-audit of 5 sampled guideline citations (Step 22). These need judgment rather than pattern-matching, and a clean-context session does them better.
