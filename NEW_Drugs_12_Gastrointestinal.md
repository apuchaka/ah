---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 12 Gastrointestinal drugs
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Gastrointestinal (AMH section 12)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.**

---

## 0.1 Drugs for Dyspepsia, Reflux and Peptic Ulcers

### 0.1.1 Proton Pump Inhibitors
*(covers build-list classes: Proton Pump Inhibitors; Proton pump inhibitors — the same class listed twice with different capitalisation)*
- **Mechanism:** irreversibly inhibit the gastric parietal cell **H⁺/K⁺-ATPase (the proton pump)** — the final common step of acid secretion. Because inhibition is irreversible, the effect outlasts the plasma level and takes days of dosing to reach full effect.
- **Key agents:** **esomeprazole, omeprazole, pantoprazole, rabeprazole, lansoprazole**.
- **Indications:** **gastro-oesophageal reflux disease and oesophagitis**; **peptic ulcer disease and *H. pylori* eradication**; **NSAID ulcer prophylaxis in at-risk patients**; **upper gastrointestinal bleeding**; Barrett oesophagus; Zollinger-Ellison syndrome; and eosinophilic oesophagitis.
- **Practical:** take **30–60 minutes before a meal** — the pump must be activated by food for the drug to bind it. Taking a PPI at bedtime on an empty stomach is much less effective, and is a common reason for apparent failure.

> [!danger] **PPIs ARE OVER-PRESCRIBED AND UNDER-REVIEWED. Deprescribing is an active clinical task, and Australia has its own guidance for it.**
> Sources describe an **Australian deprescribing guide (NSW TAG)** and Australian guidance on **why, when and how** to deprescribe, and note that guidelines **advocate periodic review with strategies including dose reduction, on-demand or intermittent use, and switching to an H₂ antagonist.**
> **Harms of long-term use reported in the sources:** **fractures** (with use beyond about a year), **kidney disease**, ***Clostridioides difficile* and other enteric infections**, **pneumonia**, **hypomagnesaemia** (described as occurring after at least 3 months and usually after a year), and **vitamin B₁₂ deficiency** (with use beyond about 2 years). Also iron and calcium malabsorption, and a signal for gastric atrophy and precancerous mucosal change with prolonged therapy.
> **Rebound acid hypersecretion on stopping is real** and makes patients believe they still need the drug — **taper or step down rather than stopping abruptly**, and warn them.
> **Every long-term PPI needs a documented indication.** Many patients started one during an admission for stress ulcer prophylaxis and are still on it years later.

- **Interactions:** **clopidogrel** — omeprazole and esomeprazole inhibit **CYP2C19**, reducing clopidogrel activation; **pantoprazole is generally preferred** when a PPI is needed with clopidogrel. Reduced absorption of **ketoconazole, itraconazole, atazanavir, rilpivirine, iron and calcium carbonate**; raised **methotrexate** levels.
- ***H. pylori* eradication:** a PPI with **two or three antimicrobials** for a defined course; **check eradication after treatment** where indicated, and be aware that **clarithromycin resistance is rising**, which drives the move to quadruple and bismuth-based regimens. See `NEW_Investigations_Gastroenterology.md` and [[03_Gastrointestinal]].

> [!danger] **Do not treat dyspepsia with acid suppression without considering the ALARM features:** **dysphagia, odynophagia, unintentional weight loss, vomiting, gastrointestinal bleeding or anaemia, a palpable mass, persistent symptoms in a patient over 50 with new onset, or a family history of upper GI cancer.** These require **endoscopy**, not a trial of a PPI — and **acid suppression can mask a gastric cancer** while it progresses.

### 0.1.2 H₂ Antagonists
- **Key agents:** **famotidine, nizatidine** (ranitidine was withdrawn worldwide over NDMA contamination; cimetidine is largely obsolete).
- **Mechanism:** competitive antagonism at the parietal cell **histamine H₂ receptor**.
- **Role:** less potent than PPIs, but **faster in onset** and useful for **on-demand symptom relief**, as a **step-down from a PPI when deprescribing**, and for **nocturnal acid breakthrough**. Tolerance develops within weeks of regular use.
- **Adverse effects:** generally well tolerated; **confusion in the elderly and in renal impairment** (dose reduction needed); **cimetidine is a significant CYP inhibitor and antiandrogen** (gynaecomastia, impotence) — which is why it is not used.

### 0.1.3 Antacids
- **Key agents:** **aluminium hydroxide, magnesium hydroxide/trisilicate, calcium carbonate**, and combinations; **alginate** preparations (Gaviscon-type), which form a physical raft on the gastric contents.
- **Role:** **rapid, short-lived symptom relief** — genuinely useful as needed and in pregnancy, where alginates and calcium-based antacids are first-line for reflux.
- **Adverse effects:** **magnesium causes diarrhoea, aluminium causes constipation** (hence the combinations); **calcium carbonate causes acid rebound and, in excess, milk-alkali syndrome**; sodium content matters in heart failure and hypertension; aluminium accumulates in renal failure.
- **Interactions:** **antacids bind and reduce absorption of many drugs — tetracyclines, quinolones, iron, thyroxine, bisphosphonates, integrase inhibitors and others. Separate doses by at least 2 hours.** This is one of the commonest silent causes of treatment failure.

### 0.1.4 Other Drugs for Ulcers
- **Sucralfate** — forms a protective barrier over ulcer bases; needs an acid environment (so do not give with a PPI at the same time), and **binds other drugs** — separate doses.
- **Misoprostol** — a prostaglandin analogue for NSAID ulcer prophylaxis; largely displaced by PPIs because it causes **diarrhoea and abdominal cramps**. **It is an abortifacient and uterotonic and is absolutely contraindicated in pregnancy** — and is used deliberately for that purpose in obstetrics (see `NEW_Drugs_16_Obstetric_and_Gynaecological.md` 0.10.1).
- **Bismuth compounds** — mucosal protection and anti-*H. pylori* activity; blacken the tongue and stool (**do not confuse with melaena**).
- **Potassium-competitive acid blockers (vonoprazan)** — a newer class with faster, more sustained acid suppression, used in *H. pylori* regimens where available.

## 0.2 Antiemetics

> [!info] **Choose the antiemetic by the MECHANISM of the vomiting, not by habit.** Chemotherapy and postoperative nausea → **5-HT₃ antagonist** ± dexamethasone ± NK₁ antagonist. Gastric stasis and reflux-associated nausea → **prokinetic dopamine antagonist**. Vestibular and motion-related → **antihistamine or anticholinergic**. Raised intracranial pressure → **dexamethasone**. Drug- and metabolically-driven (opioids, uraemia, hypercalcaemia) → **dopamine antagonist**. **And treat the cause** — nausea is a symptom, and bowel obstruction, raised ICP, pregnancy, DKA, hypercalcaemia and drug toxicity all present this way.

### 0.2.1 5-HT₃ Antagonists
- **Key agents:** **ondansetron, granisetron, palonosetron, tropisetron**.
- **Mechanism:** block **serotonin 5-HT₃** receptors on vagal afferents in the gut and in the chemoreceptor trigger zone.
- **Indications:** **chemotherapy- and radiotherapy-induced nausea and vomiting**, **postoperative nausea and vomiting**, and widely (often as first-line) in acute gastroenteritis and undifferentiated vomiting in emergency departments.
- **Adverse effects:** **CONSTIPATION** (very common and frequently the cause of the abdominal pain the patient develops next), headache, flushing; **QT PROLONGATION** — sources note ondansetron should be **avoided where there are risk factors for QT prolongation or in combination with other serotonergic medicines**; and, rarely, extrapyramidal reactions and serotonin syndrome.
- **Pregnancy:** sources note **a potential association between ondansetron and cleft lip/palate**, and advise it should be **started in secondary care or after obstetric discussion** — so it is not the first choice in early pregnancy.

### 0.2.2 Dopamine Antagonists (Antiemetic)
- **Key agents:** **metoclopramide** (also prokinetic), **domperidone**, **prochlorperazine**, **droperidol**, **haloperidol** (widely used in palliative care), and the phenothiazines.
- **Mechanism:** **D₂ antagonism** at the chemoreceptor trigger zone; metoclopramide and domperidone additionally act peripherally on the gut to **increase gastric emptying**.

> [!danger] **METOCLOPRAMIDE: EXTRAPYRAMIDAL REACTIONS AND TARDIVE DYSKINESIA, AND THE SHORT-COURSE RESTRICTION.**
> Sources state that **metoclopramide should only be prescribed for short-term use (up to about 5 days)**, and **should not be used beyond 12 weeks because of tardive dyskinesia, which can be irreversible.** **Acute dystonic reactions — oculogyric crisis, torticollis, trismus — are frightening, are often misdiagnosed as a psychiatric or neurological event, and are commonest in YOUNG WOMEN AND THE ELDERLY.** Treatment is **benztropine or an anticholinergic**, and it resolves quickly. **Prochlorperazine carries the same risk.**
> **Avoid dopamine antagonists in Parkinson disease** — they worsen it. **Domperidone does not cross the blood-brain barrier appreciably** and is therefore the prokinetic of choice in Parkinson disease, **but it prolongs the QT** and has its own cardiac restrictions.
> **Metoclopramide is considered safe in pregnancy** and is used, but sources place it as **second-line because of the extrapyramidal and tardive dyskinesia risk**.

- **Other adverse effects:** sedation, hyperprolactinaemia (galactorrhoea, gynaecomastia, amenorrhoea — see `NEW_Drugs_10_Endocrine.md` 0.5.3), postural hypotension, and neuroleptic malignant syndrome.
- **Contraindication:** **do not give a prokinetic in suspected mechanical bowel obstruction or perforation.**

### 0.2.3 Substance P (NK₁) Antagonists
- **Key agents:** **aprepitant** and its intravenous prodrug **fosaprepitant**; netupitant, rolapitant.
- **Mechanism:** block the **neurokinin-1 receptor** for substance P centrally.
- **Role:** **highly emetogenic chemotherapy**, in a triple regimen with a **5-HT₃ antagonist and dexamethasone** — particularly effective for **DELAYED** chemotherapy-induced nausea, which the 5-HT₃ antagonists control poorly. Also used in postoperative nausea prophylaxis.
- **Adverse effects:** fatigue, hiccups, constipation; **CYP3A4 interactions** — it affects dexamethasone, some chemotherapy agents, warfarin and **hormonal contraceptives (additional contraception is needed)**.

### 0.2.4 Other Drugs for Nausea and Vomiting
- **Antihistamines and anticholinergics — promethazine, cyclizine, hyoscine hydrobromide.** For **motion sickness and vestibular causes**, where they are genuinely first-line. Sedating and anticholinergic; **avoid in the elderly** (delirium, falls, retention).
- **Corticosteroids — dexamethasone.** Effective in chemotherapy and postoperative nausea, and specifically for nausea from **raised intracranial pressure** and malignant bowel obstruction.
- **Benzodiazepines** — for **anticipatory** nausea before chemotherapy.
- **Cannabinoids (nabilone)** — refractory chemotherapy-induced nausea.
- **Pyridoxine and doxylamine** — the evidence-based first-line for **nausea and vomiting of pregnancy** in many guidelines, with ginger and non-drug measures. **Hyperemesis gravidarum requires assessment for dehydration, ketosis, electrolyte disturbance and thiamine deficiency** — and **thiamine must be given before glucose-containing fluids** (see `NEW_Drugs_07_Blood_and_Electrolytes.md` 0.4.2).
- **Non-drug:** hydration, small frequent meals, treating pain and constipation, and removing the offending drug.

## 0.3 Drugs Affecting Gastrointestinal Motility

- **Prokinetics:** **metoclopramide** and **domperidone** (D₂ antagonism plus cholinergic facilitation); **erythromycin** (a **motilin receptor agonist** — used deliberately at low dose for gastroparesis and before endoscopy in upper GI bleeding to clear the stomach); prucalopride (a 5-HT₄ agonist for chronic constipation).
- **Indications:** **gastroparesis** (diabetic, post-surgical, idiopathic), functional dyspepsia with delayed emptying, feed intolerance in critical illness, and to aid post-pyloric feeding tube placement.
- **Antispasmodics:** **hyoscine butylbromide** (Buscopan — poorly absorbed orally, useful parenterally for colic), **mebeverine**, **peppermint oil** — for **irritable bowel syndrome** and colicky pain. Peppermint oil has reasonable evidence in IBS and few adverse effects.
- **Antimotility agents:** see 0.4.
- **Cautions:** the **tardive dyskinesia and duration limits** on metoclopramide (0.2.2) apply here too and are the main reason long-term prokinetic therapy is difficult; **erythromycin causes tachyphylaxis within weeks** and carries QT and interaction risks.

> [!danger] **Never give a prokinetic or a laxative when mechanical obstruction or perforation is possible.** In malignant bowel obstruction, management is specialist and often uses **hyoscine butylbromide, octreotide and dexamethasone** rather than prokinetics.

## 0.4 Antidiarrhoeals

### 0.4.1 Opioid Antidiarrhoeals
- **Key agents:** **loperamide**, **diphenoxylate with atropine**, codeine, and **opium tincture** in specialist settings.
- **Mechanism:** **µ-opioid receptor agonism in the myenteric plexus** → reduced propulsive motility and increased transit time, allowing more fluid absorption. **Loperamide does not appreciably cross the blood-brain barrier at normal doses**, so it has no analgesic or euphoric effect.
- **Indications:** **symptomatic control of non-infective diarrhoea** — IBS-D, short bowel and high-output stoma, chemotherapy-induced diarrhoea, and faecal incontinence.

> [!danger] **DO NOT GIVE ANTIMOTILITY AGENTS IN BLOODY, FEBRILE OR SUSPECTED INVASIVE DIARRHOEA, OR IN SUSPECTED *C. DIFFICILE*.**
> Slowing transit prolongs exposure to toxin and organism and is associated with **toxic megacolon** and, in Shiga-toxin-producing *E. coli*, an increased risk of **haemolytic uraemic syndrome**. **They are also avoided in acute severe ulcerative colitis.** **In children, antimotility agents are generally avoided altogether** — oral rehydration is the treatment.

> [!danger] **LOPERAMIDE CARDIAC TOXICITY IN OVERDOSE — a genuinely modern problem.**
> Sources describe an **FDA statement (2016) on heart effects and death with high doses**, note the usual recommended maximum is around **8 mg/day**, and report cardiac toxicity especially with chronic ingestion of **more than 100 mg/day**. The mechanism is **blockade of cardiac hERG (Kv11.1) potassium channels causing QT prolongation, and Nav1.5 sodium channels causing QRS widening**, producing **torsades de pointes, ventricular dysrhythmias, cardiac arrest and death.** **It is misused at very high doses to self-treat opioid withdrawal or to obtain euphoria** — so **ask about loperamide in any unexplained wide-complex or long-QT arrhythmia in a young person**, and recognise that it is cheap and available without prescription.
- **Diphenoxylate with atropine** — the atropine is included deliberately to deter misuse; **overdose in children causes opioid and anticholinergic toxicity and has been fatal.** Store safely.

### 0.4.2 Other Drugs for Diarrhoea
- **Oral rehydration solution — the single most important treatment**, and consistently under-used (see `NEW_Drugs_07_Blood_and_Electrolytes.md` 0.3.5).
- **Octreotide** — high-output stomas and fistulas, carcinoid and chemotherapy-related diarrhoea.
- **Bile acid sequestrants (colestyramine, colesevelam)** — for **bile acid diarrhoea**, which is common, easily missed, and dramatically responsive: think of it after **cholecystectomy, terminal ileal resection or Crohn disease**, and in "IBS-D" that has never been properly explained. See 0.8.
- **Racecadotril** (an enkephalinase inhibitor, antisecretory rather than antimotility) and **probiotics** (modest evidence in antibiotic-associated diarrhoea).
- **Treat the cause:** stop the offending drug (**antibiotics, metformin, colchicine, magnesium, PPIs, laxatives**), test for **infection including *C. difficile***, and consider **coeliac disease, IBD, malabsorption, hyperthyroidism, and overflow from constipation** — the last being a very common trap in the elderly and in children, where treating the "diarrhoea" makes it worse.

## 0.5 Laxatives

> [!info] **Match the laxative to the problem, and start with the non-drug measures that actually work:** fluid, fibre, activity, toileting routine and privacy, and reviewing constipating drugs (**opioids, anticholinergics, iron, calcium channel blockers, ondansetron, antipsychotics, diuretics**).

### 0.5.1 Osmotic Laxatives
- **Key agents:** **macrogol (polyethylene glycol)**, **lactulose**, **sorbitol**, **magnesium salts**, **phosphate enemas**.
- **Mechanism:** osmotically retain water in the bowel lumen, softening stool and increasing volume, which stimulates peristalsis.
- **Role:** **macrogol is generally first-line** for chronic constipation and faecal impaction in adults and children — it is effective, well tolerated and does not require an intact colonic response.
- **Adverse effects:** bloating and flatulence (**lactulose particularly**, as it is fermented by colonic bacteria); dehydration and electrolyte disturbance with large volumes; **magnesium accumulates in renal impairment**; **phosphate enemas can cause severe hyperphosphataemia, hypocalcaemia and acute kidney injury — avoid in renal impairment, in the elderly, and in bowel obstruction.**
- **Lactulose has a second, unrelated indication:** **hepatic encephalopathy**, where it reduces ammonia absorption — dosed to a target stool frequency.

### 0.5.2 Stimulant Laxatives
- **Key agents:** **senna**, **bisacodyl**, **sodium picosulfate**, **docusate with senna** combinations, glycerol suppositories.
- **Mechanism:** stimulate enteric nerves and colonic motility, and reduce water absorption.
- **Role:** **essential in opioid-induced constipation**, where a softener alone is inadequate because the problem is reduced motility. **Co-prescribe with every regular opioid** — this is one of the commonest omissions in ward prescribing (see `NEW_Drugs_03_Analgesics.md` 0.4.4).
- **Adverse effects:** **cramping and colic** (dose-related), electrolyte disturbance with prolonged use, and melanosis coli with senna (benign and reversible). **The old teaching that stimulant laxatives cause a permanently "atonic colon" is not well supported** — under-treatment of constipation causes more harm than long-term stimulant use.
- **Contraindication:** **suspected bowel obstruction.**

### 0.5.3 Stool Softeners
- **Key agents:** **docusate sodium**, and **liquid paraffin** (largely avoided).
- **Mechanism:** surfactants that allow water and fat to penetrate the stool.
- **Role:** **weak. The evidence for docusate as a single agent is poor**, and it is one of the most widely prescribed and least effective drugs on the ward — usually appearing where a stimulant or osmotic agent is what is needed. It has a place combined with a stimulant, and where straining must be avoided.
- **Liquid paraffin** — risk of **lipoid pneumonia if aspirated** (avoid in the elderly, dysphagic and bed-bound), anal seepage, and impaired fat-soluble vitamin absorption.

### 0.5.4 Other Laxatives
- **Bulk-forming agents — psyllium/ispaghula, sterculia, methylcellulose.** Increase stool bulk and water content. **Must be taken with adequate fluid — otherwise they cause obstruction**, and they are **inappropriate in opioid-induced constipation and in patients with poor fluid intake or slow transit**.
- **Peripherally acting µ-opioid receptor antagonists — methylnaltrexone, naloxegol, and oxycodone/naloxone combinations.** Block gut opioid receptors **without reversing analgesia** — genuinely useful in refractory opioid-induced constipation, particularly in palliative care.
- **Secretagogues — lubiprostone, linaclotide** — for chronic idiopathic constipation and IBS-C.
- **Prucalopride** — a selective 5-HT₄ agonist for chronic constipation refractory to laxatives.
- **Enemas and suppositories** — for faecal loading and impaction; **manual evacuation** is sometimes necessary.

> [!danger] **Do not ignore constipation as a symptom.** **New, persistent change in bowel habit in an adult over 50, with rectal bleeding, weight loss or anaemia, is colorectal cancer until excluded.** **Faecal impaction with overflow diarrhoea** is regularly misdiagnosed and mistreated with antidiarrhoeals. **Constipation in a patient with new back pain and neurological symptoms raises spinal cord compression or cauda equina.** And **severe constipation with vomiting and distension is obstruction until proven otherwise** — do not give a stimulant laxative.

## 0.6 Drugs for Inflammatory Bowel Diseases

### 0.6.1 5-Aminosalicylates
- **Key agents:** **mesalazine** (oral, and topical as suppositories and enemas), **sulfasalazine**, olsalazine, balsalazide.
- **Mechanism:** topical anti-inflammatory action on the colonic mucosa (multiple pathways including COX/LOX and NF-κB); the different formulations are designed to **release the drug at different points in the bowel**, which is why formulation choice matters.
- **Role:** **first-line for mild-to-moderate ULCERATIVE COLITIS**, for induction and maintenance of remission; **much less effective in Crohn disease**. **Topical (rectal) mesalazine is more effective than oral for distal and left-sided disease and is substantially under-used** — combining oral and topical is better than either alone.
- **Adverse effects:** generally well tolerated; headache, nausea, diarrhoea; **interstitial nephritis — uncommon but important, so renal function is monitored**; pancreatitis; and paradoxical worsening of colitis.
- **Sulfasalazine** has more adverse effects (it contains a sulfapyridine moiety): rash, haemolysis in **G6PD deficiency**, **reversible oligospermia**, folate deficiency (supplement folate), and orange discolouration of urine and contact lenses. It retains a place because it also treats the **peripheral arthritis** of IBD and is used in rheumatoid arthritis.
- **A real benefit worth knowing:** long-term 5-ASA is associated with **reduced colorectal cancer risk** in ulcerative colitis.

### 0.6.2 Corticosteroids (Gastrointestinal)
- **Key agents:** **prednisolone** (oral), **hydrocortisone/methylprednisolone** (intravenous, for acute severe colitis), **budesonide** (oral, with high first-pass metabolism so fewer systemic effects — used in ileocaecal Crohn disease and microscopic colitis), and **rectal preparations** (hydrocortisone and budesonide foams and enemas).
- **Role:** **induce remission in a flare — they do NOT maintain it.** This is the central point: **steroids are a bridge to a maintenance agent**, and a patient who cannot come off them, or who flares each time they are weaned, is **steroid-dependent and needs escalation to an immunomodulator or biologic, not another course.**
- **Adverse effects:** the full systemic corticosteroid profile (see `NEW_Drugs_10_Endocrine.md` 0.5.1), with **bone protection, glucose monitoring and adrenal considerations** on any prolonged or repeated course.

### 0.6.3 Other Drugs for Inflammatory Bowel Disease
- **Thiopurines — azathioprine, mercaptopurine.** Steroid-sparing maintenance. **Check TPMT and NUDT15 before starting** (see `NEW_Investigations_General_and_Preventive.md` 0.16), **monitor FBC and LFTs**, and remember the **azathioprine–allopurinol interaction**, which causes life-threatening myelosuppression. Long-term risks include **lymphoma and non-melanoma skin cancer** — **sun protection and skin surveillance are part of the prescription, and matter particularly in Australia.**
- **Methotrexate** — for Crohn disease; **once weekly** (see `NEW_Drugs_08_Dermatological.md` 0.3.4 for the fatal-error warning).
- **Biologics** — anti-TNF (**infliximab, adalimumab**), anti-integrin (**vedolizumab**, gut-selective), anti-IL-12/23 (**ustekinumab**) and anti-IL-23 agents; and **oral small molecules** — **JAK inhibitors (tofacitinib, upadacitinib)** and **S1P modulators (ozanimod)**. **PBS criteria in Australia are specific and change.**
- **Ciclosporin** — rescue therapy in acute severe ulcerative colitis.
- **Antibiotics** — for perianal and fistulising Crohn disease and for septic complications, not as primary therapy.

> [!danger] **ACUTE SEVERE ULCERATIVE COLITIS IS A MEDICAL EMERGENCY WITH A REAL MORTALITY.**
> Bloody diarrhoea with systemic upset requires **admission, intravenous corticosteroids, VTE prophylaxis (IBD is strongly prothrombotic — and bloody diarrhoea is NOT a contraindication to prophylactic anticoagulation), stool studies including *C. difficile*, exclusion of CMV, and early JOINT MEDICAL AND SURGICAL review.** **Avoid opioids, antimotility agents and NSAIDs** — all associated with toxic megacolon. **Daily assessment with stool frequency, CRP and abdominal examination determines whether rescue therapy or colectomy is needed** — deterioration must not be allowed to drift.

> [!danger] **BEFORE ANY IMMUNOSUPPRESSANT OR BIOLOGIC: screen for latent TB, hepatitis B and C, and HIV; vaccinate (including live vaccines) BEFORE starting; and consider Strongyloides serology.** See `NEW_Drugs_05_Anti_infectives.md` 0.6.3.

## 0.7 Drugs for Perianal Disorders

- **Key agents:** topical preparations combining a **local anaesthetic** (lidocaine, cinchocaine), a **corticosteroid**, and sometimes an astringent or antiseptic; **glyceryl trinitrate 0.2% ointment** and **topical diltiazem** for anal fissure; **botulinum toxin** injection; and **oral flavonoids** for haemorrhoids.
- **Indications:** **haemorrhoids, anal fissure, pruritus ani, proctitis.**
- **Practical points:**
  - **The foundation of treatment is stool softening and avoiding straining** — a bulk-forming or osmotic laxative, adequate fluid, and not sitting on the toilet reading. Topical agents relieve symptoms; **the laxative treats the cause**.
  - **Topical corticosteroid preparations should be used for SHORT courses only** — prolonged use causes perianal skin atrophy and can worsen pruritus ani.
  - **GTN and diltiazem work by relieving internal anal sphincter spasm** in fissure, allowing healing. **GTN causes headache in a large proportion of patients** — warn them, or they will stop; topical diltiazem causes less.
  - **Pruritus ani is usually made worse by treatment** — soaps, wipes, scrubbing and topical anaesthetics all perpetuate it. **The advice is to stop everything, wash with water only, pat dry, and avoid scratching.**

> [!danger] **NEVER attribute rectal bleeding to haemorrhoids without examining the patient and considering colorectal cancer.** **Digital rectal examination and proctoscopy at minimum; colonoscopy where there are risk factors, age over 50, a change in bowel habit, weight loss or anaemia.** "Presumed haemorrhoids" is one of the recognised routes to a delayed colorectal cancer diagnosis. Also consider **IBD, fissure, and — in the immunosuppressed or with relevant sexual history — infective proctitis and anal cancer.**

## 0.8 Other Gastrointestinal Drugs

### 0.8.1 Bile Acid Sequestrants
- **Key agents:** **colestyramine, colestipol, colesevelam**.
- **Mechanism:** **anion-exchange resins** that bind bile acids in the gut lumen, preventing their reabsorption in the terminal ileum and forcing hepatic conversion of cholesterol into new bile acids.
- **Indications:** **bile acid diarrhoea** (post-cholecystectomy, terminal ileal resection or disease, idiopathic — see 0.4.2); **cholestatic pruritus**; **dyslipidaemia** (see `NEW_Drugs_06_Cardiovascular.md` 0.9.6); and **binding toxins** in some poisonings.
- **Adverse effects:** **very poor palatability, bloating, constipation and nausea** — the main reason they are abandoned; **raised triglycerides**; and **impaired absorption of FAT-SOLUBLE VITAMINS (A, D, E, K)** with long-term use.
- **Interactions — the practical point:** they **bind other drugs indiscriminately**. **Take all other medicines at least 1 hour before or 4–6 hours after** the resin — particularly **warfarin, thyroxine, digoxin, thiazides and fat-soluble vitamins**.

### 0.8.2 Other Agents in This Group
- **Ursodeoxycholic acid** — **primary biliary cholangitis** (first-line, improves survival), intrahepatic cholestasis of pregnancy, and gallstone dissolution in selected cases.
- **Pancreatic enzyme replacement (creon)** — for **exocrine pancreatic insufficiency** in chronic pancreatitis, cystic fibrosis, pancreatic cancer and after pancreatic surgery. **Take with every meal and snack; a PPI improves efficacy** by preventing acid inactivation. **Under-dosing is very common** and causes ongoing steatorrhoea, weight loss and fat-soluble vitamin deficiency.
- **Rifaximin** — a non-absorbed antibiotic for **hepatic encephalopathy** (with lactulose) and travellers' diarrhoea.
- **Terlipressin and octreotide** — variceal bleeding; **non-selective beta-blockers** for variceal prophylaxis (see `NEW_Drugs_06_Cardiovascular.md` 0.7.2).
- **Drugs for hepatic disease** — spironolactone and furosemide for ascites, albumin with large-volume paracentesis, and antivirals for hepatitis B and C (see `NEW_Drugs_05_Anti_infectives.md` 0.6.3).
- **Antifibrotics and MASLD agents** — an evolving area; **GLP-1 agonists and pioglitazone** have the best current evidence for steatohepatitis.
- **Faecal microbiota transplantation** — recurrent *C. difficile* infection.

## 0.9 Gastrointestinal Decontaminants

- **Activated charcoal** — adsorbs many ingested toxins.
- **Whole bowel irrigation** — with macrogol electrolyte solution.
- **Gastric lavage and ipecacuanha** — **obsolete and not used.**

> [!danger] **Decontamination is a toxicologist's decision, not a reflex, and the risks are real.**
> - **Activated charcoal does NOT bind: iron, lithium, alcohols and glycols, potassium, acids and alkalis, or hydrocarbons.**
> - It has a **narrow time window** after ingestion.
> - It is **contraindicated in a patient with a reduced conscious state or unprotected airway** — **aspiration of charcoal causes a severe and sometimes fatal pneumonitis.** The decision is a balance of the risk of the poison against the risk of the charcoal; **when in doubt, do not give it.**
> - **Whole bowel irrigation** has narrow indications — **sustained-release preparations, iron, and body packers**.
> - **Never induce vomiting**, and never give anything orally in **corrosive or hydrocarbon** ingestion.
> - **CALL THE POISONS INFORMATION CENTRE — 13 11 26 in Australia** — before decontaminating anyone. See `NEW_Drugs_04_Antidotes_and_Antivenoms.md` 0.1.

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Drugs for dyspepsia reflux and peptic ulcers | SUB | yes | |
| 0.1.1 | Proton Pump Inhibitors | CLS | yes | Built jointly with `Proton pump inhibitors` — **the build list carries the same class twice, differing only in capitalisation**; both rows mapped. Australian deprescribing guidance included. |
| 0.1.1 | Proton pump inhibitors | CLS | yes | As above. |
| 0.1.2 | H2 antagonists | CLS | yes | |
| 0.1.3 | Antacids | CLS | yes | |
| 0.1.4 | Other drugs for ulcers | CLS | yes | |
| 0.2 | Antiemetics | SUB | yes | Framed on choosing by mechanism of vomiting. |
| 0.2.1 | 5HT3 antagonists | CLS | yes | QT and the pregnancy cleft signal included. |
| 0.2.2 | Dopamine antagonists (antiemetic) | CLS | yes | Metoclopramide 5-day/12-week restrictions and acute dystonia. |
| 0.2.3 | Substance P antagonists | CLS | yes | |
| 0.2.4 | Other drugs for nausea and vomiting | CLS | yes | |
| 0.3 | Drugs affecting gastrointestinal motility | SUB | yes | |
| 0.4 | Antidiarrheals | SUB | yes | |
| 0.4.1 | Opioid Antidiarrheals | CLS | yes | Loperamide cardiac toxicity in overdose, with the hERG/Nav1.5 mechanism. |
| 0.4.2 | Other drugs for diarrhoea | CLS | yes | |
| 0.5 | Laxatives | SUB | yes | |
| 0.5.1 | Osmotic laxatives | CLS | yes | |
| 0.5.2 | Stimulant laxatives | CLS | yes | |
| 0.5.3 | Stool softeners | CLS | yes | Docusate's weak evidence stated plainly. |
| 0.5.4 | Other laxatives | CLS | yes | |
| 0.6 | Drugs for inflammatory bowel diseases | SUB | yes | |
| 0.6.1 | 5-Aminosalicylates | CLS | yes | |
| 0.6.2 | Corticosteroids (gastrointestinal) | CLS | yes | Induce-not-maintain principle and steroid dependence. |
| 0.6.3 | Other drugs for inflammatory bowel disease | CLS | yes | Carries the acute severe UC emergency callout. |
| 0.7 | Drugs for perianal disorders | SUB | yes | |
| 0.8 | Other gastrointestinal drugs | SUB | yes | |
| 0.8.1 | Bile Acid Sequestrants | CLS | yes | |
| 0.9 | Gastrointestinal decontaminants | SUB | yes | |

**Rows in file: 28 (9 SUB + 19 CLS). AMH section 12 build-list rows: 28. Section complete.**

> [!note] **One pair of build-list rows is a pure capitalisation duplicate** — `Proton Pump Inhibitors` and `Proton pump inhibitors`. Built once at 0.1.1 with both rows mapped.
