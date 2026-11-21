#!/usr/bin/env python3
"""Build the GitHub Pages article page (index.html) from manuscript.md as a
standard journal article page (PLOS Medicine / BMJ benchmark), re-presenting
the manuscript's content without rewriting it:

- journal masthead: serif wordmark with thin rules above/below and a simple
  nav row (Browse / About / Systematic Reviews Hub / GitHub); no hero, no
  gradients;
- breadcrumb line, article-type label and an Open Access marker;
- article header block: large serif title, author with superscript
  affiliation number, affiliation line, corresponding author, published
  line, full citation line, DOI as a link;
- action row: Download PDF (primary), Download DOCX, Print, Cite, Share;
- Abstract in a pale bordered panel (the manuscript's bold run-in labels);
- two-column body: numbered main section headings, booktabs-style tables
  (horizontal rules only), figures with numbered legends; sidebar rail with
  Download box (PDF first), Cite box, Article information, Contents, Links;
- References as a numbered list with hanging indents;
- journal footer with the standard open-access licence sentence;
- white background, ~1200px max width, navy/grey palette, serif body;
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
SERIES = "Systematic Reviews"

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

# Main sections that carry numbers, by heading id (toc slug), in order.
NUMBERED = ["background", "objectives", "methods", "results", "discussion",
            "authors-conclusions"]

EXTS = ["tables", "sane_lists", "toc"]


def render(md_text: str) -> str:
    return markdown.markdown(md_text, extensions=EXTS)


def wrap_figures(html_text: str) -> str:
    """Lone-image paragraphs become <figure> with the alt text as legend."""
    pat = re.compile(r'<p><img alt="([^"]*)" src="([^"]*)"(?:\s*/)?></p>')

    def repl(m):
        cap, src = m.group(1), m.group(2)
        return (f'<figure><img alt="{cap}" src="{src}">'
                f'<figcaption>{cap}</figcaption></figure>')

    return pat.sub(repl, html_text)


def number_sections(html_text: str) -> str:
    """Prepend section numbers to the principal H2 headings."""
    for i, hid in enumerate(NUMBERED, start=1):
        html_text = re.sub(
            rf'(<h2 id="{hid}">)',
            rf'\g<1><span class="secno">{i}</span> ',
            html_text, count=1)
    return html_text


def number_references(html_text: str) -> str:
    """Convert the References bullet list to a numbered list."""
    ref_i = html_text.find('<h2 id="references">')
    if ref_i < 0:
        return html_text
    app_i = html_text.find('<h2 id="appendix-a', ref_i)
    end = app_i if app_i > 0 else len(html_text)
    chunk = html_text[ref_i:end]
    chunk = chunk.replace("<ul>", '<ol class="refs">', 1)
    chunk = chunk.replace("</ul>", "</ol>", 1)
    return html_text[:ref_i] + chunk + html_text[end:]


def h2_sections(html_text: str):
    return re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html_text)


def main() -> None:
    md_text = open("manuscript.md").read()
    abs_i = md_text.index("## Abstract")
    pls_i = md_text.index("## Plain language summary")
    sof_i = md_text.index("## Summary of findings")
    abstract_html = wrap_figures(render(md_text[abs_i:pls_i]))
    pls_html = wrap_figures(render(md_text[pls_i:sof_i]))
    body_html = number_references(
        number_sections(wrap_figures(render(md_text[sof_i:]))))

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
    share_url = ("https://twitter.com/intent/tweet?text="
                 + html.escape(TITLE.replace(" ", "%20"))
                 + "&url=" + PAGES)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)} | {SERIES}</title>
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
<style>
:root{{--navy:#14406e;--navy2:#1d5aa8;--ink:#1a1a1a;--mut:#5c6670;--line:#d9dee4;
--rule:#9aa7b4;--panel:#f7f9fb;--boxbg:#fbfbf8}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--ink);background:#fff;line-height:1.6}}
.wrap{{max-width:1200px;margin:0 auto;padding:0 22px}}
a{{color:var(--navy2)}}
/* --- journal masthead --- */
.masthead{{border-top:5px solid var(--navy);border-bottom:1px solid var(--ink);padding:20px 0 14px}}
.wordmark{{font-size:37px;font-weight:bold;letter-spacing:.01em;color:#0e2a47;line-height:1.05}}
.mast-sub{{font-family:Helvetica,Arial,sans-serif;font-size:12.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--mut);margin-top:5px}}
.journalnav{{border-bottom:1px solid var(--line)}}
.journalnav .wrap{{display:flex;gap:26px;padding-top:8px;padding-bottom:8px}}
.journalnav a{{font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:bold;letter-spacing:.06em;text-transform:uppercase;color:#24313d;text-decoration:none}}
.journalnav a:hover{{color:var(--navy2);text-decoration:underline}}
/* --- breadcrumb / type --- */
.crumb{{font-family:Helvetica,Arial,sans-serif;font-size:12.5px;color:var(--mut);margin:18px 0 0}}
.crumb a{{color:var(--mut);text-decoration:none}} .crumb a:hover{{text-decoration:underline}}
.typerow{{display:flex;align-items:center;gap:12px;margin:10px 0 0;flex-wrap:wrap}}
.arttype{{font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:bold;letter-spacing:.13em;text-transform:uppercase;color:var(--navy)}}
.oa{{font-family:Helvetica,Arial,sans-serif;font-size:11.5px;font-weight:bold;letter-spacing:.08em;text-transform:uppercase;color:#14632d;border:1px solid #14632d;border-radius:3px;padding:2px 8px}}
/* --- article header --- */
.article-head{{border-bottom:2px solid var(--ink);padding-bottom:16px}}
h1{{font-size:33px;line-height:1.22;margin:14px 0 8px;color:#101c28;font-weight:bold}}
.standfirst{{font-size:17.5px;color:#3c4753;margin:0 0 18px}}
.authors{{font-size:17px;margin:0 0 3px}}
.authors sup{{font-size:11px}}
.affil{{font-size:14px;color:#3c4753;margin:0 0 3px}}
.corr{{font-size:14px;color:#3c4753;margin:0 0 12px}}
.publine{{font-family:Helvetica,Arial,sans-serif;font-size:13.5px;color:#24313d;margin:0 0 5px}}
.citeline{{font-size:14.5px;color:#24313d;margin:0}}
/* --- action row --- */
.actions{{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0 4px}}
.actions a,.actions button{{font-family:Helvetica,Arial,sans-serif;font-size:13.5px;font-weight:bold;text-decoration:none;border:1px solid var(--navy);border-radius:3px;padding:8px 16px;color:var(--navy);background:#fff;cursor:pointer}}
.actions a.primary{{background:var(--navy);color:#fff}}
.actions a:hover,.actions button:hover{{background:#e8eef5}}
.actions a.primary:hover{{background:var(--navy2)}}
/* --- layout --- */
.grid{{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:40px;margin-top:22px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
/* --- article body --- */
article h2{{font-size:21px;color:#101c28;border-bottom:1px solid var(--rule);padding-bottom:5px;margin:36px 0 12px}}
article h2 .secno{{color:var(--navy)}}
article h3{{font-size:17px;color:#101c28;margin:26px 0 8px}}
article h4{{font-size:15px;color:#101c28;margin:20px 0 6px}}
article p{{margin:0 0 11px}}
article table{{border-collapse:collapse;width:100%;font-size:13px;margin:16px 0;line-height:1.45}}
article th{{background:none;color:var(--ink);text-align:left;font-weight:bold;padding:6px 8px;border-top:2.5px solid #101c28;border-bottom:1px solid #101c28}}
article td{{border:none;padding:5px 8px;vertical-align:top}}
article tbody tr:last-child td{{border-bottom:2.5px solid #101c28}}
article figure{{margin:22px 0}}
article figure img{{max-width:100%;border:1px solid var(--line)}}
article figcaption{{font-size:13.5px;color:#24313d;margin-top:7px;font-family:Helvetica,Arial,sans-serif;line-height:1.5}}
.abstract-panel{{background:var(--panel);border:1px solid var(--line);padding:16px 22px 8px;margin:4px 0 10px}}
.abstract-panel h2{{border:none;font-size:14px;letter-spacing:.13em;text-transform:uppercase;color:var(--navy);margin:0 0 10px;padding:0;font-family:Helvetica,Arial,sans-serif}}
.keyfindings{{background:var(--boxbg);border:1px solid var(--line);border-top:3px solid var(--navy);padding:13px 20px 5px;margin:20px 0}}
.keyfindings h2{{border:none;font-size:13.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--navy);margin:0 0 8px;padding:0;font-family:Helvetica,Arial,sans-serif}}
.keyfindings ul{{margin:4px 0 10px;padding-left:20px}} .keyfindings li{{margin-bottom:6px}}
ol.refs{{padding-left:0;list-style-position:outside;margin-left:2.1em}}
ol.refs li{{margin-bottom:7px;padding-left:.4em}}
/* --- sidebar rail --- */
aside .box{{border:1px solid var(--line);background:#fff;padding:14px 16px;margin-bottom:18px}}
aside h3{{margin:0 0 9px;font-size:13px;font-family:Helvetica,Arial,sans-serif;text-transform:uppercase;letter-spacing:.07em;color:var(--navy);border-bottom:1px solid var(--line);padding-bottom:6px}}
aside p,aside li{{font-size:13.5px}}
aside ul{{margin:6px 0;padding-left:18px}}
aside ul.contents{{list-style:none;padding-left:0}} aside ul.contents li{{margin-bottom:5px}}
aside ul.contents a{{color:#24313d;text-decoration:none}} aside ul.contents a:hover{{text-decoration:underline;color:var(--navy2)}}
.dl a.btn{{display:block;background:var(--navy);color:#fff;text-align:center;padding:10px;border-radius:3px;text-decoration:none;font-family:Helvetica,Arial,sans-serif;font-weight:bold;margin-bottom:8px}}
.dl a.btn:hover{{background:var(--navy2)}}
.dl a.alt{{background:#fff;color:var(--navy);border:1px solid var(--navy);font-weight:normal}}
.dl p{{color:var(--mut);margin:6px 0 0}}
pre{{white-space:pre-wrap;font-size:11px;background:#f6f4ef;padding:8px;line-height:1.4}}
button.copy{{font-size:12px;cursor:pointer}}
/* --- footer --- */
footer{{border-top:2px solid var(--ink);margin-top:44px;padding:16px 0 36px;font-size:13.5px;color:#3c4753}}
footer .seriesline{{font-family:Helvetica,Arial,sans-serif;font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--mut);margin-top:10px}}
@media print{{
 .masthead .journalnav,.crumb,.actions,aside,button.copy{{display:none}}
 .grid{{grid-template-columns:1fr}}
 body{{font-size:11pt;line-height:1.5}} a{{color:#000;text-decoration:none}}
 article h2{{break-after:avoid}} article table,article figure{{break-inside:avoid}}
}}
</style>
</head>
<body>
<div class="masthead"><div class="wrap">
<div class="wordmark">{SERIES}</div>
<div class="mast-sub">Raphael Malikian · Cochrane-Level Evidence Syntheses</div>
</div></div>
<nav class="journalnav"><div class="wrap">
<a href="{HUB}#reviews">Browse</a>
<a href="{HUB}#method">About</a>
<a href="{HUB}">Systematic Reviews Hub</a>
<a href="{REPO}">GitHub</a>
</div></nav>
<div class="wrap">
<p class="crumb"><a href="{HUB}">Systematic Reviews Hub</a> &rsaquo; Family Medicine &rsaquo; Systematic Review</p>
<div class="typerow"><span class="arttype">{ARTICLE_TYPE}</span><span class="oa">Open Access</span></div>
<header class="article-head">
<h1>{html.escape(TITLE)}</h1>
<p class="standfirst">{SUBTITLE}</p>
<p class="authors"><strong>{AUTHOR}</strong><sup>1</sup></p>
<p class="affil"><sup>1</sup> {AFFIL}</p>
<p class="corr">Corresponding author: {AUTHOR}, <a href="mailto:{EMAIL}">{EMAIL}</a> · ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a></p>
<p class="publine">Published: {PUBLISHED} &middot; {VERSION}</p>
<p class="citeline">Malikian R. {TITLE}. {VERSION}; 2026. DOI: <a href="{DOI_URL}">{DOI_URL}</a></p>
</header>
<div class="actions">
<a class="primary" href="{REPO}/raw/main/manuscript.pdf">Download PDF</a>
<a href="{REPO}/raw/main/manuscript.docx">Download DOCX</a>
<button type="button" onclick="window.print()">Print</button>
<a href="#cite">Cite</a>
<a href="{share_url}" target="_blank" rel="noopener">Share</a>
</div>
<div class="grid">
<article>
<section class="abstract-panel">
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
<div class="box" id="cite">
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
<p>This is an open access article distributed under the terms of the {LICENCE}, which permits non-commercial use, distribution, and reproduction in any medium, provided the original author and source are credited. This review makes no clinical or medication recommendation.</p>
<p>© 2026 {AUTHOR}. DOI: <a href="{DOI_URL}">{DOI_URL}</a></p>
<p class="seriesline">{SERIES} — Raphael Malikian · Cochrane-Level Evidence Syntheses</p>
</footer>
</div>
</body>
</html>"""
    open("index.html", "w").write(page)
    print("wrote index.html", len(page), "bytes;",
          len(contents), "contents entries")


if __name__ == "__main__":
    main()
