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
- **Lying and standing blood pressure** — measured supine after 5 minutes, then at 1 and 3 minutes standing. A sustained drop of **≥20 mmHg systolic or ≥10 mmHg diastolic** defines orthostatic hypotension. This is the highest-yield bedside test in a faller and is very commonly omitted.
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
- **Chronic/long-term:** **Comprehensive Geriatric Assessment** — the multidimensional, multidisciplinary assessment (medical, functional, cognitive, psychological, social, environmental) with a coordinated plan, which is the structure that ties together everything in this file. Address social isolation, arrange appropriate community supports, and reassess frailty status annually to track the trajectory rather than assuming it only goes one way.
