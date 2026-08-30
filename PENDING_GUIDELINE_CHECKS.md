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
| B12 | `13_04_ENT_-_Nose__...md` | Allergic Rhinitis (Hay Fever) | ASCIA Clinical Update: Allergic Rhinitis — cited as the 2024 edition. Confirm no newer edition before the exam, and that combined INCS/antihistamine sprays are still stated as an equal first-line option. | ⬜ |
| B13 | `17_02_Menorrhagia__...md` | Abnormal Uterine Bleeding | The symptomatic co-test rule and the "a negative co-test does not close the case" caveat come from the Cancer Council Australia abnormal-vaginal-bleeding pathway, read alongside RANZCOG C-Gyn 6. Both sit under the National Cervical Screening Program, which has been revised more than once — re-confirm before the exam. | ⬜ |
| B17 | `18_Geriatrics_and_Older_Persons_Health.md` | Falls — Timed Up and Go cutoff | Sources genuinely disagree: **>10 s** and **>12 s** both appear as the threshold identifying community-dwelling older adults more likely to fall. The entry states the range ("about 10–12 seconds") deliberately rather than picking one. **Do not resolve this to a single figure without a primary source** — confirm what the RACGP Silver Book Part A "Falls" itself states. Blocked at build time (see Section D). | ⬜ |
| B18 | `18_Geriatrics_and_Older_Persons_Health.md` | Abuse of Older People — prevalence figures | The AIFS National Elder Abuse Prevalence Study figures used (15% overall; psychological 12%, neglect 3%, financial 2%, physical 2%, sexual 1%) were **read via search snippets, not from the primary report**, which was not reachable at build time. Internally consistent and correctly attributed, but second-hand. Verify against the NEAPS report directly before relying on them. | ⬜ |
| B21 | multiple (`18_`, `19_`, `04_Neurology`, `Communication.md`) | Step 10 equity content added in the verification pass | **The age-50 aged care eligibility threshold is ✅ VERIFIED against My Aged Care (health.gov.au), a primary government source — no longer snippet-derived.** That verification also established a second qualifying population, people who are homeless or at risk of homelessness, now stated at all five places the threshold appears. Still outstanding: the **DFV hospitalisation disparity** is stated as a magnitude, not a number, because published estimates range widely (≈30-fold) and derive partly from older datasets; if a current primary figure is obtainable, replace the range with it. The **dementia prevalence ratios (3.5 at 45–49, 3.8 at 50–54)** remain from a single research source read via snippet. | 🔶 partly verified |
| B22 | `04_Neurology.md` | MCI — culturally appropriate cognitive assessment | The KICA (Kimberley Indigenous Cognitive Assessment) is named as the validated alternative to MMSE/MoCA. Confirm it is still the recommended tool and whether other validated instruments now apply, particularly outside the Kimberley region — the entry does not claim national validation and should not be edited to imply it. | ⬜ |
| ~~B24~~ | `11_09b_Ortho_-_Trauma.md` | Burns — Parkland figure | **✅ RESOLVED.** The 3-vs-4 mL/kg/%TBSA spread was **not** jurisdictional disagreement, which is how this row originally recorded it. It is a clinical distinction: **3 mL is the standard adult baseline; 4 mL is the escalation for suspected inhalation injury, high-voltage electrical injury, or associated major trauma.** The entry now states the rule and its trigger. Also documents that the *unmodified* Parkland formula is 4 mL for everyone, which is what international literature quotes — so a reader meeting that figure elsewhere is not seeing an error. | ✅ resolved |
| **B26** | `11_09b_Ortho_-_Trauma.md` | Burns — **adult resuscitation threshold** | **Carried forward from B24 as a separate open item.** The TBSA threshold for starting formal fluid resuscitation is **genuinely inconsistent across sources**: both **≥15% and ≥20%** appear for adults, including within Australian material, and the American Burn Association uses ≥20% adults / ≥15% children. **Children ≥10% was consistent** across every source checked. The entry deliberately states the inconsistency and directs to local protocol rather than fixing a figure. **Resolve against the EMSB manual or a state burns service protocol directly** — both were egress-blocked at the time of writing. Do not "tidy" this to a single number without a primary source. | ⬜ open |
| B27 | `11_09b_Ortho_-_Trauma.md` | Burns — paediatric Rule of Nines | The paediatric percentages (infant head ~18%, each leg ~14%) are stated as approximations by nature. The entry directs to a Lund and Browder chart as the accurate age-adjusted tool, which is the correct clinical behaviour, so this is low-risk — but confirm the approximations if they are ever quoted as exact. | ⬜ |
| B25 | `11_09b_Ortho_-_Trauma.md` | Major Trauma — Primary Survey | Built from ANZCOR and general Australian major-trauma-system principles; no single primary guideline was reachable. The entry deliberately asserts **no trauma-outcome disparity figure**. Confirm state trauma-system and retrieval-activation specifics against local guidance. | ⬜ |
| B31 | `Clinical-Process-…`, `Communication.md`, `19_…` | The four N6 final-round entries | Primary sources **egress-blocked** throughout. Highest-risk: the **Closing the Gap PBS Co-payment Program** eligibility and co-payment figures (the concessional rate is quoted as fixed "until 2030" — verify, and note NPS MedicineWise resources are transitioning to ACSQHC with decommissioning around May 2026, so QUM source URLs may move); and the **higher rate of potentially preventable hospitalisation** in Aboriginal and Torres Strait Islander Australians, stated as a direction with drivers rather than a figure. | ⬜ |
| B29 | `03a_Anaesthetics_Primer.md`, `Communication.md` | The three N6 round-3 entries | Primary sources **egress-blocked** throughout: ANZCA PS41(G) (2023), ACSQHC Opioid Analgesic Stewardship standard, Medical Board sexual-boundaries guidelines, AIFS/RCH child-protection guidance. Highest-risk elements: the **pre-hospital analgesia disparity finding** and the **1.4× musculoskeletal pain burden**, both from a systematic review read via snippet; and the claim that **most child protection reports are not investigated**, which shapes what the entry advises saying to a family — verify before relying on it. | ⬜ |
| B65 | `06_Metabolic_Medicine_and_Endocrinology.md` | **Hyperkalaemia — adult absolute doses under a box claiming paediatric validity** | The verification box states the drug doses are "consistent with Australian **paediatric and adult** critical care sources (Royal Children's …)". The figures beneath are **30mL of 10% calcium gluconate** and **10mg nebulised salbutamol** — absolute adult doses that do not scale. **Confirm the paediatric doses against the RCH Melbourne hyperkalaemia guideline the box already cites** (paediatric calcium gluconate is weight-based and salbutamol is age-banded) and either state them alongside or narrow the box's claim to adults. Both a rule-5 instance and a partial-verification-box instance: the box's own claim of paediatric coverage is what makes the adult figures beneath it misleading. | ⬜ |
| B66 | `15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md` | **IO insertion local anaesthetic given as an absolute volume in the paediatric/newborn entry** | The preparation step read **"lidocaine 1% 5mL"** — 50mg, an absolute adult volume, for a procedure this file performs from birth upwards. Local anaesthetic maxima are strictly weight-based and lidocaine overdose causes LAST. **Removed rather than replaced.** **Confirm the paediatric lidocaine maximum in mg/kg** (and the separate, higher maximum for lidocaine *with* adrenaline) against the RCH Melbourne guideline or the local paediatric formulary, then state it in per-kg form. Note the equipment line in the same section already bands correctly by weight (EZ-IO needle 15mm for <39kg, 25mm for >40kg) — the dose line was the outlier. Found by the corpus-wide adult-vs-paediatric sweep, 2026-08-30. | ⬜ |
| B67 | `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA.md` | **Paediatric hypoglycaemia oral carbohydrate given as the adult absolute** | The paediatric entry gave **"10–20g of fast-acting glucose by mouth"** — the identical figure to the adult entry in `06_Metabolic_Medicine_and_Endocrinology.md`, which itself **names this entry as owning child-with-diabetes management**, so the pointer led to the adult quantity. **Confirm the weight-based paediatric figure** against the RCH Melbourne hypoglycaemia guideline or the local paediatric diabetes protocol. **Removed rather than replaced.** Lower clinical severity than B64/B66 — over-treatment causes rebound hyperglycaemia, not acute harm — but the same defect shape, and notable because the two adjacent lines (IV 10% glucose 5mL/kg; glucagon banded at 500mcg if <8y or <25kg) were already correct. Found by the corpus-wide adult-vs-paediatric sweep, 2026-08-30. | ⬜ |
| B68 | `02_Respiratory.md` | **Bronchodilator reversibility stated as "or" here and "and" elsewhere in the corpus** | The asthma diagnosis box read **"FEV1 increase ≥12% *or* ≥200 mL"**; `NEW_Investigations_Respiratory.md` 0.2 states the same criterion as **≥12% *and* ≥200 mL**. Read as *or*, the criterion is far looser than intended. **Corrected to *and* here.** Two things still to confirm at point of use: (1) that *and* is what the current Australian Asthma Handbook states, and (2) which threshold the reporting laboratory applies at all, since the **2022 ATS/ERS** update replaced the rule with **>10% of predicted** and both are in current use — the conflict is set out in full in the NEW file and is deliberately not resolved. Also carries a paediatric caveat: the box sits directly beneath the 5–16yo and <5yo pathways, and the ≥200 mL component is an adult absolute. Found by the corpus-wide adult-vs-paediatric sweep, 2026-08-30. | ⬜ |
| B69 | `08_09_Infectious_Disease_-_Miscellaneous.md` | **Post-splenectomy antibiotic prophylaxis gives adult doses only, in an entry that explicitly covers children** | The verified box gives **amoxicillin 250mg daily / phenoxymethylpenicillin 250mg BD** and then states that in children prophylaxis continues **until at least 5 years of age** — extending the regimen to children without giving a paediatric dose. Paediatric penicillin prophylaxis is weight- or age-banded. **Confirm the paediatric prophylaxis dose against eTG or the local paediatric protocol and state it alongside.** Higher priority than its severity alone suggests: young children carry the greatest risk of overwhelming post-splenectomy infection, and they are the group the stated doses do not cover. Found by the corpus-wide adult-vs-paediatric sweep, 2026-08-30. | ⬜ |
| B70 | `08_09_Infectious_Disease_-_Miscellaneous.md` | **Animal and human bites: adult doses and adult drug *choices* only, for a common paediatric presentation** | The verified box gives amoxicillin-clavulanate **875/125mg 12-hourly** and, for penicillin allergy, **ciprofloxacin 500mg + clindamycin 450mg** — adult doses, and in the allergy case adult *choices*: doxycycline (also offered in the Mx line) is traditionally avoided in younger children and ciprofloxacin is not a routine paediatric option. **Confirm the paediatric amoxicillin-clavulanate mg/kg dose and the paediatric penicillin-allergy alternative** against eTG or the RCH Clinical Practice Guidelines — RCH is already cited as a source in this very box, so the paediatric guidance sits in a source the entry already uses. Distinct from the other rule 5 items: the defect is partly drug selection, not only quantity. Found by the corpus-wide adult-vs-paediatric sweep, 2026-08-30. | ⬜ |
| B64 | `15_10_Paeds_-_UTI__Nephrotic_Syndrome__Glomerulonephritis.md` | **Paediatric nephrotic syndrome had the adult proteinuria threshold** | The paediatric entry defined nephrotic syndrome as proteinuria **>3.5g per 24h** — an absolute adult quantity that a small child cannot reach, so applying it excludes the diagnosis it defines. **Removed rather than replaced.** **Confirm against RCH Melbourne's nephrotic syndrome guideline or the Kidney Health Australia / KDIGO paediatric criteria** the Australian paediatric threshold, which is body-size-indexed — commonly expressed as **>40 mg/m²/hour** on a timed collection or a **urine protein:creatinine ratio >200 mg/mmol** on a spot sample. Confirm which measure Australian paediatric practice uses first-line, since the spot ratio is what is actually done in most settings. Same shape as the paediatric DKA fluid error: an adult figure carried into a paediatric entry where the units do not transfer. | ⬜ |
| B63 | `04_Neurology.md` | **Adult bacterial meningitis — no Listeria cover stated** | The paediatric entry adds **ampicillin/benzylpenicillin for Listeria cover in infants <3 months**, with the age-based rationale verified. The adult entry gives empirical **ceftriaxone 2g IV q12h** plus conditional vancomycin and says nothing about Listeria at the *other* age extreme, where the same organism-by-age logic applies. **Confirm against eTG (Antibiotic)** whether Australian practice adds **benzylpenicillin or amoxicillin for adults >50 and the immunocompromised**, and at what dose. Not asserted here on recall — the paediatric rationale is verified and the adult extension is not. Also confirm the **IV dexamethasone dose** for adults, which this entry names without a figure. | ⬜ |
| B62 | `17_03_Termination_of_Pregnancy_and_Miscarriage.md`, `16_01-05_Antenatal_Care.md` | **Anti-D after termination — gestational threshold unresolved** | `17_03` said give anti-D "**if ≥10w**"; `16_01-05` says give it to **all** having surgical or medical terminations, with no gestational floor. Both appear in real guidance: some bodies exempt very early *medical* termination without instrumentation on the grounds of minimal fetomaternal haemorrhage. **Confirm against the NBA "Guideline for the prophylactic use of Rh D immunoglobulin in pregnancy care" (2024)** — already the cited source for the dosing in `16_01-05` — whether Australian practice sets any gestational floor for TOP, and whether surgical and medical termination differ. The threshold has been **removed** from `17_03` pending that answer rather than asserted, because the failure mode is silent: an omitted dose causes sensitisation that presents in a later pregnancy and cannot be traced back. | ⬜ |
| B61 | `16_01-05_Antenatal_Care.md` | **Anti-D — the entry carried both the corrected and the superseded doses; postnatal dose unverified** | The NBA-verified **Dosing** block gives **250 IU before 13 weeks / 625 IU from 13 weeks, including routine prophylaxis at 28 and 34 weeks**. Eighteen lines below, the **Anti-D in pregnancy** block still read **"500 units at 28w and 34w"** and **"250 units before 20w, 500 units after 20w"** — the very figure the verification box says understates the Australian dose. **Corrected to match the verified block.** Two things still need a source: (1) the **postnatal dose**, stated here as **"500 units standard dose"** and *not* covered by the verification box, where the Australian postnatal figure is commonly **625 IU** — confirm against the NBA guideline directly; (2) whether a **Kleihauer-quantified large fetomaternal haemorrhage** requires additional dosing beyond the 625 IU, and how that is calculated. | ⬜ |
| B60 | `15_18a_Paeds_-_Precocious_and_Delayed_Puberty__CAH.md` | **Delayed puberty referral age for girls** | The entry refers "males >14 years old, or females >14 years old with no breast development" — **the same age for both sexes**, where delayed puberty is conventionally defined as absent secondary sexual characteristics by **14 in boys and 13 in girls**, reflecting girls' earlier pubertal onset. Left unchanged pending a source rather than corrected on recall. **Confirm against RCH Melbourne's puberty guideline or APEG (Australasian Paediatric Endocrine Group)** the Australian referral thresholds for delayed puberty in each sex, and the menarche threshold (currently "absence of menarche ≥16", where 15 is also commonly used). Tanner staging and the Prader orchidometer have now been built in the same entry — they were named as the examination method and defined nowhere in the corpus. | ⬜ |
| B59 | `14_03_Psych_-_Psychotic_Disorders_and_Antipsychotics.md`, `16_10-13_Labour_and_Delivery.md` | **Puerperal psychosis — the two entries give different recurrence risks** | `14_03` states recurrence in a subsequent pregnancy is **>50%**, calling it the single strongest risk factor; `16_10-13` states **25–50%**. The ranges overlap only at their endpoint, and both are within the spread of published estimates (commonly quoted as ~25–57%). **Confirm against RANZCP or the Australian perinatal mental health guidance (COPE — Centre of Perinatal Excellence — publishes the national perinatal mental health guideline)** which figure Australian practice uses. Both entries now state the discrepancy openly rather than one silently overriding the other. Also confirm the **onset distribution**, given the two entries frame it differently ("within 2 weeks in up to 65%" vs "50% by 7 days, 90% by 3 months") — compatible but not identical. | ⬜ |
| B58 | `16_10-13_Labour_and_Delivery.md`, `17_06_Subfertility_and_OHSS.md` | **Two RCOG attributions not established as Australian practice** | (1) **Placenta accreta management** was labelled "(RCOG recommendations)" — planned delivery at **35–36w**, elective caesarean, hysterectomy with placenta left in situ. The file's localisation box names the LMWH/anaesthesia timing and caesarean urgency classification, not this entry. **Confirm against RANZCOG's placenta accreta spectrum guidance**, especially the delivery-timing window. (2) **OHSS severity grading** is labelled "RCOG severity classification" — the four cumulative grades (mild/moderate/severe/critical) are internally coherent and broadly international, but **confirm whether RANZCOG or the Fertility Society of Australia specifies different thresholds**, particularly the **Hct >45%** cutoff for severe. Contrast with `16_06-07`, where an RCOG Green-top guideline is used legitimately *because RANZCOG explicitly adopts it* — that is the test to apply. | ⬜ |
| B57 | `15_04a_Paeds_-_URTI_and_LRTI.md`, `08_01-03_Infectious_Disease_-_Bacterial_Infections.md` | **Diphtheria — antitoxin dose unverified; "or" corrected to "plus"** | The paediatric entry framed antitoxin and erythromycin as **alternatives**; they are complementary (antitoxin neutralises unbound circulating toxin, the antibiotic eradicates the organism and halts further toxin production). Corrected. Separately, the **antitoxin dose "10–30k U IM"** appears in only one entry and is not verified: published regimens are commonly **20,000–100,000 units**, varying by disease site and duration, and the route is often **IV** for severe disease rather than IM. **Confirm against the Australian Immunisation Handbook / CDNA Series of National Guidelines (SoNG) for diphtheria**, which also specifies antitoxin access (it is not held routinely and is released through state public health units) — a process point an intern would actually need. | ⬜ |
| B56 | `04_Neurology.md`, `15_02_Paeds_-_Ill_and_Feverish_Child__Meningitis__Encephalitis.md` | **IV aciclovir dose for encephalitis — was absent from the whole corpus** | Both encephalitis entries said "IV aciclovir" with no dose; the adult entry gave no duration either. The corpus's only aciclovir doses were **oral** regimens for cold sores, shingles and suppression. **10mg/kg every 8 hours** has been added as the standard adult figure. **Confirm against eTG (Antibiotic) or the Australian Injectable Drugs Handbook**, and specifically confirm the **paediatric dose, which is age-dependent** (neonates and young infants differ from older children) and is currently stated as the adult figure in the paediatric file. Also confirm the empirical **triple therapy** combination that entry gives (ceftriaxone + clarithromycin + aciclovir) against current Australian practice. | ⬜ |
| B55 | `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA.md` | **Paediatric hypoglycaemia — no threshold stated at all** | The entry gives full management (10–20g oral glucose, IV 10% glucose 5mL/kg, glucagon 1mg/500mcg) and **never defines hypoglycaemia**. The corpus's other two thresholds — **<3.3 mmol/L** adult and **<2.6 mmol/L** neonatal — are both wrong to read across to a child with diabetes. **Confirm against the RCH Melbourne or Queensland Children's Hospital hypoglycaemia guideline, or the APEG (Australasian Paediatric Endocrine Group) position**, what threshold triggers treatment in a child with known diabetes, and whether Australian paediatric practice uses the "4 is the floor" treat-at-<4.0 convention rather than a strict biochemical cutoff. Also confirm the **IV glucose dose** — this entry says 10% glucose **5mL/kg** while many paediatric protocols use 2mL/kg of 10%. | ⬜ |
| B54 | `09_07_Dermatology_-_Chickenpox__Shingles__Pityriasis_Rosea__Hidradenitis_Suppurativa.md` | **Hidradenitis suppurativa — drug list not staged, and two specific doubts** | The Hurley classes have been built (structural, source-independent) and management described as a stage-driven ladder, but **the existing drug list was left unchanged and is not stage-tied**. Two specific things to check against **eTG (Dermatology) or the Australasian College of Dermatologists**: (1) the entry lists **flucloxacillin**, which treats HS as a staphylococcal infection when it is primarily inflammatory — confirm whether it belongs at all, versus doxycycline as the standard systemic first-line; (2) it lists **PO rifampicin** on its own, where the recognised regimen is **clindamycin + rifampicin in combination** — rifampicin as monotherapy invites resistance. Also confirm the **PBS criteria for adalimumab** in severe HS, which is the Australian-specific fact most worth knowing here and is currently absent. | ⬜ |
| B53 | `10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma.md` | **Ann Arbor staging — stages did not partition; spleen miscategorised** | Stage 1 read "One node affected" and stage 2 "≥1 node affected on the same side of the diaphragm", making **stage 1 a strict subset of stage 2**; the unit is a lymph node **region**, and stage 2 requires **≥2** regions. Stage 4 gave the **spleen** as an example of extranodal involvement, but the spleen is lymphatic tissue recorded with the **S** suffix. Both were visible from the box alone. Corrected, with the A/B/S/E suffixes added. **Confirm against eviQ or the Cancer Council Australia lymphoma pathway** whether Australian practice now stages by the **Lugano classification** (which modified Ann Arbor and is the current international standard for FDG-avid lymphoma) rather than Ann Arbor as taught — the entry teaches Ann Arbor, which remains the standard exam answer, but the two are not identical. | ⬜ |
| B52 | `10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes.md` | **Lynch syndrome — Amsterdam criteria were a hybrid of versions I and II** | The box carried the Amsterdam **II** cancer list (colorectal, endometrial, small bowel, ureter, renal pelvis) with the Amsterdam **I** age criterion ("≥1 **colon** cancers diagnosed at <50"), so a family qualifying through non-colorectal cancers failed the age criterion as written. Corrected to Amsterdam II throughout and relabelled. **Confirm against eviQ** (the Australian cancer-genetics reference, `eviq.org.au`) which criteria set Australian familial cancer services actually apply, and the **colonoscopy surveillance interval and start age** stated in the same entry (currently "from age 20, every 1–2 years") — eviQ's Lynch surveillance protocol is gene-specific (MLH1/MSH2 differ from MSH6/PMS2), which this entry does not reflect. | ⬜ |
| B51 | `10_12_Oncology_-_Breast.md` | **Phyllodes tumour — margins and grading sourced non-Australian** | The entry's box names its sources honestly (**StatPearls, the NCCN breast cancer guideline, general literature**) and does *not* claim Australian verification, which is the correct pattern rather than a defect. Recorded so the gap is visible: the **≥1cm clear margin** recommendation and the benign/borderline/malignant grading are carried from a US guideline. **Confirm against Cancer Australia's breast cancer guidance or the RACS/BreastSurgANZ position** whether Australian practice states the same margin. Margin width for phyllodes is unlikely to be jurisdiction-specific, so this is a sourcing-provenance check rather than a suspected error. | ⬜ |
| B50 | `09_01_Dermatology_-_Dermatological_Emergencies.md`, `01_Cardiovascular.md` | **IM adrenaline — the <7.5 kg / <6 month band** | The ASCIA dose table in `09_01` — the entry both `01_Cardiovascular` and `15_01b` point at as the owner of this number — **stopped at 7.5 kg**, so a reader following the pointer for an infant reached a table that did not cover them. The only figure the corpus held for this band, **0.1–0.15 mg (0.1–0.15 mL)**, sat in `01_Cardiovascular` — a file that defers to `09_01` for the table. That figure has been carried into the owner table, but is **itself unverified**: it sits above what the box's own **0.01 mg/kg** rule gives for a <7.5 kg infant (<75 mcg), and a range rather than a single volume is unusual for a drawn-up dose. **Confirm the exact ASCIA figure for this band** against the ASCIA *Acute Management of Anaphylaxis* guideline directly — and confirm whether the band is expressed by weight (<7.5 kg), by age (<6 months), or both. Same drug and same circular-reference shape as **B43**. | ⬜ |
| B49 | `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA.md` | **Paediatric DKA maintenance fluid rate — unit error, corrected** | The table gave **">40kg — 4mL/kg/h"**; the correct figure is **40 mL/h as a fixed rate**. For a 50kg adolescent that is 200 mL/h versus 40 mL/h — a **five-fold** overestimate of maintenance in the condition where fluid overload drives cerebral oedema. Corrected from search results quoting the reduced-maintenance bands (0–9kg 2 mL/kg/h; 10–39kg 1 mL/kg/h; >40kg 40 mL/h), consistent with the **SA Health Paediatric CPG for DKA in Children** that this file's own box already cites. **Confirm against the SA Health guideline PDF directly** — `sahealth.sa.gov.au` was reachable in search results but the PDF was not read in full. Also confirm the adjacent figures in the same box, which were **not** part of this correction and are unverified here: the pH-based deficit estimate (>7.1 = 5%, <7.1 = 10%), the 48-hour correction arithmetic, and the 40 mmol K per litre. **Added 2026-08-29 (G29 absolute-threshold sweep): the dextrose rate.** The same entry says "once BG <14, start **10% dextrose infusion at 125mL/h**" — an **absolute** rate in a paediatric protocol, the same shape as the maintenance-fluid error corrected above, and it sits *outside* the box this row was originally written about. 125 mL/h is an adult-sized rate; for a 10kg toddler it is far above maintenance. Australian paediatric DKA protocols more commonly **add dextrose to the running fluid** (changing the bag to a glucose-containing solution at the existing calculated rate) rather than running a separate fixed-rate infusion alongside it. **Confirm against the SA Health paediatric DKA guideline** whether the dextrose is given as a separate infusion at all, and if so at what weight-indexed rate. | ⬜ |
| B48 | `08_01-03_Infectious_Disease_-_Bacterial_Infections.md` | Centor criteria — ARF caveat | The **ARF caveat is not in doubt** and is already source-referenced in `13_05a` (which cites RCH Melbourne and directs to the Australian ARF/RHD guideline); this row exists because the caveat has now been stated in a **second** file and the two must stay in step. **Confirm against the current Australian guideline for the prevention, diagnosis and management of ARF/RHD** what the actual high-risk-population pathway specifies — the entry deliberately says "high ARF risk is an independent indication to treat" without quoting a specific antibiotic, duration or age cut-off, and those should come from the guideline rather than be inferred. | ⬜ |
| B47 | `08_01-03_Infectious_Disease_-_Bacterial_Infections.md`, `15_24b_Paeds_-_Screening__SIDS__Vaccination_Schedule.md` | **Hib booster timing — the two NIP schedules in this corpus disagree** | `08_01-03` places the Hib booster at **18 months**; `15_24b` places it at **12 months**. **One is wrong and this was deliberately not resolved by picking a winner** — `health.gov.au` is egress-blocked and the NIP schedule is the operative document. Both tables are marked. **Check the current NIP schedule and correct both files in the same edit.** The adolescent **meningococcal ACWY** timing also differed and *was* resolved: the NIP adolescent dose is 14–16 years (Year 10), confirmed from Australian Immunisation Handbook material, and `15_24b` has been corrected from Year 7. Note these two schedules sit under different headings, so the duplicate-header check cannot pair them — they need checking together by hand. | ⬜ |
| B46 | `01_Cardiovascular.md` | ORBIT bleeding score components | The missing **reduced haemoglobin/anaemia (2 points)** component and the **maximum of 7** are confirmed from the ORBIT derivation paper (*European Heart Journal* 2015) via search results. The **risk bands quoted (low 0–2, medium 3, high ≥4)** come from the same source and are the element to confirm — band boundaries are the part most often reported inconsistently between calculators. Note also that Australian guidance (see the AF anticoagulation entry) does not treat any bleeding score as a threshold for withholding anticoagulation, so the bands inform modifiable-risk review rather than a decision. | ⬜ |
| B45 | `03_Gastrointestinal.md`, `15_08_Paeds_-_Surgical_Abdomen…` | Appendicitis scoring | The Alvarado component weights and interpretation bands (leucocytosis = **2**, total 10; 1–4 unlikely / 5–6 compatible / 7–8 probable / 9–10 very probable) and the sensitivity/specificity characterisation (<5 rules out at ~99% sensitivity; ≥7 rules in poorly, worst in men at ~57% specificity) come from **the published systematic review of the Alvarado score via search results, not an Australian guideline**. The arithmetic error corrected here is not in doubt — the itemised components summed to 9 while the box demanded ≥10. **Two open items:** (a) confirm whether Australian paediatric surgical practice actually prefers **AIR over Alvarado**, since the two files use different scores and now say so rather than resolving it; and (b) confirm the sensitivity/specificity figures if they are ever quoted as exact. | ⬜ |
| B44 | `10_05_Haemonc_-_Normocytic_Anaemia_and_Sickle_Cell_Disease.md`, `15_14_Paeds_-_…` | Sickle cell — penicillin prophylaxis schedule | The two entries disagreed: 10_05 said prophylaxis "if frequent pneumococcal infections (lifelong)", 15_14 said "from 3 months to 5 years". **15_14 is right in substance** — prophylaxis is routine from infancy, not a response to recurrent infection — and 10_05 has been corrected to match. **Confirm the exact Australian start age and minimum duration** (3 months vs 2 months, and whether Australian practice stops at 5 or continues) against RCH / eviQ / a state haematology protocol, and confirm the criteria for continuing beyond 5. Also removed a **UK carrier-prevalence statistic** ("10% of UK Afro-Caribbeans") from 15_14; **no Australian carrier rate has been substituted** and none should be added without a source. | ⬜ |
| B43 | `09_01_Dermatology_-_Dermatological_Emergencies.md`, `01_Cardiovascular.md`, `15_01b_Paeds_-_Anaphylaxis.md` | Anaphylaxis — IM adrenaline dosing | **Highest-priority row in this tracker.** The ASCIA weight-and-age criteria (0.15 mg for 7.5–20 kg and ≤5 y; 0.3 mg for >20 kg and ≥5 y; 0.5 mg for >50 kg and ≥12 y; overall 0.01 mg/kg to max 0.5 mg) were taken from **search results quoting the ASCIA acute management guidelines, not from the guideline PDF read directly** (`allergy.org.au` has been egress-blocked throughout this project). Two independent search results agreed, and the figures are consistent with the weight-based correction already recorded in `15_01b`. **Confirm against the current ASCIA *Acute Management of Anaphylaxis* guidelines directly before relying on any of the three sites** — this is the most time-critical dose in the corpus and it now appears in three files that must agree. | ⬜ |
| B42 | `03_Gastrointestinal.md` | Alcohol withdrawal severity scoring | GMAWS (a **UK/NHS Scotland** tool) previously led this box and drove the treatment trigger. Reordered so **CIWA-Ar** leads, with **AWS** named as the other instrument in NSW Health guidance, and the treatment trigger changed from "GMAWS ≥2 or CIWA-Ar ≥10" to CIWA-Ar ≥10. Confirmed from **search results citing NSW Health, SA Health and WA Health CIWA-Ar charts**, not from a primary guideline read directly. **Confirm the CIWA-Ar severity bands (<10 / 10–20 / >20) and the monitoring frequencies against your state's own chart**, since the chart is the operative document and thresholds for *treatment* versus *monitoring* are not always the same number. GMAWS retained only as a recognisable UK abbreviation. | ⬜ |
| B41 | `07_Renal_Medicine_and_Urology.md`, `11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis.md`, `12_02_Rheum_-_…` | Reference-value validity caveats (eGFR, FRAX) | Built from **standard laboratory and instrument physiology rather than a named Australian source**, so low-risk but unverified in specifics. The eGFR caveats — invalid while creatinine is unstable, over-estimates function at low muscle mass — are universal and not jurisdictional. **Two items to confirm:** (a) whether Australian laboratories' eGFR reporting carries its own stated caveats worth quoting (Kidney Health Australia / CARI guidance), and (b) that the **Australian FRAX model** is the one the 2024 RACGP/Healthy Bones threshold of ≥10% MOF was calibrated against — the entry now says to select Australia explicitly, which is correct in principle but was not confirmed against the guideline's own wording. The **removal of "NOGG"** (a UK body) is not in doubt. | ⬜ |
| B40 | `05_Ophthalmology.md` | Anti-VEGF agents for wet AMD | The **route correction (intravitreal injection, not infusion) is not in doubt** — it is the defining feature of the treatment. The open item is the **agent named as the example**: the entry now states that **ranibizumab and aflibercept are the PBS-listed intravitreal agents and bevacizumab is used off-label**, which reflects the general Australian position but was **not confirmed against a current PBS listing**. Confirm current PBS status and injection interval (the entry says "roughly every 4 weeks initially" deliberately, since maintenance intervals are individualised by treat-and-extend protocols). | ⬜ |
| B39 | `03_Gastrointestinal.md` (×3), `17_09_Cervical__Vaginal_and_Endometrial_Cancer.md` (×2) | "2-week-wait" replaced with "urgent specialist referral" | The UK NHS pathway name was removed rather than replaced with an Australian timeframe, **deliberately**: referral urgency in Australia is set per tumour stream by the **Cancer Australia Optimal Care Pathways** and by state-based criteria, and no single national two-week equivalent exists to substitute. **The open item is whether a specific timeframe should be stated for each of these presentations** — colorectal red flags, upper-GI red flags, cervical cytology, postmenopausal bleeding. Check the relevant Optimal Care Pathway for each and add the timeframe only if the pathway states one. The clinical behaviour (red flag → urgent referral) is unchanged and not in question. | ⬜ |
| B38 | `02_Respiratory.md` | Latent TB regimens | Corrected from the UK 3HR regimen to the Australian options, **from search results rather than a primary Australian TB guideline** — national TB guidance is state/territory-based and no single reachable national document was found. Confirmed from snippets: the most frequently used Australian regimens are **isoniazid 6–9 months (6–9H)** and **rifampicin monotherapy 4 months (4R)**. **Confirm against the relevant state TB service guidance**, and specifically confirm (a) whether 6H or 9H is the stated Australian duration for isoniazid monotherapy — the entry gives the range deliberately — and (b) the current availability and place of **3HP** (isoniazid + rifapentine weekly ×12), which is established internationally and used in some Australian services but should not be quoted as standard without local confirmation. | ⬜ |
| B37 | `15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md` | Paediatric ALS — adrenaline and amiodarone shock timing | **`anzcor.org` is egress-blocked**, so the corrected adrenaline timing (**first dose after the 2nd shock**, not the 3rd) was confirmed from search results quoting ANZCOR paediatric guidance rather than from Guideline 12.2 itself. It is consistent with the adult ANZCOR position already verified in `01_Cardiovascular`, which is a second independent line of support, but **confirm against Guideline 12.2 directly.** **The amiodarone timing (after the 3rd shock) was deliberately left unchanged and is NOT verified** — the paediatric shock number could not be confirmed, and changing it on the strength of the adult sequence would have been the same error in the other direction. Confirm both figures in one sitting. | ⬜ |
| B36 | `08_01-03_Infectious_Disease_-_Bacterial_Infections.md` | Passive Immunisation — Immunoglobulin After an Exposure | Built during the abbreviation triage, from **general immunology and the timing windows already verified elsewhere in this corpus** (VZIG 10 days, anti-D 72 hours — both cross-checked against the entries that own them, Step 12). The active-vs-passive distinction, the ~3–4 week antibody half-life, the hyperimmune-vs-normal product distinction and the live-vaccine interference are standard immunology and low-risk. **Two elements to confirm:** the **live-vaccine deferral interval after immunoglobulin** is deliberately *not* given as a number — it varies by product and dose, and the entry directs the reader to the Australian Immunisation Handbook; confirm before ever quoting a figure. And the **equity claim is stated as a mechanism, not a statistic** — cold-chain blood products with short deadlines are harder to deliver at distance — which was **not verified against an Australian source**; confirm supply/stocking arrangements for immunoglobulins in remote services before treating it as established. | ⬜ |
| B35 | `08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs.md` | The STI Check entry, and the two corrected regimens | **`sti.guidelines.org.au` is egress-blocked**, so the *Standard asymptomatic checkup* page was read via search snippets. Confirmed from snippets and low-risk: HIV and syphilis serology on every check; site-directed chlamydia/gonorrhoea NAAT; first-pass urine in men and self-collected vaginal swab in women; MSM three-site testing at least 12-monthly and 3-monthly at higher risk. **Higher-risk elements to confirm first-hand: the window-period figures** (chlamydia/gonorrhoea 1–2 weeks, HIV ~6 weeks on a 4th-generation assay, syphilis "several weeks") — these are quoted as approximate and should not be tightened without the primary source — **and the point-of-care testing claim in the equity box**, which is stated as a mechanism (shortening test-to-treat time in remote services) rather than as a named programme or a figure, deliberately. The corrected **chlamydia and gonorrhoea regimens** were cross-confirmed against the WA Health quick guide already cited in `17_08` plus the ASHM/CDNA gonococcal recommendations, so they rest on two independent sources rather than one snippet. | ⬜ |
| B34 | `History-Taking.md` | Clinical Formulation | Both sources **egress-blocked** and read via search snippets: the **RANZCP** mood-disorders guidelines' biopsychosocial-lifestyle framing, and **Selzer & Ellen, *Formulation for beginners*, Australasian Psychiatry 2014;22(4):397–401** (`psychdb.com` mirror blocked; the citation details come from the search result, not from the paper itself). The 4 Ps grid and the biopsychosocial axis are standard and internationally consistent, so the structural content is low-risk. The element to confirm is the **citation itself** — verify the Selzer & Ellen volume/issue/pages against the journal before quoting it. | ⬜ |
| B33 | `Clinical-Process-EBM-Consent-Capacity.md` | The three N2 epidemiology entries (study design & bias, p-values/CIs, screening principles) | Built while **`health.gov.au` and `cancer.org.au` were both egress-blocked**, so the **Population Based Screening Framework** was read via search snippets rather than the primary PDF. What is confirmed from the snippets: the framework exists, was endorsed by AHMAC in 2008 and updated in 2016 and August 2018, is explicitly built on the WHO/Wilson–Jungner 1968 principles, and is structured in two parts (criteria for whether to screen; principles for implementing and managing a programme). **What could not be read first-hand is the exact wording and grouping of the individual criteria** — the condition/test/programme three-way grouping used in the entry is a faithful and standard rendering of Wilson–Jungner, but is not quoted from the Australian document. Re-read the framework PDF and confirm the grouping before quoting it as the Australian criteria. The NHMRC levels I–IV and the bias definitions are internationally standard and low-risk. | ⬜ |
| B32 | `14_05a_Psych_-_Eating_Disorders.md`, `16_01-05_Antenatal_Care.md` (×2), `16_10-13_Labour_and_Delivery.md` | Four surviving **UK NICE** recommendations with no adjacent Australian verification | Found by the **Step 17 re-run** (see the workflow's record-error note). Unlike the other NICE mentions in the corpus — which sit beside an Australian source that confirms or contrasts them (`15_09b` Australian Prescriber/RCH; `16_01-05:247` RANZCOG) — these four state a NICE recommendation as the operative guidance with nothing Australian behind it: **(1)** guided self-help before CBT in adult bulimia; **(2)** the NICE antenatal visit schedule (<12, 16, 25, 28, 31, 34, 36, 38, 40, 41 weeks), which is a **UK** schedule and differs from Australian shared-care scheduling; **(3)** early self-monitoring of blood glucose in pre-existing diabetes in pregnancy; **(4)** water birth as NICE-recommended. They were **flagged inline rather than deleted or replaced**, because deleting loses real clinical content and substituting an "Australian equivalent" from memory would fabricate a citation. Verify each against RANZCOG / ANZAED / state maternity guidance and either re-source or remove. | ⬜ |
| ~~B30~~ | `Examination.md`, `Communication.md` | "Chaperone" vs "observer" terminology | **✅ RESOLVED.** Confirmed against the **Medical Board of Australia *Sexual boundaries* guidelines, section 7.1 "Use of observers"** — a primary source, not a snippet. All 8 instances in `Examination.md` updated. The resolution also surfaced a larger gap than the terminology itself: nothing in the corpus explained what an observer is *for*, who can act as one, or what happens if the patient declines. A full section was built in `Examination.md` (witness **and** comfort purposes; qualification requirements; the patient's right to decline and the doctor's resulting choice; observer vs support person as two distinct rights; "intimate examination" defined from the patient's perspective). The duplicate subsection in the Professional Boundaries entry was reduced to a cross-reference. | ✅ resolved |
| B28 | `Communication.md`, `Clinical-Process-…` | The four N6 round-2 entries | All built from **egress-blocked** primary sources read via search snippets: ACSQHC Open Disclosure Framework (2026 ed.), Ahpra mandatory-notification guidelines and *Good medical practice*, RACGP aggression guidance. Highest-risk elements: the **apology-protection legislation** claim (stated generally, jurisdiction not specified — verify before relying on it legally); the **treating-practitioner exemption** for notifiable conduct, where jurisdictional variation is flagged but not detailed; and the **record retention periods** (7 years adult / age 25 child), which vary by state legislation. | ⬜ |
| B23 | `Clinical-Process-EBM-Consent-Capacity.md` | Diagnostic test characteristics; ARR/RRR/NNT | Both built from RACGP and Australian Prescriber material read via **search snippets** — `racgp.org.au` and `australianprescriber.tg.org.au` are both egress-blocked. The concepts are universal and low-risk, but the **worked example figures (0.2%/0.1% → RRR 50%, NNT 1,000)** are illustrative arithmetic rather than a quoted study, and should stay labelled as such. | ⬜ |
| B19 | `19_General_Practice_and_Preventive_Medicine.md` | Preventive Medicine — immunisation | NIP funded age thresholds and included vaccines have changed repeatedly. The entry deliberately avoids stating specific funded ages for adult vaccines and tells the reader to check current eligibility. **Do not add specific ages without a current primary source.** | ⬜ |
| B20 | `19_General_Practice_and_Preventive_Medicine.md` | Continuity of Care — patient enrolment | Voluntary patient registration in Australian general practice is actively changing policy. The entry says so rather than describing a fixed arrangement. Re-check before the exam. | ⬜ |
| B14 | `18_Geriatrics_and_Older_Persons_Health.md` | Polypharmacy and Deprescribing | The MJA *Deprescribing in Older People* clinical practice guideline was published in 2026 and carries 185 consensus recommendations — this entry reflects its general principles only. Check for the full guideline's specific medicine-class recommendations before the exam. | ⬜ |
| B15 | `18_Geriatrics_and_Older_Persons_Health.md` | Falls / Frailty | Vitamin D for falls prevention is genuinely contested and dose- and setting-dependent; the entry states this rather than picking a figure. Re-check whether Australian guidance has settled. Frailty content draws on the MJA Australian Consensus Statement (modified Delphi), which is recent. | ⬜ |
| B16 | `18_Geriatrics_and_Older_Persons_Health.md` | Abuse of Older People | Elder abuse reporting is under active policy reform under the National Plan to Respond to the Abuse of Older Australians. The stated position — **no general statutory mandatory reporting duty** — is correct as of Aug 2026 but is exactly the kind of thing that changes. Re-confirm. | ⬜ |
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
| 2026-08-28 | Phase 1 (P1–P6) | Not a random sample — three citations written this round were sourced from scratch and are logged here for re-verification, not re-sampled from existing text: ASCIA Allergic Rhinitis 2024 (`13_04`); healthdirect + light-therapy meta-analysis (`14_01` SAD); RANZCOG C-Gyn 6 + Cancer Council AU pathway (`17_02`). | Sourced this round; due for re-check nearer the exam. **The formal Step 22 random-sample audit has still never been run** — this row does not discharge it. |

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

## Section D — Content built under a network egress limitation

Several primary Australian sources are **blocked by this environment's network egress proxy** and could not be fetched directly. Content citing them was written from search-result snippets — accurately attributed, but read second-hand rather than from the source document.

**Blocked domains encountered so far:** `racgp.org.au` (Silver Book, AJGP), `safetyandquality.gov.au` (ACSQHC), `ranzcog.edu.au`, `allergy.org.au` (ASCIA), `australianprescriber.tg.org.au`, `onlinelibrary.wiley.com` (MJA).

**What this does and does not mean.** The guideline *names* and the *substance* of what they recommend are correct as far as the snippets go, and nothing here is invented. But specific numbers, thresholds and exact wording carry more risk than content read from a primary source, and any place where sources visibly disagree could not be adjudicated.

| Entry | File | Source that was blocked | Highest-risk element |
|---|---|---|---|
| Allergic Rhinitis (Hay Fever) | `13_04_ENT_-_Nose__…` | ASCIA Clinical Update 2024 | ARIA duration/severity cutoffs |
| Abnormal Uterine Bleeding | `17_02_Menorrhagia__…` | RANZCOG C-Gyn 6; Cancer Council AU pathway | The symptomatic co-test rule |
| Falls in Older People | `18_Geriatrics_…` | RACGP Silver Book Part A "Falls"; ACSQHC | TUG cutoff (see B17); exercise dose |
| Frailty | `18_Geriatrics_…` | RACGP Silver Book Part A "Frailty"; MJA consensus statement | Fried criteria wording |
| Polypharmacy and Deprescribing | `18_Geriatrics_…` | RACGP Silver Book; MJA 2026 deprescribing guideline (Wiley) | Benzodiazepine taper percentages |
| Abuse of Older People | `18_Geriatrics_…` | RACGP Silver Book Part B | NEAPS prevalence (see B18) |
| Discharge Planning | `18_Geriatrics_…` | ACSQHC transitions-of-care framework | The 2.3× readmission figure |
| Goals of Care / Ceiling of Care | `Communication.md` | ACSQHC goals-of-care guidance | Document definitions |
| Domestic and Family Violence | `Communication.md` | RACGP White Book 5th ed (racgp.org.au) | Prevalence figure; strangulation "half have no external injury" |
| Motivational Interviewing | `Communication.md` | RACGP AFP (racgp.org.au) | Stage definitions |
| Clinical Handover (ISBAR) | `Communication.md` | ACSQHC ISBAR / NSQHS Standard 6 | Nothing numeric; low risk |
| Preventive Medicine and Screening | `19_General_Practice_…` | RACGP Red Book 10th ed (racgp.org.au) | Screening eligibility ages — **cross-checked against the organ-system entries, which are the source of truth** |
| Lifestyle Risk Factors (SNAP) | `19_General_Practice_…` | RACGP SNAP guide (racgp.org.au) | Quitline number; NRT combination claim |
| Continuity of Care | `19_General_Practice_…` | RACGP advocacy material; MJA (Wiley) | The 8% ED-presentation figure; patient enrolment policy status |
| Diagnostic Test Characteristics | `Clinical-Process-…` | RACGP statistics guide (blocked) | Concepts universal; low risk |
| Interpreting Treatment Effects | `Clinical-Process-…` | Australian Prescriber (blocked) | Worked example is illustrative arithmetic, not a quoted study |
| Burns and Scalds | `11_09b_…` | ANZBA manual + referral PDF (blocked); EMSB manual (blocked); Tasmanian Burns Service protocol (blocked) | ~~Parkland 3–4 mL figure~~ **— resolved, see B24.** Remaining: the **adult resuscitation threshold** (B26, genuinely inconsistent across sources) and the paediatric Rule of Nines approximations (B27) |
| Major Trauma — Primary Survey | `11_09b_…` | No single primary guideline reachable | No disparity figure asserted (deliberate) |
| Open Disclosure | `Communication.md` | ACSQHC Framework 2026 (blocked) | Apology-protection legislation claim |
| Mandatory Reporting | `Clinical-Process-…` | Ahpra guidelines (blocked) | Treating-practitioner exemption; jurisdictional variation |
| Angry Patients / Complaints | `Communication.md` | RACGP aggression guidance (blocked) | Nothing numeric; low risk |
| Documenting in the Medical Notes | `Clinical-Process-…` | Ahpra Good medical practice (blocked) | Retention periods vary by state |
| Pain Assessment and Management | `03a_…` | ANZCA PS41(G); ACSQHC opioid standard (blocked) | Pre-hospital analgesia disparity; 1.4× pain burden |
| Professional Boundaries | `Communication.md` | Medical Board sexual-boundaries guidelines (blocked) | ~~"Observer" terminology change~~ **— resolved (B30), verified against s7.1 of the primary guideline.** No remaining flagged element |
| Explaining a Safeguarding Referral | `Communication.md` | AIFS; RCH Melbourne (blocked) | "Most reports are not investigated" — shapes the advice given |
| **Equity additions (verification pass)** | `18_…`, `19_…`, `04_Neurology`, `Communication.md` | RACGP Silver Book chapter on older Aboriginal and Torres Strait Islander people (racgp.org.au, blocked); AIHW; ABS | ~~Aged care eligibility age 50~~ **— since verified against My Aged Care, primary source; removed from this list.** Remaining: dementia prevalence ratios 3.5/3.8; DFV hospitalisation magnitude; smoking 2.6× and the 35%→20% trend |

**Action:** when any of these is next reviewed from a machine with unrestricted access, re-read the primary source and either confirm the figure or correct it, then mark the row here.

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

---

## Section E — Phase 5 build items awaiting an Australian source

Content gaps found by the Phase 5 fourth pass (all 276 leaf subclasses of the
AMH therapeutic classification, `scripts/drug_classes.py`). These are **build**
items, not currency checks: the content does not exist yet. Each needs a cited
Australian source before it is written, per the project's content-build rule.

| ID | Gap | Source needed | Status |
|---|---|---|---|
| P5-C10 | **Antivenoms — snake and other Australian envenomation.** Zero hits for `antivenom` in 148 files. Pressure-immobilisation, indications for antivenom, premedication, serum sickness | eTG Toxicology and Toxinology; Australian Snakebite Project / CSL antivenom product information | ⬜ |
| P5-C11 | **H2 antagonists.** Absent entirely — no ranitidine, famotidine, nizatidine or class name — while PPIs are well covered | eTG Gastrointestinal; AMH | ⬜ |
| P5-C12 | **Decongestants, oral and intranasal**, and rhinitis medicamentosa on prolonged topical use | eTG Respiratory / ENT; ASCIA allergic rhinitis (egress-blocked, see Section D) | ⬜ |
| P5-C13 | **Bulk-forming laxatives.** The one laxative leaf of five with no coverage — an asymmetric silence inside a class the corpus otherwise teaches | eTG Gastrointestinal | ⬜ |
| P5-C14 | **CGRP antagonists** for migraine prophylaxis — now PBS-listed, absent entirely | PBS listing criteria; Therapeutic Guidelines Neurology | ⬜ |
| P5-C15 | **Carbapenems** — mechanism and the ESBL / last-line stewardship rationale in one entry. 16 uses, dose and caution only | eTG Antibiotic; national antimicrobial stewardship guidance | ⬜ |
| P5-C16 | **TNF-alpha antagonists** — pre-treatment TB and hepatitis B screening, and infection risk on treatment. 21 uses, no entry carries the screening | eTG Rheumatology; ARA (Australian Rheumatology Association) position statements | ⬜ |
| P5-C17 | **Antimycobacterials** — the four-drug TB regimen's toxicity and monitoring profile, in the entry that teaches the regimen | National Tuberculosis Advisory Committee guidelines; eTG Antibiotic | ⬜ |

### Residual work this pass did NOT clear

> [!warning] **103 leaf subclasses — the 93 THIN and 10 NAMED ONLY — have not been individually hand-verified. They are open work, not a clean result.**
>
> The scan behind them scores four dimensions by keyword proxy, and the
> mechanism proxy is **confirmed to produce false negatives**: ocular
> anticholinergics scored NAMED ONLY against a line that explains the
> mechanism correctly in plain clinical English — *"cycloplegics (dilate the
> pupil, relieving pain and photophobia, and preventing posterior
> synechiae)"* — because not one word in it belongs to mechanism vocabulary.
> The same failure can be hiding anywhere in the other 102.
>
> So each of the 103 is one of three things and the scan cannot tell them
> apart: a genuine depth gap, a proxy false negative like the one above, or a
> class correctly left thin because it sits above the intern ceiling.
> **Deciding which requires reading the entry.** Until that happens, no THIN
> or NAMED ONLY verdict from the fourth pass may be cited as either a gap or
> as coverage.
>
> Deferred deliberately for a future session under usage constraints — recorded
> here rather than dropped. The 25 ABSENT leaves were hand-checked (4 of the
> original 28 were scan artifacts); the 148 ADEQUATE were not, and carry the
> same proxy caveat in the other direction.

### Section E (continued) — Phase 5 Part A condition gaps

From the 2,585-condition external enumeration (`data/checklist_external.csv`).
Deduplicated: Baker's/popliteal cyst, hallux valgus/bunions, concussion/post-
concussive, and the four parasomnia rows are one item each.

| ID | Gap | Source needed | Status |
|---|---|---|---|
| P5-A5 | **Serum phosphate disorders** — hypo- and hyperphosphataemia, and **refeeding syndrome** as the presentation an intern meets them in. The one electrolyte with no entry in a corpus teaching all the others | eTG; ANZ refeeding guidance; local electrolyte replacement protocols | ⬜ |
| P5-A6 | **Hypermagnesaemia** — absent while hypomagnesaemia has 13 uses | eTG | ⬜ |
| P5-A7 | ~~**Concussion and post-concussive syndrome**~~ **BUILT 2026-08-29** in `04_Neurology.md`. Sources are genuinely Australian (AIS/SMA Concussion and Brain Health Position Statement 2024; Australian Concussion Guidelines for Youth and Community Sport; ASC; SMA GRTP poster). 14-day symptom-free and 21-day minimum confirmed across three independent results. **OPEN — DISAGREEMENT:** the adult (>=19) advanced-healthcare-setting exemption is given as 'minimum 12 days' by one source and 'symptom-free at least 10 days' by another. Flagged in the entry, not resolved. Confirm against the SMA statement. | SMA / AIS position statement | 🟨 |
| P5-A8 | ~~**Central and posterior cord syndrome**~~ **BUILT 2026-08-29** in `04_Neurology.md` alongside Brown-Séquard, and **anterior cord syndrome built with them** (P5-A8 originally covered central and posterior only; anterior was found later, hidden behind the ACS acronym collision). Cross-verified snippets: StatPearls, AANS, Cleveland Clinic, AMBOSS, Wheeless'. **Open:** no numeric recovery-rate or incidence figure asserted; the 24-hour prognostic window came from a single source and is stated as a clinical sign, not a threshold. | eTG / spinal injury guidance | 🟨 |
| P5-A9 | **Cerebellar infarction** — posterior circulation stroke presenting as vertigo | Stroke Foundation Clinical Guidelines | ⬜ |
| P5-A10 | **Neurologically determined death** — brain-death determination and organ donation; compounds P5-D4 | ANZICS Statement on Death and Organ Donation | ⬜ |
| P5-A11 | **TCA overdose** — sodium bicarbonate for QRS widening; zero hits | eTG Toxicology; Austin Health poisons info | ⬜ |
| P5-A12 | **Heat stroke and heat exhaustion** — zero hits; core Australian ED presentation | eTG; state heat-health guidance | ⬜ |
| P5-A13 | **Facial fractures incl. Le Fort** — zero hits | eTG / RACS trauma guidance | ⬜ |
| P5-A14 | **Benzodiazepine overdose** — one flumazenil mention, no entry | eTG Toxicology | ⬜ |
| P5-A15 | **Alcoholic ketoacidosis** — raised-anion-gap differential distinct from DKA | eTG | ⬜ |
| P5-A16 | **Adjustment disorder** — zero hits; among the commonest general-hospital psychiatric diagnoses | RANZCP; DSM-5-TR | ⬜ |
| P5-A17 | **Gender dysphoria** — zero hits; respectful and competent care is intern-level | RACGP; AusPATH standards | ⬜ |
| P5-A18 | **Delusional disorder** — a named differential within the psychotic disorders already taught | RANZCP | ⬜ |
| P5-A19 | **Parasomnias** — sleepwalking, night terrors; zero hits, paediatric sleep is GP-level | RCH Melbourne | ⬜ |
| P5-A20 | ~~**Paronychia and felon**~~ **BUILT 2026-08-29** in `09_05_Dermatology_-_Bacterial_Infections_and_Infestations.md` from cross-verified snippets (AAFP 2017, StatPearls, Merck, Melbourne Hand Surgery). **Still to confirm against eTG Antibiotic:** the AU first-line oral agent and course length — no numeric course length was stated in the entry because only one source gave one (7–10 days), below the three-source bar for a numeric. | eTG Antibiotic | 🟨 |
| P5-A21 | **Nappy rash** — zero hits; compounds the queued nystatin gap P5-C7 | RCH Melbourne | ⬜ |
| P5-A22 | ~~**Gilbert's syndrome**~~ **BUILT 2026-08-29** in `03_Gastrointestinal.md` from cross-verified snippets (J Hepatology 2023, StatPearls, World J Hepatology). **Open:** prevalence figure omitted (single source, 2–13%, too wide); the paracetamol-toxicity association is recorded as DISPUTED and needs a primary source to settle either way. | eTG / RCPA | 🟨 |
| P5-A23 | **Pancreatic pseudocyst and intra-abdominal abscess** — named complications of pancreatitis, appendicitis and diverticulitis, all taught | eTG Gastrointestinal | ⬜ |
| P5-A24 | ~~**Baker's cyst**~~ **CLOSED — FALSE GAP, WITHDRAWN.** The corpus has `Baker cyst` at `11_05_Ortho_-_Knee_and_Ankle.md:27` under the Bursitis & cysts of the knee entry. It read as absent only because the matcher split "Baker's" into [baker, s] and then demanded an apostrophe the corpus omits. Recorded rather than deleted: a false gap that reached the build queue is worth keeping visible. Popliteal cyst, its other name, is the same entry. | — | ✅ |
| P5-A25 | **Hallux valgus and mallet finger** — zero hits; ED and GP splinting/referral decisions | RACGP | ⬜ |
| P5-A26 | **Retropharyngeal abscess** — paediatric airway emergency; peritonsillar abscess is taught | RCH Melbourne; eTG | ⬜ |
| P5-A27 | **Keratoconus** — commonest corneal ectasia, presents in young adults | RANZCO | ⬜ |
| P5-A28 | **Herpetic whitlow and lymphangitis** — occupational hand infection with a do-not-incise rule; ascending streaking in cellulitis | eTG Antibiotic | ⬜ |
| P5-A29 | **Solitary pulmonary nodule** — the incidental-finding pathway | Lung Foundation Australia / RANZCR | ⬜ |
| P5-A30 | **Peripartum cardiomyopathy, pseudoaneurysm, multifocal atrial tachycardia, coronary vasospasm** — the cardiovascular four | eTG; Heart Foundation | ⬜ |
| P5-A31 | **Premature ejaculation and epispadias** — each the unnamed half of a pair the corpus half-teaches (erectile dysfunction, hypospadias) | RACGP | ⬜ |

> [!warning] **Residual, not cleared.** 788 of the 929 absent conditions were classified out of scope **by rule, not individually verified**, and the 215 prose-only rows were not read. Both are open work in the same sense as the 103 drug leaves above.

### Section E (continued) — two unresolved categories from the acronym audit

> [!warning] **23 conditions were never actually checked. They are NOT confirmed absent.**
> The corroboration test requires a ≥9-character word in the condition's own
> name. These 23 have none, so acronym matching was disabled for them and they
> fell to ABSENT **by construction, not by evidence**:
>
> 1. Afferent loop syndrome
> 2. Amniotic band syndrome
> 3. Amyand's hernia
> 4. **Anterior Cord Syndrome**
> 5. Boston-type syndrome
> 6. Cervical spine trauma
> 7. Double aortic arch
> 8. Fetal alcohol spectrum disorder
> 9. Gastric Antral Vascular Ectasia
> 10. **Heart Failure with Reduced Ejection Fraction**
> 11. Herpes Zoster Virus
> 12. Herpes zoster oticus
> 13. Hungry bone syndrome
> 14. **Left Bundle Branch Block**
> 15. Maple syrup urine disease
> 16. Middle ear neoplasm
> 17. Neoplasm of external canal
> 18. **Orbital Floor Fracture (Blow-out fracture)**
> 19. Ovarian remnant syndrome
> 20. Pyriform aperture stenosis
> 21. **Right Bundle Branch Block**
> 22. Social Anxiety Disorder
> 23. Ulnar nerve injury
>
> The bolded ones have since been hand-checked by other means and are known:
> the bundle branch blocks and HFrEF are covered; anterior cord syndrome and
> orbital floor fracture are genuine gaps, both queued. **The other 18 have no
> verdict anyone should trust.** The 9-character threshold is doing two jobs —
> collision precision, and an implicit "is this name testable" filter — and it
> is only fit for the first.
>
> **Resolution path** (deliberately deferred, not dropped): either a second
> corroboration signal that does not depend on word length — co-occurrence of
> two short tokens, or the file's own subject area — or 18 manual greps.
> Logged as a known residual rather than resolved now, because Parts C, E, F
> and G of Phase 5 are still unstarted and this is its own small project.

> [!danger] **A systematic blind spot in the corroboration test, found by the audit.**
> Corroboration fails whenever **the corpus uses an acronym exclusively and
> never spells the term out** — there is then no word that can possibly
> co-occur. It produced three false absences out of only four suspects
> examined:
>
> | Condition | Truth | Why the test failed |
> |---|---|---|
> | Staphylococcal Scalded Skin Syndrome | **owns an entry** at `09_01:116` | corpus writes "Staph", never "Staphylococcal" |
> | Focal segmental glomerulosclerosis | covered, `07_Renal:195` + `15_10:51` | corpus only ever writes FSGS |
> | Cervical intraepithelial neoplasia | taught, `17_09:30-31` with the LLETZ rule | corpus only ever writes CIN |
>
> This is the mirror image of the collision problem: the collision fix
> assumed a spelled-out form exists to corroborate against. Where the corpus
> is acronym-only, the fix inverts and manufactures absence. **Any ABSENT
> verdict on a condition the corpus would naturally abbreviate is suspect.**

### Section F — Medications_Reference.md build log (branch `medications-reference-build`)

| ID | Entry | Source standard met | Status |
|---|---|---|---|
| MR-1 | **Antiarrhythmics — Vaughan-Williams classification.** Zero corpus hits for the classification despite the corpus prescribing amiodarone, sotalol, flecainide, verapamil and diltiazem. Built from MSD Manual, StatPearls, CV Pharmacology, LITFL; CAST/flecainide contraindication additionally from *Heart Rhythm* and Drugs.com. No numerics asserted (mechanism-level table only). **Confirm against eTG Cardiovascular.** | ✅ 2 non-numeric sources exceeded | 🟨 |
| MR-2 | **Beta-blockers — selectivity, ISA, mixed alpha/beta, and the HFrEF three.** Zero corpus hits for 'cardioselective' or 'intrinsic sympathomimetic activity' despite the corpus prescribing six beta-blockers and warning about asthma. Built from Current Medical Research and Opinion 2024 (x2), bpacnz, AAFP, OHSU Drug Class Review. **No target doses stated** — the HFrEF target doses are AU-specific numerics and three agreeing sources were not obtained; logged `source-insufficient` for the dose component only. **Confirm against eTG Cardiovascular / Heart Foundation.** | ✅ non-numeric; ⚠️ doses source-insufficient | 🟨 |
| MR-3 | **CONTENT ERROR CORRECTED — levetiracetam mechanism.** `04_Neurology.md` stated levetiracetam was a "?Ca channel blocker". Its target is **SV2A**. Confirmed across PNAS, StatPearls, NCBI Jasper's, the Keppra label and DrugBank (5 sources; 2 required for non-numeric). **Also amended the verification box above it**, which claimed the mechanisms below were verified and needed no change — the 8th instance of the partial-verification-box pattern, and the most consequential, since the box is what would stop a reader checking. Surfaced only by the spreadsheet's mechanism-level granularity ("Anticonvulsants (SV2A Ligands)"); AMH lumps these as "Other antiepileptics" and could never have exposed it. **Remaining mechanisms in that block are spot-checked, not audited — a full audit of them is open work.** | ✅ 5 sources | ✅ fixed |
| S3-1 | **Envenomation — UPGRADES P5-C10.** Not just antivenom: `snakebite` 0, `redback`/`funnel-web` 0, **`pressure immobilisation` 0**, and all 3 `envenom` hits are incidental (a workflow note, a burns annotation, a serum-sickness aside). No clinical envenomation content in 148 files. Highest-consequence absence found in Phase 5. | eTG Toxicology and Toxinology; Australian Snakebite Project | ⬜ |
| S3-2 | **Toxidromes as a framework** — anticholinergic 0, cholinergic 1, sympathomimetic only in CV drug contexts. Corpus has opioid and serotonin/NMS only. | eTG Toxicology | ⬜ |
| S3-3 | **Organophosphate poisoning** — 1 use, pralidoxime 1. Rural/agricultural AU relevance. | eTG Toxicology | ⬜ |
| S3-4 | **Beta-blocker / CCB overdose** — 1 use; high-dose insulin euglycaemic therapy and glucagon-for-overdose both 0. | eTG Toxicology; Austin Health Poisons | ⬜ |
| S3-5 | **Fascia iliaca block** — 0 hits, in a corpus that covers NOF fracture. | ANZCA; local ED protocols | ⬜ |
| S3-6 | **Type 2 (hypercapnic) respiratory failure** — 2 hits vs 29 for respiratory failure generally. Thin. | eTG Respiratory | ⬜ |
| S3-7 | **Neuromuscular respiratory failure — THIN, not absent.** FVC 29 uses, myasthenic crisis 6, but `vital capacity` never appears near GBS or myasthenia. The corpus has the measurement and the diseases and does not connect them. | eTG Neurology | ⬜ |
| FUTURE | **Exam-strategy reference file** — "Zero-Context methodology" and "Distractor Elimination Rules" from Source 3 are MCQ technique, not clinical content. Out of scope for Phase 5; recorded as a candidate separate project. | — | 💡 |
| P5-E1 | **Straight leg raise** — zero hits, in a corpus teaching sciatica, lumbar radiculopathy and cauda equina. Technique and interpretation. | RACGP; standard MSK examination texts | ⬜ |
| P5-E2 | **McMurray's test** — zero hits, in a knee file whose first header is "ligament and meniscal injuries". | RACGP; MSK examination texts | ⬜ |
| P5-E3 | **Lachman's, anterior and posterior drawer, pivot shift** — knee ligament examination. Lachman and anterior drawer are named in one table cell with no technique; posterior drawer and pivot shift absent. | MSK examination texts | ⬜ |
| P5-E4 | **Spurling's, cervical distraction, FABER/Patrick's** — cervical and hip/SI special tests, all absent. Note the one "distraction test" hit is paediatric audiology, a different procedure. | MSK examination texts | ⬜ |
| P5-E5 | **Finkelstein's and femoral stretch** — named only, no technique or interpretation. | MSK examination texts | ⬜ |
| P5-E6 | **PROM confirmation tests — nitrazine, ferning, fetal fibronectin** — all zero hits, in a corpus that teaches PROM and PPROM. The condition without its diagnostic test. | RANZCOG | ⬜ |
| P5-E7 | **FeNa, plasma metanephrines, SPEP** — 1-2 hits each, against taught conditions (AKI pre-renal vs ATN, phaeochromocytoma, myeloma). Thin. | eTG; RCPA | ⬜ |
| P5-E-METHOD | **METHOD LIMITATION: Phase 5 never enumerated investigations.** Conditions, scales, drugs and procedures were each enumerated exhaustively; a fifth axis was never named until now. Recorded because the same omission may hide further axes. | — | ⚠️ |

> [!important] **This file is the single source of truth for build-item status.**
> `MASTER_VERIFICATION_WORKFLOW.md` records what each pass *found* — its narrative
> and its evidence. It does not carry build status. Eight Part C items (P5-C10 to
> C17) previously existed in both files with independent status markers, so a
> completed build could tick one copy and leave the other reading as unstarted.
> The workflow rows now point here instead. **When adding a build item, add it
> here and only here.**

### Section F (continued) — the 44 remaining granular drug classes from the Diagnoses spreadsheet

> [!note] **Itemised because they were previously one line.** The build queue carried these as a single
> Tier 4 row, "MR-4+ Remaining granular drug classes — mostly specialist subclass detail", which pre-judged
> 44 unchecked items and made *checked-and-cleared* indistinguishable from *never looked at*. Each now has an
> ID, a corpus hit count, and a tier derived from that count plus intern relevance — not from the prior assumption.
> **Nine were mis-tiered by that assumption** and are Tier 2 or 3, not Tier 4.

| ID | Item | Tier | Status |
|---|---|---|---|
| MR-4 | **Mu-opioid full vs partial agonists** — 1 corpus hits. Buprenorphine's ceiling effect and the partial-agonist distinction — governs opioid substitution and acute pain in an opioid-dependent patient | Tier 2 | ⬜ |
| MR-5 | **Opioid strong vs weak / atypical** — 4 corpus hits. Tramadol and tapentadol's atypical mechanisms; the weak/strong ladder | Tier 2 | ⬜ |
| MR-6 | **MAOIs by reversibility** — 1 corpus hits. Irreversible vs reversible MAO-A; the tyramine interaction differs between them | Tier 3 | ⬜ |
| MR-7 | **Vesicants / chemotherapy extravasation** — 6 corpus hits. A ward emergency with a time-critical response. 6 uses, no entry | Tier 2 | ⬜ |
| MR-8 | **Muscle relaxants — botulinum neurotoxins** — 13 corpus hits. 13 uses; likely adequate, needs a read not a build | Tier 4 | ⬜ |
| MR-9 | **Carbacephem** — 0 corpus hits. Obsolete class; correctly absent | Tier 4 | ⬜ |
| MR-10 | **Monobactams (aztreonam)** — 1 corpus hits. Already NAMED ONLY in the 75-agent pass; recognition-level | Tier 4 | ⬜ |
| MR-11 | **Lipopeptides (daptomycin)** — 1 corpus hits. Already NAMED ONLY in the 75-agent pass; specialist | Tier 4 | ⬜ |
| MR-12 | **Pleuromutilins** — 0 corpus hits. Not on the Australian formulary in general use | Tier 4 | ⬜ |
| MR-13 | **Bisbiguanide antiseptics (chlorhexidine)** — 2 corpus hits. Chlorhexidine is used daily for skin prep and line care; 2 uses is thin for how often an intern handles it | Tier 3 | ⬜ |
| MR-14 | **ALS therapies (riluzole, edaravone)** — 1 corpus hits. Specialist-initiated | Tier 4 | ⬜ |
| MR-15 | **MS therapies — anti-CD20** — 3 corpus hits. MS DMT landscape; recognition-level for an intern | Tier 3 | ⬜ |
| MR-16 | **MS therapies — anti-VLA-4 (natalizumab)** — 1 corpus hits. Specialist; PML risk is the one intern-relevant point | Tier 4 | ⬜ |
| MR-17 | **MS therapies — S1P modulators** — 1 corpus hits. Specialist | Tier 4 | ⬜ |
| MR-18 | **MS therapies — interferons / glatiramer** — 1 corpus hits. Specialist | Tier 4 | ⬜ |
| MR-19 | **MS therapies — pyrimidine synthesis (teriflunomide)** — 0 corpus hits. Specialist | Tier 4 | ⬜ |
| MR-20 | **IL-12/23, IL-17, IL-23 inhibitors** — 7 corpus hits. Biologics an intern will see on medication charts; infection-screening implications | Tier 3 | ⬜ |
| MR-21 | **JAK1 / TYK2 inhibitors** — 0 corpus hits. Zero hits. Increasingly common in RA/IBD/derm; VTE and infection warnings are intern-relevant | Tier 3 | ⬜ |
| MR-22 | **Calcimimetics (cinacalcet)** — 2 corpus hits. Renal/endocrine specialist | Tier 4 | ⬜ |
| MR-23 | **Tyrosine hydroxylase inhibitors (metirosine)** — 0 corpus hits. Phaeochromocytoma, specialist | Tier 4 | ⬜ |
| MR-24 | **P-selectin inhibitors (crizanlizumab)** — 0 corpus hits. Sickle cell, specialist | Tier 4 | ⬜ |
| MR-25 | **Megakaryocyte maturation inhibitors (anagrelide)** — 0 corpus hits. Haematology specialist | Tier 4 | ⬜ |
| MR-26 | **Guanylate cyclase-C agonists (linaclotide)** — 1 corpus hits. Constipation second-line, specialist-initiated | Tier 4 | ⬜ |
| MR-27 | **Intestinal chloride channel activators (lubiprostone)** — 0 corpus hits. As above | Tier 4 | ⬜ |
| MR-28 | **NHE3 inhibitors (tenapanor)** — 0 corpus hits. As above | Tier 4 | ⬜ |
| MR-29 | **5-HT4 agonists (prucalopride)** — 0 corpus hits. As above | Tier 4 | ⬜ |
| MR-30 | **Topical antibacterials by mechanism** — 18 corpus hits. 18 uses; likely adequate, needs a read not a build | Tier 4 | ⬜ |
| MR-31 | **Topical antifungals — pyridones (ciclopirox)** — 0 corpus hits. Minor; azoles and terbinafine already covered | Tier 4 | ⬜ |
| MR-32 | **Psychedelics (5-HT2A agonists)** — 1 corpus hits. Emerging; not intern-level in Australia yet | Tier 4 | ⬜ |
| MR-33 | **Monoamine releasing agents / MDMA** — 2 corpus hits. Recreational-drug presentation to ED; serotonin toxicity link | Tier 3 | ⬜ |
| MR-34 | **Azapirones (buspirone)** — 0 corpus hits. Zero hits. Non-dependence-forming anxiolytic; a real prescribing option | Tier 3 | ⬜ |
| MR-35 | **Herbal / botanical supplements** — 3 corpus hits. St John's wort interactions are an intern-level trap; 3 uses is thin | Tier 3 | ⬜ |
| MR-36 | **Essential fatty acids (omega-3)** — 3 corpus hits. Low yield | Tier 4 | ⬜ |
| MR-37 | **Essential minerals / trace elements** — 2 corpus hits. Low yield outside TPN | Tier 4 | ⬜ |
| MR-38 | **RANKL inhibitors (denosumab)** — 15 corpus hits. 15 uses; likely adequate, needs a read not a build | Tier 4 | ⬜ |
| MR-39 | **Sclerostin inhibitors (romosozumab)** — 1 corpus hits. Specialist osteoporosis | Tier 4 | ⬜ |
| MR-40 | **PDE3 inhibitors (milrinone)** — 0 corpus hits. Zero hits. ICU inotrope an intern will see running | Tier 3 | ⬜ |
| MR-41 | **Direct arteriolar vasodilators (hydralazine, minoxidil)** — 6 corpus hits. 6 uses; hydralazine already appears in the hypertension and pre-eclampsia content | Tier 4 | ⬜ |
| MR-42 | **Potassium channel openers (nicorandil)** — 2 corpus hits. Second-line antianginal | Tier 4 | ⬜ |
| MR-43 | **Alpha-1 / central alpha-2 agonists** — 13 corpus hits. 13 uses; likely adequate | Tier 4 | ⬜ |
| MR-44 | **Bile acid sequestrants / ezetimibe** — 7 corpus hits. 7 uses; adequate for intern level | Tier 4 | ⬜ |
| MR-45 | **Erythropoiesis-stimulating agents** — 14 corpus hits. 14 uses; likely adequate | Tier 4 | ⬜ |
| MR-46 | **Polyclonal antibodies (ATG)** — 0 corpus hits. Transplant specialist | Tier 4 | ⬜ |
| MR-47 | **Alpha-glucosidase inhibitors (acarbose)** — 0 corpus hits. Rarely used in Australia | Tier 4 | ⬜ |
| P5-A32 | **MSK eponym fractures and lesions — Bennett's, Rolando, Lisfranc, Gamekeeper's thumb, Stener lesion, Hill-Sachs, Jefferson, Hangman.** All zero corpus hits, all confirmed by hand in the eponym audit, and **none was ever queued** — they were recorded as GAP in `scripts/judge_conditions.py` and never carried into the tracker. The corpus owns entries for Colles', Smith's, Barton's, Monteggia, Galeazzi and Boxer, so this is the asymmetric-set pattern: the eponyms it does teach make the missing ones look covered. Lisfranc is the highest-yield (classically missed on plain films); Bennett's and Gamekeeper's/Stener are common hand injuries with a surgical-referral decision. | RACGP; MSK examination and fracture texts | ⬜ |
| P5-E8 | **Anti-RNP** — 0 hits, completing the ENA panel the corpus half-teaches (ANA, anti-dsDNA, anti-Sm, anti-Ro all present). Anti-RNP is the MCTD marker. Asymmetric-set pattern. | RCPA; eTG Rheumatology | ⬜ |
| P5-E9 | **Deamidated gliadin peptides (DGP)** — 0 hits. Anti-tTG coeliac serology is covered; DGP is the second-line test that matters in **IgA deficiency**, where tTG is falsely negative. | RCPA; Coeliac Australia | ⬜ |
| P5-E10 | **Body plethysmography** — 0 hits. Spirometry is covered; plethysmography is what distinguishes restriction from obstruction on lung volumes. Lower yield. | Lung Foundation Australia | ⬜ |

> [!warning] **Transcription fidelity was never checked, and the first Part E pass was reported complete when it was not.**
> The pass reported "263 items, complete". The source list held **279**. Sixteen were lost in transcription —
> mostly items nested inside a parenthetical beside another test (**Troponin T** beside Troponin I,
> **DGP** beside anti-tTG, **plethysmography** inside the PFT bundle), plus five standalone microbiology
> organisms and two palliative instruments (**FAMCARE-P16**, **QUAL-E**).
>
> Nothing in the method compared the transcribed file against the source. Every enumeration this phase has
> run — 2,585 conditions, 276 AMH leaves, 254 spreadsheet classes, 94 presentation items — was transcribed
> the same way and **none had its fidelity checked**. This is a distinct failure from the naming-convention
> problems: those made present things look absent; this makes items vanish entirely, and a vanished item
> leaves no trace to notice.
>
> **Re-run result: 279 items — 21 own an entry, 98 in a taught section, 17 prose, 4 acronym-only, 139 absent.**
> Of the 16 recovered: Morbidity owns an entry; Anti-Ro, Mortality and home sleep testing sit in taught
> sections; Troponin T is mentioned; and three are genuine gaps (E8, E9, E10). The rest are out of scope —
> individual organism cultures, HHV-8 PCR, and two palliative research instruments.
