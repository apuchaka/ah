#!/usr/bin/env python3
"""Drug-class section ownership, and the Vaughan-Williams test.

Two questions per class, answered separately and never merged:

  1. OWNERSHIP - does the class own a `##`/`###` header? Header text only,
     never body prose. A passing mention is not coverage.
  2. MEMBERSHIP - are the class's member drugs named anywhere in the corpus?

The interesting verdict is (1) NO and (2) YES: the members are all present and
the classification that governs choosing between them is not. That is the
Vaughan-Williams pattern, and it is what an exam tests.

WHY OWNERSHIP IS NOT DELEGATED TO section_owns.owns()
That matcher strips parenthetical glosses before comparing, so every one of
"Cephalosporins (1st Gen)" .. "(5th Gen)" normalises to "cephalosporins" and a
single `## Cephalosporins` header would claim all five. It did exactly that to
the six `Anticonvulsants (...)` subclasses, all of which matched the one
`## Anticonvulsants / Antiepileptics` header. Here the qualifier is part of the
match: the tokens inside the parentheses must be in the header too.

Aliases are checked ONE AT A TIME and the matching alias is reported, so no
general term can ever satisfy a specific query - the failure mode that made
"adult resuscitation|resuscitation" report 93 for a phrase that occurs zero
times.
"""
import re, os, sys, glob, unicodedata, csv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import section_owns as so

STOP = {"bs"}          # "Lincosamides(Bs)" - a bacteriostatic marker, not a word

def toks(t):
    """Normalise to a token set, keeping parenthetical qualifiers as tokens."""
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r"[*_`]", "", t)
    t = re.sub(r"^\d+(\.\d+)*\s*", "", t)
    out = []
    for w in re.split(r"[^a-z0-9]+", t):
        if not w or w in STOP: continue
        if len(w) > 3 and w.endswith("s"): w = w[:-1]     # plural only; no stemming
        out.append(w)
    # Rejoin a negation prefix to the word it negates. Splitting on the hyphen
    # made "non-sedating antihistamines" carry the tokens {sedating,
    # antihistamine}, so the label `**Oral non-sedating antihistamines**` was
    # returned as the corpus's subsection for H1 Antagonists (1st Gen) - the
    # sedating ones. A match on the negation of the query is worse than no
    # match, because it reads as coverage.
    merged = []
    for w in out:
        if merged and merged[-1] == "non": merged[-1] = "non" + w
        else: merged.append(w)
    return merged

def strip_md(s):
    return re.sub(r"[*_`]", "", s)

def corpus_text():
    parts = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
        b = os.path.basename(f)
        if b in so.META: continue
        parts[b] = strip_md(open(f, encoding="utf-8").read()).lower()
    return parts

# No `.` inside the capture: the first version used `\*\*(.+?)\*\*\s*[:-]`,
# and because the closing `**` had to be followed by a colon or dash it
# skipped the real closer in `**Mx:**` and ran on to the next `**` several
# clauses later. Every such capture was a whole sentence, and a sentence
# contains enough tokens to satisfy almost any class query - "Fixed drug
# eruption (FDE):** recurs at t..." was returned as the corpus's taught
# subsection for NSAIDs, sulfonamides and tetracyclines at once. A label is
# short and contains no markup, so say exactly that.
LABEL = re.compile(r"^\s*(?:[-*+]\s*)?\*\*([^*\n]{2,60}?)\*\*", re.M)

def labels():
    """Bold run-in labels: `**ACE inhibitors (-pril):**` and friends.

    THIS EXISTS BECAUSE A HEADER-ONLY SCAN UNDER-REPORTS.
    `### 0.34.1 Antihypertensives - detailed profiles` teaches ACE inhibitors,
    ARBs, beta-blockers, CCBs and thiazides as bolded run-in labels, each with
    its own mechanism, adverse effects and cautions. That is a clearly-titled
    subsection by any reading, and scoring only `##`/`###` called every one of
    those five classes uncovered. Reported as its own tier, never merged with
    header ownership, so the reader can see which kind of coverage a class has.
    """
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
        b = os.path.basename(f)
        if b in so.META: continue
        for m in LABEL.finditer(open(f, encoding="utf-8").read()):
            out.append((b, m.group(1).strip().rstrip(":\u2014- "), None))
    return out

def mr_headers():
    p = os.path.join(ROOT, "Medications_Reference.md")
    if not os.path.exists(p): return []
    return [(m.group(2).strip(), toks(m.group(2)))
            for m in so.HDR.finditer(open(p, encoding="utf-8").read())]

def named(term, text):
    """Is this term written anywhere in the corpus body? Allows a short suffix
    so a stem matches its inflections - the corpus writes `podophyllum`, and a
    search for `podophyllotoxin` found nothing while grep for `podophyll`
    found two files. Two of my own checks disagreeing is a stop-and-reconcile,
    not a coin toss: the member list was wrong, not the method."""
    t = term.lower().strip()
    if not t: return False
    rx = re.compile(r"(?<![a-z])" + re.escape(t) + r"[a-z]{0,3}(?![a-z])")
    return any(rx.search(v) for v in text.values())

def owned(name, hdrs):
    """(file, header, how) if a header owns this exact name, else None."""
    n = toks(name)
    if not n: return None
    for b, raw, _ in hdrs:
        h = toks(raw)
        if h == n: return (b, raw, "exact")
    for b, raw, _ in hdrs:
        h = toks(raw)
        if not all(t in set(h) for t in n): continue
        # A one-word query satisfied by any header that happens to contain the
        # word is the same defect as an alternation whose general branch answers
        # a specific question. `noradrenaline` matched the header `Serotonin-
        # noradrenaline reuptake inhibitors (SNRIs)` and reported SNRIs as the
        # corpus's section on noradrenaline the vasopressor. A single-token
        # query needs a header that is ABOUT that token, so cap the header's own
        # length. Every true positive of that kind (Aspirin, Lithium, Adenosine,
        # Benzodiazepines) is a one- or two-word header anyway. The exception is
        # an acronym alias, which legitimately sits inside its own expansion -
        # HRT in `Hormone replacement therapy (HRT)`, DOAC in `Direct oral
        # anticoagulants (DOACs)`. Capping length alone dropped both, so an
        # all-caps query is exempt.
        if len(n) == 1 and len(h) > 2 and not re.search(r"[A-Z0-9]{2,}", name): continue
        return (b, raw, "all tokens in header")
    return None

def main():
    hdrs = so.headers()
    labs = labels()
    mr = mr_headers()
    text = corpus_text()
    rows = []
    for line in open(os.path.join(ROOT, "data", "drug_class_members.tsv"), encoding="utf-8"):
        if not line.strip(): continue
        cls, aliases, members = line.rstrip("\n").split("\t")
        hit, how = None, ""
        r = owned(cls, hdrs)
        if r: hit, how = r, "class name"
        else:
            for a in aliases.split("|"):               # one at a time, never OR'd
                r = owned(a, hdrs)
                if r: hit, how = r, f'alias "{a}"'; break
        lab, labhow = None, ""
        if not hit:
            r = owned(cls, labs)
            if r: lab, labhow = r, "class name"
            else:
                for a in aliases.split("|"):
                    r = owned(a, labs)
                    if r: lab, labhow = r, f'alias "{a}"'; break
        mrhit = None
        for raw, h in mr:
            if all(t in set(h) for t in toks(cls)): mrhit = raw; break
        found = [m for m in members.split("|") if named(m, text)]
        # Second, independent membership signal. A class can be present in the
        # corpus under its own name with none of the members I happened to list
        # (PCSK9 inhibitors is named in two files; evolocumab and alirocumab are
        # in neither). Scoring membership only by member drug would have called
        # that ABSENT. Reported separately from `found` so the two are never
        # conflated.
        namely = [a for a in ([cls.split("(")[0].strip()] + aliases.split("|")) if named(a, text)]
        n_mem = len(members.split("|"))
        if hit:                 verdict = "OWNS"
        elif lab:               verdict = "BOLD LABEL"
        elif found or namely:   verdict = "MEMBERS ONLY"
        else:                   verdict = "ABSENT"
        rows.append(dict(cls=cls, verdict=verdict, how=how,
                         header=hit[1] if hit else "", file=hit[0] if hit else "",
                         label=lab[1] if lab else "", labelfile=lab[0] if lab else "", labelhow=labhow,
                         mr=mrhit or "", found="|".join(found), n=f"{len(found)}/{n_mem}",
                         named="|".join(namely)))
    w = csv.DictWriter(sys.stdout, fieldnames=["cls","verdict","how","header","file","label","labelfile","labelhow","mr","n","found","named"])
    w.writeheader(); w.writerows(rows)

if __name__ == "__main__":
    main()
