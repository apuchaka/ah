---
block: NEW build — Investigations (Orthopaedics, Neurology and Other)
source: data/BULK_BUILD_PLAN.md Part A; items from data/no_header_build_queue.md
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Investigations: Orthopaedics, Neurology and Other

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay- and laboratory-dependent reference intervals are **omitted with the omission stated in place**.

> [!note] **This is the catch-all Part A file.** It carries the remaining investigation categories — Acid-Base, Orthopaedics, Neurology, Oncology, Dermatology, Breast, Paediatrics, Geriatrics, Safeguarding and Sexual Health — plus `C-Spine X-Ray`, deferred here from the O&G file where the build list had miscategorised it. `Femoral Stretch Test` is an exam manoeuvre and is deferred to Part B; see the build status table.

---

## 0.1 Blood Gas and Acid-Base Analysis

**D:** Measurement of **pH, PaCO₂, PaO₂, bicarbonate and base excess**, with most analysers also reporting **lactate, electrolytes, glucose and haemoglobin** on the same sample. **Arterial** for oxygenation; **venous** for pH, CO₂ trend, lactate and electrolytes.

**Ind:** Any acutely unwell patient in whom oxygenation, ventilation or acid–base status is in question: respiratory failure, shock and sepsis, diabetic ketoacidosis, poisoning, severe vomiting or diarrhoea, acute kidney injury, reduced conscious state.

**Role:** **The single most information-dense test available at the bedside**, and the only routine test that measures ventilation.

> [!info] **Work through it in a fixed order, every time — the discipline is the skill**
> 1. **Is the patient hypoxaemic?** PaO₂ against the inspired oxygen.
> 2. **Acidaemia or alkalaemia?** pH.
> 3. **Respiratory or metabolic?** PaCO₂ moving with the pH → metabolic; against it → respiratory.
> 4. **Compensated?** Compensation moves in the same direction as the primary change and **never fully corrects the pH** — a normal pH with grossly abnormal CO₂ and bicarbonate means **two** processes, not perfect compensation.
> 5. **Anion gap** if there is a metabolic acidosis: **Na⁺ − (Cl⁻ + HCO₃⁻)**. A raised gap and a normal gap have entirely different differentials.
> 6. **Delta ratio and the osmolar gap** (0.3) if the picture is mixed or a toxic ingestion is possible.

> [!info] **Raised anion gap acidosis — the classic mnemonic content**
> Ketoacidosis (diabetic, alcoholic, starvation), **lactic acidosis** (types A and B), renal failure (urate, sulfate, phosphate), and toxins — **methanol, ethylene glycol, salicylate, metformin, iron, isoniazid**. **Normal anion gap (hyperchloraemic) acidosis:** diarrhoea, renal tubular acidosis, large-volume saline, ureteric diversion, carbonic anhydrase inhibitors.

> [!danger] **Do not ignore**
> - **A "normal" or rising PaCO₂ in an exhausted asthmatic is peri-arrest.** A tiring patient stops hyperventilating; the number normalises as the patient deteriorates. This is the most dangerous normal result in acute medicine. See [[02_Respiratory]].
> - **A venous gas is adequate for pH, bicarbonate, lactate, potassium and CO₂ trend, but it does NOT assess oxygenation.** Do not use a VBG to decide whether a patient is hypoxaemic.
> - **Record the FiO₂ with every gas.** A PaO₂ that looks acceptable on 15 L/min is severe respiratory failure.
> - **Co-oximetry** is needed for **carboxyhaemoglobin and methaemoglobin**; a routine gas and the pulse oximeter will both miss them. See `NEW_Investigations_Respiratory.md` 0.3.
> - **Delay and air bubbles alter the result**; analyse immediately, and a heparinised syringe that has sat around is not a valid sample.
> - **Lactate is a resuscitation target and a prognostic marker**, but a raised lactate is not always hypoperfusion — think salbutamol, adrenaline, metformin, seizures, liver failure, thiamine deficiency.

**Normal/abnormal:** Analyser reference ranges; **interpret the pattern, not the individual numbers**, and always alongside the patient.

**Alt:** Pulse oximetry (oxygenation only, with the limitations in the Respiratory file); end-tidal CO₂; serum bicarbonate on routine biochemistry (slower, no pH); transcutaneous CO₂; serum lactate; serum osmolality (0.3); specific drug and toxin levels.

## 0.2 Electrolytes and Minerals

**D:** The routine biochemistry panel — **sodium, potassium, chloride, bicarbonate, urea and creatinine** — extended to the divalent minerals **calcium (with albumin), magnesium and phosphate**.

**Ind:** Almost universal in acute illness. Specifically: arrhythmia, weakness, confusion, seizures, vomiting or diarrhoea, diuretic and other drug monitoring, refeeding risk, renal impairment, alcohol dependence, malignancy.

**Role:** The daily working currency of ward medicine, and the panel most likely to be looked at without being read.

> [!danger] **The minerals are the ones that get forgotten, and they are the ones that kill.**
> **Magnesium and phosphate are not on every routine panel** and must be requested. **You cannot correct hypokalaemia or hypocalcaemia without correcting magnesium**, because hypomagnesaemia causes renal potassium wasting and impairs PTH release — persistently refractory potassium or calcium is a magnesium problem until proven otherwise. **Hypophosphataemia** causes respiratory muscle weakness and is central to **refeeding syndrome**.

> [!warning] **Sodium: the number is about water, not salt.** Hyponatraemia is assessed by **volume status first**, then **paired serum and urine osmolality and urine sodium** — that combination separates SIADH from hypovolaemia from a hypervolaemic state, and none of the three is distinguishable on the serum sodium alone.
> **Correct chronic hyponatraemia slowly.** Over-rapid correction causes **osmotic demyelination**, which is irreversible; severe symptoms (seizures, coma) justify urgent hypertonic saline, but the rate limits still apply. **Specific mmol/L/24h correction limits are not stated here** — they differ between guidelines and the safe rate depends on chronicity and risk factors; use your hospital's protocol and involve seniors early. See [[07_Renal_Medicine_and_Urology]].

> [!danger] **Do not ignore**
> - **Pseudohyperkalaemia.** A haemolysed sample, a tight tourniquet with fist clenching, delayed processing, or marked thrombocytosis or leucocytosis all raise the measured potassium. **A high potassium in a well patient with no ECG change should be repeated** — but **never** ignore a high potassium in a sick one while waiting.
> - **A potassium ≥6.5 mmol/L, or any hyperkalaemia with ECG changes, is an emergency.** Get an ECG immediately: peaked T waves, PR prolongation, broad QRS, sine wave. Treat before the repeat comes back.
> - **Correct calcium for albumin** (see `NEW_Investigations_General_and_Preventive.md` 0.2), or measure ionised calcium.
> - **Hypocalcaemia after thyroid or parathyroid surgery** is expected, dangerous and time-critical — look for perioral paraesthesia, Chvostek and Trousseau signs, and a prolonged QT.
> - **Refeeding syndrome:** in a malnourished patient (prolonged poor intake, alcohol dependence, anorexia nervosa, post-bariatric), check **phosphate, magnesium and potassium before and daily after** starting feeding, and give thiamine first.
> - **Urea and creatinine move differently.** A urea rise out of proportion to creatinine suggests **upper gastrointestinal bleeding, dehydration or a catabolic state**; creatinine also depends on muscle mass, so a "normal" creatinine in a frail elderly patient can conceal significant renal impairment — read the **eGFR**, and remember eGFR is unreliable in acute kidney injury and at extremes of body size.

**Normal/abnormal:** Laboratory reference intervals; the **rate of change** is often more clinically important than the absolute value, particularly for sodium and potassium.

**Alt:** Blood gas analyser electrolytes (faster, and includes ionised calcium); paired serum and urine osmolality with urine electrolytes; **ECG** — the functional test for potassium and calcium disturbance; PTH, vitamin D, TFTs and cortisol where the disturbance is unexplained.

## 0.3 Osmolality, Osmolarity and the Osmolar Gap

**D:** **Osmolality** is solute concentration per kilogram of solvent (mOsm/kg) and is what the laboratory **measures**, by freezing-point depression. **Osmolarity** is per litre of solution (mOsm/L) and is what is **calculated**. The two terms are used interchangeably in clinical speech; the distinction matters only in that **the gap between the measured and calculated values is the clinically useful quantity**.

**Ind:** **Hyponatraemia** (with urine osmolality and urine sodium, to classify it); suspected **SIADH** or diabetes insipidus; polyuria and polydipsia; **suspected toxic alcohol ingestion** — methanol, ethylene glycol — and unexplained high anion gap metabolic acidosis; reduced conscious state of unknown cause.

**Role:** Two distinct jobs. **Paired serum and urine osmolality** classifies sodium and water disorders. **The osmolar gap** screens for unmeasured osmotically active substances.

> [!info] **The calculation, in Australian SI units**
> **Calculated osmolarity ≈ 2 × Na⁺ + urea + glucose** (all in **mmol/L**). **Osmolar gap = measured osmolality − calculated osmolarity**, normally **<10 mOsm/kg**.
> **Units trap:** US sources write the same formula as `2(Na) + BUN/2.8 + glucose/18` — the divisors exist only to convert **mg/dL** to mmol/L. Applying them to Australian SI results produces nonsense. Use the SI form above with Australian pathology.

> [!danger] **A normal osmolar gap does NOT exclude toxic alcohol poisoning — and this is stated explicitly in the sources.**
> Two mechanisms defeat it. **Late presentation:** by the time the patient is acidotic, the parent alcohol has been **metabolised** to its toxic acid, so it no longer contributes osmoles — the gap closes as the anion gap opens. **Molecular weight:** ethylene glycol is heavy enough that even toxic concentrations contribute relatively little to osmolality. Conversely, a raised gap is not specific — **ethanol** is the commonest cause by far, and mannitol, glycerol, propylene glycol (a diluent in intravenous lorazepam and other infusions), severe hyperlipidaemia and paraproteinaemia all raise it.
> **Neither the presence nor the absence of an osmolar gap confirms or excludes ingestion.** Treat on clinical suspicion, seek specific levels, and call the **Poisons Information Centre (13 11 26 in Australia)**.

> [!warning] **Do not use the gap to estimate a drug level.** Sources describe multiplying the gap by a factor to estimate methanol or ethylene glycol concentration; this is an arithmetic approximation with wide error and **is not reproduced as a working figure here** — it is not a substitute for a measured level, and treatment decisions (fomepizole or ethanol, dialysis) belong with toxicology.

> [!info] **Urine osmolality is what makes serum osmolality useful in hyponatraemia**
> A **maximally dilute urine** in a hyponatraemic patient points to primary polydipsia or low solute intake; an **inappropriately concentrated urine** with a normal volume state and a urine sodium above the expected threshold points to **SIADH**; a **low urine sodium** with concentrated urine points to hypovolaemia or a hypervolaemic oedematous state. **Take the paired samples before giving fluids** — a litre of saline destroys the diagnostic information permanently.

**Normal/abnormal:** Laboratory reference intervals for measured osmolality; osmolar gap **<10 mOsm/kg** conventionally normal, with sources reporting healthy-population reference intervals that straddle zero and extend to roughly ±8.

**Alt:** Serum and urine electrolytes; **anion gap** on the blood gas; **specific toxic alcohol levels** (send-away in most Australian hospitals, with a real turnaround delay — do not wait for them to treat); ethanol level; ketones; lactate; water deprivation testing for diabetes insipidus.

## 0.4 Bone Densitometry (DEXA)

**D:** **Dual-energy X-ray absorptiometry** — a low-dose scan measuring bone mineral density, conventionally at the **lumbar spine and proximal femur (total hip and femoral neck)**, with the **distal forearm** as the alternative site where those cannot be measured.

**Ind:** Minimal-trauma fracture; assessment before and during long-term **corticosteroids**, androgen deprivation or aromatase inhibitor therapy; premature menopause and hypogonadism; malabsorption, coeliac disease, inflammatory bowel disease; hyperparathyroidism and other secondary causes; monitoring established osteoporosis and response to treatment. **In Australia, Medicare eligibility is defined**: sources describe a rebate for **patients aged 70 and over**, for **monitoring moderate-to-marked osteopenia (T-score −1.5 to −2.5) every two years**, and for **monitoring proven low bone density (T-score ≤ −2.5)**.

**Role:** Quantifies bone density, but **fracture risk is what actually matters** and density is only one input to it.

> [!info] **T-score versus Z-score — and using the wrong one is a real error**
> - **T-score** compares the patient with a **young adult** reference. **Osteoporosis is a T-score of ≤ −2.5** at the lumbar spine, total hip or femoral neck; **osteopenia** is −1.0 to −2.5. Applies to **postmenopausal women and men aged 50 and over**.
> - **Z-score** compares the patient with **age- and sex-matched** peers, and is the score to use in **premenopausal women, men under 50, and children**. The WHO T-score categories were never intended for these groups, and applying them labels healthy young people with "osteoporosis".
> - **A low Z-score in a young person demands a search for a secondary cause** — it is not simply "low for age".

> [!danger] **A minimal-trauma fracture is osteoporosis regardless of the T-score.**
> A fragility fracture (a fall from standing height or less) in an older adult establishes the clinical diagnosis and warrants treatment **even if the DEXA is not in the osteoporotic range**. Waiting for a scan to "confirm" it delays treatment after the event that most strongly predicts the next fracture. **Vertebral fractures are frequently silent** and are found on imaging done for another reason — look for them.

> [!warning] **Artefactually raised readings are common at the spine in exactly the population being scanned** — degenerative change and osteophytes, vertebral fracture, aortic calcification, prior surgery or metalwork. The hip is usually the more reliable site in older patients, and a discordant spine result should be viewed sceptically rather than reassuringly.

> [!danger] **Do not ignore**
> - **Investigate for secondary causes before attributing osteoporosis to age**: calcium, phosphate, ALP, vitamin D, PTH, TFTs, renal and liver function, coeliac serology, testosterone in men, and myeloma screening where indicated (0.8).
> - **Falls assessment is inseparable from fracture prevention.** Density does not break bones; falls do. See [[18_Geriatrics_and_Older_Persons_Health]].
> - **Repeat scanning too soon is uninformative** — change is slow and within measurement error over short intervals; the same machine should be used for serial comparison.
> - Treatment includes calcium and vitamin D adequacy, weight-bearing exercise, smoking and alcohol reduction, and specific antiresorptive or anabolic therapy. See [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]].

**Normal/abnormal:** T-score ≥ −1.0 normal · −1.0 to −2.5 osteopenia · ≤ −2.5 osteoporosis · **established (severe) osteoporosis** = T-score ≤ −2.5 with a fragility fracture. Z-scores are read as "within" or "below" the expected range for age.

**Alt:** **Absolute fracture-risk calculators** (which integrate age, prior fracture, steroids, smoking and other factors with or without a BMD value) — these predict fracture better than density alone; plain radiographs and **vertebral fracture assessment** for silent vertebral fractures; quantitative CT; bone turnover markers (limited role).

## 0.5 Bone Scan (Technetium-99m Skeletal Scintigraphy)

**D:** A nuclear medicine study using **Tc-99m-labelled diphosphonate**, which localises to areas of **increased osteoblastic activity and blood flow**. A **three-phase** study images the **flow (angiographic)**, **blood-pool (soft tissue)** and **delayed (osseous)** phases separately.

**Ind:** Suspected **bone metastases** and staging; **occult fracture** (stress fracture, scaphoid, hip) where radiographs are normal; **osteomyelitis**, especially where MRI is unavailable or contraindicated; suspected **prosthetic loosening versus infection**; **complex regional pain syndrome**; **Paget disease** extent; unexplained bone pain.

**Role:** A **whole-body, highly sensitive but poorly specific** survey. It shows where bone is reacting, not why.

> [!info] **The three phases are what give it specificity, and the classic use is cellulitis versus osteomyelitis**
> Sources describe: **osteomyelitis** shows increased activity in **all three phases**, with uptake localising **to bone** on the delayed images. **Cellulitis** shows increased flow and diffuse **soft-tissue** activity on the early phases **without** focal bony uptake on the delayed images. Sensitivity for osteomyelitis is high — sources quote around **95%** — and it becomes positive **days to weeks before plain radiographs change**, which is the reason to use it in an acute presentation with a normal X-ray.

> [!danger] **The false negatives that matter**
> - **Multiple myeloma is the classic false negative.** Myeloma lesions are **purely lytic with little osteoblastic response**, so a bone scan can be normal in extensive disease. **Never use a bone scan to look for myeloma** — the imaging is **whole-body low-dose CT**, MRI or PET/CT, and sources confirm whole-body CT detects lytic lesions that a conventional skeletal survey misses. See [[10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma]] and 0.8.
> - **Photopenic ("cold") lesions** occur in aggressive disease with no reparative response and in early acute haematogenous osteomyelitis — sources report falsely normal or cold scans in **22–68% of neonates** with osteomyelitis. **A cold spot is an abnormal finding, not a normal one.**
> - **A "superscan"** — diffusely intense skeletal uptake with **absent renal and bladder activity** — indicates widespread metastatic disease, and can be misread as normal because it looks uniform.

> [!warning] **Specificity is the weakness.** Degenerative change, healed and healing fractures, recent surgery, infection and tumour all light up. **A positive bone scan almost always needs correlative imaging** (plain film, CT or MRI) before it means anything. **SPECT/CT** substantially improves localisation and is increasingly standard.

> [!danger] **Do not ignore**
> - **MRI is the better test for most of these questions where it is available** — spinal infection and cord compression, early osteomyelitis, and marrow disease.
> - **Suspected cord compression is an emergency requiring urgent MRI and dexamethasone**, not a bone scan.
> - Involves **ionising radiation** and requires a delay of hours between injection and delayed imaging.

**Normal/abnormal:** Reported qualitatively — focal, multifocal or diffuse increased uptake, or photopenia — against the normal physiological distribution.

**Alt:** **MRI** (best for marrow, soft tissue, spine and early osteomyelitis); **CT**; plain radiographs; **whole-body low-dose CT** for myeloma; **FDG PET/CT** and, in prostate cancer, **PSMA PET/CT**, which outperforms bone scanning for skeletal metastases; labelled white cell scan for prosthetic infection.

## 0.6 Pelvic X-Ray

**D:** An **AP pelvis** radiograph, supplemented where indicated by inlet/outlet views, Judet (oblique) views for the acetabulum, and a **lateral or cross-table lateral hip**.

**Ind:** **Major trauma** — part of the primary survey imaging in a haemodynamically unstable patient; hip pain or inability to weight-bear after a fall; suspected **neck of femur fracture**; suspected pubic rami fracture; hip pathology (osteoarthritis, avascular necrosis, dysplasia); **suspected slipped upper femoral epiphysis or Perthes disease** in a child; suspected sacroiliitis.

**Role:** Fast, available and, in trauma, the study that identifies a pelvic ring injury as a source of catastrophic haemorrhage.

> [!danger] **In the unstable trauma patient, the pelvic X-ray is a resuscitation decision, not a diagnosis.**
> An open-book or vertical shear pattern in a hypotensive patient means **apply a pelvic binder at the level of the greater trochanters** (not the iliac crests) **now**, and activate massive transfusion and interventional radiology or surgery. **Do not "spring" the pelvis** to test stability — it can dislodge clot and worsen bleeding. See [[11_09b_Ortho_-_Trauma]].

> [!warning] **A normal pelvic X-ray does not exclude a hip fracture.**
> Occult **neck of femur** fractures are well described, particularly undisplaced and in osteoporotic bone. **A patient who cannot weight-bear after a fall, with pain, a shortened externally rotated leg or pain on axial loading, needs further imaging — CT or MRI — regardless of the plain films.** MRI is the most sensitive. Missing this leads to displacement, avascular necrosis and a much worse operation.

> [!info] **Reading the pelvis systematically**
> The pelvis is a **ring**: a single displaced fracture is uncommon, so **find the second injury** — including the sacrum and sacroiliac joints, which are easily overlooked. Trace **Shenton's line** (a break indicates a femoral neck fracture or hip displacement), assess symmetry of the obturator foramina and iliac wings, and check the acetabular lines. In children, assess the physes and **Klein's line** for SUFE, which is the classic miss in an adolescent with knee or thigh pain.

> [!danger] **Do not ignore**
> - **Knee pain in a child or adolescent can be hip pathology** — SUFE and Perthes both present this way, and the hip must be examined and imaged. A **frog-leg lateral** is more sensitive than an AP alone for SUFE. See [[11_10_Ortho_-_Paediatric_Orthopaedics]].
> - **Gonadal radiation dose** is not trivial, particularly in children and in women of reproductive age — justify the film, and ask about pregnancy.
> - **Lytic or sclerotic lesions found incidentally** need characterisation, not filing — the pelvis is a common site for metastases and for myeloma.
> - **CT is the definitive study** for pelvic ring and acetabular injuries and for surgical planning; the plain film is the screening step.

**Normal/abnormal:** Reported descriptively; the surgically relevant classifications (Young-Burgess for the ring, Letournel for the acetabulum) are specialist.

**Alt:** **CT pelvis** — definitive for bony injury, and CT angiography for active arterial bleeding; **MRI** for occult hip fracture, marrow and soft tissue; **ultrasound** for paediatric hip and effusion; FAST in trauma for intraperitoneal blood.

## 0.7 C-Spine X-Ray (Cervical Spine Radiographs)

**D:** Plain radiography of the cervical spine — conventionally **AP, lateral (which must show C7/T1) and open-mouth odontoid (peg)** views.

**Ind:** Blunt neck trauma where imaging is indicated by a validated decision rule; suspected atlantoaxial instability (rheumatoid arthritis, Down syndrome, before intubation in those groups); assessment of degenerative change or deformity. **Note: in Australian trauma practice, CT has largely replaced plain films for clearing the cervical spine in adults.**

**Role:** **Decision rules decide whether to image at all** — the **Canadian C-Spine Rule** and **NEXUS** criteria are the standard tools, and knowing that imaging is rule-driven rather than reflexive is the intern-level point.

> [!danger] **Plain films are NOT adequate to clear the cervical spine in a significant blunt trauma, and treating them as if they are is dangerous.**
> Their sensitivity is materially lower than CT; **CT is the imaging of choice** in adults with a significant mechanism, an obtunded patient, or where plain films are inadequate or abnormal. Sources and practice agree that a technically inadequate film — most often **failure to visualise the C7/T1 junction** — is **not a negative study**. If the whole cervical spine down to the top of T1 is not seen, the study has not answered the question.

> [!danger] **Immobilise first, image second.**
> Suspected cervical spine injury means **maintaining spinal precautions until the spine is cleared** clinically or radiologically. The collar comes off when the spine is cleared, not when the film looks normal to the first person who sees it. Prolonged unnecessary collar use also causes harm (pressure injury, raised ICP, aspiration risk) — clearance should be prompt and protocol-driven, not indefinite.

> [!warning] **A normal X-ray does not exclude ligamentous or cord injury.**
> **SCIWORA** (spinal cord injury without radiographic abnormality) is described particularly in **children**, whose more elastic spine allows cord injury without bony disruption. **Neurological signs with normal imaging require MRI and specialist involvement**, not reassurance.

> [!info] **What to look at on the lateral view**
> The **four contour lines** — anterior vertebral, posterior vertebral, spinolaminar and the spinous process tips — should each form a smooth curve; a step is an injury. Check the **prevertebral soft tissue thickness** (widening suggests haematoma from an occult fracture), the **atlanto-dens interval**, and vertebral body height and alignment. **Specific millimetre thresholds are not stated here** — they differ by level, by age (paediatric values differ substantially) and by source, and quoting one figure across all of them would be wrong.

> [!danger] **Do not ignore**
> - **In children**, **pseudosubluxation** of C2 on C3 is a normal variant that is regularly misread as injury, and the paediatric spine has different normal measurements throughout. Paediatric imaging decisions and interpretation should involve someone experienced.
> - **Rheumatoid arthritis and Down syndrome** carry a risk of **atlantoaxial instability**, which is relevant before any airway manipulation or general anaesthetic.
> - **Suspected vascular injury** (vertebral or carotid dissection) with a cervical fracture needs **CT angiography** — a fracture through a transverse foramen is the classic trigger.
> - See [[11_06_Ortho_-_Spinal_Orthopaedics]].

**Normal/abnormal:** Reported descriptively against alignment, bony integrity, cartilage/disc spaces and soft tissues — the "ABCS" approach.

**Alt:** **CT cervical spine** — the study of choice in adult blunt trauma; **MRI** for cord, disc and ligamentous injury and for neurological deficit; CT angiography for suspected vascular injury; flexion-extension views (limited role, and contraindicated acutely in a patient with pain or spasm).

## 0.8 Protein and Immune Profile (Electrophoresis, Immunoglobulins, Free Light Chains)

**D:** A group of tests characterising circulating proteins: **serum protein electrophoresis (SPEP)** with **immunofixation/immunotyping** to identify a **paraprotein (M-band)**; **quantitative immunoglobulins** (IgG, IgA, IgM); **serum free light chains** with the **kappa:lambda ratio**; and **urine electrophoresis** for **Bence-Jones protein**.

**Ind:** **Suspected multiple myeloma** — the reason it appears on an orthopaedic list: **back pain with red flags in a patient over 50**, pathological or vertebral fracture, unexplained bone pain, lytic lesions. Also: unexplained **anaemia, renal impairment, hypercalcaemia** or a very high ESR; suspected amyloidosis; recurrent infection (suspected immunodeficiency); peripheral neuropathy of unknown cause.

**Role:** Detects and quantifies a **monoclonal protein**, and the immunoglobulin panel separately assesses **immune competence** — a low IgG in the presence of a paraproteinaemia (immunoparesis) is itself a significant finding.

> [!danger] **The myeloma screen is a SET of tests, and ordering only part of it misses cases.**
> **SPEP alone misses light-chain-only myeloma** (about a fifth of cases), which produces no serum M-band. **The screen is serum electrophoresis + immunofixation + serum free light chains, plus urine for Bence-Jones protein.** Requesting "protein electrophoresis" alone and reporting it as negative is a recognised way to miss the diagnosis.

> [!info] **The CRAB features are what convert a paraprotein into myeloma**
> **C**alcium raised · **R**enal impairment · **A**naemia · **B**one lesions. A paraprotein **without** end-organ damage is **MGUS** (monoclonal gammopathy of undetermined significance) — common, increasing with age, mostly benign, but requiring lifelong monitoring because a small percentage per year progress.

> [!danger] **Do not ignore**
> - **Back pain with red flags in an older patient is not mechanical until proven otherwise.** Age over 50, night pain, weight loss, no relief with rest, a history of cancer, fever, or any neurological deficit → image and screen. **Cord compression or cauda equina requires urgent MRI, dexamethasone and specialist referral the same day** — not an outpatient work-up.
> - **A normal bone scan does not exclude myeloma** (see 0.5) — the imaging is **whole-body low-dose CT**, MRI or PET/CT.
> - **Hypercalcaemia with renal impairment and anaemia in an older patient is myeloma until excluded**, and hypercalcaemia is itself an emergency requiring rehydration.
> - **A raised total protein with a normal albumin** should prompt electrophoresis — the gap is globulin, and a paraprotein is one explanation.
> - Free light chains are **renally cleared**, so the reference range for the kappa:lambda ratio **differs in renal impairment**; use the renal reference range or the result will mislead.
> - **Do not give nephrotoxic drugs or contrast casually** in suspected myeloma with renal impairment.

**Normal/abnormal:** Electrophoresis reported as the presence, type and **quantity** of any monoclonal band; immunoglobulins against laboratory ranges; free light chains as absolute values **and the kappa:lambda ratio**, which is the more sensitive parameter. **Numeric diagnostic thresholds are not stated here** — the diagnostic criteria are specialist, assay-dependent and revised periodically.

**Alt:** FBC and film (rouleaux), calcium, renal function, albumin, LDH, β₂-microglobulin; **whole-body low-dose CT / MRI / PET-CT**; **bone marrow aspirate and trephine with cytogenetics** — the diagnostic test; tissue biopsy with **Congo red** for amyloidosis (see `NEW_Investigations_General_and_Preventive.md` 0.11).

## 0.9 EMG and Nerve Conduction Studies (NCS)

**D:** Two complementary electrodiagnostic tests, almost always performed together. **NCS** stimulates a nerve and records the response, giving **amplitude, conduction velocity and distal latency**. **EMG** records electrical activity from a needle in muscle, at rest and on voluntary contraction.

**Ind:** Suspected **peripheral neuropathy** (and its classification); **carpal tunnel syndrome** and other focal entrapment; suspected **radiculopathy** where imaging and symptoms disagree; **Guillain-Barré syndrome** and CIDP; motor neurone disease; **myasthenia gravis** (with repetitive stimulation or single-fibre EMG); myopathy; localisation of traumatic nerve injury.

**Role:** Distinguishes **where** the lesion is (nerve root, plexus, nerve, neuromuscular junction, muscle) and **what kind** it is (axonal or demyelinating) — a distinction that plain clinical examination often cannot make and that determines the differential entirely.

> [!info] **Axonal versus demyelinating — the core reading**
> - **Axonal loss:** **reduced amplitudes**, with conduction velocity and distal latency normal or only mildly slowed. **Fibrillation potentials on EMG are the most sensitive sign of axonal loss.**
> - **Demyelinating:** **markedly slowed conduction velocity** (sources give below about 75% of the lower limit of normal) or **prolonged distal latency** (above about 130% of the upper limit), with relatively preserved amplitudes; conduction block and temporal dispersion are the acquired hallmarks.
> - **Why it matters:** most chronic length-dependent neuropathies (diabetes, alcohol, B12 deficiency) are **axonal**; a **demyelinating** pattern narrows the differential sharply to inflammatory, hereditary and paraproteinaemic causes — several of which are **treatable**.

> [!danger] **Timing determines whether the test can answer the question.**
> After an acute nerve injury, **denervation changes take time to appear**: sources describe fibrillation potentials appearing in proximal muscles within about 2 weeks and taking **3–5 weeks to appear in distal muscles**. **A study done too early is falsely reassuring.** Conversely, **NCS in early Guillain-Barré syndrome can be normal** — and **GBS is a clinical diagnosis requiring immediate treatment and respiratory monitoring (FVC), not electrodiagnostic confirmation.** Never let a pending or normal study delay treatment.

> [!warning] **What the test cannot do**
> - It **cannot distinguish axonotmesis from neurotmesis** on an initial study — that is, it cannot tell you whether a severed nerve needs surgical repair, which is a genuine limitation in acute trauma.
> - It **does not assess small fibres**, so painful small-fibre neuropathy can have entirely normal studies.
> - It is **operator-dependent**, uncomfortable, and affected by **limb temperature** — a cold limb slows conduction and mimics demyelination.
> - **EMG needling causes muscle enzyme release**, so a CK taken afterwards is unreliable, and needle EMG is relatively contraindicated in significant coagulopathy or anticoagulation at the sampled site.

> [!danger] **Do not ignore**
> - **Look for the treatable and reversible causes of neuropathy before and alongside the study**: diabetes, **B12 deficiency**, thyroid disease, alcohol, drugs, renal failure, paraprotein (0.8), vasculitis.
> - **Progressive weakness with respiratory involvement is an emergency** — serial FVC, not the electrodiagnostic result, drives escalation. See [[04_Neurology]].

**Normal/abnormal:** Reported by the neurophysiologist as an interpreted **pattern with a localisation and a mechanism**, not as raw numbers. Read the conclusion, not the tables.

**Alt:** Clinical examination with careful dermatomal and myotomal mapping (see [[11_07a_Ortho_-_Dermatomes_and_Myotomes_Reference]]); MRI of spine, plexus or nerve; nerve and muscle **ultrasound**; **nerve or muscle biopsy**; CK and inflammatory markers; autoantibodies (anti-ganglioside, anti-AChR, anti-MuSK); genetic testing for hereditary neuropathies.

## 0.10 Intracranial Pressure (ICP) Monitoring

**D:** Invasive continuous measurement of intracranial pressure, most often via an **external ventricular drain (EVD)** placed into a lateral ventricle, or an **intraparenchymal** microtransducer ("bolt").

**Ind:** Sources agree on the core indication: **severe traumatic brain injury with GCS ≤ 8 and an abnormal CT** (haematoma, contusion, swelling, herniation or compressed basal cisterns); and **GCS 3–8 with a normal CT** in the presence of additional risk features (described as age over 40, motor posturing, or systolic BP <90 mmHg). Also used in selected cases of intracranial haemorrhage, hydrocephalus, fulminant hepatic failure and severe CNS infection.

**Role:** Detects rises in pressure **before** clinical signs appear — by the time pupillary changes and posturing are visible, herniation is under way.

> [!info] **The two numbers, and why CPP is the one being defended**
> **CPP = MAP − ICP.** Sources agree that an **ICP above ~22 mmHg** in acute brain injury should be treated, and that **CPP should be maintained around 60–70 mmHg**. **The brain does not care about ICP directly; it cares about perfusion** — which is why a hypotensive patient with a "modest" ICP can still be ischaemic, and why **hypotension is as dangerous as intracranial hypertension** in head injury.

> [!warning] **EVD versus bolt.** Sources describe the **EVD** as the preferred modality — it is accurate, **can be recalibrated**, and is **therapeutic**, allowing CSF drainage to lower pressure. Its costs are a higher infection risk (ventriculitis) and technical difficulty when the ventricles are compressed or shifted, which is common in exactly the swollen brain that most needs monitoring. An **intraparenchymal** monitor is easier to place and lower-risk but cannot drain CSF and **drifts over time without the ability to be re-zeroed** in situ.

> [!danger] **Do not ignore**
> - **The number is not the treatment.** Raised ICP is managed by the whole bundle: head up ~30°, neck midline with no obstruction to venous drainage (**check the cervical collar and endotracheal tube ties**), adequate sedation and analgesia, normothermia, seizure control, normocapnia (**hyperventilation is a temporising rescue only — sustained hypocapnia causes ischaemia**), osmotherapy, and **surgical decompression or evacuation** where indicated.
> - **Avoid hypotension, hypoxia, hyperthermia, hyponatraemia and hypoglycaemia** — secondary brain injury is what determines outcome and is largely preventable on the ward and in transit.
> - **A drain that stops swinging or draining may be blocked** — a falsely low reading in a deteriorating patient is a monitoring failure, not reassurance.
> - **Never change the height of an EVD or open/close it without the neurosurgical team's instruction** — over-drainage causes collapse and haemorrhage; this is a common and serious ward error.
> - Complications: **infection, haemorrhage along the tract, malposition, drift and blockage**.
> - **Coagulopathy must be corrected before insertion.**

**Normal/abnormal:** Normal adult ICP is low; the intervention threshold in acute brain injury is **>22 mmHg**, with CPP maintained at **60–70 mmHg**. Waveform morphology and the trend carry as much information as the absolute value.

**Alt:** **Serial clinical examination and GCS** — still the foundation, and useless once a patient is sedated and paralysed, which is precisely why invasive monitoring exists; **serial CT**; transcranial Doppler; optic nerve sheath diameter on ultrasound (a non-invasive screen, not a substitute); pupillometry; jugular venous oximetry and brain tissue oxygen monitoring in specialist units.

## 0.11 Tumour Markers

**D:** Substances — usually proteins — measurable in blood, whose concentration correlates with the presence or bulk of a malignancy. Commonly encountered: **CA-125, CEA, CA 19-9, AFP, βhCG, PSA, CA 15-3, calcitonin, thyroglobulin, LDH, β₂-microglobulin**.

**Ind:** **Monitoring response to treatment** and **detecting recurrence** in a patient with a known cancer; assisting characterisation of a known mass (for example **CA-125 in a postmenopausal woman with a pelvic mass**); risk stratification and prognosis; and, in a small number of defined settings, surveillance of a high-risk population (**AFP in cirrhosis**).

**Role:** **Monitoring, not diagnosis, and almost never screening.**

> [!danger] **Tumour markers are not screening tests, and using them as one causes harm.**
> Sources state directly that, with the partial and contested exception of **PSA**, tumour markers **lack the sensitivity and specificity for screening**, and that their proper role is **monitoring response to therapy and detecting early relapse**. Ordering a "cancer panel" in a well person generates false positives, cascades of imaging and procedures, and false reassurance in those with early cancer and a normal marker. **A normal tumour marker never excludes cancer, and a raised one is not a diagnosis.**

> [!warning] **Benign causes are common and are the reason for the false positives**
> - **CA-125** — **endometriosis, fibroids, pelvic inflammatory disease, ovarian cysts, menstruation, early pregnancy**, ascites of any cause, cirrhosis, heart failure, pancreatitis, renal failure and any peritoneal irritation. It is **particularly unreliable in premenopausal women**, which is exactly why its accepted role is in the **postmenopausal** pelvic mass.
> - **CEA** — **smoking**, inflammatory bowel disease, cirrhosis, pancreatitis, peptic ulcer disease.
> - **CA 19-9** — **any biliary obstruction or cholangitis** (it rises with obstructive jaundice regardless of cause), pancreatitis, cirrhosis. Also, around 5–10% of people are **Lewis antigen negative and cannot produce it at all** — in whom it is always normal, cancer or not.
> - **AFP** — pregnancy, hepatitis, cirrhosis, and germ cell tumours as well as hepatocellular carcinoma.
> - **PSA** — benign prostatic hyperplasia, prostatitis, urinary retention, catheterisation, recent ejaculation, cycling, and digital rectal examination.

> [!danger] **Do not ignore**
> - **Trend over serial measurements is the useful signal**, and serial values must come from the **same laboratory and assay** — absolute values are not interchangeable between assays.
> - **A rising marker after treatment can precede radiological or clinical relapse**, which is its main value; but acting on a single rise without confirmation and imaging over-treats.
> - **Germ cell tumours are the important exception** where markers (**AFP, βhCG, LDH**) are integral to **diagnosis, staging and prognosis** — and where a testicular mass warrants markers **before** orchidectomy.
> - **PSA in Australia is not an organised screening program**; it is offered after an informed discussion of the benefits and the substantial harms of overdiagnosis.
> - **Hook effect:** at extremely high concentrations some immunoassays paradoxically report a **falsely low or normal** result. If the marker looks incongruously normal in overwhelming disease, say so to the laboratory.

**Normal/abnormal:** Assay- and laboratory-specific reference intervals. **No numeric thresholds are stated here** — they differ by assay, and the clinically meaningful quantity is nearly always the change over time in a named individual, not the crossing of a cut-off. See [[10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers]].

**Alt:** **Tissue diagnosis — histology remains the standard**; imaging (CT, MRI, PET/CT); endoscopy; the relevant organised **screening programs** (see `NEW_Investigations_General_and_Preventive.md` 0.12), which are validated where markers are not.

## 0.12 FAMCARE-P16

**D:** A **16-item patient-reported questionnaire** measuring **satisfaction with care** in advanced cancer, adapted from the original **FAMCARE** instrument, which measured **family** satisfaction. Validated in outpatients with advanced cancer; single-factor structure with high internal reliability.

**Ind:** **Service evaluation, quality improvement and research** — assessing satisfaction with an outpatient palliative care service or comparing models of care. **It is not a clinical assessment tool for an individual patient's symptoms**, and it will not appear in the management of a patient in front of you.

**Role:** A **patient-reported outcome/experience measure**. Its relevance to an intern is conceptual: knowing that palliative care is evaluated on **patient- and family-reported experience**, not only on survival, and that the family's experience is a legitimate outcome in its own right.

> [!info] **The construct-validity findings are the interesting part.** Sources report satisfaction was **not correlated with performance status** but was **inversely associated with symptom burden, particularly depression and anxiety**. Satisfaction tracks **how the patient feels**, not how sick they look — which is precisely the argument for measuring it separately from clinical parameters.

> [!warning] **Do not confuse this with the clinical instruments used at the bedside in Australian palliative care.** Symptom assessment and phase-of-care tools (symptom assessment scales, functional and phase measures) drive day-to-day management; **FAMCARE-P16 measures satisfaction with the service** and belongs to evaluation, not to the ward round.

> [!danger] **Do not ignore**
> - **Satisfaction instruments have a ceiling effect** — scores cluster at the favourable end, so they are better at detecting poor care than at discriminating between good services.
> - **Grieving and gratitude both distort responses**, in opposite directions, and response rates in this population are inevitably selective — the sickest and the bereaved are the least likely to complete them.
> - What actually changes families' experience is well documented and is not measured by a form: **honest, unhurried communication, symptom control, continuity, and advance care planning done early**. See [[10_11c_Oncology_-_Palliative_Care_Prescribing]].

**Normal/abnormal:** Summed item scores; interpreted comparatively (between services, over time, or between arms of a trial), not against a diagnostic threshold.

**Alt:** The original **FAMCARE** (family satisfaction); validated symptom assessment scales; functional and phase-of-illness measures used in Australian palliative care services; qualitative interview and structured family meetings.

## 0.13 Breast MRI

**D:** **Contrast-enhanced (gadolinium) MRI of the breasts**, performed prone in a dedicated breast coil, with dynamic imaging of enhancement over time. **Non-contrast MRI is not an adequate breast MRI** — the diagnostic information is in the enhancement kinetics.

**Ind:** **Surveillance of women at high genetic or familial risk** — the principal indication; **staging** of newly diagnosed breast cancer in selected cases (lobular carcinoma, dense breasts, discordant conventional imaging, consideration of breast conservation); assessment of **response to neoadjuvant chemotherapy**; suspected **occult primary** presenting with axillary nodal disease; problem-solving where mammography and ultrasound disagree; **implant integrity** assessment (a non-contrast indication).

**Role:** The **most sensitive** breast imaging test — substantially more sensitive than mammography, and the reason it is used in high-risk surveillance, where cancers arise young and in dense tissue that mammography images poorly.

> [!info] **High-risk surveillance in practice**
> Sources describe **annual MRI added to annual mammography** in women with a genetic predisposition, with MRI generally starting **younger than mammography** (from around 25–30 years) and mammography added from about 30, and note that **dual screening detects more cancers than either alone**. **In Australia, a Medicare item exists for breast MRI in asymptomatic high-risk patients**, with defined eligibility (sources describe an MSAC-recommended amendment raising the upper age limit from 50 to 60) — **eligibility criteria change and should be checked at the time of referral rather than assumed.**

> [!danger] **Sensitivity is bought with specificity, and the false positives are the cost.**
> Sources state plainly that MRI is more sensitive than mammography **but more costly and produces more false positives**. In practice that means recalls, **MRI-guided or second-look ultrasound biopsies**, and anxiety in a young woman already living with a high-risk diagnosis. This is a genuine harm and must be part of the consent conversation, not a footnote.

> [!warning] **Timing and preparation matter and are commonly forgotten**
> - **In premenopausal women, schedule MRI in the second week of the cycle (about days 7–14)** — background parenchymal enhancement in the luteal phase obscures lesions and generates false positives.
> - **Gadolinium** requires attention to **renal function**, prior contrast reactions, and pregnancy (avoided in pregnancy).
> - Claustrophobia and the prone position make the study intolerable for some patients.
> - Metallic implants and devices require MRI safety screening.

> [!danger] **Do not ignore**
> - **MRI does not replace mammography** — it is relatively poor at detecting **microcalcification**, which is how DCIS often presents. The tests are complementary, which is why high-risk protocols use both.
> - **A palpable lump is assessed by triple assessment (clinical examination, imaging and tissue biopsy) regardless of the MRI**, and a normal MRI does not remove the need for biopsy of a suspicious lump.
> - **High-risk surveillance belongs with a familial cancer service**, alongside genetic risk assessment and discussion of risk-reducing options — imaging alone is not risk management.
> - See [[10_12_Oncology_-_Breast]].

**Normal/abnormal:** Reported using a structured breast imaging assessment category with a management recommendation; enhancement kinetics and morphology drive the assessment.

**Alt:** **Mammography** (including tomosynthesis) — the population screening test; **ultrasound**, particularly in dense breasts, in younger women and for guided biopsy; **contrast-enhanced mammography** where available; **core biopsy** — the tissue diagnosis; clinical breast examination.

## 0.14 KOH Preparation

**D:** A bedside or laboratory microscopy preparation in which a skin scraping, nail clipping, hair or vaginal sample is treated with **10–20% potassium hydroxide**, which **dissolves keratin and host cells** and leaves fungal elements visible.

**Ind:** Suspected **superficial fungal infection** — tinea corporis/cruris/pedis/capitis, **onychomycosis**, pityriasis versicolor; **vulvovaginal candidiasis** as part of the wet-mount examination (0.15); suspected fungal involvement of an atypical or treatment-resistant rash.

**Role:** A **rapid, cheap confirmation** that a scaly rash is fungal before committing a patient to weeks or months of antifungal therapy.

> [!danger] **Confirm before treating nails, scalp or anything requiring systemic therapy.**
> Oral antifungals for onychomycosis and tinea capitis run for **months**, carry hepatic and drug-interaction risks, and are frequently prescribed for nails that are dystrophic from **psoriasis or trauma** rather than fungus. **Take the sample before starting**, because treatment reduces the yield of both microscopy and culture.

> [!warning] **A negative KOH does not exclude fungal infection.** Sampling error is the main reason — the yield depends entirely on **scraping the active advancing edge** of a lesion (not the centre), taking **adequate material**, and, for nails, sampling **subungual debris from the proximal diseased nail** rather than a distal clipping. **Culture is more sensitive than microscopy** and identifies the organism, but takes weeks.

> [!info] **What you are looking for**
> Branching, **septate hyphae** in dermatophyte infection; **budding yeasts with pseudohyphae** in candida; the **"spaghetti and meatballs"** appearance of short hyphae with spore clusters in **pityriasis versicolor**.

> [!danger] **Do not ignore**
> - **Topical corticosteroid applied to tinea produces "tinea incognito"** — the rash loses its scaly advancing edge, spreads, and looks like eczema. **A rash that worsens or keeps returning on a topical steroid should be scraped.**
> - **Tinea capitis requires ORAL treatment** — topical antifungals do not penetrate the hair shaft — and warrants consideration of household screening. Untreated, it can scar and cause permanent alopecia.
> - **A single "fungal" rash on one foot with a nail change** may be the reservoir for recurrent cellulitis in that leg; treating it prevents recurrences.
> - See [[09_06_Dermatology_-_Fungal_and_Viral_Skin_Infections]].

**Normal/abnormal:** Fungal elements seen or not seen — a positive is confirmatory, a negative is not exclusionary.

**Alt:** **Fungal culture** (more sensitive, speciates, slow); **PCR** for dermatophytes where available (fast and sensitive); **Wood's lamp** (fluorescence in some tinea capitis species and in erythrasma — limited and species-dependent); **skin or nail biopsy with PAS staining** for difficult cases.

## 0.15 Wet Mount (Saline Microscopy)

**D:** A drop of vaginal (or other) discharge mixed with **normal saline** on a slide and examined immediately under light microscopy, typically **paired with a KOH preparation** and a **whiff (amine) test** on the same specimen, plus **vaginal pH**.

**Ind:** **Vaginal discharge, itch, odour or irritation** — the classic three-way differential of **bacterial vaginosis, vulvovaginal candidiasis and trichomoniasis**. Also used for urethral discharge and for other body fluids.

**Role:** Immediate, bedside differentiation of the three commonest causes of vaginitis, allowing treatment at the same visit.

> [!info] **What each finding means**
> - **Clue cells** — vaginal epithelial cells so heavily coated with bacteria that their **borders are obscured** → **bacterial vaginosis**, supported by **pH >4.5** and a **positive whiff test** (fishy amine odour on adding KOH).
> - **Motile trichomonads** — pear-shaped, flagellated, visibly moving → **trichomoniasis**. Motility is the diagnostic feature, and it is **lost as the slide cools and dries**, which is why the slide must be read immediately.
> - **Budding yeasts and pseudohyphae** — best seen on the **KOH** side of the preparation, which dissolves the epithelial cells and bacteria → **candidiasis**, usually with a **normal pH**.

> [!danger] **Wet mount microscopy is INSENSITIVE for trichomoniasis** — a substantial proportion of infections are missed, and sensitivity falls further with any delay before reading the slide. **NAAT is the sensitive test** and should be sent where trichomoniasis is suspected, whatever the microscopy shows. Sources also note that **asymptomatic screening for *Trichomonas* is recommended only in particular population groups**, not universally.

> [!danger] **Do not ignore**
> - **Trichomoniasis is a sexually transmitted infection** — it requires **partner treatment**, a full STI screen (0.18), and contact tracing. Bacterial vaginosis and candidiasis are not STIs, and conflating them causes real harm in both directions.
> - **Recurrent candidiasis** should prompt a check for **undiagnosed diabetes**, immunosuppression and HIV.
> - **Discharge with pelvic pain, fever, deep dyspareunia or cervical motion tenderness is pelvic inflammatory disease** — treat empirically now; do not manage it as vaginitis. See [[17_05_PID__Endometriosis__Fibroids]].
> - **Postmenopausal discharge, blood-stained discharge, or discharge with a suspicious cervix** requires examination and specialist referral, not microscopy and a prescription.
> - **Bacterial vaginosis in pregnancy** is associated with preterm birth and is managed differently.

**Normal/abnormal:** Descriptive — presence of clue cells, trichomonads, yeast, lactobacilli and leucocytes, read with pH and the whiff test.

**Alt:** **NAAT** for *Trichomonas*, chlamydia and gonorrhoea — the sensitive tests; **high vaginal swab** for culture; vaginal pH; the composite clinical criteria for bacterial vaginosis; full STI screen (0.18). See `NEW_Investigations_Obstetrics_and_Gynaecology.md` 0.3.

## 0.16 Slit Skin Smear

**D:** A technique for diagnosing **leprosy (Hansen disease)**: the skin is pinched to exclude blood, a small **slit incision** is made, the sides and base are **scraped** for tissue fluid and dermal material, smeared, and stained by a **modified Ziehl-Neelsen (Fite)** method. Samples are taken from **multiple standard sites** and from active lesions.

**Ind:** Suspected **leprosy** — hypopigmented or erythematous **anaesthetic** skin patches, thickened peripheral nerves, painless burns or ulcers of the hands and feet; classification of disease; monitoring treatment response; investigation of a **lepra reaction**.

**Role:** Quantifies the bacillary load, which **classifies the disease** (paucibacillary versus multibacillary) and therefore determines the **duration and composition of multidrug therapy**.

> [!info] **The two indices**
> - **Bacterial index (BI)** — the density of **all** acid-fast bacilli, viable or not, on a **0 to 6+** logarithmic scale. Falls slowly over years of successful treatment.
> - **Morphological index (MI)** — the proportion of bacilli that appear **solid-staining and therefore viable**. Falls **rapidly** with effective treatment and is the more responsive measure of treatment effect and of infectivity.

> [!danger] **A negative slit skin smear does NOT exclude leprosy.**
> Smears are **negative in paucibacillary disease**, which is the commoner presentation — the diagnosis is then made on the **cardinal clinical features**: a skin lesion with **definite sensory loss**, a **thickened or enlarged peripheral nerve**, or demonstrated acid-fast bacilli. A single positive cardinal sign is sufficient; the smear supports classification rather than making the diagnosis.

> [!danger] **Do not ignore**
> - **Leprosy is rare in Australia but is not absent** — it occurs in people who have lived in endemic regions and in some Aboriginal and Torres Strait Islander communities. Delayed diagnosis is the norm, and every month of delay is more irreversible nerve damage.
> - **The disability comes from nerve damage, not the infection**, and it is largely preventable. **Assess nerve function (sensation and motor power) at diagnosis and at every review** — that assessment, not the smear, protects the patient's hands and feet.
> - **Lepra reactions (type 1 reversal and type 2 erythema nodosum leprosum) are acute immunological emergencies** that can destroy nerve function within days, and they occur **during and after** treatment. New nerve pain, weakness, or a sudden change in lesions needs urgent specialist assessment and corticosteroids.
> - **Notifiable and specialist-managed**, with contact examination and multidrug therapy supplied through public health programs.
> - Anaesthetic feet require **foot care and protective footwear education** at every visit.

**Normal/abnormal:** Reported as **BI and MI**; a positive smear defines multibacillary disease for treatment purposes.

**Alt:** **Skin biopsy with Fite stain and histopathology** (which also demonstrates the granulomatous pattern and nerve involvement); **PCR** for *M. leprae* (more sensitive than smear, and sources describe using it on already-stained smear slides to reclassify smear-negative cases); nerve conduction studies and clinical nerve function assessment; specialist referral. See [[09_05_Dermatology_-_Bacterial_Infections_and_Infestations]].

## 0.17 Newborn Bloodspot Screening

**D:** A **heel-prick** blood sample collected onto a filter-paper card ("Guthrie card") and analysed by tandem mass spectrometry, enzyme assay and **targeted genetic testing** on the same spots.

**Ind:** **Offered to every baby born in Australia.** Sources agree the sample is best taken at **48–72 hours of age**, within the first 72 hours. A repeat is needed in some circumstances — prematurity, transfusion, an early sample, or an inadequate one.

**Role:** Detects a defined set of rare but **treatable** conditions **before symptoms develop**, at the point where treatment prevents death or permanent disability. This is the clearest example in medicine of a screening program changing outcomes.

> [!info] **What is screened, and the honest caveat about consistency**
> Sources describe Australian programs covering **at least 25 conditions**, including **phenylketonuria, congenital hypothyroidism and cystic fibrosis**, with **some conditions screened only in certain states and territories** (galactosaemia and **spinal muscular atrophy** are named examples), and national work under way to harmonise the panels. The panel is **biochemical with targeted single-gene testing** for **CFTR** and **SMN** on the same specimen.
> **The specific condition list is deliberately not enumerated here**: it differs by jurisdiction and is being actively expanded, and a list that is wrong for the reader's state is worse than none. Check your state program's current panel.

> [!danger] **Do not ignore**
> - **A positive screen is a SCREEN, not a diagnosis.** It triggers urgent confirmatory testing and specialist referral. Parents must be told this clearly, because the anxiety generated by a positive result is substantial and most are false positives.
> - **Timing errors are the commonest operational failure**: samples taken **too early** (before 48 hours) can miss conditions that depend on postnatal metabolite accumulation; samples taken late delay treatment. **Early discharge is the usual reason a sample is missed** — check it has been done.
> - **An inadequate card must be repeated** — insufficient blood, layered spots or contaminated cards cannot be analysed.
> - **Screening does not test for everything.** A normal result **does not exclude** a metabolic or genetic condition, and **an unwell neonate must be investigated on clinical grounds** regardless — sepsis, hypoglycaemia, and inborn errors of metabolism all present before or independently of the screen. See [[15_17a_Paeds_-_Hyperthyroidism_and_Approach_to_Inherited_Metabolic_Disease]].
> - **Consent and storage.** Screening is offered, not mandatory, and parents can decline. Card retention, secondary use and access are governed by state policy and are a legitimate parental question.
> - Newborn screening is broader than the bloodspot: **universal newborn hearing screening**, examination of the newborn, and pulse oximetry screening for critical congenital heart disease where in place. See [[15_24b_Paeds_-_Screening__SIDS__Vaccination_Schedule]].

**Normal/abnormal:** Reported as screen negative, or as a positive requiring **urgent** confirmatory testing — with the state screening service usually contacting the family and clinician directly for a positive result.

**Alt:** Confirmatory diagnostic testing specific to the condition (plasma amino acids, urine organic acids, acylcarnitine profile, sweat chloride, thyroid function, genetic testing); antenatal and preconception **carrier screening**; clinical assessment of the unwell newborn, which always takes precedence.

## 0.18 STI Screening (Asymptomatic Sexual Health Check)

**D:** A defined set of tests offered to an **asymptomatic** person based on sexual history: **NAAT** for **chlamydia and gonorrhoea** from the relevant sites — **first-void urine** or **self-collected vaginal swab**, plus **pharyngeal and rectal** swabs where indicated by sexual practices — together with **serology for HIV, syphilis and hepatitis B** (and **hepatitis C** where risk factors exist).

**Ind:** Sexually active people at risk; a new or multiple partners; a partner with a diagnosed STI; men who have sex with men (more frequent, multi-site screening); people who inject drugs; sex workers; before and during **PrEP**; antenatal screening; and opportunistically at any consultation where it is acceptable to raise it.

**Role:** Finds **asymptomatic** infection — which is the majority of chlamydia and a large share of gonorrhoea — and so prevents pelvic inflammatory disease, infertility, ectopic pregnancy, congenital and neonatal infection, and onward transmission.

> [!danger] **Genital sampling alone misses extragenital infection.**
> Pharyngeal and rectal chlamydia and gonorrhoea are **usually asymptomatic** and are only found if those sites are swabbed. **Take a sexual history that establishes which sites are exposed**, and swab them. A urine NAAT alone in a man who has receptive anal or oral sex is an inadequate screen — and is a very common omission.

> [!info] **How to make the screen actually happen**
> - **Self-collected swabs are non-inferior for NAAT** and markedly improve uptake and acceptability; offer them.
> - Australian laboratories generally test chlamydia and gonorrhoea on the **same duplex NAAT**, so a chlamydia request returns both.
> - ***Mycoplasma genitalium*: asymptomatic screening is NOT recommended** — macrolide resistance is high and treating asymptomatic detections does more harm than good. **Asymptomatic *Trichomonas* screening is recommended only in specific population groups.** Doing more tests is not doing a better screen.

> [!danger] **Do not ignore**
> - **The window period.** A negative HIV or syphilis test taken too soon after exposure does not exclude infection; the screen must be **repeated after the window**. Telling someone they are clear when they are in the window period is a serious error.
> - **Chlamydia, gonorrhoea, syphilis and HIV are notifiable**, and **contact tracing is part of treatment**, not optional. Support the patient to do it, or use partner notification services.
> - **Offer HIV testing to everyone being screened, not selectively** — risk-based selection misses infections, and normalising the offer reduces stigma.
> - **Check hepatitis B immunity and vaccinate the non-immune**; offer **HPV vaccination** where eligible.
> - **Discuss PrEP** with those at substantial HIV risk — a sexual health screen is the natural point to raise it.
> - **A screen is for the asymptomatic.** Symptoms — discharge, ulceration, pelvic or testicular pain, dysuria — mean **assessment and empirical treatment now**, not a screening pathway.
> - **Consider sexual coercion, assault and child protection** where the history raises them; forensic requirements displace ordinary screening. See [[NEW_Safeguarding_and_Forensic]].
> - See [[08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs]].

**Normal/abnormal:** Organism detected/not detected on NAAT; serology reported as reactive/non-reactive with confirmatory testing, and **syphilis serology interpreted as a pattern** (treponemal and non-treponemal tests together) that distinguishes active from treated past infection — a specialist interpretation, not a single positive.

**Alt:** Site-specific culture with susceptibilities (essential for **gonococcal** resistance surveillance and after treatment failure); microscopy and wet mount in the symptomatic patient (0.15); point-of-care HIV and syphilis testing; postal and online self-collection programs.

## 0.19 Elder Abuse Suspicion Index (EASI)

**D:** A brief screening instrument for elder mistreatment: **six questions**, the **first five asked directly of the patient** and the **sixth answered by the clinician** from observation. Questions refer to the **past 12 months**. A **"yes" to any of questions 2–6** establishes concern warranting further exploration.

**Ind:** Older adults with **intact cognition** seen in primary care or ambulatory settings — opportunistically, and specifically where there are concerns: unexplained injuries, repeated presentations, unexplained financial change, poor hygiene or nutrition, medication non-adherence, missed appointments, depression or social withdrawal, or a carer who answers for the patient or will not leave the room.

**Role:** **Raises suspicion to the level at which the clinician explores further or refers** — the tool's own stated purpose. It does not diagnose abuse and does not quantify it.

> [!danger] **A positive screen is the beginning of a process, not a conclusion — and acting badly on it can make the patient less safe.**
> Confronting a suspected perpetrator, or documenting carelessly in a record the carer can see, can escalate risk or cut the patient off from help. The correct response is a careful, **private** assessment (see the pointer below), a risk and capacity assessment, and referral to the appropriate service.

> [!danger] **Interview the older person ALONE.**
> This is the single most important practical step, and the one most often skipped because it is socially awkward. A person will not disclose abuse in front of the person doing it. Create a routine reason to separate them ("I always examine patients on their own") rather than making it look like suspicion.

> [!warning] **Know the tool's limits**
> - **The EASI was designed for cognitively intact patients.** The people at highest risk — those with **dementia** and those most dependent — are precisely those it is least able to assess. Their assessment relies on collateral, observation, examination and a capacity assessment.
> - It screens for the **suspicion of** abuse, and it is a prompt for conversation, not evidence.
> - **Financial abuse is the commonest form in Australian data and leaves no physical sign** — ask about money, powers of attorney, and who controls the pension.

> [!danger] **Do not ignore**
> - **Elder abuse includes financial, psychological, physical, sexual and neglect**, and multiple types commonly coexist. Most is perpetrated by **family members**.
> - **Assess decision-making capacity**, which determines what can be done without the person's consent. **A person with capacity may decline intervention**, and that decision must be respected while keeping the door open and documenting the offer.
> - **Where there is immediate danger, or the person lacks capacity, escalate** — the pathways differ by state and include the **1800 ELDERHelp national line**, state elder abuse helplines, adult safeguarding and public advocate/guardian services, aged care complaints bodies, and police for criminal conduct.
> - **Document objectively**: what was said in quotation marks, what was observed, photographs of injuries with consent — records may later be evidence.
> - **Consider the carer.** Carer stress and unmet need contribute to some neglect, and support and respite can be part of the response — this is an explanation, never an excuse.
> - See [[18_Geriatrics_and_Older_Persons_Health]] and [[NEW_Safeguarding_and_Forensic]].

**Normal/abnormal:** A "yes" on **any** of questions 2–6 raises concern and prompts further assessment or referral. There is no score to interpret.

**Alt:** Structured clinical assessment and collateral history; **capacity assessment**; cognitive assessment; comprehensive geriatric assessment; social work referral; other elder-abuse screening instruments; direct observation of the carer–patient interaction, which is often more informative than any questionnaire.

## 0.20 Short Physical Performance Battery (SPPB)

**D:** A three-part objective measure of **lower limb function**: **hierarchical standing balance** (side-by-side, semi-tandem, tandem), **4-metre usual-pace gait speed**, and **five-times sit-to-stand** from a standard chair. Each component is scored **0–4** on timed criteria, summed to a **total of 0–12**, with higher scores indicating better performance.

**Ind:** Assessment of **frailty, sarcopenia and falls risk** in older adults; baseline and outcome measure in rehabilitation and hospital-associated deconditioning; pre-operative risk assessment; research and trials in ageing.

**Role:** Converts a subjective impression ("looks frail") into a **reproducible number** that predicts outcomes and can be tracked over time — and, importantly, that can be handed over between clinicians without loss of meaning.

> [!info] **It predicts more than falls.** SPPB performance is associated with disability, hospitalisation, institutionalisation, mortality and — as one source specifically reports — **incident cardiovascular events**. It is a general marker of physiological reserve, not merely a leg-strength test.

> [!warning] **Gait speed alone carries much of the signal.** The **4-metre walk** is the single most useful component and is quick enough to be done in any clinic. If the full battery cannot be done, **do the walk** — a slow usual gait speed is one of the most robust predictors of adverse outcome in older adults, and it takes under a minute.

> [!danger] **Do not ignore**
> - **The score is only useful if it changes something.** A low score should trigger a **multifactorial falls and frailty assessment** — medication review (especially psychotropics, antihypertensives and anticholinergics), postural blood pressure, vision, footwear, continence, cognition, vitamin D and nutrition, home hazards — and referral for **progressive resistance and balance training**, which is the intervention with the best evidence.
> - **Look for the reversible contributors**: pain, deconditioning after admission, anaemia, hypothyroidism, depression, Parkinsonism, cervical myelopathy, and undertreated osteoarthritis.
> - **Do not test unsafely.** Assess whether the patient can attempt each component; supervise closely and stop the test rather than risk a fall to complete a score.
> - **A ceiling effect** limits its usefulness in fitter older adults, in whom more demanding measures discriminate better.
> - **Hospital-associated deconditioning is iatrogenic and preventable** — bed rest, unnecessary catheters and lines, and not mobilising older inpatients cause measurable functional loss within days. Mobilise early. See [[18_Geriatrics_and_Older_Persons_Health]].

**Normal/abnormal:** Total 0–12; each component 0–4. Lower scores indicate worse lower-limb function and higher risk. **Specific cut-points defining "frailty" are not stated here** — the thresholds used vary between the sarcopenia and frailty definitions in circulation, and no single set met the three-source bar; use the threshold specified by the definition your service applies, and use the score primarily to **track change within an individual**.

**Alt:** **Gait speed alone**; **Timed Up and Go**; grip strength (dynamometry); chair-stand test alone; frailty indices and scales; comprehensive geriatric assessment; falls risk screening tools; functional assessment by physiotherapy and occupational therapy.

---

## Build status

| # | Item | Built | Notes |
|---|---|---|---|
| 0.1 | Blood Gas & Acid-Base | yes | |
| 0.2 | Electrolytes & Minerals | yes | Sodium correction rate limits omitted — guideline-variable; use local protocol. |
| 0.3 | Osmolarity | yes | Built jointly with `Electrolyte & Osmolality Panel` as one entry — measured osmolality, calculated osmolarity and the gap are one investigation. SI formula stated; the US mg/dL divisor form flagged as a units trap. Gap-to-level estimation refused. |
| 0.3 | Electrolyte & Osmolality Panel | yes | As above. |
| 0.4 | Bone Densitometry / DEXA | yes | |
| 0.5 | Bone Scan | yes | |
| 0.6 | Pelvic X-Ray | yes | |
| 0.7 | C-Spine X-Ray | yes | **Deferred here** from `NEW_Investigations_Obstetrics_and_Gynaecology.md`, where the build list had miscategorised it under Gynaecology. Millimetre thresholds omitted — level- and age-dependent. |
| 0.8 | Protein & Immune Profile | yes | |
| 0.9 | EMG / NCS | yes | |
| 0.10 | ICP Monitoring | yes | |
| 0.11 | Tumor Markers | yes | No numeric thresholds — assay-specific, and the trend is the clinical quantity. |
| 0.12 | FAMCARE-P16 | yes | A research/service-evaluation instrument, not a clinical assessment tool; built with that framing stated. |
| 0.13 | Breast MRI | yes | Medicare eligibility described but flagged as changing; check at referral. |
| 0.14 | KOH Prep | yes | |
| 0.15 | Wet Mount | yes | |
| 0.16 | Slit Skin Smear | yes | |
| 0.17 | Newborn Screening | yes | Condition list **not enumerated** — differs by state and territory and is being expanded; a list wrong for the reader's jurisdiction would be worse than none. |
| 0.18 | STI Screening | yes | |
| 0.19 | Elder Abuse Suspicion Index | yes | |
| 0.20 | Short Physical Performance Battery | yes | Frailty cut-points omitted — definition-dependent, did not meet the three-source bar. |
| — | Femoral Stretch Test | **deferred** | An **exam manoeuvre**, not an investigation, despite its build-list row. Deferred to `NEW_Exam_Manoeuvres_and_Procedures.md` (Part B file 12) with the other Orthopaedics manoeuvres. |

**Items in file: 20 entries covering 21 build-list rows (including `C-Spine X-Ray` deferred in from the O&G file). One row deferred to Part B.**

> [!danger] **CORRECTION (2026-08-30) — the claim originally made here was wrong, and is left visible rather than rewritten.**
> This file originally ended: *"Part A is now complete. All eleven investigation files exist, and every investigation row has been built, collapsed into another entry as a duplicate, or explicitly deferred."* **All eleven files did exist, but two of them did not cover their rows:**
> - `NEW_Investigations_Haematology.md` covered **11 of 28** Haematology rows (it was a batching-test output listed as "DONE" in the plan). **Fixed by `NEW_Investigations_Haematology_Part2.md`.**
> - `NEW_Investigations_Infectious_Diseases.md` had missed **Campylobacter** and **Clostridium perfringens**. **Fixed in place as 0.22 and 0.23 of that file.**
>
> **The error was in the evidence, not the arithmetic: "the file exists and the plan says DONE" was treated as "the file covers its rows."** With both gaps closed, **Part A is now complete against `data/build_list_investigations.md`, checked row by row** — but that statement should be re-verified by anyone relying on it, not taken from this note.
