---
name: recommended-workflow
description: The final recommended tooling and process setup for completing the Grind Time intern exam notes project — balancing efficiency, accuracy, and thoroughness. Read alongside COWORK_HANDOFF.md and MASTER_VERIFICATION_WORKFLOW.md.
---

# Recommended Workflow — Final Setup

The short version: **Claude Code, files in git, scripts written once, autonomous runs reviewed by diff, with a separate review session for judgment-heavy calls.**

---

## The core insight this rests on

This project has two genuinely different kinds of work, and they have opposite optimal setups:

| | **Mechanical work** | **Judgment work** |
|---|---|---|
| What it is | grep sweeps, CSV cross-checks, regex scans, structural verification, cross-reference audits | Is this a real gap or a search artifact? Is this depth past the intern ceiling? Is this citation accurate? Does this content actually integrate? |
| Volume | ~80% of total effort | ~20% of total effort |
| Best setup | Autonomous, scripted, batched | Reviewed, deliberate, one at a time |
| Failure mode if done wrong | Slow and inconsistent | Confident errors that propagate |

The previous chat-based approach did both in the same mode — deliberate and one-at-a-time — which was accurate but slow. Doing both autonomously would be fast but would let confident errors through. **The recommended setup splits them.**

---

## Phase 0 — One-time setup (do this before any project work)

1. **Put all files in a git repo.** 146 content `.md` files, `checklist.csv`, `MASTER_VERIFICATION_WORKFLOW.md`, `COWORK_HANDOFF.md`. Commit the current state as a baseline before any changes.

   This single step is the highest-value thing in this document. It makes every subsequent autonomous change a reviewable diff rather than an invisible edit, which is what makes autonomous running safe enough to be worth doing.

2. **Convert the workflow document's inline scan snippets into actual saved scripts.** Ask Claude Code to build:
   - `check_structure.sh` — duplicate headers, wikilink resolution, sync status, file count (Steps 0, 1, and the final sweep)
   - `csv_crosscheck.py` — full category row pull + presence check, with **case-insensitive matching, Unicode normalisation, and hyphenation-variant handling built in** (Steps 3, 21, 23, 24)
   - `citation_audit.py` — bidirectional cross-reference accuracy check (Step 8)
   - `completeness_scan.py` — the granular Ix/Mx and template scans (Steps 2, 13)

   **Why this matters more than it sounds**: the single worst error in the previous session came from retyping a grep and omitting `-i`, producing a confident 21-item false gap list. Prose descriptions of scans get retyped and mistyped; saved scripts get debugged once and stay correct. Each script should also print a **reminder of its known false-positive patterns** (documented per-step in the workflow file) alongside its results.

3. **Verify each script against a known-good case before trusting it.** Run `csv_crosscheck.py` on Neurology and confirm it does *not* flag Multiple Sclerosis, Trigeminal Neuralgia, or α-/β-thalassaemia — all of which produced false positives with naive search patterns previously. If a script flags those, it has the same bug the old approach did.

---

## Phase 1 — Autonomous execution (Claude Code, batched)

Run queue items in batches of **2–4**, not one at a time and not the whole phase at once.

**Per batch, the instruction is:**
> Run queue items [P1–P3] from MASTER_VERIFICATION_WORKFLOW.md. Use the saved scripts rather than retyping scans. For every hit any script produces, verify it manually against the actual file content before treating it as a real gap — the scripts have documented false-positive patterns, and most hits historically are artifacts. Fix confirmed gaps, verify each fix introduced no duplicate headers and that every cross-reference target's exact header text exists, commit each fix as a separate commit with a descriptive message, and update the queue status markers. Report what you found, separating confirmed gaps from dismissed false positives.

**Why batches of 2–4**: large enough to get real efficiency from autonomy, small enough that if the run develops a systematic error, you catch it after 3 items rather than 20.

**Why separate commits per fix**: makes bad individual changes revertable without losing good ones from the same run.

---

## Phase 2 — Diff review (after each batch, in Claude Code)

Review `git diff` for the batch. Specifically check:
- **Were dismissed false positives genuinely dismissed with a reason?** A run that reports "found 14 gaps, fixed 14" is more suspicious than one reporting "found 14 hits, 11 were search artifacts, fixed 3."
- **Do all new cross-references resolve?** Run `citation_audit.py` after the batch, not just during.
- **Did any fix introduce a duplicate header or break a wikilink?** `check_structure.sh` catches this.
- **Does new content sit at intern/RMO depth**, not specialist depth? This is the judgment call scripts can't make — read the actual prose of anything substantial that was added.

---

## Phase 3 — Periodic deep review (separate fresh chat session, every ~10–15 queue items)

Autonomous runs drift in ways diffs don't fully reveal — depth creep, house-style inconsistency, cross-references that resolve but describe content inaccurately. Every 10–15 items, start a **fresh chat session** (not Claude Code) and hand it:
- `MASTER_VERIFICATION_WORKFLOW.md`
- The 5–10 files most heavily modified since the last deep review
- The git diff for that period

Ask specifically for: intern/RMO depth-ceiling audit (Step 18), readability/cognitive-load check (Step 15), and a spot-audit of 5 randomly sampled guideline citations for accuracy (Step 22). These are the checks that genuinely need judgment rather than pattern-matching, and a fresh session with clean context does them better than a long-running one.

---

## Phase 4 — Content builds (Phase 2 of the queue: Geriatrics, GP/Ethics, etc.)

Handle these **differently from verification** — they're research-and-write, not search-and-check.

- Run them in Claude Code (or Cowork, which is equally suited here), **one topic at a time, not one category at a time.** Geriatrics has 11 topics; building all 11 in one autonomous run risks uniform-but-shallow output. One topic per run produces the depth the rest of this project has.
- **Require a source citation per topic**, verified against an Australian guideline (RACGP, Therapeutic Guidelines, state health guidelines, relevant college). The workflow document's Step 11 lists what counts.
- Review these more closely than verification diffs — new prose is where depth creep and unsourced claims enter most easily.

---

## What this setup is expected to achieve

- **Throughput**: batched autonomous runs replace ~245 individual human-triggered rounds with roughly 60–80 batch instructions plus periodic reviews.
- **Accuracy**: preserved by scripts (eliminating retyping errors), diff review (catching bad fixes), and periodic fresh-session judgment audits (catching drift).
- **Thoroughness**: unchanged — the same 26-step method, same queue, same standard.

**The honest caveat, carried forward from the workflow document**: this project's history is that every "complete" declaration was later proven incomplete by a new technique. This setup makes the work faster and more consistent; it does not make it provably exhaustive. Report results as "clean against everything currently known to check for," not "verified complete."
