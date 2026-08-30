# Build queue — items with no corpus header, plus ambiguous items

Generated 2026-08-30 from the header-only existence check (1,976 `##`/`###` headers, 170 files, `NEW_*.md` excluded).

**Two kinds of entry, marked inline:**

- Unmarked — **no header found**. Nothing in the corpus matched the literal name or an obvious direct variant.
- `[?]` — **ambiguous**. The name appears inside a longer header. The matched header is shown. These were added at your request; each carries a **non-binding read**:
  - `dup?` — the matched header looks like the same topic under a different form (e.g. `Hearing loss — differential diagnosis`). **Check before building; you will probably be duplicating.**
  - `fp?` — the matched header looks like a narrower named entity that merely contains the word (e.g. `Coma` → `Glasgow Coma Scale`). **Probably a real gap; build it.**

The read is my judgement from the header text alone, not from reading the entries. Twelve were reclassified by hand after the automated pass got them wrong, so treat the rest as reviewable too.

> **Drug-class caveat:** 120 of 122 subsections and 317 of 459 class rows were transcribed; `[CUT]` classes and fine-grained duplicate variants were collapsed. Drug counts are a floor.

> Presentations are included in their own section at the end — they were outside the previous queue's scope, kept separate so you can ignore them if that still holds.

---

## Conditions & Diagnoses — 358 (322 no header + 36 ambiguous)

Build product: pathophysiology, features, investigations, management (Australian guidelines).

### comparison frameworks — 7

**Acid-Base** (2)

- `[T1]` Acid-Base Disorders — HAGMA vs NAGMA vs Alkalosis vs Mixed
- `[T1]` Electrolyte Imbalance & Dehydration

**Emergency & Critical Care** (3)

- `[T1]` Emergency Medicine Core Algorithms & Procedures
- `[T1]` Sepsis Phenotypes
- `[T1]` Shock Phenotypes

**Respiratory** (1)

- `[T1]` Respiratory Failure — Type 1 (Hypoxic) vs Type 2 (Hypercapnic)

**Toxicology** (1)

- `[T1]` Toxidromes & Allergic Emergencies

### conditions — 295

**Acid-Base, Fluids & Electrolytes** (5)

- `[T2]` Alcoholic Ketoacidosis
- `[T2]` Hypermagnesaemia
- `[T2]` Hyperphosphataemia
- `[T2]` Hypophosphataemia
- `[T2]` Symptomatic Hypercalcaemia

**Cardiology & Vascular** (10)

- `[T2]` Cardiac Device Event
- `[T2]` Cardiac Glycosides
- `[T2]` Changing Heart Murmur
- `[T2]` Coronary Vasospasm
- `[T2]` Hypertensive Emergency
- `[T2]` New Heart Murmur
- `[T2]` Peripartum Cardiomyopathy
- `[T2]` Pseudoaneurysm (post-catheterisation femoral)
- `[T2]` Tachyarrhythmia
- `[T2]` Troponins / Biomarkers

**Dermatology** (19)

- `[T3]` Acne `[? fp?]` *matched:* `Acne vulgaris`
- `[T3]` Acute Erythema
- `[T3]` Alopecia `[? dup?]` *matched:* `Alopecia (Hair Loss) — Approach and Differential`
- `[T3]` Chronic Inflammatory Dermatosis
- `[T3]` Erythema `[? fp?]` *matched:* `Erythema toxicum neonatorum`
- `[T3]` Generalised Erythema
- `[T3]` Hirsutism
- `[T3]` Hypopigmentation
- `[T3]` Localised Blisters
- `[T3]` Localised Erythema
- `[T3]` Nail Disorder
- `[T3]` Pigmentary Disorder
- `[T3]` Skin Breakdown
- `[T3]` Skin Discolouration
- `[T3]` Skin Failure
- `[T3]` Skin Protectants / Astringents
- `[T3]` Vesiculobullous Eruption
- `[T3]` Widespread Maculopapular Exanthem
- `[T3]` Workplace Bullying

**ENT & Oral** (7)

- `[T3]` Chronic Rhinosinusitis
- `[T3]` Dry Mouth `[? dup?]` *matched:* `Xerostomia (dry mouth)`
- `[T3]` Incidental Calcium Disorder
- `[T3]` Nasal Congestion
- `[T3]` Nasal Obstruction
- `[T3]` Toothache
- `[T3]` Vocal Cord Paralysis

**Emergency & Critical Care** (13)

- `[T1]` Acute Deterioration
- `[T2]` Acute Airway Obstruction
- `[T2]` Apparent Life-Threatening Event
- `[T2]` Bisbiguanide Antiseptics
- `[T2]` Brief Resolved Unexplained Event
- `[T2]` Cardiac Arrest
- `[T2]` Failure to Wake Post-Sedation
- `[T2]` Lower Airway Obstruction
- `[T2]` Post-Procedural Deterioration
- `[T2]` Systemic Inflammatory Response Syndrome
- `[T2]` Tracheostomy Emergency
- `[T2]` Upper Airway Compromise
- `[T2]` Upper Airway Obstruction

**Endocrine & Metabolic** (13)

- `[T2]` Androgen / Sex Hormone
- `[T2]` Cushingoid Appearance
- `[T2]` Hyperglycaemia
- `[T2]` Hyperglycaemic Emergency
- `[T2]` Hyperlipidaemia
- `[T2]` Hypoglycaemia with Neuroglycopenia
- `[T2]` IGF-1
- `[T2]` Metabolic Bone Disease
- `[T2]` Parathyroid Hormone
- `[T2]` Suspected Diabetes
- `[T2]` Suspected Hypothyroidism
- `[T2]` Thyroid Dysfunction
- `[T2]` Thyroid Enlargement

**Environmental & Physical Injury** (4)

- `[T3]` Heat Exhaustion
- `[T3]` Heat Illness
- `[T3]` Hyperthermia
- `[T3]` Severe Hyperthermia

**Ethics, Law & Professional Practice** (2)

- `[T2]` Chronic Disease Surveillance
- `[T2]` Fitness Certification

**Gastroenterology & Hepatology** (12)

- `[T3]` Acute Liver Failure
- `[T3]` Bowel Obstruction `[? fp?]` *matched:* `Small Bowel Obstruction (SBO)`
- `[T3]` Chronic Liver Disease
- `[T3]` Chronic Liver Failure
- `[T3]` Esophagoscopy
- `[T3]` Gastrografin
- `[T3]` Gastroscopy
- `[T3]` Hepatomegaly
- `[T3]` Intra-abdominal abscess
- `[T3]` Opioid Analgesics (Weak / Atypical)
- `[T3]` Pancreatic pseudocyst
- `[T3]` Percutaneous Transhepatic Cholangiography

**General & Cross-cutting** (1)

- `[T3]` Refusal to Bear Weight

**General Practice & Preventive** (6)

- `[T3]` Lifestyle Risk Factor Management
- `[T3]` Occupational Airway Disease
- `[T3]` Occupational Exposure
- `[T3]` Preventive Health
- `[T3]` Smoking Cessation `[? dup?]` *matched:* `Lifestyle Risk Factors (SNAP) and Smoking Cessation`
- `[T3]` VTE Risk Assessment

**Geriatrics** (3)

- `[T1]` Comprehensive Geriatric Assessment
- `[T3]` Dalhousie University Clinical Frailty Scale
- `[T3]` Polypharmacy `[? dup?]` *matched:* `Polypharmacy and Deprescribing`

**Gynaecology & Reproductive** (4)

- `[T3]` Cervical Radiculopathy
- `[T3]` Contraception Request
- `[T3]` Dysmenorrhoea
- `[T3]` Family Planning

**Haematology** (21)

- `[T1]` Anticoagulant-Associated Bleeding
- `[T3]` Acute Anaemia
- `[T3]` Acute Transfusion Reaction
- `[T3]` Antepartum Haemorrhage `[? fp?]` *matched:* `Other causes of antepartum haemorrhage (APH)`
- `[T3]` Bone Marrow Failure
- `[T3]` Chemical Coagulants / Protein Precipitants
- `[T3]` Coagulopathy
- `[T3]` Febrile Neutropenia
- `[T3]` Haematoma `[? fp?]` *matched:* `Subdural Haematoma`
- `[T3]` Leucocytosis
- `[T3]` Leucopenia
- `[T3]` Leukocoria
- `[T3]` Lupus Investigation
- `[T3]` Lymphopenia
- `[T3]` Neutropenia
- `[T3]` RBC Folate
- `[T3]` Recurrent Thrombosis
- `[T3]` Sickle Cell Crisis
- `[T3]` Thrombocytopenia `[? fp?]` *matched:* `Immune thrombocytopenia (ITP)`
- `[T3]` Vaso-Occlusive Crisis
- `[T3]` White Blood Cell Abnormality

**Infectious Diseases** (12)

- `[T3]` Bloodborne Pathogen Exposure
- `[T3]` C. difficile
- `[T3]` Cutaneous Infestation
- `[T3]` Drugs against mycobacteria
- `[T3]` Herpetic Whitlow
- `[T3]` Infection in Immunocompromised Patient
- `[T3]` Lower Genital Tract Infection
- `[T3]` Lymphangitis
- `[T3]` Necrotising Soft Tissue Infection
- `[T3]` Opportunistic Infection
- `[T3]` Retropharyngeal abscess
- `[T3]` Vector-Borne Infection

**Neurology** (19)

- `[T3]` Acute Amnesia
- `[T3]` Acute Facial Palsy
- `[T3]` Acute Neuro-Ophthalmic Dysfunction
- `[T3]` Acute Rigidity
- `[T3]` Ataxia `[? fp?]` *matched:* `Friedreich's Ataxia`
- `[T3]` Cerebellar infarction
- `[T3]` Dysarthria `[? fp?]` *matched:* `Speech Disorder (Dysphasia/Aphasia vs Dysarthria)`
- `[T3]` Dysphasia `[? fp?]` *matched:* `Speech Disorder (Dysphasia/Aphasia vs Dysarthria)`
- `[T3]` Heat Stroke
- `[T3]` Hemiparesis
- `[T3]` Lumbar Radiculopathy
- `[T3]` Meningism
- `[T3]` Monoparesis
- `[T3]` Muscle Relaxants (Neurotoxins)
- `[T3]` Nystagmus
- `[T3]` Paraparesis
- `[T3]` Peripheral Neuropathy
- `[T3]` Post-concussive syndrome `[? dup?]` *matched:* `Concussion and Post-Concussive Syndrome`
- `[T3]` Quadriparesis

**Obstetrics** (7)

- `[T2]` Fetal Scalp Blood Sampling
- `[T2]` Intrauterine Fetal Demise
- `[T2]` Labour `[? fp?]` *matched:* `Normal labour`
- `[T2]` Maternal Infection in Pregnancy
- `[T2]` Postpartum Care
- `[T2]` Preterm Labour
- `[T2]` Unintended Pregnancy

**Oncology & Palliative Care** (6)

- `[T3]` Cachexia
- `[T3]` End-of-Life Care
- `[T3]` Oncologic Emergency
- `[T3]` Palliative Care `[? fp?]` *matched:* `Symptom management in palliative care`
- `[T3]` Quality of Life at the End of Life
- `[T3]` Vesicants

**Ophthalmology** (16)

- `[T1]` Acute Painful Red Eye
- `[T3]` Acute Painful Eye
- `[T3]` Acute Red Eye
- `[T3]` Blurred Vision `[? dup?]` *matched:* `Colour Vision and Blurred Vision — DDx`
- `[T3]` Chronic Eye Disease
- `[T3]` Dry Eye
- `[T3]` Exophthalmos
- `[T3]` Gritty Eye
- `[T3]` Keratoconus
- `[T3]` Painful Eye `[? dup?]` *matched:* `Red Eye / Painful Eye`
- `[T3]` Painless Acute Red Eye
- `[T3]` Proptosis
- `[T3]` Ptosis
- `[T3]` Pupillary Asymmetry
- `[T3]` Red Eye `[? dup?]` *matched:* `Red Eye / Painful Eye`
- `[T3]` Watery Eye

**Orthopaedics & Trauma** (18)

- `[CUT]` Bennett's fracture
- `[CUT]` Bunions
- `[CUT]` Hallux valgus
- `[T3]` Dislocation `[? fp?]` *matched:* `Shoulder dislocation`
- `[T3]` Facial Fractures
- `[T3]` Fracture `[? fp?]` *matched:* `Supracondylar fracture of the humerus`
- `[T3]` Gamekeeper's thumb
- `[T3]` Hangman fracture
- `[T3]` Jefferson fracture
- `[T3]` Lisfranc fracture
- `[T3]` Mallet Finger
- `[T3]` Minor Traumatic Wound
- `[T3]` Orbital Floor Fracture
- `[T3]` Rolando fracture
- `[T3]` Sprain
- `[T3]` Strain
- `[T3]` Stress Fracture
- `[T3]` Wound Management `[? dup?]` *matched:* `Wound Management — Basic Principles`

**Paediatrics & Neonatology** (26)

- `[T2]` Adolescent Eating Disorder
- `[T2]` Adolescent Substance Use
- `[T2]` Apnoea in Infant
- `[T2]` Atopic Child `[? fp?]` *matched:* `The Atopic Child (Atopic March / Atopic Multimorbidity)`
- `[T2]` Developmental Delay `[? fp?]` *matched:* `Global developmental delay`
- `[T2]` Developmental Regression
- `[T2]` Febrile Child Without Source
- `[T2]` Floppy Infant
- `[T2]` Fussing Child
- `[T2]` Hepatomegaly in Child
- `[T2]` Hyperactive Child
- `[T2]` Hypotonic Infant
- `[T2]` Inconsolable Infant
- `[T2]` Irritable Child
- `[T2]` Irritable Infant
- `[T2]` Lethargic Child
- `[T2]` Lymphadenopathy in Child
- `[T2]` Neonatal Apnoea
- `[T2]` Neonatal Distress
- `[T2]` Pale Child
- `[T2]` Refusal to Bear Weight in Child
- `[T2]` Respiratory Distress in Child
- `[T2]` Seriously Unwell Child
- `[T2]` Splenomegaly in Child
- `[T2]` Unwell Child
- `[T2]` Well Child Surveillance

**Psychiatry** (19)

- `[T1]` Suicide Risk
- `[T3]` Acute Psychosis
- `[T3]` Acute Stress Reaction
- `[T3]` Acute Suicidal Ideation
- `[T3]` Adjustment Disorder
- `[T3]` Catatonia
- `[T3]` Delusional Disorder
- `[T3]` Eating Disorder `[? fp?]` *matched:* `Binge-eating disorder`
- `[T3]` Excessive Daytime Sleepiness
- `[T3]` Mood Swing
- `[T3]` Mutism
- `[T3]` NaSSAs
- `[T3]` Parasomnias
- `[T3]` Psychosocial Stress
- `[T3]` Sleep Paralysis
- `[T3]` Sleepwalking
- `[T3]` Suicidal Behaviour
- `[T3]` Suicidal Ideation
- `[T3]` Suicide Attempt

**Renal & Urology** (8)

- `[T3]` Calcineurin inhibitor nephropathy
- `[T3]` Contrast-Induced Nephropathy
- `[T3]` Epispadias
- `[T3]` Neurologically Determined Death
- `[T3]` Posterior Urethral Valves
- `[T3]` Proteinuria
- `[T3]` Renal Colic
- `[T3]` Subacute Focal Neurological Dysfunction

**Respiratory** (11)

- `[T2]` Acute Bronchospasm
- `[T2]` Acute Respiratory Distress `[? fp?]` *matched:* `Acute Respiratory Distress Syndrome (ARDS)`
- `[T2]` Acute Respiratory Failure
- `[T2]` Apnoea `[? fp?]` *matched:* `Obstructive sleep apnoea (OSA)`
- `[T2]` Chronic Respiratory Failure
- `[T2]` Occupational Lung Disease `[? dup?]` *matched:* `Pneumoconioses (Occupational Lung Disease — brief overview)`
- `[T2]` Pleuromutilin antibiotics
- `[T2]` Recurrent Respiratory Infection
- `[T2]` Respiratory Arrest
- `[T2]` Respiratory Distress `[? fp?]` *matched:* `Acute Respiratory Distress Syndrome (ARDS)`
- `[T2]` Tuberculosis Contact

**Rheumatology & Immunology** (17)

- `[T1]` Hot Joint
- `[T3]` Acute Urticaria `[? dup?]` *matched:* `Acute urticaria and angioedema`
- `[T3]` Angioedema `[? fp?]` *matched:* `Hereditary angioedema`
- `[T3]` Arthrocentesis
- `[T3]` Arthroplasty `[? dup?]` *matched:* `Joint replacements (arthroplasty)`
- `[T3]` Arthroscopy
- `[T3]` Enthesitis
- `[T3]` Haemarthrosis
- `[T3]` Mast Cell Stabilizers
- `[T3]` Muscle Cramp
- `[T3]` Muscle Spasm
- `[T3]` Muscle Wasting
- `[T3]` Myalgia
- `[T3]` Rheumatoid Factor
- `[T3]` Swollen Joint
- `[T3]` Tendinopathy
- `[T3]` Urticaria `[? fp?]` *matched:* `Acute urticaria and angioedema`

**Safeguarding & Forensic** (3)

- `[T2]` Domestic Violence
- `[T2]` Sexual Assault
- `[T2]` Workplace Sexual Harassment

**Sexual & Gender Health** (4)

- `[T3]` Gender Dysphoria
- `[T3]` Premature Ejaculation
- `[T3]` Psychosexual Disorder
- `[T3]` Sexually Transmitted Infection

**Toxicology & Envenomation** (9)

- `[T1]` Adverse Drug Reaction
- `[T2]` Benzodiazepine overdose
- `[T2]` Envenomation `[? fp?]` *matched:* `The finding that matters: Australian envenomation is absent in a stronger sense than previously recorded`
- `[T2]` Immunotherapy Toxicity
- `[T2]` Suspected Carbon Monoxide Exposure
- `[T2]` TCA Overdose
- `[T2]` Tobacco Withdrawal
- `[T2]` Toxic Exposure
- `[T2]` Toxicological Emergency

### framework child items — 56

**(framework child)** (56)

- ABCDEFG algorithm
- ACLS
- ALS
- Acute Cardiogenic Pulmonary Oedema
- Acute Exacerbation of COPD
- Acute asthma
- Acute pulmonary oedema
- Acute renal colic
- Acute severe headache
- Adult Sepsis
- Adult analgesia
- Adult diabetic ketoacidosis
- Adult resuscitation
- Allergic reaction / anaphylaxis
- Angioedema (Non-IgE Mediated) `[? fp?]` *matched:* `Hereditary angioedema`
- Anticholinergic Toxidrome
- Australian Elapid Snakebite
- BLS
- Beta-Blocker / Calcium Channel Blocker Overdose
- Biliary Sepsis (Ascending Cholangitis)
- Burns `[? dup?]` *matched:* `Burns and Scalds`
- Cardiogenic: Acute Left Ventricular Failure
- Cholinergic Toxidrome (Organophosphates)
- Distributive: Adrenal (Addisonian) Crisis
- Fascia iliaca block
- HAGMA — Diabetic Ketoacidosis
- HAGMA — Lactic Acidosis
- Hypovolaemic: Non-Haemorrhagic
- ILS
- Intubation
- Isotonic Dehydration
- Major head injury
- Mechanical ventilation
- Meningococcal Sepsis
- Metabolic Alkalosis — Profuse Vomiting / Diuretic Use
- Minor head injury
- Mixed Acid-Base Disorder — Salicylate (Aspirin) Toxicity
- NAGMA — Severe Diarrhoea
- Neonatal resuscitation
- Neuromuscular Respiratory Failure
- Obstructive: Cardiac Tamponade
- Obstructive: Massive Pulmonary Embolism
- Opioid-Induced Respiratory Depression
- Paediatric Sepsis
- Paediatric analgesia
- Paediatric diabetic ketoacidosis
- Paediatric resuscitation
- Paracetamol (Acetaminophen) Overdose
- Procedural sedation
- Serotonin Toxicity vs Sympathomimetic Toxidrome
- Severe Community-Acquired Pneumonia / ARDS
- Spider Bites (Redback vs Funnel-web)
- Third-Spacing
- Tonsillitis / quinsy
- Toxic Alcohols (Methanol / Ethylene Glycol)
- Urosepsis / Gram-Negative Septic Shock


## Investigations & Bedside Tests — 208 (206 no header + 2 ambiguous)

Build product: indication, interpretation, normal ranges, what changes management.

### investigations — 192

**Acid-Base** (4)

- `[T1]` Blood Gas & Acid-Base
- `[T1]` Electrolytes & Minerals
- `[T2]` Electrolyte & Osmolality Panel
- `[T2]` Osmolarity

**Breast** (1)

- `[T3]` Breast MRI

**Cardiology** (5)

- `[T2]` Antiphospholipid (APL) Panel
- `[T2]` Antiphospholipid Panel
- `[T2]` Heart Failure Markers
- `[T2]` Lipid Profile
- `[T2]` Non-Stress Test

**Dermatology** (3)

- `[T3]` KOH Prep
- `[T3]` Slit Skin Smear
- `[T3]` Wet Mount

**Endocrine** (9)

- `[T3]` Carnitine Levels
- `[T3]` G6PD Assay
- `[T3]` Glucose / Diabetes
- `[T3]` Plasma Amino Acid Screen
- `[T3]` Prolactin
- `[T3]` Radioactive Iodine Uptake
- `[T3]` Renin-Aldosterone
- `[T3]` Thyroid Panel
- `[T3]` Thyroid Ultrasound

**GP & Preventive** (6)

- `[T3]` Genetic Risk Assessment
- `[T3]` Genetics & Molecular Testing
- `[T3]` Health Screening
- `[T3]` Low-Dose CT Screening
- `[T3]` Pharmacogenomic Assessment
- `[T3]` Prenatal Screening

**Gastro** (38)

- `[CUT]` D-Xylose Test
- `[CUT]` Pentagastrin Stimulation Test
- `[CUT]` Secretin Test
- `[T3]` 24-hour pH Monitoring
- `[T3]` Anorectal Manometry
- `[T3]` Anoscopy
- `[T3]` Anti-LKM Antibody
- `[T3]` Barium Enema
- `[T3]` Barium Swallow
- `[T3]` CSF Studies
- `[T3]` CT Colonography
- `[T3]` CT Enterography
- `[T3]` Colonoscopy
- `[T3]` Coombs / Direct Testing
- `[T3]` Diagnostic Paracentesis
- `[T3]` Double Balloon Enteroscopy
- `[T3]` EUS
- `[T3]` Endorectal Ultrasound
- `[T3]` Esophageal Manometry
- `[T3]` FibroScan / Transient Elastography
- `[T3]` Flexible Sigmoidoscopy
- `[T3]` G-CSF
- `[T3]` Gastrin Level
- `[T3]` H. Pylori Testing
- `[T3]` H. pylori Urea Breath Test
- `[T3]` Hepatitis Panel
- `[T3]` Liver Auto-antibodies
- `[T3]` Liver Biopsy
- `[T3]` Liver Function Panel
- `[T3]` MRCP
- `[T3]` MRI Small Bowel
- `[T3]` Pale Stools
- `[T3]` Pancreatic & Digestive Enzymes
- `[T3]` Panendoscopy
- `[T3]` Rubella / Varicella Serology
- `[T3]` Sigmoidoscopy
- `[T3]` Small Bowel Biopsy
- `[T3]` Wireless Capsule Endoscopy

**General** (11)

- `[T3]` ALP
- `[T3]` Albumin
- `[T3]` Ammonium
- `[T3]` Calcitonin
- `[T3]` Gallium Scan
- `[T3]` Incisional Biopsy
- `[T3]` Lactate Dehydrogenase
- `[T3]` Serum Albumin
- `[T3]` Serum Ceruloplasmin
- `[T3]` Stains
- `[T3]` Uric Acid

**Geriatrics** (1)

- `[T3]` Short Physical Performance Battery

**Gynaecology** (7)

- `[T3]` C-Spine X-Ray
- `[T3]` Cervical Screening Abnormality
- `[T3]` Compression Test
- `[T3]` Distraction Test
- `[T3]` Genital / Cervical Swab Panel
- `[T3]` Hormone Panel
- `[T3]` Liquid Cytology

**Haematology** (28)

- `[CUT]` Osmotic Fragility Test
- `[CUT]` Schilling Test
- `[CUT]` Sickle Cell Prep
- `[T1]` CBC & Peripheral Blood
- `[T3]` ADAMTS13 Activity
- `[T3]` Anti-Intrinsic Factor Ab
- `[T3]` Anti-Parietal Cell Ab
- `[T3]` Beta-2 Microglobulin
- `[T3]` Biopsy & Procedures
- `[T3]` Coagulation Profile
- `[T3]` Erythropoietin Level
- `[T3]` Factor VIII Assay
- `[T3]` Flow Cytometry
- `[T3]` HIT ELISA
- `[T3]` Haptoglobin
- `[T3]` Hb Electrophoresis
- `[T3]` Homocysteine
- `[T3]` Immunohematology
- `[T3]` Iron Studies `[? dup?]` *matched:* `Iron studies interpretation`
- `[T3]` Lymphoscintigraphy
- `[T3]` Methylmalonate
- `[T3]` Petechiae
- `[T3]` Ristocetin Cofactor Activity
- `[T3]` Serotonin Release Assay
- `[T3]` Serum Electrophoresis
- `[T3]` Serum Free Light Chain Quantification
- `[T3]` VWF Antigen
- `[T3]` Vitamin B12 Level

**Infectious Diseases** (28)

- `[CUT]` B. cereus
- `[CUT]` Citrobacter
- `[CUT]` Dark Field Examination
- `[CUT]` Echinococcus granulosus
- `[CUT]` Human Herpes Virus 8
- `[CUT]` India-Ink Stain
- `[T1]` Blood Cultures `[? dup?]` *matched:* `Blood Cultures and Microbiology Basics`
- `[T3]` ASOT
- `[T3]` Autoimmune / Rheum Serology
- `[T3]` Bacteroides
- `[T3]` Candida albicans
- `[T3]` Carbapenemase-Producing Enterobacteriaceae
- `[T3]` Celiac Serology
- `[T3]` Cryptosporidium
- `[T3]` Enterococcus spp.
- `[T3]` Fusobacterium
- `[T3]` Giardia lamblia
- `[T3]` Gram Stain
- `[T3]` HIV Panel
- `[T3]` Microbiology Panel
- `[T3]` Monospot
- `[T3]` Parvovirus Serology
- `[T3]` Positive Autoimmune Serology
- `[T3]` Stool & Fecal Studies
- `[T3]` Syphilis Panel
- `[T3]` Vasculitis Serology
- `[T3]` Viral Culture
- `[T3]` Western Blot

**Neurology** (2)

- `[T3]` EMG / NCS
- `[T3]` ICP Monitoring

**Obstetrics** (7)

- `[T2]` Biophysical Profile
- `[T2]` Cordocentesis
- `[T2]` Ferning Test
- `[T2]` Fetal Fibronectin
- `[T2]` Kleihauer-Betke Test
- `[T2]` Nitrazine Test
- `[T2]` Prenatal Screening Panel

**Oncology** (2)

- `[T3]` FAMCARE-P16
- `[T3]` Tumor Markers

**Orthopaedics** (5)

- `[T3]` Bone Densitometry / DEXA
- `[T3]` Bone Scan
- `[T3]` Femoral Stretch Test
- `[T3]` Pelvic X-Ray
- `[T3]` Protein & Immune Profile

**Paediatrics** (1)

- `[T3]` Newborn Screening

**Renal & Urology** (13)

- `[T1]` Urinalysis Panel
- `[T3]` 24-hour Urine Copper
- `[T3]` Adrenal / Cortisol
- `[T3]` Dark Urine
- `[T3]` Elevated PSA
- `[T3]` Fecal Incontinence
- `[T3]` Metanephrines
- `[T3]` Renal Function Panel
- `[T3]` Urine ACR
- `[T3]` Urine Cytology
- `[T3]` Urine Protein Electrophoresis
- `[T3]` Urodynamic Studies
- `[T3]` Uroflowmetry

**Respiratory** (8)

- `[T2]` Nasopharyngeal Swab
- `[T2]` Pulmonary Function Tests
- `[T2]` Pulse Oximetry
- `[T2]` Sleep Studies
- `[T2]` Sputum Culture
- `[T2]` Sweat Chloride Test
- `[T2]` Tuberculosis Screening
- `[T2]` V/Q Scan

**Rheumatology** (11)

- `[T3]` ANCA Profile
- `[T3]` Allergy Skin Testing
- `[T3]` Anti-CCP
- `[T3]` Anti-Centromere Antibodies
- `[T3]` Autoimmune / ANA Panel
- `[T3]` Creatine Kinase
- `[T3]` HLA-B27 Test
- `[T3]` Muscle Biopsy
- `[T3]` Myositis Profile
- `[T3]` Synovial Fluid Analysis
- `[T3]` Temporal Artery Biopsy

**Safeguarding** (1)

- `[T3]` Elder Abuse Suspicion Index

**Sexual Health** (1)

- `[T3]` STI Screening

### exam manoeuvres — 12

**Orthopaedics** (11)

- Adam's Test
- Anterior Drawer Test
- FABER Test
- Finkelstein's Test
- Grind Test
- Lachman Test
- Pivot Shift Test
- Posterior Drawer Test
- Straight Leg Raise
- Thompson Test
- Trendelenburg Test

**Rheumatology** (1)

- Modified Schober Test

### procedures — 4

**Cardiology** (3)

- Cardioversion
- Carotid Endarterectomy
- ICD

**Orthopaedics** (1)

- External Fixation


## Drug Classes — 420 (388 no header + 32 ambiguous)

Build product: mechanism, key agents, indications, adverse effects, interactions, monitoring.

The **subsection is the build unit**; classes inherit its tier.

### 1 Allergy and anaphylaxis

- `[T2]` **Antihistamines**
  - Antihistamines (eye)
  - Antihistamines (intranasal)
  - H1 Antagonists (1st Gen)
  - Less sedating antihistamines
  - Sedating antihistamines
- `[T2]` **Drugs for allergic and inflammatory eye conditions**
  - Corticosteroids (eye)
  - NSAIDs (eye)
- `[T2]` **Other drugs for allergic eye conditions**
- `[T2]` **Other drugs for allergy**
  - Mast cell stabilisers
- `[T2]` **Sympathomimetics (anaphylaxis)**

### 2 Anaesthetics

- `[T3]` **Drugs for local anaesthesia**
  - Local Anesthetics (Amides)
  - Local Anesthetics (Esters)
  - Local Anesthetics (VG Na+ Blockers)
  - Local anaesthetics `[? fp?]` *matched:* `Risks of local anaesthetics`
  - Local anaesthetics (eye) `[? fp?]` *matched:* `Risks of local anaesthetics`
- `[T3]` **General anaesthetics**
  - Barbiturates (GABA-A Modulators)
  - IV general anaesthetics
  - Inhalational Anesthetics (Gases)
  - Inhalational Anesthetics (Volatiles)
  - Inhaled anaesthetics
  - Intravenous Anesthetics (GABA-A Modulators)
  - Intravenous Anesthetics (NMDA Antagonists)
- `[T3]` **Neuromuscular blockers**
  - Depolarising neuromuscular blockers
  - Drugs for reversing neuromuscular blockade
  - Non-depolarising neuromuscular blockers
- `[T3]` **Other agents used in anaesthesia**
  - Anticholinergics (anaesthesia) `[? fp?]` *matched:* `Anticholinergic burden — specifically worth knowing in Australia`
  - Opioids (anaesthesia) `[? fp?]` *matched:* `Conversion between opioids`

### 3 Analgesics

- `[T2]` **Drugs for gout**
  - Other drugs for gout
  - Xanthine Oxidase Inhibitors
- `[T2]` **Drugs for migraine**
  - CGRP Antagonists (Monoclonal Antibodies)
  - Calcitonin gene-related peptide antagonists
  - Ergot Alkaloids (5-HT Agonists)
  - Migraine Therapies (Calcium Channel Blockers)
  - Other drugs to prevent migraine
  - Triptans
  - Triptans (5-HT1B/1D Agonists)
- `[T2]` **Drugs for opioid dependence**
- `[T1]` **Drugs for pain relief**
  - COX-2 Selective NSAIDs
  - Mu-Opioid Receptor Agonists (Full)
  - Mu-Opioid Receptor Agonists (Partial)
  - Mu-Opioid Receptor Antagonists
  - NSAIDs
  - Non-Selective NSAIDs
  - Non-opioid analgesics
  - Opioid Analgesics (Strong / Full Agonists)
  - Opioid analgesics

### 4 Antidotes and antivenoms

- `[T1]` **Antidotes**
  - Chelating Agents
  - Specific Reversal Agents / Antidotes
- `[T1]` **Antivenoms**
  - Other antivenoms
  - Snake antivenoms
- `[T2]` **Drugs that chelate iron**
  - Iron Chelating Agents

### 5 Anti-infectives

- `[T2]` **Anthelmintics**
  - Benzimidazoles
  - Other anthelmintics
- `[T1]` **Antibacterials**
  - Aminoglycosides
  - Ansamycins
  - Antibacterials (ear)
  - Antibacterials (skin)
  - Antimycobacterials
  - Carbacephem
  - Carbapenems
  - Cephalosporins
  - Glycopeptides
  - Lincosamides
  - Lipopeptide
  - Macrolides
  - Metronidazole
  - Monobactams
  - Nitrofurans
  - Other antibacterials
  - Penicillin combinations
  - Penicillins
  - Polypeptides
  - Quinolones
  - Rifamycins
  - Tetracyclines
- `[T2]` **Antifungals**
  - Azoles
  - Echinocandins
  - Other antifungals
- `[T2]` **Antiprotozoals**
  - Antimalarials
  - Other antiprotozoals
- `[T2]` **Antiretrovirals**
  - HIV-Protease inhibitors
  - Integrase inhibitors
  - Non-nucleoside reverse transcriptase inhibitors
  - Nucleoside reverse transcriptase inhibitors
  - Other antiretrovirals
- `[T2]` **Antivirals**
  - Antivirals (eye)
  - Antivirals (skin)
  - Antivirals for viral hepatitis
  - Guanine analogues
  - Interferons
  - Neuraminidase inhibitors
  - Other antivirals

### 6 Cardiovascular drugs

- `[T1]` **Anticoagulants** *(subsection already has a header; classes below unbuilt)*
  - Direct thrombin inhibitors
  - Factor Xa inhibitors
  - Heparins `[? fp?]` *matched:* `Unfractionated heparin (UFH)`
  - Vitamin K antagonists
- `[T1]` **Antihypertensives** `[? fp?]` *matched:* `0.2.4 Antihypertensives — side effects`
  - ACE Inhibitors
  - Alpha-1 Selective Blockers
  - Alpha-2 Adrenergic Agonists (Central)
  - Alpha-Blockers (Non-selective)
  - Alpha2 agonists
  - Angiotensin II Receptor Blockers
  - Beta-Blockers (Cardioselective) `[? fp?]` *matched:* `Beta-blockers — selectivity, and why the choice is not interchangeable`
  - Beta-Blockers (Non-selective) `[? fp?]` *matched:* `Beta-blockers — selectivity, and why the choice is not interchangeable`
  - Beta-blockers `[? dup?]` *matched:* `Beta-blockers — selectivity, and why the choice is not interchangeable`
  - Calcium Channel Blockers (DHP)
  - Calcium Channel Blockers (Non-DHP)
  - Calcium channel blockers
  - Direct Arteriolar Vasodilators
  - Diuretics (Thiazide-like)
  - Other antihypertensives
  - Sartans
  - Thiazide and related diuretics
- `[T2]` **Antiplatelet drugs**
  - Glycoprotein IIb/IIIa inhibitors
  - Other antiplatelet drugs
  - Thienopyridines
- `[T2]` **Drugs for angina and acute coronary syndromes**
  - Nitrates
  - Other antianginal drugs
- `[T2]` **Drugs for arrhythmias**
  - Antiarrhythmics `[? dup?]` *matched:* `Antiarrhythmics — the Vaughan-Williams classification`
  - Antiarrhythmics (Class III) `[? fp?]` *matched:* `Antiarrhythmics — the Vaughan-Williams classification`
  - Antiarrhythmics (Class Ia) `[? fp?]` *matched:* `Antiarrhythmics — the Vaughan-Williams classification`
  - Antiarrhythmics (Class Ib) `[? fp?]` *matched:* `Antiarrhythmics — the Vaughan-Williams classification`
  - Antiarrhythmics (Class Ic) `[? fp?]` *matched:* `Antiarrhythmics — the Vaughan-Williams classification`
- `[T2]` **Drugs for dyslipidaemia**
  - Cholesterol Absorption Inhibitors
  - Fibrates
  - HMG-CoA Reductase Inhibitors
  - Nicotinic Acid
  - Other drugs for dyslipidaemia
  - PCSK9 Inhibitors
  - Statins
- `[T1]` **Drugs for heart failure**
  - Aldosterone antagonists
  - Diuretics (Loop)
  - Loop diuretics
  - Other diuretics
  - Other drugs for heart failure
- `[T2]` **Drugs for other cardiovascular disorders**
  - Alpha-1 Adrenergic Agonists
  - Antidiuretic hormone agonists and antagonists
  - Beta-1 Adrenergic Agonists
  - Drugs for orthostatic hypotension
  - Drugs for peripheral vascular disease
  - Phosphodiesterase 3 (PDE3) Inhibitors
  - Phosphodiesterase 5 inhibitors (cardiovascular)
  - Sympathomimetics (cardiovascular)
- `[T2]` **Drugs for reversing anticoagulation**
- `[T2]` **Other drugs affecting haemostasis**
- `[T2]` **Thrombolytics**
  - Thrombolytics (Plasminogen Activators)

### 7 Blood and electrolytes

- `[T2]` **Drugs for anaemias**
  - Colony stimulating factors
  - Erythropoiesis-Stimulating Agents
  - Erythropoietin agonists
  - Iron Supplements
  - Other drugs for anaemias
- `[T2]` **Drugs for electrolyte imbalance**
  - Calcium Salts / Supplements
  - Drugs for potassium imbalance
  - Essential Minerals
  - Other drugs for electrolyte imbalance
  - Phosphate binders
- `[T2]` **Vitamins and supplements**
  - Essential Fatty Acids
  - Fat-Soluble Vitamins
  - Water-Soluble Vitamins

### 8 Dermatological drugs

- `[T3]` **Drugs for acne**
  - Keratolytics
  - Other drugs for acne
  - Retinoids (Systemic)
  - Retinoids (Topical RAR Agonists)
  - Retinoids (oral)
  - Retinoids (skin)
- `[T3]` **Drugs for eczema**
  - Corticosteroids (skin)
  - Glucocorticoids (Topical)
  - Other drugs for eczema
  - PDE-4 Inhibitors (Topical)
  - Topical Calcineurin Inhibitors
- `[T3]` **Drugs for psoriasis**
  - Antimitotics (Topical)
  - Immunosuppressants (psoriasis)
  - Other drugs for psoriasis
  - Tars
  - Vitamin D Analogs (Topical)
- `[T3]` **Drugs for skin infections**
  - Azoles (skin)
- `[T3]` **Drugs for warts**
- `[T3]` **Other dermatological drugs**
- `[T3]` **Scabicides and pediculicides**

### 9 Ear nose and throat drugs

- `[T3]` **Drugs for ear infections**
- `[T3]` **Drugs for ear wax**
  - Cerumenolytics
- `[T3]` **Drugs for mouth and throat conditions**
- `[T3]` **Drugs for other nasal conditions**
- `[T3]` **Drugs for rhinitis and sinusitis**
  - Corticosteroids (intranasal)
  - Other drugs for rhinitis and sinusitis
- `[T3]` **Intranasal decongestants**
  - Oral decongestants

### 10 Endocrine drugs

- `[T2]` **Drugs affecting bone**
  - Calcimimetics
  - Other drugs affecting bone
  - Parathyroid Hormone Analogs
  - RANK Ligand Inhibitors
  - Sclerostin Inhibitors
  - Vitamin D `[? fp?]` *matched:* `Vitamin D Deficiency`
- `[T1]` **Drugs for diabetes**
  - Alpha-Glucosidase Inhibitors
  - Biguanides
  - DPP-4 Inhibitors
  - GLP-1 Receptor Agonists
  - Glucagon-like peptide-1 analogues
  - Insulins (Intermediate-Acting) `[? fp?]` *matched:* `Insulin regimens`
  - Insulins (Long-Acting) `[? fp?]` *matched:* `Insulin regimens`
  - Insulins (Rapid-Acting) `[? fp?]` *matched:* `Insulin regimens`
  - Insulins (Short-Acting) `[? fp?]` *matched:* `Insulin regimens`
  - Meglitinides
  - Other drugs for diabetes
  - SGLT2 Inhibitors
  - Sulfonylureas
  - Thiazolidinediones
- `[T2]` **Drugs for hypoglycaemia**
  - Glucagon Receptor Agonists
- `[T2]` **Drugs for other endocrine disorders**
  - Corticosteroids
  - Dopamine Agonists (Ergot Derivatives)
  - Glucocorticoids (Systemic)
  - Growth hormone
  - Mineralocorticoids
  - Somatostatin analogues
  - Vasopressin Receptor Antagonists
- `[T2]` **Drugs for thyroid disorders**
  - Antithyroid drugs
  - Other drugs for thyroid disorders
  - Synthetic Thyroid Hormones
  - Thioamides
  - Thyroid hormones

### 11 Eye drugs

- `[T3]` **Drugs for dry eyes**
- `[T3]` **Drugs for eye examinations and procedures**
- `[T3]` **Drugs for eye infections**
- `[T3]` **Drugs for glaucoma**
  - Beta-blockers (eye) `[? fp?]` *matched:* `Beta-blockers — selectivity, and why the choice is not interchangeable`
  - Carbonic anhydrase inhibitors
  - Other drugs for glaucoma
  - Prostaglandin analogues (eye)
- `[T3]` **Drugs for retinal disease**
  - VEGF Inhibitors

### 12 Gastrointestinal drugs

- `[T2]` **Antidiarrheals**
  - Opioid Antidiarrheals
  - Other drugs for diarrhoea
- `[T1]` **Antiemetics**
  - 5HT3 antagonists
  - Dopamine antagonists (antiemetic)
  - Other drugs for nausea and vomiting
  - Substance P antagonists
- `[T2]` **Drugs affecting gastrointestinal motility**
- `[T2]` **Drugs for dyspepsia reflux and peptic ulcers**
  - Antacids
  - H2 antagonists
  - Other drugs for ulcers
  - Proton Pump Inhibitors
  - Proton pump inhibitors
- `[T2]` **Drugs for inflammatory bowel diseases**
  - 5-Aminosalicylates
  - Corticosteroids (gastrointestinal)
  - Other drugs for inflammatory bowel disease
- `[T2]` **Drugs for perianal disorders**
- `[T2]` **Gastrointestinal decontaminants**
- `[T2]` **Laxatives**
  - Osmotic laxatives
  - Other laxatives
  - Stimulant laxatives
  - Stool softeners
- `[T2]` **Other gastrointestinal drugs**
  - Bile Acid Sequestrants

### 13 Genitourinary drugs

- `[T3]` **Bladder instillations**
- `[T3]` **Drugs for adrenal insufficiency**
- `[T3]` **Drugs for benign prostatic hyperplasia and prostatitis**
  - 5-Alpha-Reductase Inhibitors
  - Alpha-1 Blockers (Uroselective)
  - Selective alpha-blockers (genitourinary)
- `[T3]` **Drugs for kidney stones**
- `[T3]` **Drugs for sexual dysfunction**
  - Other drugs for sexual dysfunction
  - Phosphodiesterase 5 inhibitors
- `[T3]` **Drugs for urinary tract disorders**
  - Anticholinergics (genitourinary) `[? fp?]` *matched:* `Anticholinergic burden — specifically worth knowing in Australia`
  - Other drugs for urinary incontinence
- `[T3]` **Urinary alkalinisers and acidifiers**

### 14 Immunomodulators and antineoplastics

- `[T3]` **Cytotoxic antineoplastics**
  - Antimetabolites
  - Cytotoxic Antibiotics
  - Other cytotoxic antineoplastics
- `[T3]` **Drugs used with antineoplastics**
- `[T3]` **Hormonal antineoplastic drugs**
  - Antiandrogens
  - Aromatase inhibitors
  - Gonadotrophin-releasing hormone agonists (oncology)
  - Other hormonal antineoplastics
- `[T3]` **Immunomodulating drugs**
  - Calcineurin Inhibitors
  - Immunosuppressants
  - Other immunomodulating drugs
  - Other immunosuppressants
  - TNF-Alpha Inhibitors
  - mTOR Inhibitors
- `[T3]` **Interferons**
- `[T3]` **Non-cytotoxic antineoplastics**
  - Antineoplastic antibodies
  - Other non-cytotoxic antineoplastics

### 15 Neurological drugs

- `[T3]` **Antiepileptics** `[? dup?]` *matched:* `Anticonvulsants / Antiepileptics`
  - Other antiepileptics
- `[T3]` **Drugs for Alzheimer's disease**
  - Acetylcholinesterase Inhibitors (Central)
  - NMDA Receptor Antagonists
  - Other drugs for Alzheimer's disease
- `[T3]` **Drugs for multiple sclerosis**
- `[T3]` **Drugs for myasthenia gravis**
- `[T3]` **Drugs for other neurological conditions**
- `[T3]` **Drugs for parkinsonism**
  - Anticholinergics `[? fp?]` *matched:* `Anticholinergic burden — specifically worth knowing in Australia`
  - Dopamine Agonists (Non-Ergot)
  - Dopamine Precursors
  - Dopamine agonists (parkinsonism)
  - MAO-B Inhibitors
  - Other drugs for Parkinson's disease
- `[T3]` **Drugs for vestibular disorders**

### 16 Obstetric and gynaecological drugs

- `[T3]` **Drugs affecting lactation**
- `[T3]` **Drugs for contraception**
  - Combined Oral Contraceptives `[? dup?]` *matched:* `Combined oral contraceptive pill (COCP)`
  - Combined oral contraceptives `[? dup?]` *matched:* `Combined oral contraceptive pill (COCP)`
  - Intrauterine devices `[? fp?]` *matched:* `Copper intrauterine device (IUD)`
  - Progestins
  - Progestogens `[? fp?]` *matched:* `Progestogen-only pill (POP / "mini pill")`
- `[T3]` **Drugs for endometriosis**
  - Gonadotrophin-releasing hormone agonists
- `[T3]` **Drugs for heavy menstrual bleeding**
- `[T3]` **Drugs for infertility**
- `[T3]` **Drugs for menopausal symptoms**
  - SERMs
  - Selective oestrogen receptor modulators
- `[T3]` **Drugs for menstrual symptoms**
- `[T3]` **Drugs for preterm labour**
- `[T3]` **Drugs for vaginal infections**
- `[T3]` **Drugs in labour**
  - Oxytocic drugs
- `[T3]` **Drugs in pre-eclampsia and eclampsia**
- `[T3]` **Other drugs used in obstetrics**
  - Prostaglandins
- `[T3]` **Sex hormones and modulators**
  - Androgens
  - Anti-androgens
  - Gender Affirming Hormone Care

### 17 Psychotropic drugs

- `[T3]` **Antidepressants** `[? fp?]` *matched:* `Tricyclic antidepressants (TCAs)`
  - MAOIs (Irreversible Non-selective) `[? dup?]` *matched:* `Monoamine oxidase inhibitors (MAOIs)`
  - NDRIs
  - Other antidepressants
  - SNRIs `[? dup?]` *matched:* `Serotonin-noradrenaline reuptake inhibitors (SNRIs)`
  - Serotonin and noradrenaline reuptake inhibitors
- `[T3]` **Drugs for alcohol dependence**
- `[T3]` **Drugs for anxiety and sleep disorders**
  - Barbiturates
  - Other drugs for anxiety and sleep disorders
- `[T3]` **Drugs for attention deficit hyperactivity disorder**
  - Non-amphetamine psychostimulants
  - Other drugs for attention deficit hyperactivity disorder
  - Psychostimulants
- `[T3]` **Drugs for bipolar disorder**
- `[T3]` **Drugs for nicotine dependence**
- `[T3]` **Other psychotropic drugs**

### 18 Respiratory drugs

- `[T3]` **Drugs for asthma and chronic obstructive pulmonary disease**
  - Anticholinergics (inhaled) `[? fp?]` *matched:* `Anticholinergic burden — specifically worth knowing in Australia`
  - Beta2 agonists
  - Corticosteroids (inhaled)
  - Other drugs for asthma
  - Short-Acting Beta-2 Agonists
  - Theophyllines
- `[T3]` **Drugs for cough**
  - Mucolytics
  - Opioid cough suppressants
- `[T3]` **Drugs for pulmonary hypertension**
  - Endothelin Receptor Antagonists
  - Endothelin antagonists
  - Other drugs for pulmonary hypertension
  - Prostacyclin Analogs
- `[T3]` **Drugs used in cystic fibrosis**
- `[T3]` **Other respiratory drugs**
- `[T3]` **Pulmonary surfactants**

### 19 Rheumatological drugs

- `[T3]` **Drugs for other musculoskeletal conditions**
  - Antimalarials / DMARDs
  - Immunosuppressants (rheumatology)
  - Muscle Relaxants (GABA-B Agonists)

### 20 Vaccines

- `[T3]` **Immunoglobulins** `[? fp?]` *matched:* `Passive Immunisation — Immunoglobulin After an Exposure`
  - Intravenous Immunoglobulins
- `[T3]` **Vaccines**

### 21 Miscellaneous

- `[T3]` **Specialised drugs**


## Presentations & Symptoms — 534 (485 no header + 49 ambiguous)

Build product: differential diagnosis, focused history, examination, first-line investigations. **Outside the previous queue's scope — included because the ambiguous set spans all lists.**

### presentations — 534

**Acid-Base, Fluids & Electrolytes** (1)

- `[T3]` Dehydration

**Breast** (3)

- `[T3]` Breast Lump
- `[T3]` Breast Pain
- `[T3]` Galactorrhoea

**Cardiology & Vascular** (16)

- `[T1]` Acute Chest Pain
- `[T3]` Bradycardia `[? fp?]` *matched:* `0.8 Bradycardia: Peri-arrest`
- `[T3]` Chest Tightness
- `[T3]` Chronic Chest Pain ‡
- `[T3]` Claudication
- `[T3]` Elevated Blood Pressure
- `[T3]` Hypertensive Urgency
- `[T3]` Hypotension
- `[T3]` Multifocal Atrial Tachycardia
- `[T3]` Orthopnoea
- `[T3]` Paroxysmal Hypertension
- `[T3]` Paroxysmal Nocturnal Dyspnoea
- `[T3]` Pleuritic Chest Pain
- `[T3]` Presyncope
- `[T3]` Symptomatic Bradycardia
- `[T3]` Tachycardia `[? fp?]` *matched:* `0.7 Ventricular Tachycardia`

**Dermatology** (36)

- `[T2]` Acute Inflammatory Dermatosis ‡
- `[T2]` Acute Rash
- `[T3]` Blistering Rash
- `[T3]` Chronic Leg Ulcer
- `[T3]` Chronic Rash
- `[T3]` Cutaneous Ulcer
- `[T3]` Cyanosis
- `[T3]` Diaper Rash (napkin dermatitis)
- `[T3]` Diaphoresis
- `[T3]` Ecchymosis
- `[T3]` Episodic Flushing
- `[T3]` Excessive Sweating
- `[T3]` Flushing
- `[T3]` Generalised Pruritus
- `[T3]` Genital Ulcer
- `[T3]` Hair Loss `[? dup?]` *matched:* `Alopecia (Hair Loss) — Approach and Differential`
- `[T3]` Hyperpigmentation
- `[T3]` Localised Pruritus
- `[T3]` Maculopapular Rash
- `[T3]` Mouth Ulcer
- `[T3]` Nail Change
- `[T3]` Nail Discolouration
- `[T3]` Night Sweats
- `[T3]` Non-Blanching Rash
- `[T3]` Non-Healing Skin Lesion
- `[T3]` Pallor `[? dup?]` *matched:* `Fatigue and Pallor — Approach and Differential`
- `[T3]` Photosensitivity
- `[T3]` Pressure Ulcer
- `[T3]` Pruritus `[? fp?]` *matched:* `Pruritus vulvae (vaginal itch)`
- `[T3]` Purpuric Rash
- `[T3]` Rash `[? dup?]` *matched:* `Skin Lesion / Rash`
- `[T3]` Skin Lesion `[? dup?]` *matched:* `Skin Lesion / Rash`
- `[T3]` Skin Mass
- `[T3]` Skin Nodule
- `[T3]` Sun Sensitivity
- `[T3]` Suspicious Pigmented Lesion

**ENT & Oral** (30)

- `[T2]` Acute Ear Pain
- `[T2]` Acute Epistaxis
- `[T2]` Acute Hoarseness
- `[T2]` Acute Sore Throat
- `[T3]` Anterior Neck Mass
- `[T3]` Chronic Ear Pain ‡
- `[T3]` Chronic Hoarseness
- `[T3]` Chronic Sore Throat
- `[T3]` Dental Pain
- `[T3]` Ear Discharge
- `[T3]` Expanding Neck Mass
- `[T3]` Facial Pain
- `[T3]` Facial Swelling
- `[T3]` Hearing Loss `[? dup?]` *matched:* `Hearing loss — differential diagnosis`
- `[T3]` Hearing Problem
- `[T3]` Hoarseness `[? dup?]` *matched:* `Dysphonia (hoarseness)`
- `[T3]` Nasal Discharge
- `[T3]` Neck Lump
- `[T3]` Neck Mass
- `[T3]` Odynophagia
- `[T3]` Recurrent Epistaxis
- `[T3]` Rhinorrhoea `[? fp?]` *matched:* `CSF rhinorrhoea`
- `[T3]` Salivary Gland Swelling
- `[T3]` Severe Facial Pain
- `[T3]` Sinus Pain
- `[T3]` Submandibular Swelling
- `[T3]` Sudden Sensorineural Hearing Loss
- `[T3]` Swollen Tongue
- `[T3]` Throat Mass
- `[T3]` Tinnitus `[? dup?]` *matched:* `Tinnitus — differential diagnosis`

**Emergency & Critical Care** (2)

- `[T3]` Chronic Airway Obstruction ‡
- `[T3]` Major Trauma `[? dup?]` *matched:* `Major Trauma — Primary Survey`

**Endocrine & Metabolic** (13)

- `[T3]` Appetite Change
- `[T3]` Hyperthyroid Symptom
- `[T3]` Hypothyroid Symptom
- `[T3]` Incidental Pituitary Mass
- `[T3]` Osteoporotic Pain
- `[T3]` Polydipsia
- `[T3]` Poor Weight Gain
- `[T3]` Progressive Acral Enlargement
- `[T3]` Suspected Thyrotoxicosis
- `[T3]` Thyroid Nodule
- `[T3]` Thyroid Swelling
- `[T3]` Weight Gain
- `[T3]` Weight Loss

**Environmental & Physical Injury** (6)

- `[T3]` Burn
- `[T3]` Chemical Burn
- `[T3]` Cold Injury
- `[T3]` Electrical Injury
- `[T3]` Heartburn
- `[T3]` Heat Intolerance

**Ethics, Law & Professional Practice** (4)

- `[T2]` Capacity Concern
- `[T2]` Multimorbidity `[? fp?]` *matched:* `The Atopic Child (Atopic March / Atopic Multimorbidity)`
- `[T2]` Professional Practice Concern
- `[T2]` Treatment Refusal

**Gastroenterology & Hepatology** (56)

- `[T1]` Acute Abdominal Pain
- `[T1]` Upper Gastrointestinal Bleeding
- `[T2]` Acute Anorectal Pain
- `[T2]` Acute Constipation
- `[T2]` Acute Diarrhoea
- `[T2]` Acute Hepatic Pain
- `[T2]` Acute Nausea ‡
- `[T2]` Acute Pancreatic Pain
- `[T2]` Acute Vomiting
- `[T3]` Abdominal Distension
- `[T3]` Abdominal Mass
- `[T3]` Abdominal Swelling
- `[T3]` Abdominal Trauma
- `[T3]` Anal Itch
- `[T3]` Anal Lump
- `[T3]` Anorectal Pain
- `[T3]` Bilious Vomiting
- `[T3]` Bloating
- `[T3]` Change in Bowel Habit
- `[T3]` Chronic Abdominal Pain
- `[T3]` Chronic Anorectal Pain ‡
- `[T3]` Chronic Constipation
- `[T3]` Chronic Nausea
- `[T3]` Chronic Pancreatic Pain ‡
- `[T3]` Chronic Vomiting ‡
- `[T3]` Conjugated Jaundice
- `[T3]` Dyspepsia
- `[T3]` Dysphagia `[? dup?]` *matched:* `Dysphagia — approach`
- `[T3]` Early Satiety
- `[T3]` Epigastric Pain
- `[T3]` Flatulence
- `[T3]` Gastrointestinal Bleeding
- `[T3]` Haematemesis `[? fp?]` *matched:* `GI Bleeding — Haematemesis, Melaena, Rectal Bleeding (history context)`
- `[T3]` Hepatosplenomegaly
- `[T3]` Left Lower Quadrant Pain
- `[T3]` Left Upper Quadrant Pain
- `[T3]` Lower Gastrointestinal Bleeding
- `[T3]` Melaena `[? fp?]` *matched:* `GI Bleeding — Haematemesis, Melaena, Rectal Bleeding (history context)`
- `[T3]` Nausea `[? dup?]` *matched:* `Nausea and Vomiting`
- `[T3]` Non-Bilious Vomiting
- `[T3]` Obstructive Jaundice
- `[T3]` Rectal Bleeding `[? fp?]` *matched:* `GI Bleeding — Haematemesis, Melaena, Rectal Bleeding (history context)`
- `[T3]` Rectal Foreign Body
- `[T3]` Reflux Symptom
- `[T3]` Refractory Nausea
- `[T3]` Refractory Vomiting
- `[T3]` Right Lower Quadrant Pain
- `[T3]` Right Upper Quadrant Pain
- `[T3]` Severe Anorectal Pain
- `[T3]` Severe Constipation
- `[T3]` Suprapubic Pain
- `[T3]` Tenesmus
- `[T3]` Travel-Associated Diarrhoea
- `[T3]` Unconjugated Hyperbilirubinaemia
- `[T3]` Unconjugated Jaundice
- `[T3]` Vomiting `[? dup?]` *matched:* `Nausea and Vomiting`

**General & Cross-cutting** (16)

- `[T2]` Acute Oedema
- `[T3]` Chronic Fatigue `[? fp?]` *matched:* `Chronic fatigue syndrome (myalgic encephalomyelitis)`
- `[T3]` Chronic Oedema ‡
- `[T3]` Chronic Progressive Fatigue
- `[T3]` Conscious Collapse
- `[T3]` Eyelid Swelling
- `[T3]` Fatigue `[? fp?]` *matched:* `Chronic fatigue syndrome (myalgic encephalomyelitis)`
- `[T3]` Generalised Oedema
- `[T3]` Generalised Pain
- `[T3]` Generalised Weakness
- `[T3]` Lethargy
- `[T3]` Limb Swelling
- `[T3]` Malaise
- `[T3]` Peripheral Oedema
- `[T3]` Rest Pain
- `[T3]` Undifferentiated Lump

**General Practice & Preventive** (1)

- `[T3]` Occupational Health Concern

**Geriatrics** (1)

- `[T1]` Falls `[? fp?]` *matched:* `Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls)`

**Gynaecology & Reproductive** (19)

- `[T1]` Acute Vaginal Bleeding
- `[T2]` Acute Pelvic Pain
- `[T3]` Abnormal Uterine Bleeding `[? dup?]` *matched:* `Abnormal Uterine Bleeding — Approach and DDx`
- `[T3]` Amenorrhoea `[? fp?]` *matched:* `Primary amenorrhoea`
- `[T3]` Cervical Spine Trauma
- `[T3]` Intermenstrual Bleeding
- `[T3]` Menopausal Symptom
- `[T3]` Menstrual Irregularity
- `[T3]` Oligomenorrhoea
- `[T3]` Pelvic Mass
- `[T3]` Pelvic Pain `[? fp?]` *matched:* `Chronic pelvic pain`
- `[T3]` Postmenopausal Bleeding
- `[T3]` Vaginal Bleeding
- `[T3]` Vaginal Discharge `[? dup?]` *matched:* `Vaginal discharge — differential diagnosis`
- `[T3]` Vaginal Foreign Body
- `[T3]` Vulval Itch
- `[T3]` Vulval Lesion
- `[T3]` Vulval Pain
- `[T3]` Vulvovaginal Symptom

**Haematology** (13)

- `[T3]` Bleeding Tendency
- `[T3]` Bruising `[? dup?]` *matched:* `Bruising and Bleeding`
- `[T3]` Chronic Anaemia ‡
- `[T3]` Eosinophilia
- `[T3]` Gum Bleeding
- `[T3]` Hyperviscosity Symptom
- `[T3]` Monoclonal Gammopathy
- `[T3]` Pancytopenia
- `[T3]` Paraproteinaemia
- `[T3]` Postcoital Bleeding
- `[T3]` Prolonged Bleeding
- `[T3]` Purpura `[? fp?]` *matched:* `Henoch-Schönlein purpura (HSP, IgA vasculitis)`
- `[T3]` Undifferentiated Bleeding

**Infectious Diseases** (10)

- `[T1]` Fever in Immunocompromised Patient
- `[T3]` Chills
- `[T3]` Fever `[? fp?]` *matched:* `Pyrexia of unknown origin (PUO) / Fever of unknown origin (FUO)`
- `[T3]` Fever in Returning Traveller
- `[T3]` Fever of Unknown Origin `[? dup?]` *matched:* `Pyrexia of unknown origin (PUO) / Fever of unknown origin (FUO)`
- `[T3]` Fever with Rash
- `[T3]` Post-Operative Fever
- `[T3]` Prolonged Fever
- `[T3]` Rigors
- `[T3]` Undifferentiated Fever

**Neurology** (51)

- `[T1]` Acute Confusion
- `[T1]` Acute Focal Neurological Deficit
- `[T1]` Reduced Consciousness
- `[T1]` Thunderclap Headache
- `[T2]` Acute Facial Weakness
- `[T2]` Acute Neuromuscular Weakness
- `[T2]` Acute Sensory Disturbance
- `[T2]` Acute Vertigo
- `[T3]` Bradykinesia
- `[T3]` Carpal Tunnel Symptom
- `[T3]` Chronic Amnesia ‡
- `[T3]` Chronic Confusion ‡
- `[T3]` Chronic Facial Palsy ‡
- `[T3]` Chronic Focal Neurological Deficit ‡
- `[T3]` Chronic Neuro-Ophthalmic Dysfunction ‡
- `[T3]` Chronic Neuromuscular Weakness ‡
- `[T3]` Chronic Rigidity ‡
- `[T3]` Chronic Sensory Disturbance ‡
- `[T3]` Chronic Vertigo
- `[T3]` Cognitive Decline
- `[T3]` Cognitive Impairment `[? fp?]` *matched:* `Mild Cognitive Impairment (MCI)`
- `[T3]` Coma `[? fp?]` *matched:* `Glasgow Coma Scale (GCS)`
- `[T3]` Disequilibrium
- `[T3]` Dizziness `[? dup?]` *matched:* `Vertigo and Dizziness`
- `[T3]` Dysgraphia
- `[T3]` Episodic Vertigo
- `[T3]` Febrile Seizure
- `[T3]` Gait Difficulty
- `[T3]` Gait Disorder
- `[T3]` Gait Unsteadiness
- `[T3]` Generalised Seizure `[? dup?]` *matched:* `Generalised Seizure Subtypes`
- `[T3]` Headache `[? fp?]` *matched:* `Cluster Headache`
- `[T3]` Hypoaesthesia
- `[T3]` Loss of Balance
- `[T3]` Loss of Smell
- `[T3]` Loss of Taste
- `[T3]` Memory Impairment
- `[T3]` Numbness
- `[T3]` Paraesthesia
- `[T3]` Positional Headache
- `[T3]` Positional Vertigo `[? dup?]` *matched:* `Benign paroxysmal positional vertigo (BPPV)`
- `[T3]` Progressive Focal Weakness
- `[T3]` Prolonged Seizure
- `[T3]` Resting Tremor
- `[T3]` Restless Legs `[? dup?]` *matched:* `Restless Legs Syndrome`
- `[T3]` Seizure `[? fp?]` *matched:* `Anti-epileptic drug (AED) options by seizure type`
- `[T3]` Sialorrhoea
- `[T3]` Slurred Speech
- `[T3]` Tic
- `[T3]` Transient Loss of Consciousness
- `[T3]` Tremor

**Obstetrics** (7)

- `[T1]` First-Trimester Pain
- `[T3]` Early Pregnancy Bleeding
- `[T3]` Early Pregnancy Loss
- `[T3]` Fetal Development Concern
- `[T3]` Fetal Growth Concern
- `[T3]` First-Trimester Bleeding
- `[T3]` Postpartum Fever

**Ophthalmology** (26)

- `[T1]` Acute Visual Loss ‡
- `[T2]` Acute Eye Pain
- `[T2]` Acute Floaters
- `[T2]` Acute Visual Disturbance
- `[T3]` Chronic Eye Pain ‡
- `[T3]` Chronic Floaters ‡
- `[T3]` Chronic Red Eye ‡
- `[T3]` Chronic Visual Disturbance ‡
- `[T3]` Chronic Visual Loss
- `[T3]` Colour Vision Loss
- `[T3]` Diplopia
- `[T3]` Eye Discharge
- `[T3]` Eyelid Lesion
- `[T3]` Floaters
- `[T3]` Generalised Eye Pain
- `[T3]` Gradual Painless Vision Loss
- `[T3]` Halos
- `[T3]` Itchy Eye
- `[T3]` Night Blindness
- `[T3]` Photophobia
- `[T3]` Photopsia
- `[T3]` Scotoma
- `[T3]` Squint `[? dup?]` *matched:* `Strabismus (Squint)`
- `[T3]` Sudden Painless Vision Loss
- `[T3]` Vision Loss `[? fp?]` *matched:* `Causes of Sudden, Sustained Vision Loss`
- `[T3]` Visual Disturbance

**Orthopaedics & Trauma** (55)

- `[CUT]` Hill-Sachs lesion
- `[CUT]` Stener lesion
- `[T1]` Acute Back Pain
- `[T1]` Acute Limb Pain
- `[T2]` Acute Neck Pain
- `[T2]` Acute Soft Tissue Swelling
- `[T3]` Animal Bite
- `[T3]` Aural Foreign Body
- `[T3]` Back Pain `[? fp?]` *matched:* `Back pain red flags → urgent MRI`
- `[T3]` Bone Pain
- `[T3]` Chemical Eye Injury
- `[T3]` Chest Trauma
- `[T3]` Chronic Back Pain
- `[T3]` Chronic Limb Pain ‡
- `[T3]` Chronic Neck Pain ‡
- `[T3]` Corneal Foreign Body
- `[T3]` Crush Injury
- `[T3]` Disproportionate Extremity Pain
- `[T3]` Ear Trauma
- `[T3]` Elbow Pain
- `[T3]` Extremity Trauma
- `[T3]` Facial Trauma
- `[T3]` Foot Pain
- `[T3]` Foreign Body Sensation
- `[T3]` Head Trauma
- `[T3]` Hip Pain
- `[T3]` Jaw Pain
- `[T3]` Knee Pain
- `[T3]` Limb Pain
- `[T3]` Limp ‡
- `[T3]` Lower Back Pain
- `[T3]` Mechanical Back Pain
- `[T3]` Mechanical Spinal Pain
- `[T3]` Mobility Difficulty
- `[T3]` Mobility Impairment
- `[T3]` Musculoskeletal Lump
- `[T3]` Nasal Foreign Body
- `[T3]` Nasal Trauma
- `[T3]` Neck Pain
- `[T3]` Non-Specific Limb Pain
- `[T3]` Non-Traumatic Bone Pain
- `[T3]` Oropharyngeal Foreign Body
- `[T3]` Reduced Mobility
- `[T3]` Sciatica
- `[T3]` Shoulder Pain
- `[T3]` Soft Tissue Mass
- `[T3]` Soft Tissue Swelling
- `[T3]` Spinal Deformity
- `[T3]` Spinal Trauma
- `[T3]` Submersion Injury
- `[T3]` Swallowed Foreign Body
- `[T3]` TLICS Classification (Thoracolumbar Injury Classification and Severity Score)
- `[T3]` Trauma-Related Disorder
- `[T3]` Undifferentiated Bone Pain
- `[T3]` Wrist Pain

**Paediatrics & Neonatology** (38)

- `[T3]` Abdominal Mass in Child
- `[T3]` Abdominal Pain in Child
- `[T3]` Adolescent Mental Health Concern
- `[T3]` Adolescent Self-Harm
- `[T3]` Bone Pain in Child
- `[T3]` Child Emotional-Behavioural Concern
- `[T3]` Conjugated Neonatal Jaundice
- `[T3]` Constipation in Child
- `[T3]` Cyanosis in Infant
- `[T3]` Developmental Concern
- `[T3]` Diarrhoea in Child
- `[T3]` Excessive Crying
- `[T3]` Excessive Infant Crying
- `[T3]` Failure to Thrive
- `[T3]` Fever in Child
- `[T3]` Fever in Infant
- `[T3]` Fever in Neonate
- `[T3]` Growth Abnormality
- `[T3]` Hearing Loss in Child
- `[T3]` Hypotonia `[? fp?]` *matched:* `Neonatal hypotonia`
- `[T3]` Infant Jaundice
- `[T3]` Limp in Child
- `[T3]` Neck Lump in Child
- `[T3]` Neonatal Cyanosis
- `[T3]` Neonatal Fever
- `[T3]` Neonatal Vomiting
- `[T3]` Nocturnal Enuresis
- `[T3]` Poor Feeding
- `[T3]` Rash in Child
- `[T3]` Red Eye in Child
- `[T3]` School Difficulty in Child
- `[T3]` School Refusal
- `[T3]` Seizure in Child
- `[T3]` Short Stature
- `[T3]` Tall Stature
- `[T3]` Vomiting in Child
- `[T3]` Vomiting in Infant
- `[T3]` Wheeze in Child

**Psychiatry** (61)

- `[T1]` Acute Behavioural Disturbance
- `[T2]` Acute Agitation
- `[T2]` Acute Anxiety
- `[T2]` Acute Severe Anxiety
- `[T3]` Aggressive Behaviour
- `[T3]` Anhedonia
- `[T3]` Anorexia `[? fp?]` *matched:* `Anorexia nervosa`
- `[T3]` Anxiety `[? fp?]` *matched:* `Illness anxiety disorder (hypochondriasis)`
- `[T3]` Attention Difficulty
- `[T3]` Behavioural Change
- `[T3]` Binge Eating
- `[T3]` Body Image Disturbance
- `[T3]` Bruxism
- `[T3]` Childhood Behavioural Disturbance
- `[T3]` Chronic Anxiety
- `[T3]` Chronic Psychosis ‡
- `[T3]` Chronic Suicidal Ideation ‡
- `[T3]` Compulsion
- `[T3]` Concentration Difficulty
- `[T3]` Delusion
- `[T3]` Depersonalisation
- `[T3]` Depressive Symptom
- `[T3]` Derealisation
- `[T3]` Disorganised Behaviour
- `[T3]` Disruptive Behaviour
- `[T3]` Dissociative Symptom
- `[T3]` Early Morning Wakening
- `[T3]` Elevated Mood
- `[T3]` Emotional Dysregulation
- `[T3]` Emotional Lability
- `[T3]` Flashback
- `[T3]` Generalised Anxiety `[? dup?]` *matched:* `Generalised anxiety disorder (GAD)`
- `[T3]` Hallucination
- `[T3]` Health Anxiety
- `[T3]` Hyperactivity `[? fp?]` *matched:* `Attention deficit hyperactivity disorder (ADHD)`
- `[T3]` Hypersomnia
- `[T3]` Intrusive Thought
- `[T3]` Irritability
- `[T3]` Low Mood
- `[T3]` Mania
- `[T3]` Medically Unexplained Symptom
- `[T3]` Night Terror
- `[T3]` Night Terrors
- `[T3]` Nightmare
- `[T3]` Non-Acute Behavioural Problem
- `[T3]` Non-Specific Mental Health Presentation
- `[T3]` Obsession
- `[T3]` Obsessive-Compulsive Symptom
- `[T3]` Panic Attack
- `[T3]` Paranoia
- `[T3]` Personality Change
- `[T3]` Psychotic Symptom
- `[T3]` Purging Behaviour
- `[T3]` Restrictive Eating
- `[T3]` Sleep Disturbance
- `[T3]` Social Anxiety
- `[T3]` Somatic Symptom `[? dup?]` *matched:* `Somatic symptom disorder (somatisation disorder)`
- `[T3]` Somnambulism
- `[T3]` Stupor
- `[T3]` Thought Disorder
- `[T3]` Violent Behaviour

**Renal & Urology** (29)

- `[T1]` Acute Scrotal Pain
- `[T2]` Acute Urinary Retention
- `[T3]` Anuria
- `[T3]` Bladder Pain
- `[T3]` Chronic Scrotal Pain ‡
- `[T3]` Chronic Urinary Retention
- `[T3]` Dysuria
- `[T3]` Frequency
- `[T3]` Groin Lump
- `[T3]` Groin Pain
- `[T3]` Groin Swelling
- `[T3]` Haematuria
- `[T3]` Incidental Adrenal Mass
- `[T3]` Loin Pain
- `[T3]` Lower Urinary Tract Symptom
- `[T3]` Macroscopic Haematuria
- `[T3]` Microscopic Haematuria
- `[T3]` Nocturia
- `[T3]` Oliguria
- `[T3]` Penile Discharge
- `[T3]` Penile Pain
- `[T3]` Polyuria
- `[T3]` Pyuria
- `[T3]` Stress Incontinence
- `[T3]` Urge Incontinence
- `[T3]` Urgency
- `[T3]` Urinary Frequency
- `[T3]` Urinary Tract Trauma
- `[T3]` Urinary Urgency

**Respiratory** (15)

- `[T1]` Acute Dyspnoea
- `[T1]` Stridor `[? dup?]` *matched:* `Stridor — differential diagnosis`
- `[T2]` Acute Cough
- `[T2]` Acute Stridor
- `[T3]` Bradypnoea
- `[T3]` Chronic Cough
- `[T3]` Chronic Dyspnoea
- `[T3]` Chronic Progressive Dyspnoea
- `[T3]` Chronic Stridor
- `[T3]` Hypoxia
- `[T3]` Noisy Breathing
- `[T3]` Productive Cough
- `[T3]` Snoring `[? fp?]` *matched:* `Primary (simple) snoring`
- `[T3]` Solitary pulmonary nodule
- `[T3]` Tachypnoea

**Rheumatology & Immunology** (17)

- `[T2]` Acute Joint Pain
- `[T2]` Acute Joint Trauma
- `[T3]` Chronic Joint Pain
- `[T3]` Chronic Urticaria ‡
- `[T3]` Chronic Widespread Pain
- `[T3]` Joint Deformity
- `[T3]` Joint Stiffness
- `[T3]` Joint Swelling
- `[T3]` Joint Trauma
- `[T3]` Monoarthralgia
- `[T3]` Morning Stiffness
- `[T3]` Muscle Stiffness
- `[T3]` Muscle Weakness
- `[T3]` Neck Stiffness
- `[T3]` Non-Articular Musculoskeletal Pain
- `[T3]` Polyarthralgia
- `[T3]` Raynaud Phenomenon

**Safeguarding & Forensic** (4)

- `[T2]` Emotional Abuse Concern
- `[T2]` Fabricated Illness Concern
- `[T2]` Neglect Concern
- `[T2]` Safe Sleep Concern

**Sexual & Gender Health** (4)

- `[T3]` Gender Identity Concern
- `[T3]` Loss of Libido
- `[T3]` Pubertal Concern
- `[T3]` Virilisation

