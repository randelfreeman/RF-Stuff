"""IC-memo slide generator (16:9, 13.333in x 7.5in) — HTML components rendered to PDF by Chromium."""
import html, re

CSS = r"""
@page { size: 13.333in 7.5in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: 'Liberation Sans', Arial, Helvetica, sans-serif; color: #13213f; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.slide { width: 13.333in; height: 7.5in; position: relative; overflow: hidden; page-break-after: always; break-after: page; background: #fff; padding: 36px 47px 0 47px; }
.slide:last-child { page-break-after: auto; break-after: auto; }
.navy { background: #13213f; color: #fff; }
.sec { font-size: 12.5px; font-weight: 700; color: #2f6fcf; letter-spacing: .3px; text-transform: uppercase; margin-top: 4px; }
.tag { position: absolute; right: 47px; top: 39px; background: #13213f; color: #fff; font-size: 11px; font-weight: 700; padding: 9px 20px; letter-spacing: .3px; text-transform: uppercase; }
.rule { position: absolute; left: 47px; right: 47px; top: 80px; border-top: 1.2px solid #13213f; }
.title { position: absolute; left: 47px; right: 47px; top: 96px; font-size: 24px; font-weight: 700; color: #13213f; line-height: 1.2; }
.body { position: absolute; left: 47px; right: 47px; top: 144px; bottom: 44px; }
.footer { position: absolute; left: 47px; right: 47px; bottom: 22px; font-size: 9.5px; color: #7d8494; display: flex; justify-content: space-between; }
.cards { display: flex; gap: 9px; margin-bottom: 18px; }
.card { flex: 1; background: #eff1f5; padding: 16px 14px 14px 14px; min-height: 96px; }
.card .v { font-size: 21px; font-weight: 700; color: #13213f; margin-bottom: 8px; }
.card .l { font-size: 9.8px; color: #5d6577; line-height: 1.4; }
.cols { display: flex; gap: 42px; }
.col { flex: 1; min-width: 0; }
.h { font-size: 14.5px; font-weight: 700; color: #13213f; padding-bottom: 7px; border-bottom: 1px solid #c9ced8; margin-bottom: 10px; }
ul.b { list-style: none; padding: 0; margin: 0; }
ul.b li { position: relative; padding-left: 17px; font-size: 11.6px; line-height: 1.5; margin-bottom: 6px; color: #1d2433; }
ul.b li:before { content: ''; position: absolute; left: 0; top: 6px; width: 9px; height: 6px; background: #2f6fcf; }
ul.b.gray li:before { background: #6b7385; }
.callout { background: #eff1f5; border-left: 6px solid #13213f; padding: 13px 18px; font-size: 11.4px; line-height: 1.5; color: #1d2433; }
table.t { border-collapse: collapse; width: 100%; font-size: 10.6px; }
table.t th { background: #13213f; color: #fff; text-align: left; padding: 6px 7px; font-weight: 700; }
table.t td { padding: 5.5px 7px; border-bottom: 1px solid #d6dae2; color: #1d2433; vertical-align: top; }
table.t td.b { font-weight: 700; }
table.t tr.hl td { background: #dce6f7; font-weight: 700; }
table.t td.r, table.t th.r { text-align: right; }
.note { font-size: 9.2px; color: #6b7385; margin-top: 6px; line-height: 1.4; }
.chart { width: 100%; }
.cal { width: 100%; border-collapse: collapse; }
.cal td { padding: 13px 4px; border-bottom: 1px solid #d6dae2; font-size: 11.4px; vertical-align: middle; }
.cal td.d { color: #2f6fcf; font-weight: 700; font-size: 10.6px; width: 205px; text-transform: uppercase; }
.cal td.e { font-weight: 700; width: 340px; color: #13213f; }
.cal td.x { color: #5d6577; font-size: 10.6px; }
.cal td.i { color: #2f6fcf; font-weight: 700; text-align: right; font-size: 10.6px; width: 90px; }
.risks { display: grid; grid-template-columns: 1fr 1fr; gap: 22px 19px; }
.risk { background: #eff1f5; padding: 20px 20px 18px 20px; display: flex; gap: 28px; min-height: 133px; }
.risk .n { font-size: 28px; font-weight: 700; color: #2f6fcf; width: 42px; }
.risk .rt { font-size: 13.6px; font-weight: 700; color: #13213f; margin: 6px 0 9px 0; }
.risk .rd { font-size: 10.8px; color: #5d6577; line-height: 1.45; }
a { color: inherit; text-decoration: none; }
a.src { color: #2f6fcf; font-size: 8.5px; vertical-align: super; }
"""

def esc(s):
    """Escape text but keep markdown-style links [label](url) and **bold**."""
    s = str(s)
    parts = re.split(r'(\[[^\]]+\]\(https?://[^)\s]+\))', s)
    out = []
    for p in parts:
        m = re.match(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', p)
        if m:
            lab, url = m.group(1), m.group(2)
            if re.match(r'^#[A-Za-z0-9_\-.]+$', lab):
                out.append(f'<a class="src" href="{html.escape(url, quote=True)}">[{html.escape(lab)}]</a>')
            else:
                out.append(f'<a href="{html.escape(url, quote=True)}" style="text-decoration:underline">{html.escape(lab)}</a>')
        else:
            t = html.escape(p)
            t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
            out.append(t)
    return ''.join(out)

def bullets(items, gray=False):
    return '<ul class="b%s">' % (' gray' if gray else '') + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul>'

def cards(items):
    return '<div class="cards">' + ''.join(f'<div class="card"><div class="v">{esc(v)}</div><div class="l">{esc(l)}</div></div>' for v, l in items) + '</div>'

def table(cols, rows, hl=(), right_from=1, widths=None, cls='t', bold_first=True):
    th = ''.join(f'<th{" class=r" if (i >= right_from) else ""}{f" style=width:{widths[i]}" if widths else ""}>{esc(c)}</th>' for i, c in enumerate(cols))
    body = ''
    for ri, r in enumerate(rows):
        tds = ''.join(f'<td class="{("b " if (i == 0 and bold_first) else "") + ("r" if i >= right_from else "")}">{esc(c)}</td>' for i, c in enumerate(r))
        body += f'<tr{" class=hl" if ri in hl else ""}>{tds}</tr>'
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'

def slide(sec, tag, title, body_html, footer_left, page, extra_style=''):
    return f'''<section class="slide">
<div class="sec">{esc(sec)}</div><div class="tag">{esc(tag)}</div><div class="rule"></div>
<div class="title">{esc(title)}</div>
<div class="body" style="{extra_style}">{body_html}</div>
<div class="footer"><span>{esc(footer_left)}</span><span>{page}</span></div></section>'''

def doc(slides_html, title):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{"".join(slides_html)}</body></html>'
