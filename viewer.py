"""
autonotes 뷰어 — PDF와 노트를 나란히 보여주는 로컬 웹 서버
사용법: python viewer.py [루트_디렉토리]  (기본값: 현재 디렉토리)
"""
import json
import mimetypes
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
PORT = 7788

HTML = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>autonotes 뷰어</title>

<!-- markdown renderer -->
<script src="https://cdn.jsdelivr.net/npm/markdown-it/dist/markdown-it.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it-task-lists/dist/markdown-it-task-lists.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it-footnote/dist/markdown-it-footnote.min.js"></script>

<!-- sanitizer -->
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js"></script>

<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/markdown-it-texmath/css/texmath.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it-texmath/texmath.min.js"></script>

<!-- highlight.js -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github-dark.min.css">
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>

<style>
  :root {
    color-scheme: dark;
    --bg: #1e1e1e;
    --panel: #252526;
    --panel-2: #202124;
    --panel-3: #2d2d30;
    --panel-4: #31343a;
    --border: #3c3c3c;
    --text: #d4d4d4;
    --muted: #9da1a6;
    --muted-2: #6f7680;
    --accent: #569cd6;
    --accent-2: #4ec9b0;
    --accent-soft: rgba(86, 156, 214, 0.16);
    --link: #79c0ff;
    --code-inline-bg: #2b2d31;
    --quote: #8b949e;
    --shadow: 0 8px 24px rgba(0, 0, 0, 0.28);
    --radius: 12px;
    --radius-sm: 8px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; }
  body {
    display: flex;
    flex-direction: column;
    height: 100vh;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg);
    color: var(--text);
    overflow: hidden;
  }

  .layout { display: flex; flex: 1; overflow: hidden; position: relative; }

  #sidebar {
    width: 240px;
    flex-shrink: 0;
    background: var(--panel);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    transition: width 0.2s ease;
  }
  #sidebar.collapsed { width: 0; overflow: hidden; border-right: none; }
  #sidebar h2 {
    position: sticky;
    top: 0;
    z-index: 2;
    padding: 11px 14px;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #858585;
    border-bottom: 1px solid var(--border);
    background: var(--panel);
    display: flex;
    align-items: center;
    justify-content: space-between;
    white-space: nowrap;
  }
  #toggle-btn,
  #sidebar-open-btn {
    background: none;
    border: 1px solid transparent;
    color: #858585;
    cursor: pointer;
    font-size: 14px;
    line-height: 1;
    border-radius: 6px;
    transition: color 0.16s ease, background 0.16s ease, border-color 0.16s ease;
  }
  #toggle-btn { padding: 3px 5px; }
  #sidebar-open-btn {
    display: none;
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 10;
    padding: 6px 8px;
    background: rgba(37, 37, 38, 0.96);
    border-color: var(--border);
    box-shadow: var(--shadow);
  }
  #toggle-btn:hover,
  #sidebar-open-btn:hover {
    color: #d4d4d4;
    border-color: var(--border);
    background: rgba(255, 255, 255, 0.04);
  }
  #sidebar-open-btn.visible { display: block; }

  .course-label {
    padding: 10px 14px 6px;
    font-size: 11px;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    white-space: nowrap;
  }
  .file-item {
    padding: 8px 14px 8px 22px;
    cursor: pointer;
    font-size: 13px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    border-left: 2px solid transparent;
    transition: background 0.16s ease, color 0.16s ease, border-color 0.16s ease;
  }
  .file-item:hover { background: #2a2d2e; }
  .file-item.active {
    background: var(--accent-soft);
    border-left-color: var(--accent);
    color: #fff;
  }
  .file-item.no-notes { color: #666; }
  .file-item.no-notes::after {
    content: ' (노트 없음)';
    font-size: 10px;
    color: #555;
  }

  .panes { display: flex; flex: 1; overflow: hidden; min-width: 0; }
  iframe {
    flex: 1;
    border: none;
    background: #fff;
    min-width: 0;
  }
  .divider {
    width: 5px;
    background: var(--border);
    cursor: col-resize;
    flex-shrink: 0;
    transition: background 0.16s ease;
  }
  .divider:hover, .divider.dragging { background: #007acc; }

  #notes-pane {
    flex: 1;
    overflow-y: auto;
    min-width: 0;
    background: linear-gradient(180deg, #1f2125 0%, #1b1d21 100%);
  }

  .notes-shell {
    max-width: 980px;
    margin: 0 auto;
    padding: 28px 28px 48px;
  }

  .notes-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 18px;
    padding: 10px 14px;
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.02);
    color: var(--muted);
    font-size: 12px;
  }

  .markdown-body {
    line-height: 1.78;
    font-size: 15px;
    word-break: keep-all;
    overflow-wrap: anywhere;
  }

  .markdown-body > *:first-child { margin-top: 0 !important; }
  .markdown-body > *:last-child { margin-bottom: 0 !important; }

  .markdown-body h1,
  .markdown-body h2,
  .markdown-body h3,
  .markdown-body h4,
  .markdown-body h5,
  .markdown-body h6 {
    line-height: 1.3;
    margin: 1.35em 0 0.55em;
    font-weight: 700;
    letter-spacing: -0.01em;
  }
  .markdown-body h1 {
    font-size: 1.75em;
    color: var(--accent-2);
    padding-bottom: 0.35em;
    border-bottom: 1px solid var(--border);
  }
  .markdown-body h2 {
    font-size: 1.35em;
    color: var(--accent);
    padding-bottom: 0.2em;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  }
  .markdown-body h3 { font-size: 1.12em; color: #9cdcfe; }
  .markdown-body h4,
  .markdown-body h5,
  .markdown-body h6 { color: #c5d7ea; }

  .markdown-body p,
  .markdown-body ul,
  .markdown-body ol,
  .markdown-body blockquote,
  .markdown-body table,
  .markdown-body pre,
  .markdown-body details {
    margin: 0.85em 0;
  }

  .markdown-body hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5em 0;
  }

  .markdown-body a {
    color: var(--link);
    text-decoration: none;
    border-bottom: 1px solid transparent;
  }
  .markdown-body a:hover {
    border-bottom-color: rgba(121, 192, 255, 0.6);
  }

  .markdown-body strong { color: #f0f6fc; font-weight: 700; }
  .markdown-body em { color: #dcdcdc; }
  .markdown-body del { color: var(--muted); }

  .markdown-body ul,
  .markdown-body ol {
    padding-left: 1.5em;
  }
  .markdown-body li {
    margin: 0.25em 0;
  }
  .markdown-body li > ul,
  .markdown-body li > ol {
    margin: 0.35em 0;
  }

  .markdown-body .task-list-item {
    list-style: none;
    margin-left: -1.4em;
    padding-left: 1.6em;
  }
  .markdown-body .task-list-item input[type="checkbox"] {
    margin-right: 0.55em;
    transform: translateY(1px);
    accent-color: var(--accent);
  }

  .markdown-body blockquote {
    border-left: 4px solid var(--accent);
    padding: 0.85em 1em;
    color: var(--quote);
    background: rgba(86, 156, 214, 0.08);
    border-radius: 0 10px 10px 0;
  }
  .markdown-body blockquote > :first-child { margin-top: 0; }
  .markdown-body blockquote > :last-child { margin-bottom: 0; }

  .markdown-body :not(pre) > code {
    display: inline-block;
    padding: 0.12em 0.46em;
    margin: 0 0.1em;
    border-radius: 6px;
    background: var(--code-inline-bg);
    border: 1px solid rgba(255, 255, 255, 0.06);
    color: #ffb86c;
    font-family: 'SFMono-Regular', Menlo, Consolas, monospace;
    font-size: 0.9em;
    line-height: 1.5;
  }

  .code-block {
    margin: 1em 0;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    overflow: hidden;
    background: #111317;
    box-shadow: var(--shadow);
  }
  .code-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 9px 12px;
    background: #161b22;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 12px;
    color: var(--muted);
  }
  .code-lang {
    font-family: 'SFMono-Regular', Menlo, Consolas, monospace;
    text-transform: lowercase;
    letter-spacing: 0.04em;
  }
  .copy-btn {
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.04);
    color: var(--text);
    border-radius: 8px;
    padding: 5px 9px;
    cursor: pointer;
    font-size: 12px;
    transition: background 0.16s ease, transform 0.16s ease;
  }
  .copy-btn:hover { background: rgba(255, 255, 255, 0.09); }
  .copy-btn:active { transform: translateY(1px); }

  .markdown-body pre {
    margin: 0;
    padding: 14px 16px;
    overflow-x: auto;
    background: #0d1117;
  }
  .markdown-body pre code {
    background: none;
    padding: 0;
    border: none;
    color: inherit;
    font-family: 'SFMono-Regular', Menlo, Consolas, monospace;
    font-size: 13px;
    line-height: 1.65;
  }

  .markdown-body table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    display: block;
    overflow-x: auto;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
  }
  .markdown-body thead {
    background: rgba(255, 255, 255, 0.045);
  }
  .markdown-body th,
  .markdown-body td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    text-align: left;
    vertical-align: top;
    min-width: 90px;
  }
  .markdown-body tr:last-child td { border-bottom: none; }
  .markdown-body th { color: #f0f6fc; font-weight: 700; }

  .markdown-body img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    display: block;
    margin: 1em auto;
    box-shadow: var(--shadow);
  }

  .markdown-body details {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.025);
    padding: 0.85em 1em;
  }
  .markdown-body summary {
    cursor: pointer;
    font-weight: 600;
    color: #f0f6fc;
  }

  .markdown-body .footnotes {
    margin-top: 1.8em;
    padding-top: 1em;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.94em;
  }
  .markdown-body .footnote-ref,
  .markdown-body .footnote-backref {
    text-decoration: none;
    font-weight: 700;
  }

  .markdown-body .katex-display {
    margin: 1.1em 0;
    padding: 0.35em 0.25em;
    overflow-x: auto;
    overflow-y: hidden;
  }
  .markdown-body .katex {
    font-size: 1.03em;
  }

  #placeholder {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #555;
    font-size: 14px;
    text-align: center;
    padding: 24px;
  }

  .empty-note {
    padding: 20px;
    border: 1px dashed rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: var(--muted);
    background: rgba(255, 255, 255, 0.02);
  }
  .empty-note code { margin-top: 8px; }

  ::-webkit-scrollbar { width: 12px; height: 12px; }
  ::-webkit-scrollbar-thumb {
    background: #3b414a;
    border-radius: 999px;
    border: 2px solid transparent;
    background-clip: padding-box;
  }
  ::-webkit-scrollbar-track { background: transparent; }
</style>
</head>
<body>
<div class="layout">
  <button id="sidebar-open-btn" onclick="toggleSidebar()">▶</button>
  <div id="sidebar">
    <h2>파일 목록 <button id="toggle-btn" onclick="toggleSidebar()" title="사이드바 닫기">◀</button></h2>
    <div id="file-list">불러오는 중...</div>
  </div>
  <div class="panes" id="panes">
    <div id="placeholder">← 왼쪽에서 파일을 선택하세요</div>
  </div>
</div>

<script>
let currentItem = null;

const md = window.markdownit({
  html: true,
  linkify: true,
  typographer: true,
  breaks: true
});

if (typeof window.markdownitTaskLists === 'function') {
  md.use(window.markdownitTaskLists, { enabled: true, label: true, labelAfter: true });
}
if (typeof window.markdownitFootnote === 'function') {
  md.use(window.markdownitFootnote);
}
if (typeof window.texmath !== 'undefined') {
  md.use(window.texmath, {
    engine: window.katex,
    delimiters: 'dollars',
    katexOptions: {
      throwOnError: false,
      strict: 'ignore',
      trust: false,
      output: 'html'
    }
  });
}

function escapeHtml(text) {
  return String(text || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function normalizeLanguageLabel(lang) {
  const value = String(lang || '').trim().toLowerCase();
  if (!value || value === 'plaintext' || value === 'text') return 'plain';
  if (value === 'py') return 'python';
  if (value === 'js') return 'javascript';
  if (value === 'ts') return 'typescript';
  if (value === 'shell' || value === 'console') return 'bash';
  return value;
}

function escapeHtmlAttr(text) {
  return escapeHtml(text).replaceAll('`', '&#096;');
}

function detectCodeHighlight(code, explicitLang = '') {
  const normalizedExplicit = normalizeLanguageLabel(explicitLang);
  const source = String(code || '');

  if (normalizedExplicit && normalizedExplicit !== 'plain' && window.hljs && hljs.getLanguage(normalizedExplicit)) {
    try {
      const result = hljs.highlight(source, { language: normalizedExplicit, ignoreIllegals: true });
      return { html: result.value, language: normalizedExplicit };
    } catch (err) {}
  }

  if (window.hljs) {
    try {
      const auto = hljs.highlightAuto(source);
      const detected = normalizeLanguageLabel(auto.language || 'plain');
      return {
        html: auto.value || escapeHtml(source),
        language: detected || 'plain'
      };
    } catch (err) {}
  }

  return { html: escapeHtml(source), language: normalizedExplicit || 'plain' };
}

function isExplicitMathLanguage(info) {
  const value = normalizeLanguageLabel(info);
  return ['math', 'latex', 'tex', 'katex'].includes(value);
}

function isLikelyMathFence(info, content) {
  if (isExplicitMathLanguage(info)) return true;
  if (String(info || '').trim()) return false;

  const text = String(content || '').trim();
  if (!text) return false;

  const lines = text.split(/\r?\n/).filter(line => line.trim());
  if (lines.length > 12) return false;

  const mathSignals = [
    /\\[a-zA-Z]+/,
    /[Σ∑Π∏∫√∞≤≥≠≈∈∀∃α-ωΑ-Ω]/,
    /[_^]\{?[^}\s]+\}?/,
    /\barg\s*(max|min)\b/i,
    /\b(sin|cos|tan|log|ln|max|min)\b/i,
    /(?:^|\s)[A-Za-z][A-Za-z0-9_]*\([^\n)]*\)\s*=/m,
    /\bN_[A-Za-z0-9]+\(/,
    /\b[xywfpqτ]\b|x_i|y_i|w_i|f̂|ŷ|τ/,
    /\{\s*\n[\s\S]*\n\}/,
    /\b(d\(|epsilon|varepsilon)\b|ε/
  ];

  const codeSignals = [
    /^\s*(def|class|import|from|return|for|while|if|elif|else|try|except|with)\b/m,
    /^\s*(const|let|var|function|async|await|export|import)\b/m,
    /^\s*(public|private|protected|static|void|int|string|bool|interface)\b/m,
    /=>/,
    /;\s*(?:\n|$)/,
    /#include\b/,
    /console\.log\b/,
    /System\.out\b/,
    /<\/?[A-Za-z][^>]*>/
  ];

  let mathScore = 0;
  let codeScore = 0;
  for (const pattern of mathSignals) {
    if (pattern.test(text)) mathScore += 1;
  }
  for (const pattern of codeSignals) {
    if (pattern.test(text)) codeScore += 1;
  }

  return mathScore >= 2 && mathScore > codeScore;
}

function renderMathBlock(content) {
  const expr = String(content || '').trim();
  if (!expr) return '';
  try {
    return `<div class="math-block">${window.katex.renderToString(expr, {
      displayMode: true,
      throwOnError: false,
      strict: 'ignore',
      trust: false,
      output: 'html'
    })}</div>`;
  } catch (err) {
    return `<pre data-lang="plain"><code class="language-plain">${escapeHtml(expr)}</code></pre>`;
  }
}

md.renderer.rules.fence = function(tokens, idx) {
  const token = tokens[idx];
  const info = String(token.info || '').trim();
  const content = token.content || '';

  if (isLikelyMathFence(info, content)) {
    return renderMathBlock(content);
  }

  const detected = detectCodeHighlight(content, info);
  const lang = normalizeLanguageLabel(info) || detected.language || 'plain';
  return `<pre data-lang="${escapeHtmlAttr(lang)}"><code class="hljs language-${escapeHtmlAttr(lang)}">${detected.html}</code></pre>`;
};

function renderMarkdown(markdown) {
  const rawHtml = md.render(markdown);
  const safeHtml = window.DOMPurify.sanitize(rawHtml, {
    USE_PROFILES: { html: true },
    ADD_ATTR: ['target', 'rel', 'class', 'data-lang']
  });
  return safeHtml;
}

function enhanceRenderedNotes(root) {
  root.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (/^https?:\/\//i.test(href)) {
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
    }
  });

  root.querySelectorAll('table').forEach(table => {
    if (table.parentElement?.classList.contains('table-wrap')) return;
    const wrap = document.createElement('div');
    wrap.className = 'table-wrap';
    table.parentNode.insertBefore(wrap, table);
    wrap.appendChild(table);
  });

  root.querySelectorAll('pre').forEach(pre => {
    if (pre.parentElement?.classList.contains('code-block')) return;

    const code = pre.querySelector('code');
    if (!code) return;

    let lang = normalizeLanguageLabel(pre.dataset.lang || '');
    if (!lang || lang === 'plain') {
      const classNames = Array.from(code.classList || []);
      const langClass = classNames.find(name => name.startsWith('language-')) || '';
      lang = normalizeLanguageLabel(langClass.replace('language-', ''));
    }

    const rawText = code.textContent || '';
    const needsHighlight = !code.classList.contains('hljs') || !lang || lang === 'plain';
    if (needsHighlight) {
      const detected = detectCodeHighlight(rawText, lang);
      lang = normalizeLanguageLabel(lang || detected.language || 'plain');
      code.innerHTML = detected.html;
      code.className = `hljs language-${lang}`;
      pre.dataset.lang = lang;
    }

    lang = normalizeLanguageLabel(lang || 'plain');

    const wrapper = document.createElement('div');
    wrapper.className = 'code-block';

    const header = document.createElement('div');
    header.className = 'code-header';
    header.innerHTML = `
      <span class="code-lang">${escapeHtml(lang)}</span>
      <button type="button" class="copy-btn">복사</button>
    `;

    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(header);
    wrapper.appendChild(pre);

    const copyBtn = header.querySelector('.copy-btn');
    copyBtn.addEventListener('click', async () => {
      const text = rawText || code.innerText || pre.innerText;
      try {
        await navigator.clipboard.writeText(text);
        const prev = copyBtn.textContent;
        copyBtn.textContent = '복사됨';
        setTimeout(() => { copyBtn.textContent = prev; }, 1200);
      } catch (err) {
        copyBtn.textContent = '실패';
        setTimeout(() => { copyBtn.textContent = '복사'; }, 1200);
      }
    });
  });
}

async function loadFiles() {
  const res = await fetch('/api/files');
  const groups = await res.json();
  const list = document.getElementById('file-list');
  list.innerHTML = '';

  if (groups.length === 0) {
    list.innerHTML = '<div style="padding:12px 14px;color:#666;font-size:13px">PDF 파일이 없습니다</div>';
    return;
  }

  for (const group of groups) {
    const g = document.createElement('div');
    g.className = 'course-group';

    const label = document.createElement('div');
    label.className = 'course-label';
    label.textContent = group.course;
    g.appendChild(label);

    for (const f of group.files) {
      const item = document.createElement('div');
      item.className = 'file-item' + (f.has_notes ? '' : ' no-notes');
      item.textContent = f.stem;
      item.title = f.pdf;
      item.addEventListener('click', () => openFile(f, item));
      g.appendChild(item);
    }
    list.appendChild(g);
  }
}

async function openFile(f, item) {
  if (currentItem) currentItem.classList.remove('active');
  item.classList.add('active');
  currentItem = item;

  const panes = document.getElementById('panes');
  const placeholder = document.getElementById('placeholder');
  if (placeholder) placeholder.remove();

  let iframe = document.getElementById('pdf-frame');
  let divider = document.getElementById('divider');
  let notesPaneEl = document.getElementById('notes-pane');

  if (!iframe) {
    iframe = document.createElement('iframe');
    iframe.id = 'pdf-frame';

    divider = document.createElement('div');
    divider.id = 'divider';
    divider.className = 'divider';

    notesPaneEl = document.createElement('div');
    notesPaneEl.id = 'notes-pane';

    panes.appendChild(iframe);
    panes.appendChild(divider);
    panes.appendChild(notesPaneEl);
    setupDivider(divider, iframe, notesPaneEl);
  }

  iframe.src = '/file?path=' + encodeURIComponent(f.pdf);

  if (f.has_notes) {
    const res = await fetch('/file?path=' + encodeURIComponent(f.md) + '&raw=1');
    const markdown = await res.text();
    const rendered = renderMarkdown(markdown);
    notesPaneEl.innerHTML = `
      <div class="notes-shell">
        <div class="notes-meta">
          <span>${f.stem}.md</span>
          <span>Markdown · 코드 하이라이트 · 수식 렌더링 · 자동 언어 감지</span>
        </div>
        <article class="markdown-body">${rendered}</article>
      </div>
    `;
    enhanceRenderedNotes(notesPaneEl);
  } else {
    notesPaneEl.innerHTML = `
      <div class="notes-shell">
        <div class="empty-note">
          <p>아직 생성된 노트가 없습니다.</p>
          <code>python script.py ${f.pdf}</code>
        </div>
      </div>
    `;
  }
}

function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const openBtn = document.getElementById('sidebar-open-btn');
  sidebar.classList.toggle('collapsed');
  openBtn.classList.toggle('visible', sidebar.classList.contains('collapsed'));
}

function setupDivider(divider, iframe, notesPane) {
  let dragging = false;

  divider.addEventListener('mousedown', e => {
    dragging = true;
    divider.classList.add('dragging');
    iframe.style.pointerEvents = 'none';
    e.preventDefault();
  });

  document.addEventListener('mousemove', e => {
    if (!dragging) return;
    const panes = document.getElementById('panes');
    const rect = panes.getBoundingClientRect();
    const ratio = ((e.clientX - rect.left) / rect.width) * 100;
    const clamp = Math.min(Math.max(ratio, 20), 80);
    iframe.style.flex = 'none';
    iframe.style.width = clamp + '%';
    notesPane.style.flex = 'none';
    notesPane.style.width = (100 - clamp - 0.4) + '%';
  });

  document.addEventListener('mouseup', () => {
    if (!dragging) return;
    dragging = false;
    divider.classList.remove('dragging');
    iframe.style.pointerEvents = '';
  });
}

loadFiles();
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/":
            self._respond(200, "text/html; charset=utf-8", HTML.encode("utf-8"))

        elif path == "/api/files":
            data = self._list_files()
            self._respond(200, "application/json; charset=utf-8", json.dumps(data, ensure_ascii=False).encode("utf-8"))

        elif path == "/file":
            rel = unquote(qs.get("path", [""])[0])
            raw = qs.get("raw", ["0"])[0] == "1"
            file_path = ROOT / rel
            if not file_path.resolve().is_relative_to(ROOT):
                self._respond(403, "text/plain; charset=utf-8", b"Forbidden")
                return
            if not file_path.exists():
                self._respond(404, "text/plain; charset=utf-8", b"Not found")
                return
            mime = "text/plain; charset=utf-8" if raw else (
                mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
            )
            self._respond(200, mime, file_path.read_bytes())

        else:
            self._respond(404, "text/plain; charset=utf-8", b"Not found")

    def _respond(self, code, mime, body):
        self.send_response(code)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _list_files(self):
        groups: dict[str, list] = {}
        for pdf in sorted(ROOT.glob("**/*.pdf")):
            rel_pdf = str(pdf.relative_to(ROOT))
            rel_md = str(pdf.with_suffix(".md").relative_to(ROOT))
            has_notes = pdf.with_suffix(".md").exists()
            parts = pdf.relative_to(ROOT).parts
            course = parts[0] if len(parts) > 1 else "."
            groups.setdefault(course, []).append({
                "stem": pdf.stem,
                "pdf": rel_pdf,
                "md": rel_md,
                "has_notes": has_notes,
            })
        return [{"course": k, "files": v} for k, v in groups.items()]


def main():
    server = HTTPServer(("localhost", 0), Handler)
    server.allow_reuse_address = True
    port = server.server_address[1]
    url = f"http://localhost:{port}"
    print(f"autonotes 뷰어 시작: {url}")
    print(f"루트 디렉토리: {ROOT}")
    print("종료하려면 Ctrl+C")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
        server.server_close()
        print("\n서버 종료.")


if __name__ == "__main__":
    main()
