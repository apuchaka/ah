# Pending Guideline Checks — running tracker

Collection point for **Step 14** (guideline-currency tracking) and **Step 20**
(source-currency spot-audit) of `MASTER_VERIFICATION_WORKFLOW.md`.

Both steps exist because the notes cite guidelines that were current when they
were written, and some were explicitly flagged as pending, in draft, or
jurisdiction-variable. Without somewhere to accumulate, those flags get
mentioned in a round's report and then lost. This file is that somewhere.

**Exam dates:** MCQ 27 Sept 2026 · OSCE 1 Nov 2026 · second MCQ 8 Nov 2026.
Re-check everything in Section A before the first date.

**How to use it**
- Append a row whenever a round finds a guideline flagged pending, in draft,
  jurisdiction-variable, or "check current" — file, line, what to re-check.
- Do not delete rows when resolved. Mark them, with the date and what changed.
  A resolved row is the record that the check was actually done.
- Regenerate the raw hit lists with the Step 14 / Step 20 greps in Section C.

---

## Section A — Explicitly pending or awaiting release

Highest priority: these name a guideline that did not exist in final form when
the note was written, or an actively-revised area.

| # | File | Line | What to re-check | Status |
|---|---|---|---|---|
| A1 | `01_Cardiovascular.md` | 169 | **2026 Australian Hypertension Guideline** (Heart Foundation / Stroke Foundation / Hypertension Australia, National Hypertension Taskforce) — in final review, expected later in 2026, not yet released as of Aug 2026. Will likely supersede the current BP targets/thresholds in that section. Check the Heart Foundation website. | ⬜ pending |
| A2 | `02_Respiratory.md` | 411 | COVID-19 management guidance — the note itself flags this as one of the most actively-revised areas. Re-check current state/local guidance for antivirals and treatment thresholds. | ⬜ pending |
| A3 | `03a_Anaesthetics_Primer.md` | 47 | COCP/HRT and perioperative VTE risk — note records the evidence base as actively evolving and the traditional "stop 4 weeks before major surgery" advice as increasingly questioned. Re-check for a settled Australian position. | ⬜ pending |

## Section B — Jurisdiction-variable or "check current" at point of use

These are not pending releases. They are places where the notes deliberately
decline to fix a single number because Australian practice genuinely varies by
state, institution, or guideline edition. The action is to confirm the note
still correctly describes the *variation*, not to pin one figure.

| # | File | Line | What to re-check | Status |
|---|---|---|---|---|
| B1 | `06_Metabolic_Medicine_and_Endocrinology.md` | 540 | Co-formulated insulin (e.g. Ryzodeg) perioperative timing — note defers to the full guideline's Appendix K rather than reproducing the decision pathway. Confirm the referenced appendix still exists in the current edition. | ⬜ |
| B2 | `10_11c_Oncology_-_Palliative_Care_Prescribing.md` | 13 | Opioid choice in renal impairment — defers to current Therapeutic Guidelines: Palliative Care renal-impairment dosing tables. | ⬜ |
| B3 | `10_11c_Oncology_-_Palliative_Care_Prescribing.md` | 29 | Buprenorphine patch conversion ratios — noted as varying between sources. | ⬜ |
| B4 | `11_07b_Ortho_-_Osteomyelitis__...md` | 21, 23 | Osteomyelitis adjunct-drug timing (fusidic acid / rifampicin) and precise duration cutoffs — flagged as a genuinely evolving, guideline-edition-specific area. Core choice (flucloxacillin) confirmed and does not need re-checking. | ⬜ |
| B5 | `14_01_Psych_-_Mood_Disorders__...md` | 30 | Australian severity-to-treatment mapping in depression — the note states it could not confirm an Australian equivalent of NICE's PHQ-9 <16/≥16 tiering, and warns the numeric gating is UK-specific. Re-check eTG/RACGP for a current Australian mapping. | ⬜ |
| B6 | `15_12a_Paeds_-_Epilepsy_Syndromes_...md` | 57 | Status epilepticus time thresholds (5/15/25/45 min) — check current APLS ANZ / local protocol. The ConSEPT levetiracetam-vs-phenytoin finding is settled and does not need re-checking. | ⬜ |
| B7 | `16_01-05_Antenatal_Care.md` | 513 | Preferred first-line IV agent for pyelonephritis in pregnancy — guided by local antibiogram and current eTG rather than a fixed national choice. | ⬜ |
| B8 | `16_06-07_Ante-Perinatal_Infections.md` | 94 | Neonatal gentamicin dose/interval — a 2025 Australian study found 5 different guidelines in use (4.5–7 mg/kg, 24–48 h). Confirm the note still correctly describes this as deliberately individualised. | ⬜ |
| B9 | `16_14-15_Obstetric_Emergencies.md` | 48 | Preferred agent for recurrent eclamptic seizures (diazepam / clonazepam / midazolam) — local protocol dependent. The 20-minute magnesium loading infusion is settled. | ⬜ |
| B10 | `17_04_Ectopic_Pregnancy_and_GTD.md` | 34 | Methotrexate route in ectopic pregnancy — genuinely state-variable (QLD splits IM/IV at β-hCG 3000 IU/L; NSW typically IM regardless). | ⬜ |
| B11 | `04_Neurology.md` | 1361 | CT head decision rule — note records that some Australian imaging pathway guidance is built on the Canadian CT Head Rule rather than the NICE-derived algorithm presented. Confirm which is current for AMC purposes. | ⬜ |

## Section C — Step 20 source-currency spot-audit

Step 20 is a *sampling* exercise, not an exhaustive one. Current scale of
claims in the corpus, measured 2026-08-28:

- **156** "verified against" claims across **54** content files
- **33** "check current"-style deferrals

Step 22 requires re-verifying a random sample of 5 specific-guideline citations
per round, to confirm the guideline name and its claimed content were captured
accurately in the first place. Log each sample here so the same rows are not
re-sampled every round and coverage actually accumulates.

### Sampling log

| Date | Round | Citations sampled (file:line) | Result |
|---|---|---|---|
| — | — | none yet | — |

### Regenerating the raw hit lists

```bash
CF=$(ls *.md | grep -vE '^(CLAUDE|CLAUDE_CODE_PROMPT|COWORK_HANDOFF|MASTER_VERIFICATION_WORKFLOW|PHASE_EXECUTION_WORKFLOW|RECOMMENDED_WORKFLOW)\.md$')

# Step 14 — pending / in-draft / due-for-update guideline flags
grep -n "pending\|in final review\|due for update\|not yet released\|check closer to the exam\|check current" $CF | grep -i "guideline"

# Step 20 — currency claims that may since have been superseded
grep -n "verified against\|as of Aug 2026\|current as of" $CF

# Step 22 — random sample of 5 specific-guideline citations to re-verify
grep -n "verified against\|per SOMANZ\|per RANZCOG\|per RACGP\|per ANZCA\|per ADS-ANZCA\|Therapeutic Guidelines" $CF | shuf -n 5
```

---

## Known limitations of this tracker

- **Line numbers drift.** Every edit to a listed file can move them. Treat the
  line number as a hint and confirm by the quoted description.
- **The greps in Section C are keyword-based and will miss flags phrased in
  ways not anticipated.** A note saying "this may change" without any of the
  tracked keywords does not appear here. Sections A and B are what has been
  found, not what exists.
- **Section B rows are not all equal.** Some are genuine "must confirm before
  the exam"; others are notes correctly describing permanent jurisdictional
  variation, where the check is that the description is still accurate. The
  distinction is in each row's wording, not in its status marker.
