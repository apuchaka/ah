---
block: NEW build — Drug Classes
source: Build list 2026-08-30 (data/no_header_build_queue.md), AMH section 6 Cardiovascular drugs
status: standalone — not yet cross-referenced into the corpus; BATCHING TEST BATCH 2
---

# NEW — Drug Classes: Antihypertensives

> [!warning] **Standalone build, not yet integrated.** No cross-references written into existing corpus files.

> [!danger] **This file has a KNOWN GAP — beta-blockers were never built here.** Three build-list rows (`Beta-Blockers (Cardioselective)`, `Beta-Blockers (Non-selective)`, `Beta-blockers`) were omitted when this batching-test file was written, and the file was then recorded as "DONE" in `data/BULK_BUILD_PLAN.md`. They are built in **[[NEW_Drugs_06_Cardiovascular]]** at entry **0.7**. Beta-blockers are mentioned incidentally below (calcium channel blocker interactions, the alpha-before-beta rule in phaeochromocytoma) — **those mentions are not the class entry**. Do not use this file as a complete antihypertensive list.

> [!danger] **Sourcing limitation applying to this whole file.** The **Australian Medicines Handbook and Therapeutic Guidelines are subscription-gated and egress-blocked** in this environment, and they are the sources that would normally supply Australian doses and product details. Entries are **snippet-sourced**. **No doses are stated anywhere in this file** — that is deliberate and applies to every class below. Use AMH or the local formulary for dosing.

> [!info] **Australian first-line context for the whole file.** Australian guidance recommends starting monotherapy with an **ACE inhibitor, ARB, calcium channel blocker, or thiazide diuretic** — with the thiazide option qualified by age in the source found (≥65 years). Preferred **combinations** are ACE inhibitor or ARB **with** a calcium channel blocker or thiazide, or a calcium channel blocker **with** a thiazide. Australian guidance notably **does not** recommend starting on a fixed-dose combination, unlike some North American guidance. *(Single Australian source; treated as orientation, not as a settled figure — confirm against the current Heart Foundation guideline.)*
> **The classes below in positions 6–10 are later-line or specialist agents**, not first-line, and the entries say so.

## ACE Inhibitors

- **Mechanism:** block angiotensin-converting enzyme, reducing conversion of angiotensin I to angiotensin II → arteriolar vasodilation, reduced aldosterone (so reduced sodium and water retention), and reduced sympathetic tone. ACE also degrades **bradykinin**, so inhibition raises bradykinin — which explains both the cough and the angioedema, and is the single fact that makes the whole adverse-effect profile predictable.
- **Key agents:** perindopril, ramipril, enalapril, captopril, lisinopril, quinapril, trandolapril.
- **Indications:** hypertension (first-line); **heart failure with reduced ejection fraction**; post-myocardial infarction; **diabetic and non-diabetic proteinuric chronic kidney disease** (renoprotective through reduced intraglomerular pressure — a benefit that is separate from blood pressure lowering).
- **Adverse effects:** **dry persistent cough** — the classic and commonest reason for switching, reported in up to a large minority of patients and bradykinin-mediated; **hyperkalaemia**; **acute kidney injury**, particularly with volume depletion or **bilateral renal artery stenosis**, where renal function can deteriorate sharply; **first-dose hypotension** (greatest in volume-depleted or heart-failure patients); **angioedema** — uncommon but potentially life-threatening, **can begin months or years after starting the drug**, and is over-represented in patients of African ancestry; rash; taste disturbance.
- **Contraindications:** **pregnancy — absolutely, in all trimesters** (fetal renal injury, oligohydramnios, skull hypoplasia); bilateral renal artery stenosis; previous angioedema on an ACE inhibitor; hyperkalaemia.
- **Interactions:** **potassium-sparing diuretics, aldosterone antagonists, potassium supplements, trimethoprim** → hyperkalaemia; **NSAIDs** → the "triple whammy" with a diuretic, a recognised and preventable cause of acute kidney injury; **lithium** → toxicity; **ARBs and direct renin inhibitors** → dual blockade, not recommended; **sacubitril/valsartan** → must not be co-prescribed and requires a washout.
- **Monitoring:** **UEC before starting and again after initiation and each dose increase** — a modest rise in creatinine is expected and acceptable; a large rise or hyperkalaemia prompts review rather than automatic cessation. Blood pressure. **Withhold during acute intercurrent illness with dehydration ("sick day" rules)** — an intern-level action that prevents a common admission.

## Angiotensin II Receptor Blockers (ARBs / "sartans")

- **Mechanism:** block the angiotensin II type 1 receptor directly, giving the same downstream effect as ACE inhibition **without** affecting bradykinin metabolism — which is exactly why the cough is absent.
- **Key agents:** candesartan, irbesartan, telmisartan, valsartan, olmesartan, losartan.
- **Indications:** as for ACE inhibitors, and **the standard substitution when an ACE inhibitor is stopped for cough**.
- **Adverse effects:** shares the ACE inhibitor profile for **hyperkalaemia, acute kidney injury and hypotension**, but **does not typically cause cough**. **Angioedema is much less common but not impossible** — sources report recurrence in a meaningful minority of patients switched to an ARB after ACE-inhibitor angioedema, so **switching after angioedema is a decision requiring caution, not a routine swap**.
- **Contraindications, interactions, monitoring:** as for ACE inhibitors, including the **absolute contraindication in pregnancy**.

> [!info] **The practical distinction between the two classes** is narrow: same efficacy, same renal and potassium considerations, same pregnancy prohibition — the difference is cough and, to a lesser degree, angioedema risk. Cost and local formulary usually decide the rest.

## Calcium Channel Blockers — Dihydropyridine (DHP)

- **Mechanism:** block L-type calcium channels with **vascular selectivity** → arteriolar vasodilation and reduced peripheral resistance, with little direct effect on cardiac conduction or contractility.
- **Key agents:** amlodipine, felodipine, nifedipine, lercanidipine.
- **Indications:** hypertension (first-line, and **particularly useful in older patients and in isolated systolic hypertension**); stable angina; Raynaud phenomenon; **the calcium channel blocker of choice when heart failure is present**, since the vascular selectivity avoids negative inotropy.
- **Adverse effects:** **peripheral (ankle) oedema is the characteristic class effect** — sources agree it is **dose-dependent**, affects roughly 5% at starting doses of amlodipine or felodipine and can rise steeply at high doses, appears within the first weeks to months of starting or increasing, and is **not a sign of fluid overload**. It does not respond to diuretics; it responds to dose reduction or to adding an ACE inhibitor or ARB, which is a genuinely useful prescribing point. Also: **flushing, headache, palpitations, reflex tachycardia** (less with amlodipine, which is long-acting), **gum hypertrophy**, constipation.
- **Interactions:** **CYP3A4 inhibitors — clarithromycin, erythromycin, azole antifungals, grapefruit juice** → raised levels and hypotension; **simvastatin** with amlodipine has a specific dose limit; CYP3A4 inducers reduce effect.
- **Monitoring:** blood pressure; **ask about and examine for ankle oedema** at review, because patients frequently attribute it to something else and stop the drug without telling anyone.

## Calcium Channel Blockers — Non-Dihydropyridine (Non-DHP)

- **Mechanism:** block L-type calcium channels with **cardiac selectivity** → **negative inotropic, chronotropic and dromotropic effects** (reduced contractility, reduced heart rate, slowed AV conduction) alongside vasodilation.
- **Key agents:** **verapamil** (phenylalkylamine; more negatively inotropic) and **diltiazem** (benzothiazepine; intermediate).
- **Indications:** hypertension; **rate control in atrial fibrillation and flutter**; **supraventricular tachycardia**; angina, including **coronary vasospasm**.
- **Adverse effects:** **bradycardia, AV block, hypotension, and precipitation or worsening of heart failure**; **constipation** — prominent and dose-limiting with verapamil; peripheral oedema; gum hypertrophy.
- **Contraindications, and these are the ones that matter:** **heart failure with reduced ejection fraction** — sources are explicit that non-DHP agents are **not recommended and are potentially harmful** here, which is the key distinction from the DHP group; second- or third-degree AV block without a pacemaker; sick sinus syndrome; **atrial fibrillation with pre-excitation (WPW)**.
- **Interactions — the important one:** **combining a non-DHP calcium channel blocker with a beta-blocker increases the risk of bradyarrhythmia, AV block and heart failure**, and sources flag this combination specifically. Also a potent **CYP3A4 inhibitor** itself → raises levels of statins, ciclosporin, carbamazepine, and **digoxin** (verapamil raises digoxin levels).
- **Monitoring:** heart rate and blood pressure; ECG where conduction disease is possible; review for signs of heart failure.

## Thiazide and Thiazide-like Diuretics

- **Mechanism:** inhibit the sodium–chloride cotransporter in the distal convoluted tubule → natriuresis, with the long-term antihypertensive effect largely due to reduced peripheral resistance rather than sustained volume loss. **Thiazide-like agents (indapamide, chlortalidone) are structurally distinct from true thiazides (hydrochlorothiazide) but are used interchangeably in practice**, with longer duration of action.
- **Key agents:** hydrochlorothiazide, indapamide, chlortalidone.
- **Indications:** hypertension (first-line, with the Australian age qualifier noted above); oedema; **calcium nephrolithiasis and idiopathic hypercalciuria** (they reduce urinary calcium — the one setting where a "side effect" is the indication); nephrogenic diabetes insipidus.
- **Adverse effects:** **hyponatraemia — sources identify thiazides as the commonest cause of drug-induced hyponatraemia in secondary care**, and it can be severe, causing confusion, falls and seizures; risk is concentrated in **older patients, low-normal baseline sodium and potassium, low solute intake, and co-prescription of other hyponatraemia-inducing drugs**. Also **hypokalaemia, hypomagnesaemia, hypercalcaemia, hyperuricaemia and gout, glucose intolerance, dyslipidaemia**, postural hypotension, erectile dysfunction, photosensitivity, and rarely pancreatitis and thrombocytopenia.
- **Contraindications/cautions:** significant renal impairment (efficacy falls, and loop diuretics are preferred), gout, hyponatraemia, hypercalcaemia.
- **Interactions:** **lithium** → toxicity; **NSAIDs** → reduced efficacy and the "triple whammy" acute kidney injury with an ACE inhibitor or ARB; **digoxin** → hypokalaemia potentiates toxicity; other QT-prolonging drugs via hypokalaemia; corticosteroids → additive potassium loss.
- **Monitoring:** **UEC before starting and after initiation** — sources specifically question whether the conventional monitoring interval is early enough for hyponatraemia. **Sodium, potassium, glucose and urate**, with **magnesium added if potassium is persistently low.** *(A specific monitoring interval in weeks is deliberately not stated — sources disagree and the question is actively under review.)*

## Alpha-1 Selective Blockers

- **Mechanism:** selectively block postsynaptic α₁-adrenoceptors → arteriolar and venous dilation with reduced peripheral resistance; also relax prostatic and bladder neck smooth muscle.
- **Key agents:** prazosin, terazosin, doxazosin; **tamsulosin and silodosin** are uroselective and used for benign prostatic hyperplasia rather than blood pressure.
- **Indications:** **later-line** in hypertension, typically as add-on in resistant disease; **benign prostatic hyperplasia** — which is where most Australian use sits; part of the pre-operative regimen in **phaeochromocytoma**; prazosin is also used for PTSD-related nightmares.
- **Adverse effects:** **first-dose phenomenon — marked postural hypotension or syncope, typically within about 30–90 minutes of the first dose** (sources agree on this window). It is more likely in patients who are **volume-depleted, on a diuretic, or on a beta-blocker**, and it is largely self-limiting after the initial period. Practical consequence: **start at a low dose, at night, with a warning to the patient.** Also postural hypotension generally, dizziness, headache, nasal congestion, **urinary incontinence in women**, and **intraoperative floppy iris syndrome** — which the ophthalmologist must be told about before cataract surgery.
- **Interactions:** additive hypotension with **PDE5 inhibitors** (sildenafil, tadalafil) — a genuinely important and commonly missed combination; other antihypertensives.
- **Monitoring:** postural blood pressure, particularly after initiation and dose increases; falls risk assessment in older patients.

## Alpha-Blockers (Non-selective)

- **Mechanism:** block both α₁ and α₂ receptors. **Phenoxybenzamine** is a **non-competitive, irreversible** blocker with a long duration of action; **phentolamine** is competitive, reversible and short-acting.
- **Key agents:** phenoxybenzamine, phentolamine.
- **Indications:** **not used for routine hypertension.** The defining indication is **phaeochromocytoma** — pre-operative blockade and control of hypertensive crisis; phentolamine is also used for extravasation of vasopressors and for cocaine-associated hypertension where beta-blockade is problematic.
- **Adverse effects:** marked **postural hypotension**, **reflex tachycardia** (α₂ blockade removes presynaptic negative feedback, so noradrenaline release increases), nasal congestion, miosis, inhibition of ejaculation, sedation.
- **The safety rule that defines this class, and it is unambiguous across sources:** **alpha blockade must be established before any beta-blocker is introduced in phaeochromocytoma.** Beta-blockade first removes β₂-mediated vasodilation and leaves **unopposed α-mediated vasoconstriction**, which can precipitate **hypertensive crisis and pulmonary oedema**. Sources describe alpha blockade being established over roughly **10–14 days pre-operatively** to allow volume expansion, with a beta-blocker added only afterwards.
- **Note on current practice:** sources record a **shift away from phenoxybenzamine** toward selective alpha-blockers and calcium channel blockers for pre-operative preparation, without worse outcomes. **No doses are stated here**; this is specialist-directed prescribing.
- **Monitoring:** blood pressure including postural, heart rate, volume status; this is an inpatient/specialist monitoring context.

## Alpha-2 Adrenergic Agonists (Central)

- **Mechanism:** stimulate presynaptic α₂-adrenoceptors in the brainstem vasomotor centre → **reduced central sympathetic outflow** → reduced peripheral resistance, heart rate and blood pressure. Methyldopa is a prodrug converted to α-methylnoradrenaline, a false neurotransmitter acting at the same receptor.
- **Key agents:** clonidine, methyldopa; (guanfacine and dexmedetomidine act at the same receptor in other settings).
- **Indications:** **later-line** in hypertension. **Methyldopa's distinctive niche is hypertension in pregnancy**, where it has the longest safety record. Clonidine is also used in ADHD, opioid and nicotine withdrawal, and menopausal flushing — and is now rarely used as an antihypertensive.
- **Adverse effects:** **sedation and drowsiness** (prominent, particularly with methyldopa), **dry mouth**, depression, bradycardia, postural hypotension, fluid retention. **Methyldopa specifically: a positive direct antiglobulin test in a substantial minority of users, with overt haemolytic anaemia rare** — which matters because it will confuse a haemolysis work-up if the drug history is not known; also drug-induced hepatitis.
- **The critical class warning: abrupt withdrawal of clonidine causes rebound hypertension**, reported within about **24–36 hours**, with tachycardia, arrhythmia and features of sympathetic overactivity, and it can be severe. **Never stop clonidine abruptly — taper it**, and specifically check for it on the medication chart of any admitted patient, because an omitted inpatient dose is a recognised cause of inpatient hypertensive crisis.
- **Interactions:** additive sedation with CNS depressants; **tricyclic antidepressants reduce clonidine's effect**; beta-blockers worsen rebound hypertension on withdrawal.
- **Monitoring:** blood pressure and heart rate; **LFTs and FBC/DAT with methyldopa**; adherence, given the withdrawal risk.

## Direct Arteriolar Vasodilators

- **Mechanism:** relax arteriolar smooth muscle directly, reducing peripheral resistance **with no venodilation** — which is why they produce a strong compensatory response. Minoxidil acts by opening potassium channels; hydralazine's mechanism is less completely defined.
- **Key agents:** hydralazine, minoxidil. (Sodium nitroprusside and diazoxide belong to the same functional group in critical-care use.)
- **Indications:** **resistant or severe hypertension**, generally as later-line therapy; **hydralazine in hypertensive disorders of pregnancy including pre-eclampsia**, where it has an established role; **hydralazine with a nitrate in heart failure** where ACE inhibitors and ARBs cannot be used.
- **Adverse effects — all three follow from the mechanism, which makes them easy to reason about:** **reflex tachycardia** (baroreflex-driven, with direct catecholamine-mediated inotropic and chronotropic stimulation), **fluid and sodium retention**, headache, flushing, palpitations, and postural hypotension. Because of the first two, sources describe these agents as **usually given with a beta-blocker and a diuretic** to blunt the reflex tachycardia and the fluid retention respectively.
  - **Hydralazine specifically: drug-induced lupus** — arthralgia, myalgia, fever, rash, pleuritis, with anti-histone antibodies; sources report it in roughly **5–10%** of patients taking hydralazine, and it is dose- and duration-related and more common in slow acetylators. Also **ANCA-associated vasculitis**, which is well described and can be severe.
  - **Minoxidil specifically: hypertrichosis** — prominent and frequently the reason for stopping, particularly in women; also **pericardial effusion** and marked fluid retention.
- **Monitoring:** blood pressure and heart rate; weight and fluid status; **ANA and clinical review for lupus features with long-term hydralazine**; echocardiography where minoxidil-associated pericardial effusion is suspected.

## Other Antihypertensives

- **What this AMH catch-all covers:** agents that do not fit the classes above — including **potassium channel openers** (minoxidil, covered above, and diazoxide), **direct renin inhibitors** (aliskiren), and agents used in specific contexts rather than for routine blood pressure control.
- **Direct renin inhibitors (aliskiren):** block renin's conversion of angiotensinogen to angiotensin I — the top of the cascade. Little used. **Must not be combined with an ACE inhibitor or ARB**, particularly in diabetes or renal impairment, where dual renin–angiotensin blockade increased hyperkalaemia, hypotension and renal impairment without benefit. Same **absolute pregnancy contraindication** as the other renin–angiotensin agents.
- **The practically important point for an intern:** when a patient is on an antihypertensive that does not fit a familiar class, **the questions to ask are the same four** — is it renin–angiotensin acting (then pregnancy, potassium and renal function matter), is it rate-limiting (then bradycardia and AV block matter), is it a diuretic (then sodium, potassium and volume matter), and **does it cause rebound on withdrawal** (then never omit a dose without a plan).
- **Sourcing note:** this catch-all subsection could not be enumerated against AMH's own contents, which is egress-blocked. **The class list above is therefore incomplete by construction** and should be reconciled against AMH section 6 before use.

---

## Batching test — Batch 2 record

| Measure | Value |
|---|---|
| Items built | 10 |
| Searches used | **8** |
| Searches per item | 0.8 |
| Items sharing a search | 4 of 10 |

**Which research genuinely shared, and which did not:**

- **Shared:** one search covered **ACE inhibitors and ARBs** together, because every source compares them directly — this was the only genuine two-for-one. One search covered **both calcium channel blocker subclasses**, since the sources are built around the DHP/non-DHP contrast. A follow-up search served **DHP oedema and alpha-1 first-dose hypotension** jointly, but only because I deliberately combined two unrelated questions into one query.
- **Did not share:** **thiazides, central alpha-2 agonists, direct vasodilators, non-selective alpha-blockers** and the **Australian first-line context** each needed a dedicated search and contributed nothing to any other entry. Each drug class has its own mechanism, its own adverse-effect profile and its own monitoring — there is no shared body of evidence the way there is for a single clinical work-up.
- **Conclusion for planning:** drug classes batch **worse** than investigations, and the reason is structural. Investigations in one work-up share a clinical question; drug classes in one therapeutic area share only a target organ. The only real savings come from **contrast pairs** (ACEi/ARB, DHP/non-DHP), which are a minority of the list.

> [!warning] **Two quality observations from this batch, both relevant to planning.**
> **(1) A search summary was factually wrong and had to be caught.** The calcium channel blocker search returned a summary stating that ankle oedema is an adverse effect of **non-dihydropyridine** agents. It is characteristically a **dihydropyridine** effect, which a dedicated follow-up search confirmed (dose-dependent, ~5% at starting doses, rising steeply at high doses). Had I taken the summary at face value the entry would have carried an inverted class fact. **This is an argument against high-throughput batching without per-item verification** — the error rate is not zero, and the errors are not obvious.
> **(2) No doses appear anywhere in this file, and they cannot.** AMH and Therapeutic Guidelines are subscription-gated as well as egress-blocked. For a build product specified as "mechanism, key agents, indications, adverse effects, interactions, monitoring", doses are not in scope — so this axis survives the block better than investigations did. But **"key agents" is as far as it goes**, and the *Other antihypertensives* entry could not be enumerated at all against AMH's contents.
