// Markdown -> styled DOCX builder for institutional research notes.
// Usage: node build_docx.js <report.md> <out.docx> <meta.json> [toc_pages.json]
const fs = require("fs");
const path = require("path");
const { marked } = require("marked");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, AlignmentType, HeadingLevel, ImageRun, PageBreak,
  Header, Footer, PageNumber, LevelFormat, ExternalHyperlink, TabStopType,
  TabStopPosition, VerticalAlign, TableLayoutType, PageOrientation, LineRuleType, Tab,
  PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
} = require("docx");

const [, , mdPath, outPath, metaPath, tocPath] = process.argv;
const md = fs.readFileSync(mdPath, "utf8");
const meta = JSON.parse(fs.readFileSync(metaPath, "utf8"));
const tocPages = tocPath && fs.existsSync(tocPath) ? JSON.parse(fs.readFileSync(tocPath, "utf8")) : {};
const baseDir = path.dirname(path.resolve(mdPath));

// ---------- palette / geometry ----------
const NAVY = "15233F", BLUE = "2F6FD0", GREY = "5B6577", LIGHT = "F2F4F7", RULE = "D0D5DD", CALLOUT = "EEF3FA";
const FONT = { ascii: "Arial", hAnsi: "Arial", cs: "Arial", eastAsia: "Yu Gothic" };
const PAGE_W = 11906, PAGE_H = 16838, MARGIN = 1080; // A4, 0.75in margins
const CONTENT_W = PAGE_W - 2 * MARGIN; // 9746 DXA

// ---------- inline rendering ----------
function decode(s) {
  return String(s)
    .replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, " ");
}
function inlineRuns(tokens, style = {}) {
  const out = [];
  for (const t of tokens || []) {
    switch (t.type) {
      case "strong": out.push(...inlineRuns(t.tokens, { ...style, bold: true })); break;
      case "em": out.push(...inlineRuns(t.tokens, { ...style, italics: true })); break;
      case "del": out.push(...inlineRuns(t.tokens, { ...style, strike: true })); break;
      case "codespan": out.push(run(decode(t.text), style)); break;
      case "br": out.push(new TextRun({ break: 1 })); break;
      case "link": {
        const children = inlineRuns(t.tokens, { ...style, color: BLUE, underline: {} });
        if (/^https?:/.test(t.href)) out.push(new ExternalHyperlink({ link: t.href, children }));
        else out.push(...children);
        break;
      }
      case "image": out.push(run(`[${t.text}]`, style)); break;
      case "html": break; // drop inline html
      case "escape": out.push(run(decode(t.text), style)); break;
      case "text":
        if (t.tokens && t.tokens.length) out.push(...inlineRuns(t.tokens, style));
        else out.push(run(decode(t.text), style));
        break;
      default:
        if (t.tokens) out.push(...inlineRuns(t.tokens, style));
        else if (t.text) out.push(run(decode(t.text), style));
    }
  }
  return out;
}
function run(text, style = {}) {
  return new TextRun({
    text, font: FONT, size: style.size || 19, bold: style.bold, italics: style.italics,
    color: style.color || style.baseColor || "1F2533", underline: style.underline, strike: style.strike,
  });
}
function plainText(tokens) {
  return (tokens || []).map((t) => (t.tokens ? plainText(t.tokens) : decode(t.text || ""))).join("");
}

// ---------- block builders ----------
const children = [];
const headingIndex = []; // for TOC
let h1Count = 0;

function para(runs, opts = {}) {
  return new Paragraph({
    children: runs,
    spacing: { after: opts.after ?? 100, before: opts.before ?? 0, line: opts.line ?? 276, lineRule: LineRuleType.AUTO },
    alignment: opts.alignment,
    indent: opts.indent,
    border: opts.border,
    shading: opts.shading,
    keepNext: opts.keepNext,
    numbering: opts.numbering,
    heading: opts.heading,
    pageBreakBefore: opts.pageBreakBefore,
  });
}

function headingPara(mdLevel, text, tokens) {
  const BL = meta.breakLevel || 1;
  const level = Math.max(1, Math.min(4, mdLevel - BL + 1)); // visual level
  const sizes = { 1: 32, 2: 25, 3: 21, 4: 19 };
  const colors = { 1: NAVY, 2: NAVY, 3: BLUE, 4: NAVY };
  const hl = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 }[level];
  const runs = inlineRuns(tokens, { bold: true, size: sizes[level], color: colors[level] });
  const isTop = level === 1;
  if (level <= (meta.tocDepth || 2)) headingIndex.push({ level, text });
  return new Paragraph({
    children: runs,
    heading: hl,
    pageBreakBefore: isTop && h1Count++ > 0,
    keepNext: true,
    keepLines: true,
    spacing: { before: isTop ? 0 : level === 2 ? 260 : 180, after: isTop ? 160 : 90, line: 252, lineRule: LineRuleType.AUTO },
    border: isTop ? { bottom: { style: BorderStyle.SINGLE, size: 12, color: BLUE, space: 6 } } : undefined,
  });
}

// numeric detection for right alignment
const NUMERIC_RE = /^[\s(+\-−–~≈<>]*[¥$€£]?[\d.,]+[\s%xX倍bnmkK)A-Za-z¥]*$|^[-–—n.a/NA ]+$|^[+\-−]?\d/;
function isNumericCell(s) {
  const t = s.trim();
  if (!t) return true;
  return /^[\s(+\-−–~≈<>]*[¥$€£]?\s?[\d][\d.,]*\s?(%|x|X|bn|m|k|pp|bp|bps|yrs?|y|倍)?\)?\s*(\(?[EAF]\)?)?$/.test(t) || /^(n\.?a\.?|n\/a|–|—|-|nm|NM)$/i.test(t);
}

function buildTable(tok) {
  const header = tok.header.map((c) => plainText(c.tokens));
  const rows = tok.rows.map((r) => r.map((c) => plainText(c.tokens)));
  const ncol = header.length;
  // ---- column widths: guarantee no mid-word / mid-number breaks, then share the rest by text volume ----
  const fsz = ncol >= 9 ? 13 : ncol >= 7 ? 14 : ncol >= 5 ? 15 : 16; // half-points
  const charDXA = (fsz / 2) * 20 * 0.52;          // approx average glyph width in DXA
  const PAD = 190;                                  // cell margins + slack
  const longestWord = (t) => (t || "").split(/[\s/]+/).reduce((m, w) => Math.max(m, w.length), 0);
  const isNum = [];
  for (let j = 0; j < ncol; j++) {
    const vals = rows.map((r) => r[j] || "");
    isNum.push(j > 0 && vals.filter((v) => isNumericCell(v)).length / Math.max(1, vals.length) >= 0.6);
  }
  const minW = [], flex = [];
  for (let j = 0; j < ncol; j++) {
    const cells = rows.map((r) => r[j] || "");
    const maxLen = Math.max(header[j].length, ...cells.map((c) => c.length));
    const avgLen = (header[j].length + cells.reduce((a, c) => a + c.length, 0)) / (cells.length + 1);
    let minChars = Math.max(longestWord(header[j]) * 1.15, ...cells.map((c) => longestWord(c)));
    if (isNum[j]) minChars = Math.max(minChars, ...cells.map((c) => Math.min(c.length, 16)));
    minChars = Math.min(minChars, 30);
    minW.push(minChars * charDXA + PAD);
    flex.push(isNum[j] ? 0.15 * avgLen : Math.max(2, 0.6 * Math.min(maxLen, 120) + 0.4 * avgLen));
  }
  let widths;
  const minSum = minW.reduce((a, b) => a + b, 0);
  if (minSum >= CONTENT_W) {
    widths = minW.map((w) => Math.floor((w / minSum) * CONTENT_W));
  } else {
    const rest = CONTENT_W - minSum, fsum = flex.reduce((a, b) => a + b, 0) || 1;
    widths = minW.map((w, j) => Math.floor(w + (flex[j] / fsum) * rest));
  }
  widths[0] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const numericCol = isNum;
  const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mkCell = (cellTok, j, isHeader, rowIdx) => {
    const runs = inlineRuns(cellTok.tokens, {
      size: fsz, bold: isHeader || (j === 0 && !isHeader ? false : undefined),
      color: isHeader ? "FFFFFF" : undefined,
    });
    const align = isHeader ? (j === 0 ? AlignmentType.LEFT : AlignmentType.CENTER) : numericCol[j] ? AlignmentType.RIGHT : AlignmentType.LEFT;
    return new TableCell({
      width: { size: widths[j], type: WidthType.DXA },
      borders,
      verticalAlign: VerticalAlign.CENTER,
      shading: isHeader ? { fill: NAVY, type: ShadingType.CLEAR, color: "auto" }
        : rowIdx % 2 === 1 ? { fill: LIGHT, type: ShadingType.CLEAR, color: "auto" } : undefined,
      margins: { top: 50, bottom: 50, left: 80, right: 80 },
      children: [new Paragraph({ children: runs.length ? runs : [run("", { size: fsz })], alignment: align, spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO } })],
    });
  };
  const trs = [];
  trs.push(new TableRow({ tableHeader: true, cantSplit: true, children: tok.header.map((c, j) => mkCell(c, j, true, 0)) }));
  tok.rows.forEach((r, i) => {
    trs.push(new TableRow({ cantSplit: true, children: r.map((c, j) => mkCell(c, j, false, i)) }));
  });
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, rows: trs, layout: TableLayoutType.FIXED });
}

function pngSize(file) {
  const b = fs.readFileSync(file);
  if (b.toString("ascii", 1, 4) === "PNG") return { w: b.readUInt32BE(16), h: b.readUInt32BE(20), type: "png" };
  // jpeg
  let i = 2;
  while (i < b.length) {
    if (b[i] !== 0xff) { i++; continue; }
    const marker = b[i + 1];
    const len = b.readUInt16BE(i + 2);
    if (marker >= 0xc0 && marker <= 0xc3) return { h: b.readUInt16BE(i + 5), w: b.readUInt16BE(i + 7), type: "jpg" };
    i += 2 + len;
  }
  throw new Error("unknown image " + file);
}

function imageBlock(src, caption, widthFrac = 1.0) {
  const file = path.isAbsolute(src) ? src : path.join(baseDir, src);
  if (!fs.existsSync(file)) { console.error("missing image", file); return []; }
  const { w, h, type } = pngSize(file);
  const maxWpx = (CONTENT_W / 1440) * 96 * widthFrac; // px at 96 dpi
  const scale = maxWpx / w;
  const out = [new Paragraph({
    alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 80, after: 40, line: 240, lineRule: LineRuleType.AUTO },
    children: [new ImageRun({ type, data: fs.readFileSync(file), transformation: { width: Math.round(w * scale), height: Math.round(h * scale) }, altText: { title: caption || "chart", description: caption || "chart", name: path.basename(file) } })],
  })];
  if (caption) out.push(para([run(caption, { italics: true, size: 16, color: GREY })], { after: 160, alignment: AlignmentType.LEFT }));
  return out;
}

function listBlocks(tok, level = 0) {
  const out = [];
  tok.items.forEach((item) => {
    // each item: tokens may include text + nested list
    const inl = [];
    const nested = [];
    for (const t of item.tokens) {
      if (t.type === "list") nested.push(t);
      else if (t.type === "text" || t.type === "paragraph") inl.push(...(t.tokens || [{ type: "text", text: t.text }]));
      else if (t.type === "space") continue;
      else inl.push(t);
    }
    out.push(new Paragraph({
      children: inlineRuns(inl),
      numbering: { reference: tok.ordered ? "num" : "bul", level, instance: tok.ordered ? numInstance : undefined },
      spacing: { after: 60, line: 264, lineRule: LineRuleType.AUTO },
    }));
    for (const n of nested) out.push(...listBlocks(n, Math.min(level + 1, 2)));
  });
  return out;
}
let numInstance = 0;

function calloutBlocks(tok) {
  const out = [];
  const inner = tok.tokens.filter((t) => t.type !== "space");
  inner.forEach((t, idx) => {
    let runs;
    if (t.type === "paragraph") runs = inlineRuns(t.tokens, { size: 18, color: NAVY });
    else if (t.type === "list") { // flatten list into lines
      t.items.forEach((it) => {
        out.push(new Paragraph({
          children: [run("▪  ", { size: 18, color: BLUE }), ...inlineRuns(it.tokens.flatMap((x) => x.tokens || [x]), { size: 18, color: NAVY })],
          shading: { fill: CALLOUT, type: ShadingType.CLEAR, color: "auto" },
          border: { left: { style: BorderStyle.SINGLE, size: 24, color: BLUE, space: 8 } },
          indent: { left: 200, right: 200 }, spacing: { after: 0, line: 264, lineRule: LineRuleType.AUTO },
        }));
      });
      return;
    } else runs = inlineRuns(t.tokens || [{ type: "text", text: t.text || t.raw }], { size: 18, color: NAVY });
    out.push(new Paragraph({
      children: runs,
      shading: { fill: CALLOUT, type: ShadingType.CLEAR, color: "auto" },
      border: { left: { style: BorderStyle.SINGLE, size: 24, color: BLUE, space: 8 } },
      indent: { left: 200, right: 200 },
      spacing: { before: idx === 0 ? 60 : 0, after: idx === inner.length - 1 ? 160 : 40, line: 264, lineRule: LineRuleType.AUTO },
    }));
  });
  return out;
}

// ---------- walk markdown ----------
const tokens = marked.lexer(md);
let skipFirstH1 = meta.skipFirstH1 !== false; // report title is on the cover
for (const tok of tokens) {
  switch (tok.type) {
    case "heading": {
      if (tok.depth === 1 && skipFirstH1) { skipFirstH1 = false; continue; }
      children.push(headingPara(tok.depth, plainText(tok.tokens), tok.tokens));
      break;
    }
    case "paragraph": {
      // standalone image paragraph
      const imgs = tok.tokens.filter((t) => t.type === "image");
      if (imgs.length && plainText(tok.tokens.filter((t) => t.type !== "image")).trim() === "") {
        for (const im of imgs) children.push(...imageBlock(im.href, im.text));
        break;
      }
      children.push(para(inlineRuns(tok.tokens), { after: 110 }));
      break;
    }
    case "list": numInstance++; children.push(...listBlocks(tok)); children.push(para([], { after: 40 })); break;
    case "table": children.push(buildTable(tok)); children.push(para([], { after: 120 })); break;
    case "blockquote": children.push(...calloutBlocks(tok)); break;
    case "hr": children.push(para([], { border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 4 } }, after: 120 })); break;
    case "code": children.push(para([new TextRun({ text: tok.text, font: "Courier New", size: 16 })], { shading: { fill: LIGHT, type: ShadingType.CLEAR, color: "auto" } })); break;
    case "html": {
      if (/pagebreak/.test(tok.raw)) children.push(new Paragraph({ children: [new PageBreak()] }));
      break;
    }
    case "space": break;
    default:
      if (tok.text) children.push(para([run(decode(tok.text))]));
  }
}

// ---------- cover page ----------
function cover() {
  const out = [];
  const banner = new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W], layout: TableLayoutType.FIXED,
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: NAVY, type: ShadingType.CLEAR, color: "auto" },
      borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } },
      margins: { top: 500, bottom: 500, left: 500, right: 500 },
      children: [
        para([run(meta.kicker || "EQUITY RESEARCH", { bold: true, size: 18, color: "8FB4F0" })], { after: 200 }),
        para([run(meta.title, { bold: true, size: 52, color: "FFFFFF" })], { after: 80, line: 240 }),
        para([run(meta.subtitle || "", { size: 26, color: "C9D3E6" })], { after: 260 }),
        para([run(meta.tagline || "", { italics: true, size: 22, color: "FFFFFF" })], { after: 0 }),
      ],
    })] })],
  });
  out.push(banner);
  out.push(para([], { after: 200 }));
  // rating / target strip
  if (meta.rating) {
    const w1 = Math.round(CONTENT_W / 3);
    const cells = [
      ["RECOMMENDATION", meta.rating, BLUE],
      ["12-MONTH TARGET", meta.target || "", NAVY],
      ["REFERENCE PRICE", meta.price || "", NAVY],
    ];
    out.push(new Table({
      width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [w1, w1, CONTENT_W - 2 * w1], layout: TableLayoutType.FIXED,
      rows: [new TableRow({ children: cells.map(([lab, val, fill], k) => new TableCell({
        width: { size: k < 2 ? w1 : CONTENT_W - 2 * w1, type: WidthType.DXA },
        shading: { fill, type: ShadingType.CLEAR, color: "auto" },
        borders: { top: { style: BorderStyle.SINGLE, size: 12, color: "FFFFFF" }, bottom: { style: BorderStyle.SINGLE, size: 12, color: "FFFFFF" }, left: { style: BorderStyle.SINGLE, size: 12, color: "FFFFFF" }, right: { style: BorderStyle.SINGLE, size: 12, color: "FFFFFF" } },
        margins: { top: 160, bottom: 160, left: 200, right: 200 },
        children: [para([run(lab, { bold: true, size: 15, color: "C9D3E6" })], { after: 40 }), para([run(val, { bold: true, size: 28, color: "FFFFFF" })], { after: 0 })],
      })) })],
    }));
    out.push(para([], { after: 200 }));
  }
  // key data table (2 x n, split in two columns)
  if (meta.keyData && meta.keyData.length) {
    const half = Math.ceil(meta.keyData.length / 2);
    const left = meta.keyData.slice(0, half), right = meta.keyData.slice(half);
    const cw = [Math.round(CONTENT_W * 0.22), Math.round(CONTENT_W * 0.28), Math.round(CONTENT_W * 0.22)];
    cw.push(CONTENT_W - cw[0] - cw[1] - cw[2]);
    const b = { style: BorderStyle.SINGLE, size: 4, color: RULE };
    const nb = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
    const rows = [];
    for (let i = 0; i < half; i++) {
      const L = left[i] || ["", ""], R = right[i] || ["", ""];
      rows.push(new TableRow({ children: [L[0], L[1], R[0], R[1]].map((t, j) => new TableCell({
        width: { size: cw[j], type: WidthType.DXA },
        borders: { top: nb, left: nb, right: nb, bottom: b },
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: [para([run(t, { size: 17, bold: j % 2 === 1, color: j % 2 === 0 ? GREY : NAVY })], { after: 0, alignment: j % 2 === 1 ? AlignmentType.RIGHT : AlignmentType.LEFT })],
      })) }));
    }
    out.push(para([run("KEY DATA", { bold: true, size: 17, color: BLUE })], { after: 60 }));
    out.push(new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: cw, rows, layout: TableLayoutType.FIXED }));
    out.push(para([], { after: 200 }));
  }
  if (meta.thesis && meta.thesis.length) {
    out.push(para([run("INVESTMENT THESIS IN BRIEF", { bold: true, size: 17, color: BLUE })], { after: 60 }));
    for (const t of meta.thesis) {
      const m = t.match(/^\*\*(.+?)\*\*\s*(.*)$/);
      out.push(new Paragraph({
        children: m ? [run(m[1] + " ", { bold: true, size: 18, color: NAVY }), run(m[2], { size: 18 })] : [run(t, { size: 18 })],
        numbering: { reference: "bul", level: 0 }, spacing: { after: 60, line: 260, lineRule: LineRuleType.AUTO },
      }));
    }
  }
  out.push(para([run(meta.coverNote || "", { italics: true, size: 15, color: GREY })], { before: 200, after: 0 }));
  out.push(new Paragraph({ children: [new PageBreak()] }));
  return out;
}

// ---------- manual TOC (page numbers from a prior render) ----------
function toc() {
  const out = [para([run("Contents", { bold: true, size: 32, color: NAVY })], { after: 160, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: BLUE, space: 6 } } })];
  for (const h of headingIndex) {
    const pg = tocPages[h.text] != null ? String(tocPages[h.text]) : "00";
    out.push(new Paragraph({
      spacing: { after: h.level === 1 ? 50 : 20, before: h.level === 1 ? 70 : 0, line: 252, lineRule: LineRuleType.AUTO },
      indent: { left: h.level === 1 ? 0 : 360 },
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W, leader: "dot" }],
      children: [
        run(h.text, { size: h.level === 1 ? 19 : 17, bold: h.level === 1, color: h.level === 1 ? NAVY : "333A47" }),
        new TextRun({ children: [new Tab()], font: FONT, size: 17 }),
        run(pg, { size: h.level === 1 ? 19 : 17, bold: h.level === 1, color: NAVY }),
      ],
    }));
  }
  out.push(new Paragraph({ children: [new PageBreak()] }));
  return out;
}

const coverBlocks = cover();
const tocBlocks = meta.toc === false ? [] : toc();

const doc = new Document({
  creator: meta.author || "Research",
  title: meta.title,
  description: meta.subtitle || "",
  styles: {
    default: { document: { run: { font: FONT, size: 19, color: "1F2533" }, paragraph: { spacing: { line: 276, lineRule: LineRuleType.AUTO } } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 32, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 0, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 25, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 260, after: 90 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 21, bold: true, color: BLUE, font: FONT }, paragraph: { spacing: { before: 180, after: 90 }, outlineLevel: 2 } },
      { id: "FooterSmall", name: "Footer Small", basedOn: "Normal", run: { size: 14, color: GREY, font: FONT }, paragraph: { spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO } } },
      { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 19, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 140, after: 60 }, outlineLevel: 3 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bul", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "▪", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } }, run: { color: BLUE } } },
        { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 260 } }, run: { color: GREY } } },
        { level: 2, format: LevelFormat.BULLET, text: "·", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1080, hanging: 260 } } } },
      ] },
      { reference: "num", levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } }, run: { color: NAVY, bold: true } } },
        { level: 1, format: LevelFormat.LOWER_LETTER, text: "%2)", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 760, hanging: 300 } } } },
        { level: 2, format: LevelFormat.LOWER_ROMAN, text: "%3.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1120, hanging: 300 } } } },
      ] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: 1000, bottom: 900, left: MARGIN, right: MARGIN, header: 450, footer: 400 } }, titlePage: true },
    headers: {
      default: new Header({ children: [new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
        tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
        children: [run(meta.headerLeft || meta.title, { size: 15, color: GREY, bold: true }), new TextRun({ children: [new Tab()], size: 15 }), run(meta.headerRight || "", { size: 15, color: GREY })],
      })] }),
      first: new Header({ children: [new Paragraph({ children: [] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        style: "FooterSmall",
        tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
        children: [run(meta.footerLeft || "For professional investors only. Not investment advice.", { size: 14, color: GREY }), new TextRun({ children: [new Tab()], size: 14 }), run("Page ", { size: 14, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 14, color: GREY }), run(" of ", { size: 14, color: GREY }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 14, color: GREY })],
      })] }),
      first: new Footer({ children: [new Paragraph({ children: [run(meta.coverFooter || "", { size: 14, color: GREY })] })] }),
    },
    children: [...coverBlocks, ...tocBlocks, ...children],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  fs.writeFileSync(outPath + ".headings.json", JSON.stringify(headingIndex, null, 1));
  console.log("wrote", outPath, "headings:", headingIndex.length);
});
