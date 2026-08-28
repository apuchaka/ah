---
block: Older Persons Health / Geriatrics
source: built from scratch — CSV category "Older Persons Health / Geriatrics (NEW)"; no equivalent existed in the source notes, which is why this whole category was absent until now
---

> [!note] Why this file exists. The CSV category "Older Persons Health / Geriatrics (NEW)" had **no corresponding file at all** — the single largest gap found in this project (Step 21). An audit of its 11 rows before building found that three were already adequately covered elsewhere and are deliberately **not** duplicated here: capacity assessment (see [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework), the cognitive screening tools themselves (see [[Investigation-Interpretation]] Cognitive Screening Tools (MMSE, MoCA, AMTS)), and osteoporosis management (see [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis, which is verified against the 2024 RACGP/Healthy Bones Australia guideline). Two further rows were built into [[04_Neurology]] rather than here, because their structural anchors already live there.
>
> This file holds the topics that no organ system owns — which is precisely why they had no home before.

## Falls in Older People

> [!note] Gap-filled from CSV ("Fall (recurrent falls)," High yield, and the falls-prevention half of "Osteopenia/osteoporosis management & falls-related fracture prevention"). Genuinely absent as clinical content: falls appeared only as a history-taking checklist bullet in [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls), which is an OSCE communication framework rather than an assessment or management approach. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Part A "Falls", the Australian Commission on Safety and Quality in Health Care falls guidelines for community care, the Cochrane review of exercise for preventing falls (Sherrington et al.), and the Exercise & Sports Science Australia position statement on exercise for falls prevention, Aug 2026.

**D:** an event resulting in a person unintentionally coming to rest on the ground or a lower level. **Roughly one third of community-dwelling people aged over 65 fall each year**, and the proportion rises with age and in residential aged care.

> [!danger] The single most important framing: a fall is a **symptom, not a diagnosis**. "Mechanical fall" is not a diagnosis either, and writing it in the notes closes an assessment that should be opening one. The cause is **multifactorial in most older fallers** — typically several modest contributors acting together rather than one dramatic cause — which is why single-intervention approaches underperform and why a multidisciplinary response is the standard.

### Distinguishing a fall from a collapse — do this first

The first branch point is whether consciousness was lost, because it splits the work-up entirely:

- **Transient loss of consciousness** → this is a *collapse*, and the differential is syncope vs seizure vs hypoglycaemia. Take that pathway instead: see [[History-Taking]] Collapse (Conscious and Unconscious) for the structured before/during/after history and [[04_Neurology]] Syncope for the differential, not repeated here.
- **No loss of consciousness** → this is a fall, and the multifactorial assessment below applies.

**In practice the distinction is often genuinely unclear**, because amnesia for the event is common in older people and there may be no witness. Where you cannot confidently exclude loss of consciousness, screen for the dangerous syncopal causes (postural blood pressure, cardiac examination, ECG) *as well as* running the falls assessment — do not simply pick one branch on the balance of probabilities.

### Risk factors — the ones worth actually asking about

**Intrinsic:**
- **Previous falls** — the strongest single predictor. A fall in the past year should trigger the full assessment.
- **Impaired balance and gait**, and **reduced lower-limb muscle strength** (sarcopenia) — the two most consistently identified modifiable contributors.
- **Visual impairment** — cataract, uncorrected refractive error, and specifically **multifocal/bifocal spectacles**, which blur the lower visual field exactly where the ground and steps are (see [[05_Ophthalmology]] Cataracts).
- **Cognitive impairment and delirium** — impaired judgement of hazards and, in delirium, fluctuating attention (see [[04_Neurology]] Dementias and [[04_Neurology]] Delirium).
- **Postural (orthostatic) hypotension** — common, frequently drug-related, and readily missed if the blood pressure is only ever taken sitting.
- **Peripheral neuropathy** — loss of proprioceptive input (see [[04_Neurology]] Diabetic Neuropathy for the commonest cause and its glove-and-stocking distribution, not repeated here).
- **Continence problems** — urgency and nocturia drive hurried, poorly-lit trips to the toilet.
- **Foot problems and inappropriate footwear** — pain, deformity, and loose or backless shoes.
- **Fear of falling** — a genuine risk factor in its own right, not merely a consequence: it drives activity avoidance, which causes deconditioning and further weakness, which raises fall risk again. Ask about it explicitly, because patients rarely volunteer it.

**Extrinsic (environmental):** loose rugs and trailing cords, poor lighting (particularly on stairs and the route to the toilet at night), absent grab rails in the bathroom, cluttered walkways, unfamiliar surroundings, pets.

> [!warning] Fall-risk-increasing drugs (FRIDs) — review these specifically, by name, rather than glancing at the list
> **Psychotropics are the highest-yield target**: benzodiazepines and Z-drugs, antipsychotics, antidepressants (including SSRIs), and anticonvulsants. Also **cardiovascular agents**: antihypertensives of all classes, diuretics, nitrates, alpha-blockers, digoxin and antiarrhythmics. Also **opioids**, **anticholinergics** (including bladder antimuscarinics, sedating antihistamines, and tricyclics), and **hypoglycaemic agents** (insulin, sulfonylureas).
>
> This matters more than it first appears: **withdrawal of psychotropic medication produced the largest effect of any single falls-prevention intervention in randomised trials** — but the same trial evidence shows sustained withdrawal is genuinely hard to achieve in practice, so this is a deprescribing project with follow-up, not a one-off stop order. See Polypharmacy and Deprescribing below.

### Assessment — the multifactorial falls risk assessment

**Screening:** ask every older patient about falls in the past 12 months, and about unsteadiness or fear of falling. Two or more falls in a year, one fall with injury, or reported gait/balance difficulty all warrant the full multifactorial assessment.

**History:** the circumstances of each fall (what they were doing, indoors/outdoors, time of day, footwear, any prodrome), whether consciousness was lost, whether they could get up unaided and how long they were down, injuries sustained, and **fear of falling and consequent activity restriction**. Collateral history where cognition is impaired.

> [!tip] "Have you had any falls?" under-detects, because many older people do not classify a stumble or a slide to the floor as a fall, and some minimise it for fear of losing independence. Ask instead: *"Have you had any slips, trips or falls, including ones where you didn't hurt yourself?"* — and follow up with *"Have you been more unsteady on your feet?"*

**Examination:**
- **Lying and standing blood pressure** — measured supine after 5 minutes, then at 1 **and** 3 minutes standing. A sustained drop of **≥20 mmHg systolic or ≥10 mmHg diastolic** defines orthostatic hypotension. This is the highest-yield bedside test in a faller and is very commonly omitted. **Both timings matter, and the reason is derivable rather than arbitrary:** the immediate drop on standing is normally corrected within seconds by the baroreflex, so a reading at 1 minute captures failure of that reflex — while **delayed orthostatic hypotension**, where compensation succeeds initially and then fails, is missed entirely by a single early reading. Measuring from *sitting* rather than lying under-detects both, because the postural change is smaller and the venous pooling less.
- **Gait and balance**, observed directly. The **Timed Up and Go (TUG)** is the standard bedside tool: time the patient rising from a standard chair, walking 3 metres, turning, returning and sitting down. **Longer than about 10–12 seconds identifies community-dwelling older adults more likely to fall** and should prompt physiotherapy referral. Watch *how* they do it, not just the clock — hesitancy, a wide base, multiple steps to turn, or reaching for furniture are all informative.
- **Cardiovascular:** heart rate and rhythm, murmurs (aortic stenosis as a syncopal cause).
- **Neurological:** lower-limb power and tone, proprioception and vibration sense, cerebellar signs, and features of parkinsonism.
- **Vision** — acuity, and specifically ask whether they wear multifocals when walking outdoors or on stairs.
- **Feet and footwear** — inspect both, including the shoes they actually walk in at home.
- **Cognitive screen** where not already known (see [[Investigation-Interpretation]] Cognitive Screening Tools (MMSE, MoCA, AMTS)).

**Ix:** directed by the assessment rather than a reflex panel. FBC (*why:* anaemia contributes to postural symptoms and fatigue; *what:* low Hb), U&Es (*why:* dehydration and electrolyte disturbance both cause postural hypotension and confusion, and diuretics are a common contributor; *what:* raised urea/creatinine, hyponatraemia), blood glucose (*why:* hypoglycaemia is a reversible cause of falls and of apparent confusion in patients on insulin or sulfonylureas; *what:* low BGL), **vitamin D and calcium** (*why:* deficiency contributes to myopathy and to fracture risk, and identifies who benefits from supplementation; *what:* low 25-OH vitamin D), and **ECG** (*why:* screens for bradyarrhythmia, heart block, and prolonged QT as syncopal causes that a purely "mechanical" framing would miss; *what:* conduction abnormality, arrhythmia). **Imaging only where injury is suspected clinically** — a CT head is indicated for a head strike with anticoagulation, reduced consciousness, or focal neurology, not routinely after every fall.

### Mx — what actually works

- **Immediate/acute:** treat injuries (a high index of suspicion for occult hip fracture — see [[11_04_Ortho_-_Hip]] Hip / neck of femur (NOF) fractures — and for subdural haematoma in an anticoagulated patient with a head strike, where presentation can be delayed by days to weeks); assess for and treat the acute precipitant (infection, delirium, dehydration, new medication); and check for a **long lie**, which carries genuine risk of rhabdomyolysis, pressure injury, hypothermia and AKI, and which independently signals that the person cannot summon help.
- **Definitive — the interventions with real evidence:**
  - **Exercise is the single most effective intervention.** The dose and type matter and are frequently prescribed too vaguely: it must **challenge balance**, and the evidence favours a total of **3 or more hours per week, sustained**. Programmes meeting those criteria reduce falls substantially more than the ~25% average effect seen across community exercise programmes generally. Refer to physiotherapy or an accredited exercise physiologist rather than advising "keep active".
  - **Medication review and deprescribing**, targeting the FRIDs above and psychotropics first — see Polypharmacy and Deprescribing below.
  - **Home hazard assessment and modification by an occupational therapist** — most effective in those at higher risk, and more effective when the OT visits the home rather than working from a checklist in clinic.
  - **Vision** — cataract surgery where indicated, updating refraction, and advising **single-vision distance glasses for walking outdoors and on stairs** in multifocal wearers.
  - **Vitamin D** — supplement where deficient. Note the evidence is dose- and setting-dependent: higher-dose supplementation (≥700 IU/day) shows benefit while low-dose does not, and the case is stronger in residential aged care than in vitamin-D-replete community dwellers. **Do not give it routinely to everyone regardless of status.**
  - **Footwear** — well-fitting, low-heeled, thin firm soles, and fastened; treat foot pain and refer to podiatry.
  - **Postural hypotension** — reduce or withdraw the contributing drug first, ensure adequate hydration, advise rising slowly in stages, and consider compression stockings; drug treatment (e.g. fludrocortisone, midodrine) is specialist-initiated and a later step.
- **Chronic/long-term:**
  - **Fracture prevention runs alongside falls prevention, and neither substitutes for the other** — a faller with osteoporosis needs both. Assess bone health and treat per [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis (not repeated here), which carries the AU-specific DXA and treatment-initiation thresholds.
  - Address **fear of falling** directly — it responds to supervised exercise and graded activity, and is a common reason a technically excellent plan achieves nothing.
  - **A personal alarm or similar means of summoning help**, which changes the consequence of a fall even when it cannot prevent one.
  - Referral pathways: falls clinic, geriatrician, community physiotherapy/OT, and an **Aged Care Assessment Team (ACAT)** assessment where support needs have changed — see Discharge Planning and Home Safety Assessment below.

> [!danger] **Aboriginal and Torres Strait Islander people — the age threshold is the actionable point, and getting it wrong delays care by 15 years.** Falls, dementia, pain and urinary incontinence all occur at **younger ages** than in the non-Indigenous population, and the health and aged care systems reflect this: **Aboriginal and Torres Strait Islander people are eligible for aged care assessment and services from age 50, not 65.** Practically, this means a 55-year-old Aboriginal patient presenting with recurrent falls warrants the **full multifactorial assessment and an ACAT referral** — not the reassurance that they are "too young" for a falls work-up, which is the error this threshold exists to prevent. Aboriginal and Torres Strait Islander Aged Care Assessment Organisations exist specifically to provide this assessment in a culturally safe way. Verified against the Australian Government's Aboriginal and Torres Strait Islander aged care eligibility criteria and the RACGP Silver Book chapter on older Aboriginal and Torres Strait Islander people, Aug 2026.

> [!danger] **The same age-50 threshold applies to a second, separate population: people who are homeless or at risk of homelessness.** Aged care eligibility is **65 by default, and 50 both for Aboriginal and Torres Strait Islander people and for people who are homeless or at risk of homelessness** — two distinct groups reaching the same threshold, and worth holding separately rather than merging, since the reasons and the clinical picture differ. What they share is the reason the rule exists: **age-related conditions occur earlier relative to chronological age**, so a threshold set at 65 systematically excludes people who already have the problems it was written for.
> Practically, a **55-year-old who is sleeping rough or in insecure housing and presenting with falls, cognitive change or functional decline is within scope for an aged care assessment** — and the reflex that they are decades too young is the same error as in the box above, in a different guise. This population is also disproportionately likely to present through the emergency department rather than general practice, so the hospital admission may be the only opportunity anyone gets to make the referral. Verified against My Aged Care (Australian Government), Aug 2026.

> [!info] The intervention hierarchy, if you remember nothing else: **balance-challenging exercise at adequate dose, deprescribe the FRIDs, and fix the home and the glasses.** Those three carry most of the evidence. Vitamin D matters where the patient is deficient, and much less where they are not.

---

## Frailty

> [!note] Gap-filled from CSV ("Frailty phenotype / frailty assessment," High yield). Genuinely absent: the word appeared three times in the whole corpus, each time as a passing modifier on some other topic (an ECOG caveat in oncology, a relaxed HbA1c target in diabetes, a bladder-drug caution) — never as a concept with a definition, an assessment method, or management. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Part A "Frailty", the Australian Consensus Statement on the Prevention and Management of Frailty Among Community-Dwelling Older Adults (MJA, modified Delphi), and the AJGP review of sarcopenia in general practice, Aug 2026.

**D:** a state of **reduced physiological reserve across multiple organ systems**, producing disproportionate vulnerability to decompensation after a stressor that a non-frail person of the same age would absorb without consequence.

> [!info] The clinical signature, which is what makes frailty a useful concept rather than a synonym for "old": **the response is out of proportion to the insult.** The same urinary tract infection produces mild dysuria in a fit 80-year-old and, in a frail one, a fall, delirium, incontinence, immobility and an admission — with function often not returning to baseline afterwards. That non-linear response, and the incomplete recovery, is frailty. It is the reason a frail patient's presenting complaint is so often one of the geriatric syndromes (falls, delirium, immobility, incontinence) rather than the organ-specific symptom of the actual illness.

**Frailty is not the same as any of the things it is routinely confused with:**
- **Not age.** Many 90-year-olds are not frail; some 65-year-olds are.
- **Not multimorbidity.** They overlap and each raises the risk of the other, but a patient can carry several well-controlled chronic diseases with intact reserve, and a patient with few diagnoses can be profoundly frail.
- **Not disability.** Disability is established loss of function; frailty is the vulnerability that predicts *future* loss. A frail person may currently be fully independent — which is exactly when intervention has the most to offer.

### Assessment — two different models, used for different jobs

**1. The frailty phenotype (Fried) — a physical, criteria-based definition.** Five components:
1. Unintentional weight loss
2. Self-reported exhaustion
3. Low physical activity
4. Slow walking speed
5. Weak grip strength

**Three or more = frail; one or two = pre-frail; none = robust.** The *pre-frail* category is the practically important one — it identifies the patient in whom the trajectory is still readily modifiable.

**2. The Clinical Frailty Scale (Rockwood) — a judgement-based 9-point scale**, running from *very fit* through to *terminally ill*, and derived from the accumulated-deficits model, which counts deficits across physical, cognitive and psychosocial domains rather than physical criteria alone. Fast enough to apply at the bedside or on admission, which is why it is the one most often seen in hospital practice and in escalation and perioperative decisions.

Both are validated and both predict mortality; they are not interchangeable, and they answer different questions. The phenotype asks *"is this patient physically frail, and can I target the components?"*; the CFS asks *"how much reserve does this patient have, and what does that mean for the decision in front of me?"*

**Australian guidance is to assess frailty annually in older patients using a validated tool** — the specific tool matters less than doing it systematically rather than by impression.

**Sarcopenia** — the age-related loss of skeletal muscle mass, strength and function — is the muscle-specific core of physical frailty, and is what the exercise and protein interventions below are actually targeting.

### Why it changes management, not just prognosis

Frailty should alter clinical decisions rather than merely describe the patient:
- **Treatment targets loosen.** Tighter is not better in frailty — see the relaxed HbA1c targets in frail older patients in [[06_Metabolic_Medicine_and_Endocrinology]], and weigh the falls and postural-hypotension cost of intensive blood-pressure lowering against its benefit.
- **Fitness for intervention.** Frailty predicts postoperative complications and chemotherapy toxicity better than age or performance status alone — note the explicit acknowledgement in [[10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers]] ECOG Performance Status that ECOG is a broad functional snapshot rather than a frailty assessment.
- **Falls and fracture risk rise together** — see Falls in Older People above and [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis.
- **Delirium risk rises sharply**, which is why reduced physiological reserve appears as the first half of the delirium equation in [[04_Neurology]] Delirium.
- **Goals of care conversations become timely**, not premature — see [[Communication]] Discussing "Do Not Attempt Cardiopulmonary Resuscitation" (DNACPR / Not-for-Resuscitation) for that conversation, and [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework for the capacity question that underlies it.

### Mx — the central message is that frailty is modifiable

> [!danger] **Frailty is not an inevitable consequence of ageing, and identifying it is not a reason for therapeutic nihilism.** Its main drivers — sarcopenia, undernutrition, physical inactivity, uncontrolled chronic disease and polypharmacy — are all modifiable, and pre-frailty in particular can be reversed. Recording "frail" and doing nothing is a clinical failure, not a diagnosis.

- **Immediate/acute:** in an acute presentation, expect an atypical one, hunt for the geriatric syndrome masking the illness, and avoid the iatrogenic harms that frail inpatients are most susceptible to — deconditioning from bed rest, delirium, pressure injury, and new medications.
- **Definitive — the interventions with evidence:**
  - **Exercise, progressive and individualised, combining resistance, aerobic, and balance/functional training**, tailored to frailty level and professionally supervised. **The resistance component is essential** and is the part most often left out when a patient is simply told to "stay active".
  - **Nutrition — an individualised, protein-rich diet**, with active identification and treatment of protein–energy malnutrition and specific deficiencies. Early dietitian involvement.
  - **Deprescribing** — see Polypharmacy and Deprescribing below.
  - **Optimise contributing chronic disease**, and correct sensory impairment (vision, hearing), which drives inactivity and social withdrawal.
  - **Early physiotherapist and dietitian involvement** is specifically recommended rather than reserved for failure of advice alone.
> [!danger] **Aboriginal and Torres Strait Islander people — frailty presents earlier, and the assessment age must move with it.** Age-related conditions occur at younger ages, and aged care eligibility begins at **50 rather than 65** — as it does for people who are homeless or at risk of homelessness, in whom frailty likewise presents early (see the equity boxes under Falls in Older People above, not repeated here). The practical consequence for this entry specifically: **do not use 65 as the trigger for frailty assessment**, and do not read a frailty phenotype or Clinical Frailty Scale score in a 55-year-old Aboriginal patient as implausible for their age. Applying an unadjusted age threshold is the mechanism by which this disparity is perpetuated in individual consultations.

- **Chronic/long-term:** **Comprehensive Geriatric Assessment** — the multidimensional, multidisciplinary assessment (medical, functional, cognitive, psychological, social, environmental) with a coordinated plan, which is the structure that ties together everything in this file. Address social isolation, arrange appropriate community supports, and reassess frailty status annually to track the trajectory rather than assuming it only goes one way.

---

## Polypharmacy and Deprescribing

> [!note] Gap-filled from CSV ("Polypharmacy review / deprescribing in the elderly," High yield). Genuinely absent as content: polypharmacy appeared only as checklist bullets inside [[Communication]] Management of Patients with Multiple Chronic Medical Problems and [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls) — "review for sedating, anticholinergic, and hypotension-causing medications" — with no method for actually doing it, and no mention of Beers, STOPP/START, the prescribing cascade, or tapering anywhere in the corpus. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Parts A "Polypharmacy" and "Deprescribing", and the *Deprescribing in Older People: A Clinical Practice Guideline* summary (MJA, 2026), Aug 2026.

**D:** **polypharmacy** is conventionally defined as the regular use of **five or more medicines**, though the number matters far less than whether each medicine still has a valid indication and a favourable benefit-to-harm balance for *this* patient now. **Deprescribing** is the planned, supervised withdrawal of a medicine that is no longer appropriate, done as a positive clinical act rather than as an omission.

> [!info] The framing that makes this a clinical skill rather than an administrative tidy-up: **deprescribing is part of the prescribing continuum, not the opposite of prescribing.** Most treatment guidelines say when to start a medicine and are silent on when to stop it, so medicines accumulate by default — each one started for a good reason at the time, none ever formally reviewed for whether that reason still holds. This is the 2026 Australian guideline's central point, and it explains why polypharmacy develops in patients whose every individual prescribing decision was defensible.

**Why it matters:** each additional medicine raises the risk of adverse drug events, drug–drug and drug–disease interactions, falls (see Falls in Older People above), delirium (see [[04_Neurology]] Delirium), cognitive impairment, non-adherence, and hospital admission. In an older person with reduced renal and hepatic clearance and reduced physiological reserve (see Frailty above), the dose–harm relationship is shifted relative to a younger patient on the same regimen.

> [!danger] **The prescribing cascade** — the single most important pattern to recognise, because it is invisible unless you look for it. An adverse effect of one drug is misinterpreted as a new medical condition, and a second drug is prescribed to treat it. Classic examples:
> - **Metoclopramide or an antipsychotic → drug-induced parkinsonism → levodopa** (see [[04_Neurology]] Parkinson's Disease (PD), where drug-induced parkinsonism is already noted as a differential).
> - **Calcium channel blocker → ankle oedema → a diuretic** (which then causes postural hypotension and falls).
> - **Anticholinergic → confusion or urinary retention → a cholinesterase inhibitor or a catheter.**
> - **NSAID → hypertension or dyspepsia → an antihypertensive or a PPI** (see [[03_Gastrointestinal]] Peptic Ulcer Disease).
>
> The diagnostic question that breaks the cascade: **"could this new symptom be a side effect of an existing medicine?"** — asked *before* reaching for a new prescription.

### Anticholinergic burden — specifically worth knowing in Australia

Anticholinergic effects are **cumulative across drugs**, so a patient can carry a substantial burden from several individually-innocuous medicines with no single obvious culprit. Contributors include bladder antimuscarinics, sedating antihistamines, tricyclic antidepressants, some antipsychotics, antispasmodics and antiemetics. The consequences in an older person are precisely the ones easily attributed to ageing or dementia instead: confusion, memory impairment, falls, constipation, urinary retention, dry mouth, blurred vision.

This is not a marginal issue in Australian practice — **roughly 20–34% of older Australians use at least one medicine with anticholinergic effects**, and these drugs remain widely prescribed despite being flagged as potentially inappropriate by both the criteria sets below.

### Tools for identifying potentially inappropriate medicines

- **Beers Criteria** (American Geriatrics Society) — a list of medicines generally to be avoided in older people, or avoided in specific conditions.
- **STOPP** (Screening Tool of Older People's Prescriptions) — medicines to consider stopping.
- **START** (Screening Tool to Alert to Right Treatment) — the complement, and the half that is routinely forgotten: **older people are also *under*-prescribed** medicines with clear benefit (osteoporosis treatment after a minimal-trauma fracture, anticoagulation in AF, statins where indicated). Deprescribing is about appropriateness in both directions, not simply about reducing the count.

**Australian services that exist to do this properly** and that an intern should know to arrange rather than attempt in a ward round: a **Home Medicines Review (HMR)** for community-dwelling patients and a **Residential Medication Management Review (RMMR)** for those in residential aged care — both accredited-pharmacist-conducted, both government-funded, and both underused.

### Mx — how to actually deprescribe

- **Immediate/acute:** on any admission, take a complete and accurate medication history including over-the-counter medicines, supplements and PRN use, and reconcile it against what the patient is actually taking. Admission is the highest-yield opportunity for review, and also the point at which unintended changes most often occur.
- **Definitive — a workable sequence:**
  1. **List every medicine with its indication.** A medicine whose indication nobody can state is the first candidate.
  2. **Assess benefit versus harm for this patient now** — including the *time to benefit*. A preventive medicine whose benefit accrues over 5–10 years offers little to a patient whose life expectancy is shorter than that, while its harms are immediate.
  3. **Establish the patient's own priorities** — symptom control and independence often matter more to them than a long-term risk-reduction target (see [[Communication]] Management of Patients with Multiple Chronic Medical Problems).
  4. **Prioritise** the medicines with the worst harm profile in older people: benzodiazepines and Z-drugs, anticholinergics, antipsychotics, opioids, and the fall-risk-increasing drugs listed under Falls in Older People above.
  5. **Stop one medicine at a time**, so that any benefit or deterioration is attributable.
  6. **Taper where withdrawal or rebound is a genuine risk** — benzodiazepines and Z-drugs, opioids, antidepressants, beta-blockers, corticosteroids, antipsychotics, and PPIs (rebound acid hypersecretion). Do **not** stop these abruptly. For benzodiazepines specifically, a workable approach is an initial reduction of around 20–25%, held for 2–4 weeks, then smaller reductions of roughly 5–12.5%, going slower if withdrawal symptoms emerge (see [[14_06a_Psych_-_Drugs_Used_in_Psychiatry]] Benzodiazepines).
  7. **Monitor and follow up** — document what was stopped and why, tell the patient what to expect and what would warrant restarting, and arrange review. Deprescribing without follow-up is not safer than not deprescribing.
- **Chronic/long-term:** schedule medication review as a recurring event rather than an incidental one, and record a stop date or review date at the time of *starting* any new medicine — the intervention that prevents the problem rather than correcting it later.

> [!tip] Deprescribing is a shared decision, and forced or abrupt withdrawal is both unsafe and counterproductive. The evidence on what makes it succeed is unglamorous: the patient's trust in the prescriber, a gradual taper, and an explicit agreement that a medicine can be restarted if stopping it turns out to be the wrong call. Framing matters — "let's see whether you still need this" is heard very differently from "I'm taking you off this."

---

## Abuse of Older People (Elder Abuse) and Carer Stress

> [!note] Gap-filled from CSV ("Elder abuse / carer stress recognition," High yield). The only genuinely absent row in the whole Geriatrics category on a corpus-wide search — the sole related content was one carer-wellbeing bullet in [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls). Deliberately structured to mirror [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] Non-accidental injury (NAI) — risk factors, features suggestive of abuse, differential, then response — so the two safeguarding entries read the same way despite living in different files. Verified against the RACGP aged care clinical guide (Silver Book) Part B "Abuse of older people", the AIFS National Elder Abuse Prevalence Study, and the Aged Care Quality and Safety Commission's Serious Incident Response Scheme guidance, Aug 2026.

**D:** a single or repeated act, or lack of appropriate action, occurring within a relationship where there is an **expectation of trust**, which causes harm or distress to an older person. The trust relationship is the defining element — it is what distinguishes elder abuse from crime committed by a stranger, and it is also why disclosure is so difficult.

**The five recognised subtypes**, with Australian 12-month prevalence among community-dwelling people aged 65+ from the National Elder Abuse Prevalence Study (**15% experienced at least one subtype**):
- **Psychological/emotional (12%)** — by far the commonest, and the one least likely to be looked for: intimidation, humiliation, threats (including threats of residential care placement), social isolation, withholding contact with family.
- **Neglect (3%)** — failure to provide necessities of life: food, hygiene, medication, medical care, warmth, supervision. May be intentional or arise from carer incapacity.
- **Financial (2%)** — misuse of funds or assets, coercion over a will or power of attorney, unpaid "borrowing", pressure to transfer property. The subtype most often uncovered incidentally.
- **Physical (2%)** — including inappropriate use of restraint or over-sedation.
- **Sexual (1%)**.

**R:** older person factors — cognitive impairment (particularly dementia), functional dependence, social isolation, communication difficulty, and previous family violence. Perpetrator factors, which matter at least as much and are commonly the adult child rather than a paid carer — financial dependence on the older person, substance misuse, mental illness, and **carer stress with inadequate support**.

> [!warning] Features suggestive of abuse of an older person
> **From the history/interaction:** delayed presentation, or an explanation inconsistent with the injury; repeated presentations to different services; a carer who answers for the patient, refuses to leave the room, or is dismissive or hostile toward them; a patient who appears fearful, withdrawn or watchful in the carer's presence; the patient's own disclosure — which may be tentative, minimised, or later retracted.
> **Physical:** bruising in unusual sites or of varying ages, pressure injuries, poor hygiene, unexplained weight loss or dehydration, over- or under-medication, untreated injuries.
> **Financial:** unexplained inability to pay for care or medicines, sudden changes to a will or power of attorney, a relative with unusual control over finances, unpaid bills despite adequate income.
> **Service-related:** missed appointments, non-collection of prescriptions, refusal of services on the patient's behalf by someone else.

> [!note] Differential — none of the features above is specific, and each has innocent explanations that must be genuinely considered rather than dismissed: bruising from anticoagulants, thrombocytopenia or repeated falls (see Falls in Older People above); weight loss from malignancy, depression or dysphagia; pressure injury from immobility despite adequate care; confusion from delirium, dementia or polypharmacy (see [[04_Neurology]] Delirium vs Dementia vs Depression); and self-neglect, which is genuinely different from neglect by another and calls for a different response.

**Assessment:**
- **Interview the older person alone.** This is the single most important step and the one most often skipped. A carer's insistence on remaining present is itself a red flag; a neutral reason to separate them ("I always examine people privately") is usually enough.
- Ask directly but non-accusatorially — *"Does anyone at home make you feel afraid?"*, *"Is anyone taking or using your money without your permission?"*, *"Do you get the help you need with washing, dressing and meals?"*
- **Assess capacity** for the specific decisions in question (see [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework), since it determines whether the person can decline intervention. **A person with capacity may choose to remain in an abusive situation**, and that choice must be respected while support and information are still offered — a genuinely difficult but legally clear point.
- Assess the **carer** as well: burden, mental health, substance use, and whether they have adequate support. Carer stress is a contributing factor to be addressed, not an excuse that discharges the concern.
- Examine and **document thoroughly and objectively** — describe and measure injuries, distinguish fact from opinion, and record the patient's own words verbatim, exactly as the NAI entry requires.

> [!danger] The Australian reporting position — and it is genuinely different from child abuse, which is where most people's intuition comes from
> **There is no general statutory mandatory reporting obligation for elder abuse in Australia.** This is a real and important contrast with mandatory reporting of child abuse (see [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] Sexual abuse for the SA mandatory-reporting duty that does apply to children). Assuming the same duty applies to older people is a common error in both directions — some clinicians report without consent believing they must, others do nothing believing that without a mandatory duty there is no pathway.
> - **Limited exception:** Commonwealth-funded aged care providers have specific reporting obligations under the *Aged Care Act 1997* (Cth), and the **Serious Incident Response Scheme (SIRS)** — in residential aged care since April 2021 and extended to in-home aged care services from December 2022 — requires providers to report serious incidents including abuse and neglect to the **Aged Care Quality and Safety Commission**. This is a *provider* obligation, not a treating-clinician one.
> - **Call the police** where there is a suspected crime or immediate danger.
> - **1800ELDERHelp (1800 353 374)** is the national number that redirects to the relevant state or territory service.
> - Other pathways: the **Office of the Public Advocate** and the relevant state tribunal (**SACAT** in South Australia) where guardianship or financial administration is in question — the same bodies already named in [[Clinical-Process-EBM-Consent-Capacity]] Consent to Medical Treatment and Palliative Care Act 1995 (SA) for capacity disputes.
> The national policy framework is the **National Plan to Respond to the Abuse of Older Australians**.

> [!info] **Two Australian-specific points.** First, **who counts as an "older person" is not 65 for everyone** — Aboriginal and Torres Strait Islander people, and people who are homeless or at risk of homelessness, are eligible for aged care from age 50, so an abuse concern in a 55-year-old from either group should be considered within this framework rather than dismissed on age (see Falls in Older People above). Second, and stated as a limitation rather than a finding: **reliable Australian prevalence data on abuse of older Aboriginal and Torres Strait Islander people specifically is limited**, and the National Elder Abuse Prevalence Study's community-dwelling sample should not be assumed to represent it. Do not extrapolate the subtype percentages above to this population — the honest position is that the data is thin, not that the rates are the same.

**Mx:**
- **Immediate/acute:** treat injuries and address any immediate safety risk. Admission is a legitimate tool where it is the only way to create a safe space while a plan is made.
- **Definitive:** raise the concern through the appropriate pathway above; involve social work early; separate the older person's needs from the carer's; and where the person has capacity and declines intervention, **keep the door open** — document the discussion, provide the contact numbers, treat what they will let you treat, and arrange follow-up. Disclosure often takes several contacts.
- **Chronic/long-term:** address the modifiable drivers — carer support and respite, home care packages via an **Aged Care Assessment Team (ACAT)** assessment, treatment of carer mental illness or substance misuse, and reducing the older person's social isolation. Reassess, because circumstances change and a refusal today is not a refusal forever.

---

## Discharge Planning and Home Safety Assessment

> [!note] Gap-filled from CSV ("Discharge planning / home safety assessment," High yield). Partially present before this: [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls) carries home-environment and referral bullets within an OSCE communication framework, and [[15_01b_Paeds_-_Anaphylaxis]] Discharge planning covers a single-condition paediatric discharge — but the discharge *process* for an older inpatient existed nowhere. Verified against the Australian Commission on Safety and Quality in Health Care's Medication Management at Transitions of Care Stewardship Framework and medication reconciliation guidance, the NSW ACI Care of Confused Hospitalised Older Persons (CHOPs) transfer-of-care principles, and the RACGP aged care clinical guide (Silver Book, 5th edition), Aug 2026.

**Why this is a clinical task rather than an administrative one:** the transition out of hospital is a **recognised high-risk period**, and older people are particularly vulnerable to re-presentation after it. The failure modes are predictable and therefore preventable — the medication list is wrong, the GP does not know what happened, nobody checked whether the person can actually manage at home, and the follow-up that the plan depends on was never arranged.

> [!danger] **Discharge planning starts on admission, not on the day of discharge.** An older person's discharge destination and support needs should be an explicit question from day one, because the assessments and services it depends on — occupational therapy home visit, ACAT assessment, package activation, equipment supply — all take days to arrange. Beginning on the morning of discharge guarantees either a delayed discharge or an unsafe one.

### Functional readiness — the question that actually decides discharge

Medical stability is necessary but not sufficient. The operative question is whether this person can manage in **their** home, which requires knowing what that home is like and what they could do before:
- **Baseline versus current function.** Compare current ADLs (washing, dressing, toileting, transferring, feeding) and IADLs (shopping, cooking, finances, medications, transport) against their **premorbid** level, not against normal. A patient discharged at a function below their baseline without new support will fail.
- **Mobility and transfers**, assessed by physiotherapy — including stairs if there are stairs, and specifically whether they can get off a low chair and off the toilet.
- **Cognition**, which determines whether they can follow the plan at all (see [[04_Neurology]] Delirium vs Dementia vs Depression — and note that delirium frequently has *not* fully resolved at discharge, so the cognitive assessment made on admission may no longer apply).
- **Continence, nutrition and swallowing.**
- **Who is at home**, what they can realistically provide, and whether that arrangement is sustainable for them (see Abuse of Older People (Elder Abuse) and Carer Stress above — carer breakdown is both a discharge failure and a safeguarding risk).

### Home safety assessment

An **occupational therapist home visit** is the substantive version of this, and is more informative than any checklist completed in the ward, because it sees the actual environment. It covers access and entry (steps, rails), the bathroom (shower access, grab rails, toilet height), the kitchen, trip hazards and lighting, bed height and transfers, and the ability to summon help. It prescribes equipment and home modifications and — importantly — checks the person can use them. OT-led discharge planning of this kind is associated with reduced readmission.

Overlaps directly with falls prevention: the same assessment addresses both, so do not commission it twice (see Falls in Older People above).

### Medication reconciliation — the highest-yield single step

**Medication reconciliation should occur at every transition of care**, and the patient and carer should leave with an accurate, updated medication list they understand.

The scale of the problem is Australian and specific: **more than half of medication errors occur at transitions of care**, and **a patient with one or more medicines missing from their discharge information is around 2.3 times more likely to be readmitted** than one whose discharge information is correct. Practically, that means:
- Reconcile the discharge list against the pre-admission list, and account for every difference — stopped, started, or changed dose — with the reason.
- **Say what was deliberately stopped and why**, or the GP or a community pharmacist will helpfully restart it. This is the point at which good deprescribing work done during the admission is most often undone (see Polypharmacy and Deprescribing above).
- Consider a dose administration aid, and whether the person can physically open the packaging and read the label.

### Communication and follow-up

- **Discharge summary to the GP, promptly**, stating the diagnosis, what changed, what was stopped and why, what is outstanding, and what the GP is being asked to do and by when. A summary that arrives after the patient does is of limited use.
- **Explicit follow-up**: GP appointment, outpatient reviews, and who is responsible for chasing any pending results.
- **The patient and carer must understand the plan** — teach-back rather than a handed-over sheet, particularly where cognition is impaired.
- **Safety-netting**: what would warrant re-presentation, and who to call.

### Australian services worth knowing by name

- **Aged Care Assessment Team (ACAT)** — the assessment gateway to Commonwealth-funded aged care, including home care packages, residential care, and transition care. Refer early; it is a common cause of discharge delay.
- **Transition Care Programme** — time-limited therapy and support after a hospital stay for people who need longer to recover; requires the acute episode to be complete, medical stability, and ACAT assessment.
- **My Aged Care** as the entry point patients and families are directed to.
- **Home Medicines Review** for the medication side (see Polypharmacy and Deprescribing above).

> [!danger] **Discharge to a remote community is a different problem, not a harder version of the same one.** Where a patient is returning to a remote or very remote community, the standard plan can fail for reasons that have nothing to do with the medical assessment: the **medicines may not be locally available** and supply arrangements need confirming before discharge rather than after; **follow-up may be through an Aboriginal Community Controlled Health Organisation (ACCHO) or a visiting service** rather than a GP clinic, so the discharge summary must reach the right service; **transport home may take days** and may itself need arranging; and **equipment and home modifications** assume an environment and a supply chain that may not exist. Aboriginal and Torres Strait Islander people are also eligible for aged care assessment from age 50 (see Falls in Older People above), so the ACAT referral threshold is younger than the default.
>
> **Discharge to no fixed address is the other version of this problem**, and it fails for overlapping reasons: there is nowhere to deliver equipment or a home modification to, no address for follow-up correspondence, no safe storage for medicines, and often no phone number that will still work next week. People who are homeless or at risk of homelessness are **also eligible for aged care assessment from age 50** (see Falls in Older People above) — which is frequently the most useful referral available and is routinely not made, because the patient does not look like the person the service is imagined to be for. Involve social work early, and ask about housing explicitly rather than inferring it from the address on the chart, which may be historical. Ask **where the patient is going and who will actually see them**, early — this is the discharge planning that most often fails silently because everyone assumes someone else arranged it.

> [!tip] The commonest avoidable discharge failures, in the order they occur: planning started too late for the services to be arranged; discharge to a function level below baseline with no new support; a medication list that does not say what changed or why; and a follow-up plan that depends on an appointment nobody actually booked.
