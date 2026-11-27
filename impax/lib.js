// Shared helpers for the Liontrust report and IC memo
const fs = require('fs');
const d = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType,
  HeadingLevel, ImageRun, LevelFormat, BorderStyle, PageBreak, Footer, Header, PageNumber, TableOfContents } = d;

const FONT = 'Arial';
const NAVY = '1F3864';
const CONTENT_W = 10466; // A4 (11906) minus 0.6in margins each side (720*2)

function runs(text, base = {}) {
  // **bold** markup
  const out = [];
  const parts = String(text).split(/(\*\*[^*]+\*\*)/g);
  for (const p of parts) {
    if (!p) continue;
    if (p.startsWith('**') && p.endsWith('**')) out.push(new TextRun({ text: p.slice(2, -2), bold: true, font: FONT, ...base }));
    else out.push(new TextRun({ text: p, font: FONT, ...base }));
  }
  return out;
}
const P = (t, o = {}) => new Paragraph({ children: runs(t, o.run || {}), spacing: { after: 100, line: 264 }, alignment: o.align, ...(o.p || {}) });
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT })], pageBreakBefore: false });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT })] });
const H3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: t, font: FONT })] });
const B = (t, lvl = 0) => new Paragraph({ numbering: { reference: 'bul', level: lvl }, children: runs(t), spacing: { after: 60, line: 252 } });
const N = (t) => new Paragraph({ numbering: { reference: 'num', level: 0 }, children: runs(t), spacing: { after: 60, line: 252 } });
const SRC = (t) => new Paragraph({ children: [new TextRun({ text: t, font: FONT, size: 15, italics: true, color: '595959' })], spacing: { after: 140 } });
const BR = () => new Paragraph({ children: [new PageBreak()] });

function img(path, wIn, hIn) {
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [new ImageRun({ type: 'png', data: fs.readFileSync(path), transformation: { width: wIn * 96, height: hIn * 96 } })] });
}

function table(headers, rows, widths, opt = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const scale = CONTENT_W / total;
  const w = widths.map(x => Math.floor(x * scale));
  w[w.length - 1] += CONTENT_W - w.reduce((a, b) => a + b, 0);
  const sz = opt.size || 15;
  const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
  const borders = { top: border, bottom: border, left: border, right: border };
  const NUMRE = /^[-–−~≈(+]*[£$€]?[0-9][0-9.,]*\s*[%xpmbn]*\)?(\s*\(.*\))?$/;
  const PH = /^(n\.a\.|n\.m\.|—|–|-|)$/;
  const colRight = headers.map((_, i) => i > 0 && rows.every(r => NUMRE.test(String(r[i]).trim()) || PH.test(String(r[i]).trim())) && rows.some(r => NUMRE.test(String(r[i]).trim())));
  const mk = (txt, i, isHead, rIdx) => new TableCell({
    width: { size: w[i], type: WidthType.DXA }, borders,
    shading: isHead ? { type: ShadingType.CLEAR, fill: NAVY, color: 'auto' } : (rIdx % 2 ? { type: ShadingType.CLEAR, fill: 'F2F5FA', color: 'auto' } : undefined),
    margins: { top: 40, bottom: 40, left: 70, right: 70 },
    children: [new Paragraph({ alignment: colRight[i] ? AlignmentType.RIGHT : AlignmentType.LEFT,
      children: runs(String(txt), { size: sz, color: isHead ? 'FFFFFF' : '000000', bold: isHead ? true : undefined }) })]
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: w,
    rows: [new TableRow({ tableHeader: true, children: headers.map((h, i) => mk(h, i, true, 0)) }),
      ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => mk(c, i, false, ri)) }))]
  });
}
const SP = () => new Paragraph({ children: [], spacing: { after: 60 } });

function doc(children, title) {
  return new d.Document({
    creator: 'Equity research', title,
    styles: {
      default: { document: { run: { font: FONT, size: 19 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: NAVY }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAVY, space: 2 } } } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 23, bold: true, color: '2E5597' }, paragraph: { spacing: { before: 200, after: 90 }, keepNext: true, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 20, bold: true, color: '404040' }, paragraph: { spacing: { before: 140, after: 70 }, keepNext: true, outlineLevel: 2 } },
        { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 44, bold: true, color: NAVY }, paragraph: { spacing: { before: 0, after: 120 } } },
      ]
    },
    numbering: { config: [
      { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } },
        { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 240 } } } }] },
      { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
    ] },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 864, bottom: 864, left: 720, right: 720 } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: title, font: FONT, size: 14, color: '7F7F7F' })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Page ', font: FONT, size: 14, color: '7F7F7F' }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 14, color: '7F7F7F' }), new TextRun({ text: '  |  For professional investors. Not investment advice. Data as of 26-27 Nov 2026.', font: FONT, size: 14, color: '7F7F7F' })] })] }) },
      children
    }]
  });
}
module.exports = { P, H1, H2, H3, B, N, SRC, BR, img, table, SP, doc, runs, d, FONT, NAVY, TableOfContents };
