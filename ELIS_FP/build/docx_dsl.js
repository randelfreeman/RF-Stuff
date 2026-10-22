// Minimal document DSL -> DOCX (docx-js). Inline markup: **bold**, __italic__, [label](url), {{sup:text}}.
const fs = require('fs');
const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, ExternalHyperlink, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, HeadingLevel, ImageRun, PageBreak, BorderStyle, Header, Footer, PageNumber, TableOfContents,
  LevelFormat, TabStopType, VerticalAlign, TableLayoutType, PageOrientation } = D;

const C = { navy: '13213F', blue: '2A78D6', ink: '0B0B0B', ink2: '52514E', muted: '898781', grid: 'D9D8D2', zebra: 'F4F5F8', card: 'EFF1F5', link: '1C5CAB', red: 'C62828', green: '1B7F3B' };
const FONT = 'Arial';
const PAGE_W = 11906, PAGE_H = 16838, MARGIN = 1020; // A4, ~1.8cm margins
const CONTENT_W = PAGE_W - 2 * MARGIN;

function inlineRuns(text, base = {}) {
  // returns array of TextRun / ExternalHyperlink
  const out = [];
  if (text === null || text === undefined) return out;
  text = String(text);
  const linkRe = /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g;
  let last = 0, m;
  const pushStyled = (seg) => {
    // bold/italic/sup tokens
    const re = /(\*\*[^*]+\*\*|__[^_]+__|\{\{sup:[^}]+\}\})/g;
    let l = 0, mm;
    while ((mm = re.exec(seg)) !== null) {
      if (mm.index > l) out.push(new TextRun({ text: seg.slice(l, mm.index), font: FONT, ...base }));
      const tok = mm[0];
      if (tok.startsWith('**')) out.push(new TextRun({ text: tok.slice(2, -2), bold: true, font: FONT, ...base }));
      else if (tok.startsWith('__')) out.push(new TextRun({ text: tok.slice(2, -2), italics: true, font: FONT, ...base }));
      else out.push(new TextRun({ text: tok.slice(6, -2), superScript: true, font: FONT, ...base }));
      l = mm.index + tok.length;
    }
    if (l < seg.length) out.push(new TextRun({ text: seg.slice(l), font: FONT, ...base }));
  };
  while ((m = linkRe.exec(text)) !== null) {
    if (m.index > last) pushStyled(text.slice(last, m.index));
    const label = m[1], url = m[2];
    const isMarker = /^#[A-Za-z0-9_\-.]+$/.test(label);
    out.push(new ExternalHyperlink({ link: url, children: [new TextRun({ text: isMarker ? `[${label}]` : label, font: FONT, color: C.link, underline: isMarker ? undefined : {}, ...base, ...(isMarker ? { size: Math.max(12, (base.size || 19) - 4) } : {}) })] }));
    last = m.index + m[0].length;
  }
  if (last < text.length) pushStyled(text.slice(last));
  return out;
}

const P = (text, opts = {}) => new Paragraph({ children: inlineRuns(text, { size: opts.size || 19, color: opts.color, bold: opts.bold }), spacing: { after: opts.after ?? 100, before: opts.before ?? 0, line: opts.line ?? 264 }, alignment: opts.align || AlignmentType.LEFT, keepNext: opts.keepNext, indent: opts.indent });

function heading(text, level, pbb) {
  const sizes = { 1: 30, 2: 24, 3: 20 };
  const lv = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3 }[level];
  return new Paragraph({ heading: lv, children: [new TextRun({ text, font: FONT, bold: true, size: sizes[level], color: level === 3 ? C.blue : C.navy })],
    spacing: { before: level === 1 ? 240 : 180, after: level === 1 ? 120 : 80 }, keepNext: true, keepLines: true, pageBreakBefore: !!pbb,
    border: level === 1 ? { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.navy, space: 4 } } : undefined });
}

function bullets(items, ref = 'bul', level = 0, size = 19) {
  const out = [];
  for (const it of items) {
    const text = typeof it === 'string' ? it : it.text;
    out.push(new Paragraph({ children: inlineRuns(text, { size }), numbering: { reference: ref, level }, spacing: { after: 60, line: 252 } }));
    if (typeof it === "object" && Array.isArray(it.sub)) out.push(...bullets(it.sub, ref, level + 1, size));
  }
  return out;
}

function cellParas(val, o) {
  const v = (val && typeof val === 'object' && !Array.isArray(val)) ? val : { text: val };
  const lines = String(v.text ?? '').split('\n');
  return { v, paras: lines.map(line => new Paragraph({ children: inlineRuns(line, { size: o.size, bold: v.bold || o.bold, color: v.color || o.color }), alignment: v.align || o.align, spacing: { after: 0, before: 0, line: 228 } })) };
}

function table(spec) {
  const n = spec.cols.length;
  const totalW = spec.width ? Math.round(CONTENT_W * spec.width) : CONTENT_W;
  const fr = spec.widths || Array(n).fill(1);
  const sum = fr.reduce((a, b) => a + b, 0);
  const colW = fr.map(f => Math.floor(totalW * f / sum));
  colW[n - 1] += totalW - colW.reduce((a, b) => a + b, 0);
  const size = spec.size || 16;
  const align = (i) => { const a = (spec.align || [])[i] || (i === 0 ? 'l' : 'r'); return a === 'r' ? AlignmentType.RIGHT : a === 'c' ? AlignmentType.CENTER : AlignmentType.LEFT; };
  const border = { style: BorderStyle.SINGLE, size: 2, color: C.grid };
  const borders = { top: border, bottom: border, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } };
  const mk = (val, i, isHead, rIdx) => {
    const { v, paras } = cellParas(val, { size, align: align(i), bold: isHead, color: isHead ? 'FFFFFF' : undefined });
    const fill = isHead ? C.navy : (v.fill || (spec.highlightRows && spec.highlightRows.includes(rIdx) ? 'DCE6F7' : (spec.zebra !== false && rIdx % 2 === 1 ? C.zebra : 'FFFFFF')));
    return new TableCell({ children: paras, width: { size: colW[i], type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill },
      margins: { top: 40, bottom: 40, left: 70, right: 70 }, verticalAlign: VerticalAlign.CENTER, borders, columnSpan: v.span });
  };
  const rows = [];
  if (spec.cols && !spec.noHeader) rows.push(new TableRow({ tableHeader: true, cantSplit: true, children: spec.cols.map((c, i) => mk(c, i, true, -1)) }));
  spec.rows.forEach((r, ri) => rows.push(new TableRow({ cantSplit: true, children: r.map((c, i) => mk(c, i, false, ri)) })));
  const out = [];
  if (spec.title) out.push(new Paragraph({ children: [new TextRun({ text: spec.title, bold: true, size: 18, color: C.navy, font: FONT })], spacing: { before: 120, after: 60 }, keepNext: true }));
  out.push(new Table({ rows, width: { size: totalW, type: WidthType.DXA }, columnWidths: colW, layout: TableLayoutType.FIXED }));
  if (spec.source) out.push(new Paragraph({ children: inlineRuns(spec.source, { size: 14, color: C.muted }), spacing: { before: 40, after: 140 } }));
  else out.push(new Paragraph({ children: [], spacing: { after: 100 } }));
  return out;
}

function image(spec) {
  const buf = fs.readFileSync(spec.path);
  // read PNG size
  const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
  const maxW = (spec.widthIn || 6.6) * 96; // px at 96dpi for docx-js transformation
  const scale = maxW / w;
  const out = [];
  if (spec.title) out.push(new Paragraph({ children: [new TextRun({ text: spec.title, bold: true, size: 18, color: C.navy, font: FONT })], spacing: { before: 120, after: 60 }, keepNext: true }));
  out.push(new Paragraph({ children: [new ImageRun({ type: 'png', data: buf, transformation: { width: Math.round(w * scale), height: Math.round(h * scale) }, altText: { title: spec.alt || 'chart', description: spec.alt || 'chart', name: path.basename(spec.path) } })], alignment: AlignmentType.CENTER, spacing: { after: 40 }, keepNext: !!spec.source }));
  if (spec.source) out.push(new Paragraph({ children: inlineRuns(spec.source, { size: 14, color: C.muted }), spacing: { after: 140 } }));
  return out;
}

function callout(spec) {
  const border = { style: BorderStyle.SINGLE, size: 24, color: spec.color || C.navy };
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  const children = [];
  if (spec.title) children.push(new Paragraph({ children: [new TextRun({ text: spec.title, bold: true, size: 19, color: C.navy, font: FONT })], spacing: { after: 60 } }));
  for (const t of [].concat(spec.text || [])) children.push(new Paragraph({ children: inlineRuns(t, { size: 18 }), spacing: { after: 60, line: 252 } }));
  if (spec.bullets) children.push(...bullets(spec.bullets, 'bul', 0, 18));
  return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W], layout: TableLayoutType.FIXED, rows: [new TableRow({ children: [new TableCell({ children, width: { size: CONTENT_W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: spec.fill || C.card }, margins: { top: 100, bottom: 100, left: 160, right: 140 }, borders: { left: border, top: none, bottom: none, right: none } })] })] }), new Paragraph({ children: [], spacing: { after: 100 } })];
}

function kpis(items) {
  const n = items.length; const w = Math.floor(CONTENT_W / n);
  const none = { style: BorderStyle.SINGLE, size: 12, color: 'FFFFFF' };
  const cells = items.map(it => new TableCell({ width: { size: w, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: C.card }, margins: { top: 100, bottom: 100, left: 120, right: 100 }, borders: { top: none, bottom: none, left: none, right: none },
    children: [new Paragraph({ children: inlineRuns(it.v, { size: 30, bold: true, color: C.navy }), spacing: { after: 40 } }), new Paragraph({ children: inlineRuns(it.l, { size: 14, color: C.ink2 }), spacing: { after: 0, line: 220 } })] }));
  return [new Table({ width: { size: w * n, type: WidthType.DXA }, columnWidths: Array(n).fill(w), layout: TableLayoutType.FIXED, rows: [new TableRow({ children: cells })] }), new Paragraph({ children: [], spacing: { after: 120 } })];
}

function render(blocks) {
  const out = [];
  for (const b of blocks) {
    switch (b.t) {
      case 'h1': out.push(heading(b.text, 1, b.pbb)); break;
      case 'h2': out.push(heading(b.text, 2)); break;
      case 'h3': out.push(heading(b.text, 3)); break;
      case 'p': out.push(P(b.text, b)); break;
      case 'bullets': out.push(...bullets(b.items, b.numbered ? 'num' : 'bul', 0, b.size || 19)); out.push(new Paragraph({ children: [], spacing: { after: 60 } })); break;
      case 'table': out.push(...table(b)); break;
      case 'img': out.push(...image(b)); break;
      case 'callout': out.push(...callout(b)); break;
      case 'kpis': out.push(...kpis(b.items)); break;
      case 'source': out.push(new Paragraph({ children: inlineRuns(b.text, { size: 14, color: C.muted }), spacing: { after: 120 } })); break;
      case 'pagebreak': out.push(new Paragraph({ children: [new PageBreak()] })); break;
      case 'toc': out.push(new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-2' })); break;
      case 'raw': out.push(...b.items); break;
      default: throw new Error('unknown block ' + b.t);
    }
  }
  return out;
}

function buildDoc({ blocks, cover, headerText, footerText, title }) {
  const numbering = { config: [
    { reference: 'bul', levels: [0, 1, 2].map(l => ({ level: l, format: LevelFormat.BULLET, text: l === 0 ? '▪' : '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 340 + l * 300, hanging: 220 } }, run: { color: C.blue, font: FONT } } })) },
    { reference: 'num', levels: [0, 1].map(l => ({ level: l, format: LevelFormat.DECIMAL, text: `%${l + 1}.`, alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400 + l * 300, hanging: 300 } } } })) },
  ] };
  const header = new Header({ children: [new Paragraph({ children: [new TextRun({ text: headerText, font: FONT, size: 14, color: C.muted })], border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: C.grid, space: 4 } } })] });
  const footer = new Footer({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }], children: [new TextRun({ text: footerText, font: FONT, size: 13, color: C.muted }), new TextRun({ children: ['\tPage ', PageNumber.CURRENT, ' of ', PageNumber.TOTAL_PAGES], font: FONT, size: 13, color: C.muted })] })] });
  const sections = [];
  if (cover) sections.push({ properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } }, children: render(cover) });
  sections.push({ properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN, header: 500, footer: 500 } } }, headers: { default: header }, footers: { default: footer }, children: render(blocks) });
  return new Document({ creator: 'Equity research (AI-assisted)', title, description: title, numbering, features: { updateFields: true },
    styles: { default: { document: { run: { font: FONT, size: 19, color: C.ink } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 30, bold: true, color: C.navy }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 24, bold: true, color: C.navy }, paragraph: { spacing: { before: 180, after: 80 }, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 20, bold: true, color: C.blue }, paragraph: { spacing: { before: 140, after: 60 }, outlineLevel: 2 } },
      ] },
    sections });
}

async function write(docSpec, outPath) {
  const doc = buildDoc(docSpec);
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(outPath, buf);
  return outPath;
}
module.exports = { write, C, CONTENT_W, inlineRuns };
