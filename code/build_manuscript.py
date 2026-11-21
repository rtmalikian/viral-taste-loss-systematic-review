#!/usr/bin/env python3
"""Build manuscript.pdf (WeasyPrint via HTML) and manuscript.docx (pandoc)
from manuscript/manuscript.md. Run with the pubtools venv python:
  ~/workspace/venvs/pubtools/bin/python scripts/build_manuscript.py
"""
import os, sys
BASE = os.path.expanduser("~/workspace/publications/viral-taste-loss-review/manuscript")

import markdown
from weasyprint import HTML

md_text = open(f"{BASE}/manuscript.md").read()
html_body = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
for marker in ('Appendix D: characteristics', 'Appendix E: studies excluded'):
    pos = html_body.find(marker)
    if pos > 0:
        nxt = html_body.find('<table>', pos)
        html_body = html_body[:nxt] + '<table class="appendix-table">' + html_body[nxt+7:]
css = open(f"{BASE}/render.css").read()
html_doc = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{css}</style></head>
<body>{html_body}</body></html>"""
HTML(string=html_doc, base_url=BASE).write_pdf(f"{BASE}/manuscript.pdf")
print("wrote manuscript.pdf")

import pypandoc
pypandoc.convert_file(
    f"{BASE}/manuscript.md", "docx",
    outputfile=f"{BASE}/manuscript.docx",
    extra_args=[f"--resource-path={BASE}", "--standalone"],
)
print("wrote manuscript.docx")
