---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 15 Neurological drugs
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Neurological (AMH section 15)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file** — including antiepileptic titration schedules, where the *principle* of slow titration is given but the numbers must come from AMH or the product information.

> [!info] **A theme for the whole section: several of these drug groups are DANGEROUS TO OMIT.** Antiepileptics, antiparkinsonian drugs and myasthenia treatments all cause serious harm when a dose is missed in hospital — through seizure, parkinsonism-hyperpyrexia and myasthenic crisis respectively. **A nil-by-mouth order is not a reason to omit them; it is a reason to find another route.**

---

## 0.1 Antiepileptics

> [!info] **Principles.** Choose by **seizure type and syndrome**, by **sex and reproductive potential**, and by **comorbidity**. **Start low and titrate slowly**; aim for **monotherapy at the maximum tolerated dose** before adding a second agent. **Most antiepileptic levels are of limited value** — sources note therapeutic drug monitoring is most justified for **phenytoin** (non-linear kinetics) and for a few others, and that levels are otherwise used to check adherence, investigate toxicity, or in pregnancy and renal/hepatic impairment. **Treat the patient, not the level.**

### 0.1.1 The Major Agents and Their Defining Features
- **Sodium valproate** — broad spectrum, effective in generalised epilepsy including absence and myoclonic seizures. **Adverse effects: weight gain, tremor, hair loss, thrombocytopenia, hepatotoxicity, pancreatitis, hyperammonaemic encephalopathy (which can occur with normal LFTs and a therapeutic level — see `NEW_Investigations_General_and_Preventive.md` 0.6), and PCOS.**
- **Carbamazepine** — focal seizures, trigeminal neuralgia. **A potent enzyme INDUCER**, causing extensive interactions (contraceptives, warfarin, DOACs, statins, antiretrovirals, immunosuppressants). Causes **hyponatraemia (SIADH)**, rash, leucopenia, and **auto-induction of its own metabolism**.
- **Lamotrigine** — broad spectrum, well tolerated cognitively, and comparatively favourable in pregnancy. **The rash is the issue** (see below).
- **Levetiracetam** — broad spectrum, few interactions, no hepatic metabolism (renally cleared, so dose-adjust in renal impairment), rapid titration possible — which is why it is the common intravenous choice in hospital. **The problem is behavioural** (see below).
- **Phenytoin** — still used for status epilepticus and loading. **Zero-order (saturable) kinetics** mean a small dose increase can cause a large level rise and toxicity — **nystagmus, ataxia, dysarthria, confusion**. Highly protein bound (**measure free phenytoin in hypoalbuminaemia**), a potent enzyme inducer, and causes **gingival hyperplasia, hirsutism, coarse facies, osteomalacia and cerebellar atrophy** with long-term use. **Intravenous administration causes hypotension and arrhythmia if given too fast, and "purple glove syndrome"** — give slowly with cardiac monitoring.
- **Others:** **topiramate** (weight loss, paraesthesia, cognitive slowing, renal stones, **acute angle-closure glaucoma**, teratogenic, reduces contraceptive efficacy at higher dose); **sodium channel blockers lacosamide** (PR prolongation) and **oxcarbazepine** (hyponatraemia); **perampanel** (behavioural effects, boxed warning); **zonisamide**; **phenobarbital** and **primidone** (sedation, enzyme induction); **ethosuximide** (absence seizures specifically); **vigabatrin** (**irreversible visual field constriction** — reserved for infantile spasms with mandatory visual monitoring); **gabapentin and pregabalin** (mainly used for neuropathic pain — see 0.6).

> [!danger] **SODIUM VALPROATE AND PREGNANCY — the highest-stakes prescribing decision in this section.**
> Valproate causes **major congenital malformations (including neural tube defects) in roughly 10% of exposed pregnancies and neurodevelopmental disorder — reduced IQ and autism — in a substantial further proportion.** The risk is dose-related and exceeds that of every other commonly used antiepileptic.
> **Formal pregnancy prevention programmes exist internationally** — sources describe the MHRA **PREVENT programme (2018)**, which made specific requirements a legal condition of prescribing in the UK. **Sources note that the Australian Advisory Committee on Medicines did not, at the time reviewed, consider a formal programme the best course of action for Australia**, and Australian data show continued initiation in women of reproductive age. **So the Australian regulatory framework differs from the UK's — but the clinical obligation does not.**
> **In practice: do not use valproate in anyone who could become pregnant unless there is no effective alternative; if it is used, ensure highly effective contraception, document the counselling, prescribe high-dose folate, and involve a neurologist and obstetric physician before conception.** This applies to its use in **bipolar disorder and migraine** as much as in epilepsy — arguably more so, since alternatives are easier there.

> [!danger] **LAMOTRIGINE RASH: TITRATE SLOWLY, AND STOP AT THE FIRST RASH.**
> Sources state that **severe reactions including Stevens-Johnson syndrome are more likely with an elevated starting dose or rapid titration, and that slow titration reduces the incidence of rash** — describing a cautious schedule beginning at a low dose for two weeks with stepwise increases thereafter.
> **The critical interaction: VALPROATE INHIBITS LAMOTRIGINE METABOLISM AND ROUGHLY DOUBLES ITS LEVEL** — sources include a case of SJS arising from exactly this combination. **The lamotrigine starting dose and titration must be halved when valproate is co-prescribed**, and increased when an enzyme inducer is. Getting this wrong causes SJS.
> **Tell every patient: "If you develop a rash, stop the tablet and contact us the same day."** And if lamotrigine has been stopped for more than a few days, **it must be re-titrated from the beginning** — restarting at the previous dose is a recognised cause of severe rash.

> [!danger] **CARBAMAZEPINE AND HLA-B\*15:02.** Sources confirm that **HLA-B\*15:02 predicts carbamazepine-induced SJS/TEN in patients of Asian ancestry**, and that **testing should be performed before initiating carbamazepine in patients with ancestry in populations where the allele may be present** (Han Chinese, Thai, Malaysian, Indian and other South-East Asian groups). See `NEW_Investigations_General_and_Preventive.md` 0.16.

> [!warning] **LEVETIRACETAM AND BEHAVIOUR.** Sources report **irritability, aggression, hostility, nervousness and agitation as common**, with **psychosis and suicidality as uncommon but serious**, and note the risk in **children** particularly. **Ask the patient AND the family about mood and behaviour at every review** — patients often do not connect the change to the drug, and it is a frequent and easily reversible cause of distress. **Pyridoxine is sometimes used to mitigate it, and brivaracetam is an alternative.**

> [!danger] **Standing rules for antiepileptics in hospital**
> - **NEVER omit an antiepileptic dose.** If the patient is nil by mouth or vomiting, **find a parenteral or alternative route** — levetiracetam, valproate, phenytoin, lacosamide and phenobarbital all have intravenous forms. Omission causes breakthrough seizures and status.
> - **Prescribe by brand where the product information advises consistency**, and avoid switching formulations for narrow-therapeutic-index agents.
> - **Enzyme-inducing antiepileptics (carbamazepine, phenytoin, phenobarbital, primidone, and topiramate at higher doses) REDUCE HORMONAL CONTRACEPTIVE EFFICACY** — and, conversely, **oestrogen reduces lamotrigine levels**, so seizure control can change with the pill and in pregnancy.
> - **All antiepileptics carry a class warning for suicidal ideation** — ask.
> - **Driving:** a seizure has statutory driving implications in every Australian state. **Tell the patient not to drive and document it**, and direct them to the current fitness-to-drive standard.
> - **Bone health** — enzyme inducers cause osteomalacia and osteoporosis with long-term use.
> - See [[04_Neurology]] and [[15_12a_Paeds_-_Epilepsy_Syndromes_and_Status_Epilepticus]].

### 0.1.2 Benzodiazepines (Neurology)
- **Key agents:** **midazolam** (buccal, intranasal, intramuscular, intravenous), **diazepam** (intravenous and rectal), **lorazepam** (intravenous — the preferred agent where available for status), **clobazam** and **clonazepam** (oral, as adjunctive antiepileptics).
- **Mechanism:** positive allosteric modulation at the **GABA-A** receptor.
- **Role:** **FIRST-LINE for terminating an acute seizure and for status epilepticus** — and for **community and school management of prolonged seizures** (buccal midazolam), which is one of the more useful prescriptions in paediatric neurology.

> [!danger] **STATUS EPILEPTICUS: give the benzodiazepine EARLY and ADEQUATELY, then move on.**
> The commonest errors are **under-dosing the benzodiazepine and giving repeated doses instead of escalating.** **Two adequate doses, then move to a second-line agent (levetiracetam, valproate, phenytoin/fosphenytoin or lacosamide).** Simultaneously: **airway, oxygen, glucose (and THIAMINE before glucose in the at-risk patient), electrolytes including calcium and magnesium, temperature, and a search for the cause** — including eclampsia (which is treated with **magnesium**, not a benzodiazepine), meningitis, haemorrhage, toxins and drug withdrawal. **Prolonged status causes permanent neuronal injury, so time matters.**
- **Adverse effects:** **respiratory depression** — profoundly potentiated by opioids; **have airway support and flumazenil available but recognise that flumazenil is rarely appropriate** (see `NEW_Drugs_02_Anaesthetics.md` 0.2.1); sedation, hypotension, tolerance and dependence.
- **Clobazam and clonazepam** as maintenance antiepileptics lose efficacy through **tolerance**, and cause sedation and, in children, drooling and behavioural change.

### 0.1.3 Other Antiepileptics
Covered in 0.1.1 alongside the major agents, because separating "other" antiepileptics from the principal ones would fragment a group that is chosen comparatively. **Also in this group:** the **ketogenic diet** and **vagus nerve stimulation** for refractory epilepsy; **epilepsy surgery**, which is under-utilised and should be considered early in drug-resistant focal epilepsy; and **cannabidiol** for Dravet and Lennox-Gastaut syndromes.

## 0.2 Drugs for Parkinsonism

> [!danger] **THE SINGLE MOST IMPORTANT RULE IN THIS SUBSECTION: NEVER STOP OR DELAY ANTIPARKINSONIAN MEDICATION, AND NEVER GIVE A DOPAMINE ANTAGONIST TO A PATIENT WITH PARKINSON DISEASE.**
> Sources describe **neuroleptic malignant-like syndrome / parkinsonism-hyperpyrexia syndrome** following **sudden withdrawal of levodopa** in chronically treated patients — **fever, altered mental state, severe rigidity, autonomic dysfunction and raised CK developing over hours** — and note it has also followed stopping **amantadine or a dopamine agonist**, and even **failure to recharge a deep brain stimulator battery**.
> **Practical consequences for an intern, and these come up constantly:**
> - **Parkinson medications are TIME-CRITICAL. They must be given at the patient's own times, not at the ward drug round times.** A delay of an hour matters.
> - **Nil by mouth is not a reason to omit them.** Use a **nasogastric tube**, **dispersible or patch formulations (rotigotine)**, or **apomorphine** — and **ask the neurology or movement disorder team for a conversion**, since levodopa equivalents are not intuitive.
> - **NEVER prescribe metoclopramide, prochlorperazine, haloperidol or a typical antipsychotic** — they block dopamine and cause severe deterioration. **For nausea use domperidone or ondansetron; for psychosis use quetiapine or clozapine**, on specialist advice.
> - Allow patients to **self-administer their own medication** in hospital where safe — this is often the most reliable way to get the timing right.

### 0.2.1 Dopamine Precursors
- **Key agents:** **levodopa**, always combined with a **peripheral decarboxylase inhibitor — carbidopa or benserazide** — which prevents peripheral conversion, reducing nausea and allowing more levodopa to reach the brain. Also available with **entacapone** (a COMT inhibitor) and as **intestinal gel infusion** for advanced disease.
- **Role:** **the most effective symptomatic treatment for Parkinson disease**, and the benchmark against which everything else is measured.
- **Long-term motor complications — the reason levodopa is not simply given at maximum dose from the start:** sources describe **"wearing off"** (end-of-dose return of bradykinesia, rigidity and tremor as the plasma and brain concentration falls), **early morning dystonia**, **on/off fluctuations**, and **dyskinesia** — involuntary movements associated with **peak** drug concentrations. These emerge with disease progression and long-term treatment, and drive the use of longer-acting formulations, more frequent dosing, adjuncts and, eventually, infusion or deep brain stimulation.
- **Adverse effects:** **nausea** (give with food initially, or add domperidone), **postural hypotension**, hallucinations and confusion (especially in older patients and in Lewy body dementia), impulse control disorders (less than with agonists), and dyskinesia.

### 0.2.2 Dopamine Agonists (Non-Ergot)
*(covers build-list classes: Dopamine Agonists (Non-Ergot); Dopamine agonists (parkinsonism))*
- **Key agents:** **pramipexole, ropinirole, rotigotine** (transdermal patch — valuable when a patient cannot swallow), **apomorphine** (subcutaneous rescue injection and infusion).
- **Role:** used as **initial therapy in younger patients** to delay levodopa-related motor complications, and as **adjuncts** later. Also used in **restless legs syndrome** at much lower doses.

> [!danger] **IMPULSE CONTROL DISORDERS — the adverse effect that ruins lives and is missed because nobody asks.**
> Sources describe **compulsive gambling, shopping, hypersexuality and binge eating**, together with **punding, dopamine dysregulation syndrome, compulsive hoarding and "walkabouts"**, and identify **dopamine agonists targeting D2/D3 receptors in the mesocorticolimbic pathway as the main risk factor** — with higher risk in **younger, early-onset patients**. Sources emphasise the impact on families and carer burden.
> **The patient will not volunteer this.** **Ask directly, and ask the partner or family, at every review** — about gambling, spending, sexual behaviour, eating and repetitive activities. **Financial and relationship ruin occurs before anyone connects it to the drug.** Management is dose reduction or switching, done carefully because of withdrawal.
> **DOPAMINE AGONIST WITHDRAWAL SYNDROME** — anxiety, panic, depression, sweating, pain and drug craving — occurs on tapering and is another reason not to stop abruptly.

- **Other adverse effects:** **sudden onset of sleep ("sleep attacks") — with implications for driving that must be discussed**; hallucinations and psychosis (more than levodopa); postural hypotension; nausea; peripheral oedema; and, for **apomorphine**, severe nausea requiring domperidone pretreatment and injection site nodules.
- **Ergot-derived agonists (bromocriptine, cabergoline, pergolide)** are largely abandoned in Parkinson disease because of **cardiac valvulopathy and fibrotic reactions** (see `NEW_Drugs_10_Endocrine.md` 0.5.3).

### 0.2.3 MAO-B Inhibitors
- **Key agents:** **selegiline, rasagiline, safinamide**.
- **Mechanism:** selectively inhibit **monoamine oxidase B**, reducing central dopamine breakdown.
- **Role:** modest monotherapy benefit in early disease; useful as an **adjunct for wearing off**.
- **Adverse effects:** generally well tolerated; insomnia (selegiline is metabolised to amfetamine derivatives — dose in the morning), nausea, and worsening of dyskinesia.
- **Interactions:** at therapeutic doses B-selectivity means the **"cheese reaction" is not a practical concern**, but **serotonin syndrome with SSRIs, SNRIs, tramadol, pethidine and triptans is** — the combinations are used cautiously in practice, and **pethidine is contraindicated**.

### 0.2.4 Anticholinergics
- **Key agents:** **benztropine, benzhexol (trihexyphenidyl)**, procyclidine, biperiden.
- **Mechanism:** restore the dopamine–acetylcholine balance in the striatum.
- **Role:** now **narrow** — mainly **tremor-predominant Parkinson disease in younger patients**, and, importantly, **acute drug-induced dystonic reactions**, where intramuscular or intravenous benztropine works within minutes and is the standard treatment.
- **Adverse effects:** the full anticholinergic burden — **confusion, delirium, memory impairment, hallucinations**, dry mouth, blurred vision, constipation, urinary retention. **They are avoided in older people and in anyone with cognitive impairment**, where the cognitive harm outweighs any motor benefit.

### 0.2.5 Other Drugs for Parkinson's Disease
- **COMT inhibitors — entacapone, opicapone, tolcapone.** Extend the levodopa half-life and reduce wearing off. **Entacapone turns urine orange-brown** (warn the patient); **tolcapone requires liver monitoring** because of hepatotoxicity.
- **Amantadine** — an NMDA antagonist with modest antiparkinsonian effect and, importantly, **the best available treatment for levodopa-induced DYSKINESIA**. Causes **livedo reticularis, ankle oedema, confusion and hallucinations**, and is renally cleared (accumulates in renal impairment). **Do not stop it abruptly** (see the danger callout above).
- **Apomorphine and levodopa-carbidopa intestinal gel** — device-assisted therapies for advanced disease with severe fluctuations; **deep brain stimulation** likewise.
- **Non-motor symptoms are frequently the greater burden and are under-treated:** constipation, orthostatic hypotension, depression and anxiety, REM sleep behaviour disorder, drooling, urinary symptoms, pain, and **dementia** (rivastigmine has evidence). **Physiotherapy, speech pathology, occupational therapy and Parkinson nurse specialists change function more than dose adjustments do.**
- **Drug-induced parkinsonism** — from antipsychotics, metoclopramide, prochlorperazine and others — is **common, under-recognised and reversible**; **review the drug list before diagnosing Parkinson disease.**

## 0.3 Drugs for Alzheimer's Disease

### 0.3.1 Central Acetylcholinesterase Inhibitors
- **Key agents:** **donepezil, rivastigmine** (oral and transdermal patch), **galantamine**.
- **Mechanism:** inhibit acetylcholinesterase, raising synaptic acetylcholine to compensate for cholinergic neuronal loss.
- **Indications:** **mild-to-moderate Alzheimer disease**; **rivastigmine also has evidence in Parkinson disease dementia and Lewy body dementia** (where it is particularly useful and where antipsychotics are hazardous).
- **Realistic expectations — and this must be explained honestly to families:** they produce **modest symptomatic benefit and do not modify the disease**. Some patients show stabilisation or small improvement in cognition and function; many show no discernible change. **Set a review point, define what would count as benefit, and stop if there is none.**
- **Adverse effects — predictably cholinergic:** **nausea, vomiting, diarrhoea, anorexia and weight loss** (titrate slowly, take with food); **BRADYCARDIA, heart block and syncope** — a genuinely important and under-recognised cause of **falls and collapse in older people**, and a reason to **check the pulse and consider an ECG before and during treatment**; vivid dreams and insomnia; muscle cramps; urinary frequency; and worsening of asthma, COPD and peptic ulcer disease.
- **Interactions:** additive bradycardia with **beta-blockers, digoxin, verapamil and diltiazem**; **antagonised by anticholinergic drugs** — and prescribing an anticholinergic (for bladder, for example) alongside a cholinesterase inhibitor is a common and self-defeating combination.

### 0.3.2 NMDA Receptor Antagonists
- **Key agent:** **memantine**.
- **Mechanism:** low-affinity, uncompetitive NMDA receptor antagonism, reducing glutamatergic excitotoxicity while preserving physiological signalling.
- **Indications:** **moderate-to-severe Alzheimer disease**, alone or with a cholinesterase inhibitor.
- **Adverse effects:** generally better tolerated than the cholinesterase inhibitors — dizziness, headache, constipation, confusion and hypertension. **Renally cleared — dose-adjust in renal impairment.**

### 0.3.3 Other Drugs for Alzheimer's Disease
- **Anti-amyloid monoclonal antibodies — lecanemab, donanemab.** The first agents with a disease-modifying signal, but with **ARIA (amyloid-related imaging abnormalities — oedema and haemorrhage)** requiring MRI surveillance, **APOE ε4 genotype-dependent risk**, high cost, and a modest clinical effect. **Australian availability and criteria are evolving — check the current position rather than relying on this note.**
- **Managing behavioural and psychological symptoms of dementia — the area where an intern is most likely to cause harm:**

> [!danger] **ANTIPSYCHOTICS IN DEMENTIA INCREASE MORTALITY AND STROKE, AND ARE OVER-USED AS CHEMICAL RESTRAINT.**
> **Non-pharmacological approaches come first and work:** look for and treat **pain (a very common unrecognised cause of agitation), infection, constipation, urinary retention, dehydration, sensory impairment, and delirium**; address environment, routine, activity and carer approach.
> **If an antipsychotic is genuinely necessary** (severe distress or risk that has not responded to other measures), **use the lowest dose for the shortest time, document the indication and the consent discussion, and set an explicit review and stop date.**
> **AVOID ANTIPSYCHOTICS ENTIRELY IN LEWY BODY DEMENTIA AND PARKINSON DISEASE DEMENTIA** — severe neuroleptic sensitivity reactions occur, which can be fatal. **Quetiapine or clozapine only, on specialist advice.**
> **Benzodiazepines worsen confusion and falls**, and **anticholinergic drugs worsen cognition** — review the whole medication list, which is often the single most effective intervention.
- **Also address:** cardiovascular risk factors, depression (which mimics and worsens dementia), hearing and vision, driving assessment, advance care planning, carer support and My Aged Care referral. See [[18_Geriatrics_and_Older_Persons_Health]].

## 0.4 Drugs for Multiple Sclerosis

- **Acute relapse:** **high-dose corticosteroids** (oral or intravenous methylprednisolone) — they **shorten the relapse but do not change long-term disability**; plasma exchange for steroid-refractory severe relapse. **Exclude infection first** — a urinary tract infection commonly causes pseudo-relapse (Uhthoff phenomenon) and steroids would be the wrong answer.
- **Disease-modifying therapies, roughly by potency:**
  - **Injectable/moderate efficacy:** **interferon beta** (flu-like symptoms, injection site reactions, LFT and FBC monitoring, depression); **glatiramer acetate** (injection site reactions and a benign but alarming post-injection systemic reaction).
  - **Oral:** **dimethyl fumarate** (flushing, GI upset, lymphopenia, **PML risk with prolonged lymphopenia**); **teriflunomide** (**teratogenic, with a long half-life requiring accelerated elimination with colestyramine before pregnancy** — this applies to **male patients too**); **fingolimod and siponimod** (S1P modulators — **first-dose bradycardia requiring cardiac monitoring**, macular oedema, lymphopenia, and **severe rebound disease activity on stopping**); **cladribine**.
  - **High-efficacy infusions:** **natalizumab** (very effective, but **PML risk stratified by JC virus antibody status, prior immunosuppression and treatment duration — JCV serology monitoring is mandatory**); **ocrelizumab and rituximab** (anti-CD20 — infusion reactions, hypogammaglobulinaemia, infection, and **hepatitis B reactivation — screen first**); **alemtuzumab** (profound and durable effect, but **secondary autoimmunity — thyroid disease, ITP and anti-GBM disease — occurring years later, requiring monthly monitoring for 4 years**).
- **Symptomatic treatment, which often matters more to the patient than the DMT:** **spasticity** (baclofen, tizanidine, botulinum toxin, intrathecal baclofen — see 0.6); **fatigue** (amantadine, modafinil, exercise); **bladder dysfunction** (antimuscarinics, intermittent catheterisation, botulinum toxin); **neuropathic pain** (0.6); **depression**; **tremor**; and **sexual dysfunction**.

> [!danger] **Before and during any MS disease-modifying therapy: screen for latent TB, hepatitis B and C, HIV and (for some agents) JC virus and varicella immunity; VACCINATE BEFORE STARTING, including live vaccines; and counsel about PREGNANCY** — several agents are teratogenic and some require washout. **New or progressive neurological symptoms in a patient on natalizumab, dimethyl fumarate or an anti-CD20 agent raise PML, not a relapse** — that distinction requires urgent MRI and specialist input, and getting it wrong (treating PML with steroids as a relapse) is harmful. See [[04_Neurology]].

## 0.5 Drugs for Myasthenia Gravis

- **Acetylcholinesterase inhibitors — pyridostigmine** (and neostigmine). **Symptomatic only — they do not modify the disease.** Adverse effects are **muscarinic**: abdominal cramps, diarrhoea, salivation, sweating, bradycardia — often managed with an antimuscarinic such as propantheline.
- **Immunosuppression — the actual treatment:** **corticosteroids** (**started at low dose and increased slowly, because a high starting dose can precipitate a transient but severe deterioration**), **azathioprine, mycophenolate, methotrexate, ciclosporin, tacrolimus**; **rituximab** (particularly effective in MuSK-antibody disease); and the newer targeted agents — **complement inhibitors (eculizumab, ravulizumab — meningococcal vaccination mandatory)** and **FcRn antagonists (efgartigimod)**.
- **Rapid therapies for crisis or pre-operative optimisation:** **intravenous immunoglobulin** and **plasma exchange**.
- **Thymectomy** — for thymoma, and beneficial in selected patients with generalised AChR-antibody disease.

> [!danger] **MYASTHENIC CRISIS AND THE DRUGS THAT PRECIPITATE IT.**
> **Respiratory failure in myasthenia is monitored by SERIAL FORCED VITAL CAPACITY, not by oxygen saturation** — the saturation stays normal until the patient is about to arrest. **A falling FVC, weak cough, bulbar weakness or inability to count aloud means imminent respiratory failure and needs ICU involvement before, not after, decompensation.**
> **Many common drugs worsen myasthenia and can precipitate crisis:** **aminoglycosides, macrolides, fluoroquinolones, telithromycin**, **beta-blockers (including eye drops)**, **magnesium** (including intravenous magnesium in obstetrics), **neuromuscular blockers**, **procainamide and quinidine**, **statins**, **penicillamine**, **chloroquine and hydroxychloroquine**, and **immune checkpoint inhibitors**. **Check every new prescription against a myasthenia list**, and be especially careful with antibiotics in a myasthenic patient with an infection — which is itself a common precipitant.
> **Distinguish myasthenic from cholinergic crisis** (the latter from excess anticholinesterase, with muscarinic features — miosis, salivation, diarrhoea, bradycardia), though in practice both are managed by supporting ventilation and involving neurology.

## 0.6 Drugs for Other Neurological Conditions

- **Neuropathic pain — a very common intern-level prescribing task:**
  - **Gabapentinoids (gabapentin, pregabalin)** — first-line for many neuropathic pain syndromes. **Renally cleared — dose-adjust and reduce in the elderly.** Cause **sedation, dizziness, ataxia, weight gain and peripheral oedema**; **additive respiratory depression with opioids** (a recognised cause of death); and there is **genuine misuse and diversion**, particularly of pregabalin.
  - **Tricyclics (amitriptyline, nortriptyline)** and **SNRIs (duloxetine)** — effective, with duloxetine having specific evidence in diabetic neuropathy. Anticholinergic effects and cardiac conduction risks limit tricyclics in older patients.
  - **Carbamazepine** — **first-line for trigeminal neuralgia specifically**.
  - **Topical lidocaine and capsaicin** — for localised neuropathic pain, and useful where systemic drugs are poorly tolerated.
  - **Opioids work poorly for neuropathic pain** and should not be escalated in its place.
- **Spasticity:** **baclofen** (a GABA-B agonist — **NEVER stop intrathecal or high-dose oral baclofen abruptly: withdrawal causes fever, severe rebound spasticity, rhabdomyolysis, seizures and death**), **tizanidine, dantrolene, benzodiazepines, botulinum toxin**, and intrathecal baclofen pumps.
- **Migraine and cluster headache** — see `NEW_Drugs_03_Analgesics.md` 0.2.
- **Restless legs syndrome** — **check and replace IRON first (ferritin and transferrin saturation, with a higher ferritin target than usual)**; then **gabapentinoids are now generally preferred to dopamine agonists**, because agonists cause **augmentation** (symptoms becoming earlier, more intense and more widespread) and impulse control disorders.
- **Essential tremor** — **propranolol** and **primidone**.
- **Motor neurone disease** — **riluzole** (modest survival benefit); multidisciplinary care, non-invasive ventilation and symptom control matter far more.
- **Huntington disease** — tetrabenazine and deutetrabenazine for chorea (**depression and suicidality are significant risks**).
- **Narcolepsy** — modafinil, armodafinil, sodium oxybate, pitolisant.
- **Raised intracranial pressure and cerebral oedema** — **dexamethasone** for tumour-associated vasogenic oedema (**not for traumatic brain injury or stroke, where it does not help and may harm**); **mannitol and hypertonic saline** for acute rises.
- **Stroke** — thrombolysis and thrombectomy, antiplatelets and anticoagulation, and secondary prevention; see `NEW_Drugs_06_Cardiovascular.md` 0.3 and 0.4.
- **Nimodipine** — specifically to reduce delayed cerebral ischaemia after **aneurysmal subarachnoid haemorrhage**, and it is given orally.

## 0.7 Drugs for Vestibular Disorders

- **Key agents:** **prochlorperazine**, **promethazine and other sedating antihistamines (cyclizine, dimenhydrinate)**, **hyoscine hydrobromide** (motion sickness, including transdermal), **betahistine** (a histamine analogue used in Ménière disease), **benzodiazepines** (short-term only), and **corticosteroids** in vestibular neuritis.
- **Indications:** **acute vestibular syndromes** — vestibular neuritis and labyrinthitis; **Ménière disease**; motion sickness.

> [!danger] **VESTIBULAR SEDATIVES ARE FOR THE FIRST FEW DAYS ONLY — PROLONGED USE PREVENTS RECOVERY.**
> **Central vestibular compensation depends on the brain receiving the abnormal signal and adapting to it.** Suppressing that signal with prochlorperazine or an antihistamine beyond the acute phase **delays or prevents compensation and leaves the patient chronically dizzy.** **Stop them after about 3 days and start VESTIBULAR REHABILITATION exercises**, which are the actual treatment. **Long-term prochlorperazine for "dizziness" is a common, harmful and easily corrected prescribing pattern**, and in older people it additionally causes **parkinsonism, falls and tardive dyskinesia.**

> [!danger] **AND THE MOST IMPORTANT POINT: NOT ALL VERTIGO IS PERIPHERAL. Exclude a posterior circulation STROKE.**
> **Sudden vertigo with any of: new headache or neck pain, focal neurology, dysarthria, dysphagia, diplopia, ataxia out of proportion (unable to sit or walk unaided), direction-changing or vertical nystagmus, or a NORMAL head impulse test — is a stroke until proven otherwise.** The **HINTS examination** outperforms early MRI in trained hands. **Vascular risk factors, sudden onset and inability to walk are the red flags.**
> **BPPV is diagnosed with the Dix-Hallpike manoeuvre and TREATED WITH THE EPLEY REPOSITIONING MANOEUVRE, not with drugs** — vestibular sedatives are ineffective for it and delay the definitive treatment, which takes minutes and works. See [[13_02_ENT_-_Hearing_Loss__Tinnitus__Vertigo__DDx_Charts_]] and [[13_03_ENT_-_Deafness_and_Vertigo_Conditions]].

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Antiepileptics | SUB | yes | |
| 0.1.2 | Benzodiazepines (neurology) | CLS | yes | Status epilepticus. |
| 0.1.3 | Other antiepileptics | CLS | yes | Built as 0.1.1 alongside the major agents, because antiepileptics are chosen comparatively and separating "other" would fragment the group; the decision is stated in the entry. Valproate pregnancy content notes that the Australian regulatory position differs from the UK PREVENT programme. |
| 0.2 | Drugs for parkinsonism | SUB | yes | Opens with the never-omit and never-give-a-dopamine-antagonist rules. |
| 0.2.1 | Dopamine Precursors | CLS | yes | |
| 0.2.2 | Dopamine Agonists (Non-Ergot) | CLS | yes | Built jointly with `Dopamine agonists (parkinsonism)` — same class, two names; both rows mapped. Impulse control disorders given in full. |
| 0.2.2 | Dopamine agonists (parkinsonism) | CLS | yes | As above. |
| 0.2.3 | MAO-B Inhibitors | CLS | yes | |
| 0.2.4 | Anticholinergics | CLS | yes | |
| 0.2.5 | Other drugs for Parkinson's disease | CLS | yes | |
| 0.3 | Drugs for Alzheimer's disease | SUB | yes | |
| 0.3.1 | Acetylcholinesterase Inhibitors (Central) | CLS | yes | Bradycardia and syncope as an under-recognised cause of falls. |
| 0.3.2 | NMDA Receptor Antagonists | CLS | yes | |
| 0.3.3 | Other drugs for Alzheimer's disease | CLS | yes | Carries the antipsychotics-in-dementia warning including Lewy body sensitivity. |
| 0.4 | Drugs for multiple sclerosis | SUB | yes | |
| 0.5 | Drugs for myasthenia gravis | SUB | yes | FVC monitoring and the drugs that precipitate crisis. |
| 0.6 | Drugs for other neurological conditions | SUB | yes | Neuropathic pain, spasticity, restless legs, and others. |
| 0.7 | Drugs for vestibular disorders | SUB | yes | Vestibular sedatives limited to days, and excluding posterior circulation stroke. |

**Rows in file: 18 (7 SUB + 11 CLS). AMH section 15 build-list rows: 18. Section complete.**

> [!note] **One pair of build-list rows is a naming duplicate** (`Dopamine Agonists (Non-Ergot)` / `Dopamine agonists (parkinsonism)`), built once at 0.2.2. **`Other antiepileptics` is built within 0.1.1 rather than as a separate entry**, for the reason stated in that entry.
