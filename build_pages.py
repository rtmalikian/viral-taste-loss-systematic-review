#!/usr/bin/env python3
"""Build the GitHub Pages article page (index.html) from manuscript.md as a
typical journal article page (PLOS/BMJ-style), re-presenting the manuscript's
content without rewriting it:

- series masthead band in the hub's visual identity (RM://NEON, Systematic
  Reviews hub) with a link back to the hub;
- article-type label, H1 title, author line, and a meta line carrying the
  verified Zenodo DOI;
- two-column layout (single column on mobile): main column + right sidebar.
  Sidebar order: Download (PDF button at the TOP), Cite this article
  (formatted citation + BibTeX + RIS), Article information, Contents,
  Keywords, Links;
- main column: structured Abstract in a shaded box, Plain language summary,
  Key findings box, then the full text with styled section headings, zebra
  tables with a header band, and figures with numbered captions;
- serif body, navy/grey journal scheme, print stylesheet;
- Highwire Press / Dublin Core scholar meta tags in the head.

Run: ~/workspace/venvs/pubtools/bin/python build_pages.py
"""
import html
import re

import markdown

TITLE = ("Loss of taste in possible viral infection: etiologies, pathogenesis, "
         "and the evidence for treatments")
SUBTITLE = "A Cochrane-level systematic review and meta-analysis where poolable"
ARTICLE_TYPE = "Systematic Review &amp; Meta-analysis"
AUTHOR = "Raphael Malikian"
AFFIL = "Independent Researcher, Palmdale, CA, USA"
EMAIL = "rtmalikian@gmail.com"
ORCID = "0009-0008-4326-4205"
REPO = "https://github.com/rtmalikian/viral-taste-loss-systematic-review"
PAGES = "https://rtmalikian.github.io/viral-taste-loss-systematic-review/"
HUB = "https://rtmalikian.github.io/systematic-reviews/"
DOI = "10.5281/zenodo.24418147"
DOI_URL = f"https://doi.org/{DOI}"
ZENODO_RECORD = "https://zenodo.org/records/24418147"
PUBLISHED = "21 November 2026"
PUBLISHED_ISO = "2026/11/21"
VERSION = "Version 1.0"
KEYWORDS = ["ageusia", "dysgeusia", "hypogeusia", "taste dysfunction",
            "gustatory", "SARS-CoV-2", "COVID-19", "viral infection",
            "pathogenesis", "systematic review", "meta-analysis", "GRADE"]
LICENCE = "Malikian Attribution — Non-Commercial Licence v1.0"

CITATION = (f"Malikian R. {TITLE}. {VERSION}; 2026. "
            f"DOI: {DOI}")
BIBTEX = f"""@misc{{malikian2026tasteloss,
  author       = {{Malikian, Raphael}},
  title        = {{{TITLE}}},
  year         = {{2026}},
  version      = {{1.0}},
  publisher    = {{Zenodo}},
  doi          = {{{DOI}}},
  url          = {{{DOI_URL}}},
  note         = {{Cochrane-level systematic review and meta-analysis where poolable}}
}}"""
RIS = f"""TY  - GEN
AU  - Malikian, Raphael
TI  - {TITLE}
PY  - 2026
DO  - {DOI}
UR  - {DOI_URL}
ER  -"""

KEY_FINDINGS = [
    "363 studies included (362 unique publications); 5,988 records retrieved.",
    "Acute taste dysfunction in SARS-CoV-2: pooled 37.7% (95% CI 32.9 to 42.7; "
    "137 studies, 155,010 participants); prediction interval 5.3 to 86.7% — "
    "all pooled evidence is SARS-CoV-2.",
    "Complete recovery pooled at 87.4% within 4 weeks, 85.2% at &gt;4–12 weeks, "
    "87.8% beyond 12 weeks (different study sets).",
    "Only 23 studies tested any treatment; no treatment can be recommended "
    "for or against.",
    "GRADE certainty very low for most outcomes.",
]

EXTS = ["tables", "sane_lists", "toc"]


def render(md_text: str) -> str:
    return markdown.markdown(md_text, extensions=EXTS)


def wrap_figures(html_text: str) -> str:
    """Turn lone-image paragraphs into <figure> with the alt text as caption."""
    pat = re.compile(
        r'<p><img alt="([^"]*)" src="([^"]*)"(?:\s*/)?></p>')

    def repl(m):
        cap, src = m.group(1), m.group(2)
        return (f'<figure><img alt="{cap}" src="{src}">'
                f'<figcaption>{cap}</figcaption></figure>')

    return pat.sub(repl, html_text)


def h2_sections(html_text: str):
    """Return [(id, title)] for every level-2 heading, in order."""
    return re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html_text)


def main() -> None:
    md_text = open("manuscript.md").read()
    abs_i = md_text.index("## Abstract")
    pls_i = md_text.index("## Plain language summary")
    sof_i = md_text.index("## Summary of findings")
    abstract_html = wrap_figures(render(md_text[abs_i:pls_i]))
    pls_html = wrap_figures(render(md_text[pls_i:sof_i]))
    body_html = wrap_figures(render(md_text[sof_i:]))

    contents = []
    for chunk in (abstract_html, pls_html, body_html):
        contents.extend(h2_sections(chunk))
    contents_html = "".join(
        f'<li><a href="#{hid}">{title}</a></li>' for hid, title in contents)

    kw_meta = "\n".join(
        f'<meta name="citation_keyword" content="{html.escape(k)}">'
        for k in KEYWORDS)
    kw_list = "".join(f"<li>{html.escape(k)}</li>" for k in KEYWORDS)
    findings_list = "".join(f"<li>{f}</li>" for f in KEY_FINDINGS)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)} — Malikian R</title>
<link rel="canonical" href="{PAGES}">
<meta name="description" content="{html.escape(TITLE)}. {SUBTITLE}. By Raphael Malikian. Zenodo DOI {DOI}.">
<meta name="citation_title" content="{html.escape(TITLE)}">
<meta name="citation_author" content="Malikian, Raphael">
<meta name="citation_publication_date" content="{PUBLISHED_ISO}">
<meta name="citation_doi" content="{DOI}">
<meta name="citation_pdf_url" content="{REPO}/raw/main/manuscript.pdf">
<meta name="citation_publisher" content="Zenodo">
<meta name="citation_language" content="en">
{kw_meta}
<meta name="DC.title" content="{html.escape(TITLE)}">
<meta name="DC.creator" content="Raphael Malikian">
<meta name="DC.date" content="2026-11-21">
<meta name="DC.identifier" content="{DOI_URL}">
<meta name="DC.type" content="Text">
<meta name="DC.rights" content="{LICENCE}">
<meta property="og:title" content="{html.escape(TITLE)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{PAGES}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{{--navy:#14335c;--navy2:#1d4e89;--ink:#1a202c;--mut:#5a6572;--line:#d7dde5;
--shade:#eef2f7;--boxbg:#f7f8f5;--void:#0a0018;--pink2:#ff71ce;--cyan:#01cdfe;--green:#05ffa1}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:#fff;line-height:1.62}}
.masthead{{background:var(--void);color:#f4f0ff;padding:14px 0 12px;border-bottom:3px solid var(--navy)}}
.masthead .wrap{{display:flex;align-items:center;gap:20px;flex-wrap:wrap}}
.logo{{font-family:Orbitron,sans-serif;font-weight:900;letter-spacing:.12em;color:#fff;text-decoration:none;font-size:19px}}
.logo span{{color:var(--pink2)}}
.series{{font-family:'JetBrains Mono',monospace;color:var(--green);font-size:12px;letter-spacing:.16em;text-transform:uppercase}}
.masthead nav{{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:12.5px}}
.masthead nav a{{color:var(--cyan);text-decoration:none}}
.masthead nav a:hover{{text-decoration:underline}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 20px}}
.article-head{{padding:30px 0 6px}}
.arttype{{font-family:Helvetica,Arial,sans-serif;font-size:12.5px;font-weight:bold;letter-spacing:.14em;text-transform:uppercase;color:var(--navy2);margin:0 0 10px}}
h1{{font-size:31px;line-height:1.24;margin:0 0 6px;color:#0d2138}}
.standfirst{{font-size:18px;color:var(--mut);margin:0 0 16px;font-style:italic}}
.author{{font-size:16.5px;margin:0 0 4px}}
.author strong{{color:#0d2138}}
.affil{{color:var(--mut);font-size:14.5px;margin:0 0 10px;font-family:Helvetica,Arial,sans-serif}}
.metaline{{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:9px 0;font-family:Helvetica,Arial,sans-serif;font-size:13.5px;color:#33404f;margin:14px 0 4px}}
.metaline a{{color:var(--navy2)}}
.grid{{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:38px;margin-top:20px;padding-bottom:10px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}aside{{order:-1}}}}
article h2{{font-size:21.5px;color:var(--navy);border-bottom:2px solid var(--navy);padding-bottom:4px;margin:34px 0 12px}}
article h3{{font-size:17.5px;color:#0d2138;margin:26px 0 8px}}
article h4{{font-size:15.5px;color:#0d2138;margin:20px 0 6px}}
article p{{margin:0 0 11px}}
article table{{border-collapse:collapse;width:100%;font-size:13px;margin:14px 0;line-height:1.45}}
article th{{background:var(--navy);color:#fff;text-align:left;padding:6px 8px;border:1px solid var(--navy)}}
article td{{border:1px solid var(--line);padding:5px 8px;vertical-align:top}}
article tbody tr:nth-child(even) td{{background:#f2f5f8}}
article figure{{margin:20px 0;text-align:center}}
article figure img{{max-width:100%;border:1px solid var(--line)}}
article figcaption{{font-size:13.5px;color:#33404f;margin-top:7px;text-align:left;font-family:Helvetica,Arial,sans-serif}}
.abstract-box{{background:var(--shade);border:1px solid #c9d6e4;border-left:5px solid var(--navy);padding:16px 20px 8px;margin:6px 0 8px}}
.abstract-box h2{{border:none;color:var(--navy);font-size:15px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 10px;padding:0;font-family:Helvetica,Arial,sans-serif}}
.keyfindings{{background:var(--boxbg);border:1px solid var(--line);border-top:4px solid var(--navy);padding:14px 20px 6px;margin:20px 0}}
.keyfindings h2{{border:none;color:var(--navy);font-size:15px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 8px;padding:0;font-family:Helvetica,Arial,sans-serif}}
.keyfindings ul{{margin:4px 0 10px;padding-left:20px}}
.keyfindings li{{margin-bottom:6px}}
aside .box{{border:1px solid var(--line);background:#fff;padding:14px 16px;margin-bottom:18px}}
aside h3{{margin:0 0 9px;font-size:13.5px;font-family:Helvetica,Arial,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--navy)}}
aside p,aside li{{font-size:13.5px}}
aside ul{{margin:6px 0;padding-left:18px}}
aside ul.contents{{list-style:none;padding-left:0}}
aside ul.contents li{{margin-bottom:5px}}
aside ul.contents a{{color:var(--navy2);text-decoration:none}}
aside ul.contents a:hover{{text-decoration:underline}}
.dl a.btn{{display:block;background:var(--navy);color:#fff;text-align:center;padding:11px;border-radius:4px;text-decoration:none;font-family:Helvetica,Arial,sans-serif;font-weight:bold;margin-bottom:8px}}
.dl a.btn:hover{{background:var(--navy2)}}
.dl a.alt{{background:#fff;color:var(--navy);border:1px solid var(--navy);font-weight:normal}}
.dl p{{color:var(--mut);margin:6px 0 0}}
pre{{white-space:pre-wrap;font-size:11px;background:#f6f2ec;padding:8px;line-height:1.4}}
button.copy{{font-size:12px;cursor:pointer}}
footer{{margin-top:40px;border-top:1px solid var(--line);padding:16px 0 34px;color:var(--mut);font-size:13.5px}}
footer a{{color:var(--navy2)}}
@media print{{
 .masthead,aside,button.copy{{display:none}}
 .grid{{grid-template-columns:1fr}}
 body{{font-size:11pt;line-height:1.5}}
 a{{color:#000;text-decoration:none}}
 article h2{{break-after:avoid}} article table,article figure{{break-inside:avoid}}
}}
</style>
</head>
<body>
<div class="masthead"><div class="wrap">
<a class="logo" href="https://rtmalikian.github.io/">RM<span>://</span>NEON</a>
<span class="series">Systematic Reviews · Cochrane-Level · Built in Public</span>
<nav><a href="{HUB}">&#8592; All reviews — Systematic Reviews Hub</a></nav>
</div></div>
<div class="wrap">
<header class="article-head">
<p class="arttype">{ARTICLE_TYPE}</p>
<h1>{html.escape(TITLE)}</h1>
<p class="standfirst">{SUBTITLE}</p>
<p class="author"><strong>{AUTHOR}</strong></p>
<p class="affil">{AFFIL} · Corresponding author: <a href="mailto:{EMAIL}">{EMAIL}</a> · ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a></p>
<p class="metaline">Published {PUBLISHED} &middot; {VERSION} &middot; DOI: <a href="{DOI_URL}">{DOI_URL}</a> &middot; Licence: {LICENCE}</p>
</header>
<div class="grid">
<article>
<section class="abstract-box">
{abstract_html}
</section>
{pls_html}
<section class="keyfindings"><h2>Key findings</h2><ul>{findings_list}</ul></section>
{body_html}
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
<h3>Cite this article</h3>
<p>{html.escape(CITATION)}</p>
<p><strong>BibTeX</strong> <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('bib').innerText)">Copy</button></p>
<pre id="bib">{html.escape(BIBTEX)}</pre>
<p><strong>RIS</strong> <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('ris').innerText)">Copy</button></p>
<pre id="ris">{html.escape(RIS)}</pre>
</div>
<div class="box">
<h3>Article information</h3>
<p>Protocol locked: 20 November 2026.<br>
Published: {PUBLISHED} ({VERSION}).</p>
<p>Funding: none. Conflicts of interest: none.</p>
<p>Correspondence: {AUTHOR}, <a href="mailto:{EMAIL}">{EMAIL}</a>, Palmdale, CA, USA. ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a>.</p>
<p>Registration: protocol locked 20 November 2026; not PROSPERO-registered — no registration number exists and none is claimed.</p>
<p>Peer review: multi-agent pre-submission peer review (Gates 0–6 plus a feedback loop) under the author's accountability; the full record, including every reviewer item and its closure, is in the repository's peer-review folder. This was internal pre-submission review, not journal peer review.</p>
<p>Methods: Cochrane Handbook v6.5; PRISMA 2020 and PRISMA-S; GRADE. Carried out by a multi-agent LLM team with the author accountable for every number (see the team log in the repository).</p>
</div>
<div class="box">
<h3>Contents</h3>
<ul class="contents">{contents_html}</ul>
</div>
<div class="box">
<h3>Keywords</h3>
<ul>{kw_list}</ul>
</div>
<div class="box">
<h3>Links</h3>
<ul>
<li><a href="{REPO}">GitHub repository</a></li>
<li><a href="{ZENODO_RECORD}">Zenodo record</a> (DOI: <a href="{DOI_URL}">{DOI}</a>)</li>
<li><a href="{HUB}">Systematic reviews hub</a></li>
<li><a href="https://orcid.org/{ORCID}">ORCID</a></li>
</ul>
</div>
</aside>
</div>
<footer>
<p>© 2026 Raphael Malikian. Published under the {LICENCE}: free for non-profit, academic, personal and other non-commercial use with acknowledgement; commercial use by separate licence — rtmalikian@gmail.com. This review makes no clinical or medication recommendation. DOI: <a href="{DOI_URL}">{DOI_URL}</a></p>
</footer>
</div>
</body>
</html>"""
    open("index.html", "w").write(page)
    print("wrote index.html", len(page), "bytes;",
          len(contents), "contents entries")


if __name__ == "__main__":
    main()
