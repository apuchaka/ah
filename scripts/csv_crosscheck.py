#!/usr/bin/env python3
"""csv_crosscheck.py — full category row pull + presence check.

Covers MASTER_VERIFICATION_WORKFLOW.md Steps 3, 4, 21, 23 and 24: pull the
COMPLETE row list for a category (never a spot-check), then test each topic
for genuine presence in the content files.

The whole point of this script is CLAUDE.md rule 2: *zero grep hits is not
proof of absence*. Every historical "missing" finding in this project turned
out to be a search artifact. So the matcher deliberately over-generates
variants rather than under-generating, and every hit reports WHICH variant
matched so the match can be audited rather than trusted.

Variant handling implemented
----------------------------
  case             Multiple sclerosis      <-> Multiple Sclerosis
  ae / oe          Thalassemia             <-> Thalassaemia, esophag <-> oesophag
                                               (also haem/hem, paed/ped, gynae/gyne,
                                                anaemia/anemia, diarrhoea/diarrhea, ...)
  Greek letters    alpha / beta / ...      <-> α / β / γ / δ / μ
  subscripts       CHA2DS2-VASc            <-> CHA₂DS₂-VASc  (and superscripts, ABCD²)
  hyphenation      Bi-fascicular <-> Bifascicular <-> Bi fascicular
                   Non-Melanoma  <-> Nonmelanoma  <-> Non Melanoma
  Unicode punct.   ’ ‘ ` <-> '   |  – — ‒ − <-> -   |  non-breaking space <-> space
  parentheticals   "Thalassemia (alpha and beta)" also searched as "Thalassemia",
                   and each parenthetical fragment searched separately
  separators       "A / B", "A, B", "A and B", "A; B", "A - B" split into parts
                   (each part >= MIN_PART_LEN chars is searched on its own)
  trailing junk    footnote markers (*, †), trailing punctuation, unbalanced "("
  possessives      Bell's palsy <-> Bells palsy <-> Bell palsy, and the reverse
                   direction: "Parkinson disease" (CSV) <-> "Parkinson's disease"
  diacritics       Guillain-Barre <-> Guillain-Barre with e-acute
  plurals          tumour/tumours, -y/-ies, -is/-es (light stemming on the last word)

Match tiers (every result reports which tier matched, so a weak match is never
presented as a strong one)
--------------------------------------------------------------------------
  exact      contiguous match of a generated variant, separators collapsed
  proximity  all discriminating words within ~90 chars, ANY order. Catches
             interposed text ("Extradural haematoma" vs "Extradural (Epidural)
             Haematoma") and transposed words ("Benign Positional Paroxysmal
             Vertigo" vs "Benign Paroxysmal Positional Vertigo")
  fuzzy      one long word recovered by edit distance, for typos in the CSV
             itself ("Tredelenburg" -> "Trendelenburg")
  acronym    short ALL-CAPS token (GCS, AVPU) matched case-sensitively on raw
             text, since case-folding one would match noise

Validation record
-----------------
`--self-test` runs 21 cases through the real search engine, including the eight
topics that the first Neurology run wrongly reported MISSING (Parkinson disease,
Guillain-Barre, Motor Neurone Disease, Extradural haematoma, BPPV, Headache in a
child, Tredelenburg's gait, and the GCS/AVPU compound row). All eight were search
artifacts, not gaps. Run --self-test after ANY change to the variant generator.

KNOWN LIMITATIONS — read before trusting a "MISSING" line
---------------------------------------------------------
  * A MISSING result is a CANDIDATE, never a conclusion. Alternate medical vs
    lay terminology (Encopresis vs faecal incontinence), abbreviation-only
    coverage, and a topic homed in a different category are NOT modelled and
    are the most likely remaining causes of a false MISSING. Hand-check every
    one against the actual files before calling it a gap.
  * A FOUND result proves the string exists, not that it is BUILT. Step 3
    requires a depth check. This script reports hit count, whether the term
    appears as a markdown header, and the longest section it heads, as depth
    SIGNALS only — a low score is a prompt to open the file, not a verdict.
  * Very short/generic topics ("Weakness", "Headache", "Tremor") will match
    trivially and tell you nothing. They are marked GENERIC in the output.
  * Splitting on separators can over-generate: matching one fragment of
    "Intra-Cranial Haemorrhage; Extra-dural, Sub-dural..." does not mean the
    whole row is covered. Fragment-only matches are marked PARTIAL.
  * Matching is substring-based, so a topic can match inside a longer unrelated
    word. Short variants (< MIN_PART_LEN chars) are dropped for this reason,
    but the risk is not eliminated.

Usage
-----
  scripts/csv_crosscheck.py --category "Neurology"
  scripts/csv_crosscheck.py --list-categories
  scripts/csv_crosscheck.py --all                       # every category
  scripts/csv_crosscheck.py --category Neurology --files '04_*.md'
  scripts/csv_crosscheck.py --category Haematology --topic "Thalassemia"
  scripts/csv_crosscheck.py --category Neurology --missing-only
  scripts/csv_crosscheck.py --self-test                 # variant-generator tests

Exit status: 0 = ran, 1 = at least one MISSING candidate, 2 = usage error.
"""

import argparse
import csv
import glob
import os
import re
import sys
import unicodedata

# --- configuration ---------------------------------------------------------

META_FILES = {
    "CLAUDE.md",
    "CLAUDE_CODE_PROMPT.md",
    "COWORK_HANDOFF.md",
    "MASTER_VERIFICATION_WORKFLOW.md",
    "PHASE_EXECUTION_WORKFLOW.md",
    "RECOMMENDED_WORKFLOW.md",
}

CSV_NAME = "checklist.csv"
CATEGORY_COL = "Category"
TOPIC_COL = "Topic"
YIELD_COL = "Yield (MCQ+OSCE)"

MIN_PART_LEN = 5      # a fragment shorter than this is too generic to search
GENERIC_LEN = 12      # whole topics shorter than this are flagged GENERIC

# --- Unicode / spelling normalisation --------------------------------------

GREEK = {
    "α": "alpha", "Α": "alpha",
    "β": "beta",  "Β": "beta",
    "γ": "gamma", "Γ": "gamma",
    "δ": "delta", "Δ": "delta",
    "μ": "mu",    "Μ": "mu",
    "κ": "kappa", "λ": "lambda",
}

SUBSUP = {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
    "¹": "1", "²": "2", "³": "3",
    "⁰": "0", "⁴": "4", "⁵": "5", "⁶": "6",
    "⁷": "7", "⁸": "8", "⁹": "9",
}

PUNCT = {
    "’": "'", "‘": "'", "ʼ": "'", "`": "'", "´": "'",
    "“": '"', "”": '"',
    "–": "-", "—": "-", "‒": "-", "−": "-", "‐": "-",
    "‑": "-",
    " ": " ", " ": " ", " ": " ", "​": "",
}

# Applied in both directions by generating the alternative spelling.
# (British form -> American form); the reverse is generated too.
DIGRAPHS = [
    ("aemia", "emia"), ("aemic", "emic"),
    ("haem", "hem"), ("hae", "he"),
    ("paed", "ped"),
    ("gynae", "gyne"),
    ("oesoph", "esoph"), ("oedema", "edema"), ("oestro", "estro"),
    ("orrhoea", "orrhea"), ("rhoea", "rhea"),
    ("aetio", "etio"), ("anaesth", "anesth"), ("anaemi", "anemi"),
    ("caesar", "cesar"), ("coeliac", "celiac"), ("foet", "fet"),
    ("leuk", "leuc"), ("tumour", "tumor"), ("colour", "color"),
    ("oedem", "edem"), ("ischaem", "ischem"), ("dyspnoea", "dyspnea"),
    ("gonorrhoea", "gonorrhea"), ("thalassaem", "thalassem"),
    ("sulph", "sulf"), ("fibre", "fiber"), ("centre", "center"),
    ("praevia", "previa"), ("oophor", "oophor"),
    ("diarrhoea", "diarrhea"), ("paediatr", "pediatr"),
    ("orthopaed", "orthoped"), ("labour", "labor"), ("behaviour", "behavior"),
    ("neurone", "neuron"), ("oestrogen", "estrogen"), ("amoeb", "ameb"),
    ("dyskinaesi", "dyskinesi"), ("anaesthes", "anesthes"), ("hyperkalaem", "hyperkalem"),
]

SPLIT_RE = re.compile(r"\s*(?::|/|,|;|\band\b|\bor\b|\bvs\.?\b|\beg\b|\be\.g\.\b|–|—| - )\s*",
                      re.IGNORECASE)

# Words carrying no discriminating power for proximity matching.
STOPWORDS = {"in", "a", "an", "the", "of", "and", "or", "with", "for", "to",
             "on", "by", "from", "is", "as", "at", "vs", "eg", "its", "may",
             "types", "type", "presentation", "management", "approach"}


def strip_accents(text):
    """Fold diacritics: Guillain-Barre <-> Guillain-Barre (e-acute)."""
    d = unicodedata.normalize("NFD", text)
    return "".join(c for c in d if not unicodedata.combining(c))


def nfkc(text):
    """Unicode-normalise, then fold Greek letters, sub/superscripts and smart punctuation."""
    out = []
    for ch in text:
        if ch in GREEK:
            out.append(GREEK[ch])
        elif ch in SUBSUP:
            out.append(SUBSUP[ch])
        elif ch in PUNCT:
            out.append(PUNCT[ch])
        else:
            out.append(ch)
    text = "".join(out)
    text = unicodedata.normalize("NFKC", text)
    # NFKC can reintroduce nothing here, but re-fold punctuation it may produce.
    for src, dst in PUNCT.items():
        text = text.replace(src, dst)
    return text


def canon(text):
    """Aggressive canonical form used for BOTH haystack and needle.

    Lowercases; folds Greek/subscript/punctuation; strips apostrophes; collapses
    hyphens, slashes and whitespace to a single space; then removes spaces
    entirely so that hyphenation and spacing variants all collapse together
    (Bi-fascicular / Bifascicular / Bi fascicular -> bifascicular).
    """
    return spaced_canon(text).replace(" ", "")


def spaced_canon(text):
    """Word-preserving canonical form: same folding as canon() but words stay
    separated by single spaces, so word-level proximity matching is possible."""
    text = strip_accents(nfkc(text)).lower()
    text = text.replace("'", "")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def digraph_variants(term):
    """Generate British<->American spelling alternatives (both directions).

    Substitution is done on the lowercased term: matching is case-insensitive
    downstream (canon() lowercases), and doing it case-sensitively silently
    missed capitalised heads such as "Oesophageal" -> "Esophageal".
    """
    out = {term, term.lower()}
    for _ in range(2):  # two passes lets multi-digraph terms settle
        for t in list(out):
            for br, am in DIGRAPHS:
                if br in t:
                    out.add(t.replace(br, am))
                if am in t:
                    out.add(t.replace(am, br))
    return out


def plural_variants(term):
    """Light stemming on the final word only: tumour/tumours, -y/-ies, -is/-es."""
    out = {term}
    m = re.search(r"(\w+)$", term)
    if not m:
        return out
    word, start = m.group(1), m.start(1)
    head = term[:start]
    forms = {word}
    if word.endswith("ies") and len(word) > 4:
        forms.add(word[:-3] + "y")
    if word.endswith("y") and len(word) > 3:
        forms.add(word[:-1] + "ies")
    if word.endswith("es") and len(word) > 4:
        forms.add(word[:-2])
        forms.add(word[:-2] + "is")
    if word.endswith("is") and len(word) > 3:
        forms.add(word[:-2] + "es")
    if word.endswith("s") and len(word) > 3:
        forms.add(word[:-1])
    else:
        forms.add(word + "s")
    for f in forms:
        out.add(head + f)
    return out


def possessive_variants(term):
    """Bell's palsy -> Bells palsy -> Bell palsy."""
    out = {term}
    t = nfkc(term)
    out.add(t)
    if "'" in t:
        out.add(t.replace("'s ", " "))
        out.add(t.replace("'s", "s"))
        out.add(t.replace("'", ""))
    else:
        # Reverse direction: the CSV writes "Parkinson disease", the notes write
        # "Parkinson's disease". Without this, every eponym the CSV de-possessives
        # becomes a false MISSING.
        words = t.split()
        for i, w in enumerate(words[:-1]):
            if w[:1].isupper() and len(w) > 3 and not w.endswith("s"):
                out.add(" ".join(words[:i] + [w + "'s"] + words[i + 1:]))
    return out


def clean_topic(topic):
    """Strip footnote markers and trailing punctuation/unbalanced brackets."""
    t = nfkc(topic).strip()
    t = t.rstrip("*†‡ ")
    t = t.strip()
    # Unbalanced opening paren, e.g. "Aphasia / Dysphasia (Receptive, expressive,"
    if t.count("(") > t.count(")"):
        t = t[: t.rindex("(")].strip()
    t = t.rstrip(" ,;:.-–—")
    return t


def expand_topic(topic):
    """Build the search-variant set for one CSV topic.

    Returns (whole_variants, part_variants). A hit on `whole` means the topic as
    named is present; a hit only on `part` is reported as PARTIAL because
    matching one fragment of a compound row does not cover the whole row.
    """
    base = clean_topic(topic)

    wholes = {base}
    # Topic with any parenthetical removed, plus each parenthetical's contents.
    parens = re.findall(r"\(([^)]*)\)", base)
    stripped = re.sub(r"\([^)]*\)", " ", base)
    stripped = re.sub(r"\s+", " ", stripped).strip(" ,;:-")
    if stripped:
        wholes.add(stripped)

    parts = set()
    for p in parens:
        for frag in SPLIT_RE.split(p):
            frag = frag.strip(" ,;:-")
            if len(frag) >= MIN_PART_LEN:
                parts.add(frag)
    for w in list(wholes):
        for frag in SPLIT_RE.split(w):
            frag = frag.strip(" ,;:-")
            if len(frag) >= MIN_PART_LEN and frag.lower() != w.lower():
                parts.add(frag)

    # Leading head-noun prefixes: "Brain tumour types and presentation" should be
    # able to match "brain tumours" through its head phrase "Brain tumour".
    # These go in `parts` (-> PARTIAL), never `wholes`: a prefix match is partial
    # evidence for the row, not proof the whole row is covered.
    STOP = {"of", "for", "the", "in", "and", "or", "with", "to", "a", "an",
            "on", "by", "from", "vs", "at", "as", "is"}
    for w in list(wholes) + list(parts):
        words = w.split()
        for n in range(2, min(len(words), 4)):
            pre = " ".join(words[:n])
            if words[n - 1].lower().strip(",;:") in STOP:
                continue
            pre = pre.strip(" ,;:-")
            if len(pre) >= MIN_PART_LEN and pre.lower() != w.lower():
                parts.add(pre)

    # "Thalassemia (alpha and beta)" -> also "alpha thalassemia", "beta thalassemia".
    # A qualifier inside parentheses very often prefixes the head noun in prose.
    if stripped and parens:
        for p in parens:
            for frag in SPLIT_RE.split(p):
                frag = frag.strip(" ,;:-")
                if 2 <= len(frag) <= 20:
                    wholes.add("%s %s" % (frag, stripped))
                    wholes.add("%s-%s" % (frag, stripped))
                    wholes.add("%s %s" % (stripped, frag))

    def blow_up(seed):
        out = set()
        for s in seed:
            for a in possessive_variants(s):
                for b in digraph_variants(a):
                    out.add(b)
                    out |= plural_variants(b)
        return {x for x in out if x.strip()}

    return blow_up(wholes), blow_up(parts)


# --- corpus ----------------------------------------------------------------

HEADER_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)


class Corpus(object):
    """The content files, pre-canonicalised in two forms.

    tight  : all separators removed  -> collapses hyphenation/spacing variants
             (Bi-fascicular / Bifascicular / Bi fascicular all become one string)
    spaced : words preserved         -> enables word-level proximity matching
             for topics whose wording differs from the notes' wording
    """

    def __init__(self, paths):
        self.files = []
        vocab = set()
        for p in sorted(paths):
            with open(p, encoding="utf-8") as fh:
                raw = fh.read()
            sp = spaced_canon(raw)
            self.files.append({
                "name": os.path.basename(p),
                "raw": raw,
                "tight": sp.replace(" ", ""),
                "spaced": sp,
                "headers": [(m.group(2), m.start()) for m in HEADER_RE.finditer(raw)],
            })
            vocab.update(w for w in sp.split() if len(w) >= 6)
        self.vocab = vocab

    # -- helpers ------------------------------------------------------------

    @staticmethod
    def _significant(term):
        """Discriminating words of a topic, for proximity matching."""
        return [w for w in spaced_canon(term).split()
                if len(w) >= 4 and w not in STOPWORDS]

    @staticmethod
    def _positions(haystack, word):
        """Start offsets where `word` begins a word in `haystack` (spaced canon).

        Matching is prefix-style so a word matches its own inflections
        (parkinson -> parkinsons, child -> children).
        """
        out = []
        i = haystack.find(word)
        while i != -1:
            if i == 0 or haystack[i - 1] == " ":
                out.append(i)
            i = haystack.find(word, i + 1)
        return out

    @staticmethod
    def _min_window(lists):
        """Smallest span (chars) containing at least one offset from every list."""
        if not lists or any(not l for l in lists):
            return None
        merged = sorted((pos, idx) for idx, l in enumerate(lists) for pos in l)
        need = len(lists)
        counts = {}
        have = 0
        best = None
        lo = 0
        for hi in range(len(merged)):
            counts[merged[hi][1]] = counts.get(merged[hi][1], 0) + 1
            if counts[merged[hi][1]] == 1:
                have += 1
            while have == need:
                span = merged[hi][0] - merged[lo][0]
                if best is None or span < best:
                    best = span
                counts[merged[lo][1]] -= 1
                if counts[merged[lo][1]] == 0:
                    have -= 1
                lo += 1
        return best

    # -- match tiers --------------------------------------------------------

    def _contiguous(self, variants):
        """Longest variant first; stop at the first that matches anywhere.

        Stopping matters twice over. It keeps the reported occurrence count
        meaningful — accumulating across overlapping variants counts the same
        text several times — and it keeps a full 872-row --all run tractable,
        since the variant sets are large by design.
        """
        seen = set()
        ordered = []
        for v in sorted(variants, key=len, reverse=True):
            cv = canon(v)
            if len(cv) < MIN_PART_LEN or cv in seen:
                continue
            seen.add(cv)
            ordered.append((v, cv))
        for v, cv in ordered:
            hits = {}
            for f in self.files:
                n = f["tight"].count(cv)
                if n:
                    hits[f["name"]] = n
            if hits:
                return hits, v
        return {}, None

    def _acronyms(self, variants):
        """Short ALL-CAPS tokens (GCS, AVPU) matched case-sensitively on raw text,
        since they are below MIN_PART_LEN and would be noise if case-folded."""
        import re as _re
        hits, best = {}, None
        for v in variants:
            t = v.strip()
            if not (3 <= len(t) <= 6 and t.isupper() and t.isalpha()):
                continue
            pat = _re.compile(r"\b%s\b" % _re.escape(t))
            for f in self.files:
                n = len(pat.findall(f["raw"]))
                if n:
                    hits[f["name"]] = hits.get(f["name"], 0) + n
                    if best is None:
                        best = t
        return hits, best

    def _proximity(self, variants, window=90):
        """All significant words of the topic within `window` chars, ANY order.

        Catches the two commonest real-world mismatches between the CSV's
        wording and the notes' wording:
          * interposed text  -- "Extradural haematoma" vs
                                "Extradural (Epidural) Haematoma"
          * transposed words -- "Benign Positional Paroxysmal Vertigo" vs
                                "Benign Paroxysmal Positional Vertigo"
        Reported separately from a contiguous match so it can be audited.
        """
        best_words, hits = None, {}
        for v in sorted(variants, key=len, reverse=True):
            words = self._significant(v)
            if len(words) < 2:
                continue
            for f in self.files:
                lists = [self._positions(f["spaced"], w) for w in words]
                span = self._min_window(lists)
                if span is not None and span <= window:
                    hits[f["name"]] = hits.get(f["name"], 0) + 1
                    if best_words is None:
                        best_words = words
            if hits:
                break
        return hits, (" + ".join(best_words) if best_words else None)

    def _fuzzy(self, variants):
        """Single-word near-miss recovery, for CSV typos.

        "Tredelenburg's gait" is a misspelling of Trendelenburg in the checklist
        itself. Without this tier the row reads as a genuine gap forever.
        """
        import difflib
        for v in sorted(variants, key=len, reverse=True):
            words = self._significant(v)
            if not words:
                continue
            longest = max(words, key=len)
            if len(longest) < 7:
                continue
            if any(self._positions(f["spaced"], longest) for f in self.files):
                continue
            near = difflib.get_close_matches(longest, self.vocab, n=1, cutoff=0.85)
            if not near:
                continue
            repaired = [near[0] if w == longest else w for w in words]
            hits = {}
            for f in self.files:
                lists = [self._positions(f["spaced"], w) for w in repaired]
                span = self._min_window(lists)
                if span is not None and span <= 90:
                    hits[f["name"]] = hits.get(f["name"], 0) + 1
            if hits:
                return hits, "%s ~= %s (probable checklist typo)" % (longest, near[0])
        return {}, None

    def _headers_for(self, variants, hits):
        headers = []
        cvs = [canon(v) for v in variants if len(canon(v)) >= MIN_PART_LEN]
        for f in self.files:
            if f["name"] not in hits:
                continue
            for i, (htext, hpos) in enumerate(f["headers"]):
                ch = canon(htext)
                hs = spaced_canon(htext)
                match = any(cv in ch for cv in cvs)
                if not match:
                    for v in variants:
                        words = self._significant(v)
                        if len(words) >= 2 and all(self._positions(hs, w) for w in words):
                            match = True
                            break
                if match:
                    end = f["headers"][i + 1][1] if i + 1 < len(f["headers"]) else len(f["raw"])
                    headers.append((f["name"], htext, end - hpos))
        return headers

    def search(self, variants):
        """Tiered search. Returns (hits, matched_description, headers, tier).

        tier is one of: exact | proximity | fuzzy | acronym | ''  — always
        reported, so a weak match is never silently presented as a strong one.
        """
        for tier, fn in (("exact", self._contiguous),
                         ("proximity", self._proximity),
                         ("fuzzy", self._fuzzy),
                         ("acronym", self._acronyms)):
            hits, best = fn(variants)
            if hits:
                return hits, best, self._headers_for(variants, hits), tier
        return {}, None, [], ""


def load_rows(csv_path):
    with open(csv_path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def content_files(root, pattern):
    paths = [p for p in glob.glob(os.path.join(root, pattern))
             if os.path.basename(p) not in META_FILES]
    return sorted(paths)


# --- self-test -------------------------------------------------------------

def self_test():
    """Assert the variant generator handles the documented traps."""
    cases = [
        # (csv topic, string as it appears in the notes)
        ("Thalassemia (alpha and beta)", "α-thalassaemia"),
        ("Thalassemia (alpha and beta)", "β-thalassaemia"),
        ("Thalassemia (alpha and beta)", "Thalassaemia"),
        ("Multiple sclerosis", "Multiple Sclerosis"),
        ("Trigeminal neuralgia", "Trigeminal Neuralgia"),
        ("Bell’s palsy", "Bells palsy"),
        ("Bell’s palsy", "Bell's Palsy"),
        ("Bi-fascicular block", "Bifascicular block"),
        ("CHA2DS2-VASc", "CHA₂DS₂-VASc"),
        ("ABCD2 score", "ABCD² score"),
        ("Cauda equina*", "Cauda Equina"),
        ("Brain tumour types and presentation", "brain tumours"),
        ("Oesophageal varices", "Esophageal varices"),
        ("Diarrhoea", "diarrhea"),
        # The eight false MISSING results from the first Neurology validation
        # run. Every one was a search artifact, not a gap; each is kept here so
        # a future change to the variant generator cannot silently reintroduce it.
        ("Parkinson disease", "Parkinson's disease"),
        ("Guillain-Barre", "Guillain-Barre Syndrome (GBS)".replace("Barre", "Barr\u00e9")),
        ("Motor Neurone Disease", "Motor Neuron Disease (MND)"),
        ("Extradural haematoma", "Extradural (Epidural) Haematoma"),
        ("Benign Positional Paroxysmal Vertigo", "Benign paroxysmal positional vertigo (BPPV)"),
        ("Headache in a child", "persistent headache in any child <4 years old"),
        ("Tredelenburg\u2019s gait", "Trendelenburg's Sign and Gait"),
    ]
    failures = []
    for topic, appears_as in cases:
        # Build a one-file throwaway corpus containing only the phrase as the
        # notes actually write it, then run the real tiered search against it.
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            fp = os.path.join(td, "probe.md")
            with open(fp, "w", encoding="utf-8") as fh:
                fh.write("## Probe\n\nclinical text " + appears_as + " more text\n")
            c = Corpus([fp])
            wholes, parts = expand_topic(topic)
            hits, matched, _, tier = c.search(wholes)
            if not hits:
                hits, matched, _, tier = c.search(parts)
        ok = bool(hits)
        print("%-4s %-38s -> %-46s %s" % ("PASS" if ok else "FAIL", topic,
                                          appears_as[:46], tier or "-"))
        if not ok:
            failures.append((topic, appears_as))
    print()
    if failures:
        print("%d self-test FAILURE(S) — fix the variant generator before use." % len(failures))
        return 1
    print("All %d self-tests passed." % len(cases))
    return 0


# --- main ------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=None, help="notes directory (default: repo root)")
    ap.add_argument("--csv", default=None, help="checklist CSV (default: <dir>/checklist.csv)")
    ap.add_argument("--category", action="append", default=[],
                    help="exact category name (repeatable)")
    ap.add_argument("--all", action="store_true", help="run every category")
    ap.add_argument("--list-categories", action="store_true")
    ap.add_argument("--files", default="*.md",
                    help="glob limiting which content files count as present (default: *.md)")
    ap.add_argument("--topic", default=None, help="check a single ad-hoc topic string")
    ap.add_argument("--missing-only", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = args.dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = args.csv or os.path.join(root, CSV_NAME)
    if not os.path.exists(csv_path):
        sys.stderr.write("checklist not found: %s\n" % csv_path)
        return 2

    rows = load_rows(csv_path)

    if args.list_categories:
        counts = {}
        for r in rows:
            counts[r[CATEGORY_COL]] = counts.get(r[CATEGORY_COL], 0) + 1
        print("%d rows, %d categories\n" % (len(rows), len(counts)))
        for c in sorted(counts):
            print("%4d | %s" % (counts[c], c))
        return 0

    paths = content_files(root, args.files)
    if not paths:
        sys.stderr.write("no content files matched %s in %s\n" % (args.files, root))
        return 2
    corpus = Corpus(paths)

    if args.topic:
        targets = [{CATEGORY_COL: "(ad-hoc)", TOPIC_COL: args.topic, YIELD_COL: ""}]
        cats = ["(ad-hoc)"]
    else:
        all_cats = sorted(set(r[CATEGORY_COL] for r in rows))
        if args.all:
            cats = all_cats
        elif args.category:
            cats = []
            for c in args.category:
                if c in all_cats:
                    cats.append(c)
                else:
                    near = [a for a in all_cats if c.lower() in a.lower()]
                    if len(near) == 1:
                        print("note: '%s' -> '%s'" % (c, near[0]))
                        cats.append(near[0])
                    else:
                        sys.stderr.write("unknown category: %r\n" % c)
                        sys.stderr.write("candidates: %s\n" % (near or all_cats))
                        return 2
        else:
            sys.stderr.write("give --category, --all, --topic or --list-categories\n")
            return 2
        targets = None

    print("=" * 78)
    print(" csv_crosscheck.py")
    print(" checklist : %s" % csv_path)
    print(" corpus    : %d file(s) matching %r (meta files excluded)" % (len(paths), args.files))
    print("=" * 78)

    any_missing = False
    for cat in cats:
        crows = targets if targets else [r for r in rows if r[CATEGORY_COL] == cat]
        print("\n" + "-" * 78)
        print("CATEGORY: %s  (%d rows)" % (cat, len(crows)))
        print("-" * 78)

        missing, partial, found = [], [], []
        for r in crows:
            topic = r[TOPIC_COL]
            wholes, parts = expand_topic(topic)
            hits, matched, headers, tier = corpus.search(wholes)
            kind = "FOUND"
            if not hits:
                hits, matched, headers, tier = corpus.search(parts)
                kind = "PARTIAL" if hits else "MISSING"

            flags = []
            if tier and tier != "exact":
                flags.append(tier)
            if len(clean_topic(topic)) < GENERIC_LEN:
                flags.append("GENERIC")
            if headers:
                flags.append("header")
            entry = (topic, r.get(YIELD_COL, ""), kind, matched, hits, headers, flags)
            if kind == "MISSING":
                missing.append(entry)
            elif kind == "PARTIAL":
                partial.append(entry)
            else:
                found.append(entry)

        def show(entries, label):
            if not entries:
                return
            print("\n%s (%d)" % (label, len(entries)))
            for topic, yld, kind, matched, hits, headers, flags in entries:
                total = sum(hits.values())
                fl = (" [%s]" % ",".join(flags)) if flags else ""
                print("  %-52s %-7s %s%s" % (topic[:52], yld, kind, fl))
                if matched:
                    print("      matched         : %r  (%d occurrence(s) of THIS "
                          "variant in %d file(s))" % (matched, total, len(hits)))
                    top = sorted(hits.items(), key=lambda kv: -kv[1])[:4]
                    print("      files           : %s" % ", ".join("%s(%d)" % (f, n) for f, n in top))
                    if headers:
                        h = max(headers, key=lambda x: x[2])
                        print("      depth signal    : header %r in %s, section ~%d chars"
                              % (h[1][:60], h[0], h[2]))
                    else:
                        print("      depth signal    : NO matching header — mention only, "
                              "open the file and check depth (Step 3.3)")

        if not args.missing_only:
            show(found, "FOUND")
            show(partial, "PARTIAL — only a fragment of the row matched; verify the whole row")
        show(missing, "MISSING CANDIDATES — hand-verify each, see LIMITATIONS in file header")

        print("\nSummary for %s: %d found, %d partial, %d missing candidate(s)"
              % (cat, len(found), len(partial), len(missing)))
        if missing:
            any_missing = True

    print("\n" + "=" * 78)
    print(" Reminder: MISSING is a candidate list, not a gap list. FOUND proves the")
    print(" string exists, not that the topic is built to intern/RMO depth.")
    print("=" * 78)
    return 1 if any_missing else 0


if __name__ == "__main__":
    sys.exit(main())
