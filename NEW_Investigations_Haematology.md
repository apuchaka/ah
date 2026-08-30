---
block: NEW build — Investigations & Bedside Tests
source: Build list 2026-08-30 (data/no_header_build_queue.md)
status: standalone — not yet cross-referenced into the corpus; BATCHING TEST BATCH 1
---

# NEW — Investigations: Haematology (anaemia and haemolysis work-up cluster)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **This file is INCOMPLETE — it covers 11 of the 28 Haematology rows on the build list.** It was produced as a batching test (batch 1) and was subsequently recorded as "DONE" in `data/BULK_BUILD_PLAN.md` when it was not. The remaining 17 rows — ADAMTS13 activity, anti-intrinsic factor and anti-parietal cell antibodies, beta-2 microglobulin, biopsy and procedures, erythropoietin, factor VIII assay, flow cytometry, HIT ELISA, homocysteine, lymphoscintigraphy, methylmalonate, ristocetin cofactor activity, serotonin release assay, serum free light chains, VWF antigen, and petechiae — are built in **[[NEW_Investigations_Haematology_Part2]]** as entries **0.11–0.25**, numbered to continue this file. **Read the two files together.** The entries in this file are themselves complete and were not affected; the defect was in scope, not in content.

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked in this environment** (verified 2026-08-30). Entries are **snippet-sourced**. Numerics appear only on three-source agreement; where sources disagreed the figure is omitted and the disagreement stated.

> [!danger] **Reference ranges: read this before using any number below.** Reference intervals are **assay- and laboratory-specific**, and the interval printed on the patient's own report is the one that applies. The ranges given below are typical Australian adult values that recurred across sources; they are for orientation, **not for deciding whether a given patient's result is abnormal**. Where a range could not be sourced to the standard, it is omitted and said so.

## CBC & Peripheral Blood (Complete Blood Count, Reticulocyte count, Peripheral blood film, Morphological variants)

- **Indication:** the single most-ordered test in hospital medicine — screening and monitoring across anaemia, infection, bleeding, malignancy, and as a baseline before most interventions. **The reticulocyte count and the blood film are separate requests in most Australian labs and must be asked for**; an FBC alone does not include them, and this is the most common practical error in the anaemia work-up.
- **Interpretation — the structure that makes it usable:**
  - **Anaemia is classified first by MCV**: microcytic (iron deficiency, thalassaemia, anaemia of chronic disease, sideroblastic), normocytic (acute blood loss, anaemia of chronic disease, renal, haemolysis, marrow failure, mixed deficiency), macrocytic (B12 or folate deficiency, alcohol, liver disease, hypothyroidism, myelodysplasia, drugs — methotrexate, hydroxyurea, azathioprine).
  - **Then by reticulocyte count**, which is the branch point most often skipped: **a raised reticulocyte count means the marrow is responding** — blood loss or haemolysis. **A low or inappropriately normal reticulocyte count in an anaemic patient means the marrow is not responding** — deficiency, marrow disease, renal failure, or anaemia of chronic disease. Ordering the reticulocyte count at the same time as the FBC saves a day.
  - **The blood film is the test that changes the diagnosis** when the indices are ambiguous. Morphological findings worth recognising: **spherocytes** (hereditary spherocytosis or autoimmune haemolysis), **schistocytes/fragments** (microangiopathy — TTP, HUS, DIC, mechanical valve; a finding that demands same-day escalation), **sickle cells**, **target cells** (thalassaemia, liver disease, post-splenectomy), **basophilic stippling** (thalassaemia, lead), **Howell–Jolly bodies** (hyposplenism), **hypersegmented neutrophils** (B12/folate deficiency), **blasts** (acute leukaemia — an immediate call), **rouleaux** (paraproteinaemia), **left shift and toxic granulation** (sepsis), **tear-drop cells** (marrow infiltration or myelofibrosis).
  - **Pancytopenia**, or any unexplained cytopenia with blasts, is a haematology referral, not a repeat-in-a-month result.
- **Typical Australian adult reference ranges** *(orientation only — use the reporting laboratory's own interval)*: **haemoglobin ~130–180 g/L (men), ~115–160 g/L (women); MCV ~80–100 fL; platelets ~150–400 ×10⁹/L; white cells ~4.0–11.0 ×10⁹/L.** **The reticulocyte reference range is deliberately omitted** — it did not reach three agreeing sources, and labs report it variably as a percentage and as an absolute count, which are not interchangeable. **Use the absolute reticulocyte count where available**, since the percentage is falsely reassuring when the red cell count is low.
- **What changes management:** a **raised reticulocyte count** redirects the work-up from deficiency to blood loss or haemolysis. **Schistocytes** trigger an urgent microangiopathy pathway. **Blasts** trigger immediate haematology contact. **Isolated thrombocytopenia with an otherwise normal film** raises ITP and changes whether the patient is transfused or treated immunologically. **Anaemia found before surgery** changes the operative plan and is a recognised, treatable predictor of transfusion.

## Vitamin B12 Level (Serum Cobalamin)

- **Indication:** macrocytic anaemia; unexplained neurological or cognitive symptoms (peripheral neuropathy, subacute combined degeneration, cognitive change) — **which can occur with a normal haemoglobin and a normal MCV, so a normal FBC does not exclude clinically important B12 deficiency**; glossitis; risk groups — vegan or restricted diet, **metformin**, **long-term proton pump inhibitors or H2 antagonists**, bariatric or gastric surgery, ileal disease or resection (Crohn's), alcohol dependence, older age, pernicious anaemia.
- **Interpretation:** the assay measures **total** B12, most of which is bound to haptocorrin and metabolically unavailable, which is why the test performs poorly in the middle of its range.
  - **Clearly low** — deficiency, treat.
  - **Clearly normal with no clinical suspicion** — deficiency unlikely.
  - **Borderline / low-normal — the problem zone, and the reason MMA and homocysteine exist.** Sources agree that when B12 sits in the low-normal band, deficiency should be assessed with **methylmalonic acid and/or homocysteine** rather than by repeating the B12. *(A numeric cut-off for the "grey zone" was found in one source only and is **deliberately not stated** — it did not reach three sources and the boundary is assay-dependent.)*
  - **Falsely low** in pregnancy, oral contraceptive use, folate deficiency, myeloma. **Falsely normal or high** in liver disease, myeloproliferative disease, and — importantly — **recent B12 supplementation, so take the sample before starting treatment.**
- **Normal range:** **omitted** — assay-dependent and reported in ng/L or pmol/L depending on the laboratory. Use the report's interval and units.
- **What changes management:** a low result with neurological features means **treat immediately without waiting for further tests** — neurological damage can become irreversible, and this is the one situation where the borderline discussion is set aside. A confirmed deficiency prompts a search for the **cause** (see the antibody entries below), not just replacement.

## Methylmalonate (Methylmalonic Acid — MMA)

- **Indication:** a **second-line test used to resolve a borderline or low-normal B12**, and to confirm true tissue deficiency where the clinical picture and the B12 level disagree.
- **Interpretation:** MMA accumulates when B12 is functionally deficient, because B12 is a cofactor for the conversion of methylmalonyl-CoA to succinyl-CoA. Sources agree that **MMA is the more sensitive and more specific of the two metabolites** for B12 deficiency, and that the pattern is diagnostic:
  - **MMA raised + homocysteine raised → B12 deficiency.**
  - **MMA normal + homocysteine raised → folate deficiency** (the discriminating pattern, and the single most useful thing in this entry).
- **The major limitation, agreed across sources:** **MMA also rises in renal impairment**, which substantially reduces its specificity in exactly the older population most likely to be tested. Check the eGFR before interpreting it. Volume depletion and small bowel bacterial overgrowth also raise it.
- **Normal range: omitted** — assay-dependent, and no range reached the sourcing standard.
- **What changes management:** a raised MMA converts a "borderline B12" into a treat decision. A normal MMA in a patient with a borderline B12 and no symptoms supports **not** treating and avoids indefinite unnecessary supplementation.

## Homocysteine

- **Indication:** as above, alongside MMA, to clarify a borderline B12 or folate status. Also requested in the work-up of unexplained or premature thrombosis and in suspected inherited homocystinuria — a different and much rarer indication.
- **Interpretation:** homocysteine rises in **both** B12 and folate deficiency, which is precisely why it cannot stand alone — **its value is in combination with MMA**, per the two-pattern rule above. Sources agree it is **less specific than MMA** for B12 deficiency.
- **Non-deficiency causes of a raised level, which matter because they are common:** **renal impairment**, hypothyroidism, smoking, several drugs, and inherited MTHFR variants. Sample handling matters — homocysteine rises in the tube if the sample is not separated promptly, so a spuriously high result should prompt a repeat with attention to collection.
- **Normal range: omitted** — assay- and laboratory-dependent.
- **What changes management:** in the B12 work-up, it refines the deficiency call. **In cardiovascular risk assessment it does not change management** — testing homocysteine as a cardiovascular risk factor, and treating it, has not been shown to improve outcomes, and is a low-value test in that setting.

## Anti-Intrinsic Factor Ab (Anti-Intrinsic Factor Antibodies)

- **Indication:** to establish **pernicious anaemia** as the cause of a confirmed B12 deficiency. It answers "why is this patient B12 deficient?", not "is this patient B12 deficient?" — and that distinction is the whole point of ordering it.
- **Interpretation — the numbers here did reach the standard and are worth carrying:** intrinsic factor antibody is **highly specific (reported around 98–99%) but poorly sensitive (roughly 40–60%)**. The consequences follow directly:
  - **A positive result effectively confirms pernicious anaemia.**
  - **A negative result does not exclude it** — roughly half of patients with pernicious anaemia are antibody-negative, so a negative test in a patient with an otherwise convincing picture should not stop the diagnosis being made clinically.
- **False positives** occur if the sample is taken **within about two weeks of a B12 injection**, so take it before starting replacement or defer it.
- **What changes management:** a positive result establishes a **lifelong** requirement for parenteral (or high-dose oral) B12 replacement, and flags the associated autoimmune conditions — **autoimmune thyroid disease, type 1 diabetes, vitiligo** — plus the **increased risk of gastric carcinoma and gastric carcinoid** that follows atrophic gastritis.

## Anti-Parietal Cell Ab (Anti-Parietal Cell Antibodies — APCA)

- **Indication:** the same question as above — the cause of a confirmed B12 deficiency — with the opposite test characteristics, which is why the two are discussed together and often ordered together.
- **Interpretation:** parietal cell antibody is **more sensitive (reported around 80–90%) but much less specific** than intrinsic factor antibody. **It is present in a meaningful proportion of healthy people (reported up to about 10%) and in other autoimmune diseases**, so a positive result on its own does not establish pernicious anaemia.
  - Sources describe the practical strategy as **parietal cell antibody as the screening test, intrinsic factor antibody as the confirmatory test**, with combined testing giving better overall performance than either alone.
- **What changes management:** a positive APCA with a negative IFAB in a B12-deficient patient still supports autoimmune gastritis and warrants the same replacement and the same awareness of associated autoimmune and gastric malignancy risk — but it is weaker evidence, and the diagnosis rests more on the clinical picture. **A positive APCA in a patient who is not B12 deficient is not a diagnosis** and should not trigger treatment.

## Haptoglobin

- **Indication:** part of the **haemolysis screen**, ordered when anaemia is normocytic with a raised reticulocyte count, or when jaundice, dark urine or a falling haemoglobin suggests red cell destruction. The screen as a whole is **FBC, blood film, reticulocytes, LDH, bilirubin (unconjugated), haptoglobin and a direct antiglobulin test** — ordering haptoglobin alone is not informative.
- **Interpretation:** haptoglobin binds free haemoglobin released from lysed red cells, and the complex is cleared, so **haptoglobin falls in haemolysis** — and falls **most markedly in intravascular haemolysis**, where free haemoglobin enters the circulation directly. In predominantly **extravascular** haemolysis (spleen, liver) haptoglobin may be only mildly reduced or normal.
  - The confirmatory pattern for haemolysis, agreed across sources: **raised reticulocytes + raised LDH + raised unconjugated bilirubin + low haptoglobin.**
- **The traps:** haptoglobin is an **acute-phase reactant, so it rises with inflammation, infection and malignancy** — which can mask haemolysis and produce a falsely normal result in exactly the unwell patient in whom haemolysis is suspected. It is **low in liver disease** without haemolysis, since it is hepatically synthesised, and congenitally absent in a small proportion of people.
- **Normal range: omitted** — assay-dependent, and a specific diagnostic cut-off did not reach three sources.
- **What changes management:** a low haptoglobin with the rest of the screen establishes haemolysis and directs the next step — **DAT** to separate immune from non-immune causes, and **the blood film** to identify microangiopathy, which is the time-critical branch.

## Immunohematology (Blood Group & Rh, Type & Screen, Direct Antiglobulin Test)

- **Indication:** before any possible transfusion; in antenatal care; in suspected haemolytic disease of the newborn; and, for the **DAT**, whenever immune haemolysis is being considered.
- **Interpretation:**
  - **Group and screen ("group and hold")** determines ABO and RhD group and screens the patient's plasma for clinically significant red cell antibodies. **It is not a crossmatch** — it does not reserve compatible units. It is appropriate where transfusion is possible but unlikely.
  - **Crossmatch** establishes compatibility between donor units and the patient and is what makes units available. It may be a **computer (electronic) crossmatch** where the group and antibody screen allow it, which is faster.
  - **Direct antiglobulin test (DAT / direct Coombs)** detects antibody or complement **already bound to the patient's red cells** — a **positive DAT indicates immune-mediated haemolysis** (autoimmune haemolytic anaemia, haemolytic transfusion reaction, haemolytic disease of the newborn, drug-induced). A **negative DAT does not exclude haemolysis** — it points to a non-immune cause (microangiopathy, mechanical, hereditary membrane or enzyme defects, infection).
- **The specimen validity rule, and it is Australian-sourced:** if the patient has been **transfused with red cells, or is or has been pregnant, within the preceding 3 months**, the pretransfusion sample is normally valid for **72 hours** — the "72-hour rule." Longer validity may apply where there is no such history. **Practical consequence: a sample taken on Monday will not cover a Thursday theatre list in a recently transfused or pregnant patient**, and this is a routine cause of avoidable delay.
- **What changes management:** the presence of **red cell antibodies** on the screen can make finding compatible units slow, which changes surgical timing and means the laboratory must be told early. A **positive DAT** changes the anaemia work-up from a search for bleeding to a search for an immune trigger. **Sample labelling errors are the dominant cause of ABO-incompatible transfusion**, so bedside identification and labelling at the bedside are part of the test, not administrative overhead.

## Hb Electrophoresis (Haemoglobin Electrophoresis / HPLC)

- **Indication:** microcytic anaemia **not explained by iron deficiency**, or microcytosis with a normal or high red cell count; family or ethnic background from a region with high haemoglobinopathy prevalence; antenatal and preconception screening; a positive newborn screen; suspected sickle cell disease or trait.
- **Interpretation:** modern laboratories use **HPLC or capillary electrophoresis** rather than classical gel electrophoresis; the quantities that matter are **HbA, HbA₂, HbF** and any variant bands (**HbS, HbC, HbE**).
  - **A raised HbA₂ is the practical marker of β-thalassaemia trait.** Sources give the diagnostic threshold as **HbA₂ above ~3.5%** taken together with a **low MCV and low MCH**, with trait values typically in the **4.0–6.0%** range. *(One source proposed ≥4.0% as a refined cut-off; because sources differ on the exact boundary, treat 3.5% as the threshold that triggers interpretation rather than as a hard line, and read it with the red cell indices.)*
  - **α-thalassaemia trait is not diagnosed by this test** — HbA₂ is normal or low, so a normal electrophoresis in a microcytic patient with normal iron studies does not exclude it, and **DNA studies are required**.
- **The critical confounder, agreed across sources: iron deficiency lowers HbA₂ and can mask β-thalassaemia trait**, producing a falsely normal result. **Correct the iron deficiency and repeat**, or interpret alongside iron studies — this is the single most important practical point in the entry.
- **What changes management:** identifying **trait** changes nothing for the patient's own health but changes **genetic counselling and partner testing**, since two carriers risk a severely affected child — which is why this test belongs in preconception and antenatal care. It also **stops the futile cycle of iron supplementation** given for a microcytosis that is not iron deficiency.

## Erythropoietin Level (Serum EPO)

- **Indication:** the work-up of **polycythaemia (erythrocytosis)** — to help separate a primary marrow disorder from a secondary, hypoxia- or tumour-driven cause. It is **not** a test for anaemia in routine practice, though a low EPO supports renal anaemia in advanced kidney disease.
- **Interpretation:**
  - **Low or suppressed EPO with a raised haemoglobin** points to **polycythaemia vera**, where autonomous marrow production suppresses the normal feedback loop. Sources agree it is a **minor diagnostic criterion** for PV.
  - **Raised or normal EPO with a raised haemoglobin** points to **secondary erythrocytosis** — hypoxia (chronic lung disease, obstructive sleep apnoea, high altitude, right-to-left shunt, smoking), **EPO-secreting tumours** (renal cell carcinoma, hepatocellular carcinoma, cerebellar haemangioblastoma, uterine fibroids), renal artery stenosis, post-renal-transplant, and **exogenous testosterone or EPO use** — which should be asked about directly.
  - **The limitation, and it is important:** a low EPO is **highly specific but very insensitive** for polycythaemia vera — one source reports specificity above 99% but sensitivity around 12% at a low threshold, and **PV can present with a normal or even raised EPO**. So a normal EPO does not exclude PV.
- **What changes management:** EPO does not stand alone — **JAK2 V617F mutation testing is the decisive investigation**, and the combination of a positive JAK2 with a low EPO confirms PV, while wild-type JAK2 with a normal or raised EPO directs the search to a secondary cause. In practice this determines whether the patient goes to haematology for venesection and cytoreduction, or to a search for hypoxia or a tumour.

---

## Batching test — Batch 1 record

| Measure | Value |
|---|---|
| Items built | 10 |
| Searches used | **7** |
| Searches per item | 0.7 |
| Items sharing a search | 8 of 10 |

**Which research genuinely shared, and which did not:**

- **Shared well (one search served several items):** the B12 cluster — a single search on MMA and homocysteine interpretation supplied the substance of **three** entries (B12, MMA, Homocysteine) because their whole clinical meaning is the *pattern between them*. Similarly, one haemolysis-screen search supplied **Haptoglobin** and the DAT half of **Immunohematology**. One antibody search supplied **both** anti-IF and anti-parietal-cell entries, since the sources compare them directly.
- **Did not share:** **Hb electrophoresis** and **Erythropoietin** each needed their own dedicated search and shared nothing with the rest — they sit in the same organ system but answer unrelated questions. **Reference ranges** needed a separate search again, and largely failed (see below).
- **Conclusion for planning:** batching worked because these ten items are **investigated together in one clinical work-up**, not merely because they are filed under "haematology". Grouping by *shared clinical question* gives real savings; grouping by *category label* would not have.

> [!warning] **A standard-related finding from this batch.** Reference ranges are the weak point. Only the FBC ranges reached three agreeing sources, and even those came from **secondary Australian sites citing RCPA rather than RCPA itself** (egress-blocked). **Five of the ten entries have their normal range deliberately omitted.** For an investigations build whose stated product includes "normal ranges", that is a structural limitation, not an occasional gap — under current network conditions this axis cannot be built to the stated product without a reference-range source being supplied.
