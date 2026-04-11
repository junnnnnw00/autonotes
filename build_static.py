#!/usr/bin/env python3
"""
Generate static files for GitHub Pages deployment.
Produces index.html, pdfview.html, files.json, manifest.json, sw.js,
icon-192.png, icon-512.png at repo root.
PDFs and MDs are served directly from their existing paths.
"""
import json
import struct
import sys
import zlib
from pathlib import Path


def _make_icon_png(size: int) -> bytes:
    """Generate an autonotes PNG icon using only stdlib (no Pillow)."""
    s = size
    f = s / 32.0  # scale factor relative to 32px design grid

    # RGBA color constants
    BG    = (30,  30,  30,  255)  # #1e1e1e — outer background
    PANEL = (37,  37,  38,  255)  # #252526 — document body
    BLUE  = (86,  156, 214, 255)  # #569cd6 — document outline / lines
    TEAL  = (78,  201, 176, 255)  # #4ec9b0 — badge circle
    DARK  = (20,  20,  20,  255)  # + symbol on badge

    pixels = [BG] * (s * s)

    def px(x, y, color):
        if 0 <= x < s and 0 <= y < s:
            pixels[y * s + x] = color

    def rect(x0, y0, x1, y1, color):
        for y in range(max(0, y0), min(s, y1)):
            for x in range(max(0, x0), min(s, x1)):
                px(x, y, color)

    def circle(cx, cy, r, color):
        for y in range(int(cy - r) - 1, int(cy + r) + 2):
            for x in range(int(cx - r) - 1, int(cx + r) + 2):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                    px(x, y, color)

    def hline(y, x0, x1, color, thickness=1):
        for t in range(thickness):
            rect(x0, y + t, x1, y + t + 1, color)

    # ── Document body ────────────────────────────────────────────────────────
    dx0, dy0 = int(5 * f), int(3 * f)
    dx1, dy1 = int(21 * f), int(25 * f)
    rect(dx0, dy0, dx1, dy1, PANEL)

    # Document border (2px on design grid)
    bw = max(1, int(1.8 * f))
    for t in range(bw):
        rect(dx0 + t, dy0 + t, dx1 - t, dy0 + t + 1, BLUE)
        rect(dx0 + t, dy1 - t - 1, dx1 - t, dy1 - t, BLUE)
        rect(dx0 + t, dy0 + t, dx0 + t + 1, dy1 - t, BLUE)
        rect(dx1 - t - 1, dy0 + t, dx1 - t, dy1 - t, BLUE)

    # Text lines
    lw = max(1, int(1.5 * f))
    for line_y in [10, 14, 18]:
        hline(int(line_y * f), int(8 * f), int(18 * f), BLUE, lw)

    # Shorten last line
    rect(int(14 * f), int(18 * f), int(18 * f), int(18 * f) + lw, PANEL)

    # ── Badge circle ─────────────────────────────────────────────────────────
    cx, cy, cr = 24 * f, 24 * f, 5.5 * f
    circle(cx, cy, cr, TEAL)

    # + symbol
    hw = int(2.8 * f)
    sw2 = max(1, int(1.6 * f))
    hline(int(cy - sw2 // 2), int(cx) - hw, int(cx) + hw + 1, DARK, sw2)
    rect(int(cx - sw2 // 2), int(cy) - hw, int(cx - sw2 // 2) + sw2, int(cy) + hw + 1, DARK)

    # ── Encode to PNG ────────────────────────────────────────────────────────
    def chunk(tag: bytes, data: bytes) -> bytes:
        payload = tag + data
        return struct.pack(">I", len(data)) + payload + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF)

    raw = bytearray()
    for y in range(s):
        raw += b"\x00"  # filter: None
        for x in range(s):
            raw += bytes(pixels[y * s + x])

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", s, s, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 6))
    png += chunk(b"IEND", b"")
    return png

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

# ── PWA assets ───────────────────────────────────────────────────────────────
for size in (192, 512):
    path = ROOT / f"icon-{size}.png"
    path.write_bytes(_make_icon_png(size))
    print(f"✓ icon-{size}.png")

for fname in ("manifest.json", "sw.js"):
    if (ROOT / fname).exists():
        print(f"✓ {fname}")
    else:
        print(f"⚠  {fname} not found — skipping")

print("\nDone. Commit index.html, pdfview.html, files.json, manifest.json, sw.js, icon-*.png to deploy.")
