---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 19 Rheumatological drugs
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Rheumatological (AMH section 19)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.**

> [!note] **Scope note.** AMH section 19 in the build list is a **single subsection with three classes**. Much of what an intern associates with rheumatology sits in other sections and is cross-referenced rather than duplicated: **NSAIDs and colchicine and the gout drugs** in `NEW_Drugs_03_Analgesics.md`; **methotrexate, biologics, TNF inhibitors and other immunosuppressants** in `NEW_Drugs_14_Immunomodulators_and_Antineoplastics.md` 0.5; **systemic corticosteroids** in `NEW_Drugs_10_Endocrine.md` 0.5.1; and **bisphosphonates and osteoporosis drugs** in `NEW_Drugs_10_Endocrine.md` 0.1.

---

## 0.1 Drugs for Other Musculoskeletal Conditions

> [!info] **The organising principle of modern rheumatology: TREAT TO TARGET, and treat EARLY.**
> In inflammatory arthritis, **the window in which disease-modifying therapy prevents irreversible joint erosion is measured in weeks to months.** **Early referral of suspected inflammatory arthritis — persistent joint swelling, early morning stiffness lasting over 30 minutes, symmetrical small joint involvement, raised inflammatory markers — is one of the highest-value referrals in general practice.** **NSAIDs and steroids relieve symptoms; they do not prevent damage.** Treatment is then escalated at defined intervals until **remission or low disease activity** is achieved, not until the patient merely feels better.

### 0.1.1 Antimalarials as DMARDs
- **Key agents:** **hydroxychloroquine** (and, less commonly, chloroquine).
- **Mechanism:** incompletely understood — lysosomal alkalinisation, interference with antigen processing and **inhibition of toll-like receptor signalling**, producing a mild immunomodulatory effect without general immunosuppression.
- **Indications:** **systemic lupus erythematosus — where it is foundational and should be given to essentially all patients**, reducing flares, organ damage, thrombosis and mortality, and being safe in pregnancy; **rheumatoid arthritis** (mild disease, or as part of combination DMARD therapy); **Sjögren syndrome**; and cutaneous lupus.

> [!danger] **RETINAL TOXICITY — irreversible, and the reason for mandatory ophthalmological screening.**
> Hydroxychloroquine accumulates in the retinal pigment epithelium and can cause a **bull's-eye maculopathy** that **continues to progress even after the drug is stopped** and causes permanent central visual loss. **Risk is related to DAILY DOSE PER ACTUAL BODY WEIGHT and CUMULATIVE DURATION**, and is increased by **renal impairment, concurrent tamoxifen, and pre-existing retinal disease.**
> **Requirements: a baseline ophthalmological assessment within the first year, and regular screening thereafter (annually after about five years of use), using modern sensitive tests — OCT and automated visual fields — not just fundoscopy, because by the time it is visible on fundoscopy the damage is advanced.** **Dose is capped by real body weight.**
- **Other adverse effects:** generally very well tolerated — gastrointestinal upset, rash, and **skin and mucosal hyperpigmentation**; **QT prolongation** (relevant with other QT-prolonging drugs); **haemolysis in G6PD deficiency**; and rarely cardiomyopathy, myopathy and neuropathy with prolonged use.
- **A distinctive strength: it is one of the few immunomodulators that is CONTINUED in pregnancy and breastfeeding** — stopping it in a pregnant woman with lupus precipitates flares and worsens outcomes, and this is a common and harmful error. See [[12_03_Rheum_-_Connective_Tissue_Diseases__SLE__Systemic_Sclerosis__Dermatomyositis__Polymyositis__Sjogren_]].

### 0.1.2 Immunosuppressants (Rheumatology)
- **Conventional synthetic DMARDs:**
  - **Methotrexate** — the **anchor drug of rheumatoid arthritis and psoriatic arthritis**. **ONCE WEEKLY dosing, with folic acid on other days** — see the fatal-error warning in `NEW_Drugs_08_Dermatological.md` 0.3.4. Monitor **FBC, LFTs and renal function**; watch for **mucositis, pneumonitis and hepatic fibrosis**; **teratogenic and abortifacient — contraception is required in both sexes**; and remember the **co-trimoxazole/trimethoprim and NSAID interactions**.
  - **Sulfasalazine** — effective, safe in pregnancy, and useful where methotrexate cannot be used; causes rash, **haemolysis in G6PD deficiency**, **reversible oligospermia**, and folate deficiency.
  - **Leflunomide** — for rheumatoid and psoriatic arthritis. **Teratogenic with a VERY LONG half-life requiring an accelerated elimination procedure with colestyramine before pregnancy — and this applies to male patients too.** Causes hypertension, diarrhoea, hepatotoxicity and peripheral neuropathy.
  - **Azathioprine, mycophenolate, ciclosporin and cyclophosphamide** — for connective tissue disease, vasculitis and organ-threatening manifestations. **Check TPMT/NUDT15 before azathioprine; mycophenolate is teratogenic and requires a pregnancy prevention programme; cyclophosphamide requires MESNA, fertility counselling and preservation.**
- **Biologic and targeted synthetic DMARDs:** **TNF inhibitors**, **IL-6 inhibitors (tocilizumab)**, **B-cell depletion (rituximab)**, **T-cell costimulation blockade (abatacept)**, **IL-17 and IL-23 inhibitors** for spondyloarthritis and psoriatic disease, and **JAK inhibitors (tofacitinib, baricitinib, upadacitinib)**. **Australian PBS authority criteria are specific, require documented failure of conventional DMARDs, and change — check them.** See `NEW_Drugs_14_Immunomodulators_and_Antineoplastics.md` 0.5.3 and 0.5.4 for the class detail.

> [!danger] **BEFORE ANY DMARD, BIOLOGIC OR JAK INHIBITOR — a standing, checkable list that is regularly incomplete:**
> **Screen for latent TUBERCULOSIS, HEPATITIS B and C, and HIV. VACCINATE — including LIVE vaccines — BEFORE starting, because they are contraindicated afterwards. Consider STRONGYLOIDES serology in anyone with relevant exposure. Discuss pregnancy, contraception and fertility. Establish the monitoring schedule and who is doing it.** See `NEW_Drugs_05_Anti_infectives.md` 0.1.2 and 0.6.3.

> [!danger] **AND THE POINT THAT MATTERS MOST ON THE WARD: A FEVER IN A PATIENT ON A DMARD OR BIOLOGIC IS SEPSIS UNTIL PROVEN OTHERWISE, AND THE SIGNS MAY BE BLUNTED.**
> **Withhold the immunosuppressant during serious infection**, take cultures broadly, image with a low threshold, and think about **opportunistic organisms**. **Also consider ADRENAL INSUFFICIENCY** in any hypotensive patient on long-term corticosteroids. **A septic joint in a patient with rheumatoid arthritis is easily dismissed as a flare — aspirate it.** See [[12_01_Rheum_-_Rheumatoid_Arthritis__Osteoarthritis__Psoriatic_Arthritis]].

### 0.1.3 Muscle Relaxants (GABA-B Agonists)
- **Key agent:** **baclofen** (oral and intrathecal); **tizanidine** (an α₂-agonist), **dantrolene** (acting directly on skeletal muscle), **diazepam**, and **botulinum toxin** are the other agents used for spasticity.
- **Mechanism:** **baclofen is a GABA-B receptor agonist** acting at the spinal cord to reduce excitatory transmission and monosynaptic and polysynaptic reflexes.
- **Indications:** **SPASTICITY of central origin — multiple sclerosis, spinal cord injury, cerebral palsy and stroke** — which is its evidence base. It is also used, with much weaker evidence, for musculoskeletal muscle spasm and low back pain.
- **Adverse effects:** **sedation, dizziness, weakness and fatigue** — and **the weakness is the therapeutic problem: reducing tone can remove the spasticity a patient is USING to stand or transfer.** Also confusion (especially in older people), nausea, hypotension, and **lowered seizure threshold**. **Renally cleared — accumulates in renal impairment, where it causes encephalopathy at ordinary doses.**

> [!danger] **BACLOFEN WITHDRAWAL IS A MEDICAL EMERGENCY, AND INTRATHECAL BACLOFEN WITHDRAWAL CAN BE FATAL.**
> Abrupt cessation — including from **a failed or empty intrathecal pump, a disconnected catheter, or simply omitting oral doses in an admitted patient** — causes **high fever, severe rebound spasticity and rigidity, altered mental state, rhabdomyolysis, multi-organ failure and death**, and closely mimics **neuroleptic malignant syndrome, serotonin syndrome and sepsis**.
> **Practical: never omit baclofen in an inpatient; if the patient cannot swallow, find a route; and if a patient with an intrathecal pump becomes unwell with fever and rigidity, think PUMP FAILURE and contact the implanting service urgently.** Treatment is restoring baclofen (oral or intrathecal) plus supportive care and benzodiazepines.
- **Note on the other agents:** **dantrolene is also the antidote in malignant hyperthermia** (see `NEW_Drugs_02_Anaesthetics.md` 0.2.3) and causes **hepatotoxicity** with long-term oral use; **tizanidine** causes hypotension and hepatotoxicity and interacts strongly with **ciprofloxacin and fluvoxamine (CYP1A2)**; and **carisoprodol and orphenadrine-type agents have poor evidence and real misuse potential** — muscle relaxants are not a good long-term answer to back pain.

> [!info] **What actually helps in musculoskeletal conditions, beyond drugs:** **exercise and physiotherapy** (the strongest evidence in osteoarthritis, back pain and inflammatory arthritis alike), **weight management**, **occupational therapy and joint protection**, **hand therapy**, **pain education for chronic pain**, and **surgery where indicated**. **For osteoarthritis specifically, there is no disease-modifying drug** — paracetamol is weakly effective, topical NSAIDs are a good first choice for knee and hand OA, oral NSAIDs work but carry the risks in `NEW_Drugs_03_Analgesics.md` 0.4.2, **opioids perform poorly and cause harm**, and **intra-articular corticosteroid gives short-term relief only**. Saying this honestly to a patient is better than escalating drugs that will not work.

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Drugs for other musculoskeletal conditions | SUB | yes | Framed on treat-to-target and early referral. |
| 0.1.1 | Antimalarials / DMARDs | CLS | yes | Hydroxychloroquine, with the mandatory retinal screening requirement and its continuation in pregnancy. |
| 0.1.2 | Immunosuppressants (rheumatology) | CLS | yes | Conventional synthetic DMARDs given in full; biologics and JAK inhibitors cross-referenced to section 14 rather than duplicated. |
| 0.1.3 | Muscle Relaxants (GABA-B Agonists) | CLS | yes | Baclofen, with the withdrawal emergency including intrathecal pump failure. |

**Rows in file: 4 (1 SUB + 3 CLS). AMH section 19 build-list rows: 4. Section complete.**

> [!note] **This is the smallest section in Part C**, because most rheumatology drug classes are catalogued under other AMH sections in the build list. Those are cross-referenced in the scope note at the top rather than duplicated, so that a single clinical topic does not exist in two places and drift apart.
