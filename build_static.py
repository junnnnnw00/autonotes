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
    """Generate an autonotes PNG icon using only stdlib (no Pillow).

    Design (32-unit grid):
      - Dark rounded-rect background with ~15% inset padding
      - Document frame  : (6, 5) – (19, 22)   [upper-left area]
      - Text lines      : y = 10, 13.5, 17     [inside document]
      - Teal badge      : cx=22, cy=22, r=5.5  [lower-right]
      - "A" glyph       : pixel-art inside badge
    """
    s = size
    f = s / 32.0

    BG   = (30,  30,  30,  255)  # #1e1e1e
    CARD = (44,  44,  46,  255)  # doc body fill (slightly lighter)
    BLUE = (86, 156, 214, 255)   # #569cd6
    TEAL = (78, 201, 176, 255)   # #4ec9b0
    DARK = (18,  18,  18,  255)  # letter on badge

    pixels = [BG] * (s * s)

    def px(x, y, c):
        if 0 <= x < s and 0 <= y < s:
            pixels[y * s + x] = c

    def rect(x0, y0, x1, y1, c):
        for y in range(max(0, int(y0)), min(s, int(y1))):
            for x in range(max(0, int(x0)), min(s, int(x1))):
                px(x, y, c)

    def circle(cx, cy, r, c):
        for y in range(int(cy - r) - 1, int(cy + r) + 2):
            for x in range(int(cx - r) - 1, int(cx + r) + 2):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                    px(x, y, c)

    # ── Rounded-rect background (squircle-ish, ~15% inset) ───────────────────
    pad = int(1.5 * f)   # ~1.5 design-units inset from icon edge
    rr  = int(5.5 * f)   # corner radius
    # Fill cross
    rect(pad + rr, pad, s - pad - rr, s - pad, BG)   # horizontal band already BG
    rect(pad, pad + rr, s - pad, s - pad - rr, BG)
    # Rounded corners via circles — use BG to "erase" the square corners
    # (We fill the whole canvas with a rounded panel instead)
    # Simpler: fill rounded rect with BG-override where corners round to BG
    # Actually: fill full area with BG first, then draw rounded panel:
    bx0, by0, bx1, by1 = pad, pad, s - pad, s - pad
    rect(bx0 + rr, by0, bx1 - rr, by1, BG)
    rect(bx0, by0 + rr, bx1, by1 - rr, BG)
    circle(bx0 + rr, by0 + rr, rr, BG)
    circle(bx1 - rr, by0 + rr, rr, BG)
    circle(bx0 + rr, by1 - rr, rr, BG)
    circle(bx1 - rr, by1 - rr, rr, BG)
    # (All BG — the background is already BG, so this is a no-op visually)
    # The icon content is drawn on BG; dock/OS provides squircle clipping for PNGs.

    # ── Document frame ────────────────────────────────────────────────────────
    # Sits in upper-left quadrant with breathing room on all sides.
    dx0, dy0 = int(6 * f), int(5 * f)
    dx1, dy1 = int(19 * f), int(22 * f)
    rect(dx0, dy0, dx1, dy1, CARD)

    # Border stroke (~1.5 design-units)
    bw = max(1, round(1.5 * f))
    rect(dx0,        dy0,        dx1,        dy0 + bw, BLUE)   # top
    rect(dx0,        dy1 - bw,   dx1,        dy1,      BLUE)   # bottom
    rect(dx0,        dy0,        dx0 + bw,   dy1,      BLUE)   # left
    rect(dx1 - bw,   dy0,        dx1,        dy1,      BLUE)   # right
    rect(dx0 + bw,   dy0 + bw,   dx1 - bw,  dy1 - bw, CARD)   # inner fill

    # Text lines
    lw  = max(1, round(1.2 * f))
    lx0 = dx0 + bw + round(1.5 * f)
    lx1 = dx1 - bw - round(1.5 * f)
    for i, ly_u in enumerate([10.0, 13.5, 17.0]):
        ly = round(ly_u * f)
        x1 = lx1 - round(3 * f) if i == 2 else lx1   # last line shorter
        rect(lx0, ly, x1, ly + lw, BLUE)

    # ── Teal badge ────────────────────────────────────────────────────────────
    bcx, bcy, bcr = 22.0 * f, 22.0 * f, 5.5 * f
    circle(bcx, bcy, bcr, TEAL)

    # ── "A" glyph (7-wide × 7-tall, diagonal legs) ───────────────────────────
    # Staircase diagonals make the A shape unambiguous at any scale.
    glyph = [
        "   #   ",   # row 0 — peak
        "  # #  ",   # row 1 — opening
        " #   # ",   # row 2 — widening
        "#     #",   # row 3 — full width
        "#######",   # row 4 — crossbar (57 % down)
        "#     #",   # row 5 — legs
        "#     #",   # row 6 — feet
    ]
    cell  = max(2, round(bcr * 0.145))   # smaller cell to fit 7-wide glyph
    gw, gh = 7 * cell, 7 * cell
    gx0   = round(bcx - gw / 2)
    gy0   = round(bcy - gh / 2)

    for ri, row in enumerate(glyph):
        for ci, ch in enumerate(row):
            if ch == "#":
                rect(
                    gx0 + ci * cell,        gy0 + ri * cell,
                    gx0 + ci * cell + cell,  gy0 + ri * cell + cell,
                    DARK,
                )

    # ── PNG encode ────────────────────────────────────────────────────────────
    def chunk(tag: bytes, data: bytes) -> bytes:
        payload = tag + data
        return struct.pack(">I", len(data)) + payload + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF)

    raw = bytearray()
    for y in range(s):
        raw += b"\x00"
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
