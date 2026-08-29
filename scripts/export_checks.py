#!/usr/bin/env python3
"""export_checks.py — render the open tracker rows as a source-grouped page.

What it does
------------
Reads every OPEN (⬜) row from `PENDING_GUIDELINE_CHECKS.md` and writes a
self-contained HTML page grouping each row under the Australian primary
source(s) that could settle it, so the backlog can be worked one source at a
time rather than one file at a time.

Rows are routed by matching source names in the row's own text. A row naming
more than one source appears under each, so the group totals exceed the row
count — the page says so.

MANUAL — the hand-routed exceptions
------------------------------------
Some rows name no matchable source (a policy question, a primary paper, an
evolving area). Those are routed by hand in the MANUAL dict rather than left
in an "Unassigned" bucket, which would defeat the point of grouping by
source. **When you add a tracker row that names no source, add it to MANUAL**
— the script prints a warning listing anything it could not route.

Keeping it current
------------------
The tracker is the single source of truth; this script only renders it. After
editing `PENDING_GUIDELINE_CHECKS.md`, re-run to regenerate. Rows are marked
"dose or threshold" when their text mentions a figure that changes what a
patient receives — those sort first in a batch-checking session.

Usage
-----
  scripts/export_checks.py                    # writes guideline-checks.html
  scripts/export_checks.py --out PATH.html    # write elsewhere

Exit status: 0 always.
"""
import argparse
import re, io, json, html, os
SRC=[("eTG — Therapeutic Guidelines", r"\beTG\b|Therapeutic Guidelines"),
 ("RANZCOG", r"\bRANZCOG\b"),
 ("RACGP — Red Book / HANDI", r"\bRACGP\b|Red Book|HANDI"),
 ("RCH Melbourne / Qld Children's", r"\bRCH\b|Royal Children|Queensland Children"),
 ("National Blood Authority", r"National Blood Authority|\bNBA\b"),
 ("ASCIA", r"\bASCIA\b"),
 ("ANZCOR", r"\bANZCOR\b"),
 ("Immunisation Handbook / ATAGI / CDNA", r"Immunisation Handbook|\bATAGI\b|\bCDNA\b|\bSoNG\b|NIP Schedule|National Immunisation"),
 ("eviQ / Cancer Australia", r"\beviQ\b|Cancer Australia|Cancer Council|BreastSurgANZ|\bNCCN\b"),
 ("State health guidelines (SA/Qld/Vic/NSW/WA)", r"SA Health|Queensland Clinical|Queensland Health|Safer Care Victoria|NSW Health|WA Health|Clinical Excellence|state/territory|state protocol|local protocol|state-variable|QLD|NSW typically"),
 ("ANZBA — burns", r"\bANZBA\b|Lund and Browder"),
 ("Austroads", r"\bAustroads\b"),
 ("KDIGO / Kidney Health Australia", r"\bKDIGO\b|Kidney Health"),
 ("APEG — paediatric endocrine", r"\bAPEG\b|Paediatric Endocrine"),
 ("RANZCP / COPE — mental health", r"\bRANZCP\b|\bCOPE\b|perinatal mental health guideline"),
 ("ASHM / STI Guidelines Australia", r"\bASHM\b|STI Guidelines"),
 ("ANZCA / ANZAAG", r"\bANZCA\b|ANZAAG"),
 ("Australian Injectable Drugs Handbook", r"Injectable Drugs Handbook"),
 ("APLS ANZ", r"\bAPLS\b"),
 ("Heart Foundation / Hypertension Australia", r"Heart Foundation|Hypertension Australia|Stroke Foundation"),
 ("MJA consensus statements", r"\bMJA\b"),
 ("AIFS / national policy", r"\bAIFS\b|National Plan|patient registration|Population Based Screening Framework|health\.gov\.au"),
 ("Primary literature", r"derivation paper|European Heart Journal|primary literature|the original paper|ConSEPT"),
]
# Rows whose source is unambiguous on reading but carries no matchable keyword.
# Routed by hand rather than left in an "unassigned" bucket, which would defeat
# the point of grouping by source.
MANUAL = {
 "A2": ["State health guidelines (SA/Qld/Vic/NSW/WA)"],
 "A3": ["ANZCA / ANZAAG"],
 "B1": ["Australian Diabetes Society / ADS-ADEA"],
 "B3": ["eTG — Therapeutic Guidelines"],
 "B4": ["eTG — Therapeutic Guidelines"],
 "B8": ["State health guidelines (SA/Qld/Vic/NSW/WA)"],
 "B11": ["RANZCR / imaging pathways"],
 "B19": ["Immunisation Handbook / ATAGI / CDNA"],
 "B22": ["Indigenous health — KICA / NACCHO"],
 "B31": ["PBS / MBS", "AIFS / national policy"],
 "B40": ["PBS / MBS"],
 "B45": ["Primary literature"],
 "B65": ["RCH Melbourne / Qld Children's"],
}

HIGH = re.compile(r"dose|dosing|mg|mcg|IU|mL|threshold|rate|infusion|regimen|anaphylax|adrenaline|DKA|cerebral oedema|sensitis|anti-D|resuscitat|emergen", re.I)

rows=[]
for l in io.open('PENDING_GUIDELINE_CHECKS.md',encoding='utf-8'):
    if not re.match(r"^\|\s*[AB]\d+\s*\|", l): continue
    p=[c.strip() for c in l.strip().strip('|').split('|')]
    if len(p)<4 or '⬜' not in p[-1]: continue
    body=" | ".join(p[2:-1])
    hits=[n for n,pat in SRC if re.search(pat, body)]
    src = sorted(set(hits) | set(MANUAL.get(p[0], [])))
    rows.append({"id":p[0],"files":p[1],"body":body,
                 "src":src or ["Unassigned — read the row to route it"],
                 "hi":bool(HIGH.search(body))})

groups={}
for r in rows:
    for s in r["src"]: groups.setdefault(s,[]).append(r)
order=sorted(groups, key=lambda k:(-len(groups[k]), k))

def md(t):
    t=html.escape(t)
    t=re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t=re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    t=re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    return t

def rowhtml(r):
    return f"""<article class="row{' hi' if r['hi'] else ''}">
<header><span class="rid">{html.escape(r['id'])}</span>{'<span class="flag">dose or threshold</span>' if r['hi'] else ''}</header>
<p class="files">{md(r['files'])}</p>
<p class="body">{md(r['body'])}</p>
</article>"""

secs=[]
for s in order:
    rs=groups[s]
    slug=re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")
    ids=" ".join(f'<a href="#{slug}">{s}<span>{len(rs)}</span></a>' for _ in [0])
    secs.append((slug,s,len(rs),"\n".join(rowhtml(r) for r in rs)))

nav="\n".join(f'<a href="#{sl}">{html.escape(n)}<span>{c}</span></a>' for sl,n,c,_ in secs)
body="\n".join(f'<section id="{sl}"><h2>{html.escape(n)}<span class="count">{c} {"row" if c==1 else "rows"}</span></h2>{h}</section>' for sl,n,c,h in secs)
nhi=sum(1 for r in rows if r["hi"])

page = f"""<title>Guideline Check Queue</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --ground:#f2f5f4; --surface:#ffffff; --ink:#12191c; --muted:#5b6b67;
  --line:#dde4e1; --accent:#0f6b5c; --accent-soft:#e4efeb; --flag:#a8620a; --flag-soft:#f8eddd;
  --shadow:0 1px 2px rgba(18,25,28,.05),0 8px 24px -16px rgba(18,25,28,.18);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground:#0e1413; --surface:#161e1c; --ink:#e6ece9; --muted:#93a49f;
    --line:#26322f; --accent:#5ec4ac; --accent-soft:#122b26; --flag:#e0a25c; --flag-soft:#2a1f12;
    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px -16px rgba(0,0,0,.6);
  }}
}}
:root[data-theme="dark"] {{
  --ground:#0e1413; --surface:#161e1c; --ink:#e6ece9; --muted:#93a49f;
  --line:#26322f; --accent:#5ec4ac; --accent-soft:#122b26; --flag:#e0a25c; --flag-soft:#2a1f12;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px -16px rgba(0,0,0,.6);
}}
*{{box-sizing:border-box}}
body{{background:var(--ground);color:var(--ink);
  font:400 16px/1.6 "Source Sans 3",ui-sans-serif,system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;margin:0}}
.wrap{{max-width:60rem;margin:0 auto;padding:clamp(1.75rem,4vw,3.5rem) clamp(1rem,4vw,2rem) 5rem}}
header.top{{border-bottom:2px solid var(--ink);padding-bottom:1.5rem;margin-bottom:2rem}}
.eyebrow{{font:500 .72rem/1 "IBM Plex Mono",ui-monospace,monospace;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent);margin:0 0 .9rem}}
h1{{font:400 clamp(2rem,5vw,3rem)/1.1 Newsreader,Georgia,serif;margin:0 0 .75rem;text-wrap:balance;letter-spacing:-.01em}}
.lede{{margin:0;max-width:62ch;color:var(--muted);font-size:1.05rem}}
.stats{{display:flex;flex-wrap:wrap;gap:.5rem 2.25rem;margin-top:1.5rem;
  font:500 .82rem/1 "IBM Plex Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums}}
.stats b{{color:var(--accent);font-weight:500}}
.stats .warn b{{color:var(--flag)}}
nav.index{{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 2.75rem}}
nav.index a{{display:inline-flex;align-items:center;gap:.5rem;text-decoration:none;color:var(--ink);
  background:var(--surface);border:1px solid var(--line);border-radius:2px;
  padding:.42rem .7rem;font-size:.84rem;transition:border-color .15s,color .15s}}
nav.index a:hover,nav.index a:focus-visible{{border-color:var(--accent);color:var(--accent)}}
nav.index a span{{font:500 .72rem/1 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted);
  font-variant-numeric:tabular-nums}}
section{{margin:0 0 3rem;scroll-margin-top:1.5rem}}
h2{{font:600 1.28rem/1.25 Newsreader,Georgia,serif;margin:0 0 1.1rem;padding-bottom:.55rem;
  border-bottom:1px solid var(--line);display:flex;justify-content:space-between;
  align-items:baseline;gap:1rem;text-wrap:balance}}
h2 .count{{font:400 .74rem/1 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted);
  white-space:nowrap;font-variant-numeric:tabular-nums}}
.row{{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:1rem 1.15rem;margin-bottom:.85rem;box-shadow:var(--shadow)}}
.row.hi{{border-left:3px solid var(--flag)}}
.row header{{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}}
.rid{{font:500 .78rem/1 "IBM Plex Mono",ui-monospace,monospace;letter-spacing:.04em;
  background:var(--accent-soft);color:var(--accent);padding:.24rem .5rem;border-radius:2px}}
.flag{{font:500 .68rem/1 "IBM Plex Mono",ui-monospace,monospace;letter-spacing:.08em;
  text-transform:uppercase;background:var(--flag-soft);color:var(--flag);padding:.24rem .5rem;border-radius:2px}}
.files{{margin:0 0 .55rem;font:400 .78rem/1.5 "IBM Plex Mono",ui-monospace,monospace;
  color:var(--muted);word-break:break-word}}
.files code{{background:none;padding:0;font-size:1em}}
.body{{margin:0;font-size:.95rem;max-width:70ch}}
.body strong{{font-weight:600}}
code{{font:400 .86em/1.4 "IBM Plex Mono",ui-monospace,monospace;
  background:var(--accent-soft);padding:.08em .32em;border-radius:2px;word-break:break-word}}
footer{{margin-top:3.5rem;padding-top:1.25rem;border-top:1px solid var(--line);
  color:var(--muted);font-size:.86rem;max-width:70ch}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>

<div class="wrap">
<header class="top">
  <p class="eyebrow">Grind Time · Phase 4 closed · coverage audit complete</p>
  <h1>Guideline checks awaiting a primary source</h1>
  <p class="lede">Every open row from <code>PENDING_GUIDELINE_CHECKS.md</code>, grouped by the source that settles it.
  Each row is a question the corpus could not answer without guideline access — not a known error left in place.
  Rows appear under every source that could resolve them, so the totals below exceed the row count. This is the final state of Phase 4: L1–L10, G1–G45, the 21-pair audit, the GBS check and the twelve-category coverage audit.</p>
  <div class="stats">
    <span><b>{len(rows)}</b> open rows</span>
    <span><b>{len(secs)}</b> sources</span>
    <span class="warn"><b>{nhi}</b> touch a dose or threshold</span>
  </div>
</header>
<nav class="index">{nav}</nav>
{body}
<footer>Generated from the tracker on 2026-08-29, after Phase 4 closed (L1–L10, G1–G45, the 21-pair audit and the GBS check).
Rows marked <em>dose or threshold</em> carry a number that changes what a patient receives — worth taking first.
Where a row says a figure was <em>removed rather than replaced</em>, the corpus now states no number at that point, so the entry is safe to read but incomplete until checked.</footer>
</div>
"""
_ap = argparse.ArgumentParser()
_ap.add_argument("--out", default="guideline-checks.html")
_args = _ap.parse_args()
io.open(_args.out, "w", encoding="utf-8").write(page)
_unrouted = [r["id"] for r in rows if r["src"] == ["Unassigned — read the row to route it"]]
if _unrouted:
    print("WARNING: %d row(s) matched no source and are not in MANUAL: %s"
          % (len(_unrouted), ", ".join(_unrouted)))
print("rows: %d | sources: %d | dose/threshold: %d" % (len(rows), len(secs), nhi))
print("wrote", _args.out)
