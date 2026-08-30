---
block: NEW build — Investigations (Cardiology and Vascular)
source: data/BULK_BUILD_PLAN.md Part A; items from data/no_header_build_queue.md
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Investigations: Cardiology and Vascular

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay-dependent values are **omitted with the omission stated in place**.

> [!note] **The build list carries `Antiphospholipid (APL) Panel` and `Antiphospholipid Panel` as two separate rows.** They are the same test; both are covered by 0.1 and the duplication is recorded in the build status table.

---

## 0.1 Antiphospholipid Panel (Lupus Anticoagulant, Anti-cardiolipin IgG/IgM, Anti-β₂-glycoprotein-I)

**D:** Three assays measured together: **lupus anticoagulant** (a clotting-based functional assay, despite the name **prolonging** phospholipid-dependent clotting times in vitro while causing **thrombosis** in vivo), and two solid-phase antibody assays — **anti-cardiolipin** and **anti-β₂-glycoprotein-I**, each in IgG and IgM.

**Ind:** **Unprovoked or recurrent venous thromboembolism**, especially in a younger patient; arterial thrombosis or stroke in a young patient; **recurrent pregnancy loss, late fetal death, or severe early pre-eclampsia/placental insufficiency**; unexplained prolonged APTT; livedo reticularis or thrombocytopenia with thrombosis; SLE.

**Role:** The laboratory arm of the diagnosis of **antiphospholipid syndrome**, which requires a **clinical event plus persistent laboratory positivity**.

> [!danger] **Persistence is a criterion, not a formality — and this is the single most important point.** Sources agree that antiphospholipid antibodies **must be positive on two or more occasions at least 12 weeks apart** to count. Transient positivity is common and non-pathogenic — it occurs with **infection and with drugs** — so a single positive result does not diagnose APS, and treating on one result commits a patient to lifelong anticoagulation on inadequate evidence.

> [!warning] **Timing and treatment both corrupt the result**
> - **Do not test during an acute thrombotic event** — antibody levels shift acutely and results are unreliable.
> - **Anticoagulants interfere with the lupus anticoagulant assay**, which is clotting-based: **warfarin and DOACs both cause false positives and false negatives.** If the patient is already anticoagulated, discuss timing with the haematology laboratory rather than sending it and interpreting the number.
> - **Triple positivity** (all three assays positive) carries the highest thrombotic risk and is the pattern that most strongly influences management.

> [!danger] **Do not ignore**
> **A prolonged APTT that does not correct on mixing studies, in a patient with thrombosis rather than bleeding** — that combination is lupus anticoagulant until proven otherwise, and it is counter-intuitive enough to be missed. **APS in pregnancy** requires specific obstetric management and is a treatable cause of recurrent loss — see [[10_06b_Haemonc_-_Thrombophilia__APS__Thrombocytosis__Methaemoglobinaemia]].

**Normal/abnormal:** **Titre thresholds are assay-dependent and deliberately not stated** — laboratories report against their own cut-offs, and low-titre IgM positivity in particular is of doubtful significance. Interpret only alongside the clinical criteria.

**Alt:** Full thrombophilia screen (also affected by acute thrombosis and anticoagulation, and generally deferred); FBC and film for thrombocytopenia; ANA and complement where SLE is suspected; imaging of the thrombus.

## 0.2 Heart Failure Markers (BNP, NT-proBNP)

**D:** Natriuretic peptides released by ventricular myocytes in response to **wall stretch** — **BNP** and its inactive cleavage fragment **NT-proBNP**.

**Ind:** **Undifferentiated breathlessness**, to help decide whether heart failure is the cause; suspected new heart failure in primary care, where it determines the urgency of echocardiography; prognostication in established heart failure.

**Role:** **A rule-out test far more than a rule-in test.** A low value in an untreated, breathless patient makes heart failure unlikely and redirects the work-up; a raised value is non-specific and requires **echocardiography**, which remains the diagnostic test.

> [!danger] **The interpretation traps are the entire clinical value of this entry, and they run in both directions**
> **Falsely LOW (heart failure missed):**
> - **Obesity** — sources are consistent that obesity lowers natriuretic peptide levels, attributed to clearance-receptor expression in adipose tissue, and note that a substantial proportion of patients with **HFpEF and obesity** have levels below the usual threshold. **A normal BNP in an obese breathless patient does not exclude heart failure.**
> - Also: flash pulmonary oedema (too rapid for the peptide to rise), and treatment already given (diuretics, sacubitril/valsartan alters BNP specifically).
>
> **Falsely HIGH (heart failure over-diagnosed):**
> - **Atrial fibrillation** — atrial stretch raises levels independent of ventricular function, and this is extremely common in the patients being tested.
> - **Renal impairment** — sources note **NT-proBNP is more affected by renal dysfunction than BNP**, since it is renally cleared.
> - Increasing age, pulmonary hypertension, pulmonary embolism, sepsis, and right heart strain of any cause.
>
> **Numeric cut-offs are deliberately omitted.** The thresholds retrieved were population-specific values from individual studies (differing for obesity, atrial fibrillation and eGFR <30), not a generalisable diagnostic threshold, and no single set met the three-source bar. **Use your laboratory's and local guideline's rule-out threshold, and know which peptide your lab measures — BNP and NT-proBNP values are not interchangeable.**

**Normal/abnormal:** Low value + untreated + not obese → heart failure unlikely. Raised value → echocardiography, and treat the number as a prompt rather than a diagnosis.

**Alt:** **Echocardiography — the diagnostic test**; ECG (a completely normal ECG makes significant systolic heart failure less likely); chest X-ray; troponin; iron studies, TFTs and FBC for precipitants and treatable contributors.

## 0.3 Lipid Profile (Total Cholesterol, LDL-C, HDL-C, Triglycerides, Non-HDL-C, ApoB, Lipoprotein(a))

**D:** Standard lipid panel, with **non-HDL cholesterol** (total minus HDL) calculable from it, and **apolipoprotein B** and **lipoprotein(a)** as additional measures.

**Ind:** **Absolute cardiovascular risk assessment**; established atherosclerotic disease; family history of premature cardiovascular disease or **familial hypercholesterolaemia**; monitoring lipid-lowering therapy; pancreatitis with suspected severe hypertriglyceridaemia; diabetes and chronic kidney disease.

**Role:** One input into **absolute risk**, not a standalone decision-maker — treating an isolated cholesterol number without calculating absolute risk is the classic error.

> [!info] **Australian absolute cardiovascular risk (2023 guideline)** — the lipid profile feeds the **Australian CVD risk calculator**, and sources describe the 2023 guideline as adding **social disadvantage, diabetes-specific markers, atrial fibrillation, and current BP- and lipid-lowering therapy** as variables. Risk categories are **high >15%, moderate 10–15%, low <10%** over **5 years**. See [[19_General_Practice_and_Preventive_Medicine]].

> [!warning] **Fasting is no longer routinely required, and this matters for access.** Sources note that **non-HDL-C and ApoB are more accurate than LDL-C in hypertriglyceridaemia, in non-fasting samples, and at very low LDL-C** — and that **ApoB changes minimally between fasting and non-fasting states**. Calculated LDL-C is the component that becomes unreliable when triglycerides are high, because the calculation assumes a fixed relationship that breaks down. **Where triglycerides are markedly raised, use non-HDL-C or ApoB rather than the calculated LDL-C.**
> **Lipoprotein(a)** is largely **genetically determined and does not respond to lifestyle or statins** — it is measured **once** in a lifetime for risk stratification, not repeated for monitoring.

> [!danger] **Do not ignore**
> **Very high triglycerides** — a cause of **acute pancreatitis**, and a different management problem from cholesterol. **Tendon xanthomata, corneal arcus under 45, or a very high LDL-C with a family history of premature coronary disease** — consider **familial hypercholesterolaemia**, which is under-diagnosed, treatable, and requires **cascade screening of first-degree relatives**; that family screening is the part that gets forgotten.
> **Check a TSH, glucose/HbA1c, LFTs and UEC before attributing dyslipidaemia to primary causes** — hypothyroidism, diabetes, nephrotic syndrome, cholestasis and alcohol are secondary causes that should be treated first.

**Normal/abnormal:** **Target values are deliberately not stated** — they depend on absolute risk category and on whether there is established disease, and Australian targets differ from some international guidance. Use the current Australian guideline and calculator.

**Alt:** Australian CVD risk calculator; coronary artery calcium score in selected intermediate-risk patients; genetic testing for familial hypercholesterolaemia.

## 0.4 Non-Stress Test (NST / Cardiotocography — CTG)

> [!warning] **Mis-filed** — an obstetric investigation listed under Cardiology & Vascular. Built as listed.

**D:** Continuous external recording of **fetal heart rate** and **uterine activity**. Antenatally this is the **non-stress test**; intrapartum it is continuous **CTG** monitoring.

**Ind:** **Antenatal** — reduced fetal movements, suspected fetal growth restriction, hypertensive disease of pregnancy, diabetes, reduced or increased liquor, antepartum haemorrhage, post-dates, maternal illness. **Intrapartum** — any pregnancy with risk factors for fetal compromise, induction or augmentation with oxytocin, meconium, epidural analgesia, and abnormal intermittent auscultation.

**Role:** A test of **current fetal oxygenation**, not of long-term wellbeing. It is a **screening test with high sensitivity and low specificity** — which is why abnormal traces are common and most are not associated with a compromised fetus.

> [!info] **The features read on every trace** — baseline rate, **baseline variability**, **accelerations**, and **decelerations** (with their timing relative to contractions), plus contraction frequency. A **reactive/normal** antenatal trace shows a normal baseline with normal variability and accelerations, and is reassuring.
> **The features that most concern:** **reduced or absent baseline variability** (the single most important abnormality), **late decelerations**, complicated variable decelerations, prolonged decelerations, and a **sinusoidal pattern** — the last suggesting severe fetal anaemia, as in massive fetomaternal haemorrhage or parvovirus.
> **Classification systems and specific numeric criteria are deliberately not stated here** — Australian intrapartum fetal surveillance guidance (RANZCOG) is egress-blocked, classification categories differ between systems, and reproducing criteria for a time-critical obstetric decision from memory is exactly the failure this project guards against. **Use your unit's fetal surveillance guideline and its classification table.**

> [!danger] **Do not ignore**
> **A CTG is interpreted with the clinical picture, never alone.** Fetal tachycardia with maternal fever suggests **chorioamnionitis**; a sudden prolonged deceleration suggests **abruption, cord prolapse or uterine rupture** and is an obstetric emergency requiring immediate senior attendance — **call for help rather than continuing to observe the trace.**
> **A reduced-fetal-movement presentation is not "excluded" by a reactive CTG alone** — it also needs ultrasound assessment of growth and liquor if there are other risk factors. See [[16_10-13_Labour_and_Delivery]] Reduced fetal movements (RFM).
> **Continuous CTG in low-risk labour increases operative delivery without improving neonatal outcome**, which is why intermittent auscultation is the standard in low-risk labour — over-monitoring is itself a harm.

**Normal/abnormal:** Normal/reassuring → continue routine care. Abnormal → escalate, change maternal position, correct hypotension and hypoxia, stop oxytocin, and consider fetal blood sampling or expedited delivery per the unit protocol.

**Alt:** Intermittent auscultation (low-risk labour); **ultrasound with umbilical artery Doppler and biophysical profile** for antenatal surveillance; fetal scalp blood sampling; fetal scalp lactate.

---

## Build status of this file

| Measure | Value |
|---|---|
| Category | Investigations — Cardiology and Vascular |
| No-header items in category | 5 |
| **Built** | **5** (as 4 entries — see duplicate note) |
| Searches used | 2 |

**Duplicate row in the source list:** `Antiphospholipid (APL) Panel` and `Antiphospholipid Panel` are the same test and are covered once, at 0.1.

**Mis-filed item built as listed:** `Non-Stress Test (NST / Cardiotocography)` is an obstetric investigation filed under Cardiology.

**Numerics carried on three-source agreement:** antiphospholipid antibodies must be persistently positive on two occasions **≥12 weeks apart** · Australian absolute CVD risk categories **high >15%, moderate 10–15%, low <10% over 5 years** (2023 Australian guideline / Heart Foundation / MJA).

**Omissions under the sourcing standard, each stated in place:** **all BNP/NT-proBNP numeric cut-offs** (the values retrieved were population-specific single-study thresholds, not a generalisable diagnostic threshold) · antiphospholipid antibody titre cut-offs · lipid target values · **all CTG classification criteria** (RANZCOG guidance egress-blocked, and a time-critical obstetric decision is not a place for reconstructed criteria).
