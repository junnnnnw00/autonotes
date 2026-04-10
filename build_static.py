#!/usr/bin/env python3
"""
Generate static files for GitHub Pages deployment.
Produces index.html, pdfview.html, files.json at repo root.
PDFs and MDs are served directly from their existing paths.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# ── Import HTML strings from viewer ──────────────────────────────────────────
sys.path.insert(0, str(ROOT))
from viewer import HTML, PDFVIEW_HTML

# ── Patch main viewer HTML for static serving ────────────────────────────────
index_html = HTML
# API → static JSON
index_html = index_html.replace(
    "fetch('/api/files')",
    "fetch('files.json')"
)
# PDF iframe URL
index_html = index_html.replace(
    "'/pdfview?path=' + encodeURIComponent(f.pdf)",
    "'pdfview.html?path=' + encodeURIComponent(f.pdf)"
)
# Markdown fetch URL (raw=1 not needed for GitHub Pages — files served as text)
index_html = index_html.replace(
    "'/file?path=' + encodeURIComponent(f.md) + '&raw=1'",
    "f.md"
)

(ROOT / "index.html").write_text(index_html, encoding="utf-8")
print("✓ index.html")

# ── Patch pdfview HTML ────────────────────────────────────────────────────────
pdfview_html = PDFVIEW_HTML
# PDF.js document load URL
pdfview_html = pdfview_html.replace(
    "'/file?path=' + encodeURIComponent(pdfPath)",
    "pdfPath"
)

(ROOT / "pdfview.html").write_text(pdfview_html, encoding="utf-8")
print("✓ pdfview.html")

# ── Generate files.json ───────────────────────────────────────────────────────
groups: dict[str, list] = {}
skip_dirs = {"__pycache__", ".git", "node_modules"}

for pdf in sorted(ROOT.glob("**/*.pdf")):
    rel = pdf.relative_to(ROOT)
    # Skip hidden dirs and known non-content dirs
    if any(p.startswith(".") or p in skip_dirs for p in rel.parts):
        continue
    rel_pdf = str(rel).replace("\\", "/")
    rel_md = str(rel.with_suffix(".md")).replace("\\", "/")
    has_notes = (ROOT / rel_md).exists()
    course = rel.parts[0] if len(rel.parts) > 1 else "."
    groups.setdefault(course, []).append({
        "stem": pdf.stem,
        "pdf": rel_pdf,
        "md": rel_md,
        "has_notes": has_notes,
    })

data = [{"course": k, "files": v} for k, v in groups.items()]
(ROOT / "files.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
total = sum(len(g["files"]) for g in data)
print(f"✓ files.json  ({len(data)} courses, {total} files)")
print("\nDone. Commit index.html, pdfview.html, files.json to deploy.")
