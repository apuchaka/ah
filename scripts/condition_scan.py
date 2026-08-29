#!/usr/bin/env python3
"""
Phase 5 Part A — condition-level coverage against an EXTERNAL condition list.

ENUMERATION SOURCE
A ~2,500-condition list supplied by the user, ordered in organ-system blocks.
This is the enumeration Part A was blocked on for three passes: the AMC and
curriculum documents are egress-blocked, and Part A twice reported honestly
that it had not been built rather than fabricating one. It is now real data,
so `data/checklist_external.csv` is finally created — the artifact that was
deliberately declined earlier, for the reason that a fabricated baseline
becomes permanent once every later round validates against it.

THE TEACH-VS-MENTION LENS
A term appearing in the corpus is not the corpus teaching it. Three verdicts,
drawn from structure rather than keyword density:

  OWNS ENTRY  the condition names a `##`/`###` section header. The corpus's
              entries carry D:/R:/S-Smx:/Ix:/Mx: markers, so a section is a
              taught unit by construction.
  IN A TAUGHT the condition is named inside a section that has >=2 of those
  SECTION     markers - it is discussed where teaching happens, but does not
              own the entry. Whether that amounts to teaching THIS condition
              or only naming it in passing is a judgement a scan cannot make;
              these are the rows that need a human read.
  MENTIONED   named only in prose with no teaching structure around it.
  ABSENT      no occurrence at all.

THREE MATCHING DEFECTS FOUND BY RUNNING THIS, FIXED HERE (rule 7)
The first version reported 77 of 170 cardiovascular conditions ABSENT. Almost
none were. The causes, in order of damage:

  1. SPELLING. The supplied list is US-spelt; this corpus is Australian.
     ischemia/ischaemia, edema/oedema, hemorrhage/haemorrhage, tumor/tumour,
     anemia/anaemia, esophagus/oesophagus, celiac/coeliac, leukemia/leukaemia.
     Both sides are now normalised through the same transform (ae/oe -> e,
     -our -> -or) so neither spelling can hide from the other. This one alone
     would have poisoned every organ system in the run, not just this one.
  2. ACRONYMS. The corpus writes LBBB, RBBB, HFrEF, HFpEF, WPW, AVM. An
     initialism is now generated mechanically from the condition's own words
     (stopwords and a trailing Syndrome/Disease/Block dropped) - it is derived
     from the list, not recalled from memory, so it adds no unsourced content.
  3. PLURALS. "Acute Coronary Syndromes" missed "Acute Coronary Syndrome".
     Matching now allows an optional trailing s/es on the final word.
  4. INTERPOSED WORDS. "Coarctation of aorta" missed "coarctation of THE
     aorta" - 22 occurrences. Substring matching cannot cross an inserted
     word; this is the same defect the Amsterdam II criteria hit in an
     earlier phase, recurring because the fix then was local to that check
     instead of being built into the matcher. Tokens are now joined by a
     gap that tolerates up to two filler words.
  6. POSSESSIVES AND PER-TOKEN PLURALS. "Eisenmenger syndrome" missed
     "Eisenmenger'S syndrome"; "Bicuspid aortic valveS" missed "bicuspid
     aortic valve". Optional 's and optional plural now apply to EVERY
     token, not just the last.

     Worth naming as a pattern rather than a sixth bullet: an externally
     supplied list names things in its own conventions, and each convention
     it does not share with the corpus is an independent source of false
     absence. Five rounds of fixes were needed here, each one found by
     disbelieving a plausible-looking ABSENT count rather than by foresight.
     Assume a seventh convention exists that this run did not find.

  8. INTERNAL HYPHENATION. "Postherpetic neuralgia" missed "post-herpetic
     neuralgia" (6 uses): the corpus compounds where the list does not, and
     token splitting cannot see across that. Fixed generally rather than
     per-case: when the token match fails, both sides are collapsed to
     letters-only and compared again, so hyphen, space and closed-compound
     forms all reduce to the same string.
  9. DIACRITICS. "Brown-Sequard" missed "Brown-Sequard" written with an
     accented e. Accents are now folded before matching.
 10. -IES PLURALS. "Radiculopathies" stemmed to "Radiculopathie" and matched
     nothing, while "radiculopathy" appears 7 times.
 11. EXTRA QUALIFIER WORDS - NOT FIXED. "Lambert-Eaton myasthenic syndrome"
     does not match "Lambert-Eaton syndrome": the gap tolerates inserted
     stopwords, not a dropped clinical adjective. Tolerating arbitrary
     dropped words would match almost anything, so this stays a known
     false-absence source; the weak-signal probe is what catches it.

  5. AN ACRONYM THE GENERATOR CANNOT REACH. "Arteriovenous Malformations"
     yields "AM", never "AVM", because the initialism is built from
     whitespace-separated words and the corpus's acronym splits inside one.
     Not fixable mechanically without inventing expansions, so instead every
     ABSENT verdict now carries a WEAK-SIGNAL probe: the hits for the name's
     most distinctive single token. A non-zero weak signal on an ABSENT row
     means "an alias probably exists - go read it", and is what the
     hand-check works from.

Markdown emphasis is stripped before matching (rule 2: this corpus writes
`**H**aemolysis`), and a parenthetical gloss is treated as an alternative,
so "Coronary artery disease (CAD)" also matches on its short form.

Every ABSENT verdict this scan produces is still hand-checked before being
called a gap. The 77 above are why.
"""
import re, glob, os, csv, sys, unicodedata

META = {"CLAUDE.md","CLAUDE_CODE_PROMPT.md","COWORK_HANDOFF.md",
        "MASTER_VERIFICATION_WORKFLOW.md","PENDING_GUIDELINE_CHECKS.md",
        "PHASE_EXECUTION_WORKFLOW.md","RECOMMENDED_WORKFLOW.md"}
MARKER = re.compile(r"^\s*[>\-\*]*\s*\*\*(D|R|S/Smx|S&Smx|Smx|Hx|Ix|Mx|Dx|Cx)\b", re.M)
HEADER = re.compile(r"^#{2,4}\s+(.+)$", re.M)

def strip_md(t):
    t = t.replace("\u2019","'").replace("\u2018","'")
    return re.sub(r"[*_`]", "", t)

def collapse(t):
    """Letters and digits only - defeats hyphen/space/compound differences."""
    return re.sub(r"[^a-z0-9]+", "", norm(t))

def norm(t):
    """Collapse AU/US spelling so neither can hide from the other."""
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = t.replace("\u00e6", "ae")
    t = re.sub(r"ae|oe", "e", t)
    t = re.sub(r"our\b", "or", t)
    t = t.replace("our", "or")
    # Convention 7, found the same way as the other six: the list writes
    # "Second Degree AV Block", the corpus writes "2nd degree". All three
    # AV-block rows read ABSENT against a section that teaches all three.
    for w, d in (("first","1st"),("second","2nd"),("third","3rd"),
                 ("fourth","4th"),("fifth","5th")):
        t = re.sub(r"\b" + d + r"\b", w, t)
    return t

GAP = r"[^A-Za-z]+(?:(?:the|of|a|an|with|and)[^A-Za-z]+){0,2}"
GENERIC = {"syndrome","disease","disorder","chronic","acute","primary","secondary",
           "congenital","idiopathic","malignant","benign","severe","failure",
           "infection","tumour","tumor","cancer","carcinoma","deficiency"}

def phrase(v):
    toks = [t for t in re.split(r"[^A-Za-z0-9]+", norm(v)) if t]
    if not toks: return re.compile(r"(?!x)x")
    # Singularise each token before allowing an optional plural, so a plural
    # in the list ("Bicuspid aortic valveS") still matches a singular in the
    # corpus. Allowing only a trailing s made the match one-directional.
    def stem(t):
        # -es is only the plural marker after s/x/z/ch/sh. Stripping it
        # blindly turned "valves" into "valv", which then could not match
        # "valve" - a fix that created the failure it was written to remove.
        if len(t) > 4 and t.endswith("ies"): return t[:-3] + "y"
        if len(t) > 4 and t.endswith("es") and re.search(r"(s|x|z|ch|sh)es$", t):
            return t[:-2]
        if len(t) > 3 and t.endswith("s") and not t.endswith("ss"): return t[:-1]
        return t
    body = GAP.join(re.escape(stem(t)) + r"(?:'s)?(?:es|s)?" for t in toks)
    return re.compile(r"(?<![A-Za-z])" + body + r"(?![A-Za-z])", re.I)

def weak_token(name):
    core = re.sub(r"\s*\([^)]*\)", " ", name)
    toks = [t for t in re.split(r"[^A-Za-z]+", core) if len(t) >= 8 and t.lower() not in GENERIC]
    return max(toks, key=len) if toks else None

STOP = {"with","of","the","and","in","to","a","an","for"}
TAIL = {"syndrome","disease","block","disorder","defect","tumour","tumor"}

def initialism(name):
    """Mechanically derived from the condition's own words - not recalled."""
    core = re.sub(r"\s*\([^)]*\)", " ", name)
    words = [w for w in re.split(r"[^A-Za-z]+", core) if w]
    words = [w for w in words if w.lower() not in STOP]
    out = []
    for drop_tail in (False, True):
        ws = words[:-1] if (drop_tail and words and words[-1].lower() in TAIL) else words
        if len(ws) >= 3: out.append("".join(w[0] for w in ws))
    return out

def load():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    out = []
    for f in sorted(glob.glob(os.path.join(root, "*.md"))):
        if os.path.basename(f) in META: continue
        raw = strip_md(open(f, encoding="utf-8").read())
        # split into sections at ##/### headers, keeping each header's text
        parts = []; last = 0; cur = "(preamble)"
        for m in HEADER.finditer(raw):
            parts.append((cur, raw[last:m.start()])); cur = m.group(1).strip(); last = m.end()
        parts.append((cur, raw[last:]))
        # Precompute the normalised and collapsed forms ONCE per section.
        # Computing them inside the per-condition loop made the scan
        # quadratic in (sections x conditions) and it timed out at two
        # systems; the earlier phase abandoned a matcher for the same reason
        # rather than shipping it, so it is fixed here instead.
        prepped = [(h, norm(h), collapse(h), norm(b), collapse(b),
                    len(MARKER.findall(b)) >= 2) for h, b in parts]
        out.append((os.path.basename(f), prepped))
    return out

def variants(name):
    """Full name plus any parenthetical short form, as separate alternatives."""
    v = [name]
    m = re.search(r"\(([^)]+)\)", name)
    if m:
        v.append(re.sub(r"\s*\([^)]*\)", "", name).strip())
        inner = m.group(1).strip()
        if len(inner) > 2 and not inner.islower(): v.append(inner)
    # slash alternatives: "Seborrhea/Seborrheic Dermatitis"
    if "/" in name and "(" not in name:
        v += [p.strip() for p in name.split("/") if len(p.strip()) > 3]
    v += initialism(name)
    return [x for x in dict.fromkeys(v) if len(x) > 2]

def classify(name, corpus):
    pats = [phrase(v) for v in variants(name)]
    cols = [collapse(v) for v in variants(name) if len(collapse(v)) >= 8]
    wk = weak_token(name)
    weak = re.compile(r"(?<![A-Za-z])" + re.escape(norm(wk)) + r"", re.I) if wk else None
    owns = []; taught = []; hits = 0; wsig = 0
    for fname, parts in corpus:
        for header, nh, ch, nb, cb, is_taught in parts:
            in_h = any(p.search(nh) for p in pats) or any(c in ch for c in cols)
            n = sum(len(p.findall(nb)) for p in pats)
            if not n: n = sum(cb.count(c) for c in cols)
            if in_h: owns.append(f"{fname}#{header}")
            if n:
                hits += n
                if is_taught: taught.append(f"{fname}#{header}")
            if weak is not None: wsig += len(weak.findall(nb))
    if owns: return "OWNS ENTRY", hits, owns[0]
    if taught: return "IN A TAUGHT SECTION", hits, taught[0]
    if hits: return "MENTIONED", hits, ""
    return "ABSENT", 0, (f"weak-signal:{wk}={wsig}" if wsig else "")

def run(system, names, corpus, writer):
    from collections import Counter
    c = Counter(); rows = []
    for nm in names:
        v, h, where = classify(nm, corpus)
        c[v] += 1
        rows.append((system, nm, v, h, where))
        writer.writerow({"system": system, "condition": nm, "verdict": v,
                         "occurrences": h, "first_location": where, "scope_judgement": ""})
    return c, rows

if __name__ == "__main__":
    print("import this module; see scan_system.py wrappers", file=sys.stderr)
