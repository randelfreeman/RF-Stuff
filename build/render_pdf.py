#!/usr/bin/env python3
"""Render the report markup into a printable institutional research PDF."""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

LIB = '/usr/share/fonts/truetype/liberation/'
for name, f in (('Body', 'LiberationSerif-Regular'), ('Body-B', 'LiberationSerif-Bold'),
                ('Body-I', 'LiberationSerif-Italic'), ('Body-BI', 'LiberationSerif-BoldItalic'),
                ('Sans', 'LiberationSans-Regular'), ('Sans-B', 'LiberationSans-Bold')):
    pdfmetrics.registerFont(TTFont(name, LIB + f + '.ttf'))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-B', italic='Body-I', boldItalic='Body-BI')
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='Sans-B', italic='Sans', boldItalic='Sans-B')

NAVY   = colors.HexColor('#0F2B46')
ACCENT = colors.HexColor('#A86B1E')
GREY   = colors.HexColor('#555F6B')
BLACK  = colors.HexColor('#1A1A1A')
ALT    = colors.HexColor('#F2F4F7')
RULE   = colors.HexColor('#C8CDD4')
CALLBG = colors.HexColor('#FAF7F1')

PW, PH = A4
LM = RM = 17 * mm
TM = 16 * mm
BM = 15 * mm
CW = PW - LM - RM

S = {}
S['body'] = ParagraphStyle('body', fontName='Body', fontSize=8.9, leading=12.3,
                           alignment=TA_JUSTIFY, textColor=BLACK, spaceAfter=5)
S['h1'] = ParagraphStyle('h1', fontName='Sans-B', fontSize=19, leading=22.5,
                         textColor=NAVY, spaceBefore=2, spaceAfter=4)
S['sub'] = ParagraphStyle('sub', fontName='Body-I', fontSize=8.4, leading=11.5,
                          textColor=GREY, spaceAfter=9)
S['h2'] = ParagraphStyle('h2', fontName='Sans-B', fontSize=12.4, leading=15,
                         textColor=NAVY, spaceBefore=12, spaceAfter=5)
S['h3'] = ParagraphStyle('h3', fontName='Sans-B', fontSize=10.1, leading=13,
                         textColor=NAVY, spaceBefore=9, spaceAfter=3)
S['h4'] = ParagraphStyle('h4', fontName='Body-B', fontSize=9.2, leading=12,
                         textColor=ACCENT, spaceBefore=7, spaceAfter=2)
S['bul'] = ParagraphStyle('bul', parent=S['body'], alignment=TA_LEFT,
                          leftIndent=9, firstLineIndent=-9, spaceAfter=2.6)
S['bul2'] = ParagraphStyle('bul2', parent=S['bul'], leftIndent=22, firstLineIndent=-9)
S['num'] = ParagraphStyle('num', parent=S['body'], alignment=TA_LEFT,
                          leftIndent=15, firstLineIndent=-15, spaceAfter=2.6)
S['call'] = ParagraphStyle('call', parent=S['body'], fontSize=8.9, leading=12.4,
                           leftIndent=8, rightIndent=4, spaceBefore=3, spaceAfter=3)
S['small'] = ParagraphStyle('small', fontName='Body-I', fontSize=7.1, leading=9.4,
                            textColor=GREY, alignment=TA_LEFT, spaceAfter=4)
S['th'] = ParagraphStyle('th', fontName='Sans-B', fontSize=7.3, leading=9.2,
                         textColor=colors.white, alignment=TA_LEFT)
S['td'] = ParagraphStyle('td', fontName='Body', fontSize=7.3, leading=9.4,
                         textColor=BLACK, alignment=TA_LEFT)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline(t):
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', t)
    return t


def rule_flowable(colour=NAVY, thick=0.9, space=2):
    from reportlab.platypus import Flowable

    class R(Flowable):
        def __init__(self):
            super().__init__(); self.width = CW; self.height = thick + space
        def draw(self):
            self.canv.setStrokeColor(colour); self.canv.setLineWidth(thick)
            self.canv.line(0, space, CW, space)
    return R()


def col_widths(rows, ncol):
    """Proportional widths from content mass, with a per-column floor set by the
    widest single word so header labels never break mid-word."""
    pad = 6.8  # cell left+right padding
    scores, floors = [], []
    for c in range(ncol):
        cells = [re.sub(r'\*', '', r[c]) for r in rows]
        longest = max(len(x) for x in cells)
        mean = sum(len(x) for x in cells) / len(cells)
        scores.append(max(6.0, 0.45 * longest + 0.55 * mean) ** 0.72)
        widest_word = 0.0
        for ri, cell in enumerate(cells):
            fnt = 'Sans-B' if ri == 0 else 'Body'
            for w in cell.replace('/', '/ ').split():
                widest_word = max(widest_word, pdfmetrics.stringWidth(w, fnt, 7.3))
        floors.append(min(widest_word + pad, CW * 0.30))
    # base proportional allocation
    tot = sum(scores)
    w = [CW * sc / tot for sc in scores]
    # lift any column below its floor, then take the excess back from the slack
    for _ in range(6):
        deficit = sum(max(0.0, floors[i] - w[i]) for i in range(ncol))
        if deficit < 0.25:
            break
        slack = [max(0.0, w[i] - floors[i]) for i in range(ncol)]
        pool = sum(slack)
        if pool <= 0:
            break
        take = min(deficit, pool)
        for i in range(ncol):
            w[i] -= take * (slack[i] / pool)
            if w[i] < floors[i]:
                w[i] = floors[i]
        f = CW / sum(w)
        w = [x * f for x in w]
    f = CW / sum(w)
    return [x * f for x in w]


def make_table(rows):
    ncol = len(rows[0])
    widths = col_widths(rows, ncol)
    data = [[Paragraph(inline(v), S['th'] if ri == 0 else S['td']) for v in row]
            for ri, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.35, RULE),
        ('LINEBELOW', (0, 0), (-1, 0), 0.7, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.4),
    ]
    for ri in range(2, len(rows), 2):
        cmds.append(('BACKGROUND', (0, ri), (-1, ri), ALT))
    t.setStyle(TableStyle(cmds))
    return t


def make_callout(text):
    p = Paragraph(inline(text), S['call'])
    t = Table([[p]], colWidths=[CW], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CALLBG),
        ('LINEBEFORE', (0, 0), (0, -1), 2.4, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def on_page(canv, doc):
    canv.saveState()
    canv.setFont('Body', 6.4); canv.setFillColor(GREY)
    canv.drawString(LM, 9 * mm,
                    'Liontrust Asset Management PLC (LIO LN) — Initiation of Coverage · 30 August 2026')
    canv.drawRightString(PW - RM, 9 * mm,
                         'For discussion purposes only — not investment advice · p.%d' % doc.page)
    canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
    canv.line(LM, 11.5 * mm, PW - RM, 11.5 * mm)
    canv.restoreState()


def build(src, out):
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=LM, rightMargin=RM,
                          topMargin=TM, bottomMargin=BM,
                          title='Liontrust Asset Management PLC (LIO LN) — Equity Research',
                          author='Institutional Equity Research', subject='LIO LN Initiation of Coverage')
    frame = Frame(LM, BM, CW, PH - TM - BM, id='f', leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=on_page)])

    story = []
    lines = open(src, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        ln = lines[i]; s = ln.strip()
        if s == '[PAGEBREAK]':
            story.append(PageBreak()); i += 1; continue
        if not s:
            i += 1; continue

        if s.startswith('|'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i].strip()); i += 1
            rows = [[c.strip() for c in r.strip('|').split('|')] for r in block
                    if not re.match(r'^\|[\s\-:|]+\|$', r)]
            n = max(len(r) for r in rows)
            rows = [r + [''] * (n - len(r)) for r in rows]
            story.append(Spacer(1, 3))
            story.append(make_table(rows))
            story.append(Spacer(1, 7))
            continue

        if s.startswith('#### '):
            story.append(Paragraph(inline(s[5:]), S['h4'])); i += 1; continue
        if s.startswith('### '):
            story.append(Paragraph(inline(s[4:]), S['h3'])); i += 1; continue
        if s.startswith('## '):
            story.append(Spacer(1, 5))
            story.append(Paragraph(inline(s[3:]), S['h2']))
            story.append(rule_flowable()); story.append(Spacer(1, 3)); i += 1; continue
        if s.startswith('# '):
            story.append(Paragraph(inline(s[2:]), S['h1'])); i += 1; continue
        if s.startswith('@@ '):
            story.append(Paragraph(inline(s[3:]), S['sub'])); i += 1; continue
        if s.startswith('> '):
            story.append(Spacer(1, 4)); story.append(make_callout(s[2:]))
            story.append(Spacer(1, 7)); i += 1; continue
        if s.startswith('~ '):
            story.append(Paragraph(inline(s[2:]), S['small'])); i += 1; continue

        m = re.match(r'^(\s*)-\s+(.*)$', ln.rstrip())
        if m:
            d = len(m.group(1)) // 2
            story.append(Paragraph('•&nbsp;&nbsp;' + inline(m.group(2)),
                                   S['bul'] if d == 0 else S['bul2']))
            i += 1; continue

        m = re.match(r'^(\s*)(\d+)\.\s+(.*)$', ln.rstrip())
        if m:
            story.append(Paragraph('<b>%s.</b>&nbsp;&nbsp;%s' % (m.group(2), inline(m.group(3))), S['num']))
            i += 1; continue

        story.append(Paragraph(inline(s), S['body'])); i += 1

    doc.build(story)
    print('wrote', out)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
