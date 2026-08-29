#!/usr/bin/env python3
"""Run every organ-system condition file in one pass.

The per-system wrapper reloads and re-preps all 148 files each time it is
called, which is fine for one system and quadratic across nineteen. This
loads the corpus once. The CSV is written whole at the end, so the run is
idempotent for the same reason the per-system writer is.
"""
import sys, os, csv, io, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import condition_scan as cs

SYSTEMS = [
 ("01_cardiovascular","Cardiovascular"), ("02_neurology","Neurology"),
 ("03_dermatology","Dermatology"), ("04_endocrine_metabolic","Endocrine and Metabolic"),
 ("05_genitourinary_repro","Genitourinary and Reproductive"),
 ("06_gastroenterology","Gastroenterology"),
 ("07_haem_genetics_onc","Haematology, Genetics and Oncology"),
 ("08_immunology_allergy","Immunology and Allergy"),
 ("09_toxicology_trauma","Toxicology, Environmental and Trauma"),
 ("10_psychiatry","Psychiatry"), ("11_rheum_msk","Rheumatology and Musculoskeletal"),
 ("12_systemic_misc","Systemic and Miscellaneous"), ("13_obstetrics","Obstetrics"),
 ("14_geriatrics_misc","Geriatrics and Safeguarding"),
 ("15_paediatrics_neonatal","Paediatrics and Neonatal"),
 ("16_renal_urology","Renal and Urology"), ("17_respiratory","Respiratory"),
 ("18_ent_ophthalmology","ENT and Ophthalmology"),
 ("19_infectious_disease","Infectious Disease"),
]
FIELDS = ["system","condition","verdict","occurrences","first_location","scope_judgement"]
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def main():
    corpus = cs.load()
    buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=FIELDS); w.writeheader()
    total = 0
    for key, name in SYSTEMS:
        path = os.path.join(ROOT, "data", f"conditions_{key}.txt")
        names = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
        counts, rows = cs.run(name, names, corpus, w)
        total += len(names)
        print(f"{name}|{len(names)}|{counts.get('OWNS ENTRY',0)}|"
              f"{counts.get('IN A TAUGHT SECTION',0)}|{counts.get('MENTIONED',0)}|{counts.get('ABSENT',0)}")
    open(os.path.join(ROOT,"data","checklist_external.csv"),"w",newline="",encoding="utf-8").write(buf.getvalue())
    print("TOTAL", total)

if __name__ == "__main__":
    main()
