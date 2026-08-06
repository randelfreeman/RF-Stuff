const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageNumber,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, TableOfContents,
  Header, Footer, PageBreak, ExternalHyperlink, LevelFormat, convertInchesToTwip,
  PageOrientation,
} = require('docx');

// ---------- page geometry (US Letter) ----------
const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = 1037;                                 // 0.72in, integer dxa
const USABLE = PAGE_W - MARGIN * 2 - 16;             // 16 dxa safety so rounding can never overflow

// ---------- palette ----------
const NAVY = '1F3557';
const SLATE = '3E5871';
const ACCENT = '9B6B2F';
const RULE = 'C3CCD8';
const HEAD_FILL = '1F3557';
const ZEBRA = 'F2F5F8';
const CALLOUT = 'FBF4E7';
const INK = '1A1A1A';
const MUTED = '5C6B7A';

const BODY_FONT = 'Calibri';
const HEAD_FONT = 'Calibri';

// ---------- inline markdown tokenizer ----------
// handles **bold**, *italic*, `code`, [text](url); bold+italic via ***text***
function inlineRuns(text, base = {}) {
  const out = [];
  const re = /(\[([^\]]+)\]\(([^)\s]+)\))|(\*\*\*(.+?)\*\*\*)|(\*\*(.+?)\*\*)|(\*(.+?)\*)|(`([^`]+)`)/g;
  let last = 0, m;
  const push = (t, opts) => { if (t) out.push(new TextRun({ text: t, ...base, ...opts })); };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index), {});
    if (m[1]) {
      out.push(new ExternalHyperlink({
        link: m[3],
        children: [new TextRun({ text: m[2], ...base, style: 'Hyperlink' })],
      }));
    } else if (m[4]) push(m[5], { bold: true, italics: true });
    else if (m[6]) push(m[7], { bold: true });
    else if (m[8]) push(m[9], { italics: true });
    else if (m[10]) push(m[11], { font: 'Consolas', size: (base.size || 19) - 2 });
    last = re.lastIndex;
  }
  push(text.slice(last), {});
  return out.length ? out : [new TextRun({ text: '', ...base })];
}

// ---------- table helpers ----------
function splitRow(line) {
  let s = line.trim();
  if (s.startsWith('|')) s = s.slice(1);
  if (s.endsWith('|')) s = s.slice(0, -1);
  // split on | not preceded by backslash
  return s.split(/(?<!\\)\|/).map(c => c.trim().replace(/\\\|/g, '|'));
}

function isDivider(line) {
  return /^\s*\|?[\s:-]*-{2,}[\s:|-]*\|?\s*$/.test(line) && line.includes('-');
}

function plainLen(s) {
  return s.replace(/\*\*|\*|`/g, '').replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').length;
}

function computeWidths(rows, total) {
  const n = rows[0].length;
  const weights = new Array(n).fill(0);
  rows.forEach(r => r.forEach((c, i) => {
    if (i < n) weights[i] = Math.max(weights[i], Math.min(plainLen(c), 90));
  }));
  // soften extremes so no column collapses
  const soft = weights.map(w => Math.pow(Math.max(w, 4), 0.72));
  const sum = soft.reduce((a, b) => a + b, 0);
  const T = Math.floor(total);
  const minW = Math.floor(T / (n * 3.2));
  let widths = soft.map(w => Math.max(minW, Math.floor((w / sum) * T)));
  // reconcile to exactly T, trimming from the widest column if minW pushed us over
  let drift = T - widths.reduce((a, b) => a + b, 0);
  while (drift !== 0) {
    const idx = drift > 0
      ? widths.indexOf(Math.max(...widths))
      : widths.indexOf(Math.max(...widths));
    const step = drift > 0 ? Math.min(drift, 50) : Math.max(drift, -50);
    if (widths[idx] + step < minW) break;
    widths[idx] += step;
    drift -= step;
  }
  return widths.map(w => Math.round(w));
}

function buildTable(rawRows, usable) {
  const header = rawRows[0];
  const body = rawRows.slice(1);
  const n = header.length;
  const norm = rawRows.map(r => {
    const c = r.slice(0, n);
    while (c.length < n) c.push('');
    return c;
  });
  const widths = computeWidths(norm, usable);
  const fontSize = n >= 7 ? 14 : n >= 5 ? 15 : 16; // half-points

  const cellBorders = {
    top: { style: BorderStyle.SINGLE, size: 1, color: RULE },
    bottom: { style: BorderStyle.SINGLE, size: 1, color: RULE },
    left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
    right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
  };

  const mkCell = (txt, i, opts) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, color: 'auto', fill: opts.fill },
    borders: cellBorders,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({
      spacing: { before: 0, after: 0, line: 230 },
      children: inlineRuns(txt, {
        size: fontSize,
        font: BODY_FONT,
        bold: opts.bold || undefined,
        color: opts.color,
      }),
    })],
  });

  const rows = [
    new TableRow({
      tableHeader: true,
      children: header.map((h, i) => mkCell(h, i, { fill: HEAD_FILL, bold: true, color: 'FFFFFF' })),
    }),
    ...body.map((r, ri) => new TableRow({
      children: r.map((c, i) => mkCell(c, i, { fill: ri % 2 ? ZEBRA : 'FFFFFF', color: INK })),
    })),
  ];

  return new Table({
    columnWidths: widths,
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    rows,
  });
}

// ---------- paragraph builders ----------
const P = (children, opts = {}) => new Paragraph({
  children,
  spacing: { before: 60, after: 110, line: 265 },
  ...opts,
});

function calloutBox(lines, usable) {
  return new Table({
    columnWidths: [usable],
    width: { size: usable, type: WidthType.DXA },
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: usable, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, color: 'auto', fill: CALLOUT },
        margins: { top: 130, bottom: 130, left: 170, right: 170 },
        borders: {
          top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
          bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
          left: { style: BorderStyle.SINGLE, size: 18, color: ACCENT },
          right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
        },
        children: lines.map((l, i) => new Paragraph({
          spacing: { before: i ? 70 : 0, after: 0, line: 260 },
          children: inlineRuns(l, { size: 17, font: BODY_FONT, color: '4A3A1E' }),
        })),
      })],
    })],
  });
}

// ---------- main parser ----------
function convert(md, usable) {
  const lines = md.split('\n');
  const out = [];
  let i = 0;
  let skippedTitle = false;

  const flushRule = () => out.push(new Paragraph({
    spacing: { before: 40, after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 1 } },
    children: [new TextRun({ text: '', size: 2 })],
  }));

  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();

    // blank
    if (!t) { i++; continue; }

    // html comment
    if (t.startsWith('<!--')) { i++; continue; }

    // horizontal rule — skip if the next meaningful line is a heading
    if (/^(-{3,}|\*{3,}|_{3,})$/.test(t)) {
      let j = i + 1;
      while (j < lines.length && !lines[j].trim()) j++;
      const nextIsHeading = j < lines.length && /^#{1,6}\s/.test(lines[j].trim());
      if (!nextIsHeading) flushRule();
      i++; continue;
    }

    // headings
    const h = t.match(/^(#{1,6})\s+(.*)$/);
    if (h) {
      const level = h[1].length;
      const text = h[2].trim();
      if (level === 1 && !skippedTitle) { skippedTitle = true; i++; continue; } // title page handles it
      if (level === 2) {
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_1,
          pageBreakBefore: true,
          spacing: { before: 0, after: 200 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 6 } },
          children: inlineRuns(text, { size: 30, bold: true, color: NAVY, font: HEAD_FONT }),
        }));
      } else if (level === 3) {
        const isGroup = /^Type [A-D]\b/.test(text);
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_2,
          spacing: { before: isGroup ? 340 : 280, after: isGroup ? 160 : 120 },
          keepNext: true,
          children: inlineRuns(text, {
            size: isGroup ? 24 : 25,
            bold: true,
            color: isGroup ? ACCENT : NAVY,
            font: HEAD_FONT,
            allCaps: isGroup || undefined,
          }),
        }));
      } else {
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_3,
          spacing: { before: 220, after: 100 },
          keepNext: true,
          children: inlineRuns(text, { size: 21, bold: true, color: SLATE, font: HEAD_FONT }),
        }));
      }
      i++; continue;
    }

    // table
    if (t.startsWith('|') && i + 1 < lines.length && isDivider(lines[i + 1])) {
      const raw = [splitRow(lines[i])];
      i += 2;
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        raw.push(splitRow(lines[i])); i++;
      }
      out.push(buildTable(raw, usable));
      out.push(new Paragraph({ spacing: { before: 0, after: 170 }, children: [new TextRun({ text: '', size: 2 })] }));
      continue;
    }

    // blockquote / callout
    if (t.startsWith('>')) {
      const buf = [];
      while (i < lines.length && lines[i].trim().startsWith('>')) {
        const c = lines[i].trim().replace(/^>\s?/, '');
        if (c) buf.push(c); else if (buf.length) buf.push('');
        i++;
      }
      out.push(calloutBox(buf.filter((x, k, a) => !(x === '' && (k === 0 || k === a.length - 1))), usable));
      out.push(new Paragraph({ spacing: { before: 0, after: 170 }, children: [new TextRun({ text: '', size: 2 })] }));
      continue;
    }

    // bullet list
    if (/^[-*+]\s+/.test(t)) {
      while (i < lines.length && /^[-*+]\s+/.test(lines[i].trim())) {
        let content = lines[i].trim().replace(/^[-*+]\s+/, '');
        i++;
        // continuation lines (indented, not a new bullet / table / heading)
        while (i < lines.length && lines[i].trim() && /^\s{2,}\S/.test(lines[i]) &&
               !/^[-*+]\s+/.test(lines[i].trim()) && !/^\d+\.\s+/.test(lines[i].trim())) {
          content += ' ' + lines[i].trim(); i++;
        }
        out.push(new Paragraph({
          numbering: { reference: 'md-bullets', level: 0 },
          spacing: { before: 40, after: 90, line: 262 },
          children: inlineRuns(content, { size: 19, font: BODY_FONT, color: INK }),
        }));
      }
      continue;
    }

    // ordered list
    if (/^\d+\.\s+/.test(t)) {
      while (i < lines.length && /^\d+\.\s+/.test(lines[i].trim())) {
        let content = lines[i].trim().replace(/^\d+\.\s+/, '');
        i++;
        while (i < lines.length && lines[i].trim() && /^\s{2,}\S/.test(lines[i]) &&
               !/^\d+\.\s+/.test(lines[i].trim()) && !/^[-*+]\s+/.test(lines[i].trim())) {
          content += ' ' + lines[i].trim(); i++;
        }
        out.push(new Paragraph({
          numbering: { reference: 'md-numbers', level: 0 },
          spacing: { before: 40, after: 90, line: 262 },
          children: inlineRuns(content, { size: 19, font: BODY_FONT, color: INK }),
        }));
      }
      continue;
    }

    // paragraph (join soft-wrapped lines)
    let buf = [t]; i++;
    while (i < lines.length) {
      const nx = lines[i].trim();
      if (!nx || /^#{1,6}\s/.test(nx) || nx.startsWith('|') || nx.startsWith('>') ||
          /^[-*+]\s+/.test(nx) || /^\d+\.\s+/.test(nx) || /^(-{3,}|\*{3,}|_{3,})$/.test(nx) ||
          nx.startsWith('<!--')) break;
      buf.push(nx); i++;
    }
    const joined = buf.join(' ');
    const italicOnly = /^\*[^*].*\*$/.test(joined) && !joined.slice(1, -1).includes('*');
    out.push(P(inlineRuns(joined, {
      size: italicOnly ? 17 : 19,
      font: BODY_FONT,
      color: italicOnly ? MUTED : INK,
    })));
  }

  return out;
}

// ---------- title page ----------
function titlePage() {
  const gap = (h) => new Paragraph({ spacing: { before: 0, after: h }, children: [new TextRun({ text: '', size: 2 })] });
  return [
    gap(2100),
    new Paragraph({
      spacing: { after: 90 },
      children: [new TextRun({ text: 'EQUITY RESEARCH  ·  SHAREHOLDER ACTIVISM', size: 17, bold: true, color: ACCENT, font: HEAD_FONT, characterSpacing: 34 })],
    }),
    new Paragraph({
      spacing: { after: 40 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 10 } },
      children: [new TextRun({ text: '', size: 2 })],
    }),
    new Paragraph({
      spacing: { before: 190, after: 60 },
      children: [new TextRun({ text: 'Korea Activist Target Screen', size: 56, bold: true, color: NAVY, font: HEAD_FONT })],
    }),
    new Paragraph({
      spacing: { after: 330 },
      children: [new TextRun({ text: '20 Candidates', size: 40, color: SLATE, font: HEAD_FONT })],
    }),
    new Paragraph({
      spacing: { after: 110 },
      children: [new TextRun({
        text: 'A screen of KOSPI and KOSDAQ companies that are structurally sound but mis-managed: chronic TSR underperformance, capital-structure inefficiency and governance weakness, combined with the balance-sheet capacity and fragmented ownership needed to make a campaign work.',
        size: 21, color: INK, font: BODY_FONT,
      })],
    }),
    gap(560),
    ...[
      ['Date', '6 August 2026'],
      ['Perspective', 'Activist hedge fund · constructive to hostile · 2–4 year hold'],
      ['Universe', 'KOSPI + KOSDAQ · market cap above US$200m'],
      ['Working FX', '₩1,200 / US$1'],
    ].map(([k, v]) => new Paragraph({
      spacing: { after: 80 },
      children: [
        new TextRun({ text: k.padEnd(14, ' ') + '  ', size: 18, bold: true, color: SLATE, font: BODY_FONT }),
        new TextRun({ text: v, size: 18, color: INK, font: BODY_FONT }),
      ],
    })),
    gap(700),
    new Paragraph({
      spacing: { after: 0 },
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 8 } },
      children: [new TextRun({
        text: 'First-pass screen assembled from public sources. Figures marked ᵛ are verified against 2026-dated sources; figures marked ᵉ are estimates requiring verification before capital is committed. Not investment advice.',
        size: 15, italics: true, color: MUTED, font: BODY_FONT,
      })],
    }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

// ---------- assemble ----------
const src = process.argv[2];
const dest = process.argv[3];
const md = fs.readFileSync(src, 'utf8');
const body = convert(md, USABLE);

const doc = new Document({
  creator: 'Equity Research',
  title: 'Korea Activist Target Screen — 20 Candidates',
  description: 'Activist screen of the Korean market, August 2026',
  features: { updateFields: true },
  styles: {
    default: {
      document: { run: { font: BODY_FONT, size: 19, color: INK } },
      hyperlink: { run: { color: '1F5FA9', underline: {} } },
    },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 30, bold: true, color: NAVY, font: HEAD_FONT } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 25, bold: true, color: NAVY, font: HEAD_FONT } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 21, bold: true, color: SLATE, font: HEAD_FONT } },
    ],
  },
  numbering: {
    config: [
      { reference: 'md-bullets', levels: [{
        level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 340, hanging: 200 } }, run: { color: ACCENT } } }] },
      { reference: 'md-numbers', levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { bold: true, color: NAVY } } }] },
    ],
  },
  sections: [
    // Section 1 — title page, no header/footer
    {
      properties: {
        page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
        titlePage: true,
      },
      children: [
        ...titlePage(),
        new Paragraph({
          spacing: { after: 220 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 6 } },
          children: [new TextRun({ text: 'Contents', size: 30, bold: true, color: NAVY, font: HEAD_FONT })],
        }),
        new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-2' }),
      ],
    },
    // Section 2 — body
    {
      properties: {
        page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            spacing: { after: 30 },
            border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: RULE, space: 5 } },
            children: [new TextRun({
              text: 'Korea Activist Target Screen  ·  20 Candidates  ·  6 August 2026',
              size: 14, color: MUTED, font: BODY_FONT, characterSpacing: 12,
            })],
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [
              new TextRun({ text: 'Page ', size: 15, color: MUTED, font: BODY_FONT }),
              new TextRun({ children: [PageNumber.CURRENT], size: 15, color: MUTED, font: BODY_FONT, bold: true }),
              new TextRun({ text: ' of ', size: 15, color: MUTED, font: BODY_FONT }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 15, color: MUTED, font: BODY_FONT }),
            ],
          })],
        }),
      },
      children: body,
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(dest, buf);
  console.log('wrote', dest, (buf.length / 1024).toFixed(0) + ' KB');
  console.log('body elements:', body.length);
});
