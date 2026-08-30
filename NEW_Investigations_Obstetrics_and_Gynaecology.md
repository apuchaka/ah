---
block: NEW build — Investigations (Obstetrics and Gynaecology)
source: data/BULK_BUILD_PLAN.md Part A; items from data/no_header_build_queue.md
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Investigations: Obstetrics and Gynaecology

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay- and laboratory-dependent values are **omitted with the omission stated in place**.

> [!note] **Three build-list rows are miscategorised and are not built here.** `C-Spine X-Ray`, `Compression Test` and `Distraction Test` appear under **Gynaecology** in `data/build_list_investigations.md`, but none is a gynaecological investigation — the two named tests are cervical-spine/nerve-root **exam manoeuvres** (Spurling compression, cervical distraction) and the third is an orthopaedic imaging study. They are deferred to the files where they belong; see the build status table.

---

## 0.1 Cervical Screening Test and Cervical Screening Abnormality (Australian NCSP)

**D:** The **Cervical Screening Test** is a **primary oncogenic HPV nucleic-acid test** with **partial genotyping** (HPV 16/18 reported separately from other oncogenic types), performed on a **liquid-based cytology** specimen so that cytology can be run **reflexively on the same sample** when the HPV result requires it.

**Ind:** **Routine screening every 5 years from age 25 to 74** in women and people with a cervix who have ever been sexually active — including those **vaccinated against HPV**, who remain in the program. Symptomatic patients (postcoital, intermenstrual or postmenopausal bleeding, or an abnormal-looking cervix) are **not** managed by screening: they need a **co-test and direct specialist assessment**.

**Role:** The test that replaced two-yearly Pap cytology in **December 2017**. It screens for the **cause** (persistent oncogenic HPV) rather than the downstream cell change, which is why the interval could safely lengthen from 2 years to 5.

> [!info] **The management pathway is the examinable content**
> - **HPV 16/18 detected** → **refer for colposcopy**, regardless of the cytology result. These genotypes carry the highest progression risk.
> - **HPV detected, not 16/18** → **reflex LBC on the same specimen**:
>   - negative, pLSIL or LSIL → **repeat HPV test in 12 months**;
>   - pHSIL, HSIL, glandular abnormality or cancer → **colposcopy**.
> - **HPV not detected** → return to routine 5-yearly screening.
> - At the **12-month repeat**, HPV still detected → colposcopy.

> [!warning] **Higher-risk groups go straight to colposcopy at the 12-month repeat if HPV is still detected, whatever the cytology says** — sources name those **two or more years overdue for screening**, those who identify as **Aboriginal or Torres Strait Islander**, and those **aged 50 or over**.

> [!tip] **Self-collection is a full-validity option, not a lesser test.** A self-collected vaginal swab is analysed on the same HPV platform and is now universally available in the program rather than restricted to the never- and under-screened. **The one limitation matters:** a self-collected sample **cannot have reflex cytology performed on it** — a patient whose self-collected sample returns HPV not-16/18 must return for a clinician-collected sample (or go to colposcopy). Uptake of self-collection has risen steeply since universal availability.

> [!danger] **Do not ignore**
> - **A negative screening test never explains symptoms.** Postcoital, intermenstrual or postmenopausal bleeding requires examination and specialist referral **even with a normal screening history** — screening is for asymptomatic people and cannot exclude cancer in a symptomatic one. This is the commonest and most serious error made with this test.
> - **HPV vaccination does not remove the need to screen.**
> - Screening continues in pregnancy where due (take the sample, avoid the endocervical brush), and post-hysterectomy management depends on whether the cervix was removed and on prior history.
> - See [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]].

**Normal/abnormal:** Reported as **HPV 16/18 detected / HPV (not 16/18) detected / HPV not detected**, with reflex cytology where applicable, and an explicit **recommended management** statement — read that statement, it is part of the report.

**Alt:** Colposcopy with directed biopsy (the diagnostic test); co-test (HPV plus cytology) in the symptomatic patient and in test-of-cure after treatment of a high-grade lesion; HPV vaccination as primary prevention.

## 0.2 Liquid-Based Cytology (LBC)

**D:** Cervical cells collected into a **liquid preservative vial** rather than smeared onto a slide; the laboratory produces a thin, even monolayer, removing blood, mucus and inflammatory debris.

**Ind:** In Australia, LBC is now performed **reflexively on the HPV-positive (not 16/18) sample** — it is a **triage test within the screening program**, not a standalone screen. It is also used in the symptomatic patient as part of a co-test, and in test-of-cure surveillance after treatment of a high-grade abnormality.

**Role:** **Cytology's role has been demoted from primary screen to triage.** Its remaining job is to sort HPV-positive patients into "repeat in 12 months" and "colposcopy now."

> [!info] **Reporting terminology (Australian Modified Bethesda System)**
> `Negative` · **`pLSIL` / `LSIL`** (possible/definite low-grade squamous intraepithelial lesion) · **`pHSIL` / `HSIL`** (possible/definite high-grade) · **glandular abnormalities** (AIS, adenocarcinoma) · **squamous cell carcinoma**. High-grade and glandular results drive referral.

> [!warning] **LBC advantages and its one real trade-off.** Fewer unsatisfactory specimens than the conventional smear, and the residual sample can be used for HPV and other molecular testing without recalling the patient. Against that, **cytology is a morphological interpretation and remains subject to sampling and reader error** — its sensitivity for a single test is materially lower than that of HPV testing, which is exactly why HPV became the primary test.

> [!danger] **Do not ignore**
> - **A negative cytology in an HPV 16/18-positive patient does not avoid colposcopy.** The genotype drives the referral.
> - **Glandular abnormalities are under-detected by cytology** and carry a higher risk of significant pathology — never watch and wait on one.
> - **Cytology is not a test for endometrial cancer.** Endometrial cells reported in a postmenopausal woman are an incidental finding that requires separate investigation, not reassurance.

**Normal/abnormal:** As the reporting categories above, plus specimen adequacy.

**Alt:** Colposcopy with **histology** — the diagnostic standard, since cytology only ever suggests; HPV genotyping; **p16/Ki-67 dual staining** as an alternative triage of HPV-positive samples (in research and some international programs, not the Australian NCSP pathway).

## 0.3 Genital / Cervical Swab Panel

**D:** A set of specimens taken to identify genital tract infection: a **NAAT** for *Chlamydia trachomatis* and *Neisseria gonorrhoeae* (self-collected vaginal swab, clinician-collected endocervical swab, or **first-void urine**); a **high vaginal swab** for microscopy, culture and susceptibility (candida, bacterial vaginosis, *Trichomonas*, group B streptococcus); an **endocervical swab for gonococcal culture** where susceptibility testing matters; and extragenital **throat and rectal** swabs where indicated by sexual history.

**Ind:** Vaginal discharge, dysuria, pelvic pain, dyspareunia, intermenstrual or postcoital bleeding; suspected **pelvic inflammatory disease**; contact tracing; asymptomatic screening in those at risk; pre-termination and pre-instrumentation screening; sexual assault (with forensic requirements taking precedence — see [[NEW_Safeguarding_and_Forensic]]).

**Role:** Identifies treatable and notifiable infection, and — critically — **identifies partners who need treatment**.

> [!info] **Which swab answers which question**
> - **Chlamydia and gonorrhoea → NAAT.** Australian laboratories generally run these as a **duplex assay**, so a request for chlamydia will also detect gonococci.
> - **A self-collected vaginal swab is not inferior for NAAT** — sources agree it performs comparably to clinician-collected sampling and it substantially improves uptake.
> - **Candida, bacterial vaginosis and *Trichomonas* → high vaginal swab** with microscopy; these are not on the standard NAAT.
> - **Gonococcal *culture* is still needed** where susceptibility is required (treatment failure, resistance surveillance) — NAAT gives no susceptibility.
> - ***Mycoplasma genitalium*:** associated with cervicitis and PID, **but asymptomatic screening is not recommended** — test only when clinically indicated, because macrolide resistance is high and detection in an asymptomatic person leads to poorly justified treatment.

> [!danger] **Do not ignore**
> - **Do not wait for results in suspected PID.** PID is a **clinical diagnosis** and empirical antibiotic treatment starts immediately — delay costs fertility. Take the swabs, then treat. See [[17_05_PID__Endometriosis__Fibroids]].
> - **Always do a pregnancy test** in a woman of reproductive age with pelvic pain. **Ectopic pregnancy presents as PID** and this mistake is fatal.
> - **Chlamydia and gonorrhoea are notifiable** in all Australian jurisdictions, and **contact tracing is part of the treatment**, not an optional extra.
> - **Offer the rest of the STI screen** — HIV, syphilis serology, hepatitis B and C — since co-infection is common and the patient is already in front of you.
> - **Extragenital sites are missed by genital sampling alone**; pharyngeal and rectal infection is frequently asymptomatic and is only found if swabbed.

**Normal/abnormal:** Organism detected or not detected (NAAT); organism grown with susceptibilities (culture); microscopy findings including clue cells, motile trichomonads and yeast.

**Alt:** First-void urine NAAT (convenient, and the specimen of choice in men); bedside vaginal pH and wet mount; pelvic ultrasound where a tubo-ovarian abscess or other structural cause is suspected; laparoscopy in diagnostic uncertainty. See [[08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs]].

## 0.4 Hormone Panel (Gynaecological / Reproductive)

**D:** A grouped set of serum measurements used to work up menstrual disturbance, hyperandrogenism and subfertility: **FSH, LH, oestradiol, prolactin, TSH**, **total testosterone with SHBG** (allowing a calculated free androgen index), **DHEAS**, **17-hydroxyprogesterone**, **mid-luteal progesterone**, and **AMH**.

**Ind:** **Amenorrhoea or oligomenorrhoea**; suspected **PCOS**; hirsutism or virilisation; galactorrhoea; suspected premature ovarian insufficiency; subfertility work-up; suspected menopause where the diagnosis is genuinely in doubt.

**Role:** Localises the problem in the **hypothalamic–pituitary–ovarian axis**, and separates the small number of dangerous causes from the common benign ones.

> [!warning] **Timing is what makes or breaks this panel**
> - **FSH, LH and oestradiol are taken in the early follicular phase — day 2–5** — because levels swing across the cycle and a mid-cycle sample is uninterpretable.
> - **Where periods are absent or very irregular, take them on any day** — there is no cycle to time to, and waiting for "day 3" in an amenorrhoeic patient wastes months.
> - **Mid-luteal progesterone (about 7 days before the expected period) is the ovulation test** — it must be timed to the individual cycle, not fixed at "day 21", which is only correct in a 28-day cycle.
> - **AMH is cycle-independent** and reflects **ovarian reserve** — it predicts response to ovarian stimulation. **It is not a fertility test and must not be used to reassure or alarm a woman about her chance of conceiving naturally.**

> [!danger] **Do not ignore**
> - **Do a pregnancy test first.** Pregnancy is the commonest cause of secondary amenorrhoea and no hormone panel substitutes for βhCG.
> - **Markedly raised prolactin needs a pituitary MRI** — and check whether the patient is on an **antipsychotic, metoclopramide or another dopamine antagonist** before imaging, since drug-induced hyperprolactinaemia is common. **Macroprolactin** is a laboratory artefact that produces a spuriously high result and should be excluded before a work-up is built on the number.
> - **Rapid-onset hirsutism with virilisation** (voice deepening, clitoromegaly, male-pattern balding) and a **markedly raised testosterone** suggests an **androgen-secreting ovarian or adrenal tumour** — urgent, and a different pathway from PCOS.
> - **Raised FSH with low oestradiol under age 40** is **premature ovarian insufficiency** — it needs confirmation on a repeat sample, karyotype and fragile X testing, bone protection and hormone therapy, and careful counselling. Do not diagnose it on one result.
> - **PCOS is a diagnosis of exclusion built on defined criteria** — hyperandrogenism, ovulatory dysfunction and polycystic ovarian morphology — and **an LH:FSH ratio is not diagnostic** and is no longer part of the criteria. See [[17_01_FGM__Amenorrhoea__PCOS]].

**Normal/abnormal:** **Reference intervals are assay- and phase-specific and are deliberately not reproduced here** — every value must be read against the laboratory's own range **for the stated cycle phase**, and against the menopausal status. Interpreting these numbers without the phase is meaningless.

**Alt:** **Urine or serum βhCG first, always**; TSH and coeliac serology in menstrual disturbance; pelvic **ultrasound** for ovarian morphology, endometrial thickness and structural pathology; DEXA in prolonged hypo-oestrogenism; pituitary MRI; karyotype and fragile X in premature ovarian insufficiency; semen analysis in the couple's subfertility work-up. See [[17_06_Subfertility_and_OHSS]].

## 0.5 Prenatal Screening Panel

**D:** Two competing first-line strategies for **screening** (not diagnosing) fetal chromosomal abnormality. **Combined first trimester screening (cFTS)** — **nuchal translucency ultrasound at 11+0 to 13+6 weeks** plus maternal serum **PAPP-A** and **free βhCG**, combined with maternal age into a risk figure. **NIPT / cfDNA** — analysis of placentally derived cell-free DNA in maternal blood from about 10 weeks. **Second-trimester maternal serum screening** is the fallback where the first-trimester window has been missed.

**Ind:** Offered to **all pregnant women**, with informed consent and after discussion of what the results can and cannot do. NIPT is not currently Medicare-funded in Australia and is paid for out of pocket — a real access issue that should be part of the counselling.

**Role:** Estimates risk for **trisomy 21, 18 and 13** (and, on NIPT, sex chromosome aneuploidies and some microdeletions). **Neither test diagnoses anything.**

> [!info] **Performance — and why NIPT has not simply replaced cFTS**
> - **cFTS** detects roughly **90% of trisomy 21** at a false-positive rate of about **3–5%**.
> - **NIPT** has a substantially higher detection rate and much lower false-positive rate for trisomy 21.
> - **But cFTS includes an ultrasound**, and the nuchal translucency and the 11–13 week scan detect **structural abnormality, multiple pregnancy, incorrect dating and early-onset pre-eclampsia risk markers** that a blood test cannot. **An increased NT with a normal karyotype still matters** — it is associated with congenital heart disease and other structural anomalies and prompts fetal echocardiography.

> [!danger] **A positive NIPT is a screening result and must be confirmed by CVS or amniocentesis before any irreversible decision.**
> The positive predictive value depends heavily on the **prior probability** — for rarer conditions and in younger women it can be low, so a "positive" result is frequently a false positive. Causes of discordance include **confined placental mosaicism** (NIPT samples placenta, not fetus), **vanishing twin**, and **maternal** chromosomal abnormality or occult malignancy. **No termination should ever follow an unconfirmed NIPT result.**

> [!warning] **Other limitations**
> - **A "no-call" / failed NIPT is not a normal result** — it is associated with low fetal fraction, higher maternal BMI, early gestation and, importantly, an **increased risk of aneuploidy**. It requires review, not simple repetition.
> - **NIPT does not screen for structural abnormality** — the **18–20 week morphology scan** does, and remains essential whatever the screening result.
> - **Neural tube defects** are detected by ultrasound (and historically by maternal serum AFP), not by NIPT.
> - Screening is **optional**. Declining is a legitimate choice, and the counselling must make clear what would be done with a positive result.

**Normal/abnormal:** cFTS reports a **numerical risk** against a stated cut-off (increased vs low risk). NIPT reports **low risk / high risk / no result** for each condition tested. Neither is a diagnosis.

**Alt:** **CVS** (0.6) and **amniocentesis** (0.7) — the diagnostic tests; second-trimester serum screening; **18–20 week morphology ultrasound**; carrier screening for recessive conditions; detailed fetal echocardiography where NT is increased. See [[16_01-05_Antenatal_Care]].

## 0.6 Chorionic Villus Sampling (CVS)

**D:** Ultrasound-guided aspiration of **placental (chorionic villus) tissue**, transabdominally or transcervically, for karyotype, microarray or targeted gene testing.

**Ind:** A **high-risk screening result** (cFTS or NIPT); a **previous affected pregnancy** or known parental balanced translocation; a **familial single-gene disorder** where an early diagnosis is wanted; abnormal early ultrasound findings.

**Role:** The **first-trimester diagnostic** option — its whole advantage over amniocentesis is **timing**. A result several weeks earlier allows an earlier, safer and more private termination if that is the couple's decision.

> [!warning] **Performed from 11 weeks — and the gestational limit is not arbitrary.** Sources are consistent that **CVS before 10 weeks was associated with limb reduction defects**, with the excess risk falling steeply from 9 weeks and approaching background at 11 weeks and beyond. Registry data on CVS performed at **10 weeks or later show no increased risk**. This is why the procedure is not done earlier, and it is a genuinely examinable historical point.

> [!danger] **Confined placental mosaicism is the characteristic pitfall of CVS.**
> CVS samples **placenta, not fetus**. Mosaicism is found in roughly **1–2%** of CVS samples (compared with about **0.25%** of amniocenteses), and in most of those the abnormality is **confined to the placenta** — sources report the fetus is involved in only around **10%** of such cases. **An ambiguous CVS result therefore usually requires a follow-up amniocentesis** to establish the fetal genotype. Confined placental mosaicism itself is not entirely benign: it is associated with fetal growth restriction, preterm birth and low birth weight.

> [!danger] **Do not ignore**
> - **Anti-D prophylaxis is required for RhD-negative women** after CVS, as after any invasive uterine procedure — this is a routinely missed step. See 0.9.
> - **Procedure-related pregnancy loss** — quote as "small" in counselling. **A single numeric figure is deliberately not stated:** retrieved values ranged widely, and contemporary cohorts report loss rates comparable to unsampled pregnancies. Use your fetal medicine unit's audited local figure, which is what the woman is actually consenting to.
> - **CVS cannot detect neural tube defects** (no amniotic fluid AFP is obtained) — those need the morphology scan.
> - The decision belongs to the woman. The role of the intern is accurate information and referral to a fetal medicine unit and genetic counselling, not persuasion in either direction.

**Normal/abnormal:** Rapid aneuploidy testing (FISH/QF-PCR) within days, with full karyotype or microarray following. Mosaic or discordant results require amniocentesis.

**Alt:** **Amniocentesis** (later, but samples fetal cells directly); **NIPT** where the indication is screening rather than diagnosis; declining testing.

## 0.7 Amniocentesis

**D:** Ultrasound-guided transabdominal aspiration of **amniotic fluid**, containing desquamated fetal cells, for karyotype, microarray, single-gene testing, infection PCR, or biochemical analysis.

**Ind:** Diagnostic confirmation after a high-risk screening result or an abnormal CVS; abnormal ultrasound findings; suspected **congenital infection** (e.g. CMV, toxoplasmosis PCR on amniotic fluid); assessment of **fetal anaemia or haemolytic disease** in some settings; therapeutic **amnioreduction** in severe polyhydramnios; historically, fetal lung maturity testing (now essentially obsolete).

**Role:** The **second-trimester diagnostic standard**, performed from **15 weeks**. Later than CVS, but it samples **fetal cells directly** and is therefore not subject to confined placental mosaicism — sources report amniocentesis predicts the true fetal genotype in **93–100%** of cases where placental mosaicism was found on CVS.

> [!warning] **Not before 15 weeks.** Early amniocentesis was associated with a higher rate of pregnancy loss and with **talipes equinovarus**, and has been abandoned. If a diagnosis is needed earlier, the procedure is CVS.

> [!danger] **Do not ignore**
> - **Anti-D prophylaxis for RhD-negative women** — again, routinely forgotten.
> - **Procedure-related loss is small.** One quoted figure is a **total fetal loss rate of about 0.6% within 14 days**, but the *attributable* excess over background is smaller and contested. **A single counselling figure is not asserted here** — use your unit's audited rate.
> - **Advise the woman what to report afterwards**: persistent leaking of fluid, bleeding, contractions, fever. Amniotic fluid leak after the procedure often seals, but must be assessed.
> - **A normal karyotype or microarray does not guarantee a normal baby.** It excludes the conditions tested for, nothing more. Saying otherwise is the commonest counselling error.
> - **Culture failure and maternal cell contamination** are recognised technical failures; results are interpreted with that in mind.

**Normal/abnormal:** Rapid aneuploidy result (FISH/QF-PCR) in 1–2 days; full karyotype or microarray in 1–2 weeks; PCR for infection as requested.

**Alt:** **CVS** where an earlier answer is needed; **NIPT** for screening; **cordocentesis** (0.8) where fetal blood specifically is required; detailed ultrasound and fetal MRI for structural questions.

## 0.8 Cordocentesis (Percutaneous Umbilical Blood Sampling, PUBS)

**D:** Ultrasound-guided needle sampling of the **umbilical vein**, usually at the placental cord insertion, to obtain **fetal blood**.

**Ind:** **Suspected fetal anaemia — the principal indication** (red cell alloimmunisation, parvovirus B19 infection, fetomaternal haemorrhage), where it is both diagnostic and the route for **intrauterine transfusion**. Also: fetal thrombocytopenia (alloimmune), rapid karyotype where an urgent answer is needed late in pregnancy, congenital infection, and some metabolic and haematological disorders.

**Role:** A **highly specialised fetal medicine procedure** — an intern will never perform one, but must recognise the situations that generate the referral. **It has largely been displaced for diagnosis** by non-invasive alternatives, and its main contemporary role is as the **access route for fetal transfusion**.

> [!warning] **Middle cerebral artery peak systolic velocity Doppler has replaced it for the detection of fetal anaemia.** MCA-PSV is non-invasive, repeatable and accurate, so cordocentesis is now generally reserved for the point at which the Doppler indicates that **transfusion** is required — sampling and transfusing in the same procedure.

> [!danger] **Do not ignore**
> - **The highest procedure risk of the three invasive tests.** Sources describe procedure-related complications in the order of **1–2%**, with **higher loss rates when performed early** — one series reports up to **4%** before 20 weeks, and higher complication rates before 17 weeks. It is done **from about 18 weeks** for this reason.
> - **Anti-D for RhD-negative women**, and cordocentesis carries a particular risk of **worsening alloimmunisation** through fetomaternal haemorrhage — a real consideration in exactly the population being sampled.
> - Other complications: **cord haematoma, fetal bradycardia, bleeding from the puncture site, chorioamnionitis, preterm labour**. Performed only where **immediate delivery is possible** if the fetus deteriorates.
> - **Rh alloimmunisation is preventable.** The reason a fetus needs this procedure is often a missed anti-D dose earlier in this or a previous pregnancy. See [[16_08-09_Antenatal_and_Perinatal_Problems]].

**Normal/abnormal:** Fetal haemoglobin, haematocrit, platelet count, blood group and direct antiglobulin test, karyotype, infection PCR — interpreted against **gestation-specific** fetal reference ranges, which differ substantially from adult and neonatal values.

**Alt:** **MCA peak systolic velocity Doppler** — first-line for fetal anaemia; **amniocentesis** for karyotype and infection; **NIPT** for fetal RhD genotyping in an alloimmunised pregnancy; maternal antibody titres for surveillance.

## 0.9 Kleihauer-Betke Test (Fetomaternal Haemorrhage Quantification)

**D:** An acid-elution stain of a maternal blood film: adult haemoglobin is eluted from maternal cells while **fetal haemoglobin resists**, so fetal cells stand out and can be counted as a proportion of maternal cells, giving an estimated **volume of fetomaternal haemorrhage**.

**Ind:** In an **RhD-negative** woman, after any **potentially sensitising event** — abdominal trauma (including minor trauma and motor vehicle accidents), antepartum haemorrhage, external cephalic version, invasive procedures, and **routinely after delivery**. Also used in any pregnancy to quantify suspected **large fetomaternal haemorrhage** presenting as reduced fetal movements, a sinusoidal CTG or unexplained stillbirth — **an indication that is independent of blood group** and is easily missed.

**Role:** **It does not decide whether to give anti-D — it decides how much.** The standard dose is given on the clinical event; the Kleihauer determines whether that dose was sufficient.

> [!info] **How the result translates into dose (Australian practice)**
> Sources agree that the standard **postpartum dose of 625 IU RhD immunoglobulin covers a fetomaternal haemorrhage of about 6 mL of fetal red cells**, and that **additional RhD immunoglobulin is required where the FMH exceeds that**, dosed at approximately **100 IU per additional mL of fetal red cells**. Sources note that FMH exceeds the standard dose in **up to 3% of deliveries** — which is the entire justification for testing routinely rather than assuming.

> [!danger] **Do not ignore**
> - **Give anti-D within 72 hours of the sensitising event. Do not wait for the Kleihauer result.** Give the standard dose first and top up on the result. This is the single most important operational point, and delay is how women become sensitised.
> - **Take the maternal sample before giving anti-D**, and take it at least 15 minutes to an hour after the event so fetal cells have distributed.
> - **Anti-D is still indicated in an RhD-negative woman even if the Kleihauer is negative** after a sensitising event — a negative test does not exclude a small immunising bleed.
> - **False positives** occur where maternal **F-cells** are increased — **haemoglobinopathies (thalassaemia, sickle cell trait), hereditary persistence of fetal haemoglobin**, and normal pregnancy itself. **Flow cytometry** is more accurate and reproducible and is used where the Kleihauer is high or the mother has a haemoglobinopathy.
> - **The test is operator-dependent** with significant interobserver variability — an unexpectedly large result should be confirmed, not acted on blindly.
> - **A massive fetomaternal haemorrhage is an obstetric emergency** regardless of blood group: the fetus may be profoundly anaemic and need urgent delivery or transfusion.

**Normal/abnormal:** Reported as fetal cells per total cells and as an **estimated volume of fetal blood or fetal red cells** — check which your laboratory reports, because **whole blood and packed red cell volumes differ by roughly a factor of two** and confusing them mis-doses the anti-D.

**Alt:** **Flow cytometry** for fetal red cells or HbF — more accurate, the preferred method where available; maternal antibody screen and group and hold; fetal MCA Doppler and CTG where significant haemorrhage is suspected.

## 0.10 Ferning Test and Nitrazine Test (Confirming Rupture of Membranes)

**D:** Two bedside tests on fluid taken from the **posterior vaginal fornix at sterile speculum examination**. **Ferning:** fluid is spread on a glass slide and air-dried for at least 10 minutes; amniotic fluid crystallises into a **fine, delicate fern (arborisation) pattern** under the microscope, distinct from the coarse arborisation of cervical mucus. **Nitrazine:** pH-indicator paper changes colour in an alkaline sample — **normal vaginal secretions are pH ~4.5–6.0, amniotic fluid ~7.1–7.3**.

**Ind:** Suspected **prelabour rupture of membranes (PROM)** or **preterm PROM (PPROM)** — a history of a gush or continued leaking of fluid — where the diagnosis is not obvious on inspection.

**Role:** Confirmatory bedside adjuncts. **Visible pooling of amniotic fluid in the posterior fornix at sterile speculum examination is diagnostic and needs no further test**; these tests are for the equivocal case.

> [!danger] **DIGITAL VAGINAL EXAMINATION IS CONTRAINDICATED in suspected PPROM.**
> It introduces infection, shortens the latency to delivery and adds nothing that a sterile speculum examination does not give. **Sterile speculum only.** This is the highest-yield single fact in this entry.

> [!warning] **Both tests are unreliable in exactly the circumstances in which they are used**
> - **Nitrazine false positives** — **blood, semen, alkaline antiseptics, bacterial vaginosis**, urine, and cervical mucus. All are common in a woman presenting in possible labour.
> - **Ferning false positives** — cervical mucus (particularly around ovulation) and semen. **False negatives** — a dry, scanty or blood-contaminated sample, or insufficient drying time.
> - Reported accuracies (roughly 84–100% for ferning and 87–97% for nitrazine) come from selected populations and **overstate real-world performance**.
> - **A negative test does not exclude ruptured membranes.** With a convincing history, manage as PROM and observe — the clinical history outranks the bedside test.

> [!danger] **Do not ignore**
> - **Confirm gestation and fetal wellbeing**, and check the **group B streptococcus** status. PPROM management — corticosteroids for fetal lung maturation, latency antibiotics, magnesium sulfate for neuroprotection at early gestations, and decisions about timing of delivery — is gestation-dependent and specialist-led.
> - **Look for chorioamnionitis**: maternal fever, tachycardia, fetal tachycardia, uterine tenderness, offensive discharge. Suspected chorioamnionitis means **antibiotics and delivery**, not expectant management.
> - **Cord prolapse** is the immediate danger with ruptured membranes and a high presenting part — check the fetal heart rate promptly.
> - See [[16_10-13_Labour_and_Delivery]].

**Normal/abnormal:** Ferning present/absent; nitrazine paper colour change indicating alkaline pH. Interpret both alongside history, pooling and ultrasound liquor volume.

**Alt:** **Direct visualisation of pooling** (the best evidence); **ultrasound assessment of amniotic fluid volume** (reduced liquor supports the diagnosis but does not confirm it); commercial immunoassays for **placental alpha-microglobulin-1 (PAMG-1)** or IGFBP-1 in cervicovaginal fluid, which are more specific than the bedside tests and unaffected by semen and blood in the way nitrazine is.

## 0.11 Fetal Fibronectin (fFN)

**D:** An immunoassay on a **cervicovaginal swab from the posterior fornix**, detecting fetal fibronectin — a glycoprotein at the choriodecidual interface. It is normally present before about 22 weeks and after about 35 weeks; its appearance in between suggests disruption of that interface.

**Ind:** **Symptomatic threatened preterm labour between roughly 22–24 and 34 weeks** — contractions with an intact cervix, where the question is whether this woman will actually deliver.

**Role:** **A rule-out test.** Its value is its **negative predictive value**, which sources report as very high — approaching 100% for delivery within 7 days. A negative result allows a woman to avoid transfer, admission, steroids and tocolysis. **A positive result is a much weaker predictor** — most fFN-positive women do not deliver preterm — so it should not by itself trigger intervention.

> [!warning] **Sample before anything else touches the cervix, and know what corrupts the result**
> - **Speculum lubricant causes false negatives** — use water only.
> - **Take the swab before digital examination and before transvaginal ultrasound.**
> - **Intercourse within 24 hours and blood in the sample cause false positives** (fFN is present in semen and in plasma). Notably, sources hold that a **negative** result remains valid even with blood or recent intercourse — the contamination pushes towards false positive, not false negative.
> - **Do not perform the test at all** where there is **ruptured membranes, cervical dilatation beyond about 3 cm, moderate or gross vaginal bleeding, placenta praevia or suspected abruption.** Those are clinical situations that need management, not a probability estimate.

> [!danger] **Do not ignore**
> - **A negative fFN does not override a woman who is in labour.** If the cervix is changing, she is in preterm labour whatever the test says.
> - **Do not delay corticosteroids in genuine preterm labour to wait for the result** — the fetal benefit of antenatal steroids depends on timing.
> - **The test predicts timing, not cause.** It says nothing about infection, abruption or growth restriction, which must be assessed separately.
> - **In-utero transfer to a centre with appropriate neonatal facilities is safer than transferring a preterm neonate.** A positive result in a woman remote from such a centre should lower the threshold to transfer.

**Normal/abnormal:** Qualitative bedside assays report positive/negative against a **50 ng/mL** threshold; quantitative assays report a concentration allowing graded risk. **Interpretation is confined to the 22–34 week window** — outside it the test is not informative.

**Alt:** **Transvaginal cervical length ultrasound** — used alone or combined with fFN, and a short cervix is the stronger structural predictor; serial clinical assessment; CTG and infection screen; assessment for the underlying cause.

## 0.12 Biophysical Profile (BPP)

**D:** An ultrasound-based assessment of fetal wellbeing scoring **five components 2 or 0** each, to a total of **10**: **fetal breathing movements**, **gross body movement**, **fetal tone**, **amniotic fluid volume**, and the **non-stress test (CTG)**. A **modified BPP** uses only the two most informative components — **NST plus amniotic fluid volume**.

**Ind:** **Abnormal or equivocal CTG**; reduced fetal movements; suspected **fetal growth restriction**; post-dates pregnancy; maternal conditions increasing the risk of placental insufficiency (hypertension, pre-eclampsia, diabetes, antiphospholipid syndrome, cholestasis); oligohydramnios.

**Role:** Assesses fetal wellbeing across **different timescales**. The acute markers — **breathing, movement, tone and the NST** — reflect current oxygenation; **amniotic fluid volume** reflects **chronic** placental function, because a chronically hypoxic fetus shunts blood away from the kidneys and produces less urine.

> [!info] **Component definitions and scoring**
> Sources agree on: **breathing** — one or more episodes of rhythmic breathing lasting ≥30 seconds within 30 minutes; **movement** — three or more discrete body or limb movements within 30 minutes; **tone** — one or more episodes of extension of a limb with return to flexion, or opening/closing of a hand; **amniotic fluid** — a single vertical pocket **exceeding 2 cm**; **NST** — reactive.
> **Score 8–10 = reassuring · 6 = equivocal, repeat or deliver depending on gestation · ≤4 = strongly suggests fetal compromise and generally means delivery.**

> [!danger] **The exception that overrides the score: oligohydramnios.**
> Sources are explicit that **8/10 is normal only if the amniotic fluid component scored 2**. **A score of 8/10 achieved by losing the fluid point is NOT reassuring** and requires further evaluation and usually delivery, whatever the composite number says. **Look at which point was lost, not just the total.** This is the trap the number is designed to hide.

> [!warning] **Interpretation depends on gestation and on maternal state**
> - **Prematurity** reduces the score legitimately — breathing movements and reactivity are less developed. A modest score in a very preterm fetus is not the same finding as in a term fetus.
> - **Maternal sedatives, opioids, magnesium sulfate, corticosteroids, smoking and hypoglycaemia** all reduce fetal activity and can produce a falsely low score.
> - **Fetal sleep cycles** last up to 40 minutes; the test should be observed long enough before concluding.

> [!danger] **Do not ignore**
> - **The BPP is a snapshot with a false-negative rate**, and a reassuring score **does not license ignoring the mother.** Persistently reduced fetal movements warrant repeat assessment and escalation whatever the last score was.
> - **A score of 0–2 is an emergency** — expedite delivery.
> - **The BPP does not replace umbilical artery Doppler in suspected growth restriction**; Doppler detects placental insufficiency earlier and drives surveillance and timing.
> - See [[16_08-09_Antenatal_and_Perinatal_Problems]].

**Normal/abnormal:** As the score bands above, always read together with gestation, the individual component lost, the growth trajectory and the Doppler studies.

**Alt:** **CTG / non-stress test** alone; **umbilical artery, MCA and ductus venosus Doppler**; serial **growth scans**; contraction stress test (rarely used in Australia); maternal monitoring of fetal movements.

---

## Build status

| # | Item | Built | Notes |
|---|---|---|---|
| 0.1 | Cervical Screening Abnormality | yes | Built as the Cervical Screening Test and its management pathway. |
| 0.2 | Liquid Cytology | yes | |
| 0.3 | Genital / Cervical Swab Panel | yes | |
| 0.4 | Hormone Panel | yes | Reference intervals omitted — assay- and cycle-phase-specific. |
| 0.5 | Prenatal Screening Panel | yes | |
| 0.6 | Chorionic Villus Sampling | yes | Single procedure-loss figure omitted — retrieved values ranged widely. |
| 0.7 | Amniocentesis | yes | As above; the 0.6% 14-day total loss figure is quoted with its limitation stated. |
| 0.8 | Cordocentesis | yes | |
| 0.9 | Kleihauer-Betke Test | yes | |
| 0.10 | Ferning Test | yes | Built jointly with Nitrazine as one PROM entry — the two are performed on the same specimen at the same examination and are not separable clinically. |
| 0.10 | Nitrazine Test | yes | As above. |
| 0.11 | Fetal Fibronectin | yes | |
| 0.12 | Biophysical Profile | yes | |
| — | C-Spine X-Ray | **deferred** | **Miscategorised** in the build list under Gynaecology. It is an orthopaedic/trauma imaging study — deferred to `NEW_Investigations_Orthopaedics_Neurology_and_Other.md` (Part A file 11). |
| — | Compression Test | **deferred** | **Miscategorised** under Gynaecology. This is the cervical **Spurling compression** exam manoeuvre — deferred to `NEW_Exam_Manoeuvres_and_Procedures.md` (Part B file 12). |
| — | Distraction Test | **deferred** | **Miscategorised** under Gynaecology. Cervical **distraction** exam manoeuvre — deferred to Part B file 12 with Compression Test. |

**Items in file: 13 entries covering 13 build-list rows. Build-list O&G investigation rows: 16; 3 deferred as miscategorised, with destinations recorded above.**
