#!/usr/bin/env python3
"""Regression and canary tests for the condition matcher.

REGRESSION CASES are the three that exposed the possessive-splitting and
generated-acronym defects. They must stay fixed.

CANARY CASES are deliberately drawn from OTHER systems with OTHER naming
conventions - paediatric eponyms, dermatology pluralisation, obstetric
abbreviation - because the two defects that were found were both found in
musculoskeletal eponyms, and a matcher proven only on the pattern that last
broke it is not proven. A canary failure means stop and fix, not proceed.

Each case states the expected verdict AND the ground truth it was checked
against by hand, so the test itself is auditable rather than self-confirming.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import condition_scan as cs

COVERED = {"OWNS ENTRY", "IN A TAUGHT SECTION", "MENTIONED"}

# (condition, must_be_covered, ground truth verified by hand)
REGRESSION = [
 ("Boxer's fracture", True,  "11_03_Ortho_-_Hand_and_Foot.md:57 '### Boxer fracture' - corpus omits the possessive"),
 ("Acromioclavicular joint pathology", True, "11_02_Ortho_-_Upper_Limb.md:48 '### Acromioclavicular joint injury' - pathology vs injury"),
 ("Achilles tendon rupture", True, "11_05_Ortho_-_Knee_and_Ankle.md:96 '## Achilles tendon' with Simmonds-Thompson test"),
 ("Clay-shoveler fracture", False, "genuinely absent - must NOT match via the generated CSF initialism"),
 ("Baker's cyst", True, "11_05_Ortho_-_Knee_and_Ankle.md:27 'Baker cyst' - possessive dropped by the corpus"),
]

# Different systems, different conventions
CANARY = [
 ("Hirschsprung's Disease", True,  "paediatrics: eponym + possessive, distinct from the MSK eponym pattern"),
 ("Kawasaki disease", True,        "paediatrics: eponym without possessive"),
 ("Tinea Corporis", True,          "dermatology: latin binomial, no plural"),
 ("Dermatophytoses", True,         "dermatology: -oses plural of -osis, a pluralisation the MSK cases never exercised"),
 ("Actinic Keratoses", True,       "dermatology: -oses plural again, different stem"),
 ("Pre-Eclampsia", True,           "obstetrics: hyphenated, and ae/oe spelling"),
 ("Placenta Previa", True,         "obstetrics: US spelling vs corpus praevia"),
 ("Zellweger syndrome", False,     "genuinely absent - a rare syndrome, guards against over-matching"),
 ("Manganese madness", False,      "genuinely absent - guards against over-matching on common words"),
]

def main():
    corpus = cs.load()
    fails = []
    for label, cases in (("REGRESSION", REGRESSION), ("CANARY", CANARY)):
        print(f"\n=== {label} ===")
        for name, want_covered, truth in cases:
            v, h, w = cs.classify(name, corpus)
            got = v in COVERED
            ok = got == want_covered
            if not ok: fails.append((label, name, v, truth))
            print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {v:20s} hits={h}")
            print(f"         expected {'covered' if want_covered else 'ABSENT'} - {truth}")
    print(f"\n{len(REGRESSION)+len(CANARY) - len(fails)}/{len(REGRESSION)+len(CANARY)} passed")
    if fails:
        print("\nFAILURES - do not run the full pass until these are fixed:")
        for lab, n, v, t in fails: print(f"  {lab}: {n} -> {v}\n     truth: {t}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
