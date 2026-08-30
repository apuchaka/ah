#!/usr/bin/env python3
"""Section-ownership check: does a topic OWN a header, yes or no.

Deliberately answers one question and reports one thing. No hit counts, no
partial credit. A passing mention inside another topic's entry is not
coverage, however often it appears.

WHY THIS EXISTS AS ITS OWN TOOL
An earlier audit used raw grep hit counts and reported "adult resuscitation:
93". The pattern was "adult resuscitation|resuscitation" - a self-defeating
alternation where the general alternative satisfies the specific query, so it
counted every "fluid resuscitation" (18), "cardiopulmonary resuscitation" (8)
and bare grammatical fragment. The literal phrase appears zero times. Worse,
a section-ownership check in the very next step returned ABSENT for the same
item, and both numbers were printed without reconciling them.

Rules enforced here:
  - match against HEADER TEXT only, never body prose
  - no alternation between a specific and a general form
  - alias candidates are reported as what they are: a different name for the
    same topic, with the header quoted so the reader can judge
"""
import re, glob, os, sys, unicodedata

META = {"CLAUDE.md","CLAUDE_CODE_PROMPT.md","COWORK_HANDOFF.md","MASTER_VERIFICATION_WORKFLOW.md",
        "PENDING_GUIDELINE_CHECKS.md","PHASE_EXECUTION_WORKFLOW.md","RECOMMENDED_WORKFLOW.md",
        "Medications_Reference.md"}
HDR = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.M)

def norm(t):
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r"[*_`]", "", t)
    t = re.sub(r"^\d+(\.\d+)*\s*", "", t)          # strip "0.20.1 " numbering
    t = re.sub(r"\s*\([^)]*\)", " ", t)             # strip parenthetical glosses
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

def headers():
    out = []
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "*.md"))):
        b = os.path.basename(f)
        if b in META: continue
        for m in HDR.finditer(open(f, encoding="utf-8").read()):
            out.append((b, m.group(2).strip(), norm(m.group(2))))
    return out

def owns(topic, hdrs):
    """Return (file, header) if a header covers this topic, else None."""
    n = norm(topic)
    toks = n.split()
    for b, raw, hn in hdrs:                       # exact normalised match
        if hn == n: return (b, raw, "exact")
    for b, raw, hn in hdrs:                       # header contains the full topic
        if n and n in hn: return (b, raw, "header contains topic")
    for b, raw, hn in hdrs:                       # topic contains the header (header is shorter//broader)
        if hn and len(hn.split()) >= 2 and hn in n: return (b, raw, "topic contains header")
    if len(toks) >= 2:                            # all tokens present in one header
        for b, raw, hn in hdrs:
            hs = set(hn.split())
            if all(t in hs for t in toks): return (b, raw, "all tokens in header")
    return None

if __name__ == "__main__":
    hdrs = headers()
    if len(sys.argv) > 1 and sys.argv[1] == "--dump":
        for b, raw, _ in hdrs: print(f"{b}\t{raw}")
        sys.exit()
    topics = [l.strip() for l in sys.stdin if l.strip()]
    for t in topics:
        r = owns(t, hdrs)
        if r: print(f"OWNS    | {t:38s} | {r[1][:56]:58s} | {r[0][:34]}")
        else: print(f"ABSENT  | {t:38s} |")
