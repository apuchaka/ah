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
| N5 | Clinical-Process-EBM-Consent-Capacity.md confirmation pass | 🔶 2026-08-28 — capacity confirmed excellent; clinical formulation confirmed absent, not built. |

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

### N6 remainder — allocated but not yet built

Deliberately left rather than thinned. Each is allocated to its destination file by the placement rule above, so the next round does not have to re-decide.

| Row | Yield | Goes in | Class |
|---|---|---|---|
| Explaining a medical error / open disclosure | Medium | `Communication.md` | absent |
| Managing complaints | Medium | `Communication.md` | absent |
| Talking to angry patients or relatives | Medium | `Communication.md` | absent |
| Dealing with an inappropriate patient (boundaries) | Medium | `Communication.md` | absent |
| Safeguarding — explaining a referral | Medium | `Communication.md` | partial (pathways exist; the conversation does not) |
| The family, families in crisis, family dysfunction | Medium | `Communication.md` | absent |
| Discussion/referral to specialities | Medium | `Communication.md` | absent |
| Documenting in the medical notes | Medium | `Clinical-Process-EBM-Consent-Capacity.md` | absent |
| Mandatory reporting (overall skill) | Medium | `Clinical-Process-EBM-Consent-Capacity.md` | partial (child + elder instances exist; no general duty entry) |
| Hospital avoidance | Medium | `19_…` | absent |
| Initial diagnostic strategy for common GP presentations | Medium | `19_…` (or `History-Taking` — decide on build) | absent |
| Key factors in selecting the most appropriate medication | Medium | `19_…` | absent |
| Assessment and basic management of pain | Medium | `19_…` | partial (palliative opioids exist; no general assessment or analgesic ladder) |
| Health promotion and patient education | Medium | folds into SNAP/preventive entries | partial |
| Counselling stations | Medium | — | `Communication.md` *is* this; no build needed |
| Initial GP investigation strategy overlap | Medium | — | see above |

---

**N2–N5 audit result (2026-08-28).** All 22 rows read, not matched.

> [!danger] **Second confirmed instance of this document's own record being wrong.** N2's row instructs a future round to "verify Notifiable Diseases and sensitivity/specificity are genuinely already adequate first." Notifiable diseases **is** adequate. **Sensitivity/specificity was not** — the terms appeared 8 times, every one an *application* to a specific test, with the concepts never defined and PPV/NPV absent entirely. This is the same conflation that produced the false "SNAP is covered" claim in N6: **applied in context ≠ built as a topic**. Two confirmed instances now. **Treat every "confirmed present" claim in this document as unverified until re-read.**

| Item | Audit result |
|---|---|
| **N3** (10 rows) | **Mostly already covered.** `Shock` — the row flagged as the most likely gap — is a **full standalone entry** (`01_Cardiovascular` 0.20, four subtypes, each with A/S-Smx/Ix/Mx/P). Adult ALS (`01_Cardiovascular` 0.5), paediatric/newborn (`15_01a`), choking (`13_05b`), overdose (`14a-2`, `03_Gastrointestinal`), head injury (`04_Neurology`), organ trauma (`11_09b`), wounds (`Examination`) all real. **Genuine gaps: Burns/scalds (zero hits — both rows) and a major-trauma primary-survey approach** (organ-specific trauma exists; no ATLS-style structured approach). |
| **N2** (6 rows) | **1 covered, 5 not.** Notifiable diseases ✅. **Built this round:** diagnostic test characteristics, and ARR/RRR/NNT. **Remaining:** study design & bias, p-values, screening principles (partly in `19_`). |
| **N4** (4 rows) | **See judgment below.** |
| **N5** (2 rows) | Capacity ✅ confirmed excellent (four-part test, SA legislation, SDM, OPA/SACAT). **Clinical formulation / structured clinical reasoning: genuinely absent**, one incidental hit corpus-wide. |

### N3 built (2026-08-28)

Both confirmed gaps built in `11_09b_Ortho_-_Trauma`, which despite its "Ortho" filename is this project's de facto general trauma file (it already held thoracic, genitourinary, splenic, liver, head and ocular trauma, none orthopaedic). Placement rejected `09_01_Dermatology_-_Dermatological_Emergencies` for burns on the grounds that it covers dermatological *disease* presenting as an emergency, not injury.

- **Burns and Scalds** — ANZCOR 9.1.3, ANZBA referral criteria. Two CSV rows, flagged absent early in the project and confirmed missing twice.
- **Major Trauma — Primary Survey** — built as a *differential* entry: the generic ABCDE is already complete in `Examination.md` and is explicitly not repeated, so this covers only what trauma changes. **Verified absent before building**, following the Shock lesson.

**Steps 5/6/10/18 applied in the same round**, not deferred. Step 5 found one gap (escharotomy named, not explained). Step 10 found a large sourced disparity in burns — rates 2–3× higher in Aboriginal and Torres Strait Islander children, and **only 34 of 208 caregivers received gold-standard first aid at the scene**, which makes the 3-hour cooling window clinically critical rather than trivia. For trauma, remoteness was stated as a *mechanism* with **no mortality figure asserted**, because none was sourced.

### N4 — judgment call, not a build

**Two of four rows should not be built, and building them would actively harm the corpus.**

- **Aboriginal and Torres Strait Islander health issues (Low)** — **189 mentions across 24 files**, condition-specific and actionable (ARF/RHD, CKD, otitis media's painless presentation, AUSDRISK's exclusion, cervical self-collection, aged care from 50, dementia at younger ages, KICA, smoking's closing gap, DFV). This is the *correct* architecture: equity content changes clinical thresholds at the point of care, which is where it belongs. A summary layer would duplicate distributed content and create two things to drift — the same problem caught and fixed with the N6 screening table. **No build.**
- **Rural general practice issues (Medium)** — distributed across 20 files, plus the remote-discharge box in `18_`. **No build.**

**Two rows are genuine gaps, both Low yield:**
- **Australian healthcare system** — Medicare/PBS/MBS appear only as incidental references inside disease entries (a PBS restriction, an MBS reform). No entry explains the system. ⬜
- **Detention / prison / immigration health** — genuinely absent; every apparent hit was "detention" under the Mental Health Act. ⬜

### N2–N5 remainder — allocated, not built

| Row | Yield | Goes in | Why not built |
|---|---|---|---|
| Study design types & bias | Medium | `Clinical-Process-EBM-Consent-Capacity` | Sits beside the two entries built this round |
| p-values & significance | Medium | `Clinical-Process-EBM-Consent-Capacity` | Same |
| Screening programme principles | Medium | `19_` (partly present) | Partly covered by the preventive medicine entry |
| Clinical formulation / reasoning | Medium | `Clinical-Process-EBM-Consent-Capacity` | Genuine gap |
| Australian healthcare system | Low | new — no existing file fits | Genuine gap |
| Detention / prison / immigration | Low | new — no existing file fits | Genuine gap |

---

### Phase 3 — mega files (M1–M10)
| # | Item | Status |
|---|---|---|
| M1 | 04_Neurology.md | 🔶 (3 rounds done — see file history; not urgent for a 4th) |
| M2 | 01_Cardiovascular.md | ⬜ |
| M3 | 03_Gastrointestinal.md | ⬜ |
| M4 | 06_Metabolic_Medicine_and_Endocrinology.md | ⬜ |
| M5 | 07_Renal_Medicine_and_Urology.md | ⬜ |
| M6 | Examination.md | 🔶 (received real work via M1's Newborn Exam find) |
| M7 | History-Taking.md | ⬜ |
| M8 | 02_Respiratory.md | ⬜ |
| M9 | 05_Ophthalmology.md | ⬜ |
| M10 | Investigation-Interpretation.md | 🔶 (received real work via M1's CT Head find) |

### Phase 4 — large files (L1–L10), then medium/small (G1–G39)
All ⬜ — see the full grouping table further down this document for exact file lists and copy-paste prompts. Work L1→L10, then G1→G39.

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

**Step 17 (UK-localisation) has now had one whole-project sweep run against it directly** — 26 files flagged, 5 spot-checked. Result: 1 genuine leftover UK term found and fixed ("A&E" → "Emergency Department (ED)" in `11_05_Ortho_-_Knee_and_Ankle.md`), 4 others confirmed as legitimate, already-verified AU-vs-UK comparison notes, not errors. This means Step 17's marginal cost per group is now genuinely lower than a from-scratch check — but **not zero**: 21 of the 26 flagged files haven't been individually confirmed yet, so when a group containing one of those 26 files comes up, still check its specific hit(s) against the flagged list below rather than assuming it's automatically fine.

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
| L1 | `verify: 08_09_Infectious_Disease_-_Miscellaneous.md` | 3 | Extensive prior work |
| L2 | `verify: 16_01-05_Antenatal_Care.md` | 4 | Moderate prior work |
| L3 | `verify: 09_08_Dermatology_-_Miscellaneous.md` | 3 | Extensive prior work |
| L4 | `verify: 08_01-03_Infectious_Disease_-_Bacterial_Infections.md, 08_04_Infectious_Disease_-_Antibiogram.md` | 3 | Extensive prior work |
| L5 | `verify: 08_05-06_Infectious_Disease_-_Viral_Infections.md, 08_10_Infectious_Disease_-_Diarrhoea_DDx_and_Gastroenteritis.md` | 3 | Extensive prior work |
| L6 | `verify: 03a_Anaesthetics_Primer.md` | 3 | Extensive prior work |
| L7 | `verify: 11_02_Ortho_-_Upper_Limb__Shoulder__Elbow__Distal_Radius_Fractures_.md` | 4 | Step 24 confirmed a real gap here (AC joint injury under-developed) — reclassified from "extensive" |
| L8 | `verify: 16_10-13_Labour_and_Delivery.md` | 4 | Moderate prior work |
| L9 | `verify: Communication.md, Clinical-Process-EBM-Consent-Capacity.md` | 5 | Never a primary target |
| L10 | `verify: 10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers.md, 10_12_Oncology_-_Breast.md` | 3 | Extensive prior work |

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

### New content required (Step 21 finding) — not verification, genuine build-from-scratch

These are fundamentally different from every row above: there's no existing file to run the 26-step pipeline (Steps 0–25) against. Run estimates here mean "rounds to research and build," not "rounds to re-check."

| # | Prompt | Est. rounds | Why |
|---|---|---|---|
| ~~N1~~ ✅ | ~~`build new content: Older Persons Health / Geriatrics — capacity assessment, cognitive screening context (link to the existing MMSE/MoCA/AMTS entry, don't duplicate), delirium vs dementia vs depression, discharge planning, elder abuse, falls, frailty, long-term care planning, osteoporosis/falls fracture prevention, polypharmacy/deprescribing` | 5–7 | 11 topics, 9 High yield, from genuinely zero existing coverage — the single largest gap found in this project |
| N2 | `build new content: Public Health/Epidemiology — NNT and absolute vs relative risk reduction, study design types and bias, p-value interpretation (verify Notifiable Diseases and sensitivity/specificity are genuinely already adequate first, don't rebuild what exists)` | 2–3 | 6 topics, but 2 already effectively covered |
| N3 | `build new content: Injury, Poisoning, Envenomation & Environmental — Shock, adult choking, major trauma, traumatic head injury, lacerations/abrasions, adult resuscitation (confirm Burns and paediatric/neonatal resuscitation status first, may already partially exist)` | 4–5 | 10 topics including Shock (High yield); several may already be scattered in emergency-medicine content elsewhere and just need consolidating rather than writing from zero |
| N4 | `build new content: Australian Context of Health — Australian healthcare system structure, rural general practice issues, detention/prison/immigration health (distinct from the disease-specific equity content already woven throughout the project)` | 2 | 4 topics, Low–Medium yield |
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
