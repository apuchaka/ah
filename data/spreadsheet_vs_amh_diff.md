# Diagnoses spreadsheet (254 classes) vs AMH classification (276 leaves)

**Method note.** An automated token-overlap match called 129 entries "new". That was
wrong and is not used: it missed `SGLT2 Inhibitors` = AMH *Sodium-glucose
co-transporter 2 inhibitors*, `SSRIs` = *Selective serotonin reuptake inhibitors*,
`DPP-4` = *Dipeptidyl peptidase-4 inhibitor*, `Factor Xa` = *Factor Xa inhibitors*,
`Metronidazole` = *Nitroimidazoles*, `Ansamycins` = *Rifamycins*, and many more —
the same acronym-versus-expansion failure the conditions pass hit. The
classification below is by hand.

## C — Not a drug class (5). Out of scope for a medications reference.
ICD (Implantable Cardioverter Defibrillator) · Cardioversion · External Fixation ·
Arthroplasty · Carotid Endarterectomy. These are procedures; if they are gaps they
belong to Part D, not here.

## B — Genuinely more granular than AMH reaches (the actual new work)

These are the receptor-subtype / mechanism-subclass splits AMH's classification
does not make. Each needs a corpus check.

### High intern relevance — check first
1. **Antiarrhythmics by Vaughan-Williams class (Ia, Ib, Ic, III)** — AMH has one leaf, "Antiarrhythmics"
2. **Beta-blockers by selectivity (cardioselective / non-selective / mixed alpha-beta / with ISA)** — AMH has one leaf
3. **Calcium channel blockers (dihydropyridine vs non-dihydropyridine)** — AMH has one leaf; the split drives the clinical choice
4. **Insulins by duration of action (rapid / short / intermediate / long)** — AMH has only "Other drugs for diabetes"
5. **Mu-opioid receptor agonists, full vs partial** — AMH has only "Opioid analgesics"
6. **Opioid analgesics, strong/full vs weak/atypical**
7. **MAOIs by reversibility and selectivity (irreversible non-selective vs reversible MAO-A)**
8. **Vesicants and chemotherapy extravasation** — a ward emergency, no AMH leaf
9. **Muscle relaxants (neurotoxins)** — botulinum
10. **Anticonvulsants by mechanism (VG sodium channel, SV2A, T-type calcium, VGCC/gabapentinoids, GABA reuptake/transaminase, broad spectrum)** — AMH has "Other antiepileptics"

### Lower relevance / specialist
11. Carbacephem · Monobactams · Lipopeptides · Pleuromutilins · Bisbiguanide antiseptics
12. ALS therapies (glutamate antagonists, free-radical scavengers, apoptosis/ER-stress)
13. MS therapies by mechanism (anti-CD20, anti-VLA-4, S1P modulators, interferons, myelin decoys, pyrimidine synthesis)
14. IL-12/23, IL-17A, IL-17A/F, IL-17 receptor, IL-23 inhibitors — AMH lumps as "Other immunomodulating drugs"
15. Calcimimetics · Tyrosine hydroxylase inhibitors · P-selectin inhibitors · Megakaryocyte maturation inhibitors
16. Guanylate cyclase-C agonists · Intestinal chloride channel activators · NHE3 inhibitors · 5-HT4 agonists
17. Topical antibacterials/antifungals by mechanism (oxidising, RNA synthetase, DNA gyrase, pyridones, cell-wall)
18. Psychedelics (5-HT2A agonists) · Monoamine releasing agents · Azapirones
19. Herbal/botanical supplements · Botanical extracts · Essential fatty acids · Simple carbohydrates · Essential minerals
20. RANKL inhibitors · Sclerostin inhibitors (AMH: "Other drugs affecting bone")

## A — Already covered by an AMH leaf, checked in the 276-leaf pass
Everything else (~200 entries). Named differently but the same class: Ansamycins=Rifamycins,
Metronidazole=Nitroimidazoles, Drugs against mycobacteria=Antimycobacterials,
H1 antagonists 1st gen=Sedating antihistamines, Biguanides/Meglitinides/TZDs="Other drugs
for diabetes", Thioamides=Antithyroid drugs, Progestins=Progestogens, SERMs=SERMs,
G-CSF=Colony stimulating factors, SSRIs/SNRIs/TCAs/NaSSAs/NDRIs/SARIs=the AMH
antidepressant leaves, CGRP mAbs=CGRP antagonists, MAO-B=MAO-B, acetylcholinesterase
inhibitors central/peripheral=the Alzheimer's and myasthenia leaves, and so on.

**No re-check needed for bucket A** — those leaves already have a verdict from commit `3e543ef`.
