---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 7 Blood and electrolytes
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Blood and Electrolytes (AMH section 7)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.** Electrolyte replacement and vitamin dosing are both areas where **paediatric doses are per-kilogram** and an adult figure copied across is dangerous (**CLAUDE.md rule 5**) — take every dose from AMH or the local protocol.

> [!note] **Resolves an item flagged earlier in this build.** `G-CSF` appeared as a row on the **investigations** build list and was logged `UNRESOLVED — needs review` during Part A, because it is a drug and not an investigation. **It belongs here**, and is built at **0.2.3**.

---

## 0.1 Blood Products

- **Scope:** **packed red blood cells**, **platelets**, **fresh frozen plasma (FFP)**, **cryoprecipitate**, and the fractionated products — **albumin**, **immunoglobulin**, **prothrombin complex concentrate**, **fibrinogen concentrate** and specific **clotting factor concentrates**. In Australia these are supplied through **Australian Red Cross Lifeblood** and governed by the **National Blood Authority's Patient Blood Management Guidelines** and the **NSQHS Blood Management Standard**.

> [!info] **What each product is for**
> - **Packed red cells** — to treat **symptomatic anaemia and acute blood loss**, raising oxygen-carrying capacity. Sources describe a **haemoglobin below about 70 g/L** as the commonest trigger in a stable patient, with **higher thresholds in acute coronary syndrome and active bleeding** — but the decision is clinical, not a number alone.
> - **Platelets** — to prevent or treat bleeding in **thrombocytopenia or platelet dysfunction**. Prophylactic thresholds differ from therapeutic ones, and from those before a procedure.
> - **FFP** — replaces **multiple coagulation factors**, for coagulopathy with bleeding, massive transfusion, and DIC. **It is a poor and slow way to reverse warfarin** — prothrombin complex concentrate is far better (see `NEW_Drugs_06_Cardiovascular.md` 0.2).
> - **Cryoprecipitate** — the concentrated **fibrinogen** product (also factor VIII, von Willebrand factor and factor XIII), for **hypofibrinogenaemia**, most often in **massive haemorrhage or consumptive coagulopathy**.
> - **Albumin** — large-volume paracentesis, spontaneous bacterial peritonitis, hepatorenal syndrome, and plasma exchange. **Not a general resuscitation fluid** and not a treatment for a low albumin number.
> - **Immunoglobulin** — replacement in primary and secondary immunodeficiency, and immunomodulation in ITP, Guillain-Barré, CIDP and Kawasaki disease. Supply is restricted by national criteria.

> [!danger] **PATIENT BLOOD MANAGEMENT: the right answer is often not to transfuse.**
> **"One unit at a time, then reassess"** in a stable patient. **Transfusion is not a treatment for a number** — it is a treatment for a patient with symptoms or active loss. The three pillars are: **optimise the patient's own red cell mass** (find and treat iron, B₁₂ and folate deficiency, and treat the cause of the anaemia — see 0.2), **minimise blood loss** (surgical technique, tranexamic acid, avoid excessive phlebotomy), and **optimise tolerance of anaemia**. **A patient transfused for iron deficiency without being given iron and investigated for the source has been actively mismanaged.**

> [!danger] **The bedside checks that prevent the deaths, and they are the intern's job**
> - **Positive patient identification at the bedside, by two people, against the unit and the compatibility label — every single time.** **ABO-incompatible transfusion from a misidentification is the classic fatal error**, and it is a clerical failure, not a laboratory one.
> - **Take the crossmatch sample correctly and label it at the bedside**, handwritten from the patient's own identification. **Never pre-label tubes.**
> - **Obtain and document informed consent**, including the alternatives and the option to decline. Some patients decline on religious grounds — that must be identified early, respected, and planned around.
> - **Baseline observations, then observation during and after** each unit, per the ANZSBT administration guidelines.
> - **Prescribe the rate.** Rapid transfusion in a small, elderly or cardiac-failure patient causes **TACO**.

> [!danger] **Acute transfusion reactions — recognise and act**
> **STOP THE TRANSFUSION, keep the line open with saline, check the patient's identity against the unit, and call for help.** Then distinguish:
> - **Acute haemolytic reaction (ABO incompatibility)** — fever, rigors, loin or chest pain, hypotension, dark urine, DIC, and a sense of impending doom, typically within minutes. **A medical emergency.** Sources note it is typically caused by naturally occurring anti-A or anti-B in the recipient. Resuscitate, maintain urine output, return the unit and samples to the laboratory, and notify.
> - **TACO — transfusion-associated circulatory overload** — pulmonary oedema from volume, with **hypertension** and a raised JVP, in a patient with cardiac or renal impairment or a large or fast transfusion. Treat as pulmonary oedema (sit up, oxygen, diuretic).
> - **TRALI — transfusion-related acute lung injury** — non-cardiogenic pulmonary oedema within 6 hours, with **hypotension** and a normal JVP. Supportive and often needs ventilation. **Sources note TACO and TRALI overlap symptomatically and are both historically under-recognised** — the blood pressure and volume state are the main discriminators.
> - **Febrile non-haemolytic reaction** — common and benign, but a diagnosis of exclusion; never assume it before excluding haemolysis and sepsis.
> - **Anaphylaxis** — treat with adrenaline (see `NEW_Drugs_01_Allergy_and_Anaphylaxis.md` 0.5); consider **IgA deficiency** in a severe reaction.
> - **Bacterial contamination / transfusion-transmitted sepsis** — rigors and rapid deterioration, particularly with platelets (stored at room temperature).
> - **All reactions are reportable to the transfusion service and through the haemovigilance system.**
> See [[10_08_Haemonc_-_Blood_Products_and_Transfusion]].

## 0.2 Drugs for Anaemias

### 0.2.1 Iron Supplements
- **Mechanism:** replaces the substrate for haem synthesis. **Absorption is duodenal, is enhanced by an acidic environment and vitamin C, and is regulated by hepcidin.**
- **Key agents:** **oral** — ferrous sulfate, ferrous fumarate, ferrous gluconate, iron polymaltose (elemental iron content differs between salts, which is what matters); **intravenous** — **ferric carboxymaltose** (the common Australian product, given as a single rapid infusion), iron polymaltose, iron sucrose.
- **Indications:** **iron deficiency, with or without anaemia** — and the deficiency is diagnosed on **ferritin and transferrin saturation**, not haemoglobin (see `NEW_Investigations_Haematology.md`). Also iron deficiency in **heart failure** (where intravenous iron improves symptoms and reduces hospitalisation irrespective of anaemia — see `NEW_Drugs_06_Cardiovascular.md` 0.10.4), chronic kidney disease, pregnancy, and before ESA therapy (0.2.2).

> [!danger] **IRON DEFICIENCY IS A SYMPTOM, NOT A DIAGNOSIS. Find the cause.**
> **In a man of any age, or a postmenopausal woman, iron deficiency anaemia is gastrointestinal blood loss until proven otherwise and requires endoscopic investigation** — upper and lower. In premenopausal women, menorrhagia is the commonest cause but does not excuse missing coeliac disease or a malignancy. **Always check coeliac serology.** Prescribing iron and not investigating is one of the ways bowel cancer is missed.

> [!info] **Oral iron: less is more, and alternate-day dosing is the change worth knowing.**
> Sources show that an oral iron dose **raises hepcidin for many hours, which BLOCKS absorption of the next dose** — so twice-daily and daily regimens are self-defeating. Absorption was **higher with alternate-day dosing (about 21.8%) than consecutive-day dosing (16.3%)**, and sources advise **lower single daily doses and avoiding twice-daily dosing to maximise fractional absorption**. Sources also note that **haemoglobin rose from baseline on both regimens with generally non-significant differences between them**, so this is about tolerability and efficiency rather than a dramatic outcome difference — but **alternate-day, single, lower dosing is better tolerated and absorbs better**, which matters when the commonest reason oral iron fails is that the patient stopped taking it.
- **Oral adverse effects:** **nausea, epigastric pain, constipation (sometimes diarrhoea), and black stools** (expected, and not melaena — but it will obscure a genuine melaena and can cause false-positive occult blood testing on older guaiac tests). **Take with vitamin C or orange juice; avoid taking with tea, coffee, dairy, calcium and antacids.**
- **Oral interactions:** iron **binds** and reduces absorption of **thyroxine, tetracyclines, quinolones, bisphosphonates, levodopa, methyldopa, penicillamine and integrase inhibitors** — **separate the doses by at least 2–4 hours** (see `NEW_Drugs_05_Anti_infectives.md` 0.5.4). Proton pump inhibitors reduce iron absorption.
- **Intravenous iron — indications:** oral intolerance or failure, malabsorption, ongoing losses exceeding oral replacement, chronic kidney disease and dialysis, inflammatory bowel disease, heart failure, late pregnancy, and where rapid repletion is needed.

> [!danger] **Two intravenous iron hazards to know**
> - **HYPOPHOSPHATAEMIA after ferric carboxymaltose — the subject of a TGA safety advisory.** Sources describe it as **most common after ferric carboxymaltose**, usually **asymptomatic**, with **recovery over about 8–10 weeks**, and **more likely with repeated infusions, lower baseline ferritin, gastrointestinal disorders, malnutrition or other causes of phosphate deficiency.** Crucially, sources note the symptoms — **fatigue, weakness, breathlessness, tachycardia, headache** — **can be mistaken for failure to respond to iron treatment**, prompting more iron rather than a phosphate level. **Check phosphate in a patient who feels worse, not better, after an iron infusion**, and especially in anyone having repeated infusions.
> - **Infusion reactions.** Modern preparations are well tolerated (sources report no serious hypersensitivity or anaphylactic reactions in the studies retrieved), but reactions occur: give **where resuscitation facilities are available**, observe during and after, and recognise the self-limiting **Fishbane reaction** (transient flushing, chest or back tightness without hypotension or wheeze) which is **not anaphylaxis** and is managed by pausing rather than stopping permanently. **Extravasation causes permanent brown skin staining** — check the cannula before and during.
> - **Avoid intravenous iron during active infection**, and note iron infusion invalidates iron studies for weeks.

> [!danger] **Iron overdose is a leading cause of paediatric poisoning death, and the danger is an adult quantity in a small child.** Counsel every family prescribed iron about **child-resistant storage**. All paediatric iron dosing is **per kilogram**. See `NEW_Drugs_04_Antidotes_and_Antivenoms.md` 0.3 for the deceptive clinical course and desferrioxamine.

### 0.2.2 Erythropoiesis-Stimulating Agents (Erythropoietin Agonists)
*(covers build-list classes: Erythropoiesis-Stimulating Agents; Erythropoietin agonists)*
- **Mechanism:** recombinant analogues of **erythropoietin**, stimulating erythroid progenitors in the marrow.
- **Key agents:** **epoetin alfa/beta, darbepoetin alfa, methoxy polyethylene glycol-epoetin beta**. **HIF prolyl hydroxylase inhibitors (roxadustat and others)** are an oral class acting upstream, used in some jurisdictions.
- **Indications:** **anaemia of chronic kidney disease** (the main use); chemotherapy-induced anaemia in selected patients; and in some autologous pre-donation and Jehovah's Witness protocols.

> [!danger] **REPLETE IRON FIRST — an ESA without adequate iron does not work.**
> Sources state that **iron repletion should begin before initiating ESA therapy**, that ESA should start once **iron stores are corrected, other reversible causes treated, and haemoglobin is sustained below about 100 g/L**, and that a haemodialysis patient may need an **extra ~1000 mg of supplemental iron in the first 3 months of ESA therapy**. **"ESA resistance" is usually iron deficiency, infection, inflammation, bleeding, or hyperparathyroidism** — look for those before escalating the dose.

> [!danger] **DO NOT AIM FOR A NORMAL HAEMOGLOBIN. Higher targets kill patients.**
> Sources are consistent: randomised trials show **increased cardiovascular events — stroke, thrombosis and death — at near-normal haemoglobin concentrations and higher ESA doses**, with a higher target associated with **increased stroke, hypertension and vascular access thrombosis**, and one analysis reporting **30% greater odds of stroke** with ESA use. Guideline targets are **≤115 g/L, typically 100–115 g/L**, individualised. **The goal is to relieve symptoms and avoid transfusion, not to normalise the number.**

- **Other adverse effects:** **hypertension** (can be severe, and rarely causes encephalopathy and seizures); **thrombosis**, including of vascular access; injection site reactions; and **tumour progression concerns** in some malignancies, which is why oncology use is restricted and specific.

> [!warning] **PURE RED CELL APLASIA is the rare but important idiosyncratic complication.** Sources describe it as antibody-mediated, following **neutralising anti-erythropoietin antibodies**. **If PRCA is diagnosed, the ESA must be stopped immediately, and — critically — the patient must NOT be switched to another ESA**, because **the antibodies cross-react with all of them.** Suspect it when a previously responsive patient develops sudden severe anaemia with a very low reticulocyte count.

- **Monitoring:** haemoglobin (frequently during titration), **iron studies (ferritin and transferrin saturation) regularly**, blood pressure, and potassium in dialysis patients.

### 0.2.3 Colony Stimulating Factors
*(this entry also resolves the `G-CSF` row miscategorised onto the investigations build list)*
- **Mechanism:** recombinant haematopoietic growth factors driving **neutrophil** production and release from the marrow.
- **Key agents:** **filgrastim** and **pegfilgrastim** (**G-CSF**, granulocyte colony-stimulating factor); lenograstim; **sargramostim** (GM-CSF, little used in Australia); **romiplostim and eltrombopag** are thrombopoietin receptor agonists — a different target (platelets), used in **ITP** and aplastic anaemia.
- **Indications:** **primary and secondary prophylaxis of febrile neutropenia** in chemotherapy regimens with a defined risk; **shortening the duration of neutropenia**; **stem cell mobilisation** before apheresis for transplantation; severe chronic and congenital neutropenia.

> [!danger] **G-CSF is NOT a treatment for established febrile neutropenia in most patients, and it is never a substitute for antibiotics.**
> **Febrile neutropenia is a medical emergency: take cultures and give broad-spectrum intravenous antibiotics within an hour** — do not delay for anything, including G-CSF. Its role is **prophylactic**, given after chemotherapy to prevent the neutropenic nadir, and its use as an adjunct in established infection is limited and specialist-directed. See [[10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies]].

- **Adverse effects:** **bone pain** — very common, often in the pelvis, sternum and long bones, and distressing if not warned about (usually manageable with simple analgesia and antihistamines); **splenic enlargement and, rarely, rupture** (investigate left upper quadrant or left shoulder-tip pain); **acute respiratory distress syndrome** and capillary leak; **Sweet syndrome** (acute febrile neutrophilic dermatosis) and cutaneous vasculitis; a leucocytosis that is expected and must not be misread as infection.
- **Practical:** **G-CSF causes uptake on FDG PET** (marrow and spleen), which confounds staging or response scans — timing matters. Filgrastim requires daily injection; **pegfilgrastim is a single dose per cycle**.

### 0.2.4 Other Drugs for Anaemias
- **Vitamin B₁₂ (hydroxocobalamin, cyanocobalamin)** — parenteral for pernicious anaemia and malabsorption; oral high-dose is effective in dietary deficiency and in many malabsorptive states. **Treat B₁₂ before folate** (see the danger below).
- **Folic acid** — deficiency, haemolytic states with high turnover, methotrexate cover, and **preconception and first-trimester supplementation to prevent neural tube defects** — a standing public health recommendation, with a **higher dose in higher-risk pregnancies** (previous affected pregnancy, diabetes, obesity, some antiepileptics).

> [!danger] **NEVER give folate to a B₁₂-deficient patient without replacing B₁₂ first.**
> Folate corrects the **anaemia** while **allowing the neurological disease — subacute combined degeneration of the cord — to progress**, and that damage is **irreversible once established**. **Check B₁₂ before treating a macrocytic anaemia**, and remember that **neurological damage occurs with a normal FBC and no macrocytosis.** See [[10_06a_Haemonc_-_Macrocytic_Anaemia]] and `NEW_Investigations_Haematology_Part2.md` 0.23.

- **Hydroxyurea (hydroxycarbamide)** — raises **fetal haemoglobin** in **sickle cell disease**, reducing crises, acute chest syndrome and transfusion need. Myelosuppressive; teratogenic; requires FBC monitoring.
- **Pyridoxine** — sideroblastic anaemia, including isoniazid-related.
- **Eculizumab and ravulizumab** — complement C5 inhibitors for **paroxysmal nocturnal haemoglobinuria** and atypical HUS. **They cause a profound predisposition to MENINGOCOCCAL infection: meningococcal vaccination is mandatory before starting, often with antibiotic prophylaxis, and any fever must be treated as meningococcal sepsis until excluded.**
- **Immunosuppression (corticosteroids, rituximab, ciclosporin) and splenectomy** — in autoimmune haemolytic anaemia and aplastic anaemia; **splenectomy requires vaccination against encapsulated organisms, antibiotic prophylaxis and lifelong patient education**.
- **Luspatercept** — for anaemia in some MDS and β-thalassaemia.

## 0.3 Drugs for Electrolyte Imbalance

### 0.3.1 Drugs for Potassium Imbalance
- **HYPERKALAEMIA — treat in three stages, and the order matters:**
  1. **STABILISE THE MYOCARDIUM: intravenous CALCIUM (gluconate or chloride).** It does **not** lower the potassium at all — it antagonises the membrane effect and buys time. **Give it first when there are ECG changes**, and repeat as needed. **Get an ECG immediately in any significant hyperkalaemia** — peaked T waves, flattened P waves, PR prolongation, broad QRS, sine wave.
  2. **SHIFT POTASSIUM INTO CELLS: INSULIN with DEXTROSE** (the mainstay), **nebulised salbutamol** (additive, useful while access is obtained), and **sodium bicarbonate** where there is metabolic acidosis. Sources note this effect is **rapid and substantial but lasts only about 4–6 hours**, so **further therapy is always required** — treating and walking away is a recognised error.
  3. **REMOVE POTASSIUM FROM THE BODY: dialysis** (definitive), **loop diuretics** with volume status permitting, and **oral potassium binders**.
- **Potassium binders:**
  - **Sodium polystyrene sulfonate (Resonium)** — an older cation-exchange resin, slow, poorly tolerated, and associated with **colonic necrosis**, particularly with sorbitol and post-operatively.
  - **Patiromer** — exchanges potassium for **calcium**; onset over hours.
  - **Sodium zirconium cyclosilicate (SZC)** — sources describe it as a **non-absorbed inorganic crystalline compound highly selective for potassium**, exchanging it for sodium and hydrogen, and **not associated with clinically significant changes in calcium or magnesium** unlike the resins and patiromer. Trial data cited: mean potassium fell by **1.28 mmol/L at 48 hours**, with **58.6% (5 g) and 77.3% (10 g) normokalaemic versus 24% on placebo**; commonest adverse effects were **mild-to-moderate constipation and oedema** (the sodium load matters in heart failure).
  - **The newer binders' real value is chronic**: they allow **ACE inhibitors, ARBs and mineralocorticoid receptor antagonists to be continued** in heart failure and CKD patients who would otherwise have them stopped for hyperkalaemia — which is a prognostically important gain.

> [!danger] **Always look for the cause and stop the culprit drugs.** Review **ACE inhibitors and ARBs, spironolactone and other MRAs, potassium supplements, trimethoprim, NSAIDs, heparin, digoxin, beta-blockers and tacrolimus**, and consider **acute kidney injury, rhabdomyolysis, tumour lysis, haemolysis, adrenal insufficiency and acidosis**. And **exclude pseudohyperkalaemia** (haemolysed sample, tight tourniquet with fist clenching, delayed processing, marked thrombocytosis or leucocytosis) — **but never delay treating a sick patient while waiting for a repeat.** See [[07_Renal_Medicine_and_Urology]].

- **HYPOKALAEMIA:** oral potassium chloride where mild and the patient can take it; **intravenous potassium for severe or symptomatic hypokalaemia, with a strict maximum concentration and rate, ideally via a central line and with cardiac monitoring at higher rates.**

> [!danger] **NEVER give undiluted potassium, and never as a bolus or "push" — it causes cardiac arrest.** Use pre-mixed bags wherever possible. **And correct MAGNESIUM: hypokalaemia refractory to replacement is hypomagnesaemia until proven otherwise**, because magnesium depletion causes renal potassium wasting.

### 0.3.2 Calcium Salts and Supplements
- **Key agents:** **calcium carbonate** (needs gastric acid — take with food; also a phosphate binder, see 0.3.3) and **calcium citrate** (absorbed independently of acid, so preferred with proton pump inhibitors and after bariatric surgery) orally; **calcium gluconate** and **calcium chloride** intravenously.
- **Indications:** dietary supplementation with vitamin D in **osteoporosis** prevention and treatment; **hypocalcaemia**; **hyperkalaemia** (membrane stabilisation — 0.3.1); calcium channel blocker and magnesium toxicity; hydrofluoric acid burns; as a phosphate binder in renal disease.
- **Adverse effects:** constipation, bloating; **hypercalcaemia and nephrolithiasis** with excess; **milk-alkali syndrome**; interference with the absorption of **thyroxine, bisphosphonates, iron, tetracyclines, quinolones and integrase inhibitors** — separate the doses.
- **Practical points:**
  - **Calcium chloride contains about three times the elemental calcium of the same volume of calcium gluconate**, and is **more irritant and vesicant** — it is generally reserved for central administration and cardiac arrest. **The two are not interchangeable volume-for-volume**, and this is a real prescribing trap.
  - **Correct calcium for albumin, or measure ionised calcium** (see `NEW_Investigations_General_and_Preventive.md` 0.2).
  - **Symptomatic or severe hypocalcaemia is an emergency** — perioral paraesthesia, carpopedal spasm, Chvostek and Trousseau signs, prolonged QT, seizures, laryngospasm. **Post-thyroidectomy and post-parathyroidectomy hypocalcaemia is expected, time-critical and must be actively looked for.**
  - **Check and correct magnesium** — hypomagnesaemia causes hypocalcaemia that will not correct until magnesium is replaced.

### 0.3.3 Phosphate Binders
- **Mechanism:** taken **with food** to bind dietary phosphate in the gut and prevent its absorption. **Timing is the entire therapeutic principle: a binder taken between meals does nothing.** This is the single most useful thing to explain to a patient, and the commonest reason the drug fails.
- **Key agents:**
  - **Calcium-based — calcium carbonate, calcium acetate.** Effective and cheap, but contribute to **calcium load and vascular calcification**, so their use is limited in patients with hypercalcaemia, adynamic bone disease or extensive calcification.
  - **Non-calcium-based — sevelamer, lanthanum carbonate**, and **iron-based binders (sucroferric oxyhydroxide, ferric citrate)** which also provide iron.
  - **Aluminium hydroxide** — very effective but causes **aluminium toxicity (encephalopathy, osteomalacia, anaemia)** with long-term use, so it is now reserved for short-term severe hyperphosphataemia.
- **Indications:** **hyperphosphataemia in chronic kidney disease**, as part of managing **CKD–mineral and bone disorder** alongside dietary phosphate restriction, vitamin D analogues (calcitriol, alfacalcidol), calcimimetics (cinacalcet) and dialysis adequacy.
- **Adverse effects:** gastrointestinal upset and constipation (all); **hypercalcaemia** (calcium-based); sevelamer can cause metabolic acidosis and lowers LDL; lanthanum accumulates in bone with unclear long-term significance.
- **Interactions:** binders **also bind other drugs** — separate **levothyroxine, quinolones, tetracyclines and others** from the binder dose.

### 0.3.4 Essential Minerals
- **Magnesium** — **the mineral most often forgotten, and the one that unlocks the others.**
  - **Indications:** hypomagnesaemia; **eclampsia and severe pre-eclampsia** (the drug of choice for seizure prophylaxis and treatment); **fetal neuroprotection** in anticipated very preterm birth; **torsades de pointes**; severe asthma; refractory hypokalaemia and hypocalcaemia; arrhythmia prophylaxis.
  - **Causes of depletion:** diuretics, proton pump inhibitors (a very common and under-recognised cause), alcohol dependence, diarrhoea, malabsorption, and refeeding.
  - **Toxicity is progressive and monitorable: loss of deep tendon reflexes first, then respiratory depression, then cardiac arrest.** In obstetric use, **reflexes, respiratory rate and urine output are checked regularly**, and **calcium gluconate is the antidote**. **Renal impairment causes accumulation** — dose reduction is required.
- **Zinc** — deficiency causes an **acral and periorificial dermatitis**, poor wound healing, alopecia, taste disturbance and diarrhoea; seen in malabsorption, parenteral nutrition and **acrodermatitis enteropathica**. Also used in **Wilson disease** to block copper absorption. **Excess zinc causes copper deficiency** with anaemia and myeloneuropathy — a described consequence of long-term supplementation and of denture adhesives.
- **Selenium, copper, chromium, manganese, iodine** — trace elements relevant chiefly in **parenteral nutrition and short bowel**, where deficiencies are real and monitored. **Iodine deficiency causes goitre and, in pregnancy, impaired fetal neurodevelopment — iodine supplementation is recommended in pregnancy and breastfeeding in Australia.**
- **Phosphate** — replacement in hypophosphataemia: **refeeding syndrome, diabetic ketoacidosis treatment, alcohol dependence, and after intravenous iron (0.2.1)**. Severe hypophosphataemia causes **respiratory muscle weakness, rhabdomyolysis, haemolysis, cardiac dysfunction and confusion**. Intravenous replacement risks **hypocalcaemia and metastatic calcification** — give slowly with monitoring.

### 0.3.5 Other Drugs for Electrolyte Imbalance
- **Sodium — hyponatraemia:** **fluid restriction** first in SIADH; **hypertonic saline** for severe symptomatic hyponatraemia (seizures, coma) under close supervision; **tolvaptan** (a V2 antagonist, see `NEW_Drugs_06_Cardiovascular.md` 0.11.4); **demeclocycline** (now little used); and **treating the cause** — which is usually a drug (thiazides, SSRIs, carbamazepine, PPIs), hypovolaemia, or an underlying condition.

> [!danger] **Over-rapid correction of chronic hyponatraemia causes OSMOTIC DEMYELINATION SYNDROME, which is devastating and irreversible.** Correction rate limits apply, and they are tighter in high-risk patients (malnutrition, alcohol dependence, liver disease, hypokalaemia, very low starting sodium). **Specific mmol/L/24 h limits are not stated here** — they differ between guidelines; use your hospital's protocol, **measure sodium frequently during correction**, and involve seniors early. **Over-correction can be actively reversed** with desmopressin and free water — so it must be recognised, not just avoided.
- **Hypernatraemia** — almost always a **water deficit**; correct the cause and replace water, again with attention to rate (rapid correction risks cerebral oedema).
- **Sodium bicarbonate** — severe metabolic acidosis, hyperkalaemia, and urinary alkalinisation (salicylate poisoning, rhabdomyolysis). **Not routinely indicated in DKA or lactic acidosis**, where it may worsen intracellular acidosis; causes hypernatraemia, volume overload and hypokalaemia.
- **Oral rehydration solution** — the WHO/reduced-osmolarity formulation. **Vastly under-used** and the correct first-line treatment for most gastroenteritis in children and adults. **Sports drinks, cordial and soft drinks are NOT rehydration solutions** — their sugar content worsens osmotic diarrhoea.
- **Intravenous fluids** — **balanced crystalloids** are generally preferred to 0.9% sodium chloride (hyperchloraemic acidosis with large volumes). **Fluid is a drug: prescribe the type, volume and rate, account for maintenance, deficit and ongoing losses, and reassess daily.**

> [!danger] **Paediatric fluid and electrolyte prescribing is per-kilogram, and hypotonic maintenance fluids have killed children through hyponatraemic encephalopathy.** Use **isotonic** maintenance fluid, calculate by weight, include glucose appropriately, and **measure electrolytes** in any child on intravenous fluids. See [[15_07_Paeds_-_Abdominal_Pain__Neuroblastoma__Coeliac_Disease__Malnutrition__Diarrhoea_and_Vomiting]].

## 0.4 Vitamins and Supplements

### 0.4.1 Fat-Soluble Vitamins (A, D, E, K)
- **The class principle: fat-soluble vitamins are STORED, so they ACCUMULATE and can reach toxicity** — unlike most water-soluble vitamins. Their **absorption requires bile and fat**, so deficiency occurs in **cholestasis, pancreatic insufficiency, cystic fibrosis, coeliac disease, short bowel and after bariatric surgery**, where supplementation is routine.
- **Vitamin A (retinol)**
  - **Deficiency:** night blindness, xerophthalmia and keratomalacia (a leading preventable cause of childhood blindness globally), impaired immunity.
  - **Toxicity:** headache and raised intracranial pressure, dry skin, alopecia, hepatotoxicity, bone pain, and hypercalcaemia.
  - **TERATOGENICITY — the critical point.** Retinoids are potent teratogens. Sources describe **isotretinoin as highly teratogenic at all therapeutic doses, with malformations reported after a single dose in pregnancy**, producing **craniofacial, cardiac, thymic and CNS malformations**. **High-dose vitamin A supplements carry the same concern.** **Pregnancy must be excluded and reliable contraception used before, during and after retinoid therapy**, under a formal pregnancy prevention programme. See [[09_03b_Dermatology_-_Acne_Vulgaris]].
- **Vitamin D (cholecalciferol, ergocalciferol; and the activated forms calcitriol and alfacalcidol)**
  - **Indications:** deficiency, **osteoporosis** (with calcium), rickets and osteomalacia, malabsorption, chronic kidney disease (where **activated forms are needed because the failing kidney cannot 1α-hydroxylate**), hypoparathyroidism.
  - **Deficiency is common in Australia despite the climate** — in those with dark skin, veiling, housebound or institutionalised people, and with strict sun avoidance.
  - **TOXICITY:** sources describe vitamin D toxicity as **rare but capable of severe hypercalcaemia**, with **acute renal failure, nephrocalcinosis, cardiac calcification and myocardial injury**, arising from **increased intestinal calcium absorption and enhanced bone resorption**. **It is a real consequence of high-dose self-supplementation and of prescribing error** — check calcium in anyone on high-dose vitamin D.
  - **The activated forms (calcitriol, alfacalcidol) cause hypercalcaemia far more readily** than cholecalciferol and need closer monitoring.
- **Vitamin E** — deficiency is rare outside severe fat malabsorption and abetalipoproteinaemia, causing **haemolysis, ataxia and peripheral neuropathy**. High-dose supplementation has **no proven benefit and is associated with harm**, including bleeding (it potentiates warfarin).
- **Vitamin K** — see `NEW_Drugs_06_Cardiovascular.md` 0.5. **Newborn vitamin K prophylaxis to prevent haemorrhagic disease of the newborn is standard Australian practice and must be offered and documented.** Deficiency also occurs in cholestasis, malabsorption and prolonged broad-spectrum antibiotic use.

### 0.4.2 Water-Soluble Vitamins (B group and C)
- **The class principle: mostly excreted rather than stored, so toxicity is uncommon — with important exceptions (B₆).** Deficiencies are commonest in **alcohol dependence, malnutrition, malabsorption, hyperemesis, bariatric surgery, dialysis and prolonged parenteral nutrition**, and rarely occur singly.
- **Thiamine (B₁)** — deficiency causes **Wernicke encephalopathy** (confusion, ophthalmoplegia, ataxia — the classic triad is present in a minority, so **treat on suspicion**), **Korsakoff syndrome** (irreversible), and **wet and dry beriberi**.

> [!danger] **GIVE PARENTERAL THIAMINE BEFORE, OR AT LEAST WITH, ANY GLUCOSE LOAD IN AN AT-RISK PATIENT.**
> Sources record the Australian guidance directly: **patients at risk of alcohol-related thiamine deficiency should receive parenteral thiamine before or with glucose, because giving glucose without thiamine may precipitate Wernicke encephalopathy.** Sources also note honestly that the evidence base is **case reports rather than trials**, and that **treating hypoglycaemia must not be delayed** while thiamine is found — the practical rule is **give the glucose the hypoglycaemic patient needs, and give thiamine immediately alongside or straight after.**
> **Oral thiamine is inadequate for treating suspected Wernicke encephalopathy** — it requires **high-dose parenteral** replacement, and treatment is far cheaper and safer than the disability it prevents. **Have a low threshold**: alcohol dependence, hyperemesis gravidarum, bariatric surgery, prolonged vomiting, malnutrition, and refeeding.

- **Vitamin B₆ (pyridoxine)** — used for **isoniazid-related neuropathy prophylaxis and isoniazid overdose seizures**, sideroblastic anaemia, and hyperemesis.

> [!danger] **B₆ is the water-soluble vitamin that IS toxic, and the toxicity is a NEUROPATHY — the same symptom people often take it for.**
> Sources describe a **sensory peripheral neuropathy with paraesthesia, ataxia and imbalance**, usually at **doses above 1000 mg/day**, but **reported below 500 mg/day with supplementation over several months**. It arises from **chronic supratherapeutic supplement use or excessive iatrogenic dosing** — including from **multivitamins and energy drinks that patients do not think of as medicines**. **There is no antidote: treatment is stopping the pyridoxine, and recovery may be incomplete.** **Ask about supplements in any unexplained sensory neuropathy.**

- **Vitamin B₁₂ and folate** — see 0.2.4, including the **B₁₂-before-folate** rule.
- **Niacin (B₃)** — deficiency causes **pellagra** (dermatitis, diarrhoea, dementia); see `NEW_Drugs_06_Cardiovascular.md` 0.9.5 for its abandoned lipid role and the flushing.
- **Riboflavin (B₂)** — deficiency causes angular stomatitis and glossitis; used in migraine prophylaxis.
- **Vitamin C (ascorbic acid)** — deficiency causes **scurvy**: perifollicular haemorrhage, corkscrew hairs, bleeding gums, poor wound healing, and in children bone pain and pseudoparalysis. **It still occurs in Australia** — in isolated older people, those with severe dietary restriction, alcohol dependence, eating disorders and some psychiatric illness — and is easily missed and dramatically reversible. Aids iron absorption. High doses cause **oxalate stones** and interfere with some glucose meters.

### 0.4.3 Essential Fatty Acids
- **Scope:** **omega-3 (EPA and DHA)** from fish and algal oils, **omega-6 (linoleic acid)**, and the parenteral lipid emulsions used in nutrition.
- **Indications with reasonable evidence:** **severe hypertriglyceridaemia** (high-dose omega-3, particularly icosapent ethyl — see `NEW_Drugs_06_Cardiovascular.md` 0.9.6); **prevention of essential fatty acid deficiency in long-term parenteral nutrition** (deficiency causes a scaly dermatitis, alopecia, poor wound healing and, in infants, growth failure); and **DHA in pregnancy and infant nutrition** for fetal neurodevelopment.
- **The honest position on general supplementation:** despite very wide use, **routine omega-3 supplements have not delivered the cardiovascular benefit once expected**, and outcome evidence is agent- and dose-specific. **Advising oily fish in the diet is better supported than advising a capsule.**
- **Adverse effects:** fishy aftertaste and eructation, gastrointestinal upset; **bleeding risk at high doses** (particularly with antiplatelets or anticoagulants); **an increase in atrial fibrillation has been observed with high-dose omega-3** in trials — a genuine and under-appreciated signal; and possible LDL rise with some preparations.
- **Practical:** **supplements are not risk-free and are not regulated as medicines** — ask about them explicitly, because patients frequently do not report them as drugs, and they interact.

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Blood products | SUB | yes | Framed on patient blood management, bedside identification, and acute reactions. |
| 0.2 | Drugs for anaemias | SUB | yes | |
| 0.2.1 | Iron Supplements | CLS | yes | Alternate-day oral dosing and the TGA ferric carboxymaltose hypophosphataemia advisory included. |
| 0.2.2 | Erythropoiesis-Stimulating Agents | CLS | yes | Built jointly with `Erythropoietin agonists` — same class under two names; both rows mapped. |
| 0.2.2 | Erythropoietin agonists | CLS | yes | As above. |
| 0.2.3 | Colony stimulating factors | CLS | yes | **Also resolves the `G-CSF` row** logged `UNRESOLVED — needs review` in Part A, where it appeared on the investigations build list despite being a drug. |
| 0.2.4 | Other drugs for anaemias | CLS | yes | |
| 0.3 | Drugs for electrolyte imbalance | SUB | yes | |
| 0.3.1 | Drugs for potassium imbalance | CLS | yes | |
| 0.3.2 | Calcium Salts / Supplements | CLS | yes | Calcium chloride vs gluconate strength difference flagged as a prescribing trap. |
| 0.3.3 | Phosphate binders | CLS | yes | |
| 0.3.4 | Essential Minerals | CLS | yes | |
| 0.3.5 | Other drugs for electrolyte imbalance | CLS | yes | Sodium correction rate limits omitted — guideline-variable; use local protocol. |
| 0.4 | Vitamins and supplements | SUB | yes | |
| 0.4.1 | Fat-Soluble Vitamins | CLS | yes | |
| 0.4.2 | Water-Soluble Vitamins | CLS | yes | Carries the thiamine-before-glucose rule with its evidence limitation stated honestly, and the B6 neuropathy warning. |
| 0.4.3 | Essential Fatty Acids | CLS | yes | |

**Rows in file: 17 (4 SUB + 13 CLS). AMH section 7 build-list rows: 17. Section complete.**

> [!note] **One pair of build-list rows is a naming duplicate** — `Erythropoiesis-Stimulating Agents` and `Erythropoietin agonists` name the same class; built once at 0.2.2 with both rows mapped.
