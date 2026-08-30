# Bulk Build Plan — retrieval-shaped content

**Persisted 2026-08-30.** This file is the standing instruction. On "continue": read this file, check which `NEW_*.md` files exist, resume from the first incomplete category. Do not ask what to do.

---

## The instruction, as given

> Read `CLAUDE.md` first. Then set up and execute the following, resuming on "continue" without re-explanation.
>
> **Step 0 — persist the plan.** Write this entire instruction to `data/BULK_BUILD_PLAN.md` and commit it, so later sessions know what they're doing without me re-explaining.
>
> **Scope — bulk retrieval-shaped content only:**
> - Drug subsections and classes (388 items from the no-header list)
> - Investigations (206 items from the no-header list)
> - Exam manoeuvres and procedures (16 items)
>
> **Explicitly NOT in scope** — do not build these, they're being handled separately in a chat session: comparison frameworks, framework child items, and conditions. If an item on your list is one of those, skip it and note the skip.
>
> **Method** — this is what produced the measured 16s/item rate:
> - Batch by coherent cluster so research is shared (all iron studies together, all beta-blockers together). Do not build item-by-item in list order.
> - Per-item verification is non-negotiable. The timing test caught a search summary inverting a calcium channel blocker class fact — ankle oedema attributed to non-dihydropyridines when it is a dihydropyridine effect. One error in 15 searches, invisible from the summary alone. Never skip verification to go faster.
>
> **Sourcing standard:** 3 agreeing independent sources for any dose, threshold or timing window; 2 for non-numeric. If sources disagree, omit the figure and note the disagreement — never pick one. If the standard cannot be reached, omit and note rather than stating an unverified number.
>
> **Format — match the existing corpus exactly.** Study `01_Cardiovascular.md` and `Investigation-Interpretation.md` before writing anything. Specifically:
> - Numbered `## 0.1 Topic` headings
> - `**D:**` `**R:**` `**A/P:**` `**S/Smx:**` `**Ix:**` labelled fields
> - Investigations written inline as `(*why:* ... ; *what:* ...)`, not as a bare list
> - `### 0.1.1 Mx – Immediate` / `Mx – Definitive` / `Mx – Chronic` numbered subsections
> - `> [!info]` `> [!warning]` `> [!tip]` `> [!danger]` callouts for criteria, cautions and mnemonics
> - `[[File]] Topic` cross-references rather than restating content that exists elsewhere
>
> **Product per category:**
> - **Drugs** — examples and identification · mechanism · indications with routes and doses · off-label uses · absolute contraindications with alternatives · relative cautions and adjustments · common adverse effects and response · life-threatening adverse effects and response · metabolism and excretion · major interactions · monitoring before and during. Expect structural fields to come out well and dose-bearing fields to be thinner under the numeric rule — that is the accepted trade.
> - **Investigations** — test · clinical indication · presentations it is initial or gold standard for and why · cost and safety/contraindications · "do not ignore" results · normal results and interpretation · abnormal results with DDx and next steps · alternative tests and why. Reference ranges will be incomplete under the egress block — note each omission in place rather than guessing.
>
> **Output:** one file per category, `NEW_` prefixed, standalone. No cross-references into existing corpus files beyond `[[File]] Topic` pointers.
>
> **No coverage checking.** Do not check whether anything already exists — deduplication is being handled manually.
>
> Commit and push after every completed file. Verify each push landed before starting the next.
>
> Work autonomously. No checkpoint reports between clusters. Stop only for a context limit, a genuinely unsourceable item, or something of rule-6 severity — log that as `UNRESOLVED — needs review` and skip to the next item rather than halting.
>
> On "continue": read `data/BULK_BUILD_PLAN.md`, check which `NEW_*.md` files exist, resume from the first incomplete category. Don't ask what to do.

---

## Source of items

`data/no_header_build_queue.md` — the no-header list. Items are also in
`data/build_list_drugclasses.md` and `data/build_list_investigations.md`.

**In scope:** `drug subsections` (113) + `drug classes` (275) = 388 · `investigations` (190) · `exam manoeuvres` (12) + `procedures` (4) = 16. **Total 594 no-header items** (the brief says 388/206/16; the 206 figure counts investigations+manoeuvres+procedures together, i.e. 190+12+4).

**Out of scope, skip and note:** comparison frameworks (7), framework child items (54), conditions (261), presentations (485).

---

## Deterministic file order — resume from the first one missing

### Part A — Investigations (one file per investigation category)
1. `NEW_Investigations_Haematology.md` — **INCOMPLETE, now completed by `NEW_Investigations_Haematology_Part2.md`.** The batching-test build covered only **11 of the category's 28 build-list rows**; listing it as "DONE" here caused Part A to be declared complete while 17 rows were unbuilt. **Corrected 2026-08-30.**
1b. `NEW_Investigations_Haematology_Part2.md` — the remaining 17 rows (numbered 0.11–0.25 to continue the category).
2. `NEW_Investigations_Infectious_Diseases.md`
3. `NEW_Investigations_Gastroenterology.md`
4. `NEW_Investigations_Renal_and_Urology.md`
5. `NEW_Investigations_Rheumatology.md`
6. `NEW_Investigations_Endocrine.md`
7. `NEW_Investigations_Cardiology.md`
8. `NEW_Investigations_Respiratory.md`
9. `NEW_Investigations_Obstetrics_and_Gynaecology.md`
10. `NEW_Investigations_General_and_Preventive.md`
11. `NEW_Investigations_Orthopaedics_Neurology_and_Other.md`

### Part B — Exam manoeuvres and procedures
12. `NEW_Exam_Manoeuvres_and_Procedures.md`

### Part C — Drug classes (one file per AMH section)
13. `NEW_Drugs_01_Allergy_and_Anaphylaxis.md`
14. `NEW_Drugs_02_Anaesthetics.md`
15. `NEW_Drugs_03_Analgesics.md`
16. `NEW_Drugs_04_Antidotes_and_Antivenoms.md`
17. `NEW_Drugs_05_Anti_infectives.md`
18. `NEW_Drugs_06_Cardiovascular.md` — antihypertensives already built in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`; this file covers the section's **other** subsections
19. `NEW_Drugs_07_Blood_and_Electrolytes.md`
20. `NEW_Drugs_08_Dermatological.md`
21. `NEW_Drugs_09_ENT.md`
22. `NEW_Drugs_10_Endocrine.md`
23. `NEW_Drugs_11_Eye.md`
24. `NEW_Drugs_12_Gastrointestinal.md`
25. `NEW_Drugs_13_Genitourinary.md`
26. `NEW_Drugs_14_Immunomodulators_and_Antineoplastics.md`
27. `NEW_Drugs_15_Neurological.md`
28. `NEW_Drugs_16_Obstetric_and_Gynaecological.md`
29. `NEW_Drugs_17_Psychotropic.md`
30. `NEW_Drugs_18_Respiratory.md`
31. `NEW_Drugs_19_Rheumatological.md`
32. `NEW_Drugs_20_Vaccines.md`
33. `NEW_Drugs_21_Miscellaneous.md`

A file counts as complete when it exists, ends with a build-status table, and has been pushed.

---

## Standing constraints carried from earlier in the project

- **Egress is blocked** for all Australian primary guideline domains (verified 2026-08-30: 38 domains, `curl` and `WebFetch`, all 403 at the gateway). AMH and Therapeutic Guidelines are also subscription-gated. Only `WebSearch` snippets are reachable. Every file carries a sourcing-limitation box.
- **Reference ranges and doses are the weak axis.** In the batching test, 5 of 10 investigation entries had their normal range omitted. Note each omission in place.
- **CLAUDE.md rule 5** — treat every absolute quantity as suspect, especially paediatric. Per-kg, per-m², per-age-band or per-kg-with-cap are the correct forms.
- **CLAUDE.md rule 8** — report honestly. "Clean against everything currently known to check for", never "verified complete".


---

## Correction log (added 2026-08-30, per CLAUDE.md rules 7 and 8)

Two completeness failures were found by **re-deriving every row from the build lists and checking each against the file's actual content**, rather than trusting a file's own narrative claim or this plan's "DONE" marker.

1. **`NEW_Investigations_Haematology.md`** covered 11 of 28 category rows. It was a **batching-test** output (the instruction was to build ten related investigations to measure a rate), and was then recorded here as DONE. **Fixed** by `NEW_Investigations_Haematology_Part2.md`.
2. **`NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`** never built the **beta-blockers** — three build-list rows, and arguably the most clinically important class in that subsection. **Fixed** in `NEW_Drugs_06_Cardiovascular.md` section 0.7.
3. **`NEW_Investigations_Infectious_Diseases.md`** missed **Campylobacter** and **Clostridium perfringens**; its own status block claimed 21 built and its arithmetic did not reconcile with the build list. **Fixed** in place as 0.22 and 0.23.

**Method change adopted for the rest of the build, and applied to every Part C file so far:** each file ends with a **build status table mapping every build-list row** — built, built jointly with another row, built elsewhere, deferred with a destination, or `UNRESOLVED — needs review`. **A narrative claim of completeness is not acceptable evidence and did not catch any of these three.**

**Still to re-check by the same method:** the presentation-axis `NEW_*` files built earlier in the session (Cardiology and Vascular, Dermatology, Neurology, Orthopaedics, and the rest), which predate this convention and were built against tier-tagged topic lists rather than the pipe-delimited build lists.
