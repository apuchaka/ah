---
block: Pharmacology
source: Built in Phase 5 Part C from the AMH therapeutic classification (SA Medicines Formulary Framework, Appendix 1) and the Diagnoses spreadsheet class list. Not derived from quackquackmed.
---

# Medications Reference

**Scope, and what this file deliberately is not.**

This file holds **drug content built in Phase 5 Part C and afterwards** — mechanism,
Australian dosing, monitoring, contraindications — organised by therapeutic class.

- **Nothing was moved here.** Drug content that already lived in organ-system files
  before this file existed stays where it is. This file is additive only, so no
  cross-reference anywhere else in the corpus was broken to create it.
- **Drug content lives once, here.** Entries cross-reference *out* to the clinical
  and disease files rather than duplicating clinical context, so there is one place
  to correct a dose.
- **Both sources sit side by side.** Where the AMH classification and the Diagnoses
  spreadsheet describe the same drugs at different granularity, or disagree, both
  are shown in the same entry rather than split across files.

**Sourcing standard for everything in this file.** Australian primary sources are
blocked by this environment's network egress proxy, so entries are built from
cross-verified search snippets: **three independent agreeing sources for any dose,
threshold or timing window; two for non-numeric content**. Where sources disagree the
figure is **omitted and the disagreement recorded**, never resolved by picking one.
Every entry carries its own sourcing banner. All of it is provisional until checked
against a primary source — tracked in `PENDING_GUIDELINE_CHECKS.md`.

---

## Cardiovascular

### Antiarrhythmics — the Vaughan-Williams classification

> [!warning] **Snippet-sourced — primary source not read.** Cross-verified across the MSD Manual Professional table, StatPearls, CV Pharmacology and LITFL; the CAST/flecainide material additionally across *Heart Rhythm* and Drugs.com. Australian primary sources are egress-blocked. Tracked in `PENDING_GUIDELINE_CHECKS.md`.

**Why this entry exists.** The corpus prescribes amiodarone, sotalol, flecainide, digoxin, verapamil and diltiazem across several files, but the phrase "Vaughan-Williams" and the class labels appear **nowhere** — zero hits corpus-wide. The classification is what makes the drug choice reasoned rather than memorised, and it is examinable.

The classification is by **effect on the cardiac action potential**.

| Class | Target | Effect | Examples |
|---|---|---|---|
| **Ia** | Fast Na⁺ channels — moderate block | ↑ QRS, ↑ QT | quinidine, procainamide, disopyramide |
| **Ib** | Fast Na⁺ channels — weak block | little QRS change | lignocaine, mexiletine, phenytoin |
| **Ic** | Fast Na⁺ channels — strong block | marked ↑ QRS | **flecainide**, propafenone |
| **II** | β-adrenoceptors | ↓ AV conduction, ↓ rate | metoprolol, atenolol, propranolol, esmolol |
| **III** | K⁺ efflux | ↑ action potential duration, ↑ QT | **amiodarone**, **sotalol**, ibutilide, dofetilide |
| **IV** | L-type Ca²⁺ channels (AV node) | ↓ AV conduction | **verapamil**, **diltiazem** |

> [!danger] **The one that kills: class Ic in structural heart disease.** Flecainide is **contraindicated in prior MI, significant structural heart disease including HFrEF, and ventricular arrhythmia with congenital heart disease.** This is not a theoretical caution — the **CAST** trial was stopped because post-MI patients with ventricular ectopy given flecainide died *more often than placebo*. Stable coronary disease, LV hypertrophy and even mild valvular disease are all treated as high-risk settings. **Before flecainide, the question is always "is the heart structurally normal?"**
>
> Mechanistically the risk follows from the class: strong sodium-channel block widens QRS, and the block is **rate-dependent**, so it worsens exactly when the heart speeds up or becomes ischaemic.

> [!note] **The classification leaks, and knowing that is part of knowing it.** Several agents act across classes — **amiodarone is nominally class III but also has sodium-channel, calcium-channel and beta-blocking activity**, which is why its side-effect profile is unlike any other antiarrhythmic. Sotalol is class III *and* a non-selective beta-blocker. Treat the class as a first approximation, not a complete description.

> [!info] **Digoxin and adenosine sit outside Vaughan-Williams entirely** — digoxin acts via Na⁺/K⁺-ATPase inhibition and vagal tone, adenosine via A1 receptors causing transient AV block. A classification that has no slot for two of the drugs an intern actually gives is worth recognising as incomplete.

**Cross-references — clinical context lives in the disease files, not here:**
- Atrial fibrillation rate and rhythm control → [[01_Cardiovascular]] Atrial Fibrillation
- Adenosine in SVT, and its mechanism → [[01_Cardiovascular]]
- Amiodarone's thyroid effects → [[06_Metabolic_Medicine_and_Endocrinology]]

**Source disagreement:** none encountered. No dose is stated in this entry — the class table is mechanism-level, and Australian dosing for individual agents needs eTG.

### Beta-blockers — selectivity, and why the choice is not interchangeable

> [!warning] **Snippet-sourced — primary source not read.** Cross-verified across *Current Medical Research and Opinion* 2024 (two separate reviews), bpac<sup>nz</sup>, AAFP and the OHSU Drug Class Review. Australian primary sources are egress-blocked. Tracked in `PENDING_GUIDELINE_CHECKS.md`.

**Why this entry exists.** The corpus prescribes metoprolol, atenolol, bisoprolol, carvedilol, propranolol and labetalol, and warns to avoid beta-blockers in asthma — but the words **"cardioselective"** and **"intrinsic sympathomimetic activity"** appear **zero times** corpus-wide. The warning is there without the property that generates it.

| Group | Agents | Property that matters |
|---|---|---|
| **β1-selective (cardioselective)** | bisoprolol, metoprolol, atenolol, nebivolol | Less β2 blockade, so less bronchoconstriction |
| **Non-selective** | propranolol, timolol, sotalol | Block β2 as well — bronchospasm risk |
| **Mixed α/β** | **carvedilol**, **labetalol** | Also block α1 → additional vasodilatation and reduced peripheral resistance |
| **With ISA** | pindolol | Partially *stimulates* while blocking → less bradycardia |

> [!danger] **Cardioselectivity is dose-dependent, not absolute — this is the point most often missed.** β1-selective agents block β2 as the dose rises. **Atenolol is the weakest of the "cardioselective" group** and blocks roughly a quarter of β2 receptors at its higher recommended dose; bisoprolol and nebivolol are the most selective. In a controlled COPD comparison at maximum recommended doses, **atenolol increased airway resistance while bisoprolol did not.**
>
> So "cardioselective" is a reason to choose bisoprolol over propranolol in a patient with airways disease — **not** a reason to treat any β1 agent as safe at any dose.

> [!danger] **Only three beta-blockers have mortality evidence in heart failure with reduced ejection fraction: carvedilol, bisoprolol, and metoprolol *succinate* (extended-release).** This is a class where the agents are **not** interchangeable, and the salt matters — metoprolol **tartrate** is not the formulation with the HFrEF evidence. In the COMET trial carvedilol reduced mortality compared with metoprolol tartrate.

**Reading the group in one line:** selectivity decides the airways question, α-blockade decides the vasodilator question, ISA is a curiosity you should recognise but rarely prescribe, and heart failure has its own three-drug list that overrides all of the above.

**Cross-references — clinical context lives in the disease files:**
- Heart failure management and the four pillars → [[01_Cardiovascular]] Heart Failure
- Beta-blockers in asthma and COPD → [[02_Respiratory]]
- Beta-blocker overdose and glucagon → [[03a_Anaesthetics_Primer]] / toxicology content
- Timolol eye drops and their systemic absorption → [[05_Ophthalmology]] Glaucoma and Anti-Glaucoma Medications

**Source disagreement:** none material. **No doses stated** — target doses for the three HFrEF agents are exactly the kind of AU-specific numeric that needs eTG or the Heart Foundation, and no three agreeing sources were obtained.

## Endocrine

## Neurological

## Psychotropic

## Analgesia and anaesthesia

## Anti-infective

## Other
