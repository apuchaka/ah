---
name: master-verification-workflow
description: Reusable prompt + workflow for reverifying the Grind Time intern exam notes — runs the full technique set (structural, CSV, mechanism, equity, dosing, citation-accuracy) against any file range, including the cross-cutting History/Examination/Investigation/Communication files.
---

# Master Verification Workflow — Grind Time Intern Exam Notes

## The Queue — say "next" and this is what runs

This is the single source of truth for sequencing. Work through it top to bottom. After finishing an item, mark it done (✅) with the date and a one-line result, then move to the next unmarked item.

**Status key**: ⬜ not started · 🔶 in progress (some rounds done, more planned) · ✅ done for now (not necessarily exhaustive — see the file's own history for what's actually been covered)

### Phase 1 (reordered to the front) — full exhaustive CSV-pull sweep for every category that's never had one

**Why this moved to the front**: every major gap found in this entire project — Geriatrics, GP/Ethics/Communication, MSK's Achilles/AC joint, Obstetrics' Newborn Exam — came from this exact technique (pull every row for a category, spot-check the most distinctive items, verify depth not just presence). It's cheap relative to deep verification and has a 100% hit rate on categories tested so far except two (Sexual Health/STIs, Clinical Process/EBM, both confirmed already fine). Six categories have never had this treatment at all — running it on all six before anything else front-loads the highest-expected-value work.

| # | Category | Rows | Status |
|---|---|---|---|
| P1 | ENT | 20 | ✅ 2026-08-28 — full pull run. 2 MISSING candidates, both artifacts or mis-filed MSK rows; no ENT gap. 5/20 rows are not ENT topics at all (see CSV-defects note below). |
| P2 | Immunology, Allergy & Infectious Disease | 39 | ✅ 2026-08-28 — full pull run. 0 MISSING. **One genuine gap found and built: Allergic Rhinitis (High yield), now in `13_04`.** |
| P3 | Psychiatry & Mental Health | 53 | ✅ 2026-08-28 — full pull run. 3 MISSING candidates, all umbrella-term artifacts. **Seasonal affective disorder corrected — it stated "little evidence for light therapy," which is wrong.** |
| P4 | Paediatrics | 31 | ✅ 2026-08-28 — full pull run. 0 MISSING, 0 genuine gaps. The cleanest of the six. |
| P5 | Gynaecology & Breast | 40 | ✅ 2026-08-28 — full pull run. 2 MISSING candidates, both artifacts. **One genuine gap found and built: Abnormal Uterine Bleeding approach (4 CSV rows), now in `17_02`.** |
| P6 | Ophthalmology | 34 | ✅ 2026-08-28 — full pull run. 1 MISSING candidate, an umbrella-term artifact. 25/34 rows have a dedicated header; the strongest-covered of the six. |

**Phase 1 result (2026-08-28): 8 MISSING candidates across 217 rows → 7 artifacts, 1 genuine absence.** The artifact ratio held at the level the Neurology validation predicted. Three genuine gaps were found by *depth* checking rather than by presence checking — the presence scan reported all three as FOUND. Fixed in place: Allergic Rhinitis (`13_04`), Abnormal Uterine Bleeding approach (`17_02`), Seasonal affective disorder correction (`14_01`).

**Flagged for a later round, not built here:**
- **Hamstring / biceps femoris tear** — the one genuine absence (zero hits corpus-wide). It is a *Musculoskeletal* topic mis-filed under ENT in the CSV, and belongs to an MSK round, not an ENT one.

### Flagged for a dedicated MSK round

| Topic | CSV category (as filed) | Correct home | Status |
|---|---|---|---|
| **Hamstring / biceps femoris tear** | ENT (mis-filed) | `11_05_Ortho_-_Knee_and_Ankle` or `11_04_Ortho_-_Hip` | ⬜ confirmed absent corpus-wide, 2026-08-28 (P1 sweep). Zero hits on any spelling. Low yield, but a genuine absence rather than a search artifact. |
| **Acromioclavicular joint injury** | Musculoskeletal | `11_02_Ortho_-_Upper_Limb` | ⬜ pre-existing flag from Step 24 — has the Rockwood grading but lacks S/Smx and Ix detail. |

> [!warning] The checklist CSV itself contains defects, found during this sweep. These are **not** content gaps and must not be treated as such:
> - **Mis-categorised rows.** ENT is the worst: 5 of its 20 rows are not ENT topics (`Biceps femoris (Hamstring) TEARS`, `meniscal tear` → MSK; `Sick Sinus Syndrome` → Cardiology; `ECG (start early…)`, `FBC, UEC, LFTs — the "core bloods"…` → investigations). Also `Intrauterine growth restriction (IUGR)` filed under Gynaecology rather than Obstetrics, and `Scleroderma`, `Sjogren's Syndrome`, `Vasculitis` under Immunology/ID rather than Rheumatology.
> - **Misspellings.** `Acute Labrynthitis` (labyrinthitis), `Angiodema` (angioedema), `Viral Preumonitis` (pneumonitis), `Henoch-Schölnein Purpura` (Schönlein), `Endopthalmitis` (endophthalmitis), `Tredelenburg` (Trendelenburg, Neurology). Each produces a false MISSING unless the scan's fuzzy tier catches it.
> - **Duplicate rows within a category**, which inflate the apparent row counts: Psychiatry has `Anxiety and panic`/`Anxiety disorders`, `Bipolar affective disorder`/`Bipolar disorder`, and four overlapping substance rows; Ophthalmology has `Glaucoma`/`Acute Glaucoma`/`Acute angle closure glaucoma`/`Chronic Glaucoma`/`Primary open-angle glaucoma`; Gynaecology has `Polycystic ovarian syndrome (PCOS)`/`Polycystic ovary syndrome`.
>
> Treat the CSV as the primary checklist, not as an authority on naming, spelling, or categorisation.

Each of these is a "next" on its own: pull the full row list, spot-check the most distinctive/least-obviously-covered items (not the broad ones), verify depth where present, fix any confirmed gap in the same round where practical, and flag it for a dedicated build round if the gap is large (Geriatrics/GP-Ethics-sized).

### Phase 2 — new content (confirmed gaps from Steps 21/23, plus anything Phase 1 adds)
| # | Item | Status |
|---|---|---|
| N1 | Geriatrics/Older Persons Health build | ✅ 2026-08-28 — audited all 11 CSV rows, then built 8 topics. See note below. |
| N6 | GP/Preventive Med/Ethics/Communication build | 🔶 2026-08-28 — all 29 rows audited; 6 topics built. 16 rows remain, allocated but unbuilt — see note below. |
| N3 | Injury/Poisoning/Envenomation/Environmental build | ✅ 2026-08-28 — audited; both confirmed gaps (Burns and scalds, Major trauma primary survey) built in `11_09b`, with Steps 5/6/10/18 applied in the same round. |
| N2 | Public Health/Epidemiology build | 🔶 2026-08-28 — audited; 2 High-yield topics built. 4 rows remain. |
| N4 | Australian Context of Health build | ✅ 2026-08-28 — audited. **Judgment: 2 of 4 rows need no build** (distributed content is correct architecture); 2 remain, both Low yield. |
| N5 | Clinical-Process-EBM-Consent-Capacity.md confirmation pass | ✅ 2026-08-28 — both CSV rows closed. Capacity confirmed excellent (re-read, not inherited). Clinical formulation was confirmed absent in an earlier round and is now **built** — in `History-Taking.md`, overriding this table's allocation. |
| N7 | Sexual Health/STIs depth-confirmation pass (`08_08`, `17_07`) | ✅ 2026-08-28 — audited from scratch, treated as genuinely unaudited. All 12 CSV rows checked. **4 fixes, one commit each**: two wrong regimens (see the un-propagated-correction note below), a dangling positional reference, and HPV vaccination added to genital warts. **1 build**: The STI Check (the 7th conflation instance). |

> [!info] **State of play as at 2026-08-28 (end of session).**
> **Phase 1 (P1–P6): complete.** All six categories fully pulled and audited.
> **Phase 2: complete — all 7 items (N1–N7).**
> **Phase 3 (M1–M10): complete 2026-08-29** — all ten largest files. What it found is not what a 'verification pass' on already-worked files was expected to find: **four content errors with clinical consequence** (paediatric adrenaline timing, the UK 3HR latent-TB regimen, anti-VEGF given as an infusion, and cognitive cutoffs applied without their validity caveat), plus **five terms defined nowhere in the corpus despite heavy use** (IVIG, MELD, TIPSS, DDAVP, MPAA).
> **Phase 4 — large-file tier (L1–L10): complete 2026-08-29.** 39 medium/small groups remain ⬜.
> **What the L tier found is a different shape from Phase 3's.** Almost nothing was wrong *inside* an entry. The defects were **between** entries: a topic named in one file with its management in another and nothing joining them (hyposplenism, GBS); a threshold in one file with its validity caveat in another (Centor/ARF); two schedules disagreeing (NIP); a scoring tool whose components did not sum (ORBIT, Alvarado); and ~20 cross-references pointing at plausible-but-wrong header names. **The medicine was sound; the seams leaked.**
>
> **→ NEXT ITEM: Phase 4.** No Phase 2 work remains. Two Low-yield rows from N4 were deliberately left unbuilt (recorded in the N4 result below as a judgment, not an omission).
>
> **What "Phase 2 complete" means, stated carefully given this document's record.** Every CSV row in the seven Phase 2 categories has been read against the corpus with the teach-vs-mention lens, and every genuine gap has been built or explicitly declined with a reason. It does **not** mean the seven categories are verified complete — Steps 18–20 have still never been run against most of this content, and each new technique this project has invented has found something the previous ones could not.
>
> **Corpus: 148 content files.** Grew from 146 this session — `18_Geriatrics_and_Older_Persons_Health.md` and `19_General_Practice_and_Preventive_Medicine.md`. `check_structure.sh` `EXPECTED_CONTENT` is set to 148.
>
> **Standing caution carried into the next session:** this document's own status claims have now been **proven wrong five times** — SNAP (N6), sensitivity/specificity (N2), and the **Step 17 UK-localisation sweep** (see the Step 17 section). The first two shared a cause: conflating *mentioned in passing* with *built as a topic*. The third and fourth share a third cause, and it is the one to watch: **a scan was run, it returned the evidence, and the evidence was cleared without being read.** Step 17 was recorded by what it changed rather than what it examined; the stranded-reference count was recorded as "one instance" after a grep returned the other eighteen and one of them was opened. **Four instances across three distinct failure modes makes unreliable self-reporting a property of this document, not a set of isolated errors** — and the newest mode is the most dangerous, because it produces a confident negative rather than a silence. Treat every status claim here — "confirmed present", "confirmed absent", "sweep run", "clean" — as unverified until re-read against the corpus.

**N1 result (2026-08-28).** All 11 CSV rows were audited by reading what each search hit actually contained before building anything — three turned out to be adequately covered already and were deliberately **not** duplicated: capacity assessment (`Clinical-Process`), the cognitive screening tools (`Investigation-Interpretation`), and osteoporosis management (`11_08b`, already verified against the 2024 RACGP/Healthy Bones guideline). Eight topics were built, one commit each:

| Topic | Built in | Why there |
|---|---|---|
| Falls in Older People | `18_Geriatrics_and_Older_Persons_Health` (new file) | No organ system owns it |
| Frailty | `18_…` | Same |
| Polypharmacy and Deprescribing | `18_…` | Same |
| Abuse of Older People and Carer Stress | `18_…` | Mirrors `15_24a`'s NAI structure; reciprocal cross-link added |
| Discharge Planning and Home Safety | `18_…` | Same |
| Delirium vs Dementia vs Depression | `04_Neurology` | Both anchors (Dementias, Delirium) already live there |
| Mild Cognitive Impairment | `04_Neurology` | Prodrome of the dementias listed below it |
| Goals of Care and Ceiling of Care | `Communication` | Completes the thought the DNACPR entry starts |

Corpus is now **147 content files**; `check_structure.sh`'s `EXPECTED_CONTENT` was updated in the same commit as the new file.

**Method note worth carrying forward:** the presence scan reported Falls as `FOUND` *with a header* — the hit was the OSCE communication station, not clinical content — and reported the MCI row as `PARTIAL` with a 4,159-character section, which was the cognitive-tools entry with MCI mentioned once as an acronym. Both would have read as covered without opening the files. **Read the hit, don't trust it.**

---

**N6 result (2026-08-28).** All 29 rows audited by reading each hit. Result: **7 adequately covered, 6 partially present, 16 genuinely absent** — *not* the "roughly half already covered" previously assumed.

> [!warning] **Correction to this document's own Step 23 findings.** The Step 23 entry below lists "smoking cessation/SNAP (appropriately scattered as a risk factor across many disease entries)" as **confirmed present**. That is wrong. Smoking cessation is mentioned widely; **the SNAP framework itself had zero corpus-wide hits** (every match was "opening snap"/"snapping"). The earlier pass conflated *mentioned as a risk factor* with *built as a topic* — a failure mode worth watching for elsewhere in this document's confirmed-present lists.

**Placement rule used** (new file as last resort, not default): consultation skill → `Communication.md` · clinical process/ethics/legal → `Clinical-Process-EBM-Consent-Capacity.md` · preventive/screening **content** → the organ-system file that already owns it · new file only for what fits none of those.

**Built, one commit each:**

| Topic | Built in | Rows covered |
|---|---|---|
| Domestic and Family Violence | `Communication.md` | Domestic violence (High) |
| Motivational Interviewing and the Stages of Change | `Communication.md` | Motivational interviewing (High) |
| Clinical Handover (ISBAR) and Prioritisation | `Communication.md` | Giving/receiving handover (Medium) |
| Preventive Medicine and Screening | `19_General_Practice_and_Preventive_Medicine` (new) | Preventative medicine (High); Immunisation (High, partial) |
| Lifestyle Risk Factors (SNAP) and Smoking Cessation | `19_…` | Life Style related Diseases (SNAP) (Medium) |
| Continuity of Care, and What Makes General Practice Different | `19_…` | Continuity of care (High); Unique features of GP (Medium) |

**All five High-yield gaps are now built.** Corpus is **148 content files**; `EXPECTED_CONTENT` updated in the same commit as the new file.

### N6 round 2 built (2026-08-28)

Five CSV rows closed across four commits, prioritising the two named as highest value:

| Topic | Built in | Rows |
|---|---|---|
| Explaining a Medical Error — Open Disclosure | `Communication.md` | Explaining a medical error |
| Mandatory Reporting — the Overarching Duty | `Clinical-Process-…` | Mandatory reporting (overall skill) |
| Talking to Angry Patients and Relatives, and Managing Complaints | `Communication.md` | Angry patients; Managing complaints |
| Documenting in the Medical Notes | `Clinical-Process-…` | Documenting in the medical notes |

**Two findings worth carrying forward.** *Mandatory reporting* was recorded as "partial" because four condition-specific instances existed — but **zero corpus-wide hits for Ahpra or notifiable conduct** meant the duty to report an unsafe **colleague** was absent entirely; "partial" understated it. And *documentation* was **instructed in about a dozen entries** across the project with no entry saying what good documentation consists of — the instruction was everywhere, the content nowhere.

### N6 round 3 built (2026-08-28)

Three rows closed. **Steps 5, 6, 10 and 18 applied during each build rather than deferred** — three prior rounds ended with the same "new content needs a verification pass" caveat, so the pass is now part of the build.

| Topic | Built in | Step 10 outcome |
|---|---|---|
| Assessment and Basic Management of Pain | `03a_Anaesthetics_Primer` | **Built** — sourced disparity, incl. the clinician-side "more stoic" belief |
| Professional Boundaries, and the Inappropriate Patient | `Communication.md` | **Declined** — no sourced disparity; general cultural-safety principle only, labelled as such |
| Explaining a Safeguarding Referral | `Communication.md` | **Declined** — relevant equity content already sits in the entries this one cross-references |

**N2 and N5 result (2026-08-28).** All 6 Public Health/Epidemiology rows and both Clinical Process rows are now closed. Built this round: **study design and bias**, **p-values and confidence intervals**, and **screening principles** (all in `Clinical-Process-EBM-Consent-Capacity.md`, replacing that file's own "Evidence-based medicine — a brief note" placeholder, which had recorded these as unbuilt), plus **clinical formulation**. Previously closed: NNT/ARR/RRR and sensitivity/specificity (built), notifiable diseases (confirmed adequate).

**Placement override #3, and the reasoning, since the previous two were both correct.** This table allocated **clinical formulation** to `Clinical-Process` alongside N5. It was built in **`History-Taking.md`** instead: formulation is the synthesis step immediately after the psychiatric history that feeds it and the MSE it pairs with, and placing it in `Clinical-Process` would have left a reader arriving at the synthesis with both of its inputs in a different file. **Screening principles** was a placement *decision* rather than an override (the table named no file): it went to `Clinical-Process` rather than `19_`, because it builds directly on the Diagnostic Test Characteristics entry already there — PPV falling with prevalence is the arithmetic behind why a screening programme generates mostly false positives — and duplicating theory into `19_` would have repeated the screening-table error from an earlier round. `19_` carries a forward cross-reference instead.

**N7 result (2026-08-28).** Treated as genuinely unaudited rather than assuming earlier passes had covered it, since this item was structurally unreachable from the queue until it was added. All 12 CSV rows checked against `08_08` and `17_07`. **Nine rows adequately covered** and deliberately not touched — chancroid, donovanosis and LGV are thin, but they are Low yield and rare in Australia, which is the correct depth rather than a gap; herpes zoster ophthalmicus is built in `05_Ophthalmology`; PrEP/PEP in `08_05-06`. **One row genuinely absent and built** (the STI check). **Three contained defects fixed**, none of which any scan would have surfaced *at the time* — one of the three has since produced a scan, and 18 further instances (see below).

> [!warning] **A failure mode this project had not previously named: the un-propagated correction.** Both the chlamydia and gonorrhoea regimens in `08_08` were **wrong**, and both had **already been found and corrected in `17_08`** in an earlier round, each with an explicit "genuine correction" box recording what the error was. Neither correction was carried across to `08_08` — **the file that is the corpus's primary STI reference**, and therefore the one a reader goes to first. The gonorrhoea error was a **double dose** of ceftriaxone plus a cefixime alternative that `17_08` explicitly names as not Australian first-line.
>
> This is **distinct from the conflation pattern**. Conflation is about mistaking a mention for a topic; this is about **fixing a claim in the file you happen to be working in without sweeping the corpus for the same claim elsewhere**. It leaves the corpus in a worse state than before the correction, because two files now disagree and the one carrying the error looks authoritative.
>
> **Scope check run immediately afterwards, so this is bounded rather than assumed:** every in-corpus "genuine correction" box was grepped and its subject checked for duplicates elsewhere. The HSV 6-weeks-before-delivery correction **was** correctly propagated (`08_05-06` and `08_08` both carry it); the eclampsia magnesium loading dose has no conflicting duplicate. **The STI regimen pair is the only confirmed instance** — one instance, not yet a pattern. **The standing rule it produces: when a correction changes a specific figure or regimen, grep the corpus for that figure before committing.**

> [!warning] **The stranded positional reference — now the most widespread single defect found in this project, and the scan for it is built.**
>
> **Found as:** the chlamydia partner-notification box in `08_08` compared the Australian window against "the UK figures below" three times, but the UK figures had been deleted when the entry was localised. **Cause:** a localisation pass writes a verification box contrasting AU practice against the UK content it is replacing, then removes that UK content, leaving the box comparing against a void.
>
> **⚠️ Correction to this document's own record, made 2026-08-29 — the fourth time a status claim here has been proven wrong.** The N7 entry originally recorded this as **one instance**, on the strength of "a bounded manual grep for `UK…below` variants found no second instance." **That was false, and the grep was not the problem — the triage was.** The grep returned the other instances; they were in its output and were cleared without being opened. A dedicated scan then found **18 more across 12 files**, every one confirmed by reading the target region:
>
> `01_Cardiovascular` · `03_Gastrointestinal` (×4) · `03a_Anaesthetics_Primer` · `04_Neurology` · `07_Renal_Medicine_and_Urology` (×2) · `08_01-03_Bacterial_Infections` (×2) · `09_05_Dermatology` · `10_08_Blood_Products` · `10_11a_Oncology` · `11_08b_Ortho` (×2) · `15_03b_Paeds_HIV` · `15_24b_Paeds_Screening`
>
> **Three were worse than a dead pointer.** `08_01-03` twice warns the reader not to quote "the UK list below" / "The UK schedule above" as the Australian standard — implying the corpus carries UK content it does not, and inviting a reader who cannot find it to assume the *Australian* table beside it is the thing being warned about. `11_08b` says strontium should not be offered "the way the UK-style note below suggests", while the list below already says strontium is no longer recommended in Australia: **the reference contradicts what actually follows it.**
>
> **The lesson is not about greps.** The rule "zero grep hits is not proof of absence" was already in `CLAUDE.md`; what failed here is its mirror image — **a grep that returns hits is not cleared by reading one of them.** Rule 3 already says every scan hit must be verified individually against file content. The dismissal was the violation, not the tooling.
>
> **`scripts/positional_refs.py` now exists** and carries three of its own mistakes as regression fixtures: resolving against the leftmost qualifier instead of the nearest one; counting *commentary about* absent content as evidence the content is present (which graded three genuine strands OK); and a self-test written against live corpus lines, which dissolved the moment those lines were fixed. **Its remaining blind spot is prose:** "as described earlier", "the approach set out previously" carry no positional keyword and are invisible to it — the same class of defect one level up.
>
> **Standing manual check, for what the scan cannot reach:** when a localisation pass removes source-note content, re-read every verification box in that file for a reference to what was just deleted. The box and the deletion are always in the same edit; nothing else is positioned to catch it.

> [!info] **What `undefined_terms.py` asks, and the question it does *not* ask — established by the abbreviation triage, 2026-08-29.**
> Of the five non-obvious abbreviations it surfaced, **three were artifacts** (CT-TAP, PERT, IAP): each was already expanded in parentheses at its main use site, which none of the scan's patterns could see. A dismissal rule now covers that, in both directions and with an initial-overlap test — added only after the first version of the rule wrongly dismissed "Tuberculous meningitis (CNS)" and "haemodynamic changes (HTN)", where the parenthetical is a category label rather than an expansion.
>
> **The two real gaps were of a kind this scan cannot find, and that is the durable lesson.** It asks *"is this term defined **anywhere** in the corpus?"* — not *"is it defined **where the reader meets it**?"* MART was expanded only in the paediatric file while the adult entry carries the primary asthma content; VZIG was expanded at one of its three use sites. Both were found by **reading the use sites**, not by the scan, and both would be dismissed by it today. **A term dismissed by `undefined_terms.py` may still be undefined in the file a reader actually opens.** Until a per-file mode exists, the substitute is manual: when a term recurs across files, check the file that owns the topic, not just whether some file somewhere glosses it.

> [!warning] **The PARTIAL verification box — now confirmed twice, in unrelated files.** Found in the M2 propagation check and again in the M8 scope audit, 2026-08-29. **The second instance settles that this is a pattern, not a one-off:** `02_Respiratory` gave the **UK 3HR latent-TB regimen** underneath a box verifying the **active-TB RIPE** regimen — accurate about RIPE, silent about latent TB, and read as covering both.
>
> `15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md` opens with *"Verified against current ANZCOR Guideline 12.2 — Paediatric Advanced Life Support… the core drug doses and defibrillation energy below already exactly match current ANZCOR recommendations."* **That statement is true.** The doses do match, exactly. But the algorithm table underneath it gave adrenaline **after the 3rd shock**, which is UK/ERC practice — **ANZCOR gives the first dose after the 2nd**, in children as in adults. The box verified the *doses* and not the *timing*, in a table containing both.
>
> **Why this is worse than the other four.** The previous instances were claims that were simply wrong. This one is a claim that is **accurate about what it checked and silent about what it did not** — and a reader has no way to tell which dimension of the content underneath it the box covers. It names the correct Australian guideline, which makes the surrounding content look adjudicated. A UK drug-timing figure survived a pass that explicitly cited the guideline contradicting it.
>
> **It was also an un-propagated correction.** [[01_Cardiovascular]] already carried this exact fix, and labelled it *"a high-stakes correction (drug timing in cardiac arrest)"*. So the same defect was simultaneously (a) corrected in one file, (b) uncorrected in another, and (c) sitting under a verification box in the uncorrected file.
>
> **The rule this produces: a verification box must say what it did NOT check.** Every existing "Verified against…" box in this corpus should be read as covering only the dimension it names — dose, or threshold, or sequence, or eligibility — and never the whole block beneath it. There are roughly a hundred such boxes and this is not a scannable property: a box's scope is a matter of what its author had in mind. **Where a box sits above a table, check each column independently.**

> [!info] **Same-topic-different-heading sweep — the seam the pair check cannot see (2026-08-29).**
> `check_structure.sh` pairs files by identical `##` headers. **Topics split across files under *different* headings are invisible to it**, and that is where two of Phase 4's findings lived: the **two NIP vaccination schedules** (`08_01-03` vs `15_24b`, two discrepancies) and **Centor** (an `###` section in `08_01-03` vs a callout in `13_05a`, the ARF caveat present in only one).
>
> **Three further candidates were checked by hand and are clean** — recorded so they are not re-done:
> - **`08_04` antibiogram vs the disease files' regimens** — no conflict, because `08_04` makes *no* empirical first-line claims. Its box says explicitly that the chart tells you what a drug *can* cover, not what to prescribe. **This is the model scoped box in the corpus.**
> - **Obstetric emergencies split across `16_14-15` and `16_10-13`** — deliberate and coherent: praevia/accreta/vasa in the labour file, abruption in the emergencies file, with the distinguishing box (painless praevia vs painful abruption) sited in the praevia entry where the differential actually arises, and cross-referenced across.
> - **Palliative prescribing (`10_11c`) vs pain (`03a`)** — no conflict: `03a` names opioid classes and the WHO ladder but gives **no doses or conversions**, deferring to `10_11c`, which owns them behind an explicit "figures are illustrative only" danger box.
>
> **The generalisable rule:** where two files could reasonably own a topic, the safe pattern is **one owner for the numbers and pointers from everywhere else** — which all three of these do, and which the anaphylaxis pair did not.

> [!tip] **The unit-and-progression check — `scripts/dose_tables.py` (2026-08-29).**
> Run deliberately across all 148 files after the paediatric DKA find. It asks of any table whose dose varies by weight or age: **does the progression behave sensibly on its own terms, before any source is opened?** Monotonic where clinically expected; no unexplained jump in unit scale. This is the cheapest check in the whole method — the DKA error needed no guideline to convict it, only the observation that the rate *fell* with weight and then *rose again*.
>
> **The sweep found 19 banded blocks across ~10 distinct tables; every one is listed in the report for 2026-08-29.** One genuine defect beyond DKA itself: the ASCIA adrenaline table's **missing <7.5 kg band** — the owner entry stopped at 7.5 kg while the only figure for smaller infants sat in a file that defers to it. Not a progression error but a *truncated* progression, which the same reading exposes.
>
> **Two flags that are correct and must not be "fixed":** levothyroxine going 8–10 mcg/kg → 5 mcg/kg → **50 mcg absolute**, and enoxaparin going 80 mg → **0.5 mg/kg** at ≥171 kg. Both are deliberate per-kg-to-absolute transitions — *the same shape as the DKA error and entirely right*. The unit change is the thing to read, never the thing to report.
>
> **Rule 4 disclosure.** The first detector required band and dose on separate lines, so **it would not have found the DKA table that motivated it.** Fixed before any result was trusted; that line is now fixture 1 in the script's self-test.

> [!warning] **The queue did not cover the corpus — found 2026-08-29, resuming G1–G39.**
> Nine content files were named **nowhere in this document**: not in a queue row, not in the grouping table, not in prose. The M-tier is defined as the ten largest files and reaches none of them; G1–G39 skipped straight from `08_07` to `09_01`, from `10_10`/`10_11b–c` past `10_11a` and `10_12`, and from `11_01` to `11_03`. They are now **G40–G43**.
>
> **This is the N7 shape for the second time.** N7 was "structurally unreachable from the queue until you added it", and the response then was to treat it as genuinely unaudited. The same applies here — and these files are not small: `08_01-03` (43 KB) and `08_09` (42 KB) are larger than most of what G1–G39 does cover.
>
> **Why it stayed invisible:** several of the nine *have* been edited this session — the Passive Immunisation build, the Centor ARF caveat, the travel-history citations fixed minutes before this was found. Work reaching a file through a corpus-wide scan makes it look attended-to while it has never once been walked as a unit. **Coverage by scan is not coverage by queue**, and only the second kind is recorded.
>
> **The check that finds this class:** enumerate the corpus from the filesystem and subtract what the queue names, rather than reading the queue and assuming it is exhaustive. Every prior completeness claim about the queue was made by reading the queue.

> [!warning] **The conflation pattern, now confirmed eight times.** The root is the same each time: *the corpus can reference something enough to look covered while never containing it.* SNAP was mentioned as a risk factor · sensitivity/specificity was applied to eight tests but never defined · documentation was instructed across a dozen entries but never specified · **"chaperone" appears 8× in `Examination.md`, every instance a procedural line inside an examination sequence, with professional boundaries never taught** · **"raise a safeguarding concern" is instructed in four entries with the conversation never taught anywhere** · **"refer to X" appears in over a hundred entries with the how-to nowhere** · **six immunoglobulin products are prescribed with doses and deadlines — VZIG, anti-D, tetanus, rabies, RhD, normal — while *passive immunisation* had zero corpus hits, so nothing said what class of thing they are or why the time windows exist** (found 2026-08-29 in the abbreviation triage) · **the STI check: `08_08` builds thirteen organisms in detail, and "offer testing for other STIs" / "comprehensive STI screen" / "STI screen (as indicated)" is instructed across four files, while nothing anywhere specified what an STI screen consists of** (N7, 2026-08-28 — the clearest instance yet, because the depth of the surrounding organism entries is exactly what made the absence invisible).
>
> **The check that works is not "does this term appear" but "does an entry actually teach this."** Apply it to every remaining row, and to any row this document records as covered.

**Placement override, recorded.** Pain was allocated to `19_` by the remainder table. `19_`'s declared scope is general practice as a discipline and preventive care as a system; pain assessment is neither, and placing it there would repeat the container error corrected earlier in N6. Built in `03a` instead — ANZCA is the Australian college for acute pain medicine, the file is already ANZCA-localised, and it holds regional anaesthesia and postoperative care. **The remainder table's allocations are a starting point, not binding.**

**Terminology finding — since resolved.** The Medical Board's guidelines use **"observer"** rather than "chaperone", confirmed against **section 7.1 "Use of observers"** of the primary guideline. All 8 instances in `Examination.md` updated, and the resolution surfaced a larger gap than the terminology: nothing explained what an observer is *for*, who can act as one, or what happens if the patient declines. Built as `Examination.md` **Observers in Clinical Examination**, with the Professional Boundaries subsection reduced to a cross-reference rather than left as a second copy. **This is the sixth confirmed instance of the referenced-but-never-taught pattern**, and the first found by pulling on a terminology thread rather than by auditing a CSV row — worth noting as a second way in.

### N6 COMPLETE (2026-08-28)

All 29 rows resolved: **19 built**, **7 confirmed already covered** in the original audit, **3 needing no build**.

**Final round built 4 topics, closing 5 rows:**

| Topic | Built in | Placement |
|---|---|---|
| Choosing a Medicine — Quality Use of Medicines | `Clinical-Process-…` | **override** — prescribing is clinical process, not GP discipline |
| Referral and Discussion with Other Specialties | `Communication.md` | as allocated |
| The Family, and Families in Crisis | `Communication.md` | as allocated |
| Hospital Avoidance and Potentially Preventable Hospitalisations | `19_…` | as allocated |

**Three rows correctly need no build**, and one of these was a live decision this round rather than inherited: *Initial diagnostic strategy for common GP presentations* is **already taught** in Continuity of Care, and What Makes General Practice Different — pre-test probability, watchful waiting, and safety-netting with its three components. Building it again would have been the screening-table error. *Counselling stations* — `Communication.md` **is** that. *Health promotion* — folds into the SNAP and preventive entries.

**Step 10 outcomes across the round:** built for pain, medication choice (Closing the Gap PBS Co-payment Program) and hospital avoidance; **declined for boundaries, safeguarding referral, referral to specialties and families in crisis** — no sourced disparity in any of those, and the relevant equity content already sits in entries they cross-reference. Four declines is the intended behaviour, not a shortfall.

**Two placement overrides** were made across N6, both recorded with reasoning: pain moved from `19_` to `03a`, and medication choice from `19_` to `Clinical-Process`. In both cases `19_`'s declared scope (general practice as a discipline, preventive care as a system) did not fit. **The remainder table's allocations are a starting point, not binding.**

---

### Phase 3 — mega files (M1–M10)
| # | Item | Status |
|---|---|---|
| M1 | 04_Neurology.md | ✅ 2026-08-29 — 4th round. Acronym-at-use-site check: **IVIG defined for the first time in the corpus** (13 uses, 8 files, 0 expansions); **FVC monitoring mechanism built** for GBS/MG. CSV 57 found / 6 partial / 0 missing. |
| M2 | 01_Cardiovascular.md | ✅ 2026-08-29 — **propagation check found the paediatric adrenaline-timing error** (see the partial-verification-box note above). AF risk scores given their interpretation; ALS expanded; HFmrEF band added. CSV 76/6/7 — all 7 MISSING read individually, all artifacts. |
| M3 | 03_Gastrointestinal.md | ✅ 2026-08-29 — liver severity scores given their interpretation (the section was two lists of variables); **MELD and TIPSS defined for the first time in the corpus**. |
| M4 | 06_Metabolic_Medicine_and_Endocrinology.md | ✅ 2026-08-29 — **DDAVP defined** and the water deprivation test given its logic. ABPI confirmed adequately built in `01_Cardiovascular` §0.35.2. |
| M5 | 07_Renal_Medicine_and_Urology.md | ✅ 2026-08-29 — **MPAA expanded** at first use in the KDIGO lupus nephritis regimen (a drug name, not a label). |
| M6 | Examination.md | ✅ 2026-08-29 — verification-box scope audit: only one `Verified` box exists and it is the **correct pattern**, stating its own scope limit. HINTS confirmed built to the standard the scoring-tool entries elsewhere needed fixing to reach. One consistency fix (a DNACPR citation my own M-round fix had failed to propagate). |
| M7 | History-Taking.md | ✅ 2026-08-29 — **carries zero verification boxes**, which is accurate rather than a gap: its content is technique, not guideline-dependent fact. Acronym check clean. CHECK A/B hits all expected for a history file (a history gathers, it does not diagnose or manage). |
| M8 | 02_Respiratory.md | ✅ 2026-08-29 — **second partial-verification-box instance**: the latent TB regimen was the UK 3HR, sitting under a box that verifies only active-TB RIPE. Corrected to 6–9H / 4R (B38). Asthma and ethambutol boxes audited and dismissed with reasons. |
| M9 | 05_Ophthalmology.md | ✅ 2026-08-29 — **anti-VEGF route corrected** (intravitreal injection, not infusion) with the VEGF mechanism added; **stye/chalazion built** — the only MISSING candidate the CSV produced, and genuine. Both verification boxes audited and honestly scoped. |
| M10 | Investigation-Interpretation.md | ✅ 2026-08-29 — the predicted shape found: the status box verifies **approach** and is silent on **numbers**, in a file of reference ranges and cutoffs. Box rewritten to state its own limits. **Cognitive-cutoff validity caveat built** (education/literacy/language; MMSE and MoCA not validated for many Aboriginal and Torres Strait Islander patients — KICA). Troponin confirmed exemplary. |

### Phase 4 — large files (L1–L10), then medium/small (G1–G45)
L1–L10 ✅. **G1–G9 ✅ 2026-08-29.** **G40–G43 ✅ 2026-08-29** — taken first, ahead of G1–G39, because they were the files found to be in no queue row at all and therefore genuinely unaudited. G1–G39 ⬜. **G44–G45 ⬜**, added by the same reconciliation. See the grouping table further down for exact file lists.

| Row | Result |
|---|---|
| G40 | ✅ **The GBS screening block contradicted its own verification box** — the bullets opened "Universal screening not routine for all" (the UK NICE position, asserted flatly) directly under a RANZCOG-verified box saying Australia permits either universal or risk-factor screening. **Fifth partial-verification-box instance.** Rewritten to lead with both strategies; pointer added from `16_06-07`, which owns the dosing and was silent on screening. `MOA` (4×) checked and **dismissed** — it labels toxin mechanisms, genuinely distinct from `A/P`, and normalising it would have destroyed a real distinction |
| G41 | ✅ **NRTI and NNRTI expanded and given mechanisms** — the HIV drug-class table's own "Mechanism" column gave side effects only for those two rows, in the file that owns HIV drug classes, where the stated Australian first-line is "2 NRTIs + 1 INSTI". The least-explained row was the backbone of first-line therapy. Cellulitis and necrotising fasciitis both confirmed as **clean pointer stubs** in `09_05`/`09_01` — the model one-owner pattern |
| G42 | ✅ **DIC expanded at its point of use** in the non-blanching-rash differential (owned by `10_05`, which a reader working through a purpuric rash has no reason to be in). Phyllodes tumour box **correctly scoped** — names StatPearls/NCCN honestly and does not claim Australian verification; recorded as **B51** for provenance, not as a defect |
| G1–G9 | ✅ 2026-08-29 — **zero non-Australian guideline bodies across all 27 files.** Four internal-coherence defects, every one found by reading a box against itself rather than against a source: **Ann Arbor stage 1 was a strict subset of stage 2** ("one node" vs "≥1 node on the same side" — the unit is a *region*) and the spleen was given as an example of stage-4 extranodal disease when it is lymphatic tissue carrying the **S** suffix; **the Amsterdam criteria mixed versions I and II**, pairing the Amsterdam II cancer list with Amsterdam I's colorectal-only age criterion, so a family qualifying through endometrial cancers failed the age rule; **the Hurley box announced "3 classes" and listed none**, so the classification could not be applied and the management below was untied to any stage. **`10_10a`, the file named for oncological emergencies, covered three and pointed at neither malignant spinal cord compression nor hypercalcaemia of malignancy** — both well owned elsewhere, both under headings its reader would never search, so the duplicate-header check is structurally blind to the split. Acronyms: **TRAP** and **HLA** expanded. PASI (4 regions × 3 signs, 0–72) and SCORAD ("six signs", six listed, 0–103) both checked and **internally consistent**. B52–B54 recorded. |
| G43 | ✅ Scoring-tool arithmetic clean: **Eron** 4/4 · **Durack-Street** "four categories"/4 · **Rockwood** "I to VI"/6 · **ECOG** 0–4 + the 5 note · **Centor** 4 criteria/threshold 3–4 · **Gartland** I–III, no count claimed. NIP schedule cross-checked against its own prose (ATSI 50/50/60 vs general 70/65/75 — matches exactly); the Hib ⚠️ resolves to the B47 warning as intended |

> [!warning] **The 21-pair audit (2026-08-29) — what reading pairs against each other found that reading them alone did not.**
> All 21 cross-file topic pairs surfaced by the new Step 1c-bis were audited fact by fact. **Seven carried genuine defects; six needed only links; eight were clean.** The defects divide into three kinds, and none was visible from either entry alone:
>
> **1. Outright contradictions (4).** Diphtheria — one entry framed antitoxin and erythromycin as **alternatives** ("or"), the other correctly as complementary (antitoxin neutralises unbound toxin, the antibiotic halts production). Prematurity — one file defined preterm as **<32 weeks**, which is the *very*-preterm band; preterm is <37 weeks. DiGeorge — one file called velocardiofacial syndrome "a similar condition", the other correctly "aka"; they are the same 22q11.2 deletion. Spinal epidural abscess — one listed the classic triad as the presentation while the other states it is **present in only 10%**, so reading the first alone invites the false reassurance the second exists to prevent.
>
> **2. Un-propagated corrections (1).** Lupus nephritis — `07_Renal` was updated to **KDIGO 2024** and gained "hydroxychloroquine for all patients unless contraindicated", flagged there as foundational. The rheumatology file, where a reader with SLE actually looks, never received it.
>
> **3. A fact present in only one of two entries that both need it (5).** The **IV aciclovir dose for encephalitis did not exist anywhere in the corpus** — both entries said "IV aciclovir", and the corpus's only aciclovir figures were oral regimens for cold sores and shingles. The **adult glucagon dose** existed only in the *paediatric* file. The **metronidazole 400mg BD** for trichomonas existed only inside a verification box, above a line that omitted it. The **epiglottitis antibiotic** was in one of three entries. The **rotavirus upper age limits** — the one part of the infant schedule that cannot be caught up later — were absent from the paediatric vaccination table.
>
> **The paediatric-acuity pattern held.** DKA, hypoglycaemia, epiglottitis and HUS were taken first on the theory that adult/paediatric splits of one condition are the high-risk shape, after the five-fold DKA fluid error. DKA and HUS agreed on every figure; the risk was real but landed differently — **the paediatric hypoglycaemia entry gives full management and never defines hypoglycaemia at all**, while the corpus's two thresholds (<3.3 adult, <2.6 neonatal) are both wrong to read across to a child with diabetes.
>
> **The generalisable rule:** *two entries can both be individually correct and still leave the reader worse off than one.* Silence in one and speech in the other is as much a defect as contradiction, and only comparison finds it.

> [!done] **The GBS consistency check — RUN 2026-08-29 at Phase 4 close. Found three more defects.**
> **Two GBS defects in two different files in one session** — L5 found the drug named without its dose (`08_01-03` pointing at `16_06-07`, which owns the regimen), and G40 found the UK "universal screening not routine" position asserted as fact directly under a box saying Australia permits either strategy. Two independent defects in one topic is a pattern, not a coincidence, and both fixes were local to the file in hand.
>
> **RESULT — the check was justified. Three further defects, in three files that had not been touched by the two earlier GBS fixes:**
> - **`16_01-05` listed Group B Strep under "do NOT offer routinely"** — the UK position, and *the same defect corrected in `08_01-03` earlier in the session*, surviving in a different file. **The correction did not propagate.** This is the third independent GBS defect and the second instance of this exact claim.
> - **`08_01-03` named vancomycin** as the penicillin-anaphylaxis alternative; the Safer Care Victoria-verified owner says **clindamycin**. A wrong drug on the severe-allergy pathway, inside a sentence that correctly deferred to the owner for everything else.
> - **The `≥4 hour` IAP timing was absent from the owner entry** — stated only in the file that defers to it. Timing is what makes the prophylaxis work.
>
> **The lesson, and it is about the check rather than about GBS:** two defects in one topic justified a dedicated sweep, and the sweep found three more — including one that was a *re-occurrence of a defect already fixed once*. **A per-topic sweep after two independent defects in that topic is worth running as a rule**, because the second defect indicates the topic was built from a source the corpus has not fully localised, not that two errors happened to coincide.
>
> Also found: **GBS is a two-meaning acronym** (Guillain-Barré / Group B Streptococcus) used in **both** senses inside `04_Neurology` alone — the organism at line 505, the syndrome defined at 1345. Second such collision after **PID**.

> **When Phase 4 closes, check GBS everywhere it appears** — not just the two locations already fixed. Every file mentioning GBS, intrapartum antibiotic prophylaxis, or early/late-onset neonatal GBS disease, checked against each other for: screening strategy, the risk-factor list, the IAP timing (≥4h before birth), the benzylpenicillin regimen and its allergy alternatives, and which file is stated to own which. Known sites so far: `08_01-03`, `16_06-07`, `15_22a`, `16_01-05`.

> [!tip] **The partition check — does a classification's own boundaries actually divide what it claims to?**
> Generalised from the **Ann Arbor** find (G5, 2026-08-29), where stage 1 read "One node affected" and stage 2 "≥1 node affected on the same side of the diaphragm": **stage 1 was a strict subset of stage 2.** The stages did not partition, and nothing external was needed to see it.
>
> This is the same check that caught ORBIT and Alvarado on arithmetic, but it **is not limited to numeric tools**. Apply it to any staging, grading, or classification system:
> - **Do the categories overlap?** Can one case satisfy two of them? (Ann Arbor 1 and 2.)
> - **Do they exhaust the space?** Is there a case that fits none of them?
> - **Is the unit consistent across categories?** Ann Arbor's real unit is a lymph node *region*; the box switched to individual *nodes* and the boundaries collapsed.
> - **Do the parts match the whole they are drawn from?** The **Amsterdam** criteria paired the version II cancer list with version I's colorectal-only age rule — internally incoherent across two editions of the same tool.
> - **Does a box that names a count deliver it?** The **Hurley** box announced "3 classes" and listed none.
>
> **Run it before checking any source.** A classification that does not cohere with itself is wrong regardless of what the guideline says, and the failure is usually cheaper to see from the inside.

## Phase 5 REDO — the original Part C was wrong

> [!danger] **Part C reported "nothing to build". That was a false negative caused by its own method, and the user caught it by checking their own knowledge against the report rather than by anything in the report.**
> The suffix regex (`-pril -olol -azole -mab …`) **structurally cannot reach any class without a shared suffix.** Antipsychotics, GTN/nitrates, aminoglycosides and macrolides were never in the search space — not checked and passed. Re-run with therapeutic-category enumeration scaffolded on the Medical Board specialty list, reading whole entries instead of a ±260-character window:

| Finding | Evidence |
|---|---|
| **Macrolides** | azithromycin 45 + clarithromycin 24 + erythromycin 21 = **106 uses, no section, and zero mechanism / QT / interaction content anywhere.** The one interaction mention is a CYP3A4 note inside a respiratory entry |
| **GTN / nitrates** | **31 uses, no section.** The only contraindication content is aortic stenosis and HOCM — **the PDE5-inhibitor interaction that causes fatal hypotension is absent entirely**, as is mechanism and tolerance |
| **Aminoglycosides / vancomycin** | gentamicin 15 + vancomycin 20. Toxicity appears as one antibiogram table row; monitoring appears only in a neonatal context in `16_06-07`. **No entry teaches therapeutic drug monitoring**, which is a core intern task |
| **Antifungals** | 30 uses, no mechanism or toxicity content anywhere |
| **Syringe driver / CSCI** | **absent entirely** despite a palliative prescribing file |

**Dismissed on verification — the wider net's false positives, as expected:** *Local anaesthetic systemic toxicity* (70 "uses" were the English word **"last"**; Intralipid is present) · *Antiplatelets* (**two** dedicated headers my drug-name pattern missed) · *Statins* (myopathy in `04_Neurology`, LFT monitoring in `01_CV` — distributed, not absent) · *Naloxone* (full dosing ladder in `14a-1`) · *Antipsychotics* (`14_03` has EPSE, NMS, hyperprolactinaemia, clozapine monitoring — real depth) · *Opioid conversion* (`10_11c` owns "Conversion between opioids").

## Phase 5 REDO — Parts B and D

**Part D's new check found a gap class the original could not produce.** The original could only find procedures the corpus *mentions* and under-explains. Enumerating what an intern must perform **first**, then checking the corpus, finds procedures never mentioned **at all**:

| Never mentioned once | Near-absent (<3 uses, no section) |
|---|---|
| Venepuncture · Local anaesthetic infiltration · ECG recording and lead placement | **Death certification/verification (1)** · **Prescribing on the national inpatient chart (2)** · **Blood transfusion bedside checks (2)** |

Death certification and NIMC prescribing are among the most-performed intern tasks and map to specialties this corpus never had a category for.

**Part B's predicted second cluster exists, and it is the ward scales.** Radiology reporting systems were the known cluster (10 of 11 still absent). The new one: **geriatrics 0/6, rehabilitation 0/3, palliative 0/3, ICU 0/4** — Braden/Waterlow/Norton, Katz/Lawton, 4AT, Barthel, modified Rankin, PPS/AKPS, CAM-ICU, RASS.

> [!warning] **Method defects found inside the redo itself — three, all mine.**
> - **Substring matching cannot cross an interposed word.** "Amsterdam criteria" reported absent while the corpus carries **Amsterdam II criteria**, which I built this session. Fixed with ordered-token matching.
> - **Two matchers disagreed** (RECIST, Paris system flipping between passes) — resolved by hand-verification, not by trusting either. "Paris system" present was **"com*paris*on"**.
> - **A token-proximity matcher timed out** at two minutes and was abandoned rather than shipped.
>
> **Part A's 38-specialty pass was NOT completed.** The conditions redo ran the original 50-item list plus verification only. Specialty-by-specialty enumeration across the full Medical Board list — and the low-coverage specialties specifically (Addiction, Occupational, Sport and exercise, Sexual health, Rehabilitation, Clinical genetics, Nuclear medicine, Medical administration) — remains open. Recorded rather than quietly dropped.

| Item | Source | Status |
|---|---|---|
| **P5-C1** | **Macrolides** — mechanism, QT prolongation, CYP3A4 interactions, and the azithro/clarithro/erythro distinction. 106 uses, no entry | ⬜ |
| **P5-C2** | **GTN / nitrates** — mechanism, indications, tolerance, and the **absolute PDE5-inhibitor contraindication** | ⬜ |
| **P5-C3** | **Aminoglycosides and vancomycin** — therapeutic drug monitoring as an intern task: trough timing, nephro/ototoxicity, renal dose adjustment | ⬜ |
| **P5-C4** | **Antifungals** — fluconazole/amphotericin mechanism, hepatotoxicity, interactions | ⬜ |
| **P5-D4** | **Death certification and verification of death** — 1 use corpus-wide; a legal document every intern completes, often unsupervised | ⬜ |
| **P5-D5** | **Prescribing on the National Inpatient Medication Chart** — 2 uses; the most-performed intern task | ⬜ |
| **P5-D6** | **Blood transfusion administration and bedside checks** — 2 uses; fatal if wrong | ⬜ |
| **P5-D7** | **Venepuncture, IV cannulation, LA infiltration, ECG lead placement** — never mentioned or ≤4 uses | ⬜ |
| **P5-B5** | **Ward assessment scales cluster** — pressure risk (Braden/Waterlow/Norton), ADL (Katz/Lawton), delirium (4AT/CAM-ICU), stroke outcome (modified Rankin), palliative performance (PPS/AKPS) | ⬜ |

## Phase 5 — CSV-blind gaps

Everything through Phase 4 was checked against `checklist.csv`. Anything never entered into that CSV was invisible to all of it. Phase 5 looks for those gaps with four separately-sourced checks.

> [!danger] **Part A could not be built as specified — egress, not judgement.**
> Part A required extracting topic lists from three independent authoritative sources. **`WebFetch` is blocked for every domain tested** — `amc.org.au`, `medicalboard.gov.au`, `tg.org.au`, `racgp.org.au`, `health.gov.au`, even `en.wikipedia.org` — and direct `curl` returns 403 CONNECT for all of them. Only `WebSearch` snippets are reachable.
>
> **The narrow-search yield test (3 searches) failed:** AMC snippets describe a *competency* framework, not named conditions; a cardiology search returned an **American** College of Cardiology list and RACP **advanced** (specialist) training, with the result itself stating intern-level Australian lists were unavailable; the ANU "Essential topics" page is a **library resource guide**, not a topic list.
>
> **`checklist_external.csv` was therefore NOT created.** Building it from snippets plus recall and committing it as a permanent artifact that all future work checks against would make a fabricated baseline permanent — every later round would validate against it. That is worse than not having it.
>
> **What was done instead**, per the method agreed mid-run: candidates from domain knowledge of standard Australian intern curricula, checked **corpus-first**, with snippets used only to corroborate. **50 named conditions and congenital anomalies checked; 2 genuinely absent** (posterior urethral valves, craniosynostosis) and 5 thin. The corpus is far more complete against this axis than the premise assumed — which is itself the finding.

| Item | Source | Status |
|---|---|---|
| **P5-A1** | Posterior urethral valves — commonest cause of bladder outlet obstruction in male infants; absent entirely (only adult prostatic obstruction in `07_Renal`). Antenatal hydronephrosis, its usual presentation, is also absent from `15_11` and `16_01-05` | ⬜ |
| **P5-A2** | Craniosynostosis — absent. `04_Neurology`'s "suture fusion" is about infant skulls accommodating raised ICP, a different concept | ⬜ |
| **P5-B1** | Bethesda thyroid cytology — `06_Metabolic` says a nodule "requires histology to exclude malignancy" and never grades the FNA. Bethesda I–VI decides repeat-FNA vs lobectomy vs thyroidectomy | ⬜ |
| **P5-B2** | BI-RADS — the triple test is built in `10_12`; BI-RADS is how every breast imaging report is worded | ⬜ |
| **P5-B3** | Fleischner criteria / incidental pulmonary nodule — no entry at all; the commonest incidental finding an intern must action | ⬜ |
| **P5-B4** | Pressure injury staging and ward risk scales (Braden/Waterlow/Norton) — pressure area content exists in `11_07b`, staging and risk scoring do not | ⬜ |
| **P5-D1** | **Biopsy as a procedure — the largest single gap found.** Ten biopsy types are named across the corpus (core, punch, excisional, FNA, liver, renal, bone marrow, endometrial, skin, temporal artery) and **only temporal artery is taught**. The rest are bare instructions | ⬜ |
| **P5-D2** | Intern-performed procedures missing technique/consent: **NG tube insertion** (10 uses, no indication or technique), **urinary catheterisation** (4 uses, nothing but complications), **joint aspiration** (interpretation taught, procedure not) | ⬜ |
| **P5-D3** | **Chest drain** (10 uses) and **cricothyroidotomy** (3) — named as management steps, never explained. Recognition and escalation are the intern-level content | ⬜ |

> [!tip] **What Phase 5's method showed about the earlier phases.**
> Parts B, C and D are corpus-first depth audits and need no egress; they found the real material. The shape that recurs: **the corpus teaches investigations as *decisions* and not as *procedures*.** It says when to aspirate a joint and what the crystals mean, and never how the aspirate is taken or what it risks. For investigations an intern orders that is correct; for the ones an intern personally performs it is a gap.
>
> **Two method defects surfaced during Phase 5 itself, both mine:**
> - **Part B's first pass used `grep` with `.` wildcards and reported `CHA₂DS₂-VASc` absent.** `.` matches a *byte*, and `₂` is three bytes in UTF-8 — so the check written *for* CLAUDE.md rule 2's Unicode case was defeated by it. Re-run in Python with subscripts folded: **34 absences dropped to 25; 9 were byte-matching artifacts.**
> - **Part C's first pass reported penicillin as taught without contraindications** across 49 uses. Penicillin allergy is in fact taught with substitution pathways in five files; the ±260-character window was too narrow. Dismissed.

> [!warning] **Coverage audit, 2026-08-29 — what generalising twelve defect categories actually showed.**
> Ten of the twelve had only ever been applied where some other check happened to surface an instance. Generalising them produced **three genuine findings and one instructive null**:
> - **ITU used 10× across 9 files** — the UK term for ICU, surviving a Step 17 sweep recorded as complete and then re-run in full. Found by re-running `undefined_terms.py` after the G-tier, not by any term list. **Fourth instance of a "confirmed complete" record being wrong.**
> - **Adult hyperkalaemia doses under a box claiming paediatric validity** (`06_Metabolic`) — found by running CLAUDE.md rule 5 corpus-wide for the first time; it had only ever been applied to `15_*` files.
> - **Nine named tools never enumerated anywhere** — seven dismissed on reading (components given inline in prose), two built (ICHD, Burch-Wartofsky).
> - **The instructive null: `box_scope.py` flagged 55 boxes and all 55 were legitimate.** A numeric proxy cannot see this defect, because every real instance turned on a *non-numeric* claim. Recorded in the script so a clean run is never read as absence.
>
> **Two categories remain structurally open, and are documented risk rather than oversight:**
> - **Same-topic pairs under different wording.** `check_structure.sh` Step 1c-bis matches identical header text, case-folded. "Temporal Arteritis (Giant Cell Arteritis)" vs "Giant cell arteritis (GCA)" is invisible to it and was found by hand. Closing this needs synonym clustering over the ~77 conditions with entries in more than one file — tractable, not attempted.
> - **Asymmetric silence.** No detector is possible: the defect is one entry being *silent* where its counterpart speaks, which has no textual signature. Roughly 30 pairs have been manually read for it. The remaining surface includes every *related-entry* pair that is not a same-topic pair at all — ectopic/miscarriage, where anti-D was found — and that surface is unbounded.

> [!tip] **The adult-figure-in-a-paediatric-entry check (G22–G33, 2026-08-29).**
> Three instances now, and the third was found by looking for the shape deliberately rather than stumbling on it:
> - **DKA maintenance fluid** — `>40kg — 4mL/kg/h` where the band is a fixed `40 mL/h` (five-fold over-infusion).
> - **Nephrotic syndrome** — proteinuria defined as `>3.5g per 24h` in the *paediatric* entry. An absolute daily mass does not scale: a small child in florid nephrotic syndrome cannot reach it, so the threshold **excludes the diagnosis it defines**.
> - **DKA dextrose** — `10% dextrose infusion at 125mL/h`, an adult-sized fixed rate (B49).
>
> **The check:** in any paediatric file, treat every **absolute** quantity (g, mg, mL, mL/h, g/24h) as suspect until shown otherwise, and ask what it does at 10kg and at 50kg. The correct paediatric forms are per-kg, per-m², per-age-band, or **per-kg with an absolute cap** — and the corpus does this well where it does it at all: `magnesium sulfate 40mg/kg (≤2g)`, `prednisolone 60mg/m²/day (max 80mg)`, the ASCIA and ANZCOR age bands. The defect is always an absolute figure standing *alone*.
>
> **Where it comes from:** these entries were written from adult sources, and a number that is right for an adult survives the copy because nothing about it looks wrong in isolation. Only asking "what does this do to a toddler" exposes it.

> [!danger] **The single most repeated error in this session is my own search shape, not the corpus.**
> Four near-misses, all 2026-08-29, all the same structure: **a search returned nothing, or nothing useful, and I read that as evidence about the corpus rather than about the query.**
>
> | What I nearly reported | Why the search failed |
> |---|---|
> | FMT mortality evidence absent | the hit was returned and **truncated** by my own `cut -c1-180` |
> | necrotising fasciitis finger test absent | same — inside a line my `-c1-280` cut off |
> | HELLP never expanded | the text is `**H**aemolysis`; **markdown split the word** |
> | no anti-D dose anywhere in the corpus | doses sat on separate bullet lines that **do not contain the string** `anti-D`; my pattern required the number within 90 chars of it |
> | 12_01 had no `###` headers | `awk '/^#{2,4} /'` — **interval expressions are off by default**, so a broken pattern matched nothing |
>
> Every one would have been "fixed" by adding content that was already there. **The corpus has not once been wrong in this way; the query has, five times.**
>
> **The rule:** when a search returns zero or an unexpectedly thin result, the first hypothesis is that the *search* is wrong — wrong pattern, wrong tool, truncated output, markup in the middle of the word, or the fact living on a line that does not contain the search term. Vary the query before believing it.

> [!danger] **Search artifact — markdown emphasis splits words and defeats plain-text greps.**
> Found 2026-08-29 (G34). `grep -i "haemolysis, elevated"` returned **zero hits** for HELLP across the corpus, and the expansion was sitting there in plain sight:
>
>     **= H**aemolysis, **E**levated **L**iver enzymes, **L**ow **P**latelets.
>
> The literal text is `**H**aemolysis` — the `**` markers fall *inside* the word, so no substring search for the word can match it. This corpus uses letter-by-letter bolding for every acronym expansion it spells out, which is precisely the construction most likely to be searched for and least likely to be found.
>
> **This is CLAUDE.md rule 2 with a fourth cause.** Case, Unicode and hyphenation were already listed; **markup inside a term** belongs beside them. Before concluding an acronym is unexpanded, search for a single distinctive letter-run (`aemolysis`), or read the entry.

> [!danger] **Standing rule — never conclude absence from a truncated grep.**
> A search that returns the right hit but is cut off before you read it carries the same risk as a search that returns nothing, and it is more dangerous because it *looks* like evidence. **View the full line before concluding anything is missing.** Twice in the G40–G43 round I called content absent from output that contained it, cut off by my own character limit; both would have been "fixed" by duplicating content already present. This is CLAUDE.md rule 2 in its inverted form and the rule as written does not cover it.

> [!tip] **Two near-misses worth more than the findings — both were my own truncated reads.**
> I twice concluded content was absent from output that *contained it*, cut off by a `cut -c1-180`/`-280`: the FMT mortality-reduction evidence (inside the ASID box) and the necrotising-fasciitis finger test (inside the Ix line). Both would have been reported as gaps and "fixed" by duplicating content that was already there.
>
> This is **"zero grep hits is not proof of absence" in its inverted form**: the hit was returned and I truncated it away. The rule as written guards against a search that finds nothing. It does not guard against a search that finds the right line and a reader who cannot see the end of it. **Widen the cut before concluding absence from any grep whose output was truncated.**



---

<details>
<summary>Full reasoning for this order (click to expand)</summary>

**Phase 1 ordering rationale**: the exhaustive full-CSV-pull technique is the single most productive method found across this entire project — it's what caught Geriatrics, GP/Ethics, MSK's two gaps, and Obstetrics' Newborn Exam gap, each time on the *first* systematic pass. Six categories (217 rows combined) have never received this treatment at all, only narrower spot-checks. Running these six first, before returning to deep individual-file verification, front-loads the highest-expected-value work — cheap to run, proven hit rate, and likely to surface the next Geriatrics-sized gap if one exists.

**Phase 2 (new content) still ranks above Phase 3/4 re-verification**: an unbuilt High-yield category is a bigger real exam-risk gap than another pass on an already-thorough file. Given the exam dates (MCQ Sept 27, OSCE Nov 1, second MCQ Nov 8), this remains true regardless of how Phase 1 turns out — though Phase 1 may add new items to this list.

**On M1 (04_Neurology.md) specifically**: three completed rounds each found something real, a strong track record — but the file has had roughly 25+ rounds total across this project, more than almost any other file, while every other group sits at zero. Not exhausted, just lower marginal priority than fresh territory right now.

</details>

---
## How to use this document

**Simplest trigger — just say:**

> `next`

This pulls the next unmarked (⬜) item from the Queue above, in order, and runs it — no need to specify a file or decide between verification and new-content building each time. After finishing, I update the Queue's status marker before reporting back, so the next "next" picks up correctly. If you want to skip the queue and target something specific instead, use the range-based trigger below.

**Targeted trigger (use this in-chat to jump to a specific file/group out of order):**

> `verify: [FILE RANGE]`

Within this same conversation, that's sufficient — the full pipeline below, the target standard, the confirmed-hits lists, and the reporting bar are already established context here, so there's no need to restate them each round. Just name the range (a category number range, or the cross-cutting files by name) and the whole workflow runs. If ever picking this up in a **fresh conversation** with no shared history, use the longer Standard Prompt below instead, since a new instance won't have this document's context pre-loaded.

---

## Target standard: intern / RMO level — read this before running any step

Every step below, especially Steps 5, 6, and 10, needs a ceiling, or the search never terminates (see the note on this at the end of this section). The ceiling is: **would a newly-graduated intern or RMO be expected to know, recognise, explain, or act on this in an Australian hospital?** Concretely:

- **In scope:** the mechanism behind a classic sign if it changes how it's recognised or interpreted (Cushing's triad, compartment syndrome's "6 Ps" hierarchy); a scoring system used to trigger a real ward-level decision (ECOG, qSOFA, ABCD²); an AU-specific dose or threshold an intern would actually prescribe or follow; a red flag that changes referral urgency; a health-equity point that changes clinical threshold or screening behaviour, not just background epidemiology.
- **Out of scope:** subspecialist-registrar-level receptor pharmacology, molecular/genetic detail beyond what explains the clinical picture, rare case-report-level exceptions unless they carry a genuine safety implication, and controversies that don't change what an intern should actually do at the bedside. When a mechanism has real depth available (e.g. B12/folate's dual-enzyme biochemistry), stop at the layer that explains the clinical consequence — don't chase it into biochemistry a specialist would need but an intern wouldn't.
- **The equity checks (Step 10) are intern-relevant by definition**, not an add-on — recognising an Australian-specific disparity or an inappropriate screening tool is exactly the kind of judgement an RMO is expected to exercise, so these stay fully in scope even though they're not "mechanism" content.

**Why this can't make the whole process definitive**, even with a ceiling: "what would an intern be expected to know" is still a judgement call, not a fixed list, and different genuinely reasonable people would draw the line slightly differently on some items. What the ceiling *does* do is stop Steps 5–6 specifically from drifting toward specialist depth, which was the main way earlier rounds kept finding "one more layer" — a mechanism explained to intern depth is a finishable task in a way that a mechanism explained to arbitrary depth is not.

---

## The Standard Prompt (for a fresh conversation with no shared history)

> Reverify all files, and see what else can be done with all files and do it. Include flags on anything that needs re-verification, per the guidelines in MASTER_VERIFICATION_WORKFLOW.md. This includes doing targeted work on remaining flags. Confirm all pipelines are completed thoroughly, all Hx/physical exam/Ix findings are accounted for, and all topics — including medium and low yield, and anything likely to be tested by AMC standard even if not explicitly in the CSV — are included and written out, calibrated to **intern/RMO level** (see "Target standard" section — not subspecialist depth). Do this for **[FILE RANGE — e.g. "01 Cardiovascular to 03a Anaesthetics Primer" / "History-Taking, Examination, Investigation-Interpretation, and Communication"]**. If all files are good, state so — only say they're good if complete, all requirements are met, and no gaps are left that you can address.

---

## Scope — every file range this applies to

This workflow is file-range-agnostic. It has been run against every organ-system category (01–13, 15–17) and must also be run against the **cross-cutting files**, which don't belong to a single organ system and are easy to skip if only category files are checked:

- `History-Taking.md`
- `Examination.md`
- `Investigation-Interpretation.md`
- `Communication.md`
- `Clinical-Process-EBM-Consent-Capacity.md`

These files are cited *from* nearly every organ-system file, which means they're also the highest-leverage place for the citation-accuracy checks (Step 8) to find real problems — a header renamed here breaks links in dozens of other files at once.

---

## Step 0 — Setup and re-sync (every round, no exceptions)

```bash
cp /mnt/user-data/outputs/*.md /home/claude/work/ 2>/dev/null
cd /home/claude/work
for f in *.md; do
  s=$(diff -q "$f" "/mnt/user-data/outputs/$f" > /dev/null 2>&1 && echo SYNC || echo OUTOFSYNC)
  [ "$s" = "OUTOFSYNC" ] && echo "$f: $s"
done
```

**Naming-pattern check — do this every single round, not just once.** A narrow glob (`14_*.md`) can silently exclude files with a different prefix (`14a-*.md` was missed for many rounds before this was caught). Always cross-check the narrow pattern against a broad one:

```bash
ls 14_*.md 2>/dev/null | wc -l      # narrow pattern
ls *.md | grep -E "^14" | wc -l     # broad pattern
# if these numbers differ, find out why before doing anything else
```

---

## Step 1 — Structural integrity (fast, catches regressions from prior rounds)

```bash
# Within-file duplicate headers
for f in *.md; do
  dups=$(grep '^## ' "$f" | sort | uniq -d)
  [ -n "$dups" ] && echo "$f: [$dups]"
done

# Cross-file duplicate headers (expect the same ~13 known, already cross-referenced pairs —
# investigate anything new)
grep -h "^## " *.md | sed 's/^## //' | sort | uniq -d

# Full wikilink integrity — every [[Target]] must resolve to an existing file
grep -oh "\[\[[^]|]*\]\]" *.md | sed 's/\[\[//; s/\]\]//' | sort -u > /tmp/links.txt
for link in $(cat /tmp/links.txt); do
  found=$(ls *.md 2>/dev/null | sed 's/\.md$//' | grep -Fx "$link")
  [ -z "$found" ] && echo "UNRESOLVED: $link"
done
```

---

## Step 2 — Corrected granular Ix/Mx completeness scan

Splits sections at **both** `##` and `###` level (a `##`-only split hides gaps in `###` subsections sitting under a sibling with its own Mx — this is how Cauda Equina and Spinal Cord Compression stayed hidden for rounds). The Mx-detection regex must also catch **bare bold-markdown headers** (`**Mx**` with no colon) — some file ranges (Obstetrics/Gynaecology) use this style, and the plain `Mx[:\s]` pattern misses it entirely.

```bash
for f in <files in range>; do
  python3 -c "
import re
with open('$f') as file:
    content = file.read()
sections = re.split(r'\n(?=#{2,3} )', content)
for sec in sections[1:]:
    title_match = re.match(r'#{2,3} ([^\n]+)', sec)
    if not title_match:
        continue
    title = title_match.group(1)
    if 'not repeated here' in sec[:400] or 'not duplicated here' in sec[:400]:
        continue
    has_smx = bool(re.search(r'S/[Ss]mx|Features:|Clinical features', sec))
    has_mx = bool(re.search(r'Mx[:\s*]|Management|treat|Treatment|watch and wait|self-resolv|supportive|reassur|resolves spontaneously|conservative', sec, re.IGNORECASE))
    if has_smx and not has_mx and len(sec) > 200:
        print(f'$f :: {title}')
"
done
```

**Every hit must be manually opened and checked** — this scan produces real false positives (a sibling `###` subsection with its own Mx that sits just outside the split boundary; a deliberately compressed reference-table entry). Confirm genuine absence before treating a hit as a gap.

For the **cross-cutting files** (History-Taking, Examination, Investigation-Interpretation, Communication), this scan doesn't apply in the same way — check instead that every Hx/examination approach entry has a **complete, systematic question/technique list**, not a partial one, and that every investigation entry has both the *why* (what it screens for) and *what* (expected findings) reasoning.

---

## Step 3 — Full CSV cross-check (systematic, not spot-checked)

Pull the **complete** list for the category, not just likely candidates — spot-checking has repeatedly missed real gaps that a full pass caught (Faecal Incontinence, Bacteraemia/Septicaemia terminology).

```python
import csv
with open('checklist.csv', encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    rows = [row for row in r if row['Category']=='<Exact Category Name>']
for row in rows:
    print(row['Topic'], '|', row['Yield (MCQ+OSCE)'])
```

Get exact category names first if unsure:
```python
cats = set(row['Category'] for row in r)
```

For every item:
1. `grep -il` for the term across the range's files.
2. **Zero hits is not proof of absence.** Before concluding a gap, check for: hyphenation variants (`Bi-fascicular` vs `Bifascicular`), Unicode subscripts (`CHA₂DS₂-VASc`), alternate medical vs lay terminology (`Encopresis` vs `faecal incontinence`), and whether the topic is more accurately homed in a different file/category (`Argyll Robertson Pupil` might be Ophthalmology or Neurology).
3. If genuinely present, spot-check **depth**, not just presence — a bare one-line mention with no Ix/Mx is functionally still a gap.
4. **AMC-standard topics not on the CSV**: the CSV is the primary checklist but isn't guaranteed exhaustive. If a topic is clearly high-yield for Australian intern-level practice (a classic must-not-miss emergency, a commonly tested classification system, a frequently examined bedside sign) and is genuinely absent, treat it as in-scope even without a CSV row — flag this explicitly when writing it up.

---

## Step 4 — Cross-category CSV search

Some genuine gaps hide because the CSV files a topic under the "wrong" category (Septic Arthritis under ID, not MSK; Rheumatic Fever under Cardiology, not ID). Search the **whole CSV**, not just the current category, for keywords relevant to the current file range:

```python
keywords = ['<relevant terms for this organ system>']
for row in rows:
    if row['Category'] != '<current category>':
        if any(kw in row['Topic'].lower() for kw in keywords):
            print(row['Category'], '|', row['Topic'], '|', row['Yield'])
```

Then verify the item is actually built in its *correct* topical home (even if that's outside the file range nominally being checked) — don't duplicate content into the wrong file just to stay "in scope." Note the cross-boundary fix explicitly when reporting.

---

## Step 5 — "Assumed but never explained" scan

The single most consistently productive technique this session. Look for named scoring systems, classifications, or eponymous signs that are **used or referenced** in the text but never actually explained — the term appears, but a reader who doesn't already know it would learn nothing.

**How to find candidates:**
- Search for capitalised acronyms/scores mentioned only once or twice (`grep -c` low counts are suspicious).
- Check every classification system a disease entry implies it uses (staging, grading, severity scores) — confirm the actual criteria are spelled out, not just named.
- When a later entry in the same file says "see X above" for a score, check that X was actually explained, not just used.

**Confirmed hits this session** (so future rounds don't need to re-find these): MMSE/MoCA/AMTS, Notifiable Diseases mechanism, TNM staging, ECOG Performance Status, Neoadjuvant/Adjuvant/Palliative intent, Grade vs Stage, DAS28, BASDAI, Schober's test technique, Fibromyalgia 2016 criteria, ABCD² (with the current AU caveat against using it in isolation), AUSDRISK (and its AU-specific exclusion for Aboriginal and Torres Strait Islander people), CHA₂DS₂-VASc (**confirmed already excellent** — false alarm, just Unicode-subscript search-term misses), Duke's criteria for IE, qSOFA/SOFA, Gustilo-Anderson, Weber classification (ankle), Ottawa Rules, Garden classification, Kellgren-Lawrence, Kocher criteria.

---

## Step 6 — "Fact stated without mechanism" scan

The second most productive technique. Look for classic clinical signs, symptom patterns, or lab findings that are stated as bare facts — a name, a value, a rule — without the underlying physiology that explains *why*. This is different from Step 5: the fact itself isn't a named external framework, it's a piece of clinical reasoning presented as trivia.

**Look for:**
- Paired/contrasting facts stated side by side without the shared mechanism connecting them (gastric vs duodenal ulcer pain timing; praevia vs abruption pain/shock; swan neck vs boutonnière).
- A classic mnemonic listing several signs as if equal-weight, when clinically they occur in a meaningful order with different reliability (compartment syndrome's 6 Ps — pulselessness/paralysis are late, dangerous-to-wait-for signs, not early diagnostic criteria).
- An arrow-chain pathophysiology (`A → B → C`) that's mechanically present but doesn't actually explain *why* each arrow holds.
- Any eponymous sign, deformity, or test described by what you'd observe, with no explanation of the underlying structural/physiological reason.

**Confirmed hits this session**: Cushing's triad (two-stage sympathetic-then-vagal mechanism), Beck's triad/pulsus paradoxus/Kussmaul's sign (all four unified under tamponade's fixed-volume physiology), mitral facies, aortic stenosis exertional syncope, aortic regurgitation's peripheral sign cluster (collapsing pulse/wide pulse pressure/De Musset's/Quincke's — all one mechanism), pericarditis positional pain, Kussmaul breathing in DKA, hyperkalaemia's ECG progression, Cushing's syndrome fat redistribution (dual depot-specific cortisol effect), secondary hyperparathyroidism (CKD's dual mechanism), aldosterone escape, HHS-vs-DKA insulin-sensitivity divergence, Addison's hyperpigmentation (POMC/MSH shared precursor — check it's explained in the *primary* disease entry, not just the comparison entry), Acromegaly vs Gigantism (growth plate fusion timing), lid lag vs exophthalmos (two different mechanisms, easily conflated), Argyll Robertson pupil (with appropriate honesty about the genuinely unsettled exact lesion location), Myasthenia Gravis fatiguability (safety-margin/receptor-reserve concept), B12 vs folate and subacute combined degeneration (dual-enzyme mechanism, with honest caveat about rare folate-only case reports), pyloric stenosis's hypochloraemic hypokalaemic alkalosis (including the "paradoxical aciduria" twist), G6PD deficiency (already excellent — false alarm), haemophilia's haemarthrosis (primary vs secondary haemostasis distinction), cremasteric reflex in testicular torsion (mechanical, not neurological), Auspitz's sign (suprapapillary plate thinning), gout's podagra distribution (temperature-dependent urate solubility), morning stiffness duration (inflammatory fluid accumulation vs mechanical "gel phenomenon"), ectopic pregnancy's 6–8 week rupture timing (tubal capacity limit, also explains isthmic-vs-ampullary danger), HELLP syndrome (microangiopathy extending pre-eclampsia's endothelial mechanism), placenta praevia vs abruption (revealed vs concealed haemorrhage).

**When checking a candidate that looks unexplained, verify the mechanism via web search before writing anything** — several of these (B12/folate, Addison's, aldosterone escape) have real nuance or genuine ongoing scientific uncertainty that must be represented honestly rather than oversimplified.

**Stop at intern/RMO depth (see Target Standard above).** The B12/folate entry stops at "two enzymes, one shared and one not" — it doesn't go further into the molecular detail of methionine synthase kinetics. The aldosterone escape entry stops at "pressure natriuresis and ANP restore sodium balance" — it doesn't detail the specific receptor pharmacology. If a web search for a mechanism keeps surfacing deeper and deeper layers, that's the signal to stop once you've reached the layer that explains the clinical picture an intern needs to recognise or act on, not a signal to keep digging.

---

## Step 7 — Connectivity / cross-reference gap checks

Content can be individually complete but functionally undiscoverable because nothing points to it from where a reader would actually arrive. Check whether a **consolidated red-flag or danger box** is cross-referenced from every scattered symptom-specific entry that should point to it.

**Method:** find the consolidated red-flag box (e.g. HNSCC's red-flag list), then check each individual symptom it lists (neck lump, dysphagia, hoarseness, otalgia) in its *own* separate file/entry — does that entry point back to the consolidated box? If not, add the connection (don't duplicate the list).

**Confirmed hits**: HNSCC red flags missing from Neck Lumps, Dysphagia, and Otalgia entries (fixed, three separate rounds); Nasopharyngeal Cancer's red flags missing from the adjacent Epistaxis entry.

**When NOT to add a new consolidating entry**: if the individual connections are already made and the target red-flag box already functions as the index, a second summary layer is redundant, not additive (checked and correctly declined once this session, for ENT's "unilateral symptom" theme).

---

## Step 8 — Bidirectional citation-accuracy scan

Distinct from Step 1's link-resolution check. A `[[Target]]` link can resolve (the file exists) while the **named section** cited alongside it no longer matches the actual header — because the target file was restructured in a later round without the citing file being touched. This is the check most likely to catch real problems in the heavily-edited files, and it must run **both directions**.

```python
import re, glob

file_headers = {}
for filepath in glob.glob("*.md"):
    with open(filepath) as f:
        content = f.read()
    file_headers[filepath.replace('.md','')] = set(re.findall(r'^#{2,3} (.+)$', content, re.MULTILINE))

targets = set(f.replace('.md','') for f in <files in range>)

# OUTGOING: citations made BY files in this range
# INCOMING: citations from ANYWHERE in the project pointing INTO this range — always check
# this direction too, especially for files that have been edited many times
issues = []
for filepath in glob.glob("*.md"):
    with open(filepath) as f:
        content = f.read()
    matches = re.finditer(r'\[\[([^\]|]+)\]\]\s+([A-Z][^,\n]{3,80}?)(?:\s+(?:for|not repeated|\(|—|,|given))', content)
    for m in matches:
        target_file, cited_section = m.group(1), m.group(2).strip()
        if target_file in file_headers:
            found = any(cited_section == h or cited_section in h or h in cited_section
                        for h in file_headers[target_file])
            if not found:
                issues.append(f"{filepath} cites [[{target_file}]] '{cited_section}'")
```

**Every hit needs manual verification — the regex produces real false positives:**
- Citations to **bold list-item text** rather than a formal `##`/`###` header (e.g. "Kocher criteria for diagnosis of septic arthritis" exists exactly as cited, just as an `[!info]` box title, not a markdown header — the scan only checks headers).
- **Parsing artifacts** where the regex grabs text past a citation's closing parenthesis into an unrelated following clause (`"...Idiopathic Intracranial Hypertension); nystagmus"` — the real citation ends at the `)`; "nystagmus" is unrelated following text).

**Confirmed genuine hits (fixed)**: 03a's DVT/PE citation (content split into two separate headers, citation described one combined header); a trivial capitalisation mismatch between two files' cross-references to the same Anaesthetics section; History-Taking's three citations to "Red Eye DDx table" when the actual header is "The Red Eye — Regional Approach and DDx."

---

## Step 9 — Structural asymmetry check

When a file groups several related sub-entities together (OA of hip/knee/hand; upper vs lower limb nerve roots; peripheral nerve lesions), check whether the **most common or most tested** member is the one missing, while less common siblings have full entries. This inversion is a genuine, recurring pattern — it's easy to build the "interesting" or first-encountered member of a group and skip the most routine one.

**Confirmed hits**: OA of the knee (explicitly the most common site) missing while OA of the hip and hand both had full subsections; Upper Limb dermatomes/nerve roots missing while Lower Limb existed (partially — peripheral nerve version was already fixed in an earlier pass, checked and confirmed).

---

## Step 10 — Health equity (Australian/AMC-context) check

Australian intern-level practice requires genuine, specific awareness of health disparities affecting Aboriginal and Torres Strait Islander patients — this is explicitly AMC-relevant, not optional colour. For any condition with a plausible disparity, check specifically for:

1. **Incidence/prevalence/mortality gap** — get real, sourced numbers, not a vague "more common."
2. **Whether a standard screening tool or threshold is known to be inappropriate or under-inclusive for this population** (this has been a recurring, specific pattern: AUSDRISK for T2DM, Centor/FeverPAIN for GAS pharyngitis vs acute rheumatic fever risk, stroke screening age thresholds) — if so, state the correct alternative/lower threshold explicitly.
3. **Treatment-access gap distinct from the incidence gap** — a second, compounding disparity (lung cancer surgery rates, renal transplant access, joint replacement access) is a distinct and recurring pattern worth checking for specifically, not assuming incidence alone explains outcomes.
4. **A specific, proven, actionable intervention**, where one exists (self-collection HPV testing more than doubling cervical screening participation) — this is more useful than statistics alone, since it gives a concrete clinical action.
5. **Nuance and honesty are required** — not every condition trends the same direction. Rheumatoid arthritis prevalence is *lower* in Aboriginal and Torres Strait Islander Australians while osteoarthritis and SLE are *higher*; state the correct direction for each specific condition rather than defaulting to "higher risk" as a template.

**Confirmed hits this session** (13 total): acute rheumatic fever/Centor-FeverPAIN caveat, Rheumatic Heart Disease, CKD, Otitis Media (with the critical "painless presentation in remote-area infants" diagnostic pitfall), Bronchiectasis, Type 2 Diabetes/AUSDRISK, Congenital Syphilis (active national emergency, not historical), Stroke, Renal Transplant access, Lung Cancer (incidence + survival + treatment access), Osteoarthritis (access gap, with the RA/OA/SLE direction nuance), SIDS/SUDI, Cervical Screening self-collection.

---

## Step 11 — AU-specific drug dosing and product-name verification

Check named drugs, doses, and brand products against **current Australian** guidance specifically — don't assume a UK- or US-sourced figure transfers.

- **Doses that look like a round, commonly-cited international figure are worth double-checking** — Australian licensed doses can genuinely differ (AOM amoxicillin: AU 60mg/kg/day vs the commonly-cited US "high-dose" 80–90mg/kg/day).
- **Named brand products** are a common source of leftover UK-specific content (EarCalm, Otosporin were both UK-market products silently sitting in an Australian-localised file).
- Verify against a genuine Australian source (Therapeutic Guidelines, RACGP, RCH Melbourne, ANZCA, SOMANZ, RANZCOG, ADS-ANZCA, state health department guidelines) — cite which one.
- When genuine international variation exists and isn't fully settled, say so honestly rather than picking one figure and presenting it as the only answer (WHO vs SOMANZ aspirin dose in pre-eclampsia).

---

## Step 12 — Internal consistency check (distinct from Step 8's citation-name check)

Step 8 verifies a cited section still exists; it never checks whether the *content* in two places genuinely agrees. Where two files discuss the same fact (a drug dose, a lab threshold, a staging system, a prevalence figure) without one explicitly citing the other, check both independently and confirm they match.

```bash
# Find candidate overlaps — the same drug/number mentioned in 3+ files is worth a consistency pass
grep -l "amiodarone" *.md   # example — repeat for any drug/value likely to recur across categories
```

There's no fully mechanical way to run this at scale — it's judgement-driven. Prioritise: drugs used across multiple specialties (aspirin, warfarin, insulin, steroids), staging/scoring systems referenced from multiple entries (TNM, CHA₂DS₂-VASc, ECOG), and any number that's been independently researched and added in two different rounds (a real risk in a project this size, since a later round has no memory of an earlier one's exact figure unless it explicitly cross-references it).

---

## Step 13 — Template completeness check (distinct from Step 2's Ix/Mx-only check)

Step 2 only flags a missing Mx given S/Smx is present. It doesn't catch an entry missing **D, R, A/P, or Ix outright** — a more basic gap that a narrower scan won't surface.

```python
import re, glob
for f in glob.glob("<files in range>"):
    with open(f) as file:
        content = file.read()
    sections = re.split(r'\n(?=#{2,3} )', content)
    for sec in sections[1:]:
        title_match = re.match(r'#{2,3} ([^\n]+)', sec)
        if not title_match:
            continue
        if 'not repeated here' in sec[:400]:
            continue
        has_d = bool(re.search(r'\*\*D[:\s*]', sec))
        has_smx = bool(re.search(r'S/[Ss]mx|Features:', sec))
        has_ix = bool(re.search(r'\*\*Ix', sec))
        # A genuine disease entry (has S/Smx) missing D or Ix outright is worth checking
        if has_smx and not (has_d and has_ix):
            print(f'{f} :: {title_match.group(1)} — missing D and/or Ix')
```

Same false-positive caveat as Step 2 — reference-table-style entries and cross-reference stubs legitimately skip parts of the template; verify before treating a hit as a gap.

---

## Step 14 — Guideline-currency tracking

Several entries explicitly flag a guideline as pending, in draft, or due for update before the exam (the 2026 Australian Hypertension Guideline is one confirmed example). These need to be collected somewhere and actually re-checked closer to the exam date, not left as a one-off note that never gets revisited.

```bash
grep -rn "pending\|in final review\|due for update\|not yet released\|check closer to the exam\|check current" *.md | grep -i "guideline"
```

Maintain a running list (append to a `PENDING_GUIDELINE_CHECKS.md` file, or a dedicated section at the bottom of this document) of every hit, with the file and expected release window, so these aren't silently forgotten between now and the exam.

---

## Step 15 — Readability / cognitive-load check

A file can be factually complete and still be genuinely hard to study from if 15–20 rounds of stacked `[!info]`/`[!danger]`/`[!note]` boxes have accumulated without ever being consolidated. This has never been checked in this project. For any file that's had many rounds of individual additions:

- Read the file start to finish as a *student would*, not as a fact-checker — does the core clinical picture (D/S-Smx/Mx) stay visible, or is it buried under stacked gap-fill boxes?
- Where multiple `[!info]` boxes on the same entry could reasonably be merged into fewer, better-organised ones without losing content, consider consolidating (this is a rare exception to the "don't rewrite for phrasing" instinct — cognitive load for exam cramming is a legitimate reason, factual completeness alone is not).
- This is a judgement call, not a script — flag it as worth doing on any file that's been through 8+ editing rounds, but don't force consolidation where the file still reads cleanly.

---

## Step 16 — Differential completeness beyond the CSV

Steps 3–4 check named CSV items. Neither checks whether the **differential for a presenting symptom** is exhaustive at intern level, independent of whether every individual cause has its own CSV row — a real gap, since presenting-symptom differentials are exactly what OSCEs and MCQs test.

For any "approach to X symptom" entry (chest pain, dyspnoea, abdominal pain, headache, etc.), check the differential list against a mental "could an intern miss this and be criticised for it" standard, not just against the CSV. This is the same reasoning that built Pruritus, Weight Change, and Fatigue/Pallor as differential-approach entries earlier in this project — apply it as a standing check, not a one-off.

---

## Step 17 — Systematic UK-localisation sweep

Every UK-ism found in this project so far (NICE, EarCalm, Otosporin, Debendox, stray "NHS"/"BNF" references) was caught **reactively**, as a side effect of some other check running in whichever file happened to be open. There has never been one dedicated pass grepping the *whole project* for these terms as its own exercise — meaning more are almost certainly still sitting in files that never had a specific reason to be opened for this.

```bash
grep -in "NICE\b\|NHS\b\|BNF\b\|A&E\b\|GP surgery\|casualty department\|Royal College of\|British Society\|British National Formulary" *.md
```

> [!warning] **This document contradicted itself about Step 17, and both versions were wrong.**
> The paragraph above says a dedicated whole-project pass has **never** been run. The run-estimate section further down says one **has** — "26 files flagged, 5 spot-checked… 1 genuine leftover UK term found and fixed". Both cannot be true, and the second is the one that was materially wrong: a full re-run of the exact term list above across all 148 content files on 2026-08-28 found **7 further genuine leftovers**, not zero — six patient-facing "go to A&E" instructions (`05_Ophthalmology` ×2, `15_02`, `15_04b`, `15_24a`, `16_10-13`) and one "check BNF/local formulary" (`16_16-17` → AMH). All seven sat in files the earlier sweep had itself flagged.
>
> **The re-run's full result**, judged hit by hit rather than replaced mechanically:
> - **A&E — 6 hits, all genuine leftovers.** Fixed.
> - **BNF — 1 hit, genuine leftover.** Fixed → AMH.
> - **NHS — 8 hits, all legitimate.** Every one sits inside a verified `[!info]` box drawing a deliberate AU-vs-UK contrast (e.g. no AAA call-recall programme equivalent; no Medicare cap equivalent to the UK's 1–3 NHS cycles). NHS presence is **not** evidence of a miss here, and an earlier report in this session that said it was has been corrected.
> - **NICE — legitimate wherever an adjacent Australian source adjudicates it** (`01_Cardiovascular`, `02_Respiratory`, `04_Neurology`, `12_01`, `14_01`, `14_02`, `15_09b`, `16_01-05:245–247`). **Four hits have no such adjudication** and were flagged inline rather than deleted or given a fabricated Australian equivalent — see `PENDING_GUIDELINE_CHECKS.md` **B32**.
> - **`GP surgery`, `casualty department`, `British Society`, `British National Formulary` — zero hits.** "Royal College of" matched only "Royal Australian and New Zealand College of…" — false positives.
>
> **The method lesson.** A grep-based sweep is only as complete as the judgement applied to its output, and this one was recorded by the count of terms *fixed* rather than the count of hits *adjudicated* — so files flagged-but-not-opened were absorbed into a "1 leftover" headline. **Record a sweep by what was examined, not by what was changed.** Step 17 is now recorded as: term list re-run across all 148 files, every hit individually judged, 7 fixed, 4 flagged to B32, the rest confirmed deliberate. That is "clean against this term list" — it is not "clean of UK-isms", because the term list itself is a guess at which UK-isms exist.

Every hit needs individual judgement — some are legitimate (a deliberate historical/comparative note explaining what was corrected, like the ARF/DVLA-vs-Austroads examples), most found this way have been genuine leftover errors. This is broad enough to run as its own dedicated full-project pass rather than folding into a per-group round — see the revised run estimates below.

---

## Step 18 — Retrospective intern/RMO depth audit

The intern/RMO ceiling (see "Target standard" above) was only made explicit partway through this project. The overwhelming majority of content — everything added before that point — was never checked against it. Some early "fact without mechanism" additions may have gone deeper than intern level without that being flagged as a problem at the time it was written.

For any file being re-verified, specifically re-read its `[!info]`/mechanism boxes with the ceiling question in mind: *does this depth change what an intern recognises, does, or refers — or has it drifted into specialist-registrar territory that's technically accurate but disproportionate?* Trim back (don't delete outright — a shorter, correctly-scoped version) anything that fails this test.

---

## Step 19 — Orphaned-reference check (inverse of Step 7)

Step 7 checks whether scattered symptom entries cite a shared red-flag/reference box. This step checks the **reverse**: entries built specifically to be a shared reference (TNM, ECOG, the dermatome/myotome tables, Duke's criteria) should have real incoming citations from the content that ought to lean on them. A reference entry with zero incoming links was either built somewhere no one will find it, or was never actually connected to the disease entries that use the concept it explains.

```python
import re, glob
# For a known reference-entry header, count incoming [[File]] citations project-wide
target_file = "<filename without .md>"
count = 0
for f in glob.glob("*.md"):
    if f == target_file + ".md":
        continue
    with open(f) as file:
        if f"[[{target_file}]]" in file.read():
            count += 1
print(f"{target_file}: cited from {count} other files")
```

A reference entry cited from zero or one other file is worth checking — is that genuinely all the content that needs it, or is there a disease entry elsewhere in the project using the same concept without pointing back to the explanation?

---

## Step 20 — Source-currency spot-audit

Many additions cite a specific guideline "verified as of Aug 2026" or similar. Nothing currently re-checks whether those citations have since been superseded, and this compounds the closer the project gets to the actual exam dates (Sept/Nov 2026 per the profile).

```bash
grep -n "verified against\|as of Aug 2026\|Aug 2026, not yet released\|current as of" *.md
```

Collect these into the same `PENDING_GUIDELINE_CHECKS.md` tracking file as Step 14, with a note to re-run a quick search on each specific guideline shortly before the exam dates, not just once during this build phase.

---

## Step 21 — Uncovered-category CSV audit (structurally different from every step above)

Every step from 0–20 assumes files already exist to be checked. This step catches the case none of them can: **an entire CSV category with no corresponding file, or with far less coverage than a category its size warrants.**

**First pass of this step (limited to the 5 categories explicitly marked "(NEW)") missed two more.** The "(NEW)" tag was a reasonable first heuristic but not sufficient — it only flags categories added *after* the initial build, not categories that were always in the checklist but never individually pulled and cross-checked against what actually exists. **The correct version of this step checks every single category name against the CSV, not just the ones with an obvious flag:**

```python
import csv
with open('checklist.csv', encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    rows = list(r)
cats = sorted(set(row['Category'] for row in rows))
for c in cats:
    count = sum(1 for row in rows if row['Category']==c)
    print(count, '|', c)
```

Then, for every category — not just the ones that look obviously new — ask: has this category's specific row list ever actually been pulled and checked item-by-item against existing files, or has coverage only ever been *assumed* because it sounds similar to a category that has been checked?

**Confirmed findings, round 1 (the "(NEW)"-only pass):** 33 rows across 5 categories — see below.

**Confirmed findings, round 2 (checking every category name directly):** two more categories, neither marked "(NEW)," had never been individually pulled:

- **General Practice, Preventive Med, Ethics & Communication — 29 rows, many High yield.** This is the **second-largest gap found in this project**, comparable in significance to Geriatrics. Specific confirmed gaps: **Motivational Interviewing's stages-of-change model** is named as a treatment modality in two files but the actual model (precontemplation → contemplation → preparation → action → maintenance → relapse) is never explained — the same "assumed but unexplained" pattern from Step 5, just never applied to a communication framework rather than a clinical score. **Domestic violence** (explicitly High yield, and separately flagged in an earlier round as deliberately deferred "see GP sec") exists as a single bare bullet — "ask about domestic violence... in unsupported women" — in an antenatal history-taking checklist, with no actual screening approach, red flags, safety planning, or mandatory reporting content anywhere in the project. **Continuity of care** and a **consolidated preventive medicine/screening reference** (explicitly High yield, covering cancer screening, cardiovascular prevention, diabetes prevention, smoking cessation as one framework) are both genuinely and completely absent.
- **Sexual Health / STIs — 12 rows.** Substantially already covered — most named STIs (chlamydia, gonorrhoea, syphilis, genital herpes, HPV, BV) exist in `08_08` and `17_07` with real depth. Confirmed present but not yet depth-checked: chancroid, granuloma inguinale, *Mycoplasma genitalium* (increasingly clinically relevant, worth confirming genuine depth rather than a passing mention). Lower priority than the GP category — mostly a verification pass, not a build.

**The meta-lesson from finding this on the second pass, not the first**: relying on an explicit "(NEW)" marker as the trigger for Step 21 was itself a scope-limiting assumption. The corrected version of this step checks **every** category name, every time it's run, not just the ones that look like an obvious gap.

**Action, not just detection:** unlike every other step, a hit here can't be fixed by editing an existing file — it requires **building new file(s) from scratch**. Treat this differently in planning: it's not "one more verify round," it's a new content-creation project, sized and estimated separately below.

---

## Step 22 — Source-citation accuracy spot-audit

Distinct from Step 20 (which tracks whether a *cited guideline* might have been superseded since citing it). This step checks something more basic that's never been verified: across roughly 200+ web searches run over this project, was the **guideline name and its claimed content** accurately captured in the first place, not misremembered or conflated with a similar-sounding source? Pick a random sample of specific-guideline citations per round (SOMANZ, RANZCOG, RACGP, Therapeutic Guidelines, ANZCA, ADS-ANZCA) and re-search to confirm the claimed recommendation is genuinely what that source says, not a plausible-sounding approximation.

```bash
grep -n "verified against\|per SOMANZ\|per RANZCOG\|per RACGP\|per ANZCA\|per ADS-ANZCA\|Therapeutic Guidelines" *.md | shuf -n 5
```

Re-verify the 5 sampled citations properly via search each round, rather than trusting the original citation was correct because it was made carefully — carefulness at the time doesn't rule out an honest transcription error.

---

## Step 23 — Full-category CSV audit for non-"(NEW)"-tagged categories (Step 21's blind spot)

Step 21 only checked categories explicitly marked "(NEW)" — a reasonable signal, but one that assumes *only* newly-added categories could be under-covered. This step closes that gap: pull the **complete row list for every remaining category**, not just the ones with a convenient tag, and spot-check the most distinctive/highest-yield items.

```python
import csv
with open('checklist.csv', encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    rows = list(r)
all_cats = sorted(set(row['Category'] for row in rows))
# cross-reference against which categories have already had a genuine full-CSV pass —
# not just "a file exists with this category's name"
```

**Confirmed finding (run once, this round):** two categories without the "(NEW)" tag had never had a full row-list pulled — **Sexual Health / STIs** (12 rows) and **General Practice, Preventive Med, Ethics & Communication** (29 rows). Checking both:

- **Sexual Health / STIs — confirmed already well covered.** Spot-checked the least obviously-mainstream items (Chancroid, Granuloma inguinale, Mycoplasma genitalium, Pubic lice) — all four present and built in `08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs.md`. No action needed; this was correctly assumed complete because it fell naturally within the extensive 08_ Infectious Disease work already done, just never formally cross-checked against its own named category.
- **General Practice, Preventive Med, Ethics & Communication — a genuine, substantial, but *partial* gap**, not total absence like Geriatrics. Confirmed **present**: breaking bad news, polypharmacy, discussing end-of-life care, smoking cessation/SNAP (appropriately scattered as a risk factor across many disease entries). Confirmed **genuinely absent**: motivational interviewing/stages-of-change model (High yield — only a passing mention in a Psych substance-misuse file, not built as its own communication-skills entry), hospital avoidance, giving/receiving handover, continuity of care, and mandatory reporting as a general overarching skill (currently only embedded in the paediatric NAI context, not built as the standalone skill the CSV names). Roughly a third to half of this category's 29 rows need checking individually — this is `Communication.md`'s scope specifically, and directly explains why that file was already flagged as "never a primary verification target" earlier in this document — it turns out that flag was correctly predictive.

**Action:** this is a mix of "verify existing content is adequate" (much of it) and genuine "build from scratch" (motivational interviewing, handover, continuity of care, general mandatory reporting) — see the updated new-build table below.

---

## Step 24 — Attention-density audit: "under-worked mega file" gaps (distinct from Step 21/23's missing-category gaps)

Steps 21 and 23 find **entire categories with zero organic attention**. This step tests something different and genuinely more subtle: a category that **has** a file and **has** received real work can still hide gaps in the specific sub-topics that never happened to come up during that work, if the volume of attention was moderate rather than extensive. Confirmed by direct testing across three categories this round, not by inference:

- **Neurology and Endocrine & Metabolic (mega files, 20+ dedicated "fact without mechanism" rounds each)** — full CSV pull, spot-checked the most distinctive items (Delirium, Charcot-Marie-Tooth, Chiari malformations, Thyroid Storm, Goitre, Respiratory Acidosis/Alkalosis). **All genuinely present.** Extensive, repeated, unstructured attention across many rounds appears to substitute for a formal CSV pull in these categories.
- **Musculoskeletal / Orthopaedics / Rheumatology (real work done, but comparatively less concentrated — e.g. `11_02_Ortho_-_Upper_Limb` never had its own multi-round dedicated "fact without mechanism" campaign the way Neurology or Cardiology did)** — full CSV pull (84 rows), spot-checked the most distinctive items. **Two confirmed genuine gaps**, both present but significantly under-developed relative to their High-yield CSV status: **Achilles tendon rupture** (no examination technique, no Ix, no Mx at all — fixed this round, now includes the Simmonds-Thompson calf-squeeze test with its false-negative pitfall, and the genuinely current surgical-vs-conservative management debate) and **Acromioclavicular joint injury** (has the Rockwood grading but lacks S/Smx and Ix detail — not yet fixed).

**The practical distinction this reveals**: "has a file, has had some work done" is not the same signal as "has had *enough concentrated* work done" — a category can pass Step 21/23's existence check and still fail this one. Run this step specifically on categories that fall in the middle: neither zero-attention (already caught by 21/23) nor extensively-mined (where Steps 5/6 have likely already surfaced most gaps organically).

```python
import csv
with open('checklist.csv', encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    rows = [row for row in r if row['Category']=='<a moderately-worked category>']
for row in rows:
    print(row['Topic'], '|', row.get('Yield (MCQ+OSCE)',''))
```

Spot-check the most specific/distinctive named items (not the broad ones already likely covered by general disease-approach entries) — this is exactly what surfaced Achilles rupture and AC joint injury out of MSK's 84 rows.

**Further confirmed hits, same technique applied to Obstetrics and Haematology**: Obstetrics' full CSV pull found **Newborn Examination genuinely absent as its own structured entry** — individual findings (red reflex, minor neonatal skin conditions) were scattered elsewhere, but the formal, sequenced physical exam itself (the actual "NIPE" — Newborn Infant Physical Examination — performed on every baby, including Barlow/Ortolani hip screening and pre-/post-ductal saturation checks) didn't exist. **Fixed, built into `Examination.md`** given that's the correct home for structured examination approaches, verified against Queensland Health's own Newborn Baby Assessment guideline. Haematology's full CSV pull, by contrast, came back clean (α-/β-thalassaemia both genuinely present and well-built — another Unicode-character search miss, not a real gap, mirroring the CHA₂DS₂-VASc case). This confirms the technique generalises beyond disease-entry files into the cross-cutting Examination/History-Taking/Investigation-Interpretation files too — worth treating those as equally in-scope for this specific check, not just organ-system disease files.

---

## Step 25 — Final comprehensive sweep (every round, before reporting)

```bash
# Full structural check
for f in *.md; do
  dups=$(grep '^## ' "$f" | sort | uniq -d)
  s=$(diff -q "$f" "/mnt/user-data/outputs/$f" > /dev/null 2>&1 && echo SYNC || echo OUTOFSYNC)
  [ -n "$dups" ] && echo "$f: DUPS"
  [ "$s" = "OUTOFSYNC" ] && echo "$f: OUTOFSYNC"
done

# Corrected granular Ix/Mx scan (Step 2, re-run after all edits)
# Full wikilink integrity (Step 1, re-run after all edits)
# Total file count sanity check
ls *.md | wc -l
```

Every edit must be individually verified (`grep -c "^## "` before/after, checkpoint to `/mnt/user-data/outputs/`) **before** moving to the next candidate — never batch multiple unverified edits.

---

## Suggested round groupings — copy-paste prompts with run estimates

Sizes and header counts pulled directly from the files. Four tiers: **10 mega** (>85KB), **10 large** (25–85KB), **31 medium** (10–25KB), **95 small** (<10KB). Each row below is ready to paste as-is (using the in-chat shorthand from "How to use this document" above).

**Step 17 (UK-localisation) has now had one whole-project sweep run against it directly** — 26 files flagged, 5 spot-checked. Result: 1 genuine leftover UK term found and fixed ("A&E" → "Emergency Department (ED)" in `11_05_Ortho_-_Knee_and_Ankle.md`), 4 others confirmed as legitimate — already-verified AU-vs-UK comparison notes, not errors. **The "1 leftover" figure was wrong — see the warning box in the Step 17 section; the 2026-08-28 re-run of the same term list found 7 more genuine leftovers, all in this same flagged file set.** This means Step 17's marginal cost per group is now genuinely lower than a from-scratch check — but **not zero**: 21 of the 26 flagged files haven't been individually confirmed yet, so when a group containing one of those 26 files comes up, still check its specific hit(s) against the flagged list below rather than assuming it's automatically fine.

**Steps 18, 19, and 20 (retrospective depth audit, orphaned-reference check, source-currency audit) are entirely undone anywhere in this project** — no partial credit for these the way Step 17 now has. This genuinely raises the honest per-group estimate versus the previous version of this document, since these three add real new work on top of everything already checked, not lighter cleanup.

**Files flagged by the Step 17 sweep** (check these specifically when their group comes up): `01_Cardiovascular`, `02_Respiratory`, `03_Gastrointestinal`, `04_Neurology`, `05_Ophthalmology`, `07_Renal_Medicine_and_Urology`, `08_01-03_Bacterial_Infections`, `08_05-06_Viral_Infections`, `11_01_Orthopaedic_Emergencies`, `11_05_Knee_and_Ankle` (fixed), `12_01_RA_OA_PsA`, `12_02_AS_Gout_etc`, `14_01_Mood_Disorders`, `14_02_Anxiety`, `14_05a_Eating_Disorders`, `14_06a_Drugs_Used_in_Psychiatry`, `15_02_Ill_Feverish_Child`, `15_04b_Asthma_in_Children`, `15_09b_Infant_Feeding_Problems` (spot-checked, clean), `15_24a_NAI_Sexual_Abuse`, `15_24b_Screening_SIDS_Vaccination`, `16_01-05_Antenatal_Care`, `16_10-13_Labour_and_Delivery`, `16_16-17_Contraception`, `17_06_Subfertility_OHSS`.

**Run estimates, revised:**
- **3 runs** (was 2) — ranges with extensive prior work (most of 01–13). The extra run absorbs Steps 18–20, which are genuinely new work regardless of how much prior verification a file has had.
- **4 runs** (was 3) — ranges with moderate prior work (16–17, 14–15 as combined sweeps). Same reasoning — Steps 18–20 are undone here too, on top of already being the less-verified tier.
- **5–6 runs** (was 4–5) — the cross-cutting files, now needing the full 20-step set applied essentially from scratch, including the three steps nothing in the project has been checked against yet.

Run the listed number, then reassess — if a run comes back with genuinely nothing new, stop early regardless of the estimate; if it's still finding things at the estimated ceiling, keep going.

### Mega files (10) — highest priority, one file per round

| # | Prompt | Est. runs | Why |
|---|---|---|---|
| M1 | `verify: 04_Neurology.md` | 3 | Extensive prior work (20+ rounds across this session) |
| M2 | `verify: 01_Cardiovascular.md` | 3 | Extensive prior work |
| M3 | `verify: 03_Gastrointestinal.md` | 3 | Extensive prior work |
| M4 | `verify: 06_Metabolic_Medicine_and_Endocrinology.md` | 3 | Extensive prior work |
| M5 | `verify: 07_Renal_Medicine_and_Urology.md` | 3 | Extensive prior work |
| M6 | `verify: Examination.md` | 5 | Received genuine substantial work this round (Newborn Examination built) — no longer purely reactive, but still under-verified relative to the true mega files given its size |
| M7 | `verify: History-Taking.md` | 6 | **Never a primary target** — only reactive citation fixes |
| M8 | `verify: 02_Respiratory.md` | 3 | Extensive prior work |
| M9 | `verify: 05_Ophthalmology.md` | 3 | Moderate-extensive prior work |
| M10 | `verify: Investigation-Interpretation.md` | 6 | **Never a primary target** — only reactive citation fixes |

### Large files (10)

| # | Prompt | Est. runs | Why |
|---|---|---|---|
| L1 | `verify: 08_09_…` | ✅ 2026-08-29 | **Hyposplenism had no Mx at all** in the file that owns it (`10_09b`) while the verified regimen sat in `08_09` under a splenectomy framing. Built + routed. |
| L2 | `verify: 16_01-05_Antenatal_Care.md` | ✅ 2026-08-29 | **Blanket "all … verified" box contradicted two "not verified" flags in its own file** — flags I had added. Fixed; all 13 file-level localisation boxes swept, this was the only one claiming everything. |
| L3 | `verify: 09_08_…` | ✅ 2026-08-29 | File itself clean (no verification boxes, no positional refs). Its seam was not: triggered the **duplicate-pair consistency sweep**, which found the anaphylaxis circular reference (B43). |
| L4 | `verify: 08_01-03_…, 08_04_Antibiogram` | ✅ 2026-08-29 | **Two NIP schedules disagreed** (meningococcal Year 7 vs Year 10 — fixed; Hib 12 vs 18 months — flagged, B47). `08_04`'s box recorded as the **model** for scoped verification. |
| L5 | `verify: 08_05-06_…, 08_10_…` | ✅ 2026-08-29 | **Centor given as a bare rule with no ARF caveat** in the ID file while `13_05a` carried the caveat (B48) — highest-equity-stakes seam found. Acronym-component check run corpus-wide: no further arithmetic defects. |
| L6 | `verify: 03a_Anaesthetics_Primer.md` | ✅ 2026-08-29 | Clean. File-level box points to the per-entry boxes (correct pattern). Dexamethasone doses across 5 files confirmed as **different indications**, not a conflict. |
| L7 | `verify: 11_02_Ortho_-_Upper_Limb…` | ✅ 2026-08-29 | **The recorded AC-joint gap is closed** — full Rockwood I–VI grading with S/Smx, Ix and grade-split Mx. Zero verification boxes, zero positional refs. Clean. Previously flagged as a real gap by Step 24 |
| L8 | `verify: 16_10-13_Labour_and_Delivery.md` | ✅ 2026-08-29 | Clean on the classification-completeness check: perineal tears carry all four degrees **with 3a/3b/3c subdivisions**; caesarean urgency Category 1–4 present and its box is honestly labelled *Partially verified*. Oxytocin 10 IU (PPH) vs 20 IU (umbilical vein, retained placenta) confirmed as different indications. |
| L9 | `verify: Communication.md, Clinical-Process-…` | ✅ 2026-08-29 | **~20 truncated cross-references fixed** in the two files carrying most of this session's original writing — a systematic habit of dropping a header's parenthetical suffix, plus two references to a `Consent` section in `03a` that **does not exist**. 63 references checked against the real header index. Both `Verified` boxes narrowly scoped to a single statute each. Record retention confirmed single-owner. ISBAR 5/5. |
| L10 | `verify: 10_11a_Oncology…, 10_12_Breast` | ✅ 2026-08-29 | Clean. ECOG 0–4 complete with grade 5 correctly flagged as research-context; TNM entry **states its own scope limit** (criteria are cancer-specific, left to the disease entries) — the one-owner pattern done right. BreastScreen eligibility: `19_` states it but names `10_12` as source of truth. Both boxes narrowly scoped. |

### Medium + small, grouped by category

| # | Prompt | Est. runs | Why |
|---|---|---|---|
| G1 | `verify: 08_07_Infectious_Disease_-_Protozoan_Infections.md, 08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs.md` | 3 | Extensive prior work |
| G2 | `verify: 09_01_Dermatology_-_Dermatological_Emergencies.md, 09_04_Dermatology_-_Eczema__Psoriasis__Rosacea.md` | 3 | Extensive prior work |
| G3 | `verify: 09_02_Dermatology_-_Melanocytic_Lesions_and_Mimickers.md, 09_03a_Dermatology_-_Non-Melanoma_Skin_Cancer.md, 09_03b_Dermatology_-_Acne_Vulgaris.md` | 3 | Extensive prior work |
| G4 | `verify: 09_05_Dermatology_-_Bacterial_Infections_and_Infestations.md, 09_06_Dermatology_-_Fungal_and_Viral_Skin_Infections.md, 09_07_Dermatology_-_Chickenpox__Shingles__Pityriasis_Rosea__Hidradenitis_Suppurativa.md` | 3 | Extensive prior work |
| G5 | `verify: 10_01_Haemonc_-_Leukaemias_and_Myeloproliferative_Disorders.md, 10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma.md` | 3 | Extensive prior work |
| G6 | `verify: 10_04_Haemonc_-_Anaemia_Overview_and_Microcytic_Anaemia.md, 10_05_Haemonc_-_Normocytic_Anaemia_and_Sickle_Cell_Disease.md, 10_06a_Haemonc_-_Macrocytic_Anaemia.md, 10_06b_Haemonc_-_Thrombophilia__APS__Thrombocytosis__Methaemoglobinaemia.md` | 3 | Extensive prior work |
| G7 | `verify: 10_08_Haemonc_-_Blood_Products_and_Transfusion.md, 10_09a_Haemonc_-_Anticoagulants_and_Antiplatelets.md, 10_09b_Haemonc_-_Miscellaneous_Haematology.md` | 3 | Extensive prior work |
| G8 | `verify: 10_03a_Haemonc_-_Primary_Immunodeficiencies.md, 10_03b_Haemonc_-_Acute_Intermittent_Porphyria.md, 10_07_Haemonc_-_Platelet_and_Clotting_Disorders__Neutropaenia.md` | 3 | Extensive prior work |
| G9 | `verify: 10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies.md, 10_10b_Haemonc_-_Transplant_Medicine.md, 10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes.md, 10_11c_Oncology_-_Palliative_Care_Prescribing.md` | 3 | Extensive prior work |
| G10 | `verify: 11_01_Ortho_-_Orthopaedic_Emergencies.md, 11_10_Ortho_-_Paediatric_Orthopaedics.md` | 3 | Extensive prior work |
| G11 | `verify: 11_06_Ortho_-_Spinal_Orthopaedics.md, 11_07a_Ortho_-_Dermatomes_and_Myotomes_Reference.md, 11_07b_Ortho_-_Osteomyelitis__Osteochondritis_Dissecans__Fat_Embolism__Charcot_Joint__Osteomalacia.md` | 3 | Extensive prior work |
| G12 | `verify: 11_03_Ortho_-_Hand_and_Foot.md, 11_04_Ortho_-_Hip.md, 11_05_Ortho_-_Knee_and_Ankle.md` | 4 | Step 24 confirmed a real gap here (Achilles rupture — now partially fixed) — this group's "less verified" flag was correct |
| G13 | `verify: 11_08a_Ortho_-_Joint_Replacements.md, 11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis.md, 11_08c_Ortho_-_Fracture_Types_and_Pathological_Fractures.md, 11_09a_Ortho_-_Orthopaedic_and_Bone_Malignancies.md, 11_09b_Ortho_-_Trauma.md` | 4 | Same "less individually verified" flag as G12, which Step 24 just confirmed was predictive there — treat as equally at-risk until actually tested |
| G14 | `verify: 12_01_Rheum_-_Rheumatoid_Arthritis__Osteoarthritis__Psoriatic_Arthritis.md, 12_02_Rheum_-_Ankylosing_Spondylitis__Gout__Pseudogout__Reactive_Arthritis__Fibromyalgia__PMR__CFS.md, 12_03_Rheum_-_Connective_Tissue_Diseases__SLE__Systemic_Sclerosis__Dermatomyositis__Polymyositis__Sjogren_.md, 12_04_Rheum_-_Vasculitis.md` | 3 | Extensive prior work |
| G15 | `verify: 13_01_ENT_-_Otalgia__Otitis_Externa__Otitis_Media__Glue_Ear.md, 13_04_ENT_-_Nose__Rhinosinusitis__Fractures__CSF_Rhinorrhoea__Epistaxis__Nasal_Cancers_.md` | 3 | Extensive prior work |
| G16 | `verify: 13_02_ENT_-_Hearing_Loss__Tinnitus__Vertigo__DDx_Charts_.md, 13_03_ENT_-_Deafness_and_Vertigo_Conditions.md, 13_05a_ENT_-_Sore_Throat_and_Tonsillitis.md, 13_05b_ENT_-_Stridor__Croup__Epiglottitis__Laryngomalacia__OSA.md` | 3 | Extensive prior work |
| G17 | `verify: 13_06a_ENT_-_Dysphonia_and_HNSCC.md, 13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology.md, 13_06c_ENT_-_Bell_s_Palsy.md, 13_07a_ENT_-_Neck_Lumps.md, 13_07b_ENT_-_Salivary_Gland_Problems_and_Xerostomia.md, 13_07c_ENT_-_Dental_and_Teeth_Problems.md` | 3 | Extensive prior work |
| G18 | `verify: 14_01_Psych_-_Mood_Disorders__Depression__Suicide__Bipolar_.md, 14_03_Psych_-_Psychotic_Disorders_and_Antipsychotics.md` | 4 | Moderate prior work (combined-bundle rounds, not individual) |
| G19 | `verify: 14a-1_Psych_-_Substance_Misuse__Recreational_Drug_Profiles_.md, 14a-2_Psych_-_Overdose_and_Poisoning_Management.md, 14_02_Psych_-_Anxiety_and_Related_Disorders.md` | 4 | Moderate prior work; 14a files only found via the naming-pattern fix, not individually deep-checked |
| G20 | `verify: 14_04_Psych_-_Personality_Disorders.md, 14_05a_Psych_-_Eating_Disorders.md, 14_05b_Psych_-_Insomnia.md, 14_05c_Psych_-_Unexplained_Symptoms__Somatoform__Dissociative__Factitious_Disorders_.md, 14_05d_Psych_-_Electroconvulsive_Therapy.md` | 4 | Moderate prior work |
| G21 | `verify: 14_06a_Psych_-_Drugs_Used_in_Psychiatry.md, 14_06b_Psych_-_Mental_Health_Act_and_Sectioning.md, 14_07_Psych_-_Attention_Deficit_Hyperactivity_Disorder.md` | 4 | Moderate prior work |
| G22 | `verify: 15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md, 15_01b_Paeds_-_Anaphylaxis.md, 15_02_Paeds_-_Ill_and_Feverish_Child__Meningitis__Encephalitis.md` | 4 | Moderate prior work (combined-bundle rounds) |
| G23 | `verify: 15_03a_Paeds_-_Childhood_Viral_Exanthems.md, 15_03b_Paeds_-_HIV_in_Children.md, 15_04a_Paeds_-_URTI_and_LRTI.md, 15_04b_Paeds_-_Asthma_in_Children.md` | 4 | Moderate prior work |
| G24 | `verify: 15_05_Paeds_-_Acyanotic_Congenital_Heart_Disease.md, 15_06_Paeds_-_Cyanotic_CHD__Kawasaki_Disease__Murmurs.md` | 4 | Moderate prior work |
| G25 | `verify: 15_07_Paeds_-_Abdominal_Pain__Neuroblastoma__Coeliac_Disease__Malnutrition__Diarrhoea_and_Vomiting.md, 15_08_Paeds_-_Surgical_Abdomen__Appendicitis__Intussusception__Pyloric_Stenosis__Hirschsprung__Oesophageal_Atresia_.md, 15_09a_Paeds_-_Congenital_Abdominal_Wall_and_GI_Anomalies.md, 15_09b_Paeds_-_Infant_Feeding_Problems.md` | 4 | Moderate prior work — pyloric stenosis mechanism already fixed here |
| G26 | `verify: 15_10_Paeds_-_UTI__Nephrotic_Syndrome__Glomerulonephritis.md, 15_11_Paeds_-_Urological_and_Renal_Anomalies__Wilms_Tumour__HUS.md` | 4 | Moderate prior work — recheck the AGN structural false-positive is still a false positive after Steps 12–13 added |
| G27 | `verify: 15_12a_Paeds_-_Epilepsy_Syndromes_and_Status_Epilepticus.md, 15_12b_Paeds_-_Brain_Tumours.md, 15_13a_Paeds_-_Neural_Tube_Defects.md, 15_13b_Paeds_-_Autism_Spectrum_Disorder_and_Cleft_Lip_Palate.md` | 4 | Moderate prior work |
| G28 | `verify: 15_14_Paeds_-_Anaemia__Sickle_Cell__Hereditary_Spherocytosis__HSP.md, 15_15a_Paeds_-_ITP_and_Acute_Lymphoblastic_Leukaemia.md, 15_15b_Paeds_-_Primary_Immunodeficiencies_and_SCID.md` | 4 | Moderate prior work |
| G29 | `verify: 15_16a_Paeds_-_Hypothyroidism.md, 15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA.md, 15_17a_Paeds_-_Hyperthyroidism_and_Approach_to_Inherited_Metabolic_Disease.md, 15_17b_Paeds_-_Glycogen_Storage_Disorders__PKU__Lysosomal_Storage_Diseases.md, 15_18a_Paeds_-_Precocious_and_Delayed_Puberty__CAH.md` | 4 | Moderate prior work |
| G30 | `verify: 15_18b_Paeds_-_Genetic_Disorders_Inheritance_Summary.md, 15_20a_Paeds_-_Trisomies_and_Sex_Chromosome_Disorders.md, 15_20b_Paeds_-_Imprinting_Disorders__Prader-Willi__Angelman_.md, 15_21a_Paeds_-_Microdeletion_Syndromes__Cri_du_Chat__DiGeorge__Williams_.md, 15_21b_Paeds_-_Fragile_X__Achondroplasia__Noonan__Marfan.md` | 4 | Moderate prior work |
| G31 | `verify: 15_19a_Paeds_-_Developmental_Milestones_and_Delay.md, 15_19b_Paeds_-_Cerebral_Palsy_and_Muscular_Dystrophies.md` | 4 | Moderate prior work |
| G32 | `verify: 15_22a_Paeds_-_Neonatal_Sepsis_and_Seizures.md, 15_22b_Paeds_-_Neonatal_Respiratory_Distress_and_Jaundice.md, 15_23a_Paeds_-_NEC__Neonatal_Hypoglycaemia__Hypotonia.md, 15_23b_Paeds_-_Minor_Neonatal_Problems.md` | 4 | Moderate prior work |
| G33 | `verify: 15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse.md, 15_24b_Paeds_-_Screening__SIDS__Vaccination_Schedule.md` | 4 | Moderate prior work — SIDS equity finding was late here, worth another pass |
| G34 | `verify: 16_06-07_Ante-Perinatal_Infections.md, 16_08-09_Antenatal_and_Perinatal_Problems.md` | 4 | Moderate prior work |
| G35 | `verify: 16_14-15_Obstetric_Emergencies.md, 16_16-17_Contraception.md` | 4 | Moderate prior work — HELLP/praevia mechanism fixes were late here, worth another pass |
| G36 | `verify: 17_01_FGM__Amenorrhoea__PCOS.md, 17_02_Menorrhagia__PMS__Menopause__HRT.md` | 4 | Moderate prior work |
| G37 | `verify: 17_03_Termination_of_Pregnancy_and_Miscarriage.md, 17_04_Ectopic_Pregnancy_and_GTD.md` | 4 | Moderate prior work — ectopic mechanism fix was late, worth another pass |
| G38 | `verify: 17_05_PID__Endometriosis__Fibroids.md, 17_06_Subfertility_and_OHSS.md` | 4 | Moderate prior work |
| G39 | `verify: 17_07_Vulval_Problems__Genital_Warts_and_Herpes__Vulval_Carcinoma.md, 17_08_Vaginal_Discharge__Urinary_Incontinence__Pelvic_Organ_Prolapse.md, 17_09_Cervical__Vaginal_and_Endometrial_Cancer.md, 17_10_Ovarian_Cancer__Cysts_and_Torsion.md` | 4 | Moderate prior work — cervical screening equity fix was late, worth another pass |
| G40 | `verify: 08_01-03_Infectious_Disease_-_Bacterial_Infections.md, 08_04_Infectious_Disease_-_Antibiogram.md` | **0** | **Added 2026-08-29 — was in no queue row at all.** 08_01-03 is 43 KB, larger than most files in G1–G39. Both have had opportunistic work this session (Passive Immunisation built; the antibiogram box identified as the model scoped box) but neither was ever a queue target |
| G41 | `verify: 08_05-06_Infectious_Disease_-_Viral_Infections.md, 08_09_Infectious_Disease_-_Miscellaneous.md, 08_10_Infectious_Disease_-_Diarrhoea_DDx_and_Gastroenteritis.md` | **0** | **Added 2026-08-29 — was in no queue row at all.** 08_09 is 42 KB and owns the returned-traveller and sepsis frameworks that four other files cite |
| G42 | `verify: 09_08_Dermatology_-_Miscellaneous.md, 10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers.md, 10_12_Oncology_-_Breast.md` | **0** | **Added 2026-08-29 — was in no queue row at all.** 09_08 is 36 KB and owns the non-blanching-rash content the fever red-flag box points at |
| G43 | `verify: 11_02_Ortho_-_Upper_Limb__Shoulder__Elbow__Distal_Radius_Fractures_.md` | **0** | **Added 2026-08-29 — was in no queue row at all.** The only orthopaedic file omitted from G10–G13, which cover 11_01 and 11_03–11_10 |
| G44 | `verify: 18_Geriatrics_and_Older_Persons_Health.md` | **0 (verify)** | **Added 2026-08-29.** Reachable only through **N1**, a *build* row naming the topic rather than the file, so 49 KB of content has been built and never given a file-level verification pass |
| G45 | `verify: 19_General_Practice_and_Preventive_Medicine.md` | **0 (verify)** | **Added 2026-08-29.** Same shape as G44 — reachable only through **N6**, a build row. Also holds the 16 N6 rows recorded as allocated but unbuilt |

### New content required (Step 21 finding) — not verification, genuine build-from-scratch

These are fundamentally different from every row above: there's no existing file to run the 26-step pipeline (Steps 0–25) against. Run estimates here mean "rounds to research and build," not "rounds to re-check."

| # | Prompt | Est. rounds | Why |
|---|---|---|---|
| ~~N1~~ ✅ | ~~`build new content: Older Persons Health / Geriatrics — capacity assessment, cognitive screening context (link to the existing MMSE/MoCA/AMTS entry, don't duplicate), delirium vs dementia vs depression, discharge planning, elder abuse, falls, frailty, long-term care planning, osteoporosis/falls fracture prevention, polypharmacy/deprescribing` | 5–7 | 11 topics, 9 High yield, from genuinely zero existing coverage — the single largest gap found in this project |
| N2 | `build new content: Public Health/Epidemiology — NNT and absolute vs relative risk reduction, study design types and bias, p-value interpretation (verify Notifiable Diseases and sensitivity/specificity are genuinely already adequate first, don't rebuild what exists)` | 2–3 | 6 topics, but 2 already effectively covered |
| ~~N3~~ ✅ | ~~`build new content: Injury, Poisoning, Envenomation & Environmental — Shock, adult choking, major trauma, traumatic head injury, lacerations/abrasions, adult resuscitation (confirm Burns and paediatric/neonatal resuscitation status first, may already partially exist)` | 4–5 | 10 topics including Shock (High yield); several may already be scattered in emergency-medicine content elsewhere and just need consolidating rather than writing from zero |
| ~~N4~~ ✅ | ~~`build new content: Australian Context of Health — Australian healthcare system structure, rural general practice issues, detention/prison/immigration health (distinct from the disease-specific equity content already woven throughout the project)` | 2 | 4 topics, Low–Medium yield |
| N5 | `verify: Clinical-Process-EBM-Consent-Capacity.md` | 1 | Already substantially covers both CSV rows in this category — light confirmation pass, not a build |
| N6 | `build new content: General Practice/Preventive Med/Ethics/Communication — motivational interviewing stages-of-change model, domestic violence screening/safety-planning/mandatory reporting, continuity of care, consolidated preventive medicine/screening reference (cancer screening, CV/diabetes prevention, smoking cessation as one framework); check remaining items (breaking bad news, ICE, handover, mandatory reporting generally, driving fitness beyond what's in Neurology already) against existing Communication.md/History-Taking.md content before assuming absent` | 5–7 | 29 topics, many High yield — the second-largest gap found in this project, found only on a second pass of Step 21 |
| N7 | `verify: 08_08_Infectious_Disease_-_Genitourinary_Infections_and_STIs.md, 17_07_Vulval_Problems__Genital_Warts_and_Herpes__Vulval_Carcinoma.md` against the full Sexual Health/STIs CSV list — confirm chancroid, granuloma inguinale, and *Mycoplasma genitalium* have genuine depth, not just a passing mention | 1–2 | 12 topics, most already substantially covered — this is mainly a verification pass |

**New-content total: 20–27 rounds**, dominated by N1 (Geriatrics, 5–7, found via Step 21) and N6 (GP/Preventive/Ethics/Communication, 5–7, found via Step 23 — Step 21's own blind spot, since GP/Ethics/Communication was never "(NEW)"-tagged) — two categories of comparable size and yield, neither caught by the same check. This should be prioritised **before** grinding through more re-verification rounds on already-built files — two unbuilt High-yield categories are a bigger real exam risk than another re-check of an already-thorough Cardiology file.

### Totals

- Mega: 10 groups, 38 runs (3×7 + 5×1 + 6×2)
- Large: 10 groups, 35 runs (3×6 + 4×3 + 5×1)
- Medium/small: 39 groups, 141 runs (3×15 + 4×24)

**Total estimated runs to apply the full current 26-step workflow (Steps 0–25) across all 146 existing files: ~214.** Down slightly from ~215 — the first time this number has moved down rather than up, specifically because Examination.md received genuine substantial work this round (the Newborn Examination build) rather than staying purely reactive, earning a real reclassification rather than just more testing revealing more to do. This is worth contrasting with every previous change to this number: three rises came from testing revealing more outstanding work (Step 17's real hit, Steps 18–20 adding untested checks, Step 24's MSK finding); this is the first that came from actual progress closing a gap, not from discovering a new one.

**Plus 20–27 rounds of genuinely new content** (Steps 21 and 23, table above) — this is additional to the 214, not included in it, since it's a different kind of work entirely (building, not re-checking). **Combined honest total: ~234–244 rounds** to reach the intern/RMO standard across everything currently known to check for, old and new.

**Worth naming directly: Step 21 itself just demonstrated the exact problem this whole document keeps running into.** Its first version, run once, found Geriatrics and called it done. Running it again with a slightly broader question — not "which categories are marked NEW" but "which categories, period, have never actually been pulled" — found a second, comparably-sized gap sitting in plain sight the whole time. There's no way to know this won't happen a third time.

The same caveat holds regardless of which number is used: this assumes 23 steps is the final set, and this project's own history — new techniques found real gaps five separate times now, the fifth being the discovery of an entire missing category — says that assumption shouldn't be trusted indefinitely.

## What "good" actually means — the reporting standard

Only state a file range is complete if:
- Every step above has been run against it (not just the ones that happened to find something last time).
- Every automated-scan hit has been manually verified, with false positives explicitly identified as such (not silently dropped).
- Any genuine gap found has been fixed and re-verified, not just noted.
- The final comprehensive sweep (Step 12) came back clean.

If a technique hasn't been tried yet on a given range, or a check was done superficially in an earlier round, say so — "good" should mean genuinely exhausted, not "nothing new happened to turn up this time."

## Phase 5 THIRD PASS — enumerate first, then check every item

> [!danger] **The enumeration bar was met for one part out of four. That is the headline, and it is stated before any finding.**
> The rule for this pass was: build a numbered, complete enumeration from an **authoritative external source** before any corpus-checking, then report a result for **every** numbered item. Three of the four parts could not clear the first half of that rule.
>
> | Part | Enumeration source attempted | Outcome |
> |---|---|---|
> | **C — medications** | AMH / BNF therapeutic classification | **Blocked.** WebSearch returns a result stating the complete AMH chapter breakdown is subscription-gated; `WebFetch` to `amc.org.au` returns `EGRESS_BLOCKED`. **Antimicrobials only** were enumerable, from the taxonomy supplied in the request itself — expanded to 75 named agents. **The other ten therapeutic classes (cardiovascular, respiratory, CNS, endocrine, GI, renal, haematological, musculoskeletal, dermatological, ophthalmic) received no third-pass enumeration.** |
> | **B — scales** | 38 specialty searches | **One family enumerated externally**, the RADS reporting systems (16, from a 2025 *Insights into Imaging* review). The other 37 specialties did not get an enumeration pass. |
> | **A — conditions** | 38 specialty searches + textbook index | **Not attempted this pass.** The second-pass finding stands: the sources are egress-blocked and the enumeration did not happen. Nothing has changed to make it achievable. |
> | **D — procedures** | AMC prevocational framework | **Blocked.** `amc.org.au/wp-content/.../Guide-to-Prevocational-Training…pdf` returns `EGRESS_BLOCKED`; the search snippet says explicitly the procedural list is not in the snippet and requires the document. |
>
> **The largest enumeration actually achieved is 75 antimicrobial agents + 16 RADS systems = 91 items, all checked, all reported.** Everything else on this pass is unenumerated and must not be read as cleared.

### The scan's own defects, found by running it (rule 7)

Three, all mine, all found before the results were reported:

- **Union scoring hid the defect it was meant to find.** The first version scored the union of every paragraph naming a drug corpus-wide — so an agent could score ADEQUATE with mechanism in one file, a dose in a second and monitoring in a third, while **no single entry teaches it**. That is the character-window flaw inverted. Fixed: every agent now carries two verdicts, `corpus` (union) and `entry` (best single paragraph). **17 of 75 split.**
- **The scan counted its own workflow document as corpus.** `MASTER_VERIFICATION_WORKFLOW.md` and `PENDING_GUIDELINE_CHECKS.md` *name* drugs while describing the gaps in them. A scan reading them reports coverage it created itself. Meta files are now excluded by name.
- **A keyword proxy is not the concept.** Macrolides score `harm+contra` off generic "diarrhoea"/"avoid"/"allergy" text in entries that merely prescribe them. **Verified by hand: the corpus carries zero QT-prolongation content for any macrolide** — the second-pass finding stands and the new scan disagreeing with it is the scan being wrong. **ADEQUATE from this scan means "nothing this scan can see is missing." It does not clear an item.**

### Part C — enumeration (75 antimicrobial agents)

**Source, stated honestly:** the taxonomy supplied in the request (penicillins / cephalosporins by generation / macrolides / tetracyclines / aminoglycosides / glycopeptides / fluoroquinolones / sulfonamides / nitroimidazoles / lincosamides / antifungals by subclass / antivirals by target), expanded to named agents. **This is not an extract of the AMH or the BNF** — those are subscription-gated. Scan: `scripts/drug_depth.py`.

**Result: 46 ADEQUATE · 16 THIN · 5 NAMED ONLY · 8 ABSENT.**

| # | Agent | Group | Uses | Verdict | Dimensions found |
|---|---|---|---|---|---|
| 1 | benzylpenicillin (penicillin G) | Penicillins | 22 | ADEQUATE / entry THIN | dose+harm+contra |
| 2 | phenoxymethylpenicillin (penicillin V) | Penicillins | 11 | ADEQUATE | mech+dose+harm+contra |
| 3 | benzathine benzylpenicillin | Penicillins | 7 | ADEQUATE / entry THIN | dose+harm+contra |
| 4 | procaine penicillin | Penicillins | 0 | ABSENT | - |
| 5 | flucloxacillin (antistaphylococcal) | Penicillins | 21 | ADEQUATE | mech+dose+harm+contra |
| 6 | amoxicillin / ampicillin | Penicillins | 46 | ADEQUATE | mech+dose+harm+contra |
| 7 | amoxicillin-clavulanate | Penicillins | 11 | ADEQUATE | mech+dose+harm+contra |
| 8 | piperacillin-tazobactam | Penicillins | 21 | ADEQUATE / entry THIN | mech+dose+harm+contra |
| 9 | 1st gen — cefalexin | Cephalosporins | 7 | ADEQUATE | mech+dose+contra |
| 10 | 1st gen — cefazolin | Cephalosporins | 8 | ADEQUATE | dose+harm+contra |
| 11 | 2nd gen — cefuroxime | Cephalosporins | 7 | ADEQUATE | mech+dose+contra |
| 12 | 2nd gen — cefoxitin | Cephalosporins | 0 | ABSENT | - |
| 13 | 3rd gen — ceftriaxone / cefotaxime | Cephalosporins | 50 | ADEQUATE | mech+dose+harm+contra |
| 14 | 3rd gen antipseudomonal — ceftazidime | Cephalosporins | 3 | ADEQUATE / entry THIN | mech+dose+contra |
| 15 | 4th/5th gen — cefepime, ceftaroline | Cephalosporins | 5 | ADEQUATE / entry THIN | mech+dose+contra |
| 16 | meropenem / imipenem / ertapenem | Carbapenems/monobactam | 14 | ADEQUATE / entry THIN | mech+dose+harm+contra |
| 17 | aztreonam | Carbapenems/monobactam | 1 | NAMED ONLY | - |
| 18 | azithromycin | Macrolides | 45 | ADEQUATE | mech+dose+harm+contra |
| 19 | roxithromycin | Macrolides | 1 | THIN | dose+contra |
| 20 | clarithromycin | Macrolides | 24 | ADEQUATE / entry THIN | dose+harm+contra |
| 21 | erythromycin | Macrolides | 21 | ADEQUATE / entry THIN | mech+dose+harm+contra |
| 22 | doxycycline | Tetracyclines | 42 | ADEQUATE | mech+dose+harm+contra |
| 23 | minocycline | Tetracyclines | 0 | ABSENT | - |
| 24 | tetracycline / tigecycline | Tetracyclines | 5 | THIN | dose+contra |
| 25 | gentamicin | Aminoglycosides | 15 | ADEQUATE / entry THIN | dose+harm+contra |
| 26 | tobramycin | Aminoglycosides | 2 | NAMED ONLY | - |
| 27 | amikacin | Aminoglycosides | 0 | ABSENT | - |
| 28 | vancomycin | Glycopeptides/lipopeptides | 20 | ADEQUATE | mech+dose+harm+contra |
| 29 | teicoplanin | Glycopeptides/lipopeptides | 4 | THIN | dose+contra |
| 30 | daptomycin | Glycopeptides/lipopeptides | 1 | NAMED ONLY | - |
| 31 | ciprofloxacin | Fluoroquinolones | 21 | ADEQUATE | mech+dose+harm+contra |
| 32 | norfloxacin | Fluoroquinolones | 1 | THIN | dose |
| 33 | moxifloxacin | Fluoroquinolones | 3 | THIN | mech+contra |
| 34 | levofloxacin / ofloxacin | Fluoroquinolones | 25 | ADEQUATE | mech+dose+harm+contra |
| 35 | trimethoprim | Sulfonamides/DHFR | 18 | ADEQUATE | mech+dose+harm+contra |
| 36 | trimethoprim-sulfamethoxazole (co-trimoxazole) | Sulfonamides/DHFR | 12 | ADEQUATE | mech+dose+harm+contra |
| 37 | metronidazole | Nitroimidazoles | 41 | ADEQUATE | mech+dose+harm+contra |
| 38 | tinidazole | Nitroimidazoles | 0 | ABSENT | - |
| 39 | clindamycin | Lincosamides | 21 | ADEQUATE | mech+dose+harm+contra |
| 40 | lincomycin | Lincosamides | 0 | ABSENT | - |
| 41 | nitrofurantoin | Other antibacterial | 7 | ADEQUATE | mech+dose+contra |
| 42 | fosfomycin | Other antibacterial | 2 | ADEQUATE | mech+dose+contra |
| 43 | linezolid | Other antibacterial | 3 | THIN | dose+contra |
| 44 | rifampicin | Other antibacterial | 21 | ADEQUATE | mech+dose+harm+contra |
| 45 | chloramphenicol | Other antibacterial | 6 | ADEQUATE / entry THIN | dose+harm+contra |
| 46 | colistin / polymyxin | Other antibacterial | 0 | ABSENT | - |
| 47 | fluconazole | Antifungal — azoles | 7 | THIN | dose+contra |
| 48 | itraconazole | Antifungal — azoles | 3 | ADEQUATE | dose+harm+contra |
| 49 | voriconazole / posaconazole | Antifungal — azoles | 1 | NAMED ONLY | - |
| 50 | clotrimazole / miconazole (topical) | Antifungal — azoles | 5 | ADEQUATE | dose+harm+contra |
| 51 | ketoconazole | Antifungal — azoles | 7 | ADEQUATE / entry THIN | mech+dose+harm+contra |
| 52 | terbinafine (allylamine) | Antifungal — other | 4 | ADEQUATE | dose+harm+contra |
| 53 | nystatin / amphotericin B (polyenes) | Antifungal — other | 4 | THIN | harm |
| 54 | caspofungin / anidulafungin (echinocandins) | Antifungal — other | 0 | ABSENT | - |
| 55 | griseofulvin | Antifungal — other | 2 | ADEQUATE | dose+harm+contra |
| 56 | aciclovir | Antiviral — herpes family | 32 | ADEQUATE | dose+harm+contra |
| 57 | valaciclovir | Antiviral — herpes family | 2 | THIN | harm+contra |
| 58 | famciclovir | Antiviral — herpes family | 2 | ADEQUATE / entry THIN | dose+harm+contra |
| 59 | ganciclovir / valganciclovir (CMV) | Antiviral — herpes family | 2 | THIN | dose+harm |
| 60 | oseltamivir | Antiviral — influenza | 3 | THIN | mech+contra |
| 61 | zanamivir | Antiviral — influenza | 3 | THIN | mech+contra |
| 62 | tenofovir | Antiviral — HIV/hepatitis | 4 | ADEQUATE | mech+dose+harm+contra |
| 63 | emtricitabine / lamivudine | Antiviral — HIV/hepatitis | 2 | ADEQUATE | mech+dose+harm+contra |
| 64 | dolutegravir / raltegravir (integrase inhibitors) | Antiviral — HIV/hepatitis | 6 | ADEQUATE | mech+harm+contra |
| 65 | entecavir (hep B) | Antiviral — HIV/hepatitis | 1 | THIN | dose |
| 66 | sofosbuvir / DAA (hep C) | Antiviral — HIV/hepatitis | 1 | THIN | harm |
| 67 | isoniazid | Antituberculous | 16 | ADEQUATE / entry THIN | mech+dose+harm+contra |
| 68 | rifampicin (TB regimen role) | Antituberculous | 21 | ADEQUATE | mech+dose+harm+contra |
| 69 | pyrazinamide | Antituberculous | 3 | ADEQUATE / entry THIN | mech+harm+contra |
| 70 | ethambutol | Antituberculous | 3 | ADEQUATE / entry THIN | mech+harm+contra |
| 71 | ivermectin | Antiparasitic | 14 | ADEQUATE / entry THIN | dose+harm+contra |
| 72 | permethrin | Antiparasitic | 7 | ADEQUATE / entry THIN | dose+harm+contra |
| 73 | albendazole / mebendazole | Antiparasitic | 4 | THIN | harm |
| 74 | praziquantel | Antiparasitic | 1 | NAMED ONLY | - |
| 75 | artemether-lumefantrine / atovaquone-proguanil (malaria) | Antiparasitic | 2 | THIN | dose+harm |

**All 8 ABSENT re-verified against markdown emphasis stripping** (rule 2): `procaine|cefoxitin|minocyclin|amikacin|tinidazol|lincomycin|colistin|polymyxin|fungin|echinocandin` — zero hits with `[*_`]` removed. The single "procaine" hit is **procaine the local anaesthetic** in `03a_Anaesthetics_Primer.md:123`, not procaine penicillin.

> [!warning] **Three absences were hidden inside lumped rows** — a defect of the enumeration's own granularity, not of the corpus. Items 15, 49 and 53 pair an agent that is present with one that is not: **ceftaroline (0), posaconazole (0) and nystatin (0)** are each absent while their row-mate (cefepime 5, voriconazole 1, amphotericin 5) is present. Lumping two agents in one numbered item makes an absence unreportable. Recorded rather than silently merged.

**Judged against the intern/RMO ceiling (Step 18), the 8 absences and 5 named-only split cleanly:** procaine penicillin, cefoxitin, minocycline, amikacin, tinidazole, lincomycin, colistin, echinocandins, ceftaroline, posaconazole, aztreonam, daptomycin, tobramycin, praziquantel are **correctly absent or correctly named-only** — an intern recognises them, does not prescribe them. **Nystatin is the one absence that is not** — topical oral/nappy candidiasis is intern work and the corpus prescribes for candidiasis elsewhere.

**The THIN results that matter at intern level**, and are queued below: **the influenza antivirals** (oseltamivir/zanamivir — mechanism and contraindication only, no Australian dosing or the 48-hour window), **valaciclovir/famciclovir dosing** (aciclovir is ADEQUATE; its two oral alternatives are not), and **albendazole/mebendazole** (threadworm is a GP-level presentation; `harm` only, no dose).

### Part B — RADS reporting systems (16, externally enumerated)

**Source:** *RADS ALPHABET: news and tips for young and general radiologists*, Insights into Imaging (2025) — the only complete named list this pass could reach.

**Result: 16 of 16 ABSENT.** BI-RADS · Bone-RADS · C-RADS · CAD-RADS · LI-RADS · Lung-RADS · MET-RADS-P · MY-RADS · NI-RADS · Node-RADS · O-RADS · ONCO-RADS · PI-RADS · ST-RADS · TI-RADS · VI-RADS — all zero hits with emphasis stripped and hyphen/space variants allowed.

**Twelve of the sixteen are correctly absent** (subspecialist reporting systems an intern never uses). **Four are not**, because an intern reads reports that carry them and is asked what the number means: **BI-RADS** (breast lump workup), **PI-RADS** (prostate MRI), **TI-RADS** (thyroid nodule), **Lung-RADS** (lung screening). This narrows the second pass's "10 of 11 absent" to a specific, defensible four.

| Item | Source | Status |
|---|---|---|
| **P5-C5** | **Influenza antivirals** — oseltamivir/zanamivir Australian dosing, the 48-hour treatment window, and who is eligible. Mechanism and contraindication present, dose absent | ⬜ |
| **P5-C6** | **Valaciclovir and famciclovir dosing** — aciclovir is fully covered; its two oral alternatives carry no dose | ⬜ |
| **P5-C7** | **Nystatin** — absent entirely; topical antifungal for oral and nappy candidiasis, both intern-level | ⬜ |
| **P5-C8** | **Albendazole / mebendazole** — threadworm dosing, absent; a GP-level paediatric presentation | ⬜ |
| **P5-B6** | **BI-RADS, PI-RADS, TI-RADS, Lung-RADS** — what the number means when it appears on a report an intern is handed. The other 12 RADS systems are correctly out of scope | ⬜ |
| **P5-C9** | ~~The ten non-antimicrobial therapeutic classes were never enumerated.~~ **CLOSED — SUPERSEDED, not built.** Written during the third pass, when only antimicrobials could be enumerated. The AMH therapeutic classification supplied afterwards covers all 21 top-level classes including these ten, and the fourth pass walked all **276 leaf subclasses** (`scripts/drug_classes.py`, commit `3e543ef`) — that pass is where the SGLT2, GLP-1, PCSK9, triptan, CGRP, TNF-alpha and xanthine-oxidase findings came from. The enumeration is now saved as `data/amh_276_leaf_classification.txt` rather than living only inside the script. **Nothing further to do under this ID.** | ✅ |
| **P5-A4** | **Part A's 38-specialty enumeration still has not happened** — third pass, same blocker, recorded again rather than dropped | ⬜ |
| **P5-D8** | **Part D's 38-specialty enumeration still has not happened** — AMC prevocational framework PDF is egress-blocked | ⬜ |

## Phase 5 FOURTH PASS — every leaf subclass of the AMH therapeutic classification

**Enumeration source:** *South Australian Medicines Formulary Framework*, Appendix 1 — Therapeutic Classes of Medicines (AMH), supplied in full by the user. This is the first drug enumeration in Phase 5 that **this project did not build itself**. 21 top-level classes expanded to their **276 bottom-level (leaf) subclasses**, each checked, each reported. Scan: `scripts/drug_classes.py`.

**Entry-level result (best single paragraph, not the union): 148 ADEQUATE · 93 THIN · 10 NAMED ONLY · 25 ABSENT.**

> [!warning] **What is still recall-based, stated before the findings.** The source names the **classes**; it does not name their **member drugs**. Mapping each leaf to the drugs that populate it is mine. So a leaf can only be found present through a drug I thought to list — the same weakness as every earlier pass, now confined to one layer instead of the whole list. It is smaller, not gone.
>
> **The source's own defect:** "Drugs for anaemias" appears **twice** under class 7, once with subclasses and once bare. Counted once. A supplied enumeration is not automatically internally coherent — the partition check applies to it too.

### Scan defects found by running it (rule 7), before the numbers were used

- **Four ABSENT verdicts were scan artifacts, found by hand-checking all 28.** `sodium cromogl**i**cate` (the Australian spelling; the pattern had *cromoglycate*) · `steroid **eye** drops` (the pattern demanded "steroid drops") · eye antibacterials matched drug-then-eye only, so `chloramphenicol eye drops` scored while the same construction for other agents did not · ocular antihistamines. Fixed and re-run: **28 ABSENT → 25**. Ratio: **4 dismissed, 24 confirmed.**
- **The mechanism proxy detects pharmacological register, not explanation.** Anticholinergics (eye) scored NAMED ONLY against a line that explains the mechanism perfectly in plain clinical English — *"cycloplegics (dilate the pupil, relieving pain and photophobia, and preventing posterior synechiae)"*. No word in it is mechanism-vocabulary. **Every NAMED ONLY and THIN verdict in this table may be this failure rather than a gap**, which is why none is queued without being read first.
- **46 leaves split corpus-ADEQUATE / entry-THIN** — the fact exists somewhere but no single entry teaches it. Marked `(corpus adequate)` in the table.

### The twelve priority classes, reported first

| # | Leaf | Entry verdict | Reading |
|---|---|---|---|
| 20 | **Carbapenems** | THIN *(corpus adequate)* | 16 uses; dose and caution present, **no mechanism or the ESBL/last-line stewardship point in any one entry** |
| 22 | Glycopeptides | ADEQUATE | vancomycin carries it; teicoplanin thin, correctly |
| 27 | Rifamycins | ADEQUATE | mechanism, harm, interactions all present |
| 29 | **Antimycobacterials** | THIN *(corpus adequate)* | 25 uses; mechanism and dose in one entry, **the toxicity profile that drives intern monitoring is elsewhere** |
| 38–42 | **Antiretrovirals — all four subclasses + other** | ADEQUATE ×5 | NRTI, NNRTI, protease, integrase, other all carry ≥3 dimensions in a single entry. **The predicted gap is not there.** |
| 63 | PCSK9 inhibitors | ADEQUATE | mech+dose+harm |
| 118 | GLP-1 analogues | ADEQUATE | |
| 119 | SGLT2 inhibitors | ADEQUATE | all four dimensions — euglycaemic DKA content is doing the work |
| 216 | Triptans | ADEQUATE | |
| 217 | **CGRP antagonists** | **ABSENT** | zero hits for erenumab, fremanezumab, galcanezumab, rimegepant or "CGRP" |
| 267 | **TNF-alpha antagonists** | THIN *(corpus adequate)* | 21 uses; **no single entry carries the pre-treatment TB/hepatitis screening and infection risk** — the part an intern acts on |
| 270 | Xanthine oxidase inhibitors | ADEQUATE | allopurinol well covered |

**Nine of twelve came back adequate.** The antiretroviral prediction was wrong in the corpus's favour, and that is worth stating as plainly as the gaps.

### The 25 ABSENT leaves, judged against the intern ceiling

**Genuine gaps at intern level (5):**

| Leaf | Why it matters |
|---|---|
| **Snake antivenoms** and **other antivenoms** | Zero hits for `antivenom` anywhere in 148 files. Australian envenomation is core ED intern work and the pressure-immobilisation/antivenom pathway is examinable |
| **H2 antagonists** | Zero hits for ranitidine, famotidine, nizatidine or the class name. PPIs are covered; the alternative class is not named once |
| **Oral and intranasal decongestants** | Zero for pseudoephedrine, oxymetazoline. Rebound rhinitis medicamentosa is a standard teaching point |
| **Other laxatives (bulk-forming)** | Zero for psyllium, ispaghula, Metamucil. The other four laxative leaves are covered; this one is not — an asymmetric silence inside a class the corpus otherwise teaches |
| **CGRP antagonists** | Now PBS-listed migraine prophylaxis; the other migraine leaves are adequate |

**Correctly absent at intern level (20):** echinocandins · other dermatological drugs · ear antiseptics · intranasal antihistamines · nonselective alpha-blockers · six ophthalmic leaves (eye aminoglycosides, eye quinolones, ocular antivirals, ocular vasoconstrictors, ocular NSAIDs, mydriatics, ocular local anaesthetics — the glaucoma and allergic-eye leaves *are* covered) · drugs for kidney stones · other hormonal antineoplastics · other vaginal anti-infectives · non-amphetamine psychostimulants · orexin antagonists · opioid cough suppressants. An intern recognises these; they do not prescribe them unsupervised.

### New build items

| Item | Source | Status |
|---|---|---|
> [!note] **Status for these eight lives in `PENDING_GUIDELINE_CHECKS.md`, not here.** They were written up in this
> narrative and then queued in the tracker, leaving two copies of each ID with independent status markers — so a
> build could tick one and leave the other reading as unstarted. The tracker is the single source of truth for build
> status; the rows below are kept as the narrative record of what the fourth pass found, with their status cells
> pointing at the tracker rather than asserting one.

| **P5-C10** | **Antivenoms** — snake and other Australian envenomation: pressure-immobilisation, when to give antivenom, premedication, serum sickness. Absent entirely | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C11** | **H2 antagonists** — where they still sit relative to PPIs; absent entirely | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C12** | **Decongestants** — oral and intranasal, and rhinitis medicamentosa; absent entirely | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C13** | **Bulk-forming laxatives** — the one laxative leaf of five with no coverage | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C14** | **CGRP antagonists** — PBS-listed migraine prophylaxis; absent | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C15** | **Carbapenems** — mechanism and the stewardship/ESBL rationale in one place | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C16** | **TNF-alpha antagonists** — pre-treatment TB and hepatitis B screening, infection risk while on treatment | → tracked in `PENDING_GUIDELINE_CHECKS.md` |
| **P5-C17** | **Antimycobacterials** — the four-drug regimen's toxicity and monitoring profile in the entry that teaches the regimen | → tracked in `PENDING_GUIDELINE_CHECKS.md` |

### Complete result — all 276 leaf subclasses

Verdict is the **best single entry**; `(corpus adequate)` marks a leaf whose facts exist but are scattered across entries.

| # | AMH class | Leaf subclass | Verdict | Paragraphs | Dimensions in that entry |
|---|---|---|---|---|---|
|   1 | 1 Allergy and anaphylaxis | Sympathomimetics (anaphylaxis) | **ADEQUATE** | 66 | mech+dose+harm+contra |
|   2 | 1 Allergy and anaphylaxis | Sedating antihistamines | **ADEQUATE** | 5 | dose+harm+contra |
|   3 | 1 Allergy and anaphylaxis | Less sedating antihistamines | **THIN** | 3 | dose+contra |
|   4 | 2 Anaesthetics | IV general anaesthetics | **THIN *(corpus adequate)*** | 8 | harm+contra  <<ASSEMBLED>> |
|   5 | 2 Anaesthetics | Inhaled anaesthetics | **ADEQUATE** | 10 | mech+dose+harm |
|   6 | 2 Anaesthetics | Non-depolarising neuromuscular blockers | **THIN** | 1 | contra |
|   7 | 2 Anaesthetics | Depolarising neuromuscular blockers | **ADEQUATE** | 3 | mech+dose+harm |
|   8 | 2 Anaesthetics | Alpha2 and imidazoline agonists | **THIN** | 3 | dose |
|   9 | 2 Anaesthetics | Opioids (anaesthesia) | **ADEQUATE** | 8 | dose+harm+contra |
|  10 | 2 Anaesthetics | Anticholinergics (anaesthesia) | **ADEQUATE** | 16 | dose+harm+contra |
|  11 | 2 Anaesthetics | Drugs for reversing neuromuscular blockade | **ADEQUATE** | 2 | mech+harm+contra |
|  12 | 2 Anaesthetics | Local anaesthetics | **ADEQUATE** | 22 | mech+dose+contra |
|  13 | 3 Analgesics | Non-opioid analgesics | **ADEQUATE** | 92 | mech+dose+harm+contra |
|  14 | 3 Analgesics | Opioid analgesics | **ADEQUATE** | 55 | dose+harm+contra |
|  15 | 4 Antidotes and antivenoms | Gastrointestinal decontaminants | **ADEQUATE** | 2 | mech+dose+contra |
|  16 | 4 Antidotes and antivenoms | Antidotes | **ADEQUATE** | 29 | mech+dose+harm+contra |
|  17 | 4 Antidotes and antivenoms | Snake antivenoms | **ABSENT** | 0 | — |
|  18 | 4 Antidotes and antivenoms | Other antivenoms | **ABSENT** | 0 | — |
|  19 | 5 Anti-infectives | Aminoglycosides | **ADEQUATE** | 25 | dose+harm+contra |
|  20 | 5 Anti-infectives | Carbapenems | **THIN *(corpus adequate)*** | 16 | dose+contra  <<ASSEMBLED>> |
|  21 | 5 Anti-infectives | Cephalosporins | **ADEQUATE** | 89 | mech+dose+contra |
|  22 | 5 Anti-infectives | Glycopeptides | **ADEQUATE** | 24 | mech+harm+contra |
|  23 | 5 Anti-infectives | Lincosamides | **THIN *(corpus adequate)*** | 21 | dose+contra  <<ASSEMBLED>> |
|  24 | 5 Anti-infectives | Macrolides | **ADEQUATE** | 107 | mech+dose+harm+contra |
|  25 | 5 Anti-infectives | Penicillins | **ADEQUATE** | 157 | mech+dose+contra |
|  26 | 5 Anti-infectives | Quinolones | **ADEQUATE** | 56 | mech+dose+contra |
|  27 | 5 Anti-infectives | Rifamycins | **ADEQUATE** | 25 | mech+harm+contra |
|  28 | 5 Anti-infectives | Tetracyclines | **ADEQUATE** | 56 | mech+harm+contra |
|  29 | 5 Anti-infectives | Antimycobacterials | **THIN *(corpus adequate)*** | 25 | mech+dose  <<ASSEMBLED>> |
|  30 | 5 Anti-infectives | Other antibacterials | **ADEQUATE** | 78 | mech+dose+contra |
|  31 | 5 Anti-infectives | Azoles (antifungal) | **ADEQUATE** | 23 | dose+harm+contra |
|  32 | 5 Anti-infectives | Echinocandins | **ABSENT** | 0 | — |
|  33 | 5 Anti-infectives | Other antifungals | **ADEQUATE** | 11 | dose+harm+contra |
|  34 | 5 Anti-infectives | Guanine analogues (antiviral) | **ADEQUATE** | 36 | dose+harm+contra |
|  35 | 5 Anti-infectives | Neuraminidase inhibitors | **THIN** | 6 | mech+contra |
|  36 | 5 Anti-infectives | Antivirals for viral hepatitis | **THIN** | 4 | dose |
|  37 | 5 Anti-infectives | Other antivirals | **ADEQUATE** | 9 | mech+dose+contra |
|  38 | 5 Anti-infectives | NRTIs | **ADEQUATE** | 12 | mech+harm+contra |
|  39 | 5 Anti-infectives | NNRTIs | **ADEQUATE** | 3 | mech+harm+contra |
|  40 | 5 Anti-infectives | HIV-Protease inhibitors | **ADEQUATE** | 9 | mech+dose+contra |
|  41 | 5 Anti-infectives | Integrase inhibitors | **ADEQUATE** | 9 | mech+harm+contra |
|  42 | 5 Anti-infectives | Other antiretrovirals | **ADEQUATE** | 4 | mech+harm+contra |
|  43 | 5 Anti-infectives | Antimalarials | **ADEQUATE** | 21 | mech+dose+contra |
|  44 | 5 Anti-infectives | Other antiprotozoals | **ADEQUATE** | 50 | mech+dose+harm |
|  45 | 5 Anti-infectives | Benzimidazoles (anthelmintic) | **THIN** | 4 | dose+harm |
|  46 | 5 Anti-infectives | Other anthelmintics | **THIN *(corpus adequate)*** | 15 | dose+harm  <<ASSEMBLED>> |
|  47 | 6 Cardiovascular | Aldosterone antagonists | **ADEQUATE** | 12 | mech+dose+harm+contra |
|  48 | 6 Cardiovascular | Loop diuretics | **ADEQUATE** | 21 | mech+dose+harm+contra |
|  49 | 6 Cardiovascular | Sympathomimetics (cardiovascular) | **ADEQUATE** | 28 | mech+dose+harm |
|  50 | 6 Cardiovascular | Other drugs for heart failure | **ADEQUATE** | 21 | mech+dose+harm+contra |
|  51 | 6 Cardiovascular | Nitrates | **ADEQUATE** | 31 | mech+dose+harm+contra |
|  52 | 6 Cardiovascular | Other antianginal drugs | **ADEQUATE** | 3 | mech+dose+contra |
|  53 | 6 Cardiovascular | Thiazide and related diuretics | **THIN *(corpus adequate)*** | 19 | mech+harm  <<ASSEMBLED>> |
|  54 | 6 Cardiovascular | Other diuretics | **ADEQUATE** | 12 | mech+dose+harm+contra |
|  55 | 6 Cardiovascular | ACE inhibitors | **ADEQUATE** | 39 | mech+dose+harm+contra |
|  56 | 6 Cardiovascular | Sartans | **ADEQUATE** | 16 | mech+dose+harm+contra |
|  57 | 6 Cardiovascular | Calcium channel blockers | **ADEQUATE** | 36 | mech+dose+harm+contra |
|  58 | 6 Cardiovascular | Beta-blockers | **ADEQUATE** | 50 | mech+dose+harm+contra |
|  59 | 6 Cardiovascular | Other antihypertensives | **ADEQUATE** | 10 | mech+dose+harm+contra |
|  60 | 6 Cardiovascular | Antiarrhythmics | **ADEQUATE** | 61 | mech+dose+harm+contra |
|  61 | 6 Cardiovascular | Statins | **ADEQUATE** | 58 | mech+dose+harm+contra |
|  62 | 6 Cardiovascular | Fibrates | **ADEQUATE** | 2 | mech+dose+harm |
|  63 | 6 Cardiovascular | PCSK9 inhibitors | **ADEQUATE** | 2 | mech+dose+harm |
|  64 | 6 Cardiovascular | Other drugs for dyslipidaemia | **ADEQUATE** | 8 | mech+dose+harm |
|  65 | 6 Cardiovascular | Prostacyclins | **THIN** | 4 | mech+contra |
|  66 | 6 Cardiovascular | Endothelin antagonists | **THIN** | 6 | mech+contra |
|  67 | 6 Cardiovascular | PDE5 inhibitors (cardiovascular) | **ADEQUATE** | 9 | mech+dose+contra |
|  68 | 6 Cardiovascular | Other drugs for pulmonary hypertension | **THIN *(corpus adequate)*** | 13 | harm+contra  <<ASSEMBLED>> |
|  69 | 6 Cardiovascular | Drugs for peripheral vascular disease | **THIN** | 1 | contra |
|  70 | 6 Cardiovascular | Drugs for orthostatic hypotension | **ADEQUATE** | 22 | mech+harm+contra |
|  71 | 7 Blood and electrolytes | Heparins | **ADEQUATE** | 26 | mech+dose+contra |
|  72 | 7 Blood and electrolytes | Vitamin K antagonists | **ADEQUATE** | 54 | mech+dose+contra |
|  73 | 7 Blood and electrolytes | Direct thrombin inhibitors | **ADEQUATE** | 8 | mech+dose+harm+contra |
|  74 | 7 Blood and electrolytes | Factor Xa inhibitors | **ADEQUATE** | 20 | mech+dose+harm |
|  75 | 7 Blood and electrolytes | Glycoprotein IIb/IIIa inhibitors | **ADEQUATE** | 3 | mech+dose+harm |
|  76 | 7 Blood and electrolytes | Thienopyridines | **ADEQUATE** | 21 | mech+dose+harm |
|  77 | 7 Blood and electrolytes | Other antiplatelet drugs | **ADEQUATE** | 100 | mech+dose+harm+contra |
|  78 | 7 Blood and electrolytes | Thrombolytics | **THIN *(corpus adequate)*** | 21 | harm+contra  <<ASSEMBLED>> |
|  79 | 7 Blood and electrolytes | Other drugs affecting haemostasis | **ADEQUATE** | 40 | mech+dose+harm |
|  80 | 7 Blood and electrolytes | Drugs for reversing anticoagulation | **ADEQUATE** | 34 | dose+harm+contra |
|  81 | 7 Blood and electrolytes | Erythropoietin agonists | **THIN *(corpus adequate)*** | 7 | dose+contra  <<ASSEMBLED>> |
|  82 | 7 Blood and electrolytes | Other drugs for anaemias | **ADEQUATE** | 87 | mech+dose+contra |
|  83 | 7 Blood and electrolytes | Drugs that chelate iron | **ADEQUATE** | 7 | mech+dose+contra |
|  84 | 7 Blood and electrolytes | Drugs for potassium imbalance | **ADEQUATE** | 11 | mech+dose+harm+contra |
|  85 | 7 Blood and electrolytes | Phosphate binders | **THIN *(corpus adequate)*** | 5 | dose+harm  <<ASSEMBLED>> |
|  86 | 7 Blood and electrolytes | Other drugs for electrolyte imbalance | **ADEQUATE** | 28 | mech+dose+harm+contra |
|  87 | 8 Dermatological | Corticosteroids (skin) | **ADEQUATE** | 44 | mech+dose+contra |
|  88 | 8 Dermatological | Tars | **THIN** | 4 | dose |
|  89 | 8 Dermatological | Other drugs for eczema | **ADEQUATE** | 27 | mech+dose+contra |
|  90 | 8 Dermatological | Immunosuppressants (psoriasis) | **ADEQUATE** | 50 | mech+dose+contra |
|  91 | 8 Dermatological | Other drugs for psoriasis | **ADEQUATE** | 10 | dose+harm+contra |
|  92 | 8 Dermatological | Retinoids (skin) | **THIN *(corpus adequate)*** | 12 | dose+harm  <<ASSEMBLED>> |
|  93 | 8 Dermatological | Retinoids (oral) | **THIN *(corpus adequate)*** | 12 | dose+harm  <<ASSEMBLED>> |
|  94 | 8 Dermatological | Other drugs for acne | **THIN** | 5 | dose+contra |
|  95 | 8 Dermatological | Azoles (skin) | **ADEQUATE** | 12 | dose+harm+contra |
|  96 | 8 Dermatological | Other antifungals (skin) | **ADEQUATE** | 6 | dose+harm+contra |
|  97 | 8 Dermatological | Antibacterials (skin) | **THIN** | 14 | dose+contra |
|  98 | 8 Dermatological | Antivirals (skin) | **THIN** | 1 | dose+contra |
|  99 | 8 Dermatological | Scabicides and pediculicides | **ADEQUATE** | 39 | dose+harm+contra |
| 100 | 8 Dermatological | Drugs for warts | **ADEQUATE** | 18 | dose+harm+contra |
| 101 | 8 Dermatological | Drugs for actinic keratoses | **ADEQUATE** | 17 | dose+harm+contra |
| 102 | 8 Dermatological | Drugs for alopecia | **THIN *(corpus adequate)*** | 23 | mech+dose  <<ASSEMBLED>> |
| 103 | 8 Dermatological | Other dermatological drugs | **ABSENT** | 0 | — |
| 104 | 9 Ear, nose and throat | Antibacterials (ear) | **ADEQUATE** | 5 | dose+harm+contra |
| 105 | 9 Ear, nose and throat | Corticosteroids with anti-infectives (ear) | **ADEQUATE** | 4 | dose+harm+contra |
| 106 | 9 Ear, nose and throat | Antiseptics (ear) | **ABSENT** | 0 | — |
| 107 | 9 Ear, nose and throat | Cerumenolytics | **NAMED ONLY** | 2 | — |
| 108 | 9 Ear, nose and throat | Drugs for vestibular disorders | **ADEQUATE** | 12 | dose+harm+contra |
| 109 | 9 Ear, nose and throat | Oral decongestants | **ABSENT** | 0 | — |
| 110 | 9 Ear, nose and throat | Intranasal decongestants | **ABSENT** | 0 | — |
| 111 | 9 Ear, nose and throat | Corticosteroids (intranasal) | **THIN *(corpus adequate)*** | 8 | dose+contra  <<ASSEMBLED>> |
| 112 | 9 Ear, nose and throat | Antihistamines (intranasal) | **ABSENT** | 0 | — |
| 113 | 9 Ear, nose and throat | Other drugs for rhinitis and sinusitis | **THIN** | 4 | dose+contra |
| 114 | 9 Ear, nose and throat | Drugs for other nasal conditions | **ADEQUATE** | 17 | dose+harm+contra |
| 115 | 9 Ear, nose and throat | Drugs for mouth and throat conditions | **THIN *(corpus adequate)*** | 2 | harm+contra  <<ASSEMBLED>> |
| 116 | 10 Endocrine | Sulfonylureas | **ADEQUATE** | 20 | mech+harm+contra |
| 117 | 10 Endocrine | Dipeptidyl peptidase-4 inhibitors | **THIN *(corpus adequate)*** | 4 | mech+contra  <<ASSEMBLED>> |
| 118 | 10 Endocrine | Glucagon-like peptide-1 analogues | **ADEQUATE** | 9 | mech+harm+contra |
| 119 | 10 Endocrine | Sodium-glucose co-transporter 2 inhibitors | **ADEQUATE** | 12 | mech+dose+harm+contra |
| 120 | 10 Endocrine | Other drugs for diabetes | **ADEQUATE** | 170 | mech+dose+harm+contra |
| 121 | 10 Endocrine | Drugs for hypoglycaemia | **ADEQUATE** | 81 | mech+dose+harm+contra |
| 122 | 10 Endocrine | Thyroid hormones | **ADEQUATE** | 17 | dose+harm+contra |
| 123 | 10 Endocrine | Antithyroid drugs | **ADEQUATE** | 17 | mech+dose+harm+contra |
| 124 | 10 Endocrine | Other drugs for thyroid disorders | **ADEQUATE** | 10 | mech+dose+harm+contra |
| 125 | 10 Endocrine | Bisphosphonates | **ADEQUATE** | 29 | dose+harm+contra |
| 126 | 10 Endocrine | Vitamin D | **ADEQUATE** | 78 | dose+harm+contra |
| 127 | 10 Endocrine | Other drugs affecting bone | **ADEQUATE** | 12 | dose+harm+contra |
| 128 | 10 Endocrine | Corticosteroids (adrenal insufficiency) | **ADEQUATE** | 89 | mech+dose+harm+contra |
| 129 | 10 Endocrine | Gonadotrophin-releasing hormone agonists | **ADEQUATE** | 10 | mech+dose+harm |
| 130 | 10 Endocrine | Other drugs for infertility | **ADEQUATE** | 39 | dose+harm+contra |
| 131 | 10 Endocrine | Androgens | **THIN *(corpus adequate)*** | 17 | mech+dose  <<ASSEMBLED>> |
| 132 | 10 Endocrine | Antidiuretic hormone agonists and antagonists | **THIN *(corpus adequate)*** | 19 | mech+harm  <<ASSEMBLED>> |
| 133 | 10 Endocrine | Growth hormone | **THIN** | 4 | mech |
| 134 | 10 Endocrine | Nonselective alpha-blockers | **ABSENT** | 0 | — |
| 135 | 10 Endocrine | Somatostatin analogues | **ADEQUATE** | 7 | mech+dose+harm+contra |
| 136 | 11 Eye | Aminoglycosides (eye) | **ABSENT** | 0 | — |
| 137 | 11 Eye | Quinolones (eye) | **ABSENT** | 0 | — |
| 138 | 11 Eye | Other antibacterials (eye) | **THIN *(corpus adequate)*** | 6 | contra  <<ASSEMBLED>> |
| 139 | 11 Eye | Antivirals (eye) | **ABSENT** | 0 | — |
| 140 | 11 Eye | Beta-blockers (eye) | **THIN *(corpus adequate)*** | 2 | mech+contra  <<ASSEMBLED>> |
| 141 | 11 Eye | Prostaglandin analogues (eye) | **THIN** | 3 | mech+contra |
| 142 | 11 Eye | Alpha2 agonists (eye) | **THIN *(corpus adequate)*** | 4 | mech+contra  <<ASSEMBLED>> |
| 143 | 11 Eye | Carbonic anhydrase inhibitors | **ADEQUATE** | 14 | mech+dose+harm+contra |
| 144 | 11 Eye | Other drugs for glaucoma | **THIN *(corpus adequate)*** | 4 | mech+contra  <<ASSEMBLED>> |
| 145 | 11 Eye | Vasoconstrictors (eye) | **ABSENT** | 0 | — |
| 146 | 11 Eye | Antihistamines (eye) | **THIN** | 1 | contra |
| 147 | 11 Eye | Mast cell stabilisers | **THIN** | 2 | contra |
| 148 | 11 Eye | NSAIDs (eye) | **ABSENT** | 0 | — |
| 149 | 11 Eye | Corticosteroids (eye) | **THIN** | 2 | dose+contra |
| 150 | 11 Eye | Other drugs for allergic eye conditions | **THIN** | 3 | harm+contra |
| 151 | 11 Eye | Drugs for dry eyes | **THIN *(corpus adequate)*** | 17 | dose+harm  <<ASSEMBLED>> |
| 152 | 11 Eye | Anticholinergics (eye) | **NAMED ONLY** | 3 | — |
| 153 | 11 Eye | Other drugs for mydriasis | **ABSENT** | 0 | — |
| 154 | 11 Eye | Local anaesthetics (eye) | **ABSENT** | 0 | — |
| 155 | 12 Gastrointestinal | Antacids | **ADEQUATE** | 7 | mech+harm+contra |
| 156 | 12 Gastrointestinal | H2 antagonists | **ABSENT** | 0 | — |
| 157 | 12 Gastrointestinal | Proton pump inhibitors | **THIN *(corpus adequate)*** | 2 | dose+contra  <<ASSEMBLED>> |
| 158 | 12 Gastrointestinal | Other drugs for ulcers | **THIN *(corpus adequate)*** | 8 | dose+harm  <<ASSEMBLED>> |
| 159 | 12 Gastrointestinal | Drugs affecting gastrointestinal motility | **ADEQUATE** | 22 | dose+harm+contra |
| 160 | 12 Gastrointestinal | Dopamine antagonists (antiemetic) | **ADEQUATE** | 22 | mech+dose+harm |
| 161 | 12 Gastrointestinal | 5HT3 antagonists | **ADEQUATE** | 11 | dose+harm+contra |
| 162 | 12 Gastrointestinal | Substance P antagonists | **THIN** | 2 | harm+contra |
| 163 | 12 Gastrointestinal | Other drugs for nausea and vomiting | **ADEQUATE** | 14 | mech+dose+harm |
| 164 | 12 Gastrointestinal | Stool softeners | **NAMED ONLY** | 1 | — |
| 165 | 12 Gastrointestinal | Stimulant laxatives | **ADEQUATE** | 1 | mech+harm+contra |
| 166 | 12 Gastrointestinal | Osmotic laxatives | **THIN *(corpus adequate)*** | 7 | dose+contra  <<ASSEMBLED>> |
| 167 | 12 Gastrointestinal | Other laxatives | **ABSENT** | 0 | — |
| 168 | 12 Gastrointestinal | Opioid antidiarrhoeals | **THIN *(corpus adequate)*** | 4 | dose+contra  <<ASSEMBLED>> |
| 169 | 12 Gastrointestinal | Other drugs for diarrhoea | **ADEQUATE** | 3 | mech+dose+harm |
| 170 | 12 Gastrointestinal | Corticosteroids (gastrointestinal) | **THIN** | 5 | contra |
| 171 | 12 Gastrointestinal | 5-Aminosalicylates | **ADEQUATE** | 21 | dose+harm+contra |
| 172 | 12 Gastrointestinal | Other drugs for inflammatory bowel disease | **ADEQUATE** | 40 | mech+dose+contra |
| 173 | 12 Gastrointestinal | Drugs for perianal disorders | **THIN** | 25 | contra |
| 174 | 12 Gastrointestinal | Other gastrointestinal drugs | **ADEQUATE** | 9 | dose+harm+contra |
| 175 | 13 Genitourinary | Anticholinergics (genitourinary) | **THIN** | 7 | mech+harm |
| 176 | 13 Genitourinary | Other drugs for urinary incontinence | **THIN** | 2 | mech+harm |
| 177 | 13 Genitourinary | Selective alpha-blockers (genitourinary) | **THIN *(corpus adequate)*** | 2 | harm+contra  <<ASSEMBLED>> |
| 178 | 13 Genitourinary | 5-Alpha-reductase inhibitors | **THIN *(corpus adequate)*** | 3 | mech+dose  <<ASSEMBLED>> |
| 179 | 13 Genitourinary | Phosphodiesterase 5 inhibitors | **ADEQUATE** | 12 | mech+dose+contra |
| 180 | 13 Genitourinary | Other drugs for sexual dysfunction | **THIN *(corpus adequate)*** | 12 | harm+contra  <<ASSEMBLED>> |
| 181 | 13 Genitourinary | Urinary alkalinisers and acidifiers | **ADEQUATE** | 3 | mech+dose+harm+contra |
| 182 | 13 Genitourinary | Drugs for kidney stones | **ABSENT** | 0 | — |
| 183 | 13 Genitourinary | Bladder instillations | **NAMED ONLY** | 1 | — |
| 184 | 14 Immunomodulators and antineoplastics | Alkylating agents | **ADEQUATE** | 12 | mech+dose+contra |
| 185 | 14 Immunomodulators and antineoplastics | Anthracyclines | **THIN** | 2 | harm |
| 186 | 14 Immunomodulators and antineoplastics | Antimetabolites | **ADEQUATE** | 37 | dose+harm+contra |
| 187 | 14 Immunomodulators and antineoplastics | Platinum compounds | **THIN** | 3 | dose |
| 188 | 14 Immunomodulators and antineoplastics | Taxanes | **THIN** | 1 | mech |
| 189 | 14 Immunomodulators and antineoplastics | Topoisomerase I inhibitors | **THIN** | 1 | mech+contra |
| 190 | 14 Immunomodulators and antineoplastics | Vinca alkaloids | **NAMED ONLY** | 1 | — |
| 191 | 14 Immunomodulators and antineoplastics | Other cytotoxic antineoplastics | **NAMED ONLY** | 1 | — |
| 192 | 14 Immunomodulators and antineoplastics | Antineoplastic antibodies | **THIN *(corpus adequate)*** | 14 | mech+contra  <<ASSEMBLED>> |
| 193 | 14 Immunomodulators and antineoplastics | Kinase inhibitors | **THIN** | 5 | mech+harm |
| 194 | 14 Immunomodulators and antineoplastics | Thalidomide analogues | **THIN** | 1 | harm |
| 195 | 14 Immunomodulators and antineoplastics | Other non-cytotoxic antineoplastics | **THIN** | 3 | harm |
| 196 | 14 Immunomodulators and antineoplastics | Anti-androgens | **THIN *(corpus adequate)*** | 10 | dose+harm  <<ASSEMBLED>> |
| 197 | 14 Immunomodulators and antineoplastics | Aromatase inhibitors | **THIN** | 2 | mech |
| 198 | 14 Immunomodulators and antineoplastics | GnRH agonists (oncology) | **THIN** | 1 | mech |
| 199 | 14 Immunomodulators and antineoplastics | Selective oestrogen receptor modulators | **ADEQUATE** | 7 | dose+harm+contra |
| 200 | 14 Immunomodulators and antineoplastics | Other hormonal antineoplastics | **ABSENT** | 0 | — |
| 201 | 14 Immunomodulators and antineoplastics | Colony stimulating factors | **NAMED ONLY** | 3 | — |
| 202 | 14 Immunomodulators and antineoplastics | Other drugs used with antineoplastics | **THIN *(corpus adequate)*** | 3 | harm+contra  <<ASSEMBLED>> |
| 203 | 14 Immunomodulators and antineoplastics | Calcineurin inhibitors | **ADEQUATE** | 36 | mech+dose+harm+contra |
| 204 | 14 Immunomodulators and antineoplastics | Corticosteroids (immunosuppressant) | **ADEQUATE** | 60 | mech+dose+harm+contra |
| 205 | 14 Immunomodulators and antineoplastics | Immunosuppressant antibodies | **THIN** | 1 | mech+harm |
| 206 | 14 Immunomodulators and antineoplastics | mTOR inhibitors | **THIN** | 3 | mech |
| 207 | 14 Immunomodulators and antineoplastics | Other immunosuppressants | **ADEQUATE** | 25 | mech+dose+contra |
| 208 | 14 Immunomodulators and antineoplastics | Interferons | **THIN *(corpus adequate)*** | 5 | dose  <<ASSEMBLED>> |
| 209 | 15 Neurological | Barbiturates | **THIN *(corpus adequate)*** | 8 | dose+harm  <<ASSEMBLED>> |
| 210 | 15 Neurological | Benzodiazepines (neurology) | **ADEQUATE** | 30 | dose+harm+contra |
| 211 | 15 Neurological | Other antiepileptics | **ADEQUATE** | 116 | dose+harm+contra |
| 212 | 15 Neurological | Dopamine agonists (parkinsonism) | **ADEQUATE** | 15 | mech+dose+harm+contra |
| 213 | 15 Neurological | Anticholinergics (parkinsonism) | **THIN** | 2 | dose |
| 214 | 15 Neurological | Monoamine oxidase type B inhibitors | **ADEQUATE** | 5 | mech+dose+contra |
| 215 | 15 Neurological | Other drugs for Parkinson's disease | **ADEQUATE** | 20 | mech+dose+harm |
| 216 | 15 Neurological | Triptans | **ADEQUATE** | 10 | dose+harm+contra |
| 217 | 15 Neurological | Calcitonin gene-related peptide antagonists | **ABSENT** | 0 | — |
| 218 | 15 Neurological | Other drugs to prevent migraine | **ADEQUATE** | 4 | dose+harm+contra |
| 219 | 15 Neurological | Anticholinesterases in Alzheimer's disease | **ADEQUATE** | 13 | mech+harm+contra |
| 220 | 15 Neurological | Other drugs for Alzheimer's disease | **THIN** | 4 | mech+contra |
| 221 | 15 Neurological | Drugs for multiple sclerosis | **ADEQUATE** | 11 | mech+dose+contra |
| 222 | 15 Neurological | Anticholinesterases in myasthenia gravis | **THIN** | 2 | dose+contra |
| 223 | 15 Neurological | Drugs for other neurological conditions | **THIN *(corpus adequate)*** | 19 | mech+harm  <<ASSEMBLED>> |
| 224 | 16 Obstetric and gynaecological | Combined oral contraceptives | **ADEQUATE** | 45 | mech+dose+contra |
| 225 | 16 Obstetric and gynaecological | Progestogens | **THIN *(corpus adequate)*** | 27 | harm+contra  <<ASSEMBLED>> |
| 226 | 16 Obstetric and gynaecological | Other combined contraceptives | **THIN** | 2 | mech |
| 227 | 16 Obstetric and gynaecological | Intrauterine devices | **THIN *(corpus adequate)*** | 20 | harm+contra  <<ASSEMBLED>> |
| 228 | 16 Obstetric and gynaecological | Hormone replacement therapy | **ADEQUATE** | 26 | mech+dose+contra |
| 229 | 16 Obstetric and gynaecological | Drugs for heavy menstrual bleeding | **ADEQUATE** | 8 | dose+harm+contra |
| 230 | 16 Obstetric and gynaecological | Drugs for endometriosis | **THIN** | 16 | contra |
| 231 | 16 Obstetric and gynaecological | Drugs for preterm labour | **THIN** | 2 | dose+contra |
| 232 | 16 Obstetric and gynaecological | Drugs in pre-eclampsia and eclampsia | **ADEQUATE** | 25 | mech+dose+harm+contra |
| 233 | 16 Obstetric and gynaecological | Oxytocic drugs | **THIN *(corpus adequate)*** | 17 | dose+harm  <<ASSEMBLED>> |
| 234 | 16 Obstetric and gynaecological | Prostaglandins | **THIN *(corpus adequate)*** | 16 | dose+harm  <<ASSEMBLED>> |
| 235 | 16 Obstetric and gynaecological | Other drugs used in obstetrics | **ADEQUATE** | 84 | mech+dose+harm+contra |
| 236 | 16 Obstetric and gynaecological | Drugs affecting lactation | **ADEQUATE** | 10 | mech+dose+harm+contra |
| 237 | 16 Obstetric and gynaecological | Azoles (vaginal) | **THIN** | 2 | dose+contra |
| 238 | 16 Obstetric and gynaecological | Other vaginal anti-infectives | **ABSENT** | 0 | — |
| 239 | 16 Obstetric and gynaecological | Drugs for menstrual symptoms | **ADEQUATE** | 10 | dose+harm+contra |
| 240 | 17 Psychotropic | Monoamine oxidase inhibitors | **ADEQUATE** | 3 | mech+dose+harm |
| 241 | 17 Psychotropic | Selective serotonin reuptake inhibitors | **ADEQUATE** | 45 | mech+dose+harm |
| 242 | 17 Psychotropic | Tricyclic antidepressants | **ADEQUATE** | 26 | dose+harm+contra |
| 243 | 17 Psychotropic | Serotonin and noradrenaline reuptake inhibitors | **ADEQUATE** | 14 | mech+dose+harm |
| 244 | 17 Psychotropic | Other antidepressants | **THIN** | 5 | harm+contra |
| 245 | 17 Psychotropic | Antipsychotics | **ADEQUATE** | 86 | mech+dose+harm |
| 246 | 17 Psychotropic | Drugs for bipolar disorder | **ADEQUATE** | 30 | dose+harm+contra |
| 247 | 17 Psychotropic | Benzodiazepines | **ADEQUATE** | 56 | mech+dose+contra |
| 248 | 17 Psychotropic | Non-amphetamine psychostimulants | **ABSENT** | 0 | — |
| 249 | 17 Psychotropic | Orexin receptor antagonists | **ABSENT** | 0 | — |
| 250 | 17 Psychotropic | Other drugs for anxiety and sleep disorders | **THIN** | 4 | contra |
| 251 | 17 Psychotropic | Psychostimulants | **ADEQUATE** | 4 | dose+harm+contra |
| 252 | 17 Psychotropic | Other drugs for attention deficit hyperactivity disorder | **ADEQUATE** | 1 | dose+harm+contra |
| 253 | 17 Psychotropic | Drugs for alcohol dependence | **ADEQUATE** | 5 | mech+harm+contra |
| 254 | 17 Psychotropic | Drugs for nicotine dependence | **THIN** | 7 | contra |
| 255 | 17 Psychotropic | Drugs for opioid dependence | **ADEQUATE** | 7 | mech+dose+harm+contra |
| 256 | 17 Psychotropic | Other psychotropic drugs | **ADEQUATE** | 24 | dose+harm+contra |
| 257 | 18 Respiratory | Beta2 agonists | **ADEQUATE** | 69 | mech+dose+harm+contra |
| 258 | 18 Respiratory | Anticholinergics (inhaled) | **THIN *(corpus adequate)*** | 20 | mech+dose  <<ASSEMBLED>> |
| 259 | 18 Respiratory | Theophyllines | **THIN *(corpus adequate)*** | 5 | mech+dose  <<ASSEMBLED>> |
| 260 | 18 Respiratory | Corticosteroids (inhaled) | **THIN *(corpus adequate)*** | 48 | dose+contra  <<ASSEMBLED>> |
| 261 | 18 Respiratory | Other drugs for asthma | **THIN** | 2 | mech+harm |
| 262 | 18 Respiratory | Opioid cough suppressants | **ABSENT** | 0 | — |
| 263 | 18 Respiratory | Mucolytics | **ADEQUATE** | 5 | mech+dose+contra |
| 264 | 18 Respiratory | Drugs used in cystic fibrosis | **NAMED ONLY** | 17 | — |
| 265 | 18 Respiratory | Pulmonary surfactants | **NAMED ONLY** | 2 | — |
| 266 | 18 Respiratory | Other respiratory drugs | **NAMED ONLY** | 2 | — |
| 267 | 19 Rheumatological | TNF-alpha antagonists | **THIN *(corpus adequate)*** | 21 | mech+dose  <<ASSEMBLED>> |
| 268 | 19 Rheumatological | Immunosuppressants (rheumatology) | **ADEQUATE** | 65 | mech+dose+contra |
| 269 | 19 Rheumatological | Other immunomodulating drugs | **THIN *(corpus adequate)*** | 11 | dose+contra  <<ASSEMBLED>> |
| 270 | 19 Rheumatological | Xanthine oxidase inhibitors | **ADEQUATE** | 15 | mech+dose+contra |
| 271 | 19 Rheumatological | Other drugs for gout | **ADEQUATE** | 10 | mech+dose+harm+contra |
| 272 | 19 Rheumatological | NSAIDs | **ADEQUATE** | 98 | mech+dose+harm+contra |
| 273 | 20 Vaccines | Vaccines | **ADEQUATE** | 214 | mech+dose+harm+contra |
| 274 | 21 Miscellaneous | Specialised drugs | **THIN *(corpus adequate)*** | 6 | dose+contra  <<ASSEMBLED>> |
| 275 | 21 Miscellaneous | Blood products | **ADEQUATE** | 36 | dose+harm+contra |
| 276 | 21 Miscellaneous | Immunoglobulins | **ADEQUATE** | 86 | dose+harm+contra |

## Phase 5 Part A — 2,585 conditions against an external list

**Enumeration source:** a ~2,585-condition list supplied by the user, ordered in organ-system blocks and transcribed verbatim into `data/conditions_01..19_*.txt`. This is the enumeration Part A was blocked on for three passes. `data/checklist_external.csv` — declined twice before, because building it from recall would have made a fabricated baseline permanent — now exists and holds a verdict for every one of the 2,585.

**Teach-vs-mention lens.** Four verdicts, from structure rather than keyword density: **OWNS ENTRY** (names a `##`/`###` header), **IN A TAUGHT SECTION** (named inside a section carrying >=2 of the corpus's D:/R:/S-Smx:/Ix:/Mx: markers), **MENTIONED** (prose only), **ABSENT**.

| System | n | owns | in a taught entry | prose only | absent | genuine gaps |
|---|---|---|---|---|---|---|
| Cardiovascular | 170 | 49 | 60 | 13 | 44 | **4** |
| Neurology | 222 | 72 | 49 | 22 | 73 | **6** |
| Dermatology | 129 | 43 | 28 | 13 | 42 | **3** |
| Endocrine and Metabolic | 162 | 57 | 43 | 10 | 48 | **4** |
| Genitourinary and Reproductive | 135 | 37 | 37 | 7 | 52 | **2** |
| Gastroenterology | 200 | 59 | 50 | 17 | 71 | **3** |
| Haematology, Genetics and Oncology | 281 | 94 | 61 | 24 | 102 | **0** |
| Immunology and Allergy | 31 | 14 | 6 | 3 | 8 | **0** |
| Toxicology, Environmental and Trauma | 108 | 17 | 19 | 21 | 45 | **6** |
| Psychiatry | 113 | 43 | 18 | 10 | 36 | **6** |
| Rheumatology and Musculoskeletal | 257 | 75 | 32 | 18 | 127 | **5** |
| Systemic and Miscellaneous | 53 | 18 | 18 | 2 | 15 | **0** |
| Obstetrics | 57 | 23 | 11 | 5 | 18 | **0** |
| Geriatrics and Safeguarding | 13 | 3 | 4 | 2 | 4 | **0** |
| Paediatrics and Neonatal | 31 | 10 | 8 | 1 | 12 | **0** |
| Renal and Urology | 93 | 26 | 30 | 7 | 29 | **1** |
| Respiratory | 99 | 32 | 23 | 7 | 36 | **1** |
| ENT and Ophthalmology | 219 | 60 | 53 | 13 | 91 | **2** |
| Infectious Disease | 212 | 72 | 48 | 20 | 70 | **2** |
| **TOTAL** | **2585** | **804** | **598** | **215** | **923** | **45** |

### Thirteen naming conventions the supplied list does not share with the corpus

The first cardiovascular run reported 77 of 170 conditions ABSENT. Almost none were. Each convention below was found by disbelieving a plausible-looking count, never by foresight, and each would have silently inflated the absence rate across all nineteen systems:

1. **US vs Australian spelling** — ischemia/ischaemia, edema/oedema, tumor/tumour. 2. **Acronyms** — LBBB, HFrEF, WPW; now derived mechanically from the condition's own words. 3. **Plurals.** 4. **Interposed words** — "coarctation of **the** aorta", 22 uses. 5. **Possessives** — Eisenmenger**'s**. 6. **A fix that created its own failure** — an `-es` stripper turned `valves` into `valv`, unable to match `valve`. 7. **Ordinals** — "Second Degree" vs "2nd degree"; all three AV blocks read ABSENT against a section teaching all three. 8. **Internal hyphenation** — `post-herpetic`; fixed generally by collapsing both sides to letters-only. 9. **Diacritics** — Brown-Sequard, which does not merely appear but **owns an entry**. 10. **-ies plurals** — `radiculopathies`. 11. **Dropped qualifiers — NOT FIXED**; "Lambert-Eaton **myasthenic** syndrome" cannot match "Lambert-Eaton syndrome" without matching almost anything. 12. **-ies that is not a plural** — `scabies` stemmed to `scaby` and read ABSENT in a corpus that prescribes permethrin for it. 13. **Spelling folding is substring surgery and cannot be made safe** — `gastroesophageal` contains `oesophag` and folded to `gastresophageal`, so GORD read ABSENT under two successive fixes. Resolved by giving up on one canonical form: every condition is now tried against three normalisations plus a letters-only collapse, and a hit in any counts.

> [!danger] **The teach-vs-mention lens was dead for the entire first full run, and that is the most serious defect in this phase.**
> `MARKER` required the literal `**` of the corpus's bold markers, but `load()` strips markdown *before* splitting into sections. It therefore matched **nothing, in all 148 files**. The IN A TAUGHT SECTION verdict could never fire; every condition sitting inside a real teaching entry was silently demoted to MENTIONED, while the scan reported confident-looking counts. **Cardiovascular and Neurology were reported to the user under it.**
> It was caught only because a summary table showed a column of nineteen zeroes. ABSENT and OWNS ENTRY were unaffected, so no gap was missed — what was lost was the entire ability to tell teaching from passing mention, which is the distinction the scan exists to draw. 598 conditions now hold that verdict.

> [!warning] **Two further defects of my own, recorded because they were nearly shipped.**
> **The scan went quadratic and timed out** at two systems, recomputing collapsed forms per condition per section; an earlier phase abandoned a matcher for exactly this rather than shipping it. **The CSV had no idempotence guard** — a stale background run landed after a foreground re-run and neurology silently carried 444 rows for 222 conditions, with nothing in the file to show it.

### Six systems returned zero gaps, and that was treated as a signal

Haematology/Genetics/Oncology, Immunology, Systemic, Obstetrics, Geriatrics and Paediatrics produced no gaps. A clean result from a method that has failed three times is not evidence of a clean corpus, so each was re-attacked by hand-grepping its absent list for aliases. **Two of them were not clean at all** — Endocrine and Genitourinary had been in this group, and hand-grepping found six gaps between them including the phosphate finding below. The remaining six survive the check: their absences are single-gene disorders, dysmorphology syndromes and non-endemic infections, and the intern-relevant candidates (wound dehiscence, G6PD, haemochromatosis, protein C/S, HIT, anti-D, IUGR, miscarriage, NEC, supracondylar fracture) are all present under Australian names.

### The pattern the gaps share

Most are not missing topics. They are **the unnamed half of a set the corpus otherwise teaches** — the same shape as the bulk-forming laxative and the incomplete cord syndromes:

- **Serum phosphate has no entry at all**, in a corpus that teaches hyper- and hypo- natraemia, kalaemia and calcaemia and hypomagnesaemia. Refeeding syndrome, where an intern meets it, has two passing mentions and no entry. **Hypermagnesaemia** is absent while hypomagnesaemia has 13 uses.
- **Central and posterior cord syndrome** absent while Brown-Sequard owns an entry.
- **Epispadias** absent while hypospadias is covered.
- **Concussion appears zero times** against 28 uses of "head injury".
- **Erectile dysfunction covered, premature ejaculation absent.**

### An independent confirmation worth recording

The external list rediscovered **posterior urethral valves** — a gap the earlier corpus-first pass found and queued as **P5-A1**. Two methods with no shared machinery reached the same finding. That is the only evidence so far that this phase's method detects real gaps rather than artefacts of its own construction.

### Honesty about what was NOT individually verified

929 conditions came back ABSENT. **45 gap rows and 85 covered-by-synonym rows were hand-grepped**, with hit counts recorded in the CSV. The remaining **788 are classified out-of-scope by rule, not by individual verification** — named fracture patterns and eponyms, tumour subtypes, congenital dysmorphology, non-endemic tropical infection, single-gene disorders. That rule is a judgement applied at scale and it will be wrong somewhere. It is recorded as a rule so a later round can attack the rule rather than re-derive 788 decisions. The 215 MENTIONED rows were also not individually read.

### Genuine intern-level gaps by system

**Cardiovascular** — Coronary Vasospasm · Multifocal Atrial Tachycardia · Peripartum Cardiomyopathy · Pseudoaneurysm

**Neurology** — Central Cord Syndrome · Cerebellar infarction · Neurologically Determined Death · Parasomnias · Post-concussive syndrome · Posterior Cord Syndrome

**Dermatology** — Diaper Rash · Felon · Paronychia

**Endocrine and Metabolic** — Alcoholic Ketoacidosis · Hypermagnesemia · Hyperphosphatemia · Hypophosphatemia

**Genitourinary and Reproductive** — Epispadias · Premature Ejaculation

**Gastroenterology** — Gilbert's Syndrome · Intra-abdominal abscess · Pancreatic pseudocyst

**Toxicology, Environmental and Trauma** — Benzodiazepine overdose · Concussion · Facial Fractures · Heat Exhaustion · Heat Stroke · TCA Overdose

**Psychiatry** — Adjustment Disorder · Delusional Disorder · Gender Dysphoria · Night Terrors · Sleepwalking · Somnambulism

**Rheumatology and Musculoskeletal** — Baker's cyst · Bunions · Hallux valgus · Mallet Finger · Popliteal cyst

**Renal and Urology** — Posterior Urethral Valves

**Respiratory** — Solitary pulmonary nodule

**ENT and Ophthalmology** — Keratoconus · Retropharyngeal abscess

**Infectious Disease** — Herpetic Whitlow · Lymphangitis

## Phase 5 Part A — matcher corrected, all 19 systems re-run

Three defects were found by hand-verifying the MSK/Rheum fracture eponyms, and **two of them manufactured coverage rather than absence** — the dangerous direction, and the first defects in this phase to do so.

| # | Defect | Effect |
|---|---|---|
| 14 | **Possessive splitting.** `"Boxer's fracture"` tokenised to `[boxer, s, fracture]` and demanded an apostrophe the corpus omits | `### Boxer fracture`, a section the corpus owns, read ABSENT. Invisible whenever *both* sides use the possessive (Smith's, Colles'), which is why twelve earlier conventions never surfaced it |
| 15 | **Generated-acronym collision.** `"Clay-shoveler fracture"` produced `CSF` | Matched `04_Neurology#CSF Interpretation` 78 times and scored **OWNS ENTRY** for a fracture the corpus has never mentioned. The generator also emits DVT, TIA, MCL, AKI, CKD, SAH, ARDS |
| 16 | **Different final word or stem derivation** — found by the canary test, not by an absence count | `## Achilles tendon` vs "Achilles tendon **rupture**"; `### Acromioclavicular joint **injury**` vs "…**pathology**"; `Dermatophyt**e** infections` vs "Dermatophyt**oses**" |

**A fix that over-corrected, caught in the diff rather than shipped.** Requiring four source words for a generated acronym also destroyed the legitimate three-word ones: *Gestational Diabetes Mellitus* and *Sexually Transmitted Infections* both came back ABSENT, and both are plainly taught. Suppressing a true positive to kill a false one is not a fix — it moves the error into the direction that merely looks safer. The floor is back at three words; the real safeguard is that a generated acronym can now **only** produce the new `ACRONYM MATCH ONLY` verdict, never coverage.

**Validation before the re-run** (`scripts/test_condition_scan.py`, 14/14). Regression cases are the three that exposed the defects. Canary cases come from *other* systems with *other* conventions — paediatric eponyms, dermatology `-oses` pluralisation, obstetric US/AU spelling — because a matcher proven only on the pattern that last broke it is not proven. The canary caught defect 16, which neither known bug explained. First run 11/14, second 13/14, third 14/14. An over-match probe then confirmed four newly-covered single-token conditions are genuinely present rather than manufactured.

### Effect on previously reported verdicts

**79 covered verdicts across 16 of 19 systems were revised downward** — 75 to `ACRONYM MATCH ONLY` (flagged, unresolved) and 4 to ABSENT. **23 absences were revised upward** to covered, 9 in MSK/Rheum alone. No system was unaffected in both directions; only Immunology, Geriatrics and Paediatrics were untouched.

| System | n | owns | in a taught entry | prose | acronym-only (flagged) | absent |
|---|---|---|---|---|---|---|
| Cardiovascular | 170 | 49 | 49 | 15 | 10 | 47 |
| Neurology | 222 | 70 | 45 | 21 | 6 | 80 |
| Dermatology | 129 | 43 | 26 | 13 | 3 | 44 |
| Endocrine and Metabolic | 162 | 56 | 40 | 12 | 2 | 52 |
| Genitourinary and Reproductive | 135 | 35 | 36 | 6 | 6 | 52 |
| Gastroenterology | 200 | 60 | 45 | 19 | 5 | 71 |
| Haematology, Genetics and Oncology | 281 | 98 | 52 | 26 | 5 | 100 |
| Immunology and Allergy | 31 | 13 | 7 | 3 | 0 | 8 |
| Toxicology, Environmental and Trauma | 108 | 18 | 17 | 19 | 4 | 50 |
| Psychiatry | 113 | 42 | 13 | 13 | 4 | 41 |
| Rheumatology and Musculoskeletal | 257 | 77 | 35 | 18 | 3 | 124 |
| Systemic and Miscellaneous | 53 | 18 | 14 | 4 | 1 | 16 |
| Obstetrics | 57 | 23 | 10 | 4 | 2 | 18 |
| Geriatrics and Safeguarding | 13 | 3 | 4 | 2 | 0 | 4 |
| Paediatrics and Neonatal | 31 | 11 | 7 | 1 | 0 | 12 |
| Renal and Urology | 93 | 24 | 26 | 6 | 7 | 30 |
| Respiratory | 99 | 31 | 20 | 8 | 3 | 37 |
| ENT and Ophthalmology | 219 | 57 | 48 | 14 | 8 | 92 |
| Infectious Disease | 212 | 76 | 39 | 20 | 6 | 71 |
| **TOTAL** | **2585** | **804** | **533** | **224** | **75** | **949** |

> [!warning] **The 75 acronym-only rows are the honest residue.** Each matched the corpus only through a generated initialism. Some are real (GDM, STI, FSGS, MGUS, LBBB — the corpus does use those acronyms); some are collisions. The scan cannot tell which, so it says so instead of guessing in either direction. They are neither counted as coverage nor reported as gaps, and they are the targeted follow-up list.

> [!danger] **The build items from this phase cannot be built in this environment.** The project requires a cited Australian source per topic; egress is blocked for `rch.org.au`, `amc.org.au`, `racgp.org.au`, `tg.org.au` and every other primary source tested this session. Writing thirty clinical entries from recall and citing documents that were never read would put unverified dosing and thresholds into the corpus permanently — the same failure the project already refused when it declined to build `checklist_external.csv` from recall. The gaps stay queued with their named sources.

## Phase 5 Part A — final: acronym corroboration

**Defect 17, and the first in this phase that hid gaps rather than inventing them.** A generated acronym could never produce coverage — it only ever yielded `ACRONYM MATCH ONLY`. But it could lift a genuinely ABSENT condition out of the gap list and bury it among the flagged. A 24-entry blocklist was the wrong instrument and missed nearly everything:

| Acronym | Corpus hits | Generated from | What the corpus actually means |
|---|---|---|---|
| `GAP` | 314 | Gastric adenomatous polyp | the ordinary English word |
| `OFF` | 85 | Orbital Floor Fracture | the ordinary English word |
| `MEN` | 51 | Middle ear neoplasm | "men", and MEN 1/2 |
| `ACS` | 40 | **Anterior Cord Syndrome** | acute coronary syndrome |
| `BMI` `PAD` `SCC` `ADH` `ALS` `PET` `ABC` | 9–36 | various | body mass index, PAD, squamous cell carcinoma, ADH, ALS, PET scan, the ABC mnemonic |

**Anterior cord syndrome is the proof the defect mattered.** Central and posterior cord syndrome were already queued as gaps; the anterior one was equally absent and sat hidden behind the ACS collision for the whole phase.

**The fix is corroboration, not a longer blocklist.** A generated acronym now counts only if a distinctive ≥9-character word from the condition's own name appears in the same section. `STI` beside "transmitted" is the corpus meaning it; `GAP` with no "adenomatous" near it is not. **65 collisions rejected across 16 of 19 systems; 10 corroborated matches remain flagged.**

Two gaps recovered from the flagged pile and queued: **anterior cord syndrome** and **orbital floor (blow-out) fracture**. One condition moved the other way by hand: **gestational diabetes is covered**, taught as `### Diabetes in pregnancy` (`16_01-05:430`) with the 28-week 75g OGTT criteria — a rename no matcher reaches, and a reminder that convention 11 stays unfixable.

| System | n | owns | in a taught entry | prose | flagged | absent | gaps |
|---|---|---|---|---|---|---|---|
| Cardiovascular | 170 | 49 | 49 | 15 | 1 | 56 | **4** |
| Neurology | 222 | 70 | 45 | 21 | 0 | 86 | **7** |
| Dermatology | 129 | 43 | 26 | 13 | 1 | 46 | **3** |
| Endocrine and Metabolic | 162 | 56 | 40 | 12 | 0 | 54 | **4** |
| Genitourinary and Reproductive | 135 | 35 | 36 | 6 | 2 | 56 | **2** |
| Gastroenterology | 200 | 60 | 45 | 19 | 0 | 76 | **3** |
| Haematology, Genetics and Oncology | 281 | 98 | 52 | 26 | 4 | 101 | **0** |
| Immunology and Allergy | 31 | 13 | 7 | 3 | 0 | 8 | **0** |
| Toxicology, Environmental and Trauma | 108 | 18 | 17 | 19 | 0 | 54 | **7** |
| Psychiatry | 113 | 42 | 13 | 13 | 0 | 45 | **6** |
| Rheumatology and Musculoskeletal | 257 | 77 | 35 | 18 | 0 | 127 | **11** |
| Systemic and Miscellaneous | 53 | 18 | 14 | 4 | 0 | 17 | **0** |
| Obstetrics | 57 | 23 | 10 | 4 | 0 | 20 | **0** |
| Geriatrics and Safeguarding | 13 | 3 | 4 | 2 | 0 | 4 | **0** |
| Paediatrics and Neonatal | 31 | 11 | 7 | 1 | 0 | 12 | **0** |
| Renal and Urology | 93 | 24 | 26 | 6 | 1 | 36 | **1** |
| Respiratory | 99 | 31 | 20 | 8 | 0 | 40 | **1** |
| ENT and Ophthalmology | 219 | 57 | 48 | 14 | 0 | 100 | **2** |
| Infectious Disease | 212 | 76 | 39 | 20 | 1 | 76 | **2** |
| **TOTAL** | **2585** | **804** | **533** | **224** | **10** | **1014** | **53** |

The absence count rose from 949 to 1,014 across the corrected runs. That is the honest direction: every correction this phase made moved conditions **out** of false coverage, and the earlier, lower absence counts were the artefact.

## Phase 5 — Source 3 cross-check (presentation-based lens)

**Enumeration source:** an AMC-style exam-prep document grouping conditions by **clinical presentation** rather than organ system — 94 sub-items across 7 groupings (emergency medicine, sepsis phenotypes, shock phenotypes, respiratory failure, acid-base, electrolytes/dehydration, toxicological and allergic emergencies). Saved as `data/conditions_20_presentation_based.txt`.

**Result: 33 own an entry · 10 in a taught section · 7 prose · 44 absent by scan → 6 genuine gaps after hand-verification.**

The premise held. A presentation-based lens does surface things an organ-system list misses — but not the ones predicted, and the biggest finding was not on the flagged list at all.

### The finding that matters: Australian envenomation is absent in a stronger sense than previously recorded

P5-C10 already recorded antivenoms as absent. This pass shows the gap is **wider than antivenom**:

| Search | Hits |
|---|---|
| `snakebite` / `snake bite` | **0** |
| `redback` / `funnel-web` | **0** |
| **`pressure immobilisation`** | **0** |
| `antivenom` / `envenom` | 3 — **and all three are incidental** |

The three hits are a build-queue note in a workflow document, a "Gap-filled from CSV" annotation about *burns*, and a serum-sickness aside in dermatology. **No clinical content on envenomation exists anywhere in 148 files.**

**Pressure immobilisation bandaging is the single highest-yield Australian first-aid intervention in this domain and has zero mentions.** For an Australian intern corpus that is the most consequential absence found in Phase 5 so far. P5-C10 is upgraded accordingly.

### The user's four flagged "between-category" predictions — three were already covered

Checked exactly as specified:

- **Toxic Shock Syndrome** — present (4 uses). Thin but not absent.
- **Adrenal (Addisonian) crisis as a shock phenotype** — present in `06_Metabolic` including the danger box on carrying injectable hydrocortisone. Covered as a crisis, not only as Addison's disease.
- **Neuromuscular respiratory failure** — **partially covered, and the unifying concept is the gap.** FVC appears 29 times and myasthenic crisis 6, but `vital capacity` never appears near GBS or myasthenia: the corpus has the measurement and the diseases and does not connect them. Logged as thin, not absent.
- **Australian envenomation** — confirmed absent, and worse than recorded (above).

Three of four predictions were already covered. Consistent with this session's pattern: a predicted gap is not a gap until checked.

### Genuine gaps this lens surfaced that Part A did not

1. **Envenomation, including pressure immobilisation** — see above.
2. **Toxidromes as a diagnostic framework.** "Toxidrome" appears 4 times, only for opioid and serotonin/NMS. **Anticholinergic toxidrome: 0. Cholinergic/organophosphate: 1. Sympathomimetic: 6, almost all in cardiovascular drug contexts.** The corpus teaches two toxidromes and neither the framework nor the other three.
3. **Organophosphate poisoning** — 1 use, pralidoxime 1 use. Rural and agricultural Australian relevance.
4. **Beta-blocker and calcium-channel-blocker overdose** — 1 use, and **high-dose insulin euglycaemic therapy and glucagon-for-overdose: 0 hits.** The specific antidote strategy is absent.
5. **Fascia iliaca block** — 0 hits, in a corpus that covers neck-of-femur fracture. An intern-performed analgesic block.
6. **Type 2 (hypercapnic) respiratory failure** — 2 hits. Thin against 29 for respiratory failure generally.

### Explicitly out of scope, recorded not folded in

**"Zero-Context methodology" and "Distractor Elimination Rules" are MCQ exam technique, not clinical content**, and are not counted as corpus gaps. Noted as a candidate **future project — an exam-strategy reference file**, separate from Phase 5.

## Phase 5 Part E — investigations and special tests (a gap in the METHOD, not just the corpus)

> [!danger] **Phase 5 enumerated conditions, scales, drugs and procedures — and never investigations.** That is a hole in the method itself, not a corpus finding. Four axes were checked exhaustively and a fifth was never named. It is recorded here as a method limitation because the same omission could hide other axes (anatomy? emergency algorithms? communication scenarios?).

**Enumeration source:** an investigations/special-tests list, 263 items, saved as `data/conditions_21_investigations.txt`.

**Result: 20 own an entry · 95 in a taught section · 16 prose · 4 acronym-only · 128 absent by scan.** Hand-verification collapses that 128 dramatically — **most are abbreviation variants, not gaps.**

### The laboratory list is almost entirely covered, under abbreviations

The scan's ABSENT list is dominated by spelled-out names the corpus writes as acronyms. Verified by hand: LFTs **67** uses · B12 **71** · IGRA/Quantiferon **65** · chlamydia **55** · PTH **47** · phosphate **23** · magnesium **23** · urine ACR **22** · C. difficile **15** · LDH **13** · G6PD **13** · CTG **9** · VBG **8** · Coombs/antiglobulin **7** · IGF-1 **7** · renin **7** · Kleihauer **6** · V/Q **5**. None of these is a gap.

**Genuinely thin or absent in the laboratory group (4):**

| Test | Hits | Why it matters |
|---|---|---|
| **Nitrazine / ferning / fetal fibronectin** | **0** | The tests that confirm **prelabour rupture of membranes** — a condition the corpus teaches. The diagnosis without its diagnostic test |
| Fractional excretion of sodium (FeNa) | 1 | Pre-renal vs ATN in AKI, both taught |
| Plasma metanephrines | 1 | Phaeochromocytoma is taught |
| Serum protein electrophoresis | 2 | Myeloma is taught |

### The physical special tests are the real gap, and they cluster

This is where a test-based lens finds what a condition-based lens cannot.

**Adequate — technique and interpretation both given (4):** Simmonds-Thompson calf-squeeze (`11_05:110`) · Schober's (`12_02:13`) · Trendelenburg (`Examination.md:642`, own section) · Adam's forward bend (`Examination.md:628`, own section).

**Named only — the test is cited as positive/negative with no technique and no interpretation (4):** **Lachman's** and **anterior drawer** (a single table cell, "positive anterior drawer & Lachman's test") · **femoral stretch** (one row of a dermatome table) · **Finkelstein's** ("teapot test positive", no method).

**Absent entirely (9):** **straight leg raise** · **McMurray's** · posterior drawer · pivot shift · **FABER/Patrick's** · **Spurling's** · cervical distraction · grind test · TLICS.

> [!warning] **Two of those absences are the asymmetric-silence pattern again, and they are the highest-yield findings of this pass.**
> - **Straight leg raise: zero hits**, in a corpus that teaches sciatica, lumbar radiculopathy and cauda equina. The condition is taught; the bedside test that identifies it is not written down anywhere.
> - **McMurray's: zero hits**, in a corpus whose knee file opens with "Knee — ligament and meniscal injuries". Same shape.
>
> Both are tests an intern is expected to perform and describe in an OSCE.

**A false positive worth recording:** "distraction test" returns one hit, but it is **paediatric audiology distraction testing** in `13_03_ENT` — a completely different procedure. The cervical distraction test is absent.

### Confirming the Simmonds-Thompson premise

Checked with `git log -S`: the Simmonds-Thompson description traces to the **initial upload commit**, not to any commit from this session. It is **original corpus content that the earlier eponym check found**, not content this session built. Re-flagging it as absent would have been wrong, and it is correctly scored ADEQUATE here.

---

## Corpus-wide adult-vs-paediatric sweep (2026-08-30)

The first sweep of its kind run across **all 209 `.md` files** rather than one round's
working set. It exists because the preceding integrity pass over the bulk-build files was
**purely structural** — tables present, callouts present, links resolve, headers unique —
and none of those checks looks at the content of a number. That pass reported the build
clean while adult doses sat unmarked in paediatric entries.

### Method

Every numeric quantity in the corpus was extracted and classified by whether its
denominator makes it a **lab value or rate** (`/L`, `/min`, `/1.73m²`), a **correct
paediatric form** (`/kg`, `/m²`), or an **absolute quantity**. Absolutes were then tested
for paediatric context at three widening scopes:

1. **Line scope** — paediatric words on the same line. 20 lines.
2. **Section scope** — paediatric words within ±8 lines or in the enclosing heading. 83
   lines, of which most were obstetric text where "baby" sits near a dose given to the
   *mother*.
3. **Widened vocabulary** — terms the first regex could not match (`paeds`, `juvenile`,
   `congenital`, `puberty`, `boys`, `girls`, `RCH`, `under 5`, `aged N`). Surfaced **8
   further lines the first two scopes missed**, two of which were genuine.

**Totals: 853 quantity matches; 542 absolute; 111 lines reviewed by hand; 11 genuine
findings; 100 dismissed with reason.**

### Why the third scope matters

The narrow regex would have reported the corpus clean at 9 findings. Widening the
*vocabulary of paediatric context* — not the quantity pattern — found two more. **A scan's
blind spot is usually in the half of the query nobody is looking at**: the quantity pattern
was tuned carefully and the context pattern was written once and trusted.

### The eleven findings

| File | Defect | Kind |
|---|---|---|
| `15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md` | IO insertion "lidocaine 1% 5mL" — 50mg absolute, in the newborn life support file | dose, high |
| `NEW_Drugs_10_Endocrine.md` | hydrocortisone 100mg induction / 200mg per 24h, bare absolutes | dose, high |
| `08_09_Infectious_Disease_-_Miscellaneous.md` (bites) | adult doses **and adult drug choices** — doxycycline, ciprofloxacin | drug choice |
| `08_09_Infectious_Disease_-_Miscellaneous.md` (post-splenectomy) | adult prophylaxis doses in an entry that extends the regimen to children | dose |
| `02_Respiratory.md` | reversibility stated as "≥12% **or** ≥200 mL" where another file said **and** | logic + adult absolute |
| `07_Renal_Medicine_and_Urology.md` | adult >3.5 g/day nephrotic threshold, in a table naming children | threshold |
| `10_08_Haemonc_-_Blood_Products_and_Transfusion.md` | "one unit raises Hb by 10 g/L" — an adult rule of thumb, not a dose | rule of thumb |
| `09_01_Dermatology_-_Dermatological_Emergencies.md` | adult aciclovir for eczema herpeticum, a disease of children | dose |
| `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA.md` | adult 10–20g oral carbohydrate in the paediatric entry | dose, low |
| `NEW_Investigations_Endocrine.md` + `06_Metabolic_Medicine_and_Endocrinology.md` | 75g OGTT load unqualified | load |
| `16_01-05_Antenatal_Care.md` | neonatal vitamin K 1mg unqualified for preterm | dose, low |

New tracker entries: **B66–B70**. No paediatric figure was invented anywhere; every
absolute was **removed or marked, never replaced**, because the Australian paediatric
sources remain egress-blocked.

### Three patterns worth carrying forward

1. **The defect is often not in a "dose" field.** Four of the eleven were a *threshold*, a
   *rule of thumb*, a *test load*, and a *drug choice*. A scan looking only for
   prescriptions would have found seven.
2. **Contradiction between two files is stronger evidence than either file alone.** The
   `or`/`and` reversibility error was invisible in each file separately and obvious across
   the pair.
3. **Cross-references between an adult and a paediatric entry were consistently one-way.**
   The paediatric nephrotic entry pointed at the adult entry; the adult entry pointed at
   children while carrying the unmarked adult number. **Check the reciprocal direction of
   every adult↔paediatric pointer** — that asymmetry is now a known corpus defect shape.

### Honest limits

Restricted to quantities that a regex can recognise. It cannot see a dose stated only in
words, a paediatric contraindication expressed as prose, an adult-only *route*, or an
adult *frequency* attached to a correct per-kg amount. **Clean against this technique
only.**
