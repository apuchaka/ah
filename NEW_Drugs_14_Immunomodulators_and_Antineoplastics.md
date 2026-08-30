---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 14 Immunomodulators and antineoplastics
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Immunomodulators and Antineoplastics (AMH section 14)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.** Cytotoxic dosing is protocol-driven, frequently **per square metre of body surface area**, and is never prescribed from memory or from a reference like this one.

> [!info] **Depth note — what an intern actually does with these drugs.**
> An intern does not prescribe chemotherapy or initiate a biologic. What they do is **recognise and act on the complications**: **neutropenic sepsis, tumour lysis, extravasation, immune-related adverse events, opportunistic infection, and drug interactions in an immunosuppressed patient**. This file is weighted accordingly — the mechanisms are given briefly, and the emergencies are given in full.

---

## 0.1 Cytotoxic Antineoplastics

> [!danger] **THE FOUR ONCOLOGICAL EMERGENCIES AN INTERN MUST RECOGNISE**
> **1. NEUTROPENIC SEPSIS.** **A fever in a patient who has had chemotherapy in the last 6 weeks is neutropenic sepsis until proven otherwise.** **Take cultures and give broad-spectrum intravenous antibiotics WITHIN ONE HOUR — do not wait for the neutrophil count, do not wait for imaging, do not wait for a senior to arrive.** Patients can be normothermic and still septic (particularly on steroids), so **rigors, hypotension, tachycardia, confusion or simply "unwell" count**. Mortality rises measurably with every hour of delay.
> **2. TUMOUR LYSIS SYNDROME.** **Hyperkalaemia, hyperphosphataemia, hyperuricaemia and hypocalcaemia** with acute kidney injury and arrhythmia, typically after starting treatment for a bulky, rapidly proliferating tumour (high-grade lymphoma, leukaemia). **Prevention is hydration plus allopurinol or rasburicase** (**rasburicase is contraindicated in G6PD deficiency**). See [[10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies]].
> **3. EXTRAVASATION** — see the callout in 0.1.2.
> **4. SPINAL CORD COMPRESSION and SVC OBSTRUCTION** — not drug complications, but they present to the same patients and need the same urgency.

### 0.1.1 Antimetabolites
- **Mechanism:** structural analogues of normal metabolites that are incorporated into or block **DNA and RNA synthesis** — hence they are **S-phase specific** and most active against rapidly dividing cells.
- **Key agents and their signature toxicities:**
  - **Methotrexate** (folate antagonist) — **mucositis, myelosuppression, hepatotoxicity, pneumonitis, nephrotoxicity at high dose.** **Rescued with FOLINIC acid (leucovorin), not folic acid.** **Dosed ONCE WEEKLY in non-oncology use** — see the fatal-error warning in `NEW_Drugs_08_Dermatological.md` 0.3.4. **Interactions: NSAIDs, co-trimoxazole/trimethoprim, penicillins and PPIs raise levels** — the co-trimoxazole combination has caused fatal pancytopenia.
  - **Fluoropyrimidines — 5-fluorouracil, capecitabine** — mucositis, diarrhoea, myelosuppression, **palmar-plantar erythrodysaesthesia (hand-foot syndrome)**, and **coronary vasospasm/chest pain**. **DPYD genotyping before treatment** identifies patients at risk of severe or fatal toxicity (see `NEW_Investigations_General_and_Preventive.md` 0.16).
  - **Thiopurines — mercaptopurine, thioguanine** — myelosuppression; **TPMT and NUDT15 testing before starting**, and the **azathioprine/mercaptopurine–allopurinol interaction** (see `NEW_Drugs_03_Analgesics.md` 0.1.1).
  - **Cytarabine** — myelosuppression, cerebellar toxicity at high dose, conjunctivitis (prophylactic steroid eye drops).
  - **Gemcitabine** — myelosuppression, flu-like symptoms, **haemolytic uraemic syndrome** (rare).
  - **Pemetrexed** — requires **folic acid and vitamin B₁₂ supplementation** to reduce toxicity.
  - **Hydroxyurea (hydroxycarbamide)** — myelosuppression, leg ulcers; also used in sickle cell disease.

### 0.1.2 Cytotoxic Antibiotics
- **Mechanism:** microbially derived agents that intercalate DNA, inhibit **topoisomerase II**, and generate free radicals.
- **Key agents:**
  - **Anthracyclines — doxorubicin, daunorubicin, epirubicin, idarubicin.** **CARDIOTOXICITY is the class-defining problem.** Sources describe **early toxicity** as mainly **sinus tachycardia and non-specific ST-T changes**, with **tachyarrhythmias, bradycardia, and atrioventricular and bundle-branch block** also reported; **late toxicity is a dose-dependent, often irreversible dilated cardiomyopathy.** **Cumulative lifetime dose is tracked, baseline and serial cardiac function (echo or MUGA) is monitored, and dexrazoxane is used as a cardioprotectant in selected patients.** Anthracyclines also cause severe myelosuppression, alopecia, mucositis, and **red discolouration of urine** (harmless — warn the patient).
  - **Bleomycin** — minimal myelosuppression, but **PULMONARY FIBROSIS** is the dose-limiting toxicity, and **high inspired oxygen concentrations can precipitate or worsen it, including during anaesthesia** — **tell the anaesthetist about any bleomycin exposure, ever**. Also causes fever and skin changes.
  - **Actinomycin D, mitomycin C** (the latter also causes **haemolytic uraemic syndrome**), mitoxantrone.

> [!danger] **CHEMOTHERAPY EXTRAVASATION IS A TIME-CRITICAL EMERGENCY.**
> Sources classify cytotoxics as **vesicants, irritants and non-vesicants**, and note that **vesicants induce tissue damage, ulceration and necrosis**. Reported resolution times range from a **median of 14 days for platinum compounds to 55 days for anthracyclines**, and anthracycline extravasation can require surgical debridement and grafting.
> **If extravasation is suspected: STOP the infusion immediately, DO NOT remove the cannula, aspirate what you can through it, mark and photograph the area, elevate the limb, and call the oncology/haematology team and the extravasation protocol NOW.** Warm or cold compresses differ by agent — follow the protocol, do not guess.
> **Specific antidotes exist:** sources note **dexrazoxane is the only registered antidote for anthracycline extravasation**; **hyaluronidase** is used for vinca alkaloids; **thiosulfate** for some agents.
> **Prevention is the real answer: vesicants are given through a central line wherever possible, by trained staff, with the site observed throughout.**

### 0.1.3 Other Cytotoxic Antineoplastics
- **Alkylating agents — cyclophosphamide, ifosfamide, chlorambucil, melphalan, busulfan, temozolomide.** Cross-link DNA. **Cyclophosphamide and ifosfamide cause HAEMORRHAGIC CYSTITIS from the metabolite acrolein — prevented with hydration and MESNA**; ifosfamide additionally causes an **encephalopathy** (treated with methylthioninium chloride). Alkylators carry a real risk of **infertility (offer fertility preservation BEFORE treatment — this is time-critical and frequently missed) and secondary malignancy**.
- **Platinum compounds — cisplatin, carboplatin, oxaliplatin.** **Cisplatin: severe emetogenicity, NEPHROTOXICITY (requires vigorous hydration and magnesium replacement), OTOTOXICITY (irreversible high-frequency hearing loss — audiometry before and during) and peripheral neuropathy.** **Carboplatin** is less nephrotoxic and ototoxic but more myelosuppressive. **Oxaliplatin causes a characteristic COLD-INDUCED acute neuropathy** — warn the patient not to drink cold fluids or touch cold objects for days after treatment — and a cumulative sensory neuropathy.
- **Vinca alkaloids — vincristine, vinblastine, vinorelbine.** Inhibit microtubule assembly. **Vincristine causes a dose-limiting PERIPHERAL NEUROPATHY** and constipation/ileus, with relatively little myelosuppression.

> [!danger] **VINCRISTINE IS FATAL IF GIVEN INTRATHECALLY. It must ONLY ever be given intravenously.** This error has killed patients repeatedly worldwide, which is why vincristine is dispensed in a **minibag rather than a syringe**, labelled **"for intravenous use only — fatal if given by other routes"**, and never taken to a room where intrathecal drugs are being administered.

- **Taxanes — paclitaxel, docetaxel.** Stabilise microtubules. **Hypersensitivity reactions require corticosteroid and antihistamine premedication**; peripheral neuropathy, myelosuppression, alopecia, and fluid retention (docetaxel).
- **Topoisomerase inhibitors — irinotecan, topotecan, etoposide.** **Irinotecan causes an ACUTE cholinergic diarrhoea (treated with atropine) and a DELAYED, potentially severe diarrhoea (treated with high-dose loperamide)** — the distinction determines the treatment, and **UGT1A1 polymorphisms increase toxicity**.

> [!warning] **Handling and safety:** cytotoxics are prepared and administered under **cytotoxic precautions**, with **body fluid precautions for a defined period afterwards** (relevant to nursing staff, carers and to advice about sexual activity and contraception). **Cytotoxic waste is segregated.** **Pregnant staff should not handle them.**

## 0.2 Drugs Used with Antineoplastics

- **Antiemetics** — the single most valued supportive treatment by patients. **Highly emetogenic regimens need a 5-HT₃ antagonist + dexamethasone + an NK₁ antagonist**, with olanzapine increasingly added; see `NEW_Drugs_12_Gastrointestinal.md` 0.2.
- **Colony stimulating factors (G-CSF)** — primary and secondary prophylaxis of febrile neutropenia; **not a substitute for antibiotics in established neutropenic sepsis** (see `NEW_Drugs_07_Blood_and_Electrolytes.md` 0.2.3).
- **Tumour lysis prophylaxis — allopurinol, rasburicase** and hydration.
- **Uroprotection — MESNA** with cyclophosphamide and ifosfamide.
- **Cardioprotection — dexrazoxane** with anthracyclines.
- **Rescue agents — folinic acid** with methotrexate and as a fluorouracil modulator; **glucarpidase** for methotrexate toxicity with renal failure.
- **Bone-targeted agents — bisphosphonates and denosumab** for skeletal-related events in bone metastases and myeloma, and for hypercalcaemia of malignancy (see `NEW_Drugs_10_Endocrine.md` 0.1).
- **Mucositis care, antimicrobial prophylaxis (PJP, antifungal, antiviral), vaccination before treatment, and fertility preservation** — all part of the supportive package.
- **Analgesia and palliative care** — see [[10_11c_Oncology_-_Palliative_Care_Prescribing]]. **Early palliative care involvement improves quality of life and, in some settings, survival** — it is not a late-stage referral.

> [!danger] **CHECK EVERY DRUG INTERACTION IN AN ONCOLOGY PATIENT.** Azole antifungals with vinca alkaloids (neurotoxicity), allopurinol with thiopurines, co-trimoxazole with methotrexate, warfarin with capecitabine, and CYP interactions with the oral targeted agents are all recognised causes of serious harm. **Complementary and herbal medicines — especially St John's wort — are common in this population and frequently undisclosed. Ask.**

## 0.3 Hormonal Antineoplastic Drugs

### 0.3.1 Antiandrogens
- **Key agents:** **bicalutamide, flutamide, nilutamide** (first generation); **enzalutamide, apalutamide, darolutamide** (second generation, androgen receptor signalling inhibitors); **abiraterone** (a CYP17 inhibitor blocking androgen synthesis, given **with prednisolone**); **cyproterone acetate**.
- **Indications:** **prostate cancer** — including as "flare cover" when starting a GnRH agonist (see 0.3.3); and cyproterone in gender-affirming hormone therapy and hypersexuality.
- **Adverse effects:** **hot flushes, gynaecomastia and breast tenderness, sexual dysfunction, fatigue**; **hepatotoxicity** (monitor LFTs — flutamide especially); enzalutamide causes **fatigue, falls and a small seizure risk**; abiraterone causes **mineralocorticoid excess — hypertension, hypokalaemia and fluid retention** (hence the co-prescribed steroid), and hepatotoxicity.

### 0.3.2 Aromatase Inhibitors
- **Key agents:** **anastrozole, letrozole** (non-steroidal), **exemestane** (steroidal).
- **Mechanism:** block **aromatase**, the enzyme converting androgens to oestrogens in peripheral tissue — the main oestrogen source **after menopause**.
- **Indications:** **hormone receptor-positive breast cancer in POSTMENOPAUSAL women** (adjuvant and metastatic); and, off-label, ovulation induction.

> [!danger] **Aromatase inhibitors DO NOT WORK in premenopausal women** — ovarian oestrogen production overwhelms them and they can paradoxically stimulate the ovary. **A premenopausal woman needs ovarian suppression (a GnRH agonist or oophorectomy) as well, or tamoxifen instead.** Confirming menopausal status matters, and chemotherapy-induced amenorrhoea is not the same as menopause.

- **Adverse effects:** **ARTHRALGIA AND MYALGIA — very common, often the reason for stopping, and a major adherence problem in adjuvant therapy**; **osteoporosis and fracture** (so **bone density monitoring and calcium/vitamin D are part of the prescription**, with a bisphosphonate or denosumab if needed); hot flushes; vaginal dryness and dyspareunia; hyperlipidaemia.

### 0.3.3 Gonadotrophin-Releasing Hormone Agonists (Oncology)
- **Key agents:** **goserelin, leuprorelin, triptorelin** (agonists); **degarelix and relugolix** (GnRH **antagonists**).
- **Mechanism:** continuous GnRH receptor stimulation causes **downregulation and desensitisation** of pituitary gonadotrophs → profound suppression of LH/FSH and therefore of testosterone or oestrogen — a "medical castration".
- **Indications:** **prostate cancer** (androgen deprivation therapy), **premenopausal breast cancer** (ovarian suppression), endometriosis and fibroids, and ovarian protection during chemotherapy.

> [!danger] **THE TESTOSTERONE "FLARE" — the reason antiandrogen cover is given.**
> A GnRH **agonist** causes an initial **surge** in testosterone over the first one to two weeks before suppression occurs. In a man with **significant metastatic disease — spinal metastases, urinary obstruction — this flare can precipitate SPINAL CORD COMPRESSION, pathological fracture or acute retention.** **An antiandrogen is started before, and continued through, the first weeks of a GnRH agonist.** **GnRH ANTAGONISTS (degarelix) cause no flare** and are preferred where flare would be dangerous.

- **Adverse effects of androgen deprivation:** hot flushes, sexual dysfunction and loss of libido, **osteoporosis** (monitor and protect bone), **metabolic syndrome, diabetes and cardiovascular risk**, sarcopenia, fatigue, gynaecomastia, anaemia, and **mood and cognitive effects**. **These are substantial, long-term and under-managed** — exercise, bone protection and cardiometabolic screening are part of care.
- **In women:** menopausal symptoms and bone loss; **add-back therapy** is used in benign indications.

### 0.3.4 Other Hormonal Antineoplastics
- **Tamoxifen** — a **selective oestrogen receptor modulator**: antagonist in breast, **agonist in endometrium and bone**. Used in **pre- and postmenopausal** hormone receptor-positive breast cancer. **Adverse effects: VTE, ENDOMETRIAL HYPERPLASIA AND CARCINOMA (any postmenopausal bleeding on tamoxifen requires urgent investigation), hot flushes, cataract**; **teratogenic**. **Interaction: CYP2D6 inhibitors (fluoxetine, paroxetine, bupropion) reduce conversion to the active metabolite endoxifen** — a genuinely important interaction, since antidepressants are commonly co-prescribed for hot flushes; **venlafaxine or escitalopram are preferred**.
- **Fulvestrant** — a selective oestrogen receptor degrader, given intramuscularly.
- **Progestogens (megestrol, medroxyprogesterone)** — endometrial cancer and appetite stimulation.
- **Corticosteroids** — integral to lymphoma and myeloma regimens, and used for cerebral oedema, cord compression, hypercalcaemia, nausea and appetite.
- **Somatostatin analogues** — neuroendocrine tumours (see `NEW_Drugs_10_Endocrine.md` 0.5.4).

## 0.4 Non-Cytotoxic Antineoplastics

### 0.4.1 Antineoplastic Antibodies
- **Key agents and targets:** **trastuzumab and pertuzumab** (HER2, breast and gastric cancer), **rituximab** (CD20, B-cell lymphoma and many autoimmune diseases), **bevacizumab** (VEGF), **cetuximab and panitumumab** (EGFR), **antibody-drug conjugates** (trastuzumab emtansine/deruxtecan, brentuximab vedotin), and the **immune checkpoint inhibitors** — **pembrolizumab and nivolumab** (PD-1), **atezolizumab and durvalumab** (PD-L1), **ipilimumab** (CTLA-4).
- **Class adverse effects:** **infusion reactions** (premedication and slow first infusions); **trastuzumab causes CARDIOTOXICITY — usually reversible, unlike anthracyclines, but requiring baseline and serial cardiac function monitoring, and additive with anthracyclines**; **bevacizumab causes hypertension, proteinuria, impaired wound healing, bleeding, arterial thrombosis and gastrointestinal perforation** (held around surgery); **EGFR inhibitors cause an acneiform rash (whose severity correlates with response) and hypomagnesaemia**.

> [!danger] **RITUXIMAB AND HEPATITIS B REACTIVATION — screen before, every time.**
> **Rituximab and other B-cell-depleting agents can reactivate hepatitis B, including in people who appear to have cleared it (HBsAg negative, anti-HBc positive), causing fulminant hepatitis and death.** **Screen for HBsAg, anti-HBc and anti-HBs before starting**, and give antiviral prophylaxis where indicated. Also screen for TB, HIV and hepatitis C, and **vaccinate before starting** — vaccine responses are poor afterwards. Rituximab also causes **hypogammaglobulinaemia with recurrent infection** and, rarely, **progressive multifocal leukoencephalopathy (PML)**.

> [!danger] **IMMUNE CHECKPOINT INHIBITORS: IMMUNE-RELATED ADVERSE EVENTS CAN AFFECT ANY ORGAN, AND THEY ARE TREATED WITH STEROIDS, NOT WITH ANTIBIOTICS OR ANTIDIARRHOEALS.**
> These drugs remove the brakes on T cells, so the toxicity is **autoimmune**, not cytotoxic. **Colitis** (diarrhoea — **and giving loperamide instead of steroids can lead to perforation**), **pneumonitis** (breathlessness and cough), **hepatitis**, **thyroiditis and hypophysitis**, **adrenal insufficiency**, **nephritis**, **myocarditis** (rare but with high mortality), **neurological syndromes** and **severe skin reactions**.
> **The practical rules for an intern: (1) ANY new symptom in a patient on a checkpoint inhibitor is an immune-related adverse event until proven otherwise; (2) they can begin WEEKS TO MONTHS after the last dose, including after treatment has finished; (3) contact the treating oncology team immediately — the management is usually high-dose CORTICOSTEROIDS; (4) do not attribute breathlessness, diarrhoea or fatigue to something else without discussing it.** Endocrinopathies (hypophysitis, adrenal insufficiency, thyroiditis) are **frequently permanent** and require lifelong replacement.

### 0.4.2 Other Non-Cytotoxic Antineoplastics
- **Small-molecule tyrosine kinase inhibitors** — **imatinib and successors** (BCR-ABL in CML — a genuine transformation of a once-fatal disease), **EGFR inhibitors** (osimertinib, erlotinib), **ALK inhibitors**, **BRAF/MEK inhibitors** (melanoma), **BTK inhibitors** (ibrutinib), **CDK4/6 inhibitors** (palbociclib, ribociclib), **PARP inhibitors** (olaparib, in BRCA-mutated disease), **VEGF-receptor inhibitors** (sunitinib, sorafenib).
- **Class issues:** most are **oral, taken at home, and CYP3A4-metabolised — so interactions with azoles, macrolides, rifampicin, anticonvulsants and St John's wort are frequent and clinically significant**; many cause **hypertension, rash, diarrhoea, hepatotoxicity, hypothyroidism and QT prolongation**; **ibrutinib causes atrial fibrillation and bleeding**; several are teratogenic. **Adherence and interaction checking are the main safety tasks, and the patient is at home rather than in a chemotherapy unit.**
- **Proteasome inhibitors — bortezomib, carfilzomib** (myeloma); bortezomib causes **peripheral neuropathy** and requires **antiviral prophylaxis against herpes zoster**.
- **Immunomodulatory drugs — thalidomide, lenalidomide, pomalidomide** (myeloma). **Powerfully TERATOGENIC — supplied under a mandatory pregnancy prevention programme**; also cause **VTE (thromboprophylaxis is required)**, neuropathy (thalidomide) and myelosuppression.
- **CAR-T cell therapy and bispecific antibodies** — **cytokine release syndrome** (fever, hypotension, hypoxia — treated with tocilizumab and steroids) and **neurotoxicity (ICANS)**; highly specialised centres.
- **Radiopharmaceuticals** — Lu-177 PSMA and DOTATATE therapies.

## 0.5 Immunomodulating Drugs

### 0.5.1 Calcineurin Inhibitors
- **Key agents:** **ciclosporin, tacrolimus**.
- **Mechanism:** bind immunophilins to inhibit **calcineurin**, blocking **IL-2 transcription** and T-cell activation.
- **Indications:** **solid organ and stem cell transplantation** (the backbone of maintenance immunosuppression), graft-versus-host disease, and severe autoimmune disease — psoriasis, atopic dermatitis, nephrotic syndrome, ulcerative colitis rescue.
- **Adverse effects:** **NEPHROTOXICITY** (both acute haemodynamic and chronic interstitial fibrosis — the dominant long-term problem); **hypertension**; **neurotoxicity** (tremor, headache, seizures, **PRES**); **hyperkalaemia, hypomagnesaemia, hyperuricaemia and gout**; **diabetes** (tacrolimus more than ciclosporin); **ciclosporin specifically causes gingival hypertrophy and hypertrichosis**, tacrolimus causes alopecia; and **increased infection and malignancy risk — particularly skin cancer and post-transplant lymphoproliferative disorder.**

> [!danger] **CALCINEURIN INHIBITORS HAVE A NARROW THERAPEUTIC INDEX AND MASSIVE CYP3A4/P-GLYCOPROTEIN INTERACTIONS. Every new drug in a transplant patient must be checked.**
> **Levels RISE with: azole antifungals, macrolides (clarithromycin, erythromycin), diltiazem and verapamil, HIV protease inhibitors, nirmatrelvir/ritonavir, grapefruit juice.** **Levels FALL with: rifampicin, phenytoin, carbamazepine, St John's wort** — causing **graft rejection**.
> **Therapeutic drug monitoring is mandatory**, formulations are **not interchangeable brand-to-brand or between immediate- and modified-release**, and **a patient's transplant unit must be contacted before changing anything.** **Never omit doses in an admitted transplant patient**, and never assume a "routine" antibiotic is safe.

### 0.5.2 mTOR Inhibitors
- **Key agents:** **sirolimus, everolimus**.
- **Mechanism:** inhibit the **mammalian target of rapamycin**, blocking IL-2-driven lymphocyte proliferation; also antiproliferative in tumours.
- **Indications:** transplantation (often as a **calcineurin-sparing** agent where nephrotoxicity is a problem); renal cell carcinoma, neuroendocrine and breast cancer; tuberous sclerosis complex; and drug-eluting stent coatings.
- **Adverse effects:** **impaired wound healing and lymphocoele** (so they are often avoided in the immediate post-transplant period), **mouth ulcers/stomatitis** (very common), **hyperlipidaemia**, **proteinuria**, **non-infectious pneumonitis**, myelosuppression, and peripheral oedema. Same **CYP3A4 interaction burden** as the calcineurin inhibitors.

### 0.5.3 TNF-Alpha Inhibitors
- **Key agents:** **adalimumab, etanercept, infliximab, golimumab, certolizumab**.
- **Mechanism:** neutralise **tumour necrosis factor alpha**, a central inflammatory cytokine.
- **Indications:** **rheumatoid arthritis, ankylosing spondylitis and axial spondyloarthritis, psoriatic arthritis, psoriasis, inflammatory bowel disease**, uveitis, hidradenitis suppurativa. **PBS authority criteria in Australia are specific, require documented failure of prior therapy, and change.**

> [!danger] **TNF INHIBITORS AND TUBERCULOSIS: SCREEN BEFORE STARTING, EVERY TIME.**
> TNF is essential for granuloma maintenance, so **TNF inhibition reactivates latent tuberculosis**, often with **atypical, extrapulmonary or disseminated** presentations. **Screen with a TST or IGRA plus a chest X-ray and history before starting** (see `NEW_Investigations_Respiratory.md` 0.7), and **treat latent TB before or alongside** the biologic. Also screen for **hepatitis B and C and HIV**, consider **Strongyloides** serology, and **vaccinate — including live vaccines — BEFORE starting, as live vaccines are contraindicated afterwards.**
> **Other class risks:** serious bacterial, fungal and opportunistic infection; **demyelinating disease** (avoid in multiple sclerosis); **worsening of heart failure** (avoid in moderate-to-severe heart failure); drug-induced lupus; injection and infusion reactions; and a debated malignancy signal, with **skin cancer surveillance particularly relevant in Australia**.
> **Withhold during serious infection**, and plan around surgery.

### 0.5.4 Immunosuppressants and Other Immunosuppressants
*(covers build-list classes: Immunosuppressants; Other immunosuppressants)*
- **Antiproliferative agents — azathioprine and mycophenolate.** **Azathioprine: check TPMT/NUDT15, monitor FBC and LFTs, and never co-prescribe with allopurinol without drastic dose reduction.** **Mycophenolate is TERATOGENIC (first-trimester pregnancy loss and major malformations) and requires a pregnancy prevention programme** — this applies to **both female and male patients** under current advice, and is frequently missed. Both increase infection and malignancy risk.
- **Corticosteroids** — the backbone of most immunosuppressive regimens; see `NEW_Drugs_10_Endocrine.md` 0.5.1 for the adverse effect profile, sick day rules and never-stop-abruptly warning.
- **Cyclophosphamide** — for severe vasculitis, lupus nephritis and other organ-threatening autoimmune disease; **haemorrhagic cystitis (MESNA), infertility (offer preservation), and secondary malignancy**.
- **Antithymocyte globulin, basiliximab, alemtuzumab** — induction and rejection therapy in transplantation.
- **Other biologics and small molecules:** **rituximab** (see 0.4.1); **tocilizumab** (IL-6, and the treatment for cytokine release syndrome); **abatacept**; **IL-17, IL-23 and IL-12/23 inhibitors**; **JAK inhibitors (tofacitinib, baricitinib, upadacitinib)** — effective and oral, but carrying class warnings for **serious infection including herpes zoster, VTE, major adverse cardiovascular events and malignancy**, with screening and monitoring requirements; **belimumab and anifrolumab** in lupus; **eculizumab and ravulizumab** (**meningococcal vaccination is MANDATORY before starting**).

> [!danger] **A FEVER IN AN IMMUNOSUPPRESSED PATIENT IS AN EMERGENCY, AND THE USUAL SIGNS MAY BE ABSENT.**
> Steroids and immunosuppressants blunt fever, peritonism and inflammatory markers — **a patient can have a perforated viscus or overwhelming sepsis with an unimpressive examination.** Think about **opportunistic organisms — PJP, CMV, invasive fungal disease, TB, Nocardia, Listeria, Strongyloides hyperinfection** — take cultures broadly, image with a low threshold, and involve infectious diseases early. **Consider prophylaxis (PJP, antifungal, antiviral) and check it is prescribed.** And **consider adrenal insufficiency** in any hypotensive patient on long-term steroids.

### 0.5.5 Other Immunomodulating Drugs
- **Immunoglobulin (IVIg and subcutaneous)** — replacement in immunodeficiency and immunomodulation in **ITP, Guillain-Barré syndrome, CIDP, myasthenic crisis and Kawasaki disease**. Adverse effects: headache and aseptic meningitis, renal impairment, **thrombosis**, haemolysis, and infusion reactions. **Supply is restricted by national criteria in Australia.**
- **Vaccines** — see `NEW_Drugs_20_Vaccines.md` 0.1.
- **Immunostimulants** — BCG (see `NEW_Drugs_13_Genitourinary.md` 0.6), imiquimod, and the CAR-T and bispecific platforms above.
- **Hydroxychloroquine, sulfasalazine, leflunomide, methotrexate** — conventional synthetic DMARDs; see `NEW_Drugs_19_Rheumatological.md` 0.1.2.

## 0.6 Interferons
- **Key agents:** **peginterferon alfa** (2a and 2b), interferon beta (multiple sclerosis), interferon gamma (chronic granulomatous disease).
- **Mechanism:** recombinant cytokines activating host antiviral, antiproliferative and immunomodulatory pathways.
- **Indications — now substantially narrowed.** **Hepatitis C use has been abandoned entirely** since the direct-acting antivirals (see `NEW_Drugs_05_Anti_infectives.md` 0.6.3). Remaining roles: **hepatitis B and D**, **myeloproliferative neoplasms** (where peginterferon has a genuine and expanding role in polycythaemia vera and essential thrombocythaemia, including in pregnancy), **melanoma** (largely displaced by checkpoint inhibitors), some renal cell carcinoma, and **interferon beta in relapsing-remitting multiple sclerosis** (see `NEW_Drugs_15_Neurological.md` 0.4).
- **Adverse effects — the reason they were abandoned as soon as alternatives existed:** a severe **flu-like syndrome** with every dose; **DEPRESSION AND SUICIDALITY** (screen before and during — this is not a minor caveat); **bone marrow suppression**; **thyroid dysfunction** (both hypo- and hyperthyroidism); autoimmune phenomena; fatigue, anorexia and weight loss; alopecia; and injection site reactions.
- **Contraindications:** **decompensated cirrhosis, uncontrolled psychiatric illness, and autoimmune disease.**

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Cytotoxic antineoplastics | SUB | yes | Opens with the four oncological emergencies. |
| 0.1.1 | Antimetabolites | CLS | yes | |
| 0.1.2 | Cytotoxic Antibiotics | CLS | yes | Anthracycline cardiotoxicity and the extravasation emergency with dexrazoxane as the registered anthracycline antidote. |
| 0.1.3 | Other cytotoxic antineoplastics | CLS | yes | Alkylators, platinums, vincas (including the never-intrathecal rule), taxanes, topoisomerase inhibitors. |
| 0.2 | Drugs used with antineoplastics | SUB | yes | |
| 0.3 | Hormonal antineoplastic drugs | SUB | yes | |
| 0.3.1 | Antiandrogens | CLS | yes | |
| 0.3.2 | Aromatase inhibitors | CLS | yes | Includes why they do not work in premenopausal women. |
| 0.3.3 | Gonadotrophin-releasing hormone agonists (oncology) | CLS | yes | Testosterone flare and antiandrogen cover. |
| 0.3.4 | Other hormonal antineoplastics | CLS | yes | Tamoxifen, including the CYP2D6 antidepressant interaction. |
| 0.4 | Non-cytotoxic antineoplastics | SUB | yes | |
| 0.4.1 | Antineoplastic antibodies | CLS | yes | Rituximab and hepatitis B reactivation; immune-related adverse events of checkpoint inhibitors. |
| 0.4.2 | Other non-cytotoxic antineoplastics | CLS | yes | |
| 0.5 | Immunomodulating drugs | SUB | yes | |
| 0.5.1 | Calcineurin Inhibitors | CLS | yes | Narrow therapeutic index and the CYP3A4 interaction warning. |
| 0.5.2 | mTOR Inhibitors | CLS | yes | |
| 0.5.3 | TNF-Alpha Inhibitors | CLS | yes | TB screening before starting. |
| 0.5.4 | Immunosuppressants | CLS | yes | Built jointly with `Other immunosuppressants` — the build list carries both with no distinguishable scope; both rows mapped. |
| 0.5.4 | Other immunosuppressants | CLS | yes | As above. |
| 0.5.5 | Other immunomodulating drugs | CLS | yes | |
| 0.6 | Interferons | SUB | yes | Built with an explicit statement of how far their role has narrowed. |

**Rows in file: 21 (6 SUB + 15 CLS). AMH section 14 build-list rows: 21. Section complete.**

> [!note] **One pair of build-list rows (`Immunosuppressants` / `Other immunosuppressants`) has no distinguishable scope** and is built once at 0.5.4 with both rows mapped.
