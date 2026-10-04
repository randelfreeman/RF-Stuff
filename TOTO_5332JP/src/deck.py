"""IC-memo style 16:9 slide primitives on a reportlab canvas (mirrors the GOOS template)."""
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table, TableStyle, Frame
from reportlab.lib.styles import ParagraphStyle
import render  # registers fonts

W, H = 960, 540
NAVY = colors.HexColor('#14233D'); NAVY2 = colors.HexColor('#2B3A55'); BLUE = colors.HexColor('#2F6FD0')
INK = colors.HexColor('#16243D'); GREY = colors.HexColor('#5E6878'); LIGHT = colors.HexColor('#F1F3F7')
RED = colors.HexColor('#B23A2E'); SLATE = colors.HexColor('#7D8799'); WHITE = colors.white
LB = colors.HexColor('#7EA6E8')

def ps(name, size, font='Lib', color=INK, lead=None, align=0):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead or size * 1.32, textColor=color, alignment=align)

BUL = ps('bul', 9.6); BULW = ps('bulw', 10, color=WHITE)
TD = ps('td', 8.2, lead=10.2, align=1); TDL = ps('tdl', 8.2, font='Lib-B', lead=10.2)
TH = ps('th', 8.2, font='Lib-B', color=WHITE, lead=10.2, align=1)


class Deck:
    def __init__(self, fn, footer):
        self.c = canvas.Canvas(fn, pagesize=(W, H)); self.footer = footer
        self.c.setTitle('TOTO (5332 JP) - Investment Committee Memo')

    def para(self, text, x, y_top, w, style, h=400):
        p = Paragraph(render._pdf_text(text), style); _, ph = p.wrap(w, h); p.drawOn(self.c, x, y_top - ph); return ph

    def header(self, kicker, tag, title):
        c = self.c
        c.setFillColor(WHITE); c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFont('Lib-B', 8.6); c.setFillColor(BLUE)
        c.drawString(34, H - 34, ' '.join(kicker.upper()) if False else kicker.upper())
        tw = c.stringWidth(tag.upper(), 'Lib-B', 8) + 40
        c.setFillColor(NAVY2); c.rect(W - 34 - tw, H - 46, tw, 22, fill=1, stroke=0)
        c.setFillColor(WHITE); c.setFont('Lib-B', 8); c.drawCentredString(W - 34 - tw / 2, H - 38, tag.upper())
        c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(34, H - 52, W - 34, H - 52)
        self.para(title, 34, H - 60, W - 68, ps('t', 20.5, 'Lib-B', INK, 25))
        c.setFont('Lib', 6.8); c.setFillColor(GREY); c.drawString(34, 16, self.footer)
        c.drawRightString(W - 34, 16, str(c.getPageNumber()))

    def tiles(self, items, y_top=H - 122, h=88, x0=34, w_total=W - 68, dark=False, hi=None):
        n = len(items); gap = 2; w = (w_total - gap * (n - 1)) / n
        for i, (big, small) in enumerate(items):
            x = x0 + i * (w + gap)
            fill = BLUE if (hi is not None and i == hi) else (NAVY if dark else LIGHT)
            self.c.setFillColor(fill); self.c.rect(x, y_top - h, w, h, fill=1, stroke=0)
            col = WHITE if dark or hi == i else INK
            self.para(big, x + 12, y_top - 12, w - 20, ps('big', 18, 'Lib-B', col, 21))
            self.para(small, x + 12, y_top - 46, w - 20, ps('sm', 7.6, 'Lib', colors.HexColor('#C9D3E6') if (dark or hi == i) else GREY, 9.6))
        return y_top - h

    def col_head(self, text, x, y, w, color=INK):
        self.c.setFont('Lib-B', 10.5); self.c.setFillColor(color); self.c.drawString(x, y, text)
        self.c.setStrokeColor(colors.HexColor('#C9CED8')); self.c.setLineWidth(0.8); self.c.line(x, y - 7, x + w, y - 7)
        return y - 16

    def bullets(self, items, x, y, w, style=BUL, sq=BLUE, gap=8):
        for it in items:
            self.c.setFillColor(sq); self.c.rect(x, y - 7, 7, 4.5, fill=1, stroke=0)
            h = self.para(it, x + 16, y, w - 16, style)
            y -= h + gap
        return y

    def callout(self, text, x, y_top, w, dark=True, h=None):
        st = ps('co', 9.6, 'Lib', WHITE if dark else INK, 13)
        p = Paragraph(render._pdf_text(text), st); _, ph = p.wrap(w - 30, 300); hh = h or ph + 22
        self.c.setFillColor(NAVY2 if dark else LIGHT); self.c.rect(x, y_top - hh, w, hh, fill=1, stroke=0)
        self.c.setFillColor(BLUE if dark else NAVY); self.c.rect(x, y_top - hh, 3, hh, fill=1, stroke=0)
        p.drawOn(self.c, x + 16, y_top - 11 - ph)
        return y_top - hh

    def table(self, header, rows, x, y_top, widths, first_bold=True, hl_col=None, fs=None):
        td = TD if fs is None else ps('tdx', fs, lead=fs * 1.24, align=1)
        tdl = TDL if fs is None else ps('tdlx', fs, 'Lib-B', lead=fs * 1.24)
        th = TH if fs is None else ps('thx', fs, 'Lib-B', WHITE, fs * 1.24, 1)
        data = [[Paragraph(render._pdf_text(h), ps('th0', th.fontSize, 'Lib-B', WHITE, th.leading, 0) if i == 0 else th) for i, h in enumerate(header)]]
        for r in rows:
            row = []
            for i, v in enumerate(r):
                if i == 0 and first_bold: row.append(Paragraph(render._pdf_text(v), tdl))
                elif hl_col is not None and i == hl_col: row.append(Paragraph('<font color="#2F6FD0"><b>%s</b></font>' % render._pdf_text(v), td))
                else: row.append(Paragraph(render._pdf_text(v), td))
            data.append(row)
        t = Table(data, colWidths=widths)
        st = [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
              ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#D5D9E0')),
              ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
        for i in range(2, len(data), 2): st.append(('BACKGROUND', (0, i), (-1, i), LIGHT))
        t.setStyle(TableStyle(st)); tw, th_ = t.wrap(0, 0); t.drawOn(self.c, x, y_top - th_)
        return y_top - th_

    def note(self, text, x, y, w):
        return self.para('<i>%s</i>' % text, x, y, w, ps('n', 7.4, 'Lib-I', GREY, 9.4))

    def image(self, path, x, y_top, w):
        from reportlab.lib.utils import ImageReader
        ir = ImageReader(path); iw, ih = ir.getSize(); h = w * ih / iw
        self.c.drawImage(ir, x, y_top - h, w, h); return y_top - h

    def dark_bg(self):
        self.c.setFillColor(NAVY); self.c.rect(0, 0, W, H, fill=1, stroke=0)

    def next(self):
        self.c.showPage()

    def save(self):
        self.c.save()
