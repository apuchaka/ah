---
block: General Practice / Preventive Medicine / Ethics
source: built from scratch — CSV category "General Practice, Preventive Med, Ethics & Communication"; no equivalent existed in the source notes
---

> [!note] Why this file exists. The CSV category "General Practice, Preventive Med, Ethics & Communication" (29 rows) was found by Step 23 to be the **second-largest gap in this project**, and it was never "(NEW)"-tagged, which is why Step 21's first pass missed it. An audit of all 29 rows before building classified them as **7 adequately covered, 6 partially present, 16 genuinely absent** — not the "roughly half covered" previously assumed.
>
> **Placement rule applied to all 29 rows, in this order** — a new file was the last resort, not the default:
> 1. **Consultation skill → [[Communication]]** (the task-led station file): breaking bad news, DNACPR and goals of care, domestic and family violence, motivational interviewing, clinical handover, open disclosure, complaints, angry patients, professional boundaries, explaining a safeguarding referral.
> 2. **Clinical process / ethics / legal → [[Clinical-Process-EBM-Consent-Capacity]]**: documenting in the medical notes, mandatory reporting as a general duty.
> 3. **Preventive and screening *content* → the relevant organ-system file**, where it already lives and is already source-verified: bowel screening in [[03_Gastrointestinal]] Colorectal Cancer, cervical in [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening, cardiovascular risk in [[01_Cardiovascular]], diabetes risk in [[06_Metabolic_Medicine_and_Endocrinology]]. **This file does not restate any of it** — those entries remain authoritative.
> 4. **This file, only for what fits none of the above:** general practice as a discipline and preventive care as a *system* — the consolidating framework that no single organ file can hold, continuity of care, the features that distinguish general practice, hospital avoidance, and behavioural risk factors spanning all four SNAP domains. Same justification as the five orphan topics in [[18_Geriatrics_and_Older_Persons_Health]]: a genuine cluster that no existing file owns, not a convenient container.
>
> Rows confirmed already covered and deliberately **not** duplicated here: breaking bad news, discussing end-of-life care, polypharmacy (see [[18_Geriatrics_and_Older_Persons_Health]] Polypharmacy and Deprescribing), ICE (applied throughout [[History-Taking]]), fitness to drive (Austroads-verified across [[01_Cardiovascular]], [[04_Neurology]] and others), and palliative care (see [[10_11c_Oncology_-_Palliative_Care_Prescribing]]).

## Preventive Medicine and Screening in Australian General Practice

> [!note] Gap-filled from CSV ("Preventative medicine in General Practice including cancer screen, premature cardiovascular diseases, infections, diabetes, conditions occurring during pregnancy, genetic disorders, behavioural disorders, smoking cessation," High yield). Every *component* existed somewhere — cervical screening in [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening, cardiovascular risk in [[01_Cardiovascular]], diabetes risk in [[06_Metabolic_Medicine_and_Endocrinology]] — but **no entry consolidated them into a framework**, and nothing stated what preventive care an asymptomatic Australian adult should actually be offered and when. Built as an index and framework that routes to the existing disease entries rather than duplicating them. Verified against the RACGP *Guidelines for preventive activities in general practice* ("Red Book," 10th edition), the Australian Government's National Bowel Cancer Screening Program, BreastScreen Australia and National Cervical Screening Program, and the National Immunisation Program, Aug 2026.

> [!info] **The theory behind this entry lives elsewhere, deliberately.** *Why* a programme exists for bowel and cervical cancer but not for prostate or ovarian — the screening criteria, and the lead-time, length-time and overdiagnosis biases that make screening look better than it is — is built in [[Clinical-Process-EBM-Consent-Capacity]] Screening — Why a Programme Exists, and the Biases That Make Screening Look Better Than It Is. This entry stays the Australian *what and who*; that one is the *why*.

**The organising idea:** preventive activities apply to **asymptomatic people**, and are therefore justified differently from treatment — the intervention must do more good than harm in a population that currently feels well. That is why eligibility is defined by **age and risk band** rather than by symptoms, and why "more screening" is not automatically better.

**The three levels, because the CSV row spans all three:**
- **Primary** — prevent the disease occurring (immunisation, smoking cessation, physical activity).
- **Secondary** — detect it early in an asymptomatic person (the cancer screening programs, blood pressure and lipid measurement).
- **Tertiary** — limit the consequences of established disease (cardiac rehabilitation, diabetic foot surveillance).

### The three national cancer screening programs

These are population programs with defined eligibility, and an intern is expected to know who is invited and how often.

| Programme | Eligibility, in brief | Detail lives in |
|---|---|---|
| **National Bowel Cancer Screening** | 45–74; **50–74 automatically mailed a kit, 45–49 can request one**; iFOBT, 2-yearly | [[03_Gastrointestinal]] Colorectal Cancer |
| **BreastScreen Australia** | Women 50–74 invited; screening mammogram, 2-yearly | [[10_12_Oncology_-_Breast]] Breast cancer |
| **National Cervical Screening** | 25–74; **HPV test** first-line with **self-collection available to all**, 5-yearly, exit test at 70–74 | [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening |

> [!info] **The right-hand column is the source of truth, not this table.** Each of those entries is independently source-verified and carries the reasoning, the pathway after an abnormal result, and the equity detail. The table exists only to make the three programmes comparable side by side, which is the thing that had no home. Checked for internal consistency against each entry before writing (Step 12) — the bowel figures here match `03_Gastrointestinal` exactly, including the 1 July 2024 eligibility change.

> [!danger] The distinction that gets tested and gets missed clinically: **these programs are for asymptomatic people.** A symptomatic patient is investigated diagnostically, on their symptom, **irrespective of where they sit in the screening schedule** — a patient with rectal bleeding gets colonoscopy, not an iFOBT; a patient with abnormal vaginal bleeding gets a symptomatic co-test and further investigation regardless of when their last cervical screen was due (see [[17_02_Menorrhagia__PMS__Menopause__HRT]] Abnormal Uterine Bleeding — Approach and DDx, not repeated here). Using a screening test to investigate a symptom delays diagnosis and falsely reassures.

**Prostate and skin cancer are not population-screened in Australia**; both are shared-decision or risk-based, and offering routine PSA to an unselected asymptomatic man is not the Australian position.

> [!info] **Self-collection for cervical screening is the single most useful equity intervention in this whole area** — it more than doubled participation in under-screened groups, and it is available to every eligible person, not only those who decline a clinician-collected sample. Offer it, rather than waiting to be asked (already established in [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening).

### Cardiovascular, diabetes and kidney risk

- **Absolute cardiovascular risk** assessment — calculated risk over a defined period, rather than treating each risk factor in isolation. This is the reasoning behind the treatment thresholds in [[01_Cardiovascular]] 0.39 Dyslipidaemia and 0.2 Hypertension, not repeated here.
- **Type 2 diabetes** — **AUSDRISK** is the Australian risk tool, with the specific caveat already established in [[06_Metabolic_Medicine_and_Endocrinology]] that it is **not validated for Aboriginal and Torres Strait Islander people** and a different, earlier screening approach applies.
- **Chronic kidney disease** — risk-based screening (eGFR and urine ACR) in diabetes, hypertension and other risk groups, per [[07_Renal_Medicine_and_Urology]].
- **Osteoporosis and fracture prevention** — see [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis for the AU-specific DXA and treatment-initiation thresholds, and [[18_Geriatrics_and_Older_Persons_Health]] Falls in Older People for the other half of fracture prevention.

### Immunisation across the lifespan

The **National Immunisation Program (NIP)** provides funded vaccines. The **childhood schedule** is built in [[15_24b_Paeds_-_Screening__SIDS__Vaccination_Schedule]] Vaccination schedule (Australia — National Immunisation Program) and is not repeated here.

**Adult immunisation is the half that is easy to forget**, because it appears in this corpus only as one-line adjuncts inside disease entries (influenza and pneumococcal vaccination under heart failure and COPD):
- **Annual influenza** vaccination — funded for those ≥65, pregnant women, Aboriginal and Torres Strait Islander people, and people with specified medical risk conditions.
- **Pneumococcal** vaccination in older adults and in defined risk groups.
- **Herpes zoster (shingles)** vaccination in older adults.
- **COVID-19** boosters per current age- and risk-based guidance.
- **dTpa in every pregnancy**, and influenza in pregnancy — see [[16_01-05_Antenatal_Care]].
- **Aboriginal and Torres Strait Islander people are eligible earlier** for several NIP vaccines than the general population — a specific, actionable difference rather than a general statement about disparity.

> [!warning] Check current NIP eligibility rather than relying on a remembered age cut-off: funded age thresholds and the vaccines included have changed repeatedly, and this is a place where an out-of-date figure leads directly to a patient missing a funded vaccine.

### Other preventive domains named in the CSV row

- **Behavioural and lifestyle risk** — see Lifestyle Risk Factors (SNAP) and Smoking Cessation below.
- **Conditions occurring during pregnancy** — antenatal screening is built in [[16_01-05_Antenatal_Care]] (including Structural abnormality screening and Aneuploidy & screening), not repeated here.
- **Genetic disorders** — family-history-based risk assessment and referral, per [[10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes]].
- **Infections** — sexual health screening per [[08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs]], and blood-borne virus screening in risk groups.
- **Mental health** — note that **Australia does not recommend general population screening for depression**; the RACGP approach is opportunistic case-finding, an established point in [[14_01_Psych_-_Mood_Disorders__Depression__Suicide__Bipolar_]] that is a genuine AU-vs-UK difference.

> [!tip] The practical intern-level summary: know **who is invited to the three national cancer screening programs and how often**, know that a **symptomatic patient is investigated rather than screened**, know that **AUSDRISK is not validated for Aboriginal and Torres Strait Islander people**, and know that **adult immunisation exists** and needs checking against current NIP eligibility rather than memory.

---

## Lifestyle Risk Factors (SNAP) and Smoking Cessation

> [!warning] **Correction to this project's own record.** The workflow document's Step 23 findings list "smoking cessation/SNAP (appropriately scattered as a risk factor across many disease entries)" as **confirmed present**. That is wrong, and the error is instructive: *smoking cessation* is indeed mentioned across many entries, but **the SNAP framework itself appeared nowhere** — a corpus-wide search returns zero hits for the acronym as a framework (every match is "opening snap" or "snapping"). Being mentioned as a risk factor is not the same as being built as a topic, and the earlier pass conflated the two.

> [!note] Gap-filled from CSV ("Life Style related Diseases (SNAP)," Medium yield). Placed here rather than in an organ-system file because SNAP spans all four domains and belongs to none of them; the *brief-intervention conversation* itself is a communication skill and is cross-referenced to [[Communication]] Motivational Interviewing and the Stages of Change rather than duplicated. Verified against the RACGP *Smoking, nutrition, alcohol, physical activity (SNAP): a population health guide to behavioural risk factors in general practice*, Aug 2026.

**SNAP** is the Australian general-practice framework for the four behavioural risk factors that together account for most of the modifiable burden of chronic disease: **S**moking, **N**utrition, **A**lcohol, **P**hysical activity. They cluster — heavy smoking is commonly accompanied by poor nutrition, hazardous drinking and inactivity — so finding one is a reason to ask about the other three rather than to address it in isolation.

### The 5As — the structure for a brief intervention

| | | In practice |
|---|---|---|
| **Ask** | Identify and record the risk factor | Systematically, not opportunistically-if-remembered |
| **Assess** | Level of risk, **and readiness to change** | This is where the stages-of-change model does the work — see [[Communication]] Motivational Interviewing and the Stages of Change, not repeated here |
| **Advise** | Clear, personalised, non-judgemental advice to change | Personalised to *their* clinical situation beats generic advice |
| **Assist** | Help them act — goal setting, self-monitoring, pharmacotherapy | The step most often skipped after giving advice |
| **Arrange** | Referral and follow-up | Quitline, dietitian, exercise physiologist, alcohol services; and a review appointment |

> [!info] The 5As and the stages of change interlock: **Assess** determines *how much* of the rest of the sequence is useful today. A precontemplative patient gets Ask, Assess, Advise, and an open door — pushing Assist and Arrange on them wastes the consultation. Someone in preparation should get all five in one visit.

### Smoking — the highest-yield of the four

- **Ask about smoking status at every opportunity and record it.** Brief advice from a clinician measurably increases quit rates, and it takes under a minute.
- **Pharmacotherapy** roughly doubles quit rates over behavioural support alone: **nicotine replacement therapy** (combination therapy — a long-acting patch plus a short-acting form such as gum, lozenge, inhalator or spray for breakthrough cravings — is more effective than a patch alone), **varenicline**, and **bupropion**. Already named briefly in [[02_Respiratory]] under COPD; this is the fuller version.
- **Quitline (13 7848)** is the national behavioural-support service and is the concrete "Arrange" step. Multi-session behavioural support plus pharmacotherapy outperforms either alone.
- **Relapse is expected**, not a failure — most people make several attempts before sustained cessation, and a lapse should re-enter the cycle rather than end the conversation (see the Relapse row in [[Communication]] Motivational Interviewing and the Stages of Change).
- **Smoking is the dominant modifiable risk factor** across an enormous share of this project's content — see [[02_Respiratory]] COPD and Lung Cancer, [[01_Cardiovascular]], and [[10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers]] — which is exactly why it is worth having a method rather than a reflex to advise stopping.

> [!danger] **Aboriginal and Torres Strait Islander people — a disparity with a genuinely positive trajectory, which is unusual enough in this area to be worth stating accurately.** Daily smoking is **around 2.6 times** as likely as in the non-Indigenous population after age adjustment — but the direction of travel matters as much as the gap: daily smoking fell from **more than 1 in 3 adults in 2010 to about 1 in 5 in 2022–23**, one of the more substantial public health shifts in recent Australian data, supported by the **Tackling Indigenous Smoking** program. The clinical consequence is the opposite of fatalism: **quit attempts in this population succeed, and offering cessation support is worthwhile rather than futile** — the error to avoid is not offering it. Refer to an Aboriginal Community Controlled Health Organisation or a local Tackling Indigenous Smoking service alongside Quitline where the patient prefers. Verified against AIHW National Drug Strategy Household Survey 2022–23 and ABS smoking trend data, Aug 2026.

### Nutrition, alcohol and physical activity

- **Nutrition** — assess dietary pattern rather than individual nutrients; refer to a dietitian where there is an established condition (diabetes, CKD, coeliac disease, malnutrition in frailty — see [[18_Geriatrics_and_Older_Persons_Health]] Frailty for the protein-intake point specifically).
- **Alcohol** — screen with **AUDIT-C**, already established in [[14a-1_Psych_-_Substance_Misuse__Recreational_Drug_Profiles_]] Alcohol use disorder, which carries the dependence, withdrawal and pharmacotherapy content and is not repeated here. Brief intervention is effective in hazardous drinkers who are not dependent; **dependence is a different problem needing a different pathway**, and the important clinical step is distinguishing the two before advising someone to cut down (abrupt cessation in a dependent drinker risks withdrawal — see [[03_Gastrointestinal]] Alcohol withdrawal).
- **Physical activity** — ask about it specifically rather than inferring it; any increase from a low base carries benefit, and the framing that matters for an older or deconditioned patient is that **something beats nothing** (see [[18_Geriatrics_and_Older_Persons_Health]] Falls in Older People for the balance-challenging exercise dose specifically, which is a different and more demanding prescription than general activity advice).

> [!tip] What makes this a topic rather than a slogan: the four factors **cluster**, the **5As give a structure** so the consultation does not stop at "you should really quit", and **matching the intervention to readiness** determines whether any of it lands. An intern who can do Ask–Assess–Advise well, and knows that Assist means pharmacotherapy and Arrange means Quitline, is doing the useful part.

---

## Hospital Avoidance and Potentially Preventable Hospitalisations

> [!note] Gap-filled from CSV ("Hospital avoidance," Medium yield). Verified absent: the only corpus-wide hit was this file's own placement-rule line listing it as a row to build. Placed here rather than in a disease file because it is a **property of how care is organised** rather than of any one condition — the same test that put continuity of care in this file. Verified against the AIHW *Atlas of avoidable hospitalisations in Australia: ambulatory care-sensitive conditions* and Victorian and NSW health department ACSC work, Aug 2026.

**D:** an **ambulatory care-sensitive condition (ACSC)** is one for which hospitalisation is considered **potentially avoidable through timely and effective care in the community**. Admissions for these are counted as **potentially preventable hospitalisations**, and the rate is used in Australia as a health-system performance measure — which is why the term appears in service planning as well as clinically.

> [!info] **The concept is a measure of the *system*, not a judgement about the patient or the admitting doctor — and this distinction matters clinically.** A "potentially preventable" admission does not mean the admission was wrong at the point it happened. It means that somewhere upstream — access, follow-up, medication supply, education, or a review that did not occur — there was a modifiable opportunity. **Admitting a patient who needs admitting is always correct**; the question the measure asks is what happened in the weeks before.

**The conditions this applies to** fall into three groups:
- **Chronic** — diabetes complications, COPD, congestive heart failure, angina, hypertension, asthma. These dominate the numbers, and the modifiable factor is usually **continuity, medication access and early review** (see Continuity of Care, and What Makes General Practice Different below).
- **Acute** — urinary tract and other infections, dehydration, cellulitis: conditions where earlier community treatment could have prevented deterioration.
- **Vaccine-preventable** — influenza, pneumococcal disease (see Preventive Medicine and Screening in Australian General Practice above, not repeated here).

### What an intern can actually do

The temptation is to read this as policy. It is not — several of the levers sit with the person doing the discharge:

- **Ask why this admission happened now**, not only what to treat. Ran out of medicine? Could not get a GP appointment? Did not understand the sick-day plan? Nobody at home? Each has a different fix, and none is addressed by treating the presenting problem alone.
- **Make the discharge do the preventive work** — accurate medication list, a follow-up appointment that actually exists, a written action plan for the chronic condition, and a discharge summary the GP receives promptly. This is the single largest lever an inpatient team holds (see [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment, not repeated here).
- **Know the alternatives to admission** your service has: **Hospital in the Home (HITH)** for conditions treatable with community-delivered IV therapy or monitoring, ambulatory or rapid-access clinics, outreach and post-acute services, and — for older patients — the aged care pathways in [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment.
- **In residential aged care**, transfer decisions turn on whether the facility can deliver the care and on the resident's **advance care directive and ceiling of care** — an admission that contradicts a documented plan is a failure of communication rather than of medicine (see [[Communication]] Goals of Care and Ceiling of Care (Treatment Escalation Planning)).

> [!danger] **Aboriginal and Torres Strait Islander Australians experience substantially higher rates of potentially preventable hospitalisation**, including frequent avoidable admissions for chronic conditions — and the drivers identified in Australian research are **access and continuity**, not disease severity alone. The clinical consequence sits with the discharging team: **the generic discharge plan is the one most likely to fail here.** Ask specifically whether the patient can get the medicine (see [[Clinical-Process-EBM-Consent-Capacity]] Choosing a Medicine — Quality Use of Medicines for the Closing the Gap PBS Co-payment Program, not repeated here), whether follow-up is with a service they will actually attend — an **Aboriginal Community Controlled Health Organisation** may be that service — and whether the discharge summary is going to the clinician who will see them. Verified against Australian cohort research on frequent avoidable admissions among Aboriginal people with chronic conditions in NSW, Aug 2026.

---

## Continuity of Care, and What Makes General Practice Different

> [!note] Gap-filled from CSV ("Continuity of care," High yield, and "Unique features of General practice," Medium — built together because the second is largely an explanation of why the first matters). Genuinely absent: **zero corpus-wide hits** for "continuity of care". Placed here rather than in [[Communication]] because this is a property of the *system and the therapeutic relationship over time*, not a consultation skill performed within a single station. Verified against RACGP position and advocacy material on the role of specialist GPs and continuity, the MJA analysis of patient enrolment and continuity in Australian general practice, and RACGP-reported NSW Health linked-data findings on post-discharge follow-up, Aug 2026.

**D:** the extent to which a patient experiences care as **connected and coherent over time**. Conventionally three components, which are genuinely different things and can come apart:
- **Relational** — seeing the *same clinician* over time, so accumulated knowledge of the person does not have to be rebuilt each visit.
- **Informational** — the *record* travels even when the clinician changes: results, medication changes, what has already been tried and failed.
- **Management** — different clinicians deliver a *consistent plan* rather than contradicting one another.

> [!info] Why the distinction matters practically: a patient can have excellent informational continuity (a complete shared record) and no relational continuity at all, and the two are not interchangeable. A locum with the full notes still does not know that this patient always minimises symptoms, or that the last three presentations were really about a deteriorating home situation.

**The evidence — this is not merely a nice principle:** continuity of care is associated with **greater patient satisfaction and better chronic disease self-management, fewer hospitalisations, and lower mortality**. An Australian-specific finding worth knowing: linked NSW Health and general practice data show patients **promptly followed up by their GP after a hospital admission are substantially less likely to be readmitted**, and aged care residents who keep seeing their regular GP after entering a facility have around **8% fewer emergency department presentations**.

> [!tip] The direct implication for an intern working in hospital, which is where this content is most immediately actionable: **the discharge summary and the follow-up appointment are the continuity mechanism.** They are not paperwork — they are the intervention that connects the admission to the rest of the patient's care, and the evidence above is the reason they matter (see [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment for how to do them well, and [[Communication]] Clinical Handover (ISBAR) and Prioritisation of Jobs for the in-hospital equivalent).

**Australian context:** patient enrolment with a single practice has historically **not** been a feature of Australian general practice, unlike several comparable systems — patients may attend multiple practices, which fragments both relational and informational continuity. Voluntary registration arrangements have been introduced to address this. Check current arrangements rather than relying on this description, as the policy is actively changing.

### What actually distinguishes general practice as a discipline

Worth understanding because it explains why GP reasoning differs from hospital reasoning, and why an intern rotating into general practice finds their hospital habits do not transfer cleanly:

- **Undifferentiated presentations.** Patients arrive with symptoms, not diagnoses, and often very early in the illness when discriminating features have not yet appeared. Much of the skill is tolerating diagnostic uncertainty safely rather than resolving it immediately.
- **Very different pre-test probabilities.** The same symptom carries a far lower probability of serious disease in general practice than in an emergency department, because the population is different. **A test with good characteristics in a hospital population performs much worse in a low-prevalence one**, generating more false positives than true — which is why reflexively investigating everything is not the safer option it appears to be (see [[Clinical-Process-EBM-Consent-Capacity]] Evidence-based medicine — a brief note).
- **Time as a diagnostic tool.** Reviewing in a defined interval — "watchful waiting" with an explicit plan — is a legitimate and often superior strategy to immediate investigation, provided the safety net is real.
- **Safety-netting is the core skill this depends on.** Tell the patient specifically **what should improve and by when, what would mean they need to be seen sooner, and exactly how to get seen**. Vague advice to "come back if it gets worse" is not a safety net.
- **Whole-person and longitudinal care** — comorbidity, family and social context, and the same clinician seeing the consequences of their own decisions over years, which is a genuinely different accountability from an episode of hospital care.
- **The gatekeeping and coordinating role** — managing the interface with specialist services rather than being one, and holding the whole picture when several specialists each hold part of it (see [[Communication]] Management of Patients with Multiple Chronic Medical Problems).
