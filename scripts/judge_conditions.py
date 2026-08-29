#!/usr/bin/env python3
"""Apply scope judgements to the ABSENT rows of checklist_external.csv.

HOW HONEST THIS IS, STATED PLAINLY
932 conditions came back ABSENT. Every one named in GAP or SYN below was
checked BY HAND with a targeted grep for its likely aliases, and the hit
count is recorded in the judgement text. Everything else is classified
OUT OF SCOPE **by rule, not by individual verification**: named fracture
patterns and eponyms, tumour subtypes, congenital dysmorphology, tropical
and imported infections not endemic to Australia, and single-gene disorders.
That rule is a judgement applied at scale and it will be wrong somewhere.
It is recorded here as a rule so that a later round can attack the rule
itself rather than re-deriving 900 individual decisions.
"""
import csv, os, sys

GAP = {
 # cardiovascular (system 1)
 "Peripartum Cardiomyopathy":"GAP: zero hits; postpartum breathlessness differential",
 "Pseudoaneurysm":"GAP: zero hits; post-catheterisation femoral pseudoaneurysm is a ward finding",
 "Multifocal Atrial Tachycardia":"GAP: zero hits; ECG differential in COPD",
 "Coronary Vasospasm":"GAP: an ACS mimic; vasospasm appears only in neurology and obstetrics contexts",
 # neurology (system 2)
 "Post-concussive syndrome":"GAP: 'concussion' appears ZERO times corpus-wide against 28 head-injury uses; the return-to-work and return-to-sport advice has nowhere to live",
 "Concussion":"GAP: zero hits corpus-wide despite 28 head-injury uses",
 "Cerebellar infarction":"GAP: posterior circulation stroke presenting as vertigo, the classic miss; no cerebellar stroke content",
 "Central Cord Syndrome":"GAP: commonest incomplete cord syndrome; Brown-Sequard owns an entry, this has no mention",
 "Posterior Cord Syndrome":"GAP: completes the incomplete-cord-syndrome set the corpus half-covers",
 "Neurologically Determined Death":"GAP: brain-death determination and organ donation; compounds the death-certification gap queued as P5-D4",
 # endocrine and metabolic - found ONLY because a zero-gap system was
 # disbelieved and its absent list grepped by hand afterwards
 "Alcoholic Ketoacidosis":"GAP: zero hits; a raised-anion-gap differential an intern must separate from DKA",
 "Hypophosphatemia":"GAP: zero hits. The corpus teaches hyper/hypo natraemia, kalaemia, calcaemia and hypomagnesaemia - phosphate is the one electrolyte with no entry at all, and refeeding syndrome (2 passing mentions, no entry) is where an intern meets it",
 "Hyperphosphatemia":"GAP: zero hits; see Hypophosphatemia - completes the missing electrolyte",
 "Hypermagnesemia":"GAP: zero hits while hypomagnesaemia has 13; the other half of a pair the corpus half-teaches",
 # genitourinary
 "Premature Ejaculation":"GAP: zero hits; a GP-level sexual health presentation, and erectile dysfunction IS covered",
 "Epispadias":"GAP: zero hits while hypospadias is covered; the other half of a pair",
 # dermatology
 "Paronychia":"GAP: zero hits; a common GP/ED presentation with a drainage decision",
 "Diaper Rash":"GAP: zero hits for nappy or diaper rash; compounds the queued nystatin gap (P5-C7)",
 "Felon":"GAP: zero hits; closed-space pulp infection needing urgent drainage",
 # toxicology and trauma
 "Heat Stroke":"GAP: zero hits for heat stroke or heatstroke; core Australian ED presentation",
 "Heat Exhaustion":"GAP: zero hits; the distinction from heat stroke is the clinical decision",
 "TCA Overdose":"GAP: zero hits; sodium bicarbonate for QRS widening is classic intern-level toxicology",
 "Facial Fractures":"GAP: zero hits, and zero for Le Fort; ED assessment of facial trauma",
 "Benzodiazepine overdose":"GAP - thin: only one flumazenil mention, no entry",
 # psychiatry
 "Adjustment Disorder":"GAP: zero hits; one of the commonest psychiatric diagnoses in general hospital work",
 "Gender Dysphoria":"GAP: zero hits; respectful and competent care is intern-level",
 "Delusional Disorder":"GAP: zero hits; a named differential within the psychotic disorders the corpus does teach",
 "Parasomnias":"GAP: zero hits for parasomnia, sleepwalking, somnambulism or night terrors; paediatric sleep is GP-level",
 "Night Terrors":"GAP: zero hits; see Parasomnias",
 "Sleepwalking":"GAP: zero hits; see Parasomnias",
 # gastroenterology
 "Gilbert's Syndrome":"GAP: zero hits; the commonest benign cause of an isolated raised bilirubin an intern must recognise",
 "Pancreatic pseudocyst":"GAP: zero hits; a named complication of the pancreatitis the corpus teaches",
 "Intra-abdominal abscess":"GAP: zero hits; a named complication of appendicitis and diverticulitis, both taught",
 # musculoskeletal
 "Hallux valgus":"GAP: zero hits for hallux valgus or bunion",
 "Bunions":"GAP: zero hits; see Hallux valgus",
 "Mallet Finger":"GAP: zero hits; a splinting decision an intern makes in ED",
 # Gaps that were HIDDEN by generated-acronym collisions until the
 # corroboration check was added - found by auditing the flagged pile,
 # not by any absence count
 "Anterior Cord Syndrome":"GAP: zero hits, hidden behind the ACS collision (acute coronary syndrome, 40 uses). Completes the incomplete-cord-syndrome set with central and posterior, both already queued",
 "Orbital Floor Fracture (Blow-out fracture)":"GAP: zero hits, hidden behind the OFF collision (the ordinary English word, 85 uses). Blow-out fracture is intern-level ED assessment and pairs with the queued facial-fracture gap",
 # musculoskeletal eponyms - hand-verified in the targeted eponym pass
 "Bennett's fracture":"GAP: zero hits; intra-articular base-of-thumb-metacarpal fracture, and the corpus owns entries for Colles, Smith, Barton, Monteggia, Galeazzi and Boxer",
 "Rolando fracture":"GAP: zero hits; the comminuted counterpart of Bennett, same asymmetry",
 "Lisfranc fracture":"GAP: zero hits; midfoot injury classically missed on plain films, and the corpus owns a metatarsal fracture entry",
 "Gamekeeper's thumb":"GAP: zero hits for gamekeeper or skier's thumb",
 "Stener lesion":"GAP: zero hits; the finding that makes a gamekeeper's thumb surgical",
 "Hill-Sachs lesion":"GAP: zero hits, while Bankart is named in the shoulder dislocation content - half of a pair",
 "Jefferson fracture":"GAP: zero hits; C1 burst fracture",
 "Hangman fracture":"GAP: zero hits; C2 traumatic spondylolisthesis",
 # ENT and ophthalmology
 "Retropharyngeal abscess":"GAP: zero hits; paediatric airway emergency, and the corpus teaches peritonsillar abscess",
 "Keratoconus":"GAP: zero hits; commonest corneal ectasia, presents in young adults",
 # infectious disease
 "Herpetic Whitlow":"GAP: zero hits; occupational hand infection with a do-not-incise rule",
 "Lymphangitis":"GAP: zero hits; the corpus teaches cellulitis but not the ascending-streaking sign",
 # respiratory
 "Solitary pulmonary nodule":"GAP: zero hits; the incidental-finding pathway an intern is asked about",
 # renal - independently rediscovers a gap the earlier corpus-first pass queued as P5-A1
 "Posterior Urethral Valves":"GAP: zero hits - INDEPENDENTLY CONFIRMS the P5-A1 finding from the earlier corpus-first pass, reached by a different method",
}

SYN = {
 "Gastroesophageal reflux disease":"COVERED: GORD owns an entry (28 uses); US/AU spelling",
 "GERD":"COVERED: GORD owns an entry",
 "Cholelithiasis":"COVERED-SYNONYM: gallstones, 28 uses",
 "Upper Gastrointestinal Bleeding":"COVERED-SYNONYM: upper GI bleed / haematemesis, 21 uses",
 "Lower Gastrointestinal Bleeding":"COVERED-SYNONYM: GI bleed content, 20 uses",
 "Helicobacter pylori":"COVERED-SYNONYM: H. pylori, 24 uses (abbreviated genus)",
 "Acute Liver Failure":"COVERED-SYNONYM: fulminant hepatic failure, 3 uses",
 "Mallory-Weiss Syndrome":"COVERED-SYNONYM: Mallory-Weiss tear, 5 uses",
 "Boerhaave's syndrome":"COVERED-SYNONYM: oesophageal perforation",
 "Dental cavities":"COVERED-SYNONYM: dental caries",
 "Fistula-in-ano":"COVERED-SYNONYM: anal fistula, 5 uses",
 "Skin Abscess":"COVERED-SYNONYM: abscess incision and drainage, 6 uses",
 "Dermatophytoses":"COVERED: the tinea entries own this",
 "Scabies":"COVERED: owns an entry",
 "Intrauterine growth restriction":"COVERED-SYNONYM: IUGR / small for gestational age, 15 uses",
 "Spontaneous abortion":"COVERED-SYNONYM: miscarriage, 55 uses",
 "Threatened abortion":"COVERED-SYNONYM: miscarriage content",
 "Recurrent pregnancy loss":"COVERED-SYNONYM: recurrent miscarriage",
 "Umbilical Cord Prolapse":"COVERED-SYNONYM: cord prolapse, 4 uses",
 "Perineal Lacerations":"COVERED-SYNONYM: perineal tear, 4 uses",
 "Rhesus (Rh) Alloimmunization":"COVERED: anti-D and alloimmunisation, 93 uses",
 "Erythroblastosis fetalis":"COVERED-SYNONYM: haemolytic disease of the newborn / anti-D content",
 "Hemolytic Disease of the Newborn / Rhesus (Rh) Incompatibility":"COVERED: anti-D content",
 "Gestational Hypertension":"COVERED: hypertension in pregnancy content",
 "Bipolar I Disorder":"COVERED-SYNONYM: bipolar I/II distinction present, 7 uses",
 "Bipolar II Disorder":"COVERED-SYNONYM: as above",
 "Insomnia Disorder":"COVERED-SYNONYM: insomnia, 12 uses",
 "Alcohol dependence":"COVERED-SYNONYM: alcohol use disorder owns an entry",
 "Stimulant Use Disorder":"COVERED-SYNONYM: substance use disorder content",
 "Cannabis Use Disorder":"COVERED-SYNONYM: substance use disorder content",
 "Somatization Disorder":"COVERED-SYNONYM: somatic symptom disorder",
 "Somnambulism":"GAP: zero hits; see Parasomnias",
 "Acetaminophen Overdose":"COVERED-SYNONYM: paracetamol overdose (AU generic name)",
 "Salicylate Overdose":"COVERED-SYNONYM: salicylate content, 8 uses",
 "Mild Traumatic Brain Injury":"COVERED-SYNONYM: head injury content - but see the Concussion gap",
 "Hyaline Membrane Disease":"COVERED-SYNONYM: respiratory distress syndrome / surfactant",
 "Transient Tachypnea of the Newborn (TTN)":"COVERED-SYNONYM: transient tachypnoea, thin",
 "Supracondylar Humerus Fracture":"COVERED-SYNONYM: supracondylar fracture, 4 uses",
 "Radial Head Subluxation (Nursemaid's Elbow)":"COVERED-SYNONYM: pulled elbow, thin",
 "Necrotizing Enterocolitis":"COVERED-SYNONYM: necrotising enterocolitis (AU spelling)",
 "Femoral neck fracture":"COVERED-SYNONYM: neck of femur / NOF fracture, 29 uses",
 "Clavicle fracture":"COVERED-SYNONYM: clavicle content, 25 uses",
 "Anterior cruciate ligament tear":"COVERED-SYNONYM: ACL, 20 uses",
 "Cruciate ligament tear":"COVERED-SYNONYM: ACL content",
 "Meniscal tear":"COVERED-SYNONYM: meniscus content",
 "Achilles tendon rupture":"COVERED-SYNONYM: Achilles content",
 "Rotator cuff disease":"COVERED-SYNONYM: rotator cuff, 10 uses",
 "Lumbar Spinal Stenosis":"COVERED-SYNONYM: spinal stenosis",
 "Ganglion Cyst":"COVERED-SYNONYM: ganglion, 10 uses",
 "Legg-Calve-Perthes disease":"COVERED-SYNONYM: Perthes",
 "Coxa plana":"COVERED-SYNONYM: Perthes",
 "Greenstick fracture":"COVERED-SYNONYM: greenstick/torus/buckle content",
 "Torus fracture":"COVERED-SYNONYM: greenstick/torus/buckle content",
 "Necrotizing Fasciitis":"COVERED-SYNONYM: necrotising fasciitis (AU spelling), 14 uses",
 "Human papillomavirus":"COVERED-SYNONYM: HPV, 38 uses",
 "Trichomoniasis":"COVERED-SYNONYM: trichomonas, 5 uses",
 "Typhoid fever":"COVERED-SYNONYM: typhoid, 12 uses",
 "Hydatid disease":"COVERED-SYNONYM: hydatid, 3 uses",
 "Hydatid cyst":"COVERED-SYNONYM: hydatid",
 "Preseptal cellulitis":"COVERED-SYNONYM: periorbital cellulitis",
 "Foreign Body Aspiration":"COVERED-SYNONYM: foreign body content, 27 uses",
 "Nasal Foreign Body":"COVERED-SYNONYM: foreign body content",
 "Foreign body in ear":"COVERED-SYNONYM: foreign body content",
 "Acute Exacerbation of COPD":"COVERED-SYNONYM: COPD exacerbation, 10 uses",
 "Ureteral Stones":"COVERED-SYNONYM: ureteric stone / renal colic",
 "Membranous glomerulopathy":"COVERED-SYNONYM: membranous nephropathy, thin",
 "Compartment syndrome":"COVERED: 15 uses",
 # --- Hand-resolution of the 14 acronym rows (survivors + suspect rejections).
 # THREE FALSE SURVIVORS: the acronym meant something else entirely.
 "Congenital bleeding disorders":"UMBRELLA - FALSE SURVIVOR: the corpus's CBD is corticobasal degeneration (04_Neurology:442) and common bile duct (03_Gastrointestinal). Corroborated only on the generic word 'disorders'. The concept is covered by its members - haemophilia A/B and vWD in 10_07",
 "Autosomal recessive polycystic kidney disease":"ABSENT - FALSE SURVIVOR: 07_Renal:170 teaches autosomal DOMINANT PKD; the recessive form has no mention. Out of scope at intern level (paediatric nephrology)",
 "Vaginal Intraepithelial Neoplasia":"ABSENT - FALSE SURVIVOR: VIN in this corpus is VULVAL intraepithelial neoplasia (17_07:81). VaIN has no mention - and a grep for 'VaIN' matches only 'de QuerVAIN's'. Out of scope at intern level",
 # THREE FALSE REJECTIONS: covered, but the corpus uses the acronym and never
 # spells the term out, so no corroborating word could ever co-occur.
 "Staphylococcal Scalded Skin Syndrome":"COVERED - FALSE REJECTION: owns an entry, '## Staph scalded skin syndrome (SSSS)' 09_01:116. Rejected because the corpus writes 'Staph', never 'Staphylococcal'",
 "Focal segmental glomerulosclerosis":"COVERED - FALSE REJECTION: 07_Renal:195 and 15_10:51. Rejected because the corpus only ever writes FSGS, never 'glomerulosclerosis'",
 "Cervical intraepithelial neoplasia":"COVERED - FALSE REJECTION: 17_09:30-31 teaches CIN I/II/III with the LLETZ referral rule. Rejected because the corpus only ever writes CIN",
 # CONFIRMED CORRECT
 "Acute Generalized Exanthematous Pustulosis":"COVERED: 09_01:75 names it with its recognisable features and states explicitly that it is not detailed further - a deliberate scope decision, not an omission",
 "Heart Failure with Preserved Ejection Fraction":"COVERED: 01_Cardiovascular:938 classifies HF by ejection fraction; HFpEF/HFrEF named at :1457",
 "Hereditary Non-Polyposis Colon Cancer":"COVERED: 17_09:87 'Hereditary non-polyposis colorectal carcinoma (HNPCC/Lynch syndrome)', plus 03_GI and 17_10",
 "Monoclonal Gammopathy of Unknown Significance":"COVERED: 10_02:84 and 04_Neurology:1383. The list says 'Unknown', the corpus says 'undetermined' - which is why the name match failed",
 "Nephrogenic Diabetes Insipidus":"COVERED: 06_Metabolic:697, a row in the diabetes insipidus differential table",
 "Vulvar Intraepithelial Neoplasia":"COVERED: owns an entry, 17_07:81 '## Vulval intraepithelial neoplasia (VIN)'. US 'vulvar' vs AU 'vulval' is why the name match failed",
 "Systemic Inflammatory Response Syndrome":"ABSENT - CORRECTLY: the corpus's two SIRS hits are the aged-care Serious Incident Response Scheme. The syndrome is genuinely absent, and defensibly so - qSOFA is taught at 08_09:155 and Sepsis-3 has superseded the SIRS criteria",
 "Contrast-Induced Nephropathy":"ABSENT - CORRECTLY: zero hits for contrast nephropathy in any wording",
 "Calcineurin inhibitor nephropathy":"ABSENT - CORRECTLY: calcineurin inhibitors appear in 07_Renal:141 immunosuppression, but not their nephrotoxicity as a named condition. Out of scope at intern level",
 "Gestational Diabetes Mellitus":"COVERED-SYNONYM: taught as '### Diabetes in pregnancy' 16_01-05:430, with the 28-week 75g OGTT criteria; no matcher reaches this rename",
 # WITHDRAWN GAPS. Both were queued as build items and both were wrong: the
 # corpus writes "Baker cyst" without the possessive, and my tokeniser split
 # "Baker's" into ["baker","s"] and then demanded the apostrophe. Recorded as
 # withdrawn rather than deleted - a false gap that reached the tracker is
 # worth keeping visible.
 "Baker's cyst":"COVERED - GAP WITHDRAWN: 11_05_Ortho_-_Knee_and_Ankle 'Baker cyst' (l.27), under the Bursitis & cysts of the knee entry",
 "Popliteal cyst":"COVERED - GAP WITHDRAWN: same entry as Baker cyst, its other name",
 "Boxer's fracture":"COVERED: owns an entry, 11_03_Ortho_-_Hand_and_Foot '### Boxer fracture' (l.57)",
 "Acromioclavicular joint pathology":"COVERED: owns an entry, 11_02_Ortho_-_Upper_Limb '### Acromioclavicular joint injury' (l.48)",
 "Achilles tendon rupture":"COVERED: 11_05_Ortho_-_Knee_and_Ankle '## Achilles tendon' (l.96) with the Simmonds-Thompson calf-squeeze test",
 # cardiovascular and neurology synonyms verified in the per-system passes
 "First Degree AV Block":"COVERED-SYNONYM: 01_Cardiovascular 'first degree heart block' (l.537)",
 "Second Degree AV Block":"COVERED-SYNONYM: 'Mobitz I, Wenckebach' / 'Mobitz II' (l.492-3)",
 "Third Degree AV Block":"COVERED-SYNONYM: complete heart block",
 "Rheumatic valve disease":"COVERED-SYNONYM: rheumatic heart disease, 14 uses",
 "Chronic limb threatening ischemia (CLTI)":"COVERED-SYNONYM: critical limb ischaemia",
 "Vascular claudication":"COVERED-SYNONYM: claudication under PAD",
 "Venous claudication":"COVERED-SYNONYM: claudication under PAD",
 "Acute Decompensated Heart Failure":"COVERED-SYNONYM: acute heart failure content",
 "Dementia with Lewy bodies":"COVERED-SYNONYM: Lewy body dementia (word order)",
 "Lambert-Eaton myasthenic syndrome":"COVERED-SYNONYM: Lambert-Eaton syndrome; the list adds a qualifier the corpus omits",
 "Radial nerve palsy":"COVERED-SYNONYM: radial nerve injury",
 "Sciatic nerve palsy":"COVERED-SYNONYM: sciatic nerve injury",
 "Peroneal nerve injury":"COVERED-SYNONYM: peroneal nerve content",
 "Lumbar radiculopathy":"COVERED-SYNONYM: L5/S1 radiculopathy, sciatica entry",
 "Hemineglect":"COVERED-SYNONYM: neglect / inattention in stroke content",
 "Intracranial Aneurysms":"COVERED: taught within the subarachnoid haemorrhage entry",
 "Chronic non-cancer pain":"COVERED-SYNONYM: chronic pain entry",
 "Herniation Syndromes":"COVERED-SYNONYM: herniation / coning, 26 uses",
 "Subfalcine Herniation":"COVERED-SYNONYM: herniation content",
 "Tonsillar Herniation":"COVERED-SYNONYM: herniation content",
 "Lateral Tentorial Herniation":"COVERED-SYNONYM: herniation content",
 "Upward Herniation":"COVERED-SYNONYM: herniation content",
 "Cerebrospinal Fluid Fistulas":"COVERED-SYNONYM: CSF leak / otorrhoea / rhinorrhoea",
 "Reflex sympathetic dystrophy":"COVERED-SYNONYM: complex regional pain syndrome",
}
UMBRELLA = {"Cardiac Infections","Cardiovascular diseases","Cardiovascular toxicity","CVD events",
 "Hemodynamic shock","Vascular occlusion","Venous Disease","Venous hypertension","Venous stasis edema",
 "Neuromuscular disease","Neurospinal disease","Vestibular Disease","Cerebrovascular events",
 "Prion Disease","Leukodystrophies","Collagen disorders","Musculoskeletal disorders","Limb anomalies","Anorectal disease",
 "Gastrointestinal Infections","Infectious Colitis","Herpes infection","Adverse drug reaction",
 "Immunologic reactions","Idiosyncratic reactions","Antibiotic allergies","Neurotrauma",
 "Renal Trauma","Fractures of the Spine","Pathologic fracture","Neurocognitive disorders",
 "Phobic disorders","Paraphilic Disorders","Renal anomalies","Kidney cysts","Congenital stenosis",
 "Lower Urinary Tract Dysfunction","Hypoventilation Syndromes","Sleep-Disordered Breathing",
 "Hypercoagulable Disorders","Metastatic Tumours","Cerebral Tumour","Lung malignancy",
 "Pulmonary Neoplasm","Cardiac tumour","Dental disease","Bladder and Bowel Dysfunction",
 "Familial Colon Cancer Syndromes","Subcutaneous Fungal Infections","Bacteroides infection",
 "Pseudomonas infection","Klebsiella infection","Graft infection","Herpes Zoster Virus"}
RULE = ("OUT OF SCOPE at intern/RMO level (classified by rule, not individually verified - "
        "named fracture patterns and eponyms, tumour subtypes, congenital dysmorphology, "
        "non-endemic tropical infection, single-gene disorders)")

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "checklist_external.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    n = {"GAP":0,"COVERED":0,"UMBRELLA":0,"RULE":0}
    for r in rows:
        v, c = r["verdict"], r["condition"]
        if v == "OWNS ENTRY": r["scope_judgement"] = "covered - owns an entry"
        elif v == "IN A TAUGHT SECTION": r["scope_judgement"] = "covered - named inside a teaching entry"
        elif v == "MENTIONED": r["scope_judgement"] = "named in prose only - not individually verified"
        elif v == "ABSENT":
            j = GAP.get(c) or SYN.get(c)
            if j: r["scope_judgement"] = j; n["GAP" if j.startswith("GAP") else "COVERED"] += 1
            elif c in UMBRELLA: r["scope_judgement"] = "UMBRELLA LABEL - not a condition an entry could own"; n["UMBRELLA"] += 1
            else: r["scope_judgement"] = RULE; n["RULE"] += 1
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(n)

if __name__ == "__main__":
    main()
