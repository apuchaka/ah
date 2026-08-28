---
name: cowork-handoff
description: Complete setup and onboarding instructions for continuing the Grind Time intern exam notes project in Claude Cowork. Read this first, then MASTER_VERIFICATION_WORKFLOW.md.
---

# Cowork Handoff — Grind Time Intern Exam Notes

**Read this file first. Then read `MASTER_VERIFICATION_WORKFLOW.md` in full before doing any work.**

---

## Part A — What to transfer

Three things need to exist in the Cowork project folder:

1. **`MASTER_VERIFICATION_WORKFLOW.md`** (~72KB) — the complete method: 26 steps, the queue, confirmed-hits lists, false-positive patterns, per-group run estimates, and the reasoning behind the ordering. This is the single most important file.
2. **The 146 content `.md` files** (~2.9MB total) — the actual notes. Named `01_Cardiovascular.md` through `17_10_...`, plus the five cross-cutting files (`History-Taking.md`, `Examination.md`, `Investigation-Interpretation.md`, `Communication.md`, `Clinical-Process-EBM-Consent-Capacity.md`).
3. **`checklist.csv`** — the 872-row "Grind Time" master checklist, 24 categories. Every CSV-based step depends on this. Note the encoding quirk: **read it with `encoding='utf-8-sig'`**, not plain utf-8, or the first column header breaks.

**How to transfer**: download all 147 `.md` files plus the CSV from this chat's outputs, then upload them into a Cowork project folder. Keep the exact filenames — the entire `[[wikilink]]` cross-reference system (112 unique link targets) depends on filenames matching precisely.

---

## Part B — The opening prompt for the first Cowork session

> I'm continuing an existing project building intern-level medical exam notes for the Australian AMC-standard exams (MCQ Sept 27 2026, OSCE Nov 1, second MCQ Nov 8). All project files are in this folder: 146 content .md files, checklist.csv (the master topic checklist), and MASTER_VERIFICATION_WORKFLOW.md.
>
> Read MASTER_VERIFICATION_WORKFLOW.md in full first — it contains the complete 26-step verification method, a prioritised queue of remaining work, lists of already-confirmed findings (so you don't rediscover them), known false-positive patterns for several automated checks, and the target standard (intern/RMO level, explicitly not subspecialist depth).
>
> Then work through the queue starting at Phase 1, item P1. For each item: run the relevant steps, verify every automated-scan hit manually before treating it as a real gap, fix confirmed gaps, update the queue's status marker in MASTER_VERIFICATION_WORKFLOW.md, and report what you found.
>
> Critical working rules, all learned the hard way in the previous session:
> - Verify a cross-reference target's exact header text before writing the citation — don't assume a plausible-sounding section name exists.
> - Zero grep hits is not proof of absence. Check case-sensitivity, Unicode characters (α/β/₂ subscripts), hyphenation variants, and alternate medical terminology before concluding something is missing.
> - Every automated scan in the workflow produces real false positives. The document names the specific patterns for each — read them.
> - One fix at a time: verify no duplicate headers introduced, then save, then move on. Never batch unverified edits.
> - Match depth to the intern/RMO ceiling defined in the workflow document, not to how much detail is available on a topic.

---

## Part C — What Cowork can do that this chat couldn't

- **Run multiple queue items autonomously** in a single task, rather than needing a human `next` each round. This is the main reason to move.
- **Work directly on files on disk** rather than re-reading them into conversation context each round — which is what made the chat version increasingly token-expensive.
- **Maintain the queue state in the file itself** (status markers ⬜/🔶/✅), so progress survives across sessions rather than living in conversation memory.

---

## Part D — Project state as of handoff

**Completed**: 146 files built and localised from UK sources to Australian guidelines. Extensive verification across most organ-system categories. All files structurally clean (zero duplicate headers, all 112 wikilinks resolving, all files in sync).

**The queue's current state** (full detail in the workflow document):
- **Phase 1** — 6 categories that have never had a full exhaustive CSV-pull sweep: ENT, Immunology/Allergy/ID, Psychiatry & Mental Health, Paediatrics, Gynaecology & Breast, Ophthalmology (217 rows combined). **Start here.** This technique found every major gap in the project so far.
- **Phase 2** — confirmed unbuilt content: **Geriatrics (11 rows, 9 High-yield — essentially nothing exists)** and **GP/Preventive Med/Ethics/Communication (29 rows, roughly half genuinely absent)** are the two big ones, plus Injury/Poisoning, Public Health/Epidemiology, and Australian Context of Health.
- **Phase 3–4** — deep verification rounds on the 10 mega files, then large, then medium/small groups.

**Estimated remaining work**: roughly 245 rounds total at the depth this project has been running (Phase 1: 6 · Phase 2: ~30–38 · Phase 3–4: ~211). Treat this as a working estimate, not a guarantee — it's been revised several times as testing revealed more, and the workflow document explains why it shouldn't be trusted as final.

---

## Part E — The honest caveat to carry forward

This project's own history is that **every time the method was declared complete, a new technique found more**. Steps 17 through 24 in the workflow document each exist because an earlier "thorough" pass wasn't. The 26-step method is the best current version, not a proven-complete one.

Practical implication: when a category comes back clean, that means "clean against everything currently known to check for," not "verified perfect." Say it that way rather than overclaiming — the workflow document's final section ("What 'good' actually means") sets the reporting standard in detail.
