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
