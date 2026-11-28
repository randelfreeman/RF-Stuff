"""Builds 16-slide IC memo decks (HTML -> PDF) in the house format for LIO LN and IPX LN."""
import json, os, html
from memo_content import LIO, IPX

CH = 'file:///home/user/RF-Stuff/ic_memos/charts/'
CSS = """
@page { size: 1333px 750px; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
body { font-family: 'Liberation Sans', Arial, Helvetica, sans-serif; color: #13203d; }
.slide { width: 1333px; height: 750px; position: relative; page-break-after: always; overflow: hidden; background: #fff; }
.dark { background: #13203d; color: #fff; }
.kicker { position: absolute; left: 58px; top: 44px; font-size: 12.5px; font-weight: 700; color: #2f6fd1; letter-spacing: .2px; }
.tag { position: absolute; right: 58px; top: 39px; background: #13203d; color: #fff; font-size: 11px; font-weight: 700; padding: 9px 25px; }
.rule { position: absolute; left: 58px; right: 58px; top: 86px; border-top: 1.3px solid #13203d; }
.title { position: absolute; left: 58px; right: 58px; top: 106px; font-size: 23px; font-weight: 700; }
.foot { position: absolute; left: 58px; bottom: 30px; font-size: 9px; color: #6b7280; }
.pno { position: absolute; right: 58px; bottom: 30px; font-size: 9px; color: #6b7280; }
.body { position: absolute; left: 58px; right: 58px; top: 160px; bottom: 60px; }
.cols { display: flex; gap: 62px; } .col { flex: 1; }
h3 { font-size: 13.5px; font-weight: 700; padding-bottom: 8px; border-bottom: 1px solid #cfd4dc; margin-bottom: 14px; }
ul.b { list-style: none; } ul.b li { position: relative; padding-left: 20px; font-size: 11px; line-height: 1.5; margin-bottom: 9px; color: #222; }
ul.b li:before { content: ''; position: absolute; left: 0; top: 6px; width: 7px; height: 5px; background: #2f6fd1; }
ul.g li:before { background: #8a94a6; }
.stats { display: flex; gap: 6px; margin-bottom: 24px; } .stat { flex: 1; background: #eff1f5; padding: 20px 20px 18px; min-height: 122px; }
.stat .v { font-size: 24px; font-weight: 700; margin-bottom: 12px; } .stat .l { font-size: 10px; color: #444; line-height: 1.45; }
table.t { width: 100%; border-collapse: collapse; font-size: 10.5px; } table.t th { background: #13203d; color: #fff; text-align: left; padding: 6px 7px; font-weight: 700; }
table.t td { padding: 5.5px 7px; border-bottom: 1px solid #d4d8df; color: #222; } table.t td:first-child { font-weight: 700; color: #13203d; }
table.t tr.hl td { background: #dbe5f5; font-weight: 700; }
.note { font-size: 8.5px; color: #555; margin-top: 7px; line-height: 1.4; }
.callout { position: absolute; left: 58px; right: 58px; bottom: 64px; background: #eff1f5; border-left: 5px solid #13203d; padding: 18px 22px; font-size: 11px; line-height: 1.55; }
img.ch { display: block; }
.risk { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; } .rk { background: #eff1f5; padding: 18px 20px; display: flex; gap: 22px; min-height: 108px; }
.rk .n { font-size: 21px; font-weight: 700; color: #2f6fd1; } .rk .h { font-size: 12px; font-weight: 700; margin-bottom: 9px; } .rk .d { font-size: 10px; color: #444; line-height: 1.5; }
.cal { width: 100%; border-collapse: collapse; } .cal td { padding: 15px 0; border-bottom: 1px solid #cfd4dc; vertical-align: top; font-size: 10px; color: #444; }
.cal td.dt { width: 180px; color: #2f6fd1; font-weight: 700; font-size: 10px; } .cal td.ev { width: 330px; font-size: 12.5px; font-weight: 700; color: #13203d; } .cal td.im { width: 110px; text-align: right; font-weight: 700; color: #13203d; }
"""

def esc(s):
    s = html.escape(s)
    # **bold**
    out, b = '', False
    for part in s.split('**'):
        out += (('<b>' + part + '</b>') if b else part); b = not b
    return out

def bl(items, grey=False):
    return '<ul class="b%s">' % (' g' if grey else '') + ''.join('<li>%s</li>' % esc(i) for i in items) + '</ul>'

def tbl(head, rows, hl=None, widths=None):
    h = '<tr>' + ''.join('<th%s>%s</th>' % ((' style="width:%s"' % widths[i]) if widths else '', esc(x)) for i, x in enumerate(head)) + '</tr>'
    r = ''.join('<tr%s>%s</tr>' % (' class="hl"' if hl is not None and i in (hl if isinstance(hl, (list, tuple)) else [hl]) else '', ''.join('<td>%s</td>' % esc(c) for c in row)) for i, row in enumerate(rows))
    return '<table class="t">' + h + r + '</table>'

def stats(items):
    return '<div class="stats">' + ''.join('<div class="stat"><div class="v">%s</div><div class="l">%s</div></div>' % (esc(v), esc(l)) for v, l in items) + '</div>'

def frame(c, n, kicker, tag, title, inner, callout=None):
    s = '<div class="slide"><div class="kicker">%s</div><div class="tag">%s</div><div class="rule"></div><div class="title">%s</div><div class="body">%s</div>' % (esc(kicker), esc(tag), esc(title), inner)
    if callout:
        s += '<div class="callout">%s</div>' % esc(callout)
    s += '<div class="foot">%s</div><div class="pno">%d</div></div>' % (esc(c['footer']), n)
    return s

def build(c):
    S = []
    # 1 cover
    cv = c['cover']
    right = ''.join('<div style="padding:44px 0 26px;border-bottom:1px solid #45536f"><div style="font-size:27px;font-weight:700;color:%s">%s</div><div style="font-size:10px;color:#c9d1e0;margin-top:16px;line-height:1.5">%s</div></div>' % ('#8fb3ef' if i == 2 else '#fff', esc(v), esc(l)) for i, (v, l) in enumerate(cv['right']))
    facts = ''.join('<div style="width:181px;margin-bottom:28px"><div style="font-size:9.5px;color:#b7c1d6;margin-bottom:12px">%s</div><div style="font-size:11px;color:#fff">%s</div></div>' % (esc(k), esc(v)) for k, v in cv['facts'])
    S.append('<div class="slide dark"><div style="position:absolute;left:76px;top:145px;font-size:11px;font-weight:700;color:#8fb3ef;border-bottom:1px solid #8fb3ef;padding-bottom:5px">INVESTMENT COMMITTEE MEMO</div>'
             '<div style="position:absolute;left:76px;top:195px;width:730px;font-size:42px;font-weight:700;line-height:1.3">%s</div>'
             '<div style="position:absolute;left:76px;top:%dpx;width:730px;font-size:16px;color:#d6dceb;line-height:1.35">%s</div>'
             '<div style="position:absolute;left:76px;top:%dpx;display:flex;gap:12px"><div style="background:#2f6fd1;padding:12px 44px;font-size:12px;font-weight:700">%s</div><div style="border:1.3px solid #fff;padding:11px 52px;font-size:12px;font-weight:700">%s</div></div>'
             '<div style="position:absolute;left:76px;top:%dpx;width:760px;display:flex;flex-wrap:wrap">%s</div>'
             '<div style="position:absolute;left:863px;top:70px;bottom:85px;border-left:1px solid #45536f"></div><div style="position:absolute;left:896px;top:70px;width:354px">%s</div>'
             '<div style="position:absolute;left:76px;width:980px;top:661px;border-top:1px solid #45536f"></div><div style="position:absolute;left:76px;top:675px;font-size:9.5px;color:#b7c1d6">Prepared for Investment Committee review | %s</div></div>'
             % (esc(cv['name']), cv['sub_top'], esc(cv['sub']), cv['btn_top'], esc(cv['rec']), esc(cv['tgt']), cv['btn_top'] + 70, facts, right, esc(c['date'])))
    n = 2
    # 2 exec summary
    e = c['exec']
    inner = stats(e['stats']) + '<div class="cols"><div class="col"><h3>%s</h3>%s</div><div class="col"><h3>What has to go right</h3>%s</div></div>' % (esc(e['why_h']), bl(e['why']), bl(e['right'], True))
    S.append(frame(c, n, 'EXECUTIVE SUMMARY', 'RECOMMENDATION', e['title'], inner, e['callout'])); n += 1
    # 3 business overview
    b = c['biz']
    inner = '<div class="cols"><div class="col"><h3>What it does</h3>%s</div><div class="col"><h3>%s</h3>%s<div class="note">%s</div></div></div>' % (bl(b['what']), esc(b['tab_h']), tbl(b['head'], b['rows'], hl=len(b['rows']) - 1), esc(b['note']))
    S.append(frame(c, n, 'BUSINESS OVERVIEW', 'CONTEXT', b['title'], inner, b['callout'])); n += 1
    # 4 setup
    s = c['setup']
    cat = ''.join('<tr><td style="padding:8px 0;font-size:10px;font-weight:700;width:115px;vertical-align:top"><span style="display:inline-block;width:7px;height:7px;background:#2f6fd1;margin-right:7px"></span>%s</td><td style="padding:8px 0;font-size:10px;color:#333">%s</td></tr>' % (esc(d), esc(t)) for d, t in s['cats'])
    inner = '<div style="display:flex;gap:40px"><img class="ch" src="%s" style="width:740px"><div style="flex:1"><h3>Key catalysts</h3><table style="width:100%%;border-collapse:collapse">%s</table></div></div>' % (CH + s['img'], cat)
    S.append(frame(c, n, 'THE SETUP', 'CONTEXT', s['title'], inner)); n += 1
    # 5 peers
    p = c['peers']
    inner = tbl(p['head'], p['rows']) + '<div class="note">%s</div><div class="cols" style="margin-top:28px"><div class="col"><h3>What the comparison shows</h3>%s</div><div class="col"><h3>The honest counter-read</h3>%s</div></div>' % (esc(p['note']), bl(p['shows']), bl(p['counter'], True))
    S.append(frame(c, n, 'QUESTION 1 - IS %s UNDERVALUED?' % c['short'].upper(), 'VALUATION', p['title'], inner)); n += 1
    # 6 regression
    r = c['reg']
    inner = '<div style="display:flex;gap:46px"><div><div style="font-size:12.5px;font-weight:700;margin-bottom:8px">EV/Sales (x-axis) vs EBIT margin (y-axis) - 10 UK listed asset & wealth managers</div><img class="ch" src="%s" style="width:720px"><div class="note">%s</div></div><div style="flex:1"><h3>How to read it</h3>%s</div></div>' % (CH + r['img'], esc(r['note']), bl(r['read']))
    S.append(frame(c, n, 'QUESTION 1 - IS %s UNDERVALUED?' % c['short'].upper(), 'VALUATION', r['title'], inner)); n += 1
    # 7 SOTP
    so = c['sotp']
    inner = '<div style="display:flex;gap:48px"><img class="ch" src="%s" style="width:610px"><div style="flex:1"><h3>%s</h3>%s<div style="margin-top:22px">%s</div></div></div>' % (CH + so['img'], esc(so['tab_h']), tbl(['Component', 'Method', '£m'], so['rows'], hl=len(so['rows']) - 1), bl(so['bul']))
    S.append(frame(c, n, 'WHERE THE VALUE SITS', 'VALUATION', so['title'], inner)); n += 1
    # 8 hidden assets
    h = c['hidden']
    inner = stats(h['stats']) + '<div style="display:flex;gap:40px"><div style="width:600px">%s<div class="note">%s</div></div><div style="flex:1"><h3>What to watch</h3>%s</div></div>' % (tbl(h['head'], h['rows'], hl=h['hl']), esc(h['note']), bl(h['watch']))
    S.append(frame(c, n, 'THE HIDDEN ASSETS', 'HIDDEN ASSET', h['title'], inner)); n += 1
    # 9 earnings
    ea = c['earn']
    inner = '<div style="display:flex;gap:46px"><div style="width:600px"><img class="ch" src="%s" style="width:600px"><div class="note">%s</div></div><div style="flex:1">%s<div class="note">%s</div><div style="margin-top:22px">%s</div></div></div>' % (CH + ea['img'], esc(ea['cap']), tbl(ea['head'], ea['rows']), esc(ea['note']), bl(ea['bul']))
    S.append(frame(c, n, 'QUESTION 2 - VALUE TRAP, OR GENUINE RECOVERY?', 'EARNINGS', ea['title'], inner)); n += 1
    # 10 capital
    ca = c['cap']
    inner = stats(ca['stats']) + '<div class="cols"><div class="col"><h3>Capital-allocation record</h3>%s</div><div class="col"><h3>Priorities we would push for</h3>%s</div></div>' % (bl(ca['record']), bl(ca['push'], True))
    S.append(frame(c, n, 'BALANCE SHEET & CAPITAL ALLOCATION', 'CAPITAL', ca['title'], inner)); n += 1
    # 11 activist
    ac = c['act']
    inner = stats(ac['stats']) + '<div class="cols"><div class="col"><h3>%s</h3>%s</div><div class="col"><h3>%s</h3>%s</div></div>' % (esc(ac['lh']), bl(ac['left']), esc(ac['rh']), bl(ac['right'], True))
    S.append(frame(c, n, 'IS THERE AN ACTIVIST IN HERE?', 'GOVERNANCE', ac['title'], inner)); n += 1
    # 12 M&A
    m = c['ma']
    inner = '<div style="display:flex;gap:60px"><div style="width:600px">%s<div class="note">%s</div></div><div style="flex:1"><h3>What a control price would look like</h3>%s</div></div>' % (tbl(['Transaction', 'Date', 'Value', 'Multiple'], m['rows']), esc(m['note']), bl(m['bul']))
    S.append(frame(c, n, 'QUESTION 3 - TAKEOVER TARGET?', 'M&A', m['title'], inner)); n += 1
    # 13 scenario
    sc = c['scen']
    inner = tbl(sc['head'], sc['rows'], hl=sc['hl'], widths=['22%', '26%', '26%', '26%'])
    S.append(frame(c, n, 'SCENARIO ANALYSIS', 'VALUATION', sc['title'], inner, sc['callout'])); n += 1
    # 14 catalysts
    ct = c['cat']
    inner = '<table class="cal" style="margin-top:-12px">' + ''.join('<tr><td class="dt">%s</td><td class="ev">%s</td><td>%s</td><td class="im">%s</td></tr>' % tuple(esc(x) for x in row) for row in ct['rows']) + '</table>'
    S.append(frame(c, n, 'CATALYST CALENDAR', 'CATALYSTS', ct['title'], inner)); n += 1
    # 15 risks
    inner = '<div class="risk">' + ''.join('<div class="rk"><div class="n">%02d</div><div><div class="h">%s</div><div class="d">%s</div></div></div>' % (i + 1, esc(h_), esc(d_)) for i, (h_, d_) in enumerate(c['risks'])) + '</div>'
    S.append(frame(c, n, 'KEY RISKS', 'RISKS', 'What would make this thesis wrong', inner)); n += 1
    # 16 decision
    dd = c['dec']
    st = ''.join('<div style="width:174px"><div style="font-size:24px;font-weight:700;color:%s">%s</div><div style="font-size:9.5px;color:#c9d1e0;margin-top:8px">%s</div></div>' % ('#8fb3ef' if i == 0 else '#fff', esc(v), esc(l)) for i, (v, l) in enumerate(dd['stats']))
    bul = ''.join('<li style="position:relative;padding-left:20px;font-size:11px;line-height:1.5;margin-bottom:12px;color:#fff"><span style="position:absolute;left:0;top:6px;width:7px;height:5px;background:#8fb3ef"></span>%s</li>' % esc(x) for x in dd['bul'])
    side = ''.join('<p style="font-size:10px;color:#d6dceb;line-height:1.6;margin-bottom:16px">%s</p>' % esc(x) for x in dd['side'])
    S.append('<div class="slide dark"><div style="position:absolute;left:97px;top:74px;font-size:11px;font-weight:700;color:#8fb3ef">INVESTMENT COMMITTEE DECISION</div>'
             '<div style="position:absolute;left:97px;top:110px;font-size:31px;font-weight:700">Recommendation: %s</div>'
             '<div style="position:absolute;left:97px;top:172px;display:flex">%s</div>'
             '<ul style="position:absolute;left:97px;top:248px;width:720px;list-style:none">%s</ul>'
             '<div style="position:absolute;left:931px;top:208px;width:322px;height:334px;background:#1e3158;padding:24px 22px"><div style="font-size:13px;font-weight:700;margin-bottom:18px">Sizing & monitoring</div>%s</div>'
             '<div style="position:absolute;left:97px;width:1153px;top:660px;border-top:1px solid #45536f"></div><div style="position:absolute;left:97px;top:675px;font-size:9.5px;color:#b7c1d6">%s | %s</div></div>'
             % (esc(dd['rec']), st, bul, side, esc(c['footer_short']), esc(c['date'])))
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (CSS, ''.join(S))

if __name__ == '__main__':
    for c in (LIO, IPX):
        open('/home/user/RF-Stuff/ic_memos/%s.html' % c['file'], 'w').write(build(c))
        print('html', c['file'])
