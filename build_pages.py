#!/usr/bin/env python3
"""Build the journal-style GitHub Pages article page (index.html) from
manuscript.md, following Raphael's series template (pages-template):
article header with badges/author/DOI slot, HTML full text in the main
column, sidebar with download box at the top, citation export, keywords,
article information and links. No DOI exists yet — the DOI slot states
that plainly and no citation field carries one.
Run: ~/workspace/venvs/pubtools/bin/python build_pages.py
"""
import html
import re

import markdown

TITLE = ("Loss of taste in possible viral infection: etiologies, pathogenesis, "
         "and the evidence for treatments")
SUBTITLE = "A Cochrane-level systematic review and meta-analysis where poolable"
AUTHOR = "Raphael Malikian"
AFFIL = "Independent Researcher, Palmdale, CA, USA"
EMAIL = "rtmalikian@gmail.com"
ORCID = "0009-0008-4326-4205"
REPO = "https://github.com/rtmalikian/viral-taste-loss-systematic-review"
PAGES = "https://rtmalikian.github.io/viral-taste-loss-systematic-review/"
PUBLISHED = "21 November 2026"
VERSION = "Version 1.0"
KEYWORDS = ["ageusia", "dysgeusia", "hypogeusia", "taste dysfunction",
            "gustatory", "SARS-CoV-2", "COVID-19", "viral infection",
            "pathogenesis", "systematic review", "meta-analysis", "GRADE"]
LICENCE = "Malikian Attribution — Non-Commercial Licence v1.0"

CITATION = (f"Malikian R. {TITLE}. {SUBTITLE}. {VERSION}, 2026. "
            f"GitHub: {REPO}")
BIBTEX = f"""@misc{{malikian2026tasteloss,
  author       = {{Malikian, Raphael}},
  title        = {{{TITLE}}},
  year         = {{2026}},
  version      = {{1.0}},
  url          = {{{REPO}}},
  note         = {{Cochrane-level systematic review; Zenodo DOI pending deposit}}
}}"""
RIS = f"""TY  - GEN
AU  - Malikian, Raphael
TI  - {TITLE}
PY  - 2026
UR  - {REPO}
ER  -"""


def body_html(md_text: str) -> str:
    start = md_text.index("## Abstract")
    body = md_text[start:]
    return markdown.markdown(body, extensions=["tables", "sane_lists"])


def main() -> None:
    md_text = open("manuscript.md").read()
    article = body_html(md_text)
    kw_meta = "\n".join(f'<meta name="citation_keyword" content="{html.escape(k)}">'
                        for k in KEYWORDS)
    kw_list = "".join(f"<li>{html.escape(k)}</li>" for k in KEYWORDS)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)} — Malikian R</title>
<meta name="citation_title" content="{html.escape(TITLE)}">
<meta name="citation_author" content="Malikian, Raphael">
<meta name="citation_publication_date" content="2026/11/21">
<meta name="citation_pdf_url" content="{REPO}/raw/main/manuscript.pdf">
{kw_meta}
<style>
:root{{--ink:#1a1a1a;--mut:#5a5a5a;--acc:#7a1f1f;--line:#ddd;--bg:#faf8f5}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:var(--bg);line-height:1.55}}
.wrap{{max-width:1180px;margin:0 auto;padding:24px 18px 64px}}
.badges span{{display:inline-block;border:1px solid var(--acc);color:var(--acc);border-radius:3px;padding:1px 8px;font-size:12px;margin-right:6px;font-family:Helvetica,Arial,sans-serif}}
h1{{font-size:30px;line-height:1.25;margin:14px 0 4px}}h2.sub{{font-size:19px;font-weight:normal;color:var(--mut);margin:0 0 14px}}
.author{{font-size:16px}}.meta{{color:var(--mut);font-size:14px;font-family:Helvetica,Arial,sans-serif}}
.grid{{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:34px;margin-top:22px}}
@media(max-width:860px){{.grid{{grid-template-columns:1fr}}}}
article h2{{font-size:22px;border-bottom:2px solid var(--acc);padding-bottom:4px;margin-top:34px}}
article h3{{font-size:18px;margin-top:26px}}article table{{border-collapse:collapse;width:100%;font-size:13.5px;margin:14px 0}}
article th,article td{{border:1px solid var(--line);padding:5px 7px;vertical-align:top}}article th{{background:#f0ebe4}}
article img{{max-width:100%}}aside .box{{border:1px solid var(--line);background:#fff;padding:14px 16px;margin-bottom:18px}}
aside h3{{margin:0 0 8px;font-size:15px;font-family:Helvetica,Arial,sans-serif;text-transform:uppercase;letter-spacing:.04em}}
aside p,aside li{{font-size:14px}}aside ul{{margin:6px 0;padding-left:18px}}
.dl a.btn{{display:block;background:var(--acc);color:#fff;text-align:center;padding:10px;border-radius:4px;text-decoration:none;font-family:Helvetica,Arial,sans-serif;margin-bottom:8px}}
.dl a.alt{{background:#fff;color:var(--acc);border:1px solid var(--acc)}}
pre{{white-space:pre-wrap;font-size:11.5px;background:#f6f2ec;padding:8px}}
button.copy{{font-size:12px;cursor:pointer}}
footer{{margin-top:44px;border-top:1px solid var(--line);padding-top:14px;color:var(--mut);font-size:13.5px}}
</style>
</head>
<body>
<div class="wrap">
<header>
<div class="badges"><span>Systematic Review</span><span>Open Access</span><span>{VERSION}</span><span>Cochrane-Level — Not a Cochrane Review</span></div>
<h1>{html.escape(TITLE)}</h1>
<h2 class="sub">{html.escape(SUBTITLE)}</h2>
<p class="author"><strong>{AUTHOR}</strong> — <a href="mailto:{EMAIL}">{EMAIL}</a> · ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a></p>
<p class="meta">{AFFIL}<br>
Published {PUBLISHED} · {VERSION}<br>
DOI: pending Zenodo deposit — no DOI exists yet and none is claimed.<br>
Licence: {LICENCE} (see the repository LICENSE.md).<br>
Registration: protocol locked 20 November 2026; not PROSPERO-registered — no registration number exists and none is claimed.</p>
</header>
<div class="grid">
<article>
{article}
</article>
<aside>
<div class="box dl">
<h3>Download</h3>
<a class="btn" href="{REPO}/raw/main/manuscript.pdf">Download PDF (full article)</a>
<a class="btn alt" href="{REPO}/raw/main/manuscript.docx">Download DOCX</a>
<a class="btn alt" href="{REPO}/raw/main/manuscript.md">Markdown source</a>
<a class="btn alt" href="{REPO}/raw/main/data/extraction_settled_full.csv">Settled extraction dataset (CSV)</a>
<a class="btn alt" href="{REPO}/tree/main/code">Analysis code</a>
<p>One click — no sign-up, no paywall.</p>
</div>
<div class="box">
<h3>Key findings</h3>
<ul>
<li>363 studies included (362 unique publications); 5,988 records retrieved.</li>
<li>Acute taste dysfunction in SARS-CoV-2: pooled 37.7% (95% CI 32.9 to 42.7; 137 studies, 155,010 participants); prediction interval 5.3 to 86.7% — all pooled evidence is SARS-CoV-2.</li>
<li>Complete recovery pooled at 87.4% within 4 weeks, 85.2% at &gt;4–12 weeks, 87.8% beyond 12 weeks (different study sets).</li>
<li>Only 23 studies tested any treatment; no treatment can be recommended for or against.</li>
<li>GRADE certainty very low for most outcomes.</li>
</ul>
</div>
<div class="box">
<h3>Cite this article</h3>
<p>{html.escape(CITATION)}</p>
<p><strong>BibTeX</strong> <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('bib').innerText)">Copy</button></p>
<pre id="bib">{html.escape(BIBTEX)}</pre>
<p><strong>RIS</strong> <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('ris').innerText)">Copy</button></p>
<pre id="ris">{html.escape(RIS)}</pre>
</div>
<div class="box">
<h3>Keywords</h3>
<ul>{kw_list}</ul>
</div>
<div class="box">
<h3>Article information</h3>
<p>Peer review: multi-agent pre-submission peer review (Gates 0–6 plus a feedback loop) under the author's accountability; the full record, including every reviewer item and its closure, is in the repository's peer-review folder. This was internal pre-submission review, not journal peer review.</p>
<p>Version history: v1.0, {PUBLISHED} (first public version).</p>
<p>Funding: none. Conflicts of interest: none.</p>
<p>Methods: Cochrane Handbook v6.5; PRISMA 2020 and PRISMA-S; GRADE. Carried out by a multi-agent LLM team with the author accountable for every number (see the team log in the repository).</p>
</div>
<div class="box">
<h3>Links</h3>
<ul>
<li><a href="{REPO}">GitHub repository</a></li>
<li>Zenodo record: pending deposit (no DOI yet)</li>
<li><a href="https://rtmalikian.github.io/systematic-reviews/">Systematic reviews hub</a></li>
<li><a href="https://orcid.org/{ORCID}">ORCID</a></li>
</ul>
</div>
</aside>
</div>
<footer>
<p>© 2026 Raphael Malikian. Published under the {LICENCE}: free for non-profit, academic, personal and other non-commercial use with acknowledgement; commercial use by separate licence — rtmalikian@gmail.com. This review makes no clinical or medication recommendation.</p>
</footer>
</div>
</body>
</html>"""
    open("index.html", "w").write(page)
    print("wrote index.html", len(page), "bytes")


if __name__ == "__main__":
    main()
