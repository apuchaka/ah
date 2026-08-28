---
block: General Practice / Preventive Medicine / Ethics
source: built from scratch — CSV category "General Practice, Preventive Med, Ethics & Communication"; no equivalent existed in the source notes
---

> [!note] Why this file exists. The CSV category "General Practice, Preventive Med, Ethics & Communication" (29 rows) was found by Step 23 to be the **second-largest gap in this project**, and it was never "(NEW)"-tagged, which is why Step 21's first pass missed it. An audit of all 29 rows before building classified them as **7 adequately covered, 6 partially present, 16 genuinely absent** — not the "roughly half covered" previously assumed.
>
> The **consultation-skill** rows live in [[Communication]], which is the task-led communication station file: breaking bad news, DNACPR and goals of care, domestic and family violence, motivational interviewing, and clinical handover. This file holds the rows that are about **general practice as a discipline and preventive care as a system** — which no organ-system file owns, and which is why they had no home.
>
> Rows confirmed already covered and deliberately **not** duplicated here: breaking bad news, discussing end-of-life care, polypharmacy (see [[18_Geriatrics_and_Older_Persons_Health]] Polypharmacy and Deprescribing), ICE (applied throughout [[History-Taking]]), fitness to drive (Austroads-verified across [[01_Cardiovascular]], [[04_Neurology]] and others), and palliative care (see [[10_11c_Oncology_-_Palliative_Care_Prescribing]]).

## Preventive Medicine and Screening in Australian General Practice

> [!note] Gap-filled from CSV ("Preventative medicine in General Practice including cancer screen, premature cardiovascular diseases, infections, diabetes, conditions occurring during pregnancy, genetic disorders, behavioural disorders, smoking cessation," High yield). Every *component* existed somewhere — cervical screening in [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening, cardiovascular risk in [[01_Cardiovascular]], diabetes risk in [[06_Metabolic_Medicine_and_Endocrinology]] — but **no entry consolidated them into a framework**, and nothing stated what preventive care an asymptomatic Australian adult should actually be offered and when. Built as an index and framework that routes to the existing disease entries rather than duplicating them. Verified against the RACGP *Guidelines for preventive activities in general practice* ("Red Book," 10th edition), the Australian Government's National Bowel Cancer Screening Program, BreastScreen Australia and National Cervical Screening Program, and the National Immunisation Program, Aug 2026.

**The organising idea:** preventive activities apply to **asymptomatic people**, and are therefore justified differently from treatment — the intervention must do more good than harm in a population that currently feels well. That is why eligibility is defined by **age and risk band** rather than by symptoms, and why "more screening" is not automatically better.

**The three levels, because the CSV row spans all three:**
- **Primary** — prevent the disease occurring (immunisation, smoking cessation, physical activity).
- **Secondary** — detect it early in an asymptomatic person (the cancer screening programs, blood pressure and lipid measurement).
- **Tertiary** — limit the consequences of established disease (cardiac rehabilitation, diabetic foot surveillance).

### The three national cancer screening programs

These are population programs with defined eligibility, and an intern is expected to know who is invited and how often.

| Programme | Who | Test | Interval |
|---|---|---|---|
| **National Bowel Cancer Screening** | 50–74 invited automatically; **45–49 can request a kit** | Immunochemical faecal occult blood test (iFOBT), done at home | 2-yearly |
| **BreastScreen Australia** | Women 50–74 invited | Screening mammogram | 2-yearly |
| **National Cervical Screening** | 25–74 | **HPV test** (not cytology first-line), with **self-collection available to all eligible participants** | 5-yearly |

> [!danger] The distinction that gets tested and gets missed clinically: **these programs are for asymptomatic people.** A symptomatic patient is investigated diagnostically, on their symptom, **irrespective of where they sit in the screening schedule** — a patient with rectal bleeding gets colonoscopy, not an iFOBT; a patient with abnormal vaginal bleeding gets a symptomatic co-test and further investigation regardless of when their last cervical screen was due (see [[17_02_Menorrhagia__PMS__Menopause__HRT]] Abnormal Uterine Bleeding — Approach and DDx, not repeated here). Using a screening test to investigate a symptom delays diagnosis and falsely reassures.

**Where the disease-level content lives:** [[03_Gastrointestinal]] Colorectal Cancer, [[10_12_Oncology_-_Breast]] Breast cancer, [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer — not repeated here. **Prostate and skin cancer are not population-screened in Australia**; both are shared-decision or risk-based, and offering routine PSA to an unselected asymptomatic man is not the Australian position.

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
