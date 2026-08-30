---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 3 Analgesics
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Analgesics (AMH section 3)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.** Where a source supplied a figure that is genuinely part of the clinical concept rather than a prescribing instruction — the serum urate **target**, the definition of **medication overuse headache** — it is given and labelled as such. Use AMH or the local formulary for all dosing.

---

## 0.1 Drugs for Gout

> [!danger] **The single most important prescribing principle in gout: NEVER start, stop or change the dose of a urate-lowering drug during an acute flare unless the patient is already established on it.**
> Any shift in serum urate — up **or down** — destabilises crystal deposits and precipitates or prolongs an attack. If the patient is **already on allopurinol, continue it unchanged** through the flare. If they are not, treat the flare first and start urate-lowering therapy afterwards, with **flare prophylaxis co-prescribed**.

### 0.1.1 Xanthine Oxidase Inhibitors

- **Mechanism:** inhibit **xanthine oxidase**, the enzyme converting hypoxanthine → xanthine → uric acid, so **less urate is produced**.
- **Key agents:** **allopurinol** (first-line in Australia), **febuxostat** (second-line).
- **Indications:** **recurrent gout flares, tophi, urate nephrolithiasis, gouty arthropathy on imaging**, and **tumour lysis syndrome** prophylaxis. **Asymptomatic hyperuricaemia is generally not treated.**
- **How they are used — "start low, go slow, treat to target":** sources agree allopurinol is **started at a low dose** (lower still in renal impairment) and **titrated every 2–4 weeks against the serum urate**, to a **target below 0.36 mmol/L** (lower where there are tophi or frequent flares). **The dose that matters is the one that reaches target, not the starting dose** — under-titration is the commonest reason gout stays uncontrolled. See `NEW_Investigations_General_and_Preventive.md` 0.5.
- **Adverse effects — allopurinol:** rash (common and usually benign, but see below); gastrointestinal upset; deranged LFTs; **precipitation of flares on initiation**, which is why prophylaxis is co-prescribed for **at least 3–6 months**; rarely bone marrow suppression.

> [!danger] **ALLOPURINOL HYPERSENSITIVITY SYNDROME (DRESS / SJS-TEN) is rare and can be fatal.**
> **Any rash on starting allopurinol must be taken seriously and the drug stopped** until it is characterised — a benign-looking maculopapular rash can be the prodrome. Features: rash, **fever, eosinophilia, hepatitis, acute kidney injury**, and mucosal involvement.
> **Risk factors:** **renal impairment** and a **higher starting dose** (which is the reason for "start low"), diuretic use, and — the pharmacogenomic association — **HLA-B\*58:01**. Sources recommend **testing for HLA-B\*58:01 before starting allopurinol in patients of Korean, Han Chinese, Thai and African ancestry**, where the allele is common. See `NEW_Investigations_General_and_Preventive.md` 0.16.

> [!warning] **Febuxostat is second-line, and cardiovascular safety is why.** Sources describe febuxostat as limited by **increased cardiovascular and all-cause mortality** in trial data, so it is generally reserved for patients intolerant of, or inadequately controlled on, allopurinol — and used with caution in established cardiovascular disease. It requires **less dose adjustment in mild-to-moderate renal impairment** than allopurinol, which is its main advantage.

- **Interactions (both agents):**
  - **AZATHIOPRINE and MERCAPTOPURINE — the dangerous one.** Xanthine oxidase metabolises them, so inhibiting it causes **massive accumulation and life-threatening myelosuppression**. This combination should generally be avoided; where unavoidable it requires drastic dose reduction and specialist supervision. **Never prescribe allopurinol to a patient on azathioprine without checking.**
  - **Warfarin, theophylline** — levels may rise.
  - **Thiazide and loop diuretics** raise urate and worsen gout; **ACE inhibitors, ARBs and aspirin** also affect urate handling. Review the whole medication list — sometimes the best gout treatment is changing an antihypertensive.
- **Monitoring:** **serum urate to target**, renal and liver function, FBC, and any rash.

### 0.1.2 Other Drugs for Gout

- **Colchicine**
  - **Mechanism:** binds tubulin, disrupting microtubule assembly and so **neutrophil migration, chemotaxis and inflammasome activation**.
  - **Use:** acute flares and **flare prophylaxis** when starting urate-lowering therapy (sources support continuing prophylaxis for **at least 3–6 months**).
  - **Adverse effects — dose-limiting and predictable:** **diarrhoea, nausea, vomiting and abdominal pain**; at higher exposure, **myelosuppression, myopathy, neuropathy and multi-organ failure**. **Colchicine has a narrow therapeutic index and overdose is potentially fatal with no antidote.**
  - **Dose reduction is required in renal and hepatic impairment and in the elderly** — sources describe reduced dose or reduced frequency in lower creatinine clearance.
  - **Interactions that cause toxicity:** **clarithromycin and erythromycin, azole antifungals, ciclosporin, verapamil and diltiazem, and statins** — via CYP3A4 and P-glycoprotein. **The colchicine–clarithromycin combination has caused deaths**, and this is a genuinely common prescribing scenario (a patient with gout who gets a chest infection).
- **Uricosurics — probenecid**
  - **Mechanism:** blocks renal tubular reabsorption of urate, **increasing urinary excretion**.
  - **Use:** an option in under-excretors intolerant of xanthine oxidase inhibitors; sources describe it as **minimally effective** and **not recommended when creatinine clearance is below about 30 mL/min**.
  - **Cautions:** requires **good hydration** — increasing urinary urate risks **urate stones**; contraindicated where there is a history of urolithiasis; interacts with many renally secreted drugs (it was historically used deliberately to prolong penicillin levels).
- **Corticosteroids** (oral, intra-articular or intramuscular) — a first-line option for acute flares, particularly where NSAIDs and colchicine are contraindicated (renal impairment, anticoagulation, heart failure). **Aspirate the joint and exclude septic arthritis before injecting a steroid into it.**
- **NSAIDs** — first-line for acute flares in patients without contraindications (see 0.4.2).
- **Pegloticase (recombinant uricase)** and **IL-1 inhibitors (anakinra, canakinumab)** — specialist agents for refractory or tophaceous gout, or where all else is contraindicated.

> [!danger] **A hot swollen joint is septic arthritis until proven otherwise** — aspirate, Gram stain and culture. A history of gout and a raised urate do not exclude infection, and the two can coexist. See [[12_02_Rheum_-_Ankylosing_Spondylitis__Gout__Pseudogout__Reactive_Arthritis__Fibromyalgia__PMR__CFS]].

## 0.2 Drugs for Migraine

### 0.2.1 Triptans (5-HT₁B/₁D Agonists)
*(covers build-list classes: Triptans; Triptans (5-HT1B/1D Agonists))*

- **Mechanism:** agonists at **5-HT₁B** (cranial vasoconstriction) and **5-HT₁D/1F** (inhibition of trigeminal nociceptive transmission and of CGRP and other neuropeptide release). They are **migraine-specific acute treatments**, not general analgesics.
- **Key agents:** **sumatriptan** (oral, **subcutaneous** and intranasal — the subcutaneous route is the fastest and most reliable, and matters in severe attacks and in cluster headache), **rizatriptan, zolmitriptan, naratriptan, eletriptan, almotriptan, frovatriptan**.
- **Indications:** **acute treatment of moderate-to-severe migraine**, and **cluster headache** (subcutaneous or intranasal sumatriptan, plus high-flow oxygen).
- **How to use them well — the practical points that determine whether they work:**
  - **Take early in the attack**, while the pain is still mild — efficacy falls once central sensitisation and allodynia are established.
  - **If one triptan fails, another may work** — non-response to one does not predict non-response to the class, and switching is a standard step.
  - **Gastric stasis in migraine impairs oral absorption**; co-administering an antiemetic (metoclopramide, prochlorperazine, domperidone) improves both nausea and drug absorption. Non-oral routes bypass the problem entirely.
- **Adverse effects:** **"triptan sensations"** — chest, throat, neck and jaw tightness, pressure or heaviness; flushing, paraesthesia, dizziness, drowsiness. These are common, usually benign and **not** typically cardiac — but a first episode of chest tightness needs assessment rather than assumption.
- **Contraindications:** sources and product labelling agree — **ischaemic heart disease or previous myocardial infarction, coronary vasospasm (Prinzmetal angina), stroke or TIA, peripheral vascular disease, uncontrolled hypertension**, hemiplegic and basilar migraine, and severe hepatic impairment. **The absolute risk of a vascular event is very low** — sources describe roughly 1 in 30,000 initiators — but the contraindications stand.

> [!danger] **Do not give a triptan within 24 hours of an ergot alkaloid, or an ergot within 6 hours of a triptan** — sources state both intervals explicitly. The additive vasoconstriction is the reason.

- **Interactions:** **MAOIs** (sumatriptan, rizatriptan, zolmitriptan are metabolised by MAO-A); **serotonergic drugs** — the risk of serotonin syndrome with SSRIs and SNRIs is described but is now considered low, and is not a reason to withhold a triptan from a patient on an antidepressant without discussion; propranolol raises rizatriptan levels.

> [!danger] **Not every severe headache is a migraine, and triptans do not treat the dangerous causes.** Red flags — **thunderclap onset, first or worst headache, fever with meningism, new headache over 50, focal neurology, papilloedema, immunosuppression or cancer, headache worse lying flat or on waking, pregnancy/postpartum, or a change in a long-standing headache pattern** — require investigation, not an acute migraine treatment. See [[04_Neurology]].

### 0.2.2 Ergot Alkaloids (5-HT Agonists)

- **Key agents:** **ergotamine** (usually with caffeine), **dihydroergotamine**.
- **Mechanism:** non-selective agonism at serotonin, dopamine and **α-adrenergic** receptors — hence potent and prolonged **vasoconstriction**, which is both the therapeutic effect and the problem.
- **Role:** **largely superseded by triptans** and now rarely first-line. Retained for occasional patients with long-duration attacks who respond to nothing else.
- **Adverse effects:** nausea and vomiting (prominent), **peripheral vasoconstriction and ischaemia (ergotism)**, muscle cramps, and **a strong tendency to cause medication overuse headache and rebound**.
- **Contraindications:** sources list **peripheral vascular disease, coronary artery disease, uncontrolled hypertension, stroke, severe renal or hepatic impairment**, and **pregnancy** (ergot alkaloids are uterotonic and are teratogenic).
- **Interactions:** **potent CYP3A4 inhibitors — macrolides, azole antifungals, HIV protease inhibitors — can precipitate severe ergotism**; and the triptan spacing rule above.

### 0.2.3 Calcitonin Gene-Related Peptide (CGRP) Antagonists
*(covers build-list classes: CGRP Antagonists (Monoclonal Antibodies); Calcitonin gene-related peptide antagonists)*

- **Mechanism:** CGRP is a neuropeptide released from trigeminal afferents that is central to migraine pathophysiology. Two drug types block it:
  - **Monoclonal antibodies** — against the **CGRP ligand** (fremanezumab, galcanezumab, eptinezumab) or the **CGRP receptor** (erenumab). Given by **subcutaneous injection monthly or quarterly** (eptinezumab intravenously).
  - **Small-molecule receptor antagonists ("gepants")** — oral, used acutely and, for some agents, preventively.
- **Indications:** **migraine prevention**, in Australia typically after failure of several conventional preventives, with **PBS authority criteria** governing access (chronic migraine, documented failure of prior preventives, and required response for continuation). **Check the current PBS criteria — they change.**
- **Evidence:** sources report all four monoclonal antibodies are **safe and effective for prevention**, with **no cardiovascular or immunological safety signals in trials**, and note particular value in the **most disabled subgroups — chronic migraine, multiple prior preventive failures, and medication overuse headache**.
- **Adverse effects:** **injection site reactions** (the commonest), **constipation** (notably with erenumab), hypertension, and hypersensitivity. Long-term safety data are still accumulating — CGRP is a vasodilator with a physiological role, so caution is advised in significant vascular disease despite reassuring trial data.
- **Practical points:** they are **preventives, not acute treatments** (except the acute gepants); assess response over **about 3 months** before judging them; **avoid in pregnancy** (long half-life; discuss contraception and planning).

### 0.2.4 Other Drugs to Prevent Migraine
*(covers build-list class: Migraine Therapies (Calcium Channel Blockers))*

- **When to offer prevention:** frequent, disabling or prolonged attacks, poor response to or overuse of acute treatment, or hemiplegic/brainstem-aura migraine. **A headache diary is part of the assessment and of measuring response.**
- **The conventional classes, all of which are drugs borrowed from other indications:**
  - **β-blockers — propranolol, metoprolol.** Best evidence, often first choice. **Avoid in asthma**; caution in depression, bradycardia and peripheral vascular disease.
  - **Tricyclic antidepressants — amitriptyline, nortriptyline.** Particularly useful with **coexisting tension-type headache, insomnia or chronic pain**. Anticholinergic effects, sedation, weight gain, QT prolongation.
  - **Anticonvulsants — topiramate, sodium valproate.** Topiramate: paraesthesia, cognitive slowing ("word-finding difficulty"), weight loss, renal stones, **acute angle-closure glaucoma**, and **teratogenicity**.
  - **Calcium channel blockers — verapamil, flunarizine, pizotifen** (a serotonin antagonist grouped here in some references). **Verapamil is first-line for CLUSTER headache prevention** (requiring ECG monitoring for heart block as the dose rises) rather than for migraine, and this distinction is worth holding.
  - **Candesartan** — an ARB with reasonable evidence in prevention.
  - **Botulinum toxin type A** — for **chronic migraine** specifically (≥15 headache days per month), under specialist protocol.
  - **Riboflavin, magnesium, coenzyme Q10** — modest evidence, low harm.

> [!danger] **VALPROATE AND TOPIRAMATE IN PEOPLE WHO CAN BECOME PREGNANT**
> **Sodium valproate is highly teratogenic** — neural tube defects, other major malformations, and a substantial risk of **neurodevelopmental disorder** — and **must not be used for migraine prevention in anyone who could become pregnant** other than under specialist supervision with a formal pregnancy prevention programme. **Topiramate is also teratogenic** and additionally **reduces the efficacy of combined hormonal contraception at higher doses**. Migraine predominantly affects women of reproductive age, so **this is not an edge case — it is the main population being prescribed to.** Discuss contraception and pregnancy planning explicitly before prescribing either.

> [!danger] **MEDICATION OVERUSE HEADACHE — always ask, because it is the reason the preventives are not working.**
> Sources give the ICHD definition: **headache on ≥15 days per month for more than 3 months in a patient with a pre-existing primary headache disorder, caused by overuse of acute headache medication.** The thresholds differ by drug class — **simple analgesics** at a higher frequency, and **triptans, ergots, opioids and combination analgesics** at a lower one. Risk factors named include **female sex, psychiatric comorbidity, pre-existing pain and medication use**.
> **Management** is to **withdraw the overused drug** (with warning that headache worsens transiently), start or optimise a **preventive**, and support the patient through it — CGRP antibodies are noted to be effective in this group. **A patient using acute treatment more than about two days a week needs prevention, not more acute treatment.**

## 0.3 Drugs for Opioid Dependence

- **Scope:** **opioid agonist treatment (OAT)** — the evidence-based, long-term management of opioid dependence — plus **naltrexone** for relapse prevention and **naloxone** for overdose reversal (0.4.6).
- **Methadone** — a **full µ-agonist**, long half-life, given as a daily oral liquid, historically usually under **supervised dosing**.
  - **Advantages:** long track record; effective; suits patients needing full agonist activity.
  - **Risks:** **respiratory depression, particularly during induction and dose increases**, when the half-life exceeds the duration of the analgesic effect and levels accumulate over days — **most methadone deaths occur in the first two weeks of treatment**. **QT prolongation and torsades de pointes** (dose-related; ECG monitoring is required, more so at higher doses and with other QT-prolonging drugs). Numerous CYP interactions.
- **Buprenorphine and buprenorphine/naloxone** — buprenorphine is a **partial µ-agonist** with **high receptor affinity** and a **ceiling on respiratory depression**, which makes it substantially safer in overdose than methadone. The **naloxone** component in the combination product is poorly absorbed sublingually and is there to deter injection.
  - **PRECIPITATED WITHDRAWAL** is the characteristic hazard: because buprenorphine binds more avidly than full agonists but activates less, **giving it to someone with a full agonist still on board displaces it and precipitates acute severe withdrawal**. Induction therefore requires the patient to be **in objective withdrawal first**, and is done to protocol by an experienced prescriber.
  - **Long-acting injectable buprenorphine (LAIB)** — sources describe **weekly and monthly depot formulations (Buvidal, Sublocade) available in Australia since April 2020**, removing the need for daily supervised dosing. Uptake has been rapid: sources report that by December 2022 Australian treatment was roughly **48% methadone, 26% sublingual buprenorphine and 26% long-acting injectable buprenorphine**, and that **buprenorphine has overtaken methadone as the most common opioid agonist medicine in Australia**.
- **Naltrexone** — a **µ-antagonist** used for relapse prevention after detoxification (and in alcohol use disorder). It **blocks** opioid effects rather than substituting for them, and adherence is the limiting factor. **The patient must be fully opioid-free before starting or it precipitates withdrawal**, and **tolerance is lost while taking it — so overdose risk on relapse is very high.**

> [!danger] **Things an intern must get right around opioid agonist treatment**
> - **NEVER omit or "hold" a patient's regular methadone or buprenorphine dose without specialist advice**, and **confirm the dose and the last dispensed date with the dosing pharmacy or clinic before prescribing it** — a missed dose causes withdrawal, and a wrong dose can be fatal. Tolerance is lost after a few days off treatment.
> - **OAT is a maintenance treatment; it does not provide analgesia for acute pain.** A patient on methadone or buprenorphine with a fracture or after surgery **needs their usual OAT dose continued AND additional analgesia**, often at higher opioid doses than usual because of tolerance and, with buprenorphine, receptor occupancy. Withholding analgesia because "they're on methadone" is a recognised and inhumane failure.
> - **Take-home naloxone** should be offered to anyone at risk of opioid overdose and to their household — it is available in Australia without prescription through the **Take Home Naloxone program**.
> - **Stigma is a clinical problem.** Document the treatment neutrally, involve the addiction medicine service early, and do not discharge a dependent patient without a plan.
> - See [[14_06a_Psych_-_Drugs_Used_in_Psychiatry]].

## 0.4 Drugs for Pain Relief

> [!info] **The framework.** Use the **analgesic ladder** as a starting structure but not a rule: **non-opioid → weak opioid → strong opioid**, with **adjuvants at every step**. Modern practice is **multimodal** — combining paracetamol, an NSAID (if safe), a regional or local anaesthetic technique, and adjuvants (gabapentinoids, ketamine, antidepressants for neuropathic pain) to **minimise opioid dose**. In chronic non-cancer pain, opioids have **poor long-term evidence and substantial harm**, and non-pharmacological management is central.

### 0.4.1 Non-Opioid Analgesics (Paracetamol)

- **Mechanism:** incompletely understood — central COX inhibition, and effects on the endocannabinoid and serotonergic descending inhibitory systems. **Not a meaningful anti-inflammatory at clinical doses.**
- **Indications:** **first-line for mild-to-moderate pain and fever**, and the **background analgesic in multimodal regimens** — it should be regular, not "as required", when treating significant pain.
- **Advantages:** safe in pregnancy and breastfeeding, safe with anticoagulation, safe in renal impairment, safe in asthma, no gastrointestinal ulceration. This safety profile is why it is the default.
- **Adverse effects:** minimal at therapeutic dose. **Hepatotoxicity in overdose** is the whole story.

> [!danger] **Paracetamol overdose is the commonest cause of acute liver failure requiring transplantation in Australia, and it is entirely treatable if caught.**
> - **The antidote is N-acetylcysteine**, and it is **most effective when given early** — before hepatic injury is established. **Do not wait for LFTs to become abnormal.**
> - **Take a paracetamol level at the appropriate time after ingestion and plot it on the nomogram**; for staggered or unknown-time ingestions, treat and consult.
> - **Always call the Poisons Information Centre (13 11 26 in Australia)** and follow the current Australian guideline — the protocols have changed and are the authoritative source.
> - **Higher-risk patients** — chronic alcohol use, malnutrition, low body weight, enzyme-inducing drugs — sustain injury at lower doses.
> - **The commonest real-world hazard is unintentional supratherapeutic dosing**: patients taking a regular paracetamol preparation **plus** a combination cold-and-flu or codeine-containing product without realising both contain it. **Ask specifically about over-the-counter products, and count the total daily paracetamol.**
> - Dose reduction is advised in low body weight, frailty and significant hepatic impairment.

### 0.4.2 NSAIDs — Non-Selective
*(covers build-list classes: NSAIDs; Non-Selective NSAIDs)*

- **Mechanism:** inhibit **cyclo-oxygenase**, reducing prostaglandin synthesis. **COX-1** is constitutive — gastric mucosal protection, platelet thromboxane, renal perfusion. **COX-2** is largely inducible at sites of inflammation. **Non-selective agents inhibit both, and every major adverse effect follows from COX-1 inhibition.**
- **Key agents:** **ibuprofen, naproxen, diclofenac, indomethacin, ketorolac, piroxicam, aspirin** (irreversible, and the only one used as an antiplatelet).
- **Indications:** inflammatory and nociceptive pain, **acute gout**, musculoskeletal injury, dysmenorrhoea, renal colic (where they are genuinely first-line and often better than opioids), fever, and — for aspirin — antiplatelet therapy at low dose.
- **Adverse effects — organised by mechanism, which is how to remember them:**
  - **Gastrointestinal:** dyspepsia, **peptic ulceration, bleeding and perforation** — often **without preceding dyspepsia**, particularly in the elderly. Risk rises with age, prior ulcer, *H. pylori*, corticosteroids, anticoagulants and SSRIs. **Co-prescribe a proton pump inhibitor in at-risk patients.** See [[03_Gastrointestinal]].
  - **Renal:** prostaglandins maintain afferent arteriolar dilatation, so NSAIDs cause **acute kidney injury** in any state of reduced renal perfusion — dehydration, sepsis, heart failure, cirrhosis, existing chronic kidney disease. Also **sodium and water retention, hyperkalaemia** and worsening hypertension. See [[07_Renal_Medicine_and_Urology]].
  - **Cardiovascular:** increased risk of **myocardial infarction, stroke and heart failure decompensation** — a class effect that is not confined to COX-2 selective agents (diclofenac carries a risk comparable to the coxibs). **Naproxen appears the least cardiotoxic** of the commonly used agents.
  - **Respiratory:** **aspirin/NSAID-exacerbated respiratory disease** — the triad of asthma, nasal polyps and NSAID sensitivity; bronchospasm can be severe.
  - Other: fluid retention, hepatotoxicity, aseptic meningitis (rare), and **impaired fracture and soft tissue healing** (debated).
- **Contraindications:** active peptic ulceration or GI bleeding; severe heart failure; significant renal impairment; NSAID-sensitive asthma; **third trimester of pregnancy** (premature closure of the ductus arteriosus, oligohydramnios, and delayed labour); anticoagulation (relative).

> [!danger] **THE "TRIPLE WHAMMY": ACE inhibitor (or ARB) + diuretic + NSAID = acute kidney injury.**
> Each drug attacks a different part of glomerular perfusion. The combination is one of the commonest **preventable** causes of hospital admission with acute kidney injury in Australia, and the NSAID is usually the one the patient bought over the counter. **Ask every patient with acute kidney injury what they have been taking for pain**, and give **"sick day" advice** — withhold the NSAID, ACE inhibitor/ARB and diuretic during acute illness with dehydration.

- **Interactions:** **warfarin and DOACs** (bleeding); **SSRIs** (bleeding, additively); **lithium and methotrexate** (reduced clearance, toxicity); **antihypertensives** (reduced effect); **ibuprofen interferes with the antiplatelet effect of low-dose aspirin** if taken shortly before it.
- **Monitoring:** renal function and blood pressure with regular use; symptoms and signs of GI bleeding; **and a stop date — NSAIDs are for the shortest effective course.**

### 0.4.3 COX-2 Selective NSAIDs (Coxibs)

- **Key agents:** **celecoxib, etoricoxib, meloxicam** (partially selective), parecoxib.
- **Mechanism and rationale:** preferential COX-2 inhibition, sparing the constitutive COX-1 that protects the gastric mucosa and supports platelet function.
- **Advantages:** **lower risk of gastrointestinal ulceration and bleeding** than non-selective NSAIDs, and **no effect on platelet aggregation** — which makes them useful where bleeding risk matters (though not risk-free).
- **The trade-off:** **cardiovascular and thrombotic risk** — the reason rofecoxib was withdrawn. **Contraindicated in established ischaemic heart disease, cerebrovascular disease, peripheral arterial disease and moderate-to-severe heart failure.**
- **The renal effects are NOT spared.** COX-2 is constitutively expressed in the kidney, so coxibs cause **the same acute kidney injury, fluid retention, hyperkalaemia and hypertension** as non-selective NSAIDs. **A coxib is not a "safe NSAID" in renal impairment**, and this is a common misconception.
- **Celecoxib** is a sulfonamide — caution with sulfonamide allergy.

### 0.4.4 Opioid Analgesics — Full µ-Agonists
*(covers build-list classes: Mu-Opioid Receptor Agonists (Full); Opioid Analgesics (Strong / Full Agonists); Opioid analgesics)*

- **Mechanism:** **µ-opioid receptor agonism** in the dorsal horn, brainstem and higher centres — reducing nociceptive transmission and, importantly, altering the **affective** response to pain.
- **Key agents:** **morphine, oxycodone, hydromorphone, fentanyl, methadone, tapentadol** (also noradrenaline reuptake inhibition), **tramadol** and **codeine** (both weak, both prodrugs — see below).
- **Indications:** **moderate-to-severe acute nociceptive pain**, **cancer pain**, palliative symptom control including breathlessness, and — with much greater caution and poor evidence — selected chronic non-cancer pain.
- **Adverse effects:**
  - **Respiratory depression** — the one that kills. **Increasing sedation precedes it**, so **monitor sedation score, not just respiratory rate.**
  - **Constipation** — universal, and **no tolerance develops**. **Always co-prescribe an aperient** with a regular opioid; this is one of the commonest omissions in ward prescribing.
  - **Nausea and vomiting** (tolerance usually develops), sedation, pruritus, urinary retention, delirium and **myoclonus**, dry mouth, and **hypogonadism, immunosuppression and opioid-induced hyperalgesia** with long-term use.
  - **Tolerance, physical dependence and, in a minority, addiction** — three distinct things that are routinely conflated.
- **Agent-specific points that change practice:**
  - **Morphine's active metabolite morphine-6-glucuronide accumulates in RENAL IMPAIRMENT**, causing delayed sedation, respiratory depression and myoclonus. In significant renal impairment, agents with less problematic metabolites (fentanyl, hydromorphone, buprenorphine) are preferred.
  - **Codeine and tramadol are prodrugs requiring CYP2D6.** **Ultra-rapid metabolisers** convert too much and can suffer respiratory depression at ordinary doses (this caused deaths in children after tonsillectomy and in breastfed infants of ultra-rapid metaboliser mothers); **poor metabolisers get no analgesia at all**. Both are avoided in children and in breastfeeding.
  - **Tramadol** additionally inhibits serotonin and noradrenaline reuptake, so it **lowers the seizure threshold** and can cause **serotonin syndrome** with SSRIs, SNRIs, MAOIs and other serotonergic drugs. It is often wrongly perceived as a "mild" or "safe" opioid.
  - **Fentanyl patches** are for **stable chronic pain only** — **never for acute pain or opioid-naive patients**; they take many hours to reach effect and continue to release drug after removal, and **heat (fever, heat packs, hot showers) increases absorption unpredictably.**
  - **Methadone** has a long and variable half-life, accumulates over days, and prolongs the QT — its use for pain is a specialist decision.
- **Interactions:** **benzodiazepines, gabapentinoids, alcohol, antipsychotics and sedating antihistamines** — additive respiratory depression; **CYP2D6 inhibitors (fluoxetine, paroxetine, bupropion)** block codeine and tramadol activation; serotonergic drugs with tramadol and tapentadol.
- **Australian regulatory context:** sources record that **all codeine-containing medicines were rescheduled to prescription-only (Schedule 4) on 1 February 2018**, on the basis that low-dose codeine adds little analgesia to a non-opioid and carries real harm. There are **real-time prescription monitoring systems** in Australian jurisdictions, and opioid prescribing is subject to PBS quantity and indication restrictions.

> [!danger] **Safe opioid prescribing on the ward — the practical rules**
> - **Prescribe an aperient, an antiemetic and naloxone availability alongside any regular opioid.**
> - **Do not prescribe two regular strong opioids concurrently**, and be explicit about which is the breakthrough agent and its interval.
> - **Reduce doses in the elderly, in renal and hepatic impairment, and in obstructive sleep apnoea.**
> - **Opioids do not treat neuropathic pain well** — reach for the appropriate adjuvant instead of escalating the opioid.
> - **Set a stop date for acute pain.** Discharging a patient on an open-ended opioid supply is how chronic use starts; **prescribe the smallest quantity and communicate the plan to the GP.**
> - See [[10_11c_Oncology_-_Palliative_Care_Prescribing]] for the different calculus in cancer and end-of-life care.

### 0.4.5 Partial µ-Agonists and Mixed Agonist-Antagonists
*(covers build-list class: Mu-Opioid Receptor Agonists (Partial))*

- **Buprenorphine** — a **high-affinity partial µ-agonist** (and κ-antagonist).
  - **The ceiling effect on respiratory depression** makes it comparatively safe in overdose, and its **long duration and transdermal/depot formulations** make it useful in chronic pain, in the elderly, and in **renal impairment** (metabolites are not renally problematic).
  - **The high receptor affinity is a double-edged property:** it **precipitates withdrawal** in someone with a full agonist on board, and it **can blunt the effect of full agonists given for acute pain** — which is why perioperative and acute pain management in a patient on buprenorphine needs a plan made with the acute pain or addiction service, not improvised.
  - Because it binds so tightly, **reversal with naloxone may require higher doses and an infusion.**
- **Tramadol and tapentadol** — atypical opioids combining µ-agonism with monoamine reuptake inhibition (see 0.4.4); **tapentadol** has a lower µ-affinity but stronger noradrenergic action and is used in neuropathic and mixed pain.
- **Mixed agonist–antagonists (pentazocine, nalbuphine, butorphanol)** — κ-agonist/µ-antagonist agents, now little used: they cause dysphoria and hallucinations, have an analgesic ceiling, and **precipitate withdrawal** in opioid-dependent patients.

### 0.4.6 µ-Opioid Receptor Antagonists

- **Naloxone** — a short-acting competitive µ-antagonist for **opioid overdose**.
  - **Titrate in small increments** to restore adequate ventilation, **not** to restore full consciousness. A large bolus in a tolerant or postoperative patient causes **acute severe pain, agitation, catecholamine surge, hypertension, arrhythmia and pulmonary oedema**.
  - **Its duration of action is SHORTER than that of most opioids** — especially methadone, modified-release preparations and fentanyl patches — so **the patient must be observed and often needs an infusion.** Re-sedation after a single successful dose is a classic and lethal error.
  - **Take-home naloxone** (intranasal or intramuscular) is available in Australia without prescription and should be offered to anyone at risk and to their family.
- **Naltrexone** — long-acting oral (and implant/depot) antagonist for **relapse prevention** in opioid and alcohol use disorder. **Must not be started until the patient is opioid-free**, and **tolerance is lost during treatment**, making relapse overdose particularly dangerous.
- **Peripherally acting antagonists — methylnaltrexone, naloxegol, and naloxone in fixed combination with oxycodone.** These block **gut** µ-receptors to treat **opioid-induced constipation** without crossing the blood–brain barrier, so analgesia is preserved. Useful when standard aperients fail, particularly in palliative care.

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Drugs for gout | SUB | yes | |
| 0.1.1 | Xanthine Oxidase Inhibitors | CLS | yes | Urate target (<0.36 mmol/L) stated as a clinical concept, not a dose. |
| 0.1.2 | Other drugs for gout | CLS | yes | Colchicine, probenecid, corticosteroids, uricase, IL-1 inhibitors. |
| 0.2 | Drugs for migraine | SUB | yes | |
| 0.2.1 | Triptans | CLS | yes | Built jointly with `Triptans (5-HT1B/1D Agonists)` — same class, two names. |
| 0.2.1 | Triptans (5-HT1B/1D Agonists) | CLS | yes | As above. |
| 0.2.2 | Ergot Alkaloids (5-HT Agonists) | CLS | yes | |
| 0.2.3 | CGRP Antagonists (Monoclonal Antibodies) | CLS | yes | Built jointly with `Calcitonin gene-related peptide antagonists`. PBS criteria flagged as changeable, not quoted. |
| 0.2.3 | Calcitonin gene-related peptide antagonists | CLS | yes | As above. |
| 0.2.4 | Other drugs to prevent migraine | CLS | yes | |
| 0.2.4 | Migraine Therapies (Calcium Channel Blockers) | CLS | yes | Within 0.2.4; verapamil's cluster-headache role distinguished from migraine. |
| 0.3 | Drugs for opioid dependence | SUB | yes | |
| 0.4 | Drugs for pain relief | SUB | yes | |
| 0.4.1 | Non-opioid analgesics | CLS | yes | Paracetamol. NAC dosing and nomogram thresholds **not stated** — referred to the current Australian guideline and the Poisons Information Centre. |
| 0.4.2 | NSAIDs | CLS | yes | Built jointly with `Non-Selective NSAIDs`. |
| 0.4.2 | Non-Selective NSAIDs | CLS | yes | As above. |
| 0.4.3 | COX-2 Selective NSAIDs | CLS | yes | |
| 0.4.4 | Mu-Opioid Receptor Agonists (Full) | CLS | yes | Built jointly with `Opioid Analgesics (Strong / Full Agonists)` and `Opioid analgesics`. |
| 0.4.4 | Opioid Analgesics (Strong / Full Agonists) | CLS | yes | As above. |
| 0.4.4 | Opioid analgesics | CLS | yes | As above. |
| 0.4.5 | Mu-Opioid Receptor Agonists (Partial) | CLS | yes | |
| 0.4.6 | Mu-Opioid Receptor Antagonists | CLS | yes | |

**Rows in file: 22 (4 SUB + 18 CLS). AMH section 3 build-list rows: 22. Section complete.**

> [!note] **Seven build-list rows are naming duplicates of others** (the two triptan rows, the two CGRP rows, the two NSAID rows, and the three full-agonist opioid rows collapsing to one). Each concept is written once and every row mapped in the table.
