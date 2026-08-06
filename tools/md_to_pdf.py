#!/usr/bin/env python3
"""Render the activist-screen markdown to a formatted PDF.

Same feature subset as tools/md_to_docx.js: ATX headings, pipe tables,
bullet/ordered lists, blockquote callouts, and inline **bold** / *italic* /
`code` / [links](url).

Usage: python tools/md_to_pdf.py input.md output.pdf
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph,
    Spacer, Table, TableStyle,
)

# Base-14 Helvetica has no ₩ and no modifier letters. Liberation Sans is
# metric-compatible with Arial and covers everything this document uses.
_LIB = "/usr/share/fonts/truetype/liberation"
try:
    for _name, _file in [("Doc", "LiberationSans-Regular.ttf"),
                         ("Doc-Bold", "LiberationSans-Bold.ttf"),
                         ("Doc-Italic", "LiberationSans-Italic.ttf"),
                         ("Doc-BoldItalic", "LiberationSans-BoldItalic.ttf"),
                         ("DocMono", "LiberationMono-Regular.ttf")]:
        pdfmetrics.registerFont(TTFont(_name, f"{_LIB}/{_file}"))
    pdfmetrics.registerFontFamily("Doc", normal="Doc", bold="Doc-Bold",
                                  italic="Doc-Italic", boldItalic="Doc-BoldItalic")
    BASE, BOLD, ITAL, MONO = "Doc", "Doc-Bold", "Doc-Italic", "DocMono"
except Exception:  # fall back to base-14 rather than fail the build
    BASE, BOLD, ITAL, MONO = ("Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier")

NAVY = colors.HexColor("#1F3557")
SLATE = colors.HexColor("#3E5871")
ACCENT = colors.HexColor("#9B6B2F")
RULE = colors.HexColor("#C3CCD8")
ZEBRA = colors.HexColor("#F2F5F8")
CALLOUT = colors.HexColor("#FBF4E7")
INK = colors.HexColor("#1A1A1A")
MUTED = colors.HexColor("#5C6B7A")

MARGIN = 0.72 * inch
USABLE = LETTER[0] - 2 * MARGIN

S = {
    "body": ParagraphStyle("body", fontName=BASE, fontSize=8.6, leading=12.2,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5),
    "h1": ParagraphStyle("h1", fontName=BOLD, fontSize=15, leading=19,
                         textColor=NAVY, spaceBefore=2, spaceAfter=9),
    "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=11.5, leading=14.5,
                         textColor=NAVY, spaceBefore=13, spaceAfter=5),
    "h2g": ParagraphStyle("h2g", fontName=BOLD, fontSize=10, leading=13,
                          textColor=ACCENT, spaceBefore=16, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=9.4, leading=12.5,
                         textColor=SLATE, spaceBefore=9, spaceAfter=4),
    "li": ParagraphStyle("li", fontName=BASE, fontSize=8.6, leading=12.2,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=4,
                         leftIndent=13, bulletIndent=3),
    "cell": ParagraphStyle("cell", fontName=BASE, fontSize=7.1, leading=9.4, textColor=INK),
    "cellh": ParagraphStyle("cellh", fontName=BOLD, fontSize=7.1, leading=9.4,
                            textColor=colors.white),
    "callout": ParagraphStyle("callout", fontName=BASE, fontSize=8.2, leading=11.6,
                              textColor=colors.HexColor("#4A3A1E"), alignment=TA_JUSTIFY),
    "quote": ParagraphStyle("quote", fontName=ITAL, fontSize=8.2, leading=11.6,
                            textColor=MUTED, spaceAfter=5),
}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    """Markdown inline -> reportlab mini-HTML."""
    t = esc(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               r'<link href="\2" color="#1F5FA9"><u>\1</u></link>', t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="DocMono" size="7.6">\1</font>', t)
    # provenance markers -> real superscripts
    t = t.replace("\u1d5b", "<super>v</super>").replace("\u1d49", "<super>e</super>")
    return t


def split_row(line):
    s = line.strip().strip("|")
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def is_div(line):
    return bool(re.match(r"^\s*\|?[\s:|-]*-{2,}[\s:|-]*\|?\s*$", line)) and "-" in line


def plain(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.replace("**", "").replace("*", "").replace("`", "")


def col_widths(rows, total):
    n = len(rows[0])
    w = [0] * n
    for r in rows:
        for i, c in enumerate(r[:n]):
            w[i] = max(w[i], min(len(plain(c)), 90))
    soft = [max(x, 4) ** 0.72 for x in w]
    s = sum(soft)
    mn = total / (n * 3.2)
    out = [max(mn, (x / s) * total) for x in soft]
    k = total / sum(out)
    return [x * k for x in out]


def build_table(rows, total):
    n = len(rows[0])
    norm = [(r + [""] * n)[:n] for r in rows]
    widths = col_widths(norm, total)
    data = [[Paragraph(inline(c), S["cellh"]) for c in norm[0]]]
    data += [[Paragraph(inline(c), S["cell"]) for c in r] for r in norm[1:]]
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle(st))
    return t


def build_callout(lines, total):
    inner = [Paragraph(inline(l), S["callout"]) for l in lines if l.strip()]
    t = Table([[inner]], colWidths=[total])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CALLOUT),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, ACCENT),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


def parse(md):
    lines = md.split("\n")
    flow = []
    i = 0
    seen_title = False
    while i < len(lines):
        raw = lines[i]
        t = raw.strip()
        if not t or t.startswith("<!--"):
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", t):
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", t)
        if h:
            lvl, txt = len(h[1]), h[2].strip()
            if lvl == 1 and not seen_title:
                seen_title = True
                i += 1
                while i < len(lines) and not re.match(r"^##\s", lines[i].strip()):
                    i += 1
                continue
            if lvl == 2:
                flow.append(PageBreak())
                flow.append(Paragraph(inline(txt), S["h1"]))
                flow.append(Table([[""]], colWidths=[USABLE], rowHeights=[1.6],
                                  style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY)])))
                flow.append(Spacer(1, 7))
            elif lvl == 3:
                grp = bool(re.match(r"^Type [A-D]\b", txt))
                flow.append(Paragraph(inline(txt.upper() if grp else txt),
                                      S["h2g"] if grp else S["h2"]))
            else:
                flow.append(Paragraph(inline(txt), S["h3"]))
            i += 1
            continue
        if t.startswith("|") and i + 1 < len(lines) and is_div(lines[i + 1]):
            rows = [split_row(lines[i])]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            flow.append(build_table(rows, USABLE))
            flow.append(Spacer(1, 8))
            continue
        if t.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            flow.append(build_callout(buf, USABLE))
            flow.append(Spacer(1, 8))
            continue
        if re.match(r"^[-*+]\s+", t):
            while i < len(lines) and re.match(r"^[-*+]\s+", lines[i].strip()):
                c = re.sub(r"^[-*+]\s+", "", lines[i].strip())
                i += 1
                while (i < len(lines) and lines[i].strip()
                       and re.match(r"^\s{2,}\S", lines[i])
                       and not re.match(r"^([-*+]|\d+\.)\s+", lines[i].strip())):
                    c += " " + lines[i].strip()
                    i += 1
                flow.append(Paragraph(inline(c), S["li"], bulletText="•"))
            continue
        if re.match(r"^\d+\.\s+", t):
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                m = re.match(r"^(\d+)\.\s+(.*)$", lines[i].strip())
                num, c = m[1], m[2]
                i += 1
                while (i < len(lines) and lines[i].strip()
                       and re.match(r"^\s{2,}\S", lines[i])
                       and not re.match(r"^([-*+]|\d+\.)\s+", lines[i].strip())):
                    c += " " + lines[i].strip()
                    i += 1
                flow.append(Paragraph(inline(c), S["li"], bulletText=f"{num}."))
            continue
        buf = [t]
        i += 1
        while i < len(lines):
            nx = lines[i].strip()
            if (not nx or re.match(r"^#{1,6}\s", nx) or nx.startswith(("|", ">", "<!--"))
                    or re.match(r"^([-*+]|\d+\.)\s+", nx)
                    or re.match(r"^(-{3,}|\*{3,}|_{3,})$", nx)):
                break
            buf.append(nx)
            i += 1
        j = " ".join(buf)
        italic_only = bool(re.match(r"^\*[^*].*\*$", j)) and "*" not in j[1:-1]
        flow.append(Paragraph(inline(j), S["quote"] if italic_only else S["body"]))
    return flow


def title_page():
    return [
        Spacer(1, 2.0 * inch),
        Paragraph("EQUITY RESEARCH &#183; SHAREHOLDER ACTIVISM",
                  ParagraphStyle("k", fontName=BOLD, fontSize=8.5,
                                 textColor=ACCENT, leading=12)),
        Spacer(1, 5),
        Table([[""]], colWidths=[USABLE], rowHeights=[2],
              style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY)])),
        Spacer(1, 15),
        Paragraph("Korea Activist Target Screen",
                  ParagraphStyle("t", fontName=BOLD, fontSize=28,
                                 textColor=NAVY, leading=33)),
        Paragraph("20 Candidates",
                  ParagraphStyle("s", fontName=BASE, fontSize=20,
                                 textColor=SLATE, leading=26, spaceAfter=16)),
        Paragraph(
            "A screen of KOSPI and KOSDAQ companies that are structurally sound but "
            "mis-managed: chronic TSR underperformance, capital-structure inefficiency "
            "and governance weakness, combined with the balance-sheet capacity and "
            "fragmented ownership needed to make a campaign work.",
            ParagraphStyle("l", fontName=BASE, fontSize=10, leading=14.5, textColor=INK)),
        Spacer(1, 34),
    ] + [
        Paragraph(f"<b>{k}</b>&nbsp;&nbsp;&nbsp;{v}",
                  ParagraphStyle("m", fontName=BASE, fontSize=9, leading=14, textColor=INK))
        for k, v in [("Date", "6 August 2026"),
                     ("Perspective", "Activist hedge fund &#183; constructive to hostile &#183; 2–4 year hold"),
                     ("Universe", "KOSPI + KOSDAQ &#183; market cap above US$200m"),
                     ("Working FX", "₩1,200 / US$1")]
    ] + [
        Spacer(1, 40),
        Paragraph(
            "First-pass screen assembled from public sources. Figures marked ᵛ are verified "
            "against 2026-dated sources; figures marked ᵉ are estimates requiring verification "
            "before capital is committed. Not investment advice.",
            ParagraphStyle("d", fontName=ITAL, fontSize=7.5, leading=10.5,
                           textColor=MUTED)),
    ]


def decorate(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont(BASE, 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, LETTER[1] - MARGIN + 12,
                          "Korea Activist Target Screen  ·  20 Candidates  ·  6 August 2026")
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        canvas.line(MARGIN, LETTER[1] - MARGIN + 7, LETTER[0] - MARGIN, LETTER[1] - MARGIN + 7)
        canvas.drawRightString(LETTER[0] - MARGIN, MARGIN - 16, f"Page {doc.page}")
    canvas.restoreState()


def main():
    src, dst = sys.argv[1], sys.argv[2]
    md = open(src, encoding="utf-8").read()
    doc = BaseDocTemplate(dst, pagesize=LETTER,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=MARGIN,
                          title="Korea Activist Target Screen — 20 Candidates",
                          author="Equity Research")
    frame = Frame(MARGIN, MARGIN, USABLE, LETTER[1] - 2 * MARGIN, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])
    doc.build(title_page() + parse(md))
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
