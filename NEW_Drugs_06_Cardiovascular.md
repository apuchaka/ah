---
block: NEW build — Drug Classes
source: data/BULK_BUILD_PLAN.md Part C; AMH section 6 Cardiovascular drugs
status: standalone — not yet cross-referenced into the corpus
---

# NEW — Drug Classes: Cardiovascular (AMH section 6, excluding antihypertensives)

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment. Entries are **snippet-sourced**, and **no doses are stated anywhere in this file.**

> [!info] **Scope, and one gap found and fixed.**
> The **Antihypertensives** subsection of AMH section 6 was built earlier in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`; this file covers the section's **other ten subsections**.
> **However, that earlier file did not build the beta-blockers** — the build list's `Beta-blockers`, `Beta-Blockers (Cardioselective)` and `Beta-Blockers (Non-selective)` rows sit under Antihypertensives and were missed. **That gap is fixed here at 0.7**, and it is recorded in the build status table rather than left for someone to discover.

---

## 0.1 Anticoagulants

> [!danger] **Anticoagulants are the drug class most often implicated in serious preventable inpatient harm.** Before prescribing any of them, ask: **indication, target duration, renal function, weight, bleeding risk, and what else the patient is on.** Then check whether there is a **procedure coming up**, and whether the patient is on an **antiplatelet as well** — "triple therapy" is sometimes correct but is never accidental.

### 0.1.1 Vitamin K Antagonists (Warfarin)
- **Mechanism:** inhibits **vitamin K epoxide reductase**, so the vitamin K-dependent factors **II, VII, IX and X** (and proteins C and S) cannot be γ-carboxylated. Takes **days** to work, because existing factors must first be cleared.
- **Indications:** **mechanical heart valves** and **antiphospholipid syndrome — the two settings where warfarin remains mandatory and DOACs are contraindicated**; severe renal impairment; atrial fibrillation and VTE where a DOAC is unsuitable, unaffordable or not tolerated; rheumatic mitral stenosis.
- **Monitoring:** **INR**, with a target range set by indication; time in therapeutic range is the quality measure.
- **Adverse effects:** **bleeding** (the dominant risk); **skin necrosis** early in treatment in protein C/S deficiency (the reason for heparin overlap when starting for acute thrombosis); purple toe syndrome; **teratogenic — warfarin embryopathy — so it is avoided in pregnancy**, particularly the first trimester (mechanical valves in pregnancy are a specialist balancing act).
- **Interactions — warfarin has more clinically significant interactions than almost any other drug:**
  - **Raise INR:** antibiotics (**metronidazole, macrolides, ciprofloxacin, co-trimoxazole**, most broad-spectrum agents), **azole antifungals including topical miconazole oral gel**, amiodarone, NSAIDs and aspirin (also direct bleeding risk), SSRIs, statins, thyroxine, alcohol binges, **cranberry juice**.
  - **Lower INR:** **rifampicin, carbamazepine, phenytoin, St John's wort**, and a sudden **increase in dietary vitamin K** (green leafy vegetables — the message is *consistency*, not avoidance).
  - **Any acute illness, heart failure, or liver disease raises the INR.**
- **Practical:** **an INR must never be prescribed without a plan for who reviews it.** Patients need an INR booklet or app, education about consistent diet and about telling every prescriber they are on warfarin, and a clear point of contact.

> [!danger] **DOACs are CONTRAINDICATED in mechanical heart valves and in antiphospholipid syndrome.** Sources state both explicitly: mechanical valve thrombosis has occurred on rivaroxaban, and the only agents approved for mechanical valves are vitamin K antagonists; DOACs are listed as contraindicated in antiphospholipid syndrome for both VTE and AF indications. **A patient on warfarin for either indication must not be "modernised" onto a DOAC.**

### 0.1.2 Heparins (Unfractionated Heparin)
- **Mechanism:** binds **antithrombin**, accelerating its inactivation of **thrombin (IIa) and factor Xa** — unfractionated heparin is long enough to bridge antithrombin to thrombin, which is why it inhibits both.
- **Advantages that define its niche:** **short half-life, fully reversible with protamine, given intravenously, and cleared independently of the kidneys** — so it is the anticoagulant of choice in **severe renal impairment**, in patients at high bleeding risk, and where an urgent procedure may be needed.
- **Monitoring:** **APTT** (or anti-Xa) for therapeutic infusions, with a nomogram; **prophylactic subcutaneous dosing is not monitored**.
- **Adverse effects:** bleeding; **hyperkalaemia** (aldosterone suppression — genuinely common and often missed); osteoporosis with long-term use; and **HIT**.

> [!danger] **HEPARIN-INDUCED THROMBOCYTOPENIA (HIT) — a PROTHROMBOTIC emergency, not a bleeding one.**
> Immune-mediated, against **platelet factor 4–heparin complexes**. **The platelet count falls, but the patient CLOTS** — venous and arterial, sometimes catastrophically. Sources describe the **4Ts score**: **T**hrombocytopenia, **T**iming of the fall, **T**hrombosis, and absence of o**T**her causes, scored 0–8 with **0–3 low, 4–5 intermediate, 6–8 high probability**; intermediate or high scores warrant immunoassay and functional assay confirmation.
> **Timing is the classic clue: the platelet fall occurs 5–10 days after starting heparin, or within a day if there has been heparin exposure in the previous 30 days.**
> **Management: STOP ALL HEPARIN IMMEDIATELY — including flushes and heparin-coated lines — and start a NON-HEPARIN anticoagulant** (sources name **argatroban, danaparoid, bivalirudin or fondaparinux**; DOACs are increasingly used and appear not to stimulate HIT antibodies). **Do NOT simply stop anticoagulation** — the thrombotic risk persists for weeks. **Do NOT give warfarin alone during acute HIT** (risk of venous limb gangrene and skin necrosis), and sources note the bleeding risk of overlapping argatroban with warfarin. **Do NOT transfuse platelets routinely.** Label the allergy and tell the patient.

### 0.1.3 Low Molecular Weight Heparins
- **Key agents:** **enoxaparin**, dalteparin; and **fondaparinux** (a pure synthetic factor Xa inhibitor, grouped here in practice).
- **Mechanism:** shorter chains — enough to catalyse **anti-Xa** activity but mostly too short to bridge to thrombin, so the action is **predominantly anti-Xa**.
- **Advantages over unfractionated heparin:** **predictable pharmacokinetics** (so routine monitoring is unnecessary), **once- or twice-daily subcutaneous dosing**, **lower risk of HIT**, and outpatient use.
- **Indications:** VTE prophylaxis and treatment, ACS, bridging, and **the anticoagulant of choice in pregnancy** (it does not cross the placenta).
- **The limitations that matter:**
  - **Renally cleared** — **accumulates in renal impairment**, requiring dose reduction or a switch to unfractionated heparin. **Check the eGFR before prescribing enoxaparin**, particularly in the elderly.
  - **Dose by weight** — and both extremes matter: under-dosing in obesity and over-dosing in low body weight.
  - **Only partially reversed by protamine.**
  - **Anti-Xa monitoring** is reserved for pregnancy, extremes of weight, and renal impairment.
- **Spinal/epidural point:** **strict timing intervals apply between an LMWH dose and neuraxial anaesthesia or catheter removal** — spinal haematoma causes permanent paraplegia. Follow the anaesthetic protocol exactly.

### 0.1.4 Direct Thrombin Inhibitors
- **Key agents:** **dabigatran** (oral); **argatroban** and **bivalirudin** (parenteral, used in HIT and in PCI).
- **Mechanism:** bind thrombin directly, independent of antithrombin — so they also inhibit **clot-bound** thrombin, unlike heparins.
- **Dabigatran specifics:** **substantially renally cleared** (more so than the factor Xa inhibitors), so it is the DOAC most affected by renal impairment and the most likely to accumulate in acute kidney injury; causes **dyspepsia** in a significant minority; and the capsules **must not be removed from their blister packaging or crushed**.
- **Reversal:** **idarucizumab**, a monoclonal antibody fragment giving rapid, specific reversal — see 0.2.
- **Argatroban** — hepatically cleared, so it is the agent of choice in HIT with renal failure; it **prolongs the INR**, which complicates transition to warfarin.

### 0.1.5 Factor Xa Inhibitors
- **Key agents:** **apixaban, rivaroxaban, edoxaban** (oral); **fondaparinux** (parenteral, indirect via antithrombin).
- **Indications:** **non-valvular atrial fibrillation**, VTE treatment and prophylaxis, and post-operative thromboprophylaxis.
- **Advantages over warfarin:** **no routine monitoring, fewer food and drug interactions, fixed dosing, faster onset and offset**, and (for most) **lower intracranial haemorrhage** rates.
- **The practical points that cause errors:**
  - **Dosing differs by indication and by phase** — VTE treatment regimens have a **higher loading period** followed by a maintenance dose, and AF dosing is different again. **Check which indication and which phase.**
  - **Dose reduction criteria** exist based on **age, weight and renal function** and differ between agents — apply them, and re-check when renal function changes.
  - **Renal function must be checked before starting and monitored**; all are contraindicated below an agent-specific creatinine clearance.
  - **Rivaroxaban must be taken with food** at treatment doses, or absorption is unreliable.
  - **Adherence matters more than with warfarin**, because the anticoagulant effect disappears within a day — and there is no INR to reveal that doses are being missed.
- **Interactions:** combined **P-glycoprotein and strong CYP3A4** inhibitors (azoles, HIV protease inhibitors, some macrolides) raise levels; **rifampicin, carbamazepine, phenytoin and St John's wort** lower them and cause treatment failure.
- **Contraindications:** as above — **mechanical valves, antiphospholipid syndrome**, severe renal impairment, pregnancy and breastfeeding, and significant active bleeding.
- **Reversal:** **andexanet alfa** where available; otherwise **prothrombin complex concentrate** — see 0.2.

## 0.2 Drugs for Reversing Anticoagulation

| Anticoagulant | Reversal | Points |
|---|---|---|
| **Warfarin** | **Vitamin K** (oral or IV) ± **prothrombin complex concentrate (PCC)**; FFP only if PCC unavailable | **Vitamin K takes hours; PCC works in minutes.** The decision is driven by **bleeding severity first, INR second** — a high INR without bleeding is managed very differently from a bleeding patient. High-dose IV vitamin K makes re-anticoagulation difficult for days, which matters in a mechanical valve. |
| **Unfractionated heparin** | **Protamine** | Complete reversal; protamine itself causes hypotension, bradycardia and anaphylactoid reactions — give slowly. |
| **LMWH** | **Protamine (partial only)** | Reverses roughly 60% of the anti-Xa effect; there is no complete antidote. |
| **Dabigatran** | **Idarucizumab** | Rapid and specific. Dabigatran is also dialysable, unlike the Xa inhibitors. |
| **Apixaban / rivaroxaban / edoxaban** | **Andexanet alfa** where stocked; otherwise **PCC** | Know what your hospital actually holds — availability is not uniform. |
| **Thrombolytics** | **Tranexamic acid, cryoprecipitate/fibrinogen concentrate, FFP, platelets** | No specific antidote. |

> [!danger] **Reversal is not automatic, and the decision is a balance of two risks.**
> Reversing anticoagulation in a patient with a **mechanical valve, a recent stroke, or a fresh coronary stent** exposes them to catastrophic thrombosis. **Major or life-threatening bleeding, or emergency surgery, justifies it; a raised INR alone usually does not.** Alongside any reversal agent: **stop the anticoagulant, apply local haemostasis, resuscitate, transfuse, identify and treat the bleeding source, and correct temperature, calcium and acidosis.** Discuss with haematology, and **document a plan for when and whether anticoagulation restarts** — that plan is as important as the reversal and is frequently never made.

## 0.3 Antiplatelet Drugs

### 0.3.1 Antiplatelets — COX Inhibitors (Aspirin)
- **Mechanism:** **irreversibly** acetylates **COX-1**, abolishing platelet **thromboxane A₂** production for the platelet's whole lifespan (about 7–10 days) — because platelets have no nucleus and cannot resynthesise the enzyme. This is why the effect outlasts the drug and why cessation before surgery is measured in days.
- **Indications:** **secondary prevention** after myocardial infarction, stroke/TIA and peripheral arterial disease; acute coronary syndrome (a **chewed loading dose**); after stenting as part of dual therapy. **Primary prevention is now largely NOT recommended** — the bleeding harm offsets the modest benefit in most people without established disease.
- **Adverse effects:** **GI bleeding and dyspepsia** (dose-related; consider a PPI in at-risk patients); **bronchospasm in aspirin-exacerbated respiratory disease**; tinnitus at high dose; **Reye syndrome — aspirin is avoided in children under 16 with viral illness**, the exception being Kawasaki disease.
- **Interaction:** **ibuprofen taken shortly before aspirin blocks its antiplatelet effect** by competing for the COX-1 site — a real and under-recognised problem in patients self-medicating for arthritis.

### 0.3.2 Antiplatelets — P2Y12 Inhibitors (including Thienopyridines)
*(covers build-list classes: Antiplatelets (P2Y12 Inhibitors); Thienopyridines)*
- **Mechanism:** block the platelet **P2Y12 ADP receptor**, preventing ADP-mediated activation and GPIIb/IIIa expression.
- **Two chemical groups:**
  - **Thienopyridines — clopidogrel, prasugrel** (and ticlopidine, abandoned because of neutropenia and TTP). **Prodrugs**, binding **irreversibly**.
  - **Non-thienopyridine — ticagrelor** (and cangrelor, IV). **Not a prodrug**, binds **reversibly**.
- **Comparative evidence:** sources report that **American, Canadian and European ACS guidelines recommend ticagrelor or prasugrel over clopidogrel unless bleeding risk is high**, because they give **more consistent and faster platelet inhibition** and better ischaemic outcomes — at the cost of **more bleeding**. In patients aged **≥75**, one analysis found ticagrelor had a lower one-year MACE risk than clopidogrel **with no difference in major bleeding**.
- **Agent-specific points:**
  - **Clopidogrel is a prodrug requiring CYP2C19.** **Poor metabolisers get reduced antiplatelet effect**, and **omeprazole and esomeprazole inhibit CYP2C19** — pantoprazole is generally preferred when a PPI is needed with clopidogrel.
  - **Ticagrelor** — **twice-daily dosing** (adherence matters more), and two distinctive adverse effects: **dyspnoea** (usually transient, adenosine-mediated, and alarming if unexplained) and **bradyarrhythmia/ventricular pauses**. Avoid with strong CYP3A4 inhibitors and inducers.
  - **Prasugrel** — the most potent; **contraindicated after prior stroke or TIA**, and cautioned in those over 75 or under 60 kg, because of intracranial bleeding risk.
- **Duration:** sources describe **12 months of dual antiplatelet therapy with aspirin plus a potent P2Y12 inhibitor** as the guideline standard after ACS with a new-generation drug-eluting stent, shortened in high bleeding risk and sometimes extended in high ischaemic risk.

> [!danger] **NEVER stop dual antiplatelet therapy after a recent coronary stent without discussing it with cardiology.**
> Premature cessation causes **stent thrombosis**, which presents as ST-elevation myocardial infarction and carries a high mortality. This comes up constantly when a stented patient needs surgery, a dental procedure or an endoscopy — **the decision belongs to cardiology and the proceduralist together**, and "the surgeon said to stop it" is not a plan. Document the stent date and type.

### 0.3.3 Glycoprotein IIb/IIIa Inhibitors
- **Key agents:** **abciximab, eptifibatide, tirofiban** — intravenous only.
- **Mechanism:** block the **final common pathway** of platelet aggregation — the GPIIb/IIIa receptor that binds fibrinogen and cross-links platelets. The most complete platelet inhibition available.
- **Role:** now **narrow** — used in the catheter laboratory during PCI for high thrombus burden, no-reflow, or as bailout. Displaced from routine use by potent oral P2Y12 inhibitors.
- **Adverse effects:** **major bleeding**, and **profound acute thrombocytopenia** (which can occur within hours and requires urgent platelet count checking after starting).

### 0.3.4 Other Antiplatelet Drugs
- **Dipyridamole** — phosphodiesterase inhibition and adenosine reuptake blockade; used with aspirin in secondary stroke prevention. **Headache is common and dose-limiting.** Also used pharmacologically for cardiac stress testing (and is therefore withheld before it).
- **Cilostazol** — a PDE3 inhibitor with antiplatelet and vasodilator action, used in **intermittent claudication** (see 0.11.6). **Contraindicated in heart failure**, as with all PDE3 inhibitors.
- **Vorapaxar** — a PAR-1 (thrombin receptor) antagonist; contraindicated with any history of stroke, TIA or intracranial haemorrhage.

## 0.4 Thrombolytics
*(covers build-list class: Thrombolytics (Plasminogen Activators))*
- **Mechanism:** **plasminogen activators** — convert plasminogen to **plasmin**, which digests fibrin and lyses established thrombus.
- **Key agents:** **alteplase (tPA), tenecteplase, reteplase**; streptokinase (largely historical, antigenic, and cannot be repeated).
- **Indications:**
  - **Acute ischaemic stroke** within the licensed time window, after CT excludes haemorrhage and strict criteria are met — increasingly with **tenecteplase**, and alongside or superseded by **endovascular thrombectomy** for large vessel occlusion.
  - **STEMI** where **primary PCI is not available within the recommended time** — the situation in much of rural and remote Australia, where prehospital or regional thrombolysis followed by transfer is standard.
  - **Massive (haemodynamically unstable) pulmonary embolism**.
  - Selected acute limb ischaemia and occluded lines and grafts.
- **Adverse effects:** **major haemorrhage, and intracranial haemorrhage in particular** — the risk that defines the class; reperfusion arrhythmias; hypotension; angioedema (alteplase, more with concurrent ACE inhibitors); allergic reactions with streptokinase.
- **Contraindications** (broadly): any **intracranial haemorrhage ever**, recent ischaemic stroke, known intracranial neoplasm or vascular malformation, active bleeding or bleeding diathesis, recent major surgery or trauma, suspected aortic dissection, and severe uncontrolled hypertension. **Relative contraindications are numerous and the checklist must be worked through formally, not from memory.**

> [!danger] **In stroke, time is brain, and the CT comes first.** Thrombolysis **must not** be given before imaging excludes haemorrhage, and **blood pressure must be controlled to the protocol threshold before and after** — post-thrombolysis hypertension causes intracranial haemorrhage. **A deteriorating conscious state or new headache after thrombolysis means immediate CT and reversal measures.** See [[04_Neurology]].

## 0.5 Other Drugs Affecting Haemostasis
- **Tranexamic acid** — an **antifibrinolytic** that blocks lysine binding sites on plasminogen. Reduces mortality in **trauma with significant haemorrhage when given early**, reduces bleeding in **postpartum haemorrhage**, surgery, epistaxis and **menorrhagia** (a genuinely useful and under-used oral option in general practice). Caution in active thromboembolic disease; seizures at high doses; needs dose reduction in renal impairment. **Never inject it intrathecally — inadvertent intrathecal administration is fatal**, and syringe-swap errors have caused deaths.
- **Vitamin K (phytomenadione)** — warfarin reversal, obstructive jaundice and malabsorption, and **routine prophylaxis in the newborn to prevent haemorrhagic disease of the newborn** — a standing Australian practice that must be offered and documented. Intravenous administration can cause anaphylactoid reactions; give slowly and diluted.
- **Desmopressin (DDAVP)** — releases stored von Willebrand factor and factor VIII from endothelium; used in **mild haemophilia A, type 1 von Willebrand disease, and uraemic platelet dysfunction**. **Causes hyponatraemia through water retention — restrict fluids and monitor sodium**, especially in children and the elderly. See 0.11.4.
- **Clotting factor concentrates** — factor VIII and IX, **prothrombin complex concentrate**, fibrinogen concentrate, and **recombinant factor VIIa** (a haematologist's decision, with real thrombotic risk).
- **Protamine** — see 0.2.
- **Vitamin K antagonism, and blood products generally** — see [[10_08_Haemonc_-_Blood_Products_and_Transfusion]].

## 0.6 Drugs for Angina and Acute Coronary Syndromes

### 0.6.1 Nitrates
- **Mechanism:** metabolised to **nitric oxide**, activating guanylate cyclase → cGMP → smooth muscle relaxation. Predominantly **VENODILATION at usual doses**, reducing **preload** and therefore myocardial wall stress and oxygen demand; coronary vasodilation and reduced afterload at higher doses.
- **Key agents:** **glyceryl trinitrate** (sublingual spray/tablet, transdermal patch, IV infusion), **isosorbide mononitrate and dinitrate** (oral, for prophylaxis).
- **Indications:** **acute angina** (sublingual); angina prophylaxis; **acute pulmonary oedema and hypertensive emergency** (IV — where the preload reduction is the point); ACS with ongoing pain.
- **Adverse effects:** **headache** (very common, usually settles, and the reason patients stop — warn them and pre-empt with simple analgesia); **hypotension, flushing, dizziness, reflex tachycardia**.
- **TOLERANCE** develops rapidly with continuous exposure. **A nitrate-free interval of 8–12 hours daily is required** — patches are removed overnight, and asymmetric oral dosing is used. Continuous nitrate therapy stops working, and this is why patients on patches around the clock get no benefit.

> [!danger] **NITRATES + PDE5 INHIBITORS = PROFOUND, POTENTIALLY FATAL HYPOTENSION.**
> **Ask every man presenting with chest pain whether he has taken sildenafil, tadalafil or vardenafil**, and how long ago — the required interval is much longer for **tadalafil** because of its long half-life. This applies to recreational as well as prescribed use, and to nitrate-containing recreational inhalants ("poppers"). **The question must be asked directly, in private, before giving GTN.**

> [!danger] **Nitrates are contraindicated (or dangerous) in: right ventricular / inferior myocardial infarction** — a preload-dependent ventricle can crash with venodilation; **severe aortic stenosis** and **hypertrophic obstructive cardiomyopathy**; and any **hypotensive** patient. Check the ECG for inferior/right-sided involvement before reaching for GTN.

### 0.6.2 Other Antianginal Drugs
- **Beta-blockers** — first-line antianginal therapy (see 0.7): they reduce heart rate, contractility and therefore oxygen demand, and improve survival after MI.
- **Calcium channel blockers** — dihydropyridines for afterload reduction; **verapamil and diltiazem** where rate control is also wanted (but **never with a beta-blocker** — see 0.7).
- **Ivabradine** — inhibits the sinoatrial **I_f ("funny") current**, slowing the heart rate **without affecting contractility or blood pressure**. Useful in angina and heart failure where the heart rate remains high despite (or without) a beta-blocker. **Requires sinus rhythm** — it does nothing in atrial fibrillation. Causes **visual phosphenes** (transient bright patches), a distinctive and harmless effect that alarms patients if unexplained.
- **Nicorandil** — a potassium channel opener with a nitrate moiety; causes **painful, persistent oral, gastrointestinal, anal and skin ULCERATION** that is easily misdiagnosed as inflammatory bowel or malignant disease and resolves only on stopping the drug.
- **Perhexiline** — a metabolic modulator used in refractory angina, **largely an Australian phenomenon**: it requires **therapeutic drug monitoring** because CYP2D6 poor metabolisers develop **hepatotoxicity and peripheral neuropathy**.
- **Trimetazidine, ranolazine** — metabolic and late sodium current agents used in refractory angina.
- **And the interventions that matter most:** statin, antiplatelet, blood pressure control, **smoking cessation**, diabetes management, cardiac rehabilitation, and revascularisation where indicated. **Antianginals treat symptoms; the prognostic drugs are elsewhere.** See [[01_Cardiovascular]].

## 0.7 Beta-Blockers
*(build-list rows `Beta-blockers`, `Beta-Blockers (Cardioselective)` and `Beta-Blockers (Non-selective)` sit under the Antihypertensives subsection and were **not** built in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`. **Built here as a gap fix.**)*

- **Mechanism:** competitive antagonism at **β-adrenoceptors**. **β₁** predominates in the heart (rate, contractility, conduction, and renin release from the juxtaglomerular apparatus); **β₂** in bronchial and vascular smooth muscle, liver and skeletal muscle.
- **Indications:** **heart failure with reduced ejection fraction** (one of the four pillars — see 0.10.4); **post-myocardial infarction and stable angina** (prognostic and symptomatic); **rate control in atrial fibrillation and other tachyarrhythmias**; hypertension (no longer first-line in uncomplicated hypertension in Australian practice, but appropriate where there is a compelling comorbid indication); **thyrotoxicosis** (propranolol also blocks peripheral T4→T3 conversion); **essential tremor**, **migraine prophylaxis**, **portal hypertension and variceal bleeding prophylaxis** (non-selective), performance anxiety, and glaucoma (topical timolol).

### 0.7.1 Cardioselective (β₁-Selective) Beta-Blockers
- **Key agents:** **metoprolol, bisoprolol, atenolol, nebivolol** (which also has nitric-oxide-mediated vasodilation).
- **Why selectivity matters:** less β₂ blockade means **less bronchospasm, less peripheral vasoconstriction, and less masking of hypoglycaemia**. **Selectivity is relative and is LOST AT HIGHER DOSES** — a "cardioselective" beta-blocker at high dose behaves non-selectively, which is the point most often forgotten.
- **Practical:** **bisoprolol, metoprolol succinate (extended release), carvedilol and nebivolol are the agents with mortality evidence in heart failure** — they are not interchangeable with immediate-release metoprolol tartrate for that indication.

### 0.7.2 Non-Selective Beta-Blockers
- **Key agents:** **propranolol, sotalol, timolol, nadolol**; **carvedilol** and **labetalol** additionally block **α₁** (giving vasodilation, and making them useful in heart failure and in pregnancy respectively).
- **Specific roles:** **propranolol** — thyrotoxicosis, tremor, migraine, portal hypertension, infantile haemangioma; **sotalol** — also a class III antiarrhythmic (see 0.8.5), with the QT risk that entails; **labetalol** — hypertension in pregnancy and pre-eclampsia; **carvedilol** — heart failure.

### 0.7.3 Adverse Effects, Contraindications and the Warnings That Matter (both groups)
- **Adverse effects:** **bradycardia and heart block**; **hypotension**; **fatigue and exercise intolerance**; **cold peripheries and worsening of Raynaud phenomenon and claudication**; **sleep disturbance, vivid dreams and nightmares** (worse with lipophilic agents such as propranolol that cross into the CNS); erectile dysfunction; **bronchospasm**; **masking of hypoglycaemia awareness** and impaired glycogenolysis; dyslipidaemia.
- **Cautions and contraindications:** **severe asthma** (a **cardioselective** agent may be used with care where there is a strong indication — an absolute prohibition is no longer standard, but this is a considered decision, not a routine one); **second- or third-degree heart block without a pacemaker**; **decompensated heart failure** (they are started only when the patient is stable and euvolaemic, at low dose, and titrated slowly — **starting a beta-blocker in acute decompensation makes it worse**); severe peripheral arterial disease; **cocaine or amfetamine toxicity** (unopposed α-stimulation).

> [!danger] **NEVER combine a beta-blocker with intravenous verapamil or diltiazem** — the combination causes **profound bradycardia, complete heart block and asystole**. Even oral combination requires great caution and specialist input.

> [!danger] **DO NOT STOP A BETA-BLOCKER ABRUPTLY.** Chronic blockade upregulates β-receptors, so sudden withdrawal causes **rebound tachycardia, hypertension, angina, myocardial infarction and arrhythmia** — most dangerous in ischaemic heart disease. **Withdraw gradually over weeks**, and if a patient is nil by mouth or missing doses in hospital, find a route rather than simply omitting them.

> [!warning] **Beta-blocker overdose** causes bradycardia and refractory hypotension; **glucagon** is the specific measure, with high-dose insulin–euglycaemia therapy and vasopressors. See `NEW_Drugs_04_Antidotes_and_Antivenoms.md` 0.1.1.

## 0.8 Drugs for Arrhythmias

### 0.8.1 Antiarrhythmics — the Class Overview
- **Vaughan Williams classification:**
  - **Class I — sodium channel blockers**, subdivided by their effect on the action potential duration: **Ia** prolongs, **Ib** shortens, **Ic** has little effect.
  - **Class II — beta-blockers** (0.7).
  - **Class III — potassium channel blockers**, prolonging repolarisation and the QT.
  - **Class IV — non-dihydropyridine calcium channel blockers** (verapamil, diltiazem).
  - **Unclassified but essential:** **adenosine, digoxin, magnesium, atropine**.

> [!danger] **Every antiarrhythmic drug is also PROARRHYTHMIC.** This is the governing principle of the whole subsection. The clearest examples are **torsades de pointes from QT-prolonging class III agents** and the **increased mortality with class Ic agents in structural heart disease** demonstrated by the CAST trial — which is why **flecainide is contraindicated in ischaemic heart disease and structural heart disease**. Before starting any of them: **correct potassium and magnesium**, review the ECG and QT, review every other QT-prolonging drug, and know the patient's ventricular function.

- **The essential practical hierarchy in an acute arrhythmia:** **is the patient stable?** Adverse features — shock, syncope, myocardial ischaemia, heart failure — mean **synchronised DC cardioversion**, not a drug (see `NEW_Exam_Manoeuvres_and_Procedures.md` 0.16). And **look for the cause**: ischaemia, electrolytes, sepsis, thyrotoxicosis, pulmonary embolism, alcohol, drugs.

### 0.8.2 Class Ia
- **Key agents:** **quinidine, procainamide, disopyramide.**
- **Effect:** moderate sodium channel block with potassium channel block — **QRS widening and QT prolongation**.
- **Role:** now very limited. **Procainamide** retains a place in **stable wide-complex tachycardia** and in **pre-excited atrial fibrillation (WPW)**; **quinidine** in Brugada syndrome and short-QT syndrome.
- **Adverse effects:** **torsades de pointes**; **quinidine** — cinchonism (tinnitus, deafness, visual disturbance, confusion), thrombocytopenia, diarrhoea; **procainamide** — **drug-induced lupus** and agranulocytosis on prolonged use; **disopyramide** — marked **anticholinergic** effects and negative inotropy (used deliberately in HOCM for that reason).

### 0.8.3 Class Ib
- **Key agents:** **lidocaine (lignocaine)**, mexiletine, phenytoin.
- **Effect:** shorten the action potential; act preferentially on **ischaemic and depolarised** tissue and on **ventricular** myocardium — they have **no useful atrial activity**.
- **Role:** **ventricular arrhythmias**, particularly in the context of ischaemia; lidocaine is an alternative to amiodarone in refractory VF/pulseless VT.
- **Adverse effects:** **CNS toxicity — perioral tingling, tinnitus, confusion, seizures** (the same spectrum as local anaesthetic systemic toxicity — see `NEW_Drugs_02_Anaesthetics.md` 0.1.5); accumulation in **hepatic impairment and low cardiac output states**.

### 0.8.4 Class Ic
- **Key agents:** **flecainide**, propafenone.
- **Effect:** the most potent sodium channel blockade, markedly slowing conduction (**QRS widening**) with little effect on repolarisation.
- **Role:** **rhythm control in atrial fibrillation and other supraventricular arrhythmias in patients with STRUCTURALLY NORMAL HEARTS** — including the **"pill-in-the-pocket"** strategy for paroxysmal AF.

> [!danger] **Flecainide and propafenone are CONTRAINDICATED in ischaemic heart disease, prior myocardial infarction, and structural heart disease** — the CAST trial showed **increased mortality** from proarrhythmia. **Confirm normal ventricular function and no coronary disease (echocardiography, and often stress testing) before prescribing.**

> [!danger] **Always co-prescribe an AV-nodal blocking agent (a beta-blocker or a non-dihydropyridine calcium channel blocker) when using a class Ic drug for atrial fibrillation or flutter.** Class Ic agents slow the atrial rate, which can allow **1:1 AV conduction of atrial flutter** at a catastrophic ventricular rate with a wide QRS.

### 0.8.5 Class III
- **Key agents:** **amiodarone, sotalol, dronedarone**; ibutilide, dofetilide, vernakalant.
- **Effect:** potassium channel blockade → prolonged repolarisation and refractory period → **QT prolongation**.
- **Amiodarone** — the most effective and most toxic. Multi-class action (I, II, III and IV properties), and unusually **safe in structural heart disease and heart failure**, which is why it survives despite its toxicity. Used in AF rhythm control, ventricular arrhythmias, and cardiac arrest.
  - **Enormous volume of distribution and a half-life of WEEKS TO MONTHS** — so effects and interactions persist long after stopping, and loading is prolonged.
  - **TOXICITY — the reason for structured monitoring.** Sources give incidences of roughly **thyroid 1–22%, hepatic 15–50%, pulmonary 2–7%**:
    - **THYROID:** both **hypothyroidism** and **thyrotoxicosis** (amiodarone is iodine-rich); amiodarone-induced thyrotoxicosis has two types with different treatment and is difficult to manage.
    - **PULMONARY:** pneumonitis and **fibrosis** — sources note it is **usually reversible if amiodarone is withdrawn early, but NOT once fibrosis develops.** Presents with **non-productive cough, dyspnoea, weight loss and sometimes fever** — investigate with **lung function including DLCO/transfer factor and a chest X-ray**.
    - **HEPATIC:** transaminitis to hepatitis and cirrhosis.
    - **Also:** **corneal microdeposits** (near-universal, usually asymptomatic, occasionally causing haloes), **optic neuropathy**, **blue-grey skin discolouration and severe photosensitivity** (Australian sun exposure makes this practically important — counsel on sun protection), peripheral neuropathy, bradycardia and heart block.
  - **MONITORING (sources specify a baseline and interval schedule):** **baseline ECG, TFTs, LFTs, chest X-ray and — where possible — lung function tests before starting**, then **TFTs and LFTs approximately 6-monthly**, with a chest X-ray and lung function if pulmonary symptoms appear, and periodic ophthalmological review. Sources emphasise that **serial monitoring allows toxicity to be caught before irreversible sequelae**.
  - **Interactions:** raises **digoxin** (halve the dose), **warfarin** (raises INR substantially and for months), statins (myopathy), and additively prolongs the QT with everything else that does.
  - **Administration:** **irritant to peripheral veins — give via a central line where possible** and never as a rapid bolus outside cardiac arrest.
- **Sotalol** — a **non-selective beta-blocker with class III activity**. Carries both the beta-blocker profile and a **dose- and renal-function-dependent risk of QT prolongation and torsades**; it is **renally cleared**, so accumulation in renal impairment is a recognised cause of torsades. Usually initiated with ECG monitoring.
- **Dronedarone** — an amiodarone analogue without iodine, with less organ toxicity but **less efficacy**, and **contraindicated in permanent AF and in heart failure** (increased mortality).

> [!info] **Other essential antiarrhythmic drugs that sit outside the Vaughan Williams scheme**
> - **Adenosine** — transient AV nodal block; **diagnostic and therapeutic in regular narrow-complex SVT**. **Warn the patient about the brief but severe chest tightness, flushing and sense of doom**; give as a **rapid push with an immediate flush through a large proximal cannula**; **avoid in asthma**; effects are potentiated by dipyridamole and blocked by caffeine and theophylline. **Record a rhythm strip while giving it** — the response is diagnostic even when it does not terminate the arrhythmia.
> - **Digoxin** — increases vagal tone and inhibits Na⁺/K⁺-ATPase; **rate control at rest** (poor with exertion) and a symptomatic role in heart failure. **Narrow therapeutic index. HYPOKALAEMIA POTENTIATES TOXICITY** (digoxin and potassium compete for the same binding site), as do **hypomagnesaemia, hypercalcaemia, renal impairment and age**. **Toxicity:** nausea and vomiting, confusion, **xanthopsia (yellow-green visual haloes)**, and almost any arrhythmia — classically bradyarrhythmias with ectopy. **Interactions: amiodarone, verapamil, clarithromycin, and anything causing hypokalaemia (diuretics).** Antidote: **digoxin-specific Fab fragments** for life-threatening arrhythmia or hyperkalaemia.
> - **Magnesium** — the treatment for **torsades de pointes**, and useful in digoxin toxicity and refractory arrhythmia.
> - **Atropine** — symptomatic bradycardia.

## 0.9 Drugs for Dyslipidaemia

> [!info] **The Australian framing:** lipid-lowering decisions are made on **absolute cardiovascular risk**, not on a cholesterol number in isolation — with **automatic high-risk categories** (established cardiovascular disease, diabetes with end-organ damage, moderate-to-severe chronic kidney disease, familial hypercholesterolaemia, very high individual risk factor levels) treated regardless of the calculated score. **Lifestyle change is prescribed alongside, never instead of, drug therapy in high-risk patients.**

### 0.9.1 Statins (HMG-CoA Reductase Inhibitors)
*(covers build-list classes: Statins; HMG-CoA Reductase Inhibitors)*
- **Mechanism:** competitively inhibit **HMG-CoA reductase**, the rate-limiting enzyme of hepatic cholesterol synthesis → upregulated LDL receptors → increased LDL clearance. They also have **pleiotropic effects** on plaque stability and inflammation.
- **Key agents:** **atorvastatin, rosuvastatin** (high intensity); **simvastatin, pravastatin, fluvastatin** (moderate).
- **Indications:** **secondary prevention in everyone with established atherosclerotic cardiovascular disease** (the single most effective drug class in that setting); primary prevention by absolute risk; familial hypercholesterolaemia; diabetes with risk factors; chronic kidney disease.
- **Adverse effects:**
  - **Muscle symptoms** — **myalgia is common; true myositis with a raised CK is uncommon; rhabdomyolysis is rare.** Sorting these out is a routine clinical task: **check CK, exclude hypothyroidism and vitamin D deficiency, review interacting drugs, and try a dose reduction, an alternate-day regimen, or a different statin** before abandoning the class. **Most patients labelled "statin intolerant" can tolerate some statin**, and randomised n-of-1 and blinded rechallenge studies show much of the symptom burden is not drug-specific.
  - **Transaminase rise** — usually modest and not a reason to stop; significant hepatotoxicity is rare.
  - **New-onset diabetes** — a small real effect, **far outweighed by cardiovascular benefit** in those with an indication.
  - Not associated with the cognitive harm often attributed to them.
- **Interactions:** **simvastatin and atorvastatin are CYP3A4 substrates** — **macrolides (clarithromycin, erythromycin), azole antifungals, HIV protease inhibitors, ciclosporin, amiodarone, verapamil/diltiazem and grapefruit juice** all raise levels and myopathy risk; **specific maximum simvastatin doses apply with amiodarone, verapamil and diltiazem.** **Rosuvastatin and pravastatin are less CYP-dependent** and are often the pragmatic choice in a polypharmacy patient. **Fusidic acid with a statin has caused fatal rhabdomyolysis** — hold the statin.
- **Contraindication:** **pregnancy and breastfeeding** — discuss contraception with women of reproductive age on a statin.

### 0.9.2 Cholesterol Absorption Inhibitors
- **Ezetimibe** — blocks the **NPC1L1** transporter in the intestinal brush border, reducing absorption of dietary and biliary cholesterol.
- **Role:** **add-on to a statin** when LDL remains above target, or **monotherapy in genuine statin intolerance**. Gives roughly a further 20% LDL reduction on top of a statin, with proven (if modest) outcome benefit. Very well tolerated; available in fixed combination with statins.

### 0.9.3 PCSK9 Inhibitors
- **Key agents:** **evolocumab and alirocumab** (monoclonal antibodies, subcutaneous, fortnightly or monthly); **inclisiran** (a small interfering RNA, dosed roughly twice yearly after loading).
- **Mechanism:** PCSK9 targets the hepatic LDL receptor for degradation; **inhibiting it means more LDL receptors survive, so more LDL is cleared** — producing very large LDL reductions on top of a statin.
- **Role:** **familial hypercholesterolaemia** and very high-risk secondary prevention where LDL remains above target on maximal tolerated statin plus ezetimibe. **PBS authority criteria in Australia are restrictive and change — check them.**
- **Adverse effects:** injection site reactions; otherwise remarkably well tolerated, with no signal of harm from very low LDL levels.

### 0.9.4 Fibrates
- **Key agents:** **fenofibrate**, gemfibrozil.
- **Mechanism:** **PPAR-α agonists** — increase lipoprotein lipase activity and fatty acid oxidation. **They lower triglycerides substantially and raise HDL**, with modest LDL effect.
- **Role:** **severe hypertriglyceridaemia to prevent pancreatitis** — the clearest indication; and as an adjunct in mixed dyslipidaemia (with limited cardiovascular outcome evidence). Fenofibrate also reduces diabetic retinopathy progression.
- **Adverse effects:** myopathy (**greatly increased when combined with a statin — GEMFIBROZIL WITH A STATIN IS PARTICULARLY DANGEROUS AND SHOULD BE AVOIDED; fenofibrate is the safer partner**); a **rise in creatinine** that is largely a haemodynamic/analytical effect rather than injury; gallstones; deranged LFTs.

### 0.9.5 Nicotinic Acid (Niacin)
- **Mechanism:** reduces hepatic VLDL production; historically the most effective agent for **raising HDL**.
- **Role: essentially abandoned.** Large outcome trials (adding niacin to a statin) showed **no cardiovascular benefit and increased harm**, and it is a good illustration of why a favourable lipid profile is not the same as a clinical benefit — a point worth understanding rather than a drug worth prescribing.
- **Adverse effects:** intense **flushing and pruritus** (prostaglandin-mediated, reduced by aspirin pretreatment and slow-release formulations), hyperglycaemia, hyperuricaemia and gout, hepatotoxicity, and myopathy with statins.

### 0.9.6 Other Drugs for Dyslipidaemia
- **Bile acid sequestrants (colestyramine, colesevelam)** — bind bile acids in the gut, forcing hepatic cholesterol into bile acid synthesis. Not absorbed, so **safe in pregnancy** and in children. **Very poorly tolerated** (bloating, constipation, unpalatable), **raise triglycerides**, and **bind other drugs — separate all other medication doses by several hours** (warfarin, thyroxine, digoxin and fat-soluble vitamins in particular).
- **Omega-3 fatty acids (icosapent ethyl and others)** — triglyceride lowering; outcome evidence is agent- and dose-specific and generally disappointing outside high-dose icosapent ethyl.
- **Bempedoic acid** — an ATP citrate lyase inhibitor acting upstream of HMG-CoA reductase, activated only in the liver, so it **does not cause muscle symptoms** — of interest specifically in statin intolerance.
- **Lomitapide, evinacumab and lipoprotein apheresis** — homozygous familial hypercholesterolaemia, specialist only.

## 0.10 Drugs for Heart Failure

> [!info] **The "FOUR PILLARS" of heart failure with reduced ejection fraction — the organising fact of this subsection.**
> Sources describe the four guideline-directed classes as: **(1) an ARNI (sacubitril/valsartan) — preferred over an ACE inhibitor or ARB; (2) a beta-blocker; (3) a mineralocorticoid receptor antagonist; and (4) an SGLT2 inhibitor.** The **2023 ESC focused update** emphasises implementing all four **early and together** rather than sequentially, and sources describe the combined effect as reducing the risk of death by around 50%. Sources also note that **real-world use remains substantially below what the evidence supports** — under-prescribing and under-titration are the norm, and are something an intern can actively help fix.
> **Diuretics are for SYMPTOMS (congestion) and do not improve survival** — they are essential but they are not one of the pillars.

### 0.10.1 Loop Diuretics
*(covers build-list classes: Loop diuretics; Diuretics (Loop))*
- **Mechanism:** inhibit the **Na⁺/K⁺/2Cl⁻ cotransporter** in the thick ascending limb of the loop of Henle — the most powerful natriuretic site.
- **Key agents:** **furosemide (frusemide)**, bumetanide, ethacrynic acid (useful in true sulfonamide allergy).
- **Indications:** **acute pulmonary oedema and congestive symptoms in heart failure**; oedema in nephrotic syndrome, cirrhosis and renal failure; hypercalcaemia (with fluid replacement); resistant hypertension in renal impairment.
- **Adverse effects:** **hypokalaemia, hypomagnesaemia, hyponatraemia, hypochloraemic metabolic alkalosis**; **hypovolaemia and prerenal acute kidney injury**; **hyperuricaemia and gout**; **ototoxicity** (dose- and infusion-rate-related, worse with aminoglycosides — give large IV doses slowly); hyperglycaemia; hypocalcaemia.
- **Practical points that matter:**
  - **Oral bioavailability of furosemide is erratic**, and **gut wall oedema in decompensated heart failure impairs absorption further** — which is why the intravenous route is used in acute decompensation and why a patient can appear "diuretic resistant" on oral therapy.
  - **Weigh the patient daily and chart fluid balance** — weight is the more reliable measure.
  - **Diuretic resistance:** consider adherence, salt and fluid intake, NSAIDs, worsening renal function, and **sequential nephron blockade** (adding a thiazide) under supervision — a combination that produces profound electrolyte loss and requires close monitoring.
  - **Withhold during acute dehydrating illness** as part of "sick day" advice.

### 0.10.2 Aldosterone Antagonists (Mineralocorticoid Receptor Antagonists)
- **Key agents:** **spironolactone, eplerenone**; **finerenone** (a non-steroidal MRA, used in chronic kidney disease with type 2 diabetes).
- **Mechanism:** block the mineralocorticoid receptor in the distal nephron — a **potassium-sparing** diuretic effect, but the benefit in heart failure is largely **anti-fibrotic and anti-remodelling** rather than diuretic.
- **Indications:** **HFrEF — one of the four pillars**; **resistant hypertension** (where spironolactone is the most effective fourth agent); **primary hyperaldosteronism**; **ascites and oedema in cirrhosis** (spironolactone is first-line there); acne, hirsutism and gender-affirming hormone therapy (spironolactone's anti-androgen effect).
- **Adverse effects:** **HYPERKALAEMIA — the one that causes harm**, especially in renal impairment, in the elderly, and combined with ACE inhibitors/ARBs, potassium supplements, trimethoprim or NSAIDs. **Spironolactone also causes gynaecomastia, breast tenderness and menstrual irregularity** through its anti-androgen and progestogenic activity; **eplerenone is more selective and causes less of this**, which is the usual reason to switch.
- **Monitoring:** **potassium and creatinine before starting, after initiation, after every dose increase, and during any intercurrent illness.** This is a standing, checkable action and a common ward omission.

### 0.10.3 Other Diuretics
- **Thiazide and thiazide-like diuretics** — built in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`. In heart failure, their role is **sequential nephron blockade added to a loop diuretic** in resistant congestion — effective and dangerous, requiring close electrolyte monitoring.
- **Potassium-sparing diuretics — amiloride, triamterene** — epithelial sodium channel blockers; used to offset potassium loss and in Liddle syndrome. **Hyperkalaemia** risk as above.
- **Carbonic anhydrase inhibitors — acetazolamide** — weak diuretic; used in **glaucoma, altitude sickness, and metabolic alkalosis** from over-diuresis; causes metabolic acidosis, paraesthesia and renal stones. It also has an emerging role added to loop diuretics in decompensated heart failure.
- **Osmotic diuretics — mannitol** — raised intracranial pressure and, historically, forced diuresis. **Causes an osmolar gap** (see `NEW_Investigations_Orthopaedics_Neurology_and_Other.md` 0.3); risks fluid overload, hypernatraemia and acute kidney injury.
- **Vasopressin (V2) receptor antagonists — tolvaptan** — see 0.11.4.

### 0.10.4 Other Drugs for Heart Failure
- **ARNI — sacubitril/valsartan.** **Sacubitril inhibits neprilysin**, so natriuretic peptides are not degraded (promoting natriuresis and vasodilation), combined with an ARB.
  - **THE CRITICAL PRESCRIBING RULE: a 36-hour washout is required when switching from an ACE inhibitor**, because combining neprilysin inhibition with ACE inhibition causes **angioedema**. **Never co-prescribe an ACE inhibitor with sacubitril/valsartan.** Contraindicated with any history of ACE-inhibitor angioedema.
  - **Note it raises BNP (but not NT-proBNP)** — relevant when interpreting natriuretic peptides in a treated patient (see `NEW_Investigations_Cardiology.md` 0.2).
- **SGLT2 inhibitors — dapagliflozin, empagliflozin.** Now a **heart failure drug in their own right, with benefit in both reduced AND preserved ejection fraction, and irrespective of diabetes.** Watch for **genital mycotic infection, volume depletion, and euglycaemic diabetic ketoacidosis** (which must be actively considered in an unwell patient on one of these, because the glucose may be near-normal — and they are **withheld before surgery and during acute illness**). See [[06_Metabolic_Medicine_and_Endocrinology]].
- **ACE inhibitors, ARBs and beta-blockers** — pillars 1 and 2 (see 0.7 and the antihypertensives file).
- **Ivabradine** — added where the heart rate remains ≥70–75 in sinus rhythm despite a maximally tolerated beta-blocker.
- **Digoxin** — symptomatic and hospitalisation benefit, no mortality benefit (see 0.8.5).
- **Hydralazine with isosorbide dinitrate** — an alternative where ACE inhibitors and ARBs cannot be used, and with specific benefit demonstrated in patients of African ancestry.
- **Vericiguat** — a soluble guanylate cyclase stimulator for worsening chronic HFrEF.
- **Intravenous iron** — corrects iron deficiency in heart failure (**defined by ferritin and transferrin saturation criteria, not haemoglobin — patients need not be anaemic**), improving symptoms and reducing hospitalisation. Frequently missed: **check iron studies in every heart failure patient.**
- **Non-drug measures:** fluid and salt advice, daily weights, immunisation, cardiac rehabilitation, device therapy (CRT and ICD — see `NEW_Exam_Manoeuvres_and_Procedures.md` 0.17), and management of the precipitant. See [[01_Cardiovascular]].

## 0.11 Drugs for Other Cardiovascular Disorders

### 0.11.1 Sympathomimetics (Cardiovascular), including α₁- and β₁-Agonists
*(covers build-list classes: Sympathomimetics (cardiovascular); Alpha-1 Adrenergic Agonists; Beta-1 Adrenergic Agonists)*
- **Choosing by receptor is the whole skill here:**
  - **Noradrenaline** — predominantly **α₁** with some β₁: **vasoconstriction**. **The first-line vasopressor in septic and most vasodilatory shock.**
  - **Adrenaline** — α and β: inotropy, chronotropy and vasoconstriction. **Anaphylaxis** (see `NEW_Drugs_01_Allergy_and_Anaphylaxis.md` 0.5), **cardiac arrest**, and cardiogenic shock.
  - **Dobutamine** — predominantly **β₁**: **inotropy** with some vasodilation. Used in **cardiogenic shock and low cardiac output states**, and for stress echocardiography. It can **drop the blood pressure**, which surprises people.
  - **Phenylephrine and metaraminol** — pure **α₁** vasoconstrictors; useful where tachycardia is undesirable, and the common perioperative and ward agents for anaesthetic-induced hypotension.
  - **Dopamine** — dose-dependent receptor effects; **"renal-dose dopamine" has been disproven and abandoned**, and dopamine causes more arrhythmia than noradrenaline in shock.
  - **Vasopressin** — a non-adrenergic vasoconstrictor added to noradrenaline in refractory vasodilatory shock (see 0.11.4).
  - **Isoprenaline** — β₁/β₂: chronotropy in bradycardia and torsades, as a bridge to pacing.
- **Adverse effects:** **tachyarrhythmia, myocardial ischaemia, hypertension, peripheral and mesenteric ischaemia, hyperglycaemia, lactic acidosis** (a metabolic effect of adrenaline, not necessarily hypoperfusion).

> [!danger] **Vasopressors and inotropes should be given through a CENTRAL line wherever possible and with invasive blood pressure monitoring.**
> **EXTRAVASATION of noradrenaline or another vasoconstrictor causes tissue necrosis** — the treatment is to stop the infusion, **aspirate from the cannula, and infiltrate the area with phentolamine** while escalating urgently. Peripheral administration is acceptable in defined emergency circumstances with a large proximal cannula and close observation, but the site must be checked constantly. **Never give these drugs without continuous monitoring**, and never as a bolus unless the protocol says so.

### 0.11.2 Phosphodiesterase 3 (PDE3) Inhibitors
- **Key agents:** **milrinone**, enoximone; **cilostazol** (peripheral, see 0.11.6).
- **Mechanism:** inhibit PDE3, raising cyclic AMP in myocardium and vascular smooth muscle → **"inodilation"** — increased contractility **plus** vasodilation, achieved **without** the β-receptor, which is why it still works in a patient on beta-blockers or with downregulated receptors.
- **Role:** short-term support in **decompensated heart failure and cardiogenic shock**, and after cardiac surgery, particularly with **pulmonary hypertension and right ventricular failure**.
- **Adverse effects:** **hypotension** (the dose-limiting effect); arrhythmia; **renally cleared, so it accumulates in renal impairment**; **long-term oral use increases mortality**, which is why it is a short-term intravenous drug only.

### 0.11.3 Phosphodiesterase 5 Inhibitors (Cardiovascular)
- **Key agents:** **sildenafil, tadalafil**.
- **Mechanism:** inhibit PDE5, so **cGMP persists** in smooth muscle — vasodilation, with relative selectivity for the **pulmonary vasculature** and corpus cavernosum.
- **Cardiovascular indication:** **pulmonary arterial hypertension** (alongside endothelin receptor antagonists such as bosentan and macitentan, and prostacyclin analogues) — specialist-initiated.
- **Adverse effects:** headache, flushing, dyspepsia, nasal congestion, visual disturbance (blue tinge), and rarely **non-arteritic anterior ischaemic optic neuropathy** and sudden hearing loss.

> [!danger] **PDE5 inhibitors are ABSOLUTELY CONTRAINDICATED with nitrates in any form** (see 0.6.1) — including nicorandil and recreational nitrites. **Also avoid with riociguat.** Caution with α-blockers (additive hypotension).

### 0.11.4 Antidiuretic Hormone Agonists and Antagonists
- **Agonists:**
  - **Desmopressin (DDAVP)** — a **V2-selective** analogue: antidiuretic without vasoconstriction. Used in **cranial diabetes insipidus**, **nocturnal enuresis**, and **mild haemophilia A / type 1 von Willebrand disease / uraemic bleeding** (see 0.5). **HYPONATRAEMIA from water retention is the main harm — restrict fluids and monitor sodium**, and be particularly careful in children and the elderly.
  - **Vasopressin and terlipressin** — **V1**-mediated vasoconstriction: **refractory vasodilatory shock**, **variceal bleeding** (terlipressin), and hepatorenal syndrome. Risk **peripheral, mesenteric and cardiac ischaemia**, and hyponatraemia.
- **Antagonists — the "vaptans":**
  - **Tolvaptan** — an oral **V2 antagonist** producing **aquaresis** (free water loss without electrolyte loss). Used in **hypervolaemic and euvolaemic hyponatraemia including SIADH**, and (at higher doses) to slow progression in **autosomal dominant polycystic kidney disease**.
  - **Its dangers are specific:** **over-rapid correction of hyponatraemia risking osmotic demyelination** — so it is **started in hospital with close sodium monitoring and without fluid restriction initially**; and **hepatotoxicity**, particularly at ADPKD doses, requiring a monitoring programme.

### 0.11.5 Drugs for Orthostatic Hypotension
- **Non-drug measures come first and are genuinely effective:** **stop or reduce the offending drugs** (antihypertensives, diuretics, α-blockers, tricyclics, antipsychotics, dopaminergic agents, nitrates) — **medication review is the single highest-yield intervention**; adequate salt and fluid; slow positional change; counter-pressure manoeuvres; compression garments; head-up sleeping; and avoiding large hot carbohydrate meals and alcohol.
- **Fludrocortisone** — a mineralocorticoid expanding plasma volume. Causes **supine hypertension, hypokalaemia, oedema and heart failure decompensation.**
- **Midodrine** — a peripherally acting **α₁ agonist** prodrug. **Supine hypertension** is the main problem: **do not take it within several hours of lying down**, and it is contraindicated in severe cardiovascular disease and urinary retention.
- **Droxidopa, pyridostigmine** — in autonomic failure, specialist use.

> [!danger] **The central tension in treating orthostatic hypotension is SUPINE HYPERTENSION.** Every drug that raises standing blood pressure also raises it lying down. **Measure lying and standing blood pressure, treat the symptom (falls, syncope, presyncope) rather than the number, and reassess the whole medication list at every review.** In older patients, falls are the outcome that matters. See [[18_Geriatrics_and_Older_Persons_Health]].

### 0.11.6 Drugs for Peripheral Vascular Disease
- **The disease-modifying treatment is risk factor management, and it is what changes outcomes:** **SMOKING CESSATION above all**, a **statin**, an **antiplatelet**, blood pressure and diabetes control, and — the intervention with the best evidence for claudication distance — **supervised exercise therapy**.
- **Symptomatic agents:** **cilostazol** (a PDE3 inhibitor with vasodilator and antiplatelet action; improves walking distance; **contraindicated in heart failure** like all PDE3 inhibitors; causes headache, palpitations and diarrhoea); **pentoxifylline** (marginal benefit); **naftidrofuryl**.
- **Critical limb ischaemia** — revascularisation, wound care and analgesia; drug therapy alone is inadequate.
- **Raynaud phenomenon** — **nifedipine** and other dihydropyridines first-line; then PDE5 inhibitors; **iloprost** and endothelin antagonists for digital ulceration in systemic sclerosis. Cold avoidance and smoking cessation are essential.
- **Vasospastic and vasodilatory adverse effects of other drugs** — beta-blockers and ergots can worsen peripheral ischaemia; check the list.

> [!danger] **ACUTE LIMB ISCHAEMIA — the six Ps (pain, pallor, pulselessness, perishing cold, paraesthesia, paralysis) — is a surgical emergency**, not a prescribing problem. **Paraesthesia and paralysis mean the limb is threatened and time is measured in hours.** Give analgesia, start heparin, and call vascular surgery immediately.

---

## Build status

| # | Build-list row | Type | Built | Notes |
|---|---|---|---|---|
| 0.1 | Anticoagulants | SUB | yes | |
| 0.1.1 | Vitamin K antagonists | CLS | yes | |
| 0.1.2 | Heparins | CLS | yes | Carries the HIT 4Ts and management callout. |
| 0.1.3 | Low Molecular Weight Heparins | CLS | yes | |
| 0.1.4 | Direct thrombin inhibitors | CLS | yes | |
| 0.1.5 | Factor Xa inhibitors | CLS | yes | |
| 0.2 | Drugs for reversing anticoagulation | SUB | yes | Built as a table; no doses. |
| 0.3 | Antiplatelet drugs | SUB | yes | |
| 0.3.1 | Antiplatelets (COX Inhibitors) | CLS | yes | |
| 0.3.2 | Antiplatelets (P2Y12 Inhibitors) | CLS | yes | Built jointly with `Thienopyridines` — thienopyridines are a chemical subgroup of P2Y12 inhibitors; both rows mapped. |
| 0.3.2 | Thienopyridines | CLS | yes | As above. |
| 0.3.3 | Glycoprotein IIb/IIIa inhibitors | CLS | yes | |
| 0.3.4 | Other antiplatelet drugs | CLS | yes | |
| 0.4 | Thrombolytics | SUB | yes | |
| 0.4 | Thrombolytics (Plasminogen Activators) | CLS | yes | Same content as the subsection; built once. |
| 0.5 | Other drugs affecting haemostasis | SUB | yes | |
| 0.6 | Drugs for angina and acute coronary syndromes | SUB | yes | |
| 0.6.1 | Nitrates | CLS | yes | |
| 0.6.2 | Other antianginal drugs | CLS | yes | |
| 0.7 | **Beta-blockers** | CLS | **yes — GAP FIX** | **Not built in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md` despite sitting in that subsection.** Built here. |
| 0.7.1 | **Beta-Blockers (Cardioselective)** | CLS | **yes — GAP FIX** | As above. |
| 0.7.2 | **Beta-Blockers (Non-selective)** | CLS | **yes — GAP FIX** | As above. |
| 0.8 | Drugs for arrhythmias | SUB | yes | |
| 0.8.1 | Antiarrhythmics | CLS | yes | Vaughan Williams overview plus adenosine, digoxin, magnesium, atropine. |
| 0.8.2 | Antiarrhythmics (Class Ia) | CLS | yes | |
| 0.8.3 | Antiarrhythmics (Class Ib) | CLS | yes | |
| 0.8.4 | Antiarrhythmics (Class Ic) | CLS | yes | |
| 0.8.5 | Antiarrhythmics (Class III) | CLS | yes | Amiodarone monitoring schedule stated as a schedule, not a dose. |
| 0.9 | Drugs for dyslipidaemia | SUB | yes | |
| 0.9.1 | Statins | CLS | yes | Built jointly with `HMG-CoA Reductase Inhibitors` — same class. |
| 0.9.1 | HMG-CoA Reductase Inhibitors | CLS | yes | As above. |
| 0.9.2 | Cholesterol Absorption Inhibitors | CLS | yes | |
| 0.9.3 | PCSK9 Inhibitors | CLS | yes | PBS criteria flagged as changeable, not quoted. |
| 0.9.4 | Fibrates | CLS | yes | |
| 0.9.5 | Nicotinic Acid | CLS | yes | Built with an explicit statement that the outcome evidence does not support use. |
| 0.9.6 | Other drugs for dyslipidaemia | CLS | yes | |
| 0.10 | Drugs for heart failure | SUB | yes | Four-pillars framing. |
| 0.10.1 | Loop diuretics | CLS | yes | Built jointly with `Diuretics (Loop)` — same class. |
| 0.10.1 | Diuretics (Loop) | CLS | yes | As above. |
| 0.10.2 | Aldosterone antagonists | CLS | yes | |
| 0.10.3 | Other diuretics | CLS | yes | |
| 0.10.4 | Other drugs for heart failure | CLS | yes | ARNI washout rule included. |
| 0.11 | Drugs for other cardiovascular disorders | SUB | yes | |
| 0.11.1 | Sympathomimetics (cardiovascular) | CLS | yes | Built jointly with `Alpha-1 Adrenergic Agonists` and `Beta-1 Adrenergic Agonists` — organised by receptor, which is the clinical skill. |
| 0.11.1 | Alpha-1 Adrenergic Agonists | CLS | yes | As above. |
| 0.11.1 | Beta-1 Adrenergic Agonists | CLS | yes | As above. |
| 0.11.2 | Phosphodiesterase 3 (PDE3) Inhibitors | CLS | yes | |
| 0.11.3 | Phosphodiesterase 5 inhibitors (cardiovascular) | CLS | yes | |
| 0.11.4 | Antidiuretic hormone agonists and antagonists | CLS | yes | |
| 0.11.5 | Drugs for orthostatic hypotension | CLS | yes | |
| 0.11.6 | Drugs for peripheral vascular disease | CLS | yes | |
| — | Antihypertensives (SUB) and its remaining 14 classes | SUB+CLS | **built elsewhere** | ACE Inhibitors, Angiotensin II Receptor Blockers, Sartans, Calcium Channel Blockers (DHP), (Non-DHP), Calcium channel blockers, Thiazide and related diuretics, Diuretics (Thiazide-like), Alpha-1 Selective Blockers, Alpha-Blockers (Non-selective), Alpha-2 Adrenergic Agonists (Central), Alpha2 agonists, Direct Arteriolar Vasodilators, Other antihypertensives — all in `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md`. |

**Rows in this file: 51 (10 SUB + 41 CLS, including the 3 beta-blocker gap-fix rows). Rows built in the earlier antihypertensives file: 15 (1 SUB + 14 CLS). AMH section 6 build-list rows: 66. Section complete.**

> [!warning] **Limitation found in the earlier build, recorded per CLAUDE.md rule 7.** The antihypertensives file was built during the timed batching test and its own build record did not flag that **beta-blockers — three build-list rows and arguably the most clinically important class in the subsection — were never written.** The gap was found only by re-deriving the row list from `data/build_list_drugclasses.md` while building this file. **Any earlier file whose completeness rests on a narrative claim rather than a row-by-row mapping should be re-checked the same way.**
