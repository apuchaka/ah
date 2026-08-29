#!/usr/bin/env python3
"""
Phase 5 Part C (third pass) — drug-depth check over an ENUMERATED drug list.

WHY THIS EXISTS, AND WHAT IT FIXES
The first two passes built the drug list from a suffix regex (-cillin, -mycin,
-azole ...). That method fixes how thoroughly a *found* drug is checked; it
cannot fix how the list of drugs to check was *built*. It structurally could
not reach GTN, antipsychotics, cephalosporins, clindamycin, metronidazole.
So the list here is not derived from the corpus at all. It is an external
enumeration, walked item by item, and every item gets a reported result —
including the ones that turn out to be fine.

ENUMERATION SOURCE (stated honestly, per rule 8)
The antimicrobial taxonomy is the one supplied in the requesting prompt
(penicillins / cephalosporins by generation / macrolides / tetracyclines /
aminoglycosides / glycopeptides / fluoroquinolones / sulfonamides /
nitroimidazoles / lincosamides / antifungals by subclass / antivirals by
target), expanded to named agents. It is NOT an extract of the AMH or the
BNF: those are subscription-gated and WebFetch is blocked in this
environment. That limit is real and is reported with the results rather
than papered over.

SCORING
For each agent, every paragraph in the corpus that names it is read WHOLE
(paragraph boundaries, not a character window — the character window was the
defect the user caught). Four dimensions are scored across the union of those
paragraphs:
    mech        mechanism / class of action
    dose        an Australian dose, route or frequency
    harm        side effects or monitoring
    contra      contraindications, cautions, interactions, resistance caveats
  ADEQUATE   >= 3 dimensions
  THIN       1-2 dimensions
  NAMED ONLY 0 dimensions but the agent is mentioned
  ABSENT     no mention anywhere in the corpus

TWO SCORES, AND WHY (rule 4 — assume the scan has a blind spot)
The first version of this scan scored the UNION of every paragraph mentioning
the agent, corpus-wide. That is too permissive in exactly the way the
character window was too narrow: a drug can score ADEQUATE with mechanism in
one file, a dose in a second and monitoring in a third, while no single entry
anywhere teaches it. So each agent now carries two verdicts:
    CORPUS  the union verdict — is the fact present anywhere at all
    ENTRY   the best single paragraph — does one place actually teach it
A CORPUS-ADEQUATE / ENTRY-THIN split is not a missing fact; it is a fact the
reader can only assemble by already knowing where to look. Those splits are
reported, not hidden inside the ADEQUATE count.

KNOWN BLIND SPOT, STATED UP FRONT (rule 3)
Each dimension is a keyword proxy, and a proxy can be satisfied by a word that
has nothing to do with the drug being taught. Macrolides score harm+contra
here off generic "diarrhoea"/"avoid"/"allergy" text in entries that merely
prescribe them, while the corpus carries ZERO QT-prolongation content for any
macrolide (verified by hand). So an ADEQUATE verdict from this scan is a
statement about vocabulary density, not about teaching. Every verdict below
ADEQUATE is a candidate finding; ADEQUATE means only "nothing this scan can
see is missing." It does not clear an item.

A THIN verdict is not automatically a defect: intern-level notes are allowed
to name a drug they only ever need to recognise. THIN is a candidate for
review, not a finding. That judgement is made by hand afterwards.
"""
import re, sys, glob, os

# ---------------------------------------------------------------- enumeration
# (group, agent, regex)
ITEMS = [
 ("Penicillins", "benzylpenicillin (penicillin G)", r"benzylpenicillin|penicillin G"),
 ("Penicillins", "phenoxymethylpenicillin (penicillin V)", r"phenoxymethylpenicillin|penicillin V"),
 ("Penicillins", "benzathine benzylpenicillin", r"benzathine"),
 ("Penicillins", "procaine penicillin", r"procaine penicillin"),
 ("Penicillins", "flucloxacillin (antistaphylococcal)", r"flucloxacillin|dicloxacillin"),
 ("Penicillins", "amoxicillin / ampicillin", r"amoxicillin|amoxycillin|ampicillin"),
 ("Penicillins", "amoxicillin-clavulanate", r"amoxicillin.?clavulan|amoxycillin.?clavulan|Augmentin|clavulanate"),
 ("Penicillins", "piperacillin-tazobactam", r"piperacillin|tazobactam|Tazocin"),
 ("Cephalosporins", "1st gen — cefalexin", r"cefalexin|cephalexin|Keflex"),
 ("Cephalosporins", "1st gen — cefazolin", r"cefazolin|cephazolin"),
 ("Cephalosporins", "2nd gen — cefuroxime", r"cefuroxime"),
 ("Cephalosporins", "2nd gen — cefoxitin", r"cefoxitin"),
 ("Cephalosporins", "3rd gen — ceftriaxone / cefotaxime", r"ceftriaxone|cefotaxime"),
 ("Cephalosporins", "3rd gen antipseudomonal — ceftazidime", r"ceftazidime"),
 ("Cephalosporins", "4th/5th gen — cefepime, ceftaroline", r"cefepime|ceftaroline"),
 ("Carbapenems/monobactam", "meropenem / imipenem / ertapenem", r"meropenem|imipenem|ertapenem"),
 ("Carbapenems/monobactam", "aztreonam", r"aztreonam"),
 ("Macrolides", "azithromycin", r"azithromycin"),
 ("Macrolides", "roxithromycin", r"roxithromycin"),
 ("Macrolides", "clarithromycin", r"clarithromycin"),
 ("Macrolides", "erythromycin", r"erythromycin"),
 ("Tetracyclines", "doxycycline", r"doxycycline"),
 ("Tetracyclines", "minocycline", r"minocycline"),
 ("Tetracyclines", "tetracycline / tigecycline", r"\btetracycline\b|tigecycline"),
 ("Aminoglycosides", "gentamicin", r"gentamicin"),
 ("Aminoglycosides", "tobramycin", r"tobramycin"),
 ("Aminoglycosides", "amikacin", r"amikacin"),
 ("Glycopeptides/lipopeptides", "vancomycin", r"vancomycin"),
 ("Glycopeptides/lipopeptides", "teicoplanin", r"teicoplanin"),
 ("Glycopeptides/lipopeptides", "daptomycin", r"daptomycin"),
 ("Fluoroquinolones", "ciprofloxacin", r"ciprofloxacin"),
 ("Fluoroquinolones", "norfloxacin", r"norfloxacin"),
 ("Fluoroquinolones", "moxifloxacin", r"moxifloxacin"),
 ("Fluoroquinolones", "levofloxacin / ofloxacin", r"levofloxacin|ofloxacin"),
 ("Sulfonamides/DHFR", "trimethoprim", r"trimethoprim"),
 ("Sulfonamides/DHFR", "trimethoprim-sulfamethoxazole (co-trimoxazole)", r"sulfamethoxazole|co.?trimoxazole|Bactrim"),
 ("Nitroimidazoles", "metronidazole", r"metronidazole"),
 ("Nitroimidazoles", "tinidazole", r"tinidazole"),
 ("Lincosamides", "clindamycin", r"clindamycin"),
 ("Lincosamides", "lincomycin", r"lincomycin"),
 ("Other antibacterial", "nitrofurantoin", r"nitrofurantoin"),
 ("Other antibacterial", "fosfomycin", r"fosfomycin"),
 ("Other antibacterial", "linezolid", r"linezolid"),
 ("Other antibacterial", "rifampicin", r"rifampicin"),
 ("Other antibacterial", "chloramphenicol", r"chloramphenicol"),
 ("Other antibacterial", "colistin / polymyxin", r"colistin|polymyxin"),
 ("Antifungal — azoles", "fluconazole", r"fluconazole"),
 ("Antifungal — azoles", "itraconazole", r"itraconazole"),
 ("Antifungal — azoles", "voriconazole / posaconazole", r"voriconazole|posaconazole"),
 ("Antifungal — azoles", "clotrimazole / miconazole (topical)", r"clotrimazole|miconazole"),
 ("Antifungal — azoles", "ketoconazole", r"ketoconazole"),
 ("Antifungal — other", "terbinafine (allylamine)", r"terbinafine"),
 ("Antifungal — other", "nystatin / amphotericin B (polyenes)", r"nystatin|amphotericin"),
 ("Antifungal — other", "caspofungin / anidulafungin (echinocandins)", r"caspofungin|anidulafungin|micafungin|echinocandin"),
 ("Antifungal — other", "griseofulvin", r"griseofulvin"),
 ("Antiviral — herpes family", "aciclovir", r"aciclovir|acyclovir"),
 ("Antiviral — herpes family", "valaciclovir", r"valaciclovir|valacyclovir"),
 ("Antiviral — herpes family", "famciclovir", r"famciclovir"),
 ("Antiviral — herpes family", "ganciclovir / valganciclovir (CMV)", r"ganciclovir"),
 ("Antiviral — influenza", "oseltamivir", r"oseltamivir"),
 ("Antiviral — influenza", "zanamivir", r"zanamivir"),
 ("Antiviral — HIV/hepatitis", "tenofovir", r"tenofovir"),
 ("Antiviral — HIV/hepatitis", "emtricitabine / lamivudine", r"emtricitabine|lamivudine"),
 ("Antiviral — HIV/hepatitis", "dolutegravir / raltegravir (integrase inhibitors)", r"dolutegravir|raltegravir|integrase"),
 ("Antiviral — HIV/hepatitis", "entecavir (hep B)", r"entecavir"),
 ("Antiviral — HIV/hepatitis", "sofosbuvir / DAA (hep C)", r"sofosbuvir|velpatasvir|glecaprevir|direct.acting antiviral"),
 ("Antituberculous", "isoniazid", r"isoniazid"),
 ("Antituberculous", "rifampicin (TB regimen role)", r"rifampicin"),
 ("Antituberculous", "pyrazinamide", r"pyrazinamide"),
 ("Antituberculous", "ethambutol", r"ethambutol"),
 ("Antiparasitic", "ivermectin", r"ivermectin"),
 ("Antiparasitic", "permethrin", r"permethrin"),
 ("Antiparasitic", "albendazole / mebendazole", r"albendazole|mebendazole"),
 ("Antiparasitic", "praziquantel", r"praziquantel"),
 ("Antiparasitic", "artemether-lumefantrine / atovaquone-proguanil (malaria)", r"artemether|lumefantrine|atovaquone|proguanil|Riamet|Malarone"),
]

MECH = re.compile(r"mechanism|inhibit|bacteriocid|bactericid|bacteriostat|cell wall|ribosom|beta.?lactam|β.?lactam|DNA gyrase|folate|ergosterol|protein synthesis|binds|blocks|acts on|transpeptid|topoisomerase|reverse transcript", re.I)
DOSE = re.compile(r"\d+\s*(mg|g|micrograms|mcg|units|IU|mL)\b|\bmg/kg\b|\bBD\b|\bTDS\b|\bQID\b|\bdaily\b|\bIV\b|\bIM\b|\boral", re.I)
HARM = re.compile(r"side.?effect|adverse|toxicit|monitor|level|trough|nephrotox|ototox|hepatotox|QT|C\.? ?difficile|diarrhoea|rash|nausea|marrow|neutropen|photosensitiv|tendon|red man|myopath|neuropath", re.I)
CONTRA=re.compile(r"contraindicat|caution|avoid|not (in|for|used)|allerg|anaphyla|pregnan|renal impair|hepatic impair|interact|resistan|CYP|warfarin|breastfeed", re.I)

def paragraphs(text, rx):
    out=[]
    for m in rx.finditer(text):
        s=text.rfind("\n\n",0,m.start()); s=0 if s<0 else s+2
        e=text.find("\n\n",m.end()); e=len(text) if e<0 else e
        out.append(text[s:e])
    return out

def main():
    # Meta files (the workflow doc, the tracker, CLAUDE.md) NAME drugs while
    # describing gaps in them. Counting them as corpus makes a scan report
    # coverage it created itself. Excluded by name, not by heuristic.
    META = {"CLAUDE.md","CLAUDE_CODE_PROMPT.md","COWORK_HANDOFF.md",
            "MASTER_VERIFICATION_WORKFLOW.md","PENDING_GUIDELINE_CHECKS.md",
            "PHASE_EXECUTION_WORKFLOW.md","RECOMMENDED_WORKFLOW.md"}
    files=[f for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__),"..","*.md")))
           if os.path.basename(f) not in META]
    corpus=[(os.path.basename(f), open(f,encoding="utf-8").read()) for f in files]
    splits=[]
    counts={"ADEQUATE":0,"THIN":0,"NAMED ONLY":0,"ABSENT":0}
    n=0
    for group,agent,pat in ITEMS:
        n+=1
        rx=re.compile(pat,re.I)
        paras=[]; hits=0; where=set()
        for name,text in corpus:
            p=paragraphs(text,rx)
            if p: hits+=len(p); where.add(name)
            paras+=p
        DIMS=(("mech",MECH),("dose",DOSE),("harm",HARM),("contra",CONTRA))
        def score(txt): return [d for d,r in DIMS if r.search(txt)]
        def verdict(dims,any_para):
            if not any_para: return "ABSENT"
            if len(dims)>=3: return "ADEQUATE"
            return "THIN" if dims else "NAMED ONLY"
        udims=score("\n".join(paras))
        best=max((score(x) for x in paras), key=len, default=[])
        uv=verdict(udims,paras); ev=verdict(best,paras)
        counts[uv]+=1
        if uv!=ev: splits.append((n,agent,uv,ev))
        flag=" <-- assembled across entries" if uv!=ev else ""
        print(f"{n:3d}. [corpus {uv:10s}| entry {ev:10s}] {agent}  ({group}){flag}")
        print(f"       mentions={hits} files={len(where)} corpus={'+'.join(udims) or '-'} entry={'+'.join(best) or '-'}")
    print("\nTOTAL", len(ITEMS), counts)
    print(f"CORPUS/ENTRY SPLITS: {len(splits)}")
    for n,a,uv,ev in splits: print(f"   {n:3d}. {a}: corpus {uv} but best single entry {ev}")

if __name__=="__main__":
    main()
