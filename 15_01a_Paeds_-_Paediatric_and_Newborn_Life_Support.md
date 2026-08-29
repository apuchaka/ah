---
block: Paediatrics
source: quackquackmed 15.01 Paediatric life support, Newborn life support, Intraosseous infusion
---

> [!info] Verified against current ANZCOR (Australian and New Zealand Committee on Resuscitation) Guideline 12.2 — Paediatric Advanced Life Support, Aug 2026 — **the core drug doses and defibrillation energy below already exactly match current ANZCOR recommendations**: adrenaline 10mcg/kg (max 1mg) IV/IO, amiodarone 5mg/kg (max 300mg) IV/IO, and 4J/kg initial defibrillation energy for VF/pulseless VT are all genuinely internationally standardised (ILCOR-based) figures shared between UK Resus Council and ANZCOR, not UK-specific numbers needing replacement. The adrenaline-after-3rd-shock-then-alternate-cycles timing and the 4Hs/4Ts reversible causes framework are likewise consistent with current ANZCOR guidance. This is a case where checking confirmed the content was already correct — no numeric changes needed, though for the most current version always check ANZCOR directly (anzcor.org) given resuscitation guidelines are periodically revised following international evidence reviews.

## Paediatric basic life support (BLS)

- Unresponsive? → Shout for help + open airway.
- Not breathing normally? → 5 rescue breaths.
- No signs of life? → 15 chest compressions → then 2 breaths + 15 compressions.

### Rescue breaths

- Position: neutral for infant, "sniffing" position for child.
- Mouth over mouth and nose for infant; mouth over mouth for child.
- Watch for the chest to rise and fall.

### Choking algorithm

- If coughing, encourage the cough.
- If ineffective cough and conscious: 5 back blows, 5 thrusts (chest for infant, abdominal for child).

## Paediatric advanced life support (ALS)

> [!danger] Unresponsive? Not breathing / only occasional gasps → CPR: 5 initial breaths, then 15:2. Attach defib/monitor. Assess rhythm.

| | Shockable (VF or pulseless VT) | Non-shockable (PEA or asystole) |
|---|---|---|
| Action | 1 shock (4J/kg), resume CPR for 2 min | Resume CPR for 2 min |
| Adrenaline | **After the 2nd shock**, give adrenaline 10mcg/kg IV/IO; repeat on alternate cycles (~every 4 min) | Give adrenaline ASAP; repeat on alternate cycles until ROSC |
| Amiodarone | After 3rd shock, give amiodarone bolus 5mg/kg IV/IO; repeat once more after 5th shock (or later if relapse) | — |

> [!danger] **Correction — adrenaline timing, found by the propagation check in the M2 round (2026-08-29).** This table previously said adrenaline **after the 3rd shock**, which is **UK/ERC practice, not ANZCOR**. **ANZCOR gives the first adrenaline dose after the SECOND shock in a shockable rhythm** — in children as in adults. Re-verified against ANZCOR paediatric guidance directly, not carried across from the adult file (see `PENDING_GUIDELINE_CHECKS.md` B37).
>
> **How it survived, which is the part worth noting.** [[01_Cardiovascular]] already carried this exact correction — its resuscitation box says adrenaline after the 2nd shock, "not the 3rd, as in UK/ERC practice", and calls it *"a high-stakes correction (drug timing in cardiac arrest)"*. It was never carried across to the paediatric file. Worse, **the verification box at the top of this file states the drug doses were checked against ANZCOR Guideline 12.2 and match** — and they do. The **timing was not checked**, and a reader has no way to tell that the box covers one dimension of the table and not the other.
>
> **Only the adrenaline timing has been changed.** Amiodarone after the 3rd shock is retained as written, because that is what the adult ANZCOR sequence uses and the paediatric shock number was **not** independently confirmed — propagating an unverified second change would repeat the error in the other direction.

- Call the resus team (1 minute of CPR first if alone).
- Use the ABCDE approach; control oxygenation and ventilation; investigate + treat the precipitating cause; temperature control.

> [!info] Reversible causes ("4 Hs and 4 Ts")
> Hypoxia; Hypovolaemia; Hypo/hyperkalaemia; Hypothermia; Tension pneumothorax; Toxins; cardiac Tamponade; Thromboembolism.

## Newborn life support

### Preparation

- Check and warm the resuscitaire.
- Check other equipment — masks, bag valve mask, suction, laryngoscope, ET tubes, O2, ≥2 towels.
- Ascertain PMH: gestation, antenatal history, antenatal concerns.

> [!warning] Standby for high-risk deliveries: emergency C-section; breech; twins/triplets; prematurity; instrumental delivery; eclampsia; thick meconium-stained liquor.

### At birth

- Assess colour, tone, breathing.
  - If baby is pink and crying: return to mother for 1h of skin-to-skin.
  - If not: rub vigorously while drying. Floppy babies are likely to need respiratory support.
- Assess breathing and heart rate with a stethoscope.
- If no spontaneous breathing: open the airway, give 5 inflation breaths via BVM, applying pressure of 20–30cmH2O for 2–3 seconds to inflate the newborn's lungs (goal is to open the lungs).
- If the chest is not expanding, readjust head position and try again ± direct inspection of the oropharynx & suction.
- Key indicator of response is ↑HR — check HR and breathing every 30 seconds, or establish continuous monitoring.
- After 5 inflation breaths and adequate chest expansion, if the baby is still not making respiratory effort, continue ventilation breaths at 30–40 breaths/min using 5–6cmH2O of PEEP if available. If not pinking up, add O2 stepwise.
- If HR is not improving and <60bpm, start compressions and ventilation breaths at a rate of 3:1.

### Temperature

- Use the resuscitaire while the baby is being checked. Naked, wet newborns cannot maintain body temperature.
- Hypothermia = <36.5°C for newborns — associated with increased mortality in all babies.

### Thick meconium

- If babies are delivered floppy, apnoeic, and covered in thick viscous meconium — rapidly visualise the oropharynx ± suction before stimulation and inflation breaths.
- Do not routinely intubate or suction, as there is no supporting evidence.

### Prematurity

- **Preterm = born before 37 weeks** gestation (term is 37–41 weeks). The commonly used sub-bands are **very preterm <32 weeks** and **extreme prematurity <28 weeks** — this entry previously gave **<32 weeks as the definition of preterm**, which is the very-preterm band, not the definition. Corrected by the pairs audit (2026-08-29); [[16_08-09_Antenatal_and_Perinatal_Problems]] Prematurity had it right and owns the risk factors and the complications table.
- Require stabilisation and help with temperature regulation, feeding, and respiration.

### APGAR score (at 1, 5 ± 10 minutes of age)

- Appearance, pulse, stimulation (grimace), muscle tone, respiration — each scored 0, 1, or 2.
- 7–10 = good; 4–6 = moderate; 0–3 = very low.

## Intraosseous (IO) infusion

> [!danger] Contraindications: osteoporosis, osteogenesis imperfecta, infection at the insertion site, vascular injury proximal to the insertion site, fracture in the target bone, previous IO insertion at the site within 48h.

### Equipment

- Manual needle vs semi-automatic. Semi-auto options: bone injection gun (children and adults); EZ-IO (reusable drill — 15mm needle for <39kg, 25mm needle for >40kg, 45mm needle for larger patients).

### Preparation

- Decontaminate the field. Lidocaine 1% 5mL if conscious. Syringe for blood sampling. Flush. Tape for securing. Primed infusion set ± 3-way tap.

### Site of insertion

- Best: proximal tibia, anteromedial surface (1–2cm medial to and 1–2cm distal to the tibial tuberosity).
- Others: distal femur, distal tibia, proximal humerus.

### Procedure

- Clean with antiseptic, lidocaine.
- Insert the IO needle at 90° to the skin. Advance with a screwing motion to the marrow cavity.
- Correct location = decreased resistance on entering the marrow cavity.
- The needle flange should not touch the skin, to prevent necrosis.
- Verify position by aspirating bone marrow, or by flushing NaCl without infiltration of surrounding tissue.
- The needle should stand upright without support, but secure with tape.
- Connect to the IV infusion via extension ± 3-way tap.

> [!warning] Complications: extravasation, dislodgment, local infection, necrosis, fracture, pain, compartment syndrome, emboli. More common with prolonged use — discontinue once IV access is achieved (aim <24h).

## Common Childhood Injuries

> [!note] Gap-filled from CSV ("Common Childhood injuries," Medium yield) — genuinely absent as a general approach despite specific injury types being covered individually elsewhere in this project (e.g. [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] for NAI-related fracture patterns, [[04_Neurology]] CT Head, Head Injury, and Intracranial Pressure for head injury Ix/Mx). Verified against AIHW national injury data and RCH Melbourne's Trauma Service guidance, Aug 2026.

**Why children are injured differently from adults — the underlying framework worth holding in mind rather than a list to memorise:** injury patterns in children reflect their stage of development, not just smaller-scale adult trauma — infants reach, grasp, and mouth objects (foreign body risk) before rolling and "cruising" around furniture (fall risk); pre-schoolers gain mobility and curiosity without a mature sense of hazard (falls, burns, unintentional ingestions dominate this age group); older children and adolescents shift toward sporting and higher-mechanism injuries as their activities change. **Falls are the single most common cause of childhood injury across all ages** — the majority of infant injuries specifically occur at home.

**Australian injury epidemiology (AIHW):** children aged 1–4 have the highest rate of head and neck injury ED presentations of any paediatric age group, with boys higher than girls throughout; open wounds are the most common specific injury type to the head/neck in this data. A separate Western Australian study found falls were the leading cause of injury-related hospital admission, with fractures (radius/ulna most commonly) and head injuries the most common consequences — head injury specifically was the most common injury type in infants and toddlers, while fractures predominated in older children and teenagers.

**Minor head injury — approach (per RACGP Australian guidance):**
- Determine mechanism (fall height, surface, what — if anything — was struck) and assess with the **Children's Glasgow Coma Scale** (age-appropriate modification of the adult GCS, given verbal response criteria differ meaningfully in pre-verbal children) — see [[04_Neurology]] Glasgow Coma Scale (GCS) for the general framework this modifies, not repeated here.
- Screen specifically for confusion, disorientation, perseveration, retrograde/anterograde amnesia, nausea, vomiting, headache, lethargy, and visual changes.
- Pupil examination — size, symmetry, direct/consensual light reflexes, and any fixation/dilation (raises concern for herniation or brainstem injury).
- Most childhood head injuries are minor, but the mechanism and age-specific injury pattern above should inform the threshold for imaging/observation — see [[04_Neurology]] CT Head, Head Injury, and Intracranial Pressure for the fuller Ix/Mx approach this feeds into, not repeated here.

**Burns — first aid (per Better Health Channel, Victoria):**
- **Cool running water for a minimum of 20 minutes** is the correct immediate first aid for a burn or scald — never ice, oil, butter, or other home remedies/ointments, given these can worsen tissue damage or introduce infection risk.
- Seek medical attention if clothing is stuck to the burn site, or if the burn involves the face, hands, genitals, or a large body surface area — these locations/extents carry disproportionate functional and cosmetic risk and warrant a lower threshold for specialist assessment.

**Foreign body ingestion/insertion:** a very common paediatric ED presentation given young children characteristically explore objects by mouth — screen for choking risk and airway compromise first; nasal and aural foreign bodies are also common and generally lower acuity than ingested/inhaled foreign bodies, but still warrant assessment given the risk of local tissue injury or, rarely, migration.

**When an injury pattern doesn't fit the history:** given how common minor childhood injury is, it's precisely this context in which recognising an inconsistent or implausible mechanism matters most — see [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] Non-accidental injury (NAI) for the specific red-flag injury patterns and approach, not repeated here; the vast majority of childhood injury is genuinely accidental and reflects the developmental patterns above, but this differential should remain active rather than being set aside by default.

**Cross-reference:** see [[04_Neurology]] CT Head, Head Injury, and Intracranial Pressure and Glasgow Coma Scale (GCS), and [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] for the disease-level and safeguarding detail this entry connects to, not repeated here.
