"""GOOS-style 16:9 investment-committee deck components (HTML -> PDF via Chromium)."""
import html as _h
import base64, os

def esc(s):
    return _h.escape(str(s), quote=False)

def rich(s):
    """Allow **bold** inside strings."""
    out, bold = [], False
    parts = str(s).split("**")
    for i, p in enumerate(parts):
        t = esc(p)
        out.append(f"<b>{t}</b>" if i % 2 == 1 else t)
    return "".join(out)

CSS = r"""
@page { size: 13.333in 7.5in; margin: 0 }
* { box-sizing: border-box; }
html, body { overflow: hidden; } body { margin: 0; font-family: "Liberation Sans", Arial, "IPAGothic", sans-serif; color: #15233F; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.slide { width: 13.36in; height: 7.5in; padding: 0.25in 0.47in 0.3in 0.47in; page-break-after: always; position: relative; overflow: hidden; background: #fff; }
.slide:last-child { page-break-after: auto; }
.kicker { font-size: 11.5pt; letter-spacing: 0.12em; font-weight: 700; color: #2F6FD0; text-transform: uppercase; margin-top: 0.12in; }
.tag { position: absolute; right: 0.47in; top: 0.25in; background: #2C3A55; color: #fff; font-weight: 700; font-size: 10pt; letter-spacing: 0.12em; padding: 0.1in 0.24in; text-transform: uppercase; }
.rule { border-bottom: 1.6px solid #15233F; margin-top: 0.12in; }
h1.title { font-size: 25pt; margin: 0.16in 0 0.22in 0; font-weight: 700; color: #15233F; line-height: 1.12; }
.cols { display: flex; gap: 0.4in; }
.col { flex: 1; min-width: 0; }
.col.w60 { flex: 1.5; } .col.w40 { flex: 1; }
h3 { font-size: 13.5pt; margin: 0 0 0.08in 0; color: #15233F; padding-bottom: 0.07in; border-bottom: 1.2px solid #D7DBE2; }
ul.b { list-style: none; padding: 0; margin: 0.1in 0 0 0; }
ul.b li { position: relative; padding-left: 0.3in; font-size: 11.2pt; line-height: 1.38; margin-bottom: 0.15in; color: #15233F; }
ul.b li:before { content: ""; position: absolute; left: 0; top: 0.07in; width: 0.13in; height: 0.075in; background: #2F6FD0; }
ul.b.grey li:before { background: #7C8596; }
ul.b.tight li { margin-bottom: 0.08in; font-size: 10.6pt; }
.tiles { display: flex; gap: 0.04in; margin: 0.05in 0 0.25in 0; }
.tile { flex: 1; background: #F1F3F7; padding: 0.2in 0.22in; min-height: 1.45in; }
.tile .v { font-size: 25pt; font-weight: 700; color: #15233F; line-height: 1.05; }
.tile .l { font-size: 10pt; color: #5B6577; margin-top: 0.22in; line-height: 1.3; }
.tile.hl { background: #2F6FD0; } .tile.hl .v, .tile.hl .l { color: #fff; }
table.t { border-collapse: collapse; width: 100%; font-size: 10pt; }
table.t th { background: #15233F; color: #fff; font-weight: 700; padding: 0.085in 0.1in; text-align: center; border: 1px solid #15233F; }
table.t th:first-child { text-align: left; }
table.t td { padding: 0.07in 0.1in; border: 1px solid #DADDE3; text-align: center; color: #15233F; }
table.t td:first-child { text-align: left; font-weight: 700; }
table.t tr:nth-child(even) td { background: #F1F3F7; }
table.t td.hl { color: #2F6FD0; font-weight: 700; }
table.t.small { font-size: 9pt; }
table.t.small td, table.t.small th { padding: 0.05in 0.07in; }
.note { font-size: 9pt; color: #5B6577; font-style: italic; margin-top: 0.08in; line-height: 1.35; }
.callout { background: #F1F3F7; border-left: 0.07in solid #15233F; padding: 0.2in 0.3in; font-size: 11.5pt; line-height: 1.45; color: #15233F; }
.callout.dark { background: #2C3A55; color: #fff; border-left-color: #5B8FE0; }
.bottom { position: absolute; left: 0.47in; right: 0.47in; bottom: 0.38in; }
.cover { background: #15233F; color: #fff; padding: 0.75in 0.6in; }
.cover .kick { color: #6FA0EE; font-weight: 700; font-size: 12.5pt; letter-spacing: 0.14em; }
.cover .kick:after { content: ""; display: block; width: 1.15in; border-bottom: 2.5px solid #2F6FD0; margin-top: 0.1in; }
.cover h1 { font-size: 40pt; line-height: 1.12; margin: 0.42in 0 0.3in 0; }
.cover .sub { font-size: 16pt; color: #D3DAE8; margin-bottom: 0.32in; }
.btn { display: inline-block; padding: 0.15in 0.22in; font-weight: 700; font-size: 13pt; margin-right: 0.08in; }
.btn.fill { background: #2F6FD0; color: #fff; }
.btn.line { border: 1.6px solid #5B8FE0; color: #fff; }
.facts { display: flex; gap: 0.25in; margin-top: 0.32in; font-size: 10.5pt; color: #D3DAE8; line-height: 1.6; }
.facts div { width: 1.45in; }
.coverright { position: absolute; left: 7.05in; top: 0.6in; bottom: 0.9in; border-left: 1px solid #2B3A58; padding-left: 0.42in; width: 5.6in; }
.big { font-size: 30pt; font-weight: 700; margin-top: 0.42in; }
.big.blue { color: #8FB4F0; }
.bigl { font-size: 11pt; color: #C9D3E6; margin-top: 0.1in; padding-bottom: 0.2in; border-bottom: 1px solid #2B3A58; line-height: 1.35; }
.foot { position: absolute; left: 0.6in; right: 0.6in; bottom: 0.4in; border-top: 1px solid #2B3A58; padding-top: 0.15in; font-size: 10pt; color: #8D97AA; }
.cal { display: flex; align-items: center; margin-bottom: 0.16in; }
.cal .d { width: 2.3in; min-height: 0.56in; background: #15233F; color: #fff; font-weight: 700; font-size: 10.5pt; display: flex; align-items: center; justify-content: center; text-align: center; padding: 0.05in; }
.cal .x { flex: 1; padding: 0 0.3in; }
.cal .x .h { font-weight: 700; font-size: 12pt; }
.cal .x .s { color: #5B6577; font-size: 10.5pt; margin-top: 0.03in; line-height: 1.3; }
.cal .p { width: 1.7in; text-align: center; color: #fff; font-weight: 700; font-size: 10pt; padding: 0.12in 0; }
.p.crit { background: #B7392F; } .p.high { background: #2F6FD0; } .p.med { background: #7C8596; }
.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; background: #F1F3F7; }
.grid .cell { padding: 0.24in 0.27in; border-right: 1px solid #D0D4DC; border-bottom: 1px solid #D0D4DC; min-height: 2.3in; }
.grid .n { color: #B7392F; font-weight: 700; font-size: 13pt; }
.grid .h { font-weight: 700; font-size: 13pt; margin: 0.16in 0 0.12in 0; }
.grid .s { color: #5B6577; font-size: 10.5pt; line-height: 1.4; }
.dec { background: #15233F; color: #fff; }
.dec .kicker { color: #6FA0EE; }
.dec h1.title { color: #fff; font-size: 34pt; }
.dec .tile { background: #15233F; border: 1px solid #22314F; }
.dec .tile .v { color: #fff; } .dec .tile .l { color: #C9D3E6; }
.dec .tile.hl { background: #2F6FD0; }
.dec ul.b li { color: #fff; } .dec ul.b li:before { background: #5B8FE0; }
.panel { background: #fff; color: #15233F; padding: 0.28in 0.32in; }
.panel h3 { border-bottom: 2.5px solid #2F6FD0; display: inline-block; padding-bottom: 0.08in; }
.panel p { font-size: 11pt; line-height: 1.45; margin: 0.18in 0 0.25in 0; }
img.chart { width: 100%; display: block; }
.small { font-size: 9.5pt; }
"""

def page(slides):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(slides)}</body></html>"

def header(kicker, tag, title):
    return f"<div class='kicker'>{esc(kicker)}</div><div class='tag'>{esc(tag)}</div><div class='rule'></div><h1 class='title'>{rich(title)}</h1>"

def slide(inner, cls=""):
    return f"<div class='slide {cls}'>{inner}</div>"

def bullets(items, grey=False, tight=False):
    cls = "b" + (" grey" if grey else "") + (" tight" if tight else "")
    lis = []
    for it in items:
        if isinstance(it, (tuple, list)):
            lead, rest = it
            lis.append(f"<li><b>{esc(lead)}</b>&nbsp; {rich(rest)}</li>")
        else:
            lis.append(f"<li>{rich(it)}</li>")
    return f"<ul class='{cls}'>{''.join(lis)}</ul>"

def tiles(items, hl_last=False):
    out = []
    for i, (v, l) in enumerate(items):
        hl = " hl" if (hl_last and i == len(items) - 1) else ""
        out.append(f"<div class='tile{hl}'><div class='v'>{esc(v)}</div><div class='l'>{rich(l)}</div></div>")
    return f"<div class='tiles'>{''.join(out)}</div>"

def table(headers, rows, hl_col=None, small=False, col_widths=None):
    cw = ""
    if col_widths:
        cw = "<colgroup>" + "".join(f"<col style='width:{w}'>" for w in col_widths) + "</colgroup>"
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = []
    for r in rows:
        tds = []
        for j, c in enumerate(r):
            cls = " class='hl'" if (hl_col is not None and j == hl_col) else ""
            tds.append(f"<td{cls}>{rich(c)}</td>")
        trs.append("<tr>" + "".join(tds) + "</tr>")
    return f"<table class='t{' small' if small else ''}'>{cw}<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table>"

def callout(lead, text, dark=False, style=""):
    return f"<div class='callout{' dark' if dark else ''}' style='{style}'><b>{esc(lead)}</b> {rich(text)}</div>"

def img(path, style=""):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"<img class='chart' style='{style}' src='data:image/png;base64,{b64}'/>"

def cal_row(date, head, sub, prio):
    cls = {"CRITICAL": "crit", "HIGH": "high", "MEDIUM": "med"}.get(prio, "med")
    return f"<div class='cal'><div class='d'>{esc(date)}</div><div class='x'><div class='h'>{esc(head)}</div><div class='s'>{rich(sub)}</div></div><div class='p {cls}'>{esc(prio)}</div></div>"

def risk_grid(items):
    cells = "".join(f"<div class='cell'><div class='n'>{i+1:02d}</div><div class='h'>{esc(h)}</div><div class='s'>{rich(s)}</div></div>" for i, (h, s) in enumerate(items))
    return f"<div class='grid'>{cells}</div>"
