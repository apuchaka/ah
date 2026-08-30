---
block: NEW build — Investigations (Haematology, part 2)
source: data/BULK_BUILD_PLAN.md Part A; items from data/build_list_investigations.md
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Investigations: Haematology (Part 2 — completing the category)

> [!danger] **Why this file exists, recorded per CLAUDE.md rules 7 and 8.**
> `NEW_Investigations_Haematology.md` was built during the **timed batching test**, where the instruction was to build **ten related investigations** to measure a build rate. It did exactly that — but `data/BULK_BUILD_PLAN.md` then listed it as **"DONE"**, and the **remaining 17 of the category's 28 rows were never built**. Part A was subsequently declared complete on that basis, which was wrong.
> The gap was found only by **re-deriving every row from `data/build_list_investigations.md` and checking it against the file** — the same technique that found the missing beta-blockers in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`. **This file completes the category.** The correction to the Part A completeness claim is recorded in the build status table below and in `data/BULK_BUILD_PLAN.md`.

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay-dependent values are **omitted with the omission stated in place**.

---

## 0.11 Coagulation Profile (PT/INR, APTT, Fibrinogen, D-dimer)

**D:** The routine screen of the clotting cascade. **PT/INR** assesses the **extrinsic and common** pathways (factors VII, X, V, II, fibrinogen); **APTT** assesses the **intrinsic and common** pathways (XII, XI, IX, VIII, X, V, II, fibrinogen); **fibrinogen** and **D-dimer** complete the picture.

**Ind:** Bleeding or bruising; before invasive procedures in at-risk patients; monitoring warfarin (INR) and unfractionated heparin (APTT); suspected liver disease, DIC or massive transfusion; suspected inherited bleeding disorder; suspected antiphospholipid syndrome.

**Role:** A **screen that localises the problem to a part of the cascade** — it does not identify the factor, and it does not measure bleeding risk directly.

> [!info] **Reading the pattern is the skill**
> - **Isolated prolonged PT/INR** → factor **VII** deficiency; **early liver disease**; **early vitamin K deficiency or warfarin** (factor VII has the shortest half-life, so it falls first).
> - **Isolated prolonged APTT** → haemophilia A (**VIII**) or B (**IX**), factor XI or XII deficiency, **von Willebrand disease**, heparin, or a **lupus anticoagulant**.
> - **Both prolonged** → liver disease, **DIC**, vitamin K deficiency, massive transfusion, common pathway factor deficiency.
> - **Both normal in a patient who is clearly bleeding** → **platelet disorder, von Willebrand disease, factor XIII deficiency, or a vascular/connective tissue cause.** The coagulation screen is normal in all of them, and this is the trap.

> [!warning] **The MIXING STUDY is the next step and it separates the two possibilities.** Mix the patient's plasma 1:1 with normal plasma: **if it CORRECTS, it is a factor DEFICIENCY** (the normal plasma supplies the missing factor); **if it does NOT correct, there is an INHIBITOR** — a lupus anticoagulant (thrombosis risk) or a factor inhibitor such as acquired haemophilia (bleeding risk). **The same prolonged APTT therefore means opposite things**, and the mixing study is what tells them apart. See `NEW_Investigations_Cardiology.md` 0.1.

> [!danger] **Do not ignore**
> - **Pre-analytical error is the commonest cause of a wrong result:** an underfilled citrate tube (wrong blood-to-anticoagulant ratio), a difficult or clotted collection, a sample taken from a **heparinised line** (a classic and very common false result — always flush and discard, or take from elsewhere), and delayed processing.
> - **The INR is only validated for warfarin.** Using it to grade liver disease severity is done (Child-Pugh, MELD) but it is not a warfarin-equivalent measure, and **DOACs affect the PT and APTT unpredictably** — a normal or abnormal screen does not tell you whether a DOAC is present or at what level.
> - **A normal coagulation screen does NOT exclude a bleeding disorder** — take a proper **bleeding history** (menorrhagia, dental extractions, surgery, postpartum haemorrhage, family history) and use a structured bleeding assessment tool, because history outperforms the screen.
> - **Do not "correct" an abnormal INR with FFP before a procedure reflexively** — the evidence for benefit is poor and transfusion carries real harm; discuss with haematology.
> - **D-dimer is a rule-out test only, in a patient with a low or intermediate pre-test probability.** It is raised by age, pregnancy, infection, malignancy, surgery, trauma and inflammation, and **must never be used alone to rule in thrombosis.**

**Normal/abnormal:** Laboratory reference intervals, with the **INR target set by indication** for warfarinised patients. **Age-adjusted D-dimer thresholds** exist and are laboratory-specific; the numeric cut-offs are **not stated here**.

**Alt:** Individual **factor assays**; **mixing studies**; **thromboelastography/ROTEM** (viscoelastic point-of-care testing in trauma, cardiac surgery and obstetric haemorrhage, which assesses clot formation and lysis as a whole and guides targeted product use); anti-Xa assay for LMWH and specific DOAC assays; platelet function testing; **FBC and film**. See [[10_07_Haemonc_-_Platelet_and_Clotting_Disorders__Neutropaenia]].

## 0.12 Factor VIII Assay

**D:** A functional (one-stage clotting or chromogenic) assay measuring **factor VIII activity**, reported as a percentage of normal or in IU/dL.

**Ind:** **Prolonged APTT**; suspected or known **haemophilia A**; suspected **von Willebrand disease** (where factor VIII is carried and stabilised by VWF, so it falls when VWF falls); **acquired haemophilia** (an autoantibody, typically in an older person or postpartum, presenting with sudden severe bleeding and no prior history); monitoring factor replacement; pre-operative assessment in a known carrier or patient.

**Role:** Distinguishes haemophilia A from haemophilia B and from von Willebrand disease, and **grades severity**, which determines bleeding phenotype and treatment.

> [!info] **Severity bands (factor activity)** — sources agree: **severe <1%** (spontaneous joint and muscle bleeds), **moderate 1–5%** (bleeding with minor trauma), **mild 5–40%** (bleeding with surgery or significant trauma, often diagnosed late or after a procedure).

> [!danger] **Do not ignore**
> - **Haemophilia A is X-linked recessive** — but **carrier females can have low levels and can bleed**, particularly with menorrhagia and childbirth, and they must not be dismissed as "just carriers".
> - **Factor VIII is an ACUTE-PHASE REACTANT** — it rises with inflammation, pregnancy, exercise, stress and oestrogen. **A "normal" level taken during acute illness can conceal mild haemophilia or type 1 von Willebrand disease**, so equivocal results are repeated in a well, unstressed state.
> - **INHIBITORS (alloantibodies) are the major complication of treatment** and cause factor replacement to stop working — suspect them when a treated patient stops responding, and quantify with a **Bethesda assay**.
> - **A bleeding haemophiliac gets factor FIRST.** Do not delay replacement for imaging or investigation — head injury in particular is treated presumptively and urgently, and **any head strike in a severe haemophiliac is treated as intracranial bleeding until excluded.**
> - **Avoid intramuscular injections, aspirin and NSAIDs**, and involve the haemophilia treatment centre in every presentation.

**Normal/abnormal:** As the severity bands above, against the laboratory's reference range. Note that **one-stage and chromogenic assays can disagree** in some variants.

**Alt:** **Factor IX assay** (haemophilia B); **VWF antigen and activity** (0.13); mixing study; **Bethesda inhibitor assay**; genetic testing for the family; **FBC and coagulation screen** (0.11). See [[10_07_Haemonc_-_Platelet_and_Clotting_Disorders__Neutropaenia]].

## 0.13 von Willebrand Factor Antigen and Ristocetin Cofactor Activity

**D:** Two halves of the same question, always interpreted together with factor VIII.
- **VWF antigen (VWF:Ag)** — **how much** VWF protein is present (quantity).
- **VWF activity — the ristocetin cofactor assay (VWF:RCo)** and its modern automated equivalents — **how well it works** (function). Ristocetin induces VWF to bind platelet GPIb, so the assay detects **functional defects that a quantitative antigen assay cannot see**. Sources note that many contemporary automated systems no longer use platelets, instead relying on **latex particle agglutination** measured immunoturbidimetrically on routine coagulation analysers.

**Ind:** Easy bruising, **menorrhagia**, epistaxis, prolonged bleeding after dental work or surgery, postpartum haemorrhage, and a family history of bleeding. **Von Willebrand disease is the commonest inherited bleeding disorder and is substantially under-diagnosed, particularly in women**, in whom heavy menstrual bleeding is normalised for years.

**Role:** Diagnoses and **subtypes** von Willebrand disease — and the subtype determines treatment.

> [!info] **The activity-to-antigen ratio is what separates the types**
> - **Type 1 (~75%, quantitative partial deficiency):** VWF:Ag and activity **both reduced proportionately**; **ratio normal**. Factor VIII often mildly reduced.
> - **Type 2 (qualitative defect):** **activity reduced OUT OF PROPORTION to antigen** — sources describe a normal or near-normal antigen with reduced ristocetin cofactor activity as pointing to type 2, with an **abnormally increased activity:antigen discrepancy** triggering reflex ristocetin cofactor testing and, subsequently, **multimer analysis** to determine the subtype (2A, 2B, 2M, 2N).
> - **Type 3 (rare, severe):** **VWF essentially absent**, with markedly low factor VIII — clinically resembling haemophilia.

> [!danger] **Do not ignore**
> - **VWF is an ACUTE-PHASE REACTANT and rises with inflammation, stress, exercise, pregnancy, oestrogen (including the combined oral contraceptive) and with blood group.** **Levels are physiologically LOWER in blood group O.** A single normal result does **not** exclude von Willebrand disease — **repeat testing on more than one occasion in a well state is standard**, and the history matters more than one number.
> - **Type 2B is the exception that changes management: DESMOPRESSIN IS CONTRAINDICATED** because it releases abnormal VWF that binds platelets and causes **thrombocytopenia**. Subtyping therefore precedes treatment.
> - **Menorrhagia in an adolescent that has been heavy since menarche warrants a bleeding disorder work-up**, not just an oral contraceptive.
> - **Tranexamic acid is a genuinely useful and under-used treatment** in mild disease and in menorrhagia (see `NEW_Drugs_06_Cardiovascular.md` 0.5).

**Normal/abnormal:** Laboratory-specific reference ranges; sources describe a **VWF activity below about 55%, or an abnormally increased activity:antigen ratio**, as the trigger for reflex ristocetin cofactor testing in one laboratory's protocol. **Diagnostic cut-offs are laboratory- and assay-specific and are not stated here.**

**Alt:** **Factor VIII assay** (0.12); **VWF multimer analysis** and collagen-binding assay for subtyping; **VWF:FVIII binding assay** for type 2N; platelet function analysis; genetic testing; and — before all of them — a **structured bleeding assessment tool**.

## 0.14 ADAMTS13 Activity

**D:** A functional assay of **ADAMTS13**, the plasma metalloprotease that cleaves ultra-large von Willebrand factor multimers. Reported as a percentage of normal activity, with an accompanying **inhibitor/antibody assay** where activity is low.

**Ind:** **Suspected thrombotic thrombocytopenic purpura (TTP)** — the essential test; and differentiation of the thrombotic microangiopathies.

**Role:** Confirms TTP and separates it from the other causes of **microangiopathic haemolytic anaemia with thrombocytopenia** — HUS, complement-mediated (atypical) HUS, DIC, malignant hypertension, HELLP, and drug-induced microangiopathy — which have entirely different treatments.

> [!info] **Interpretation.** Sources are consistent: **immune-mediated TTP presents with ADAMTS13 activity <10%**, and one assay evaluation reported **sensitivity 100% and specificity 99%**. A low activity with a demonstrable inhibitor indicates **acquired (immune) TTP**; low activity without an inhibitor raises **congenital TTP (Upshaw-Schulman syndrome)**.

> [!danger] **DO NOT WAIT FOR THE RESULT. Sources state this explicitly: the decision to start plasma exchange must not be delayed pending the ADAMTS13 assay.**
> **Untreated TTP has a mortality approaching 90%; with prompt plasma exchange it falls dramatically.** The assay is usually a **send-away test with a turnaround of days**, so it confirms the diagnosis retrospectively and guides ongoing therapy — it does not gate treatment.
> **Take the sample BEFORE plasma exchange or any plasma product**, because transfused plasma supplies ADAMTS13 and destroys the result.
> **Recognise TTP clinically:** **microangiopathic haemolytic anaemia (anaemia, raised LDH, low haptoglobin, SCHISTOCYTES/red cell fragments on the film) plus thrombocytopenia**, with neurological features, renal impairment and fever variably present — **the classic pentad is present in a minority and waiting for it is dangerous.** The **PLASMIC score** helps stratify probability while the assay is pending. **A normal coagulation screen distinguishes TTP from DIC.**

> [!danger] **Do not ignore**
> - **PLATELET TRANSFUSION IS RELATIVELY CONTRAINDICATED in TTP** — it can fuel further microvascular thrombosis. Do not treat the low platelet count as if it were ITP or marrow failure.
> - **Urgent haematology involvement is mandatory**; treatment is **plasma exchange plus corticosteroids**, with **rituximab** and **caplacizumab** in current regimens.
> - **Look for a trigger:** drugs (quinine, clopidogrel, ticlopidine, calcineurin inhibitors, gemcitabine), pregnancy, HIV, autoimmune disease, malignancy.

**Normal/abnormal:** Activity as a percentage, with **<10% supporting TTP**; interpreted with the inhibitor assay and the clinical picture.

**Alt:** **Blood film for schistocytes — the immediate bedside-equivalent test**; FBC, reticulocytes, LDH, haptoglobin, bilirubin, direct antiglobulin test (**negative** in microangiopathy); coagulation screen and fibrinogen (to exclude DIC); renal function; **stool testing for Shiga toxin / STEC** in suspected typical HUS; complement studies in atypical HUS; pregnancy test. See [[10_07_Haemonc_-_Platelet_and_Clotting_Disorders__Neutropaenia]] and [[15_11_Paeds_-_Urological_and_Renal_Anomalies__Wilms_Tumour__HUS]].

## 0.15 HIT ELISA (Anti-PF4/Heparin Antibody Immunoassay)

**D:** An **enzyme immunoassay** detecting antibodies against **platelet factor 4 (PF4) complexed with heparin** — the immune basis of heparin-induced thrombocytopenia.

**Ind:** Suspected **HIT**, in a patient with an **intermediate or high 4Ts score** (see `NEW_Drugs_06_Cardiovascular.md` 0.1.2). **It should not be sent in low-probability patients** — doing so generates false positives and unnecessary switching to more expensive, less familiar anticoagulants.

**Role:** A **sensitive screening test with limited specificity** — it detects antibodies, many of which are **clinically irrelevant**, so a positive result must be interpreted with the 4Ts score and, where doubt remains, confirmed functionally (0.16).

> [!info] **Performance.** Sources report a PF4/heparin ELISA sensitivity and specificity of about **87% and 92%** for an in-house assay and **90% and 98%** for a commercial kit. **The high sensitivity means a NEGATIVE test in a low- or intermediate-probability patient effectively excludes HIT** — which is its main clinical value. A **positive** test in a low-probability patient is more likely to be a false positive than HIT.

> [!danger] **Do not wait for the result before acting.**
> **If HIT is clinically suspected, STOP ALL HEPARIN — including flushes and heparin-bonded lines — and START A NON-HEPARIN ANTICOAGULANT immediately.** HIT is **prothrombotic**: the danger is thrombosis, not bleeding, and simply stopping anticoagulation leaves the patient at high risk for weeks. The immunoassay confirms or refutes afterwards.
> **Do NOT give warfarin alone during acute HIT** (venous limb gangrene and skin necrosis), and **do NOT transfuse platelets routinely.**

> [!warning] **Optical density matters.** Many laboratories report a numeric optical density with the qualitative result: **a strongly positive OD correlates much better with true, functionally active HIT than a weakly positive one.** A weak positive with a low 4Ts score usually is not HIT. **Numeric OD thresholds are assay-specific and are not stated here.**

**Normal/abnormal:** Positive or negative, usually with an optical density value; interpreted alongside the 4Ts score and, if needed, a functional assay.

**Alt:** **4Ts score** (the essential first step, and free); **serotonin release assay or heparin-induced platelet activation assay** (0.16) as the confirmatory functional test; **serial platelet counts** (the trigger for suspicion in the first place); imaging for thrombosis, which should be actively sought — including **bilateral leg ultrasound**, since silent DVT is common in HIT.

## 0.16 Serotonin Release Assay (Functional HIT Assay)

**D:** A **functional** assay: donor platelets are loaded with radiolabelled serotonin and incubated with the patient's serum at high and low heparin concentrations. **Release of serotonin at low but not high heparin concentrations** demonstrates that the antibody is genuinely **platelet-activating**. The heparin-induced platelet activation (HIPA) assay is a related functional method.

**Ind:** **Confirmation of HIT** where the immunoassay is positive but the diagnosis remains uncertain, and in high-probability cases where a definitive answer will change long-term management.

**Role:** **The reference standard for HIT** — sources describe HIT being affirmed by demonstrating heparin-dependent anti-platelet antibodies with the ¹⁴C-serotonin release assay. It has **high specificity**, which is exactly what the immunoassay lacks.

> [!warning] **Its limitations are practical rather than analytical.** It is **technically demanding, performed only in specialised reference laboratories, and has a turnaround of days to weeks.** It is therefore a **retrospective confirmation**, never a test that guides the acute decision. **Its main clinical value is for the rest of the patient's life** — a confirmed diagnosis means a permanent, documented heparin allergy label affecting every future admission, dialysis, cardiac surgery and pregnancy; an excluded diagnosis returns a useful and often necessary drug to the patient.

> [!danger] **Do not ignore**
> - **The diagnostic sequence is: 4Ts score → PF4 immunoassay if intermediate or high → functional assay to confirm.** Skipping to the functional assay wastes a scarce test; skipping the 4Ts score generates false positives.
> - **Whatever the assay shows, the acute management is decided clinically** (see 0.15) — a functional assay result arriving a week later cannot help the patient who is clotting today.
> - **Document the outcome explicitly** in the discharge summary, on the allergy list, and to the patient — an unrecorded HIT diagnosis will lead to heparin re-exposure.

**Normal/abnormal:** Positive (serotonin release at low heparin concentrations, suppressed at high) or negative.

**Alt:** **HIT ELISA** (0.15); **4Ts score**; heparin-induced platelet activation and flow-cytometric functional assays; serial platelet counts and imaging for thrombosis.

## 0.17 Flow Cytometry (Immunophenotyping)

**D:** Cells in suspension are labelled with **fluorochrome-conjugated antibodies** against surface and intracellular antigens and passed single-file through a laser, so each cell's **size, granularity and antigen expression** are measured individually. Sources list the usable specimens as **peripheral blood, bone marrow aspirate, fine needle aspirate, body fluids (including CSF) and cell suspensions from fresh tissue.**

**Ind:** Suspected **acute leukaemia** (unexplained cytopenias, blasts on the film, leucocytosis); suspected **lymphoma or chronic lymphoproliferative disorder** (lymphocytosis, lymphadenopathy); **myeloma** (plasma cell phenotyping); **minimal residual disease** monitoring; **paroxysmal nocturnal haemoglobinuria** (loss of CD55/CD59 — the diagnostic test); **CD4 counts in HIV**; **primary immunodeficiency** lymphocyte subsets; fetomaternal haemorrhage quantification (see `NEW_Investigations_Obstetrics_and_Gynaecology.md` 0.9).

**Role:** **Classifies haematological malignancy by lineage and maturation** — sources describe it as essential for the diagnosis and immunologic classification of B-cell ALL, and as a **valuable complement to morphology** that resolves differential diagnostic problems morphology alone cannot.

> [!danger] **The specimen requirement is the thing an intern must get right: flow cytometry needs FRESH, UNFIXED cells.**
> **Send the sample in EDTA or heparin (per your laboratory's requirement), unfixed, and get it to the laboratory promptly** — **formalin destroys the cells and makes flow cytometry impossible**, and the sample usually cannot be retaken without repeating an invasive procedure. **Ring the laboratory before taking the sample**, especially out of hours, because cells degrade and some laboratories cannot process overnight. This is the single commonest practical failure with this test.

> [!warning] **Interpretation is not automatic.** Sources include a case report of **follicular lymphoma in leukaemic phase misdiagnosed as CLL** on flow cytometry — the immunophenotype is read as a pattern in the context of morphology, clinical picture and, usually, cytogenetics and molecular studies. **A single marker never makes a diagnosis.**

> [!danger] **Do not ignore**
> - **Suspected acute leukaemia is an emergency**: check for **tumour lysis** (potassium, phosphate, urate, calcium, renal function), **neutropenic sepsis**, **DIC** (especially in **acute promyelocytic leukaemia**, which is a haematological emergency requiring immediate ATRA and haematology involvement), **hyperleucocytosis and leucostasis**, and anaemia and thrombocytopenia. **Take the samples and call haematology the same day** — do not book an outpatient appointment.
> - **Flow cytometry does not show tissue architecture**, so it does not replace a **lymph node excision biopsy** for lymphoma classification (see `NEW_Investigations_General_and_Preventive.md` 0.10).
> - **Take samples before starting corticosteroids** wherever possible — steroids lyse lymphoblasts and can render the diagnosis unobtainable, which then compromises treatment stratification for the whole illness.

**Normal/abnormal:** Reported as an interpreted **immunophenotype with a diagnosis or differential**, not as raw numbers. Read the conclusion.

**Alt:** **Morphology on blood film and marrow aspirate**; **immunohistochemistry** on fixed tissue (which does show architecture — see `NEW_Investigations_General_and_Preventive.md` 0.11); **cytogenetics and FISH**; **molecular studies and next-generation sequencing**; lymph node or tissue biopsy. See [[10_01_Haemonc_-_Leukaemias_and_Myeloproliferative_Disorders]].

## 0.18 Biopsy and Procedures (Bone Marrow Aspirate and Trephine, Lymph Node Biopsy)

**D:** **Bone marrow aspirate** — liquid marrow drawn from the posterior iliac crest (or sternum in adults, rarely) for **morphology, flow cytometry, cytogenetics, molecular studies and iron staining**. **Trephine biopsy** — a **core of intact bone and marrow** taken through the same site, showing **architecture, cellularity, fibrosis and infiltration** that an aspirate cannot. The two are complementary and are almost always taken together.

**Ind:** Unexplained cytopenias or pancytopenia; suspected **acute leukaemia, myelodysplastic syndrome, myeloproliferative neoplasm, myeloma, lymphoma or aplastic anaemia**; **staging** of lymphoma; unexplained splenomegaly; suspected marrow infiltration by solid tumour; suspected storage disorder; **pyrexia of unknown origin** (with culture, including mycobacterial); assessment of iron stores where serum tests are uninterpretable.

**Role:** The **definitive assessment of haematopoiesis** and the diagnostic procedure for most primary marrow disease.

> [!info] **What each part answers, and why "dry tap" is informative rather than a failure**
> The **aspirate** gives cell detail — blast percentage, dysplasia, plasma cells, iron stores. The **trephine** gives **cellularity relative to age, fibrosis, and the pattern of infiltration**. **A "dry tap" (no aspirable marrow) is itself a finding** — it points to **myelofibrosis, hairy cell leukaemia, or a packed/infiltrated marrow** — and it makes the trephine essential rather than optional.

> [!danger] **Do not ignore**
> - **Coagulopathy and thrombocytopenia must be assessed and, where necessary, corrected** before the procedure. Severe thrombocytopenia is **not** an absolute contraindication (the posterior iliac crest is compressible), but the decision is a haematologist's.
> - **Send the samples correctly and in the right media** — **fresh and unfixed for flow cytometry and cytogenetics, formalin for the trephine, and separate specimens for microbiology culture where infection is a question.** Getting this wrong wastes an invasive procedure.
> - **Take the samples before starting corticosteroids or chemotherapy** where at all possible.
> - **Analgesia and explanation matter.** The procedure is painful — particularly the aspiration itself — and patients should be warned about the brief intense suction sensation, offered adequate local anaesthesia, and considered for sedation. Complications are uncommon but include bleeding, infection, and (with sternal aspiration) very rare but catastrophic mediastinal injury.
> - **Lymph node biopsy for suspected lymphoma should be an EXCISION biopsy of a whole node where feasible** — core biopsy is often adequate but **fine-needle aspiration alone is usually not**, because classification requires architecture. Choose the most abnormal, and not simply the most accessible, node.

**Normal/abnormal:** A descriptive report integrating morphology, cellularity, immunophenotype, cytogenetics and molecular findings into a diagnosis and, where relevant, a risk stratification.

**Alt:** Peripheral **blood film and flow cytometry** (which increasingly answer the question without marrow sampling in some conditions); **imaging including PET/CT** for staging; **tissue biopsy** of an involved site; **liquid biopsy / circulating tumour DNA** in selected settings.

## 0.19 Serum Electrophoresis and Serum Free Light Chain Quantification

**D:** **Serum protein electrophoresis (SPEP)** separates serum proteins by charge, revealing a **monoclonal band (M-band or paraprotein)**; **immunofixation/immunotyping** identifies its heavy and light chain class; **serum free light chain (sFLC) assay** measures unbound κ and λ chains and — critically — their **ratio**.

**Ind:** Suspected **myeloma** (bone pain, pathological fracture, unexplained anaemia, renal impairment, hypercalcaemia, very high ESR); **amyloidosis**; monoclonal gammopathy of undetermined significance monitoring; peripheral neuropathy of unknown cause; recurrent infection; and **monitoring response to treatment**.

**Role:** Detects, characterises and **quantifies** the monoclonal protein — and the sFLC ratio provides a sensitive measure of clonal burden that the electrophoresis alone cannot.

> [!danger] **The myeloma screen is a SET of tests and ordering only the electrophoresis misses cases.**
> **SPEP alone misses light-chain-only myeloma** — roughly a fifth of cases — because those patients produce no intact immunoglobulin and therefore no serum M-band. **The screen is: serum electrophoresis + immunofixation + SERUM FREE LIGHT CHAINS, plus urine for Bence-Jones protein.** Reporting "electrophoresis negative" as excluding myeloma is a recognised and serious error. (See also `NEW_Investigations_Orthopaedics_Neurology_and_Other.md` 0.8, which covers the same panel from the orthopaedic back-pain angle.)

> [!warning] **The free light chain RATIO, not the absolute value, is the meaningful result — and the reference range differs in renal impairment.** Light chains are renally cleared, so both κ and λ rise together when the kidneys fail; **a renal reference range for the κ:λ ratio must be applied** or normal renal impairment will be read as a clone.

> [!danger] **Do not ignore**
> - **A paraprotein without end-organ damage is MGUS, not myeloma.** Myeloma requires the **CRAB** features — hyperCalcaemia, Renal impairment, Anaemia, Bone lesions — or a defined biomarker of malignancy. MGUS is common, increases with age, and needs lifelong monitoring rather than treatment.
> - **AL amyloidosis can present with a small or even absent M-band but an abnormal free light chain ratio** — think of it in unexplained nephrotic syndrome, cardiomyopathy with a low-voltage ECG, hepatomegaly, macroglossia, periorbital purpura, or carpal tunnel syndrome. It needs tissue biopsy with **Congo red** staining and specialist referral.
> - **Hypercalcaemia with renal impairment and anaemia in an older patient is myeloma until excluded**, and hypercalcaemia itself is an emergency.
> - **A normal bone scan does not exclude myeloma** (lesions are lytic without osteoblastic response) — imaging is **whole-body low-dose CT, MRI or PET/CT**.
> - **Avoid nephrotoxins and contrast** where myeloma with renal impairment is suspected, and maintain hydration.

**Normal/abnormal:** Presence, class and **quantity** of any monoclonal band; free light chains as absolute κ and λ with the **κ:λ ratio** against the appropriate (renal or non-renal) range. **Numeric diagnostic thresholds are not stated here** — the criteria are specialist, assay-dependent and periodically revised.

**Alt:** **Urine electrophoresis and immunofixation** (Bence-Jones protein); **urine protein:creatinine ratio**; FBC and film (**rouleaux**), calcium, renal function, albumin, LDH, **β₂-microglobulin** (0.20); **bone marrow aspirate and trephine with cytogenetics — the diagnostic test** (0.18); **whole-body low-dose CT / MRI / PET-CT**; tissue biopsy with Congo red for amyloid. See [[10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma]].

## 0.20 Beta-2 Microglobulin

**D:** The **light chain of the MHC class I molecule**, shed from the surface of all nucleated cells and **cleared almost entirely by the kidney** — filtered at the glomerulus and reabsorbed and catabolised in the proximal tubule.

**Ind:** **Staging and prognosis in multiple myeloma** — it is a component of the **International Staging System**; prognosis in **lymphoma and CLL**; monitoring in some lymphoproliferative disorders; and, in nephrology, as a marker of **proximal tubular dysfunction** and of dialysis-related amyloidosis.

**Role:** A **prognostic marker reflecting both tumour burden and renal function** — which is exactly why it is useful in myeloma staging (where both matter) and useless as a diagnostic test.

> [!danger] **It is NOT a diagnostic or screening test for any malignancy.** Sources note it is elevated in lymphoproliferative disease with abnormal levels indicating potentially worse disease characteristics — but it is also raised by **any renal impairment**, by **infection (notably HIV and CMV)**, by **inflammatory and autoimmune disease**, and by **liver disease**. **A raised β₂-microglobulin in isolation means very little**, and it must never be used to look for cancer in an undifferentiated patient.

> [!warning] **The renal confound is the whole interpretive problem.** Because it is renally cleared, a raised level in a myeloma patient may reflect **the myeloma, the renal impairment the myeloma caused, or unrelated kidney disease** — which is precisely why the ISS combines it with **serum albumin** rather than using it alone, and why the revised staging system adds cytogenetics and LDH.

**Normal/abnormal:** Laboratory reference interval; **staging thresholds are part of formal, periodically revised staging systems and are not reproduced here** — they must come from the current criteria, not from a note.

**Alt:** **Serum albumin, LDH and cytogenetics** — the other components of myeloma staging; **serum and urine electrophoresis and free light chains** (0.19); renal function; imaging; bone marrow examination (0.18). See [[10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma]].

## 0.21 Osmotic Fragility Test

**D:** Red cells are incubated in **progressively hypotonic saline** and the concentration at which haemolysis occurs is measured. **Spherocytes**, having lost membrane surface area relative to volume, tolerate less water entry and **lyse at higher (less hypotonic) concentrations** — increased osmotic fragility.

**Ind:** Suspected **hereditary spherocytosis** — a Coombs-negative haemolytic anaemia with spherocytes on the film, splenomegaly, jaundice, pigment gallstones, and a family history.

**Role:** A **historical test that has largely been superseded**, retained here because the name persists in teaching and in older records.

> [!warning] **Its limitations are why it was replaced**
> - **Neither sensitive nor specific.** It is **normal in a significant minority of patients with hereditary spherocytosis** (particularly mild cases), and it is **abnormal in any condition producing spherocytes** — including **autoimmune haemolytic anaemia**, which is a completely different disease with completely different management.
> - **Recent transfusion invalidates it**, because donor cells dominate the sample.
> - **Coexisting iron deficiency masks it** (iron-deficient cells are relatively resistant to osmotic lysis), so a patient with both can test normal.
> - **Incubated (24-hour) osmotic fragility** is more sensitive than the immediate test but is slower and still imperfect.

> [!info] **What has replaced it: the EMA (eosin-5-maleimide) binding test by flow cytometry**, which measures band 3 protein and is more sensitive and specific and much faster, usually combined with the **acidified glycerol lysis test** or **cryohaemolysis**, and with **genetic testing** where the diagnosis remains unclear. **If your laboratory offers EMA binding, request that instead.**

> [!danger] **Do not ignore**
> - **The FIRST test in a spherocytic haemolytic anaemia is the DIRECT ANTIGLOBULIN TEST (Coombs).** **A positive DAT means autoimmune haemolytic anaemia, not hereditary spherocytosis** — and the treatments (immunosuppression versus supportive care and, sometimes, splenectomy) are opposite. Never order an osmotic fragility test before a DAT.
> - **Parvovirus B19 causes APLASTIC CRISIS in hereditary spherocytosis and other chronic haemolytic states** — a sudden fall in haemoglobin with a **low reticulocyte count** in a patient with known haemolysis is aplastic crisis until proven otherwise, and needs urgent transfusion support.
> - **Folate supplementation** is standard in chronic haemolysis, and **gallstones** should be anticipated.
> - **Splenectomy** (which is not undertaken lightly, and requires **vaccination against encapsulated organisms and long-term antibiotic prophylaxis and education**) is reserved for significant disease. See [[10_05_Haemonc_-_Normocytic_Anaemia_and_Sickle_Cell_Disease]].

**Normal/abnormal:** Increased fragility supports spherocytosis; a normal result does not exclude it.

**Alt:** **EMA binding test by flow cytometry — the current test of choice**; acidified glycerol lysis test; cryohaemolysis; **blood film** (the first and most informative test); **direct antiglobulin test** (mandatory first); reticulocytes, bilirubin, LDH and haptoglobin; genetic testing of the membrane protein genes.

## 0.22 Sickle Cell Prep (Sickle Solubility Test)

**D:** A **solubility screening test**: deoxygenating reagent is added to blood, and **haemoglobin S polymerises and precipitates**, producing turbidity. A positive test means **haemoglobin S is present** — nothing more.

**Ind:** Screening for haemoglobin S — historically in emergency, pre-operative and antenatal settings, and in family and population screening.

**Role:** **A screening test that is now largely obsolete in Australian practice**, because it answers only half the question.

> [!danger] **THE CRITICAL LIMITATION: the sickle solubility test CANNOT DISTINGUISH SICKLE CELL TRAIT (HbAS) FROM SICKLE CELL DISEASE (HbSS), or from the compound heterozygous states (HbSC, HbS/β-thalassaemia).**
> It is **positive in all of them** — and their clinical implications could hardly be more different. **A positive test must always be followed by HAEMOGLOBIN ELECTROPHORESIS OR HPLC** to quantify the haemoglobin fractions and make the actual diagnosis. Acting on a positive solubility test alone — labelling a trait carrier as having sickle cell disease, or vice versa — has real consequences for the patient, for anaesthetic planning, and for genetic counselling.

> [!warning] **Other failure modes**
> - **FALSE NEGATIVE in infants under about 6 months**, because **fetal haemoglobin still predominates** and HbS levels are too low — which is exactly the age at which newborn screening is instead done on the bloodspot by electrophoresis/HPLC.
> - **False negative** in severe anaemia and after recent transfusion (donor HbA dilutes the sample).
> - **False positive** in hyperproteinaemia, hyperlipidaemia, and other rare sickling haemoglobin variants.

> [!danger] **Do not ignore**
> - **Sickle cell TRAIT is usually benign but is not entirely without consequence** — it is associated with **renal medullary carcinoma (rare but important), papillary necrosis and haematuria, hyposthenuria, splenic infarction at altitude, and exertional rhabdomyolysis under extreme conditions.** It should be **documented and communicated for genetic counselling**, since two carriers have a 1-in-4 risk per pregnancy.
> - **Sickle cell DISEASE presenting acutely is a medical emergency**: **vaso-occlusive crisis needs prompt, adequate analgesia — often opioids — without delay or suspicion**, alongside hydration, oxygen, and a search for the precipitant (infection, dehydration, cold, hypoxia). **Acute chest syndrome, stroke, splenic sequestration, aplastic crisis and priapism are the life- and organ-threatening complications.** Patients are **functionally hyposplenic** and at risk from encapsulated organisms — fever is treated urgently.
> - **Under-treatment of sickle pain in emergency departments is a well-documented failure with a racial dimension.** Believe the patient, use their individualised plan where one exists, and involve haematology.
> - See [[10_05_Haemonc_-_Normocytic_Anaemia_and_Sickle_Cell_Disease]] and [[15_14_Paeds_-_Anaemia__Sickle_Cell__Hereditary_Spherocytosis__HSP]].

**Normal/abnormal:** Positive (HbS present, type undetermined) or negative.

**Alt:** **Haemoglobin electrophoresis or HPLC — the definitive test** (built as 0.9 of `NEW_Investigations_Haematology.md`); **newborn bloodspot screening**; blood film (sickle cells, target cells, Howell-Jolly bodies indicating hyposplenism); FBC and reticulocytes; **genetic testing** for antenatal diagnosis and family screening.

## 0.23 Schilling Test

**D:** A historical, multi-stage test of **vitamin B₁₂ absorption**, using **radiolabelled B₁₂** given orally with an intramuscular unlabelled flushing dose, and measuring **urinary excretion of the label**. A second stage repeated **with intrinsic factor** distinguished **pernicious anaemia** (corrected by intrinsic factor) from **intestinal malabsorption** (not corrected).

**Ind:** **None in current practice.**

**Role:** **Entirely obsolete, and it is included here only because it appears on the build list and persists in older textbooks and exam questions.** It was abandoned because it required **radioisotopes**, a **complete and reliable 24-hour urine collection**, and was **inaccurate in renal impairment** — and because serology and simpler biochemistry answer the question better.

> [!info] **What replaced it, and how the question is actually answered now**
> 1. **Serum B₁₂** — with the caveat that it is an unreliable test at the margins.
> 2. **Metabolites where B₁₂ is borderline: METHYLMALONIC ACID and HOMOCYSTEINE**, both of which rise in true tissue deficiency (**MMA is the more specific for B₁₂**, since homocysteine also rises in folate deficiency). These are built as 0.3 and 0.4 of `NEW_Investigations_Haematology.md`.
> 3. **Anti-intrinsic factor antibodies** — highly **specific but insensitive**, so a positive result confirms pernicious anaemia and a negative one does not exclude it; and **anti-parietal cell antibodies** — sensitive but non-specific. Both are built as 0.5 and 0.6 of `NEW_Investigations_Haematology.md`.
> 4. **Gastroscopy with biopsy** where atrophic gastritis or malignancy is suspected, and **coeliac serology** where malabsorption is the question.

> [!danger] **Do not ignore — the clinical points that outlast the test**
> - **NEUROLOGICAL DAMAGE FROM B₁₂ DEFICIENCY CAN OCCUR WITH A NORMAL FULL BLOOD COUNT AND NO ANAEMIA OR MACROCYTOSIS.** **Subacute combined degeneration of the cord** — dorsal column and corticospinal involvement with paraesthesia, ataxia and weakness — is treatable early and **irreversible late**. Do not wait for a macrocytosis.
> - **TREAT BEFORE FOLATE.** Giving folate to a B₁₂-deficient patient corrects the anaemia while **allowing the neurological disease to progress**. **Check and replace B₁₂ first.**
> - **Look for the cause**, not just the number: pernicious anaemia, **metformin**, **proton pump inhibitors and H₂ antagonists**, gastrectomy or bariatric surgery, terminal ileal disease or resection (Crohn disease), coeliac disease, strict vegan diet, and **nitrous oxide exposure — including recreational use** (see `NEW_Drugs_02_Anaesthetics.md` 0.2.4).
> - **Pernicious anaemia carries an increased risk of gastric carcinoma and carcinoid**, and is associated with other autoimmune disease (thyroid, type 1 diabetes, vitiligo).
> - See [[10_06a_Haemonc_-_Macrocytic_Anaemia]].

**Normal/abnormal:** Not applicable — the test is not performed.

**Alt:** All of the above: serum B₁₂, **MMA and homocysteine**, **anti-intrinsic factor and anti-parietal cell antibodies**, FBC and film, reticulocytes, LDH and bilirubin (ineffective erythropoiesis causes a degree of intramedullary haemolysis), coeliac serology, and endoscopy.

## 0.24 Lymphoscintigraphy

**D:** A nuclear medicine study in which a **radiolabelled colloid (typically Tc-99m)** is injected **intradermally or subcutaneously** and its uptake and transit through **lymphatic channels and nodes** is imaged.

**Ind:** Two distinct purposes.
1. **Sentinel lymph node mapping** before surgery in **melanoma and breast cancer** — identifying which node or nodes drain the tumour so they can be located, excised and examined, avoiding a full nodal dissection in node-negative patients.
2. **Assessment of lymphoedema** — confirming lymphatic obstruction or dysfunction, and distinguishing lymphoedema from venous oedema, lipoedema and other causes of limb swelling.

**Role:** In cancer, it is the **anatomical roadmap for sentinel node biopsy** — a technique that substantially reduced the morbidity of surgical staging. In lymphoedema, it is a **functional** study where the diagnosis is not clinically obvious.

> [!info] **Sentinel node mapping in practice** — lymphoscintigraphy is performed before theatre, usually combined intraoperatively with a **blue dye** and a **handheld gamma probe**. Drainage is not always predictable: **melanoma of the trunk and head and neck in particular can drain to unexpected or multiple basins**, which is precisely why mapping is done rather than assumed.

> [!danger] **Do not ignore**
> - **A negative sentinel node does not exclude metastatic disease** — it substantially lowers the probability, but false negatives occur, and clinical follow-up continues.
> - **In lymphoedema, the priority is excluding a treatable or dangerous cause of the swelling FIRST**: **DVT**, **malignant nodal obstruction or pelvic mass**, cardiac, renal and hepatic causes of oedema, and **infection**. New unilateral limb swelling is investigated, not assumed to be lymphoedema.
> - **CELLULITIS IS THE MAJOR COMPLICATION OF LYMPHOEDEMA and it is recurrent** — patients need skin care education, prompt treatment of breaks and fungal infection between the toes, and sometimes prophylactic antibiotics. Each episode worsens the lymphoedema, creating a cycle.
> - **The mainstay of lymphoedema treatment is not a drug**: **complex decongestive therapy — skin care, manual lymphatic drainage, compression garments and exercise**, delivered by a trained lymphoedema therapist. **Diuretics do not treat lymphoedema** and cause harm if used for it.
> - **A rapidly progressive or painful "lymphoedema", or one with skin change, raises malignancy** — including the rare **angiosarcoma (Stewart-Treves syndrome)** in long-standing post-mastectomy lymphoedema.

**Normal/abnormal:** Reported descriptively — the identity and location of sentinel nodes, or the pattern of lymphatic transit, dermal backflow and collateral formation in lymphoedema.

**Alt:** **Sentinel node biopsy with blue dye and gamma probe** (the procedure lymphoscintigraphy serves); **ultrasound** of nodes with fine-needle aspiration; CT, MRI and **MR lymphangiography**; **indocyanine green near-infrared lymphography** (increasingly used for lymphoedema and surgical planning); **Doppler ultrasound to exclude DVT**; bioimpedance and limb volume measurement for lymphoedema monitoring. See [[10_12_Oncology_-_Breast]].

## 0.25 Petechiae — **UNRESOLVED: not an investigation**

> [!warning] **`Petechiae` appears as a row in the Haematology section of `data/build_list_investigations.md`, but it is a CLINICAL SIGN, not an investigation or bedside test.**
> It is recorded here rather than silently dropped, consistent with the handling of `Fecal Incontinence` (a symptom on the investigations list) and `G-CSF` (a drug on the investigations list) earlier in this build. **Logged as `UNRESOLVED — needs review`** for the person maintaining the build lists: it most likely belongs on the **Presentations & Symptoms** list.

> [!danger] **Because the sign itself is high-stakes, the clinical content is given here rather than omitted entirely.**
> **Petechiae are non-blanching**, which is the finding that separates them from every benign rash — **test with a glass or by pressing.**
> **The investigations a non-blanching rash demands, urgently:** **FBC and film** (is the platelet count low? are there blasts?), **coagulation screen and fibrinogen** (is this DIC?), **renal function and LFTs**, **blood cultures and inflammatory markers**, and a **lactate**.
> **The three diagnoses that must be excluded immediately:**
> 1. **MENINGOCOCCAL SEPSIS** — a non-blanching rash with fever in a child or adult is meningococcaemia until proven otherwise. **Give antibiotics IMMEDIATELY — do not wait for investigations, imaging or transfer.** See [[15_02_Paeds_-_Ill_and_Feverish_Child__Meningitis__Encephalitis]].
> 2. **ACUTE LEUKAEMIA** — petechiae with other cytopenias, bone pain, lymphadenopathy or hepatosplenomegaly.
> 3. **THROMBOTIC MICROANGIOPATHY (TTP/HUS)** — thrombocytopenia with anaemia, schistocytes and renal impairment (see 0.14).
> **Other causes:** immune thrombocytopenia, DIC, drug-induced thrombocytopenia (including **heparin — see 0.15**), marrow failure, vasculitis (**Henoch-Schönlein purpura** — palpable purpura on the buttocks and legs of a child, with a **normal platelet count**), severe vitamin C deficiency, and mechanical causes (coughing, vomiting, tourniquet) which are confined to the head and neck or the limb.
> **A normal platelet count with purpura points to a vascular or vasculitic cause, not a platelet one** — and that distinction is made on the FBC in minutes.

---

## Build status

| # | Build-list row | Built | Notes |
|---|---|---|---|
| 0.11 | Coagulation Profile | yes | Age-adjusted D-dimer thresholds omitted — laboratory-specific. |
| 0.12 | Factor VIII Assay | yes | |
| 0.13 | VWF Antigen | yes | Built jointly with `Ristocetin Cofactor Activity` — the two are a single interpretive unit and separating them would be clinically wrong. |
| 0.13 | Ristocetin Cofactor Activity | yes | As above. |
| 0.14 | ADAMTS13 Activity | yes | |
| 0.15 | HIT ELISA | yes | |
| 0.16 | Serotonin Release Assay | yes | |
| 0.17 | Flow Cytometry | yes | |
| 0.18 | Biopsy & Procedures | yes | Built as bone marrow aspirate + trephine and lymph node biopsy, which is what the row denotes in a haematology context. |
| 0.19 | Serum Electrophoresis | yes | Built jointly with `Serum Free Light Chain Quantification` — ordering one without the other is the error the entry exists to prevent. |
| 0.19 | Serum Free Light Chain Quantification | yes | As above. |
| 0.20 | Beta-2 Microglobulin | yes | Staging thresholds omitted — part of formal, periodically revised staging systems. |
| 0.21 | Osmotic Fragility Test | yes | Flagged as superseded by EMA binding; built rather than dropped because the name persists in teaching. |
| 0.22 | Sickle Cell Prep | yes | |
| 0.23 | Schilling Test | yes | Obsolete; built with what replaced it, because the clinical points outlast the test. |
| 0.24 | Lymphoscintigraphy | yes | |
| 0.25 | Petechiae | **UNRESOLVED — needs review** | **Not an investigation** — a clinical sign miscategorised onto the investigations list. Recorded, with the clinical content given because the sign is high-stakes. |

**Items in file: 15 entries covering 17 build-list rows.**
**Category total: `NEW_Investigations_Haematology.md` (11 rows) + this file (17 rows) = 28 rows = every Haematology row in `data/build_list_investigations.md`. Category now complete.**

> [!danger] **Correction to an earlier claim, per CLAUDE.md rule 8.**
> `NEW_Investigations_Orthopaedics_Neurology_and_Other.md` ends with a note stating **"Part A is now complete."** **That claim was wrong when it was written** — 17 Haematology rows and 2 Infectious Diseases rows were unbuilt at that moment. Both gaps have now been closed (the ID items as 0.22 and 0.23 of `NEW_Investigations_Infectious_Diseases.md`), and `data/BULK_BUILD_PLAN.md` has been corrected.
> **The generalisable lesson: a file listed as "DONE" in a plan is not evidence that it covers its rows.** Completeness must be re-derived from the build list, row by row, against the file's actual content — and the numbering continues from 0.11 in this file specifically so that the two Haematology files read as one continuous category rather than concealing the split.
