"""Build the Elis IC memo (16:9 slides, Sanken-memo layout) as HTML, then PDF via Chromium (html2pdf.js)."""
import json, os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from memo_lib import esc, bullets, cards, table, slide, doc

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CH = lambda f: 'file://' + os.path.join(ROOT, 'charts', f)
SPL = json.load(open(os.path.join(ROOT, 'model', 'sp_source_links.json')))
PEERS = json.load(open(os.path.join(ROOT, 'model', 'E_peer_multiples_lead.json')))

def sp(item, period, display):
    r = SPL.get(f'C_27989|{item}|{period}')
    return f'[{display}]({r["url"]})' if r and r.get('url') else f'{display} (S&P, link n/a)'

S = lambda n: f'[#{n.split("-")[-1]}](https://gam.prontonlp.com/#/ref/$SENTID_{n})'
H126 = '[H1 2026 call](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119)'
FY25 = '[FY2025 call](https://gam.prontonlp.com/#/ref/$DOCID_T000003676656)'
URD25 = '[FY2025 URD](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000259591248)'
SR26 = '[H1 2026 report](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000264324010)'
FOOT = 'Elis SA (ELIS FP) | Investment Committee memo | 12 October 2026 | Data: S&P Capital IQ and ProntoNLP only'
TOTAL = 16
slides = []
def add(sec, tag, title, body, style=''):
    slides.append(slide(sec, tag, title, body, FOOT, f'{len(slides) + 1} / {TOTAL}', style))

def two(left, right, lw='1fr', rw='1fr', gap=36):
    return f'<div style="display:grid;grid-template-columns:{lw} {rw};gap:{gap}px">{"<div>"+left+"</div>"}{"<div>"+right+"</div>"}</div>'

def img(f, h=None):
    return f'<img class="chart" src="{CH(f)}" style="{f"max-height:{h}px;object-fit:contain;" if h else ""}">'

H = lambda t: f'<div class="h">{esc(t)}</div>'
NOTE = lambda t: f'<div class="note">{esc(t)}</div>'

# 1 Cover --------------------------------------------------------------------------------
slides.append(f'''<section class="slide navy" style="padding:0">
<div style="position:absolute;left:60px;top:70px;font-size:13px;font-weight:700;letter-spacing:.5px;color:#8fb3ef">INVESTMENT COMMITTEE MEMO  |  EVENT-DRIVEN / SPECIAL SITUATIONS</div>
<div style="position:absolute;left:60px;top:150px;font-size:54px;font-weight:700">Elis SA</div>
<div style="position:absolute;left:60px;top:222px;font-size:22px;color:#c9d6ef">ELIS FP  ·  Euronext Paris  ·  Textile rental, hygiene and facility services</div>
<div style="position:absolute;left:60px;top:300px;width:820px;font-size:20px;line-height:1.45">A capital-intensive compounder priced as a value trap: 11x headline earnings, ~8% FCF yield and a ~20% Brazilian family holder, with the OCEANE soft call and Q3 revenue as near-term tests.</div>
<div style="position:absolute;left:60px;top:450px;display:flex;gap:14px">
{''.join(f'<div style="background:#1f3460;padding:16px 22px;min-width:170px"><div style="font-size:26px;font-weight:700">{esc(v)}</div><div style="font-size:11px;color:#c9d6ef;margin-top:6px">{esc(l)}</div></div>' for v, l in [('BUY', 'Recommendation (medium conviction)'), ('€26', 'Target price, +22%'), ('€21.26', 'Price, close 9-Oct-2026'), ('€17 / €33', 'Bear / bull value'), ('€30–38', 'Takeover value')])}
</div>
<div style="position:absolute;left:60px;bottom:36px;font-size:10.5px;color:#8fb3ef">12 October 2026  ·  Sources: S&P Global Capital IQ and ProntoNLP only (no web). Figures link to source documents; see the data-provenance file for every connector call.</div>
</section>''')

# 2 Executive summary ----------------------------------------------------------------------
add('Executive summary', 'Recommendation', 'BUY, target €26 (+22%): the de-rating has run ahead of the fundamentals',
    cards([('BUY · €26', '12-month target (+22%); probability-weighted €25'), ('5.2x', 'EV / LTM adjusted EBITDA [calc]'), ('11.3x', 'P/E on LTM headline diluted EPS [calc]'), ('~8%', 'FCF yield on equity, after leases [calc]'), ('2.09x', 'Net debt / EBITDA at 30-Jun-2026 (covenant 3.75x)'), ('−25%', 'From the 3-Jul-2026 high of €28.20')]) +
    two(H('Why now: four things converge') + bullets([
        f'**De-rating done:** −24.6% from the July high; H1 call sentiment the lowest since 2020, yet guidance confirmed {S("T000003774119-292")}.',
        f'**Capital returns at scale:** €466.8m bought back at €26.25 in H1 2026 (7.6% of capital); all cash beyond bolt-ons returned {S("T000003676656-493")}.',
        f'**OCEANE soft call from 13-Oct-2026:** conversion cuts net debt ~€362m at no cash cost, leverage to ~1.65x {S("T000003676656-517")}.',
        f'**~20% strategic holder:** Moreira Salles family bought CPP\'s block at €25.00 (Feb-2026), 18% above today {S("NONSEC000259591248-6728")}.',
    ]), H('What has to go right') + bullets([
        'Q3 revenue (28-Oct) shows the promised H2 organic acceleration despite Mexico (~€14m headwind).',
        f'2027 indexation restores margin expansion ("super nice price increase") {S("T000003774119-472")}.',
        'H2 free cash flow of ~€390m+ after the −€30m H1; the OCEANE converts.',
        'No large leveraging US acquisition (the 2024 talks cost 21% in four days).',
    ], gray=True) + '<div class="callout" style="margin-top:10px"><b>Trade:</b> buy below €22; add on a Q3 print ≥3% organic growth; stop / review below €17 (bear-case value).</div>'))

# 3 Business ----------------------------------------------------------------------------------
add('Business overview', 'Franchise', 'A "laundry-as-a-service" utility: €4.8bn revenue, ~87% recurring, 35% EBITDA margin',
    two(H('How each division contributes (FY2025)') + table(['Segment', 'Revenue €m', 'Share', 'Organic', 'Adj. EBITDA mgn'], [
        ['France', '~1,401', '~29%', '+3.3%', '41.9%'], ['Central Europe', '~1,242', '~26%', '+3.0%', '32.9%'], ['Scandinavia & E. Europe', '~640', '~13%', '+1.9%', '35.5%'],
        ['UK & Ireland', '~580', '~12%', '+2.6%', '32.4%'], ['Latin America', '~458', '~10%', '+8.2%', '33.6%'], ['Southern Europe', '~451', '~9%', '+6.7%', '33.7%'],
        ['Group', sp('Total Revenues', 'FY2025', '4,796.8'), '100%', '+3.8%', '35.4%']], hl=(6,)) +
        NOTE(f'Segment revenues from the regional profiles in the {URD25}; segment EBITDA margins from the FY2025 results release. Group revenue linked to S&P Capital IQ.'),
        H('What it does and why it is defensible') + bullets([
        'Rents, launders and delivers flat linen (~45%), workwear (~36%) and hygiene / well-being equipment (~17%) in 31 countries; 70% of revenue outside France.',
        'Customers: healthcare ~30%, hospitality 27%, industry ~26%, trade & services ~18%; top-10 clients <10% of revenue, largest contract <1%.',
        'Moat = route density: a full van and a full laundry. #1, #2 or #3 in most countries and #1 in more than half.',
        'Weak points: labour is ~60% of costs and energy 6–7% of revenue; capex runs at ~18% of sales; cost inflation is passed on only with a lag.',
    ]) + '<div class="callout" style="margin-top:8px">Economic profile: ROIC ~7% on EBITA after tax; free cash flow after leases is only ~21% of EBITDA.</div>', '1.15fr', '1fr'))

# 4 Stock --------------------------------------------------------------------------------------
ev = json.load(open(os.path.join(ROOT, 'charts', 'price_catalysts_events.json')))
add('Share-price history', 'Catalysts', 'What moved the stock: ten catalysts since 2020',
    two(img('price_catalysts_memo.png', 480),
        '<table class="t"><thead><tr><th>#</th><th>When</th><th>What happened</th></tr></thead><tbody>' +
        ''.join(f'<tr><td class="b" style="color:{"#1a8a4a" if d == "up" else "#c0392b"}">{i + 1}</td><td style="white-space:nowrap">{esc(w)}</td><td>{esc(t)}</td></tr>' for i, (_, w, t, d) in enumerate(ev)) + '</tbody></table>', '1.25fr', '1fr', 24))

# 5 Financials ----------------------------------------------------------------------------------
add('Financial track record', 'Five years', 'Revenue +57% since 2021; adjusted EBITDA margin up from 33.0% (2022) to 35.4%',
    two(img('hist_revenue.png', 225) + img('hist_margins.png', 225),
        table(['EUR m', 'FY2021', 'FY2023', 'FY2024', 'FY2025', 'LTM Jun-26'], [
            ['Revenue', sp('Total Revenues', 'FY2021', '3,048.3'), sp('Total Revenues', 'FY2023', '4,309.4'), sp('Total Revenues', 'FY2024', '4,573.7'), sp('Total Revenues', 'FY2025', '4,796.8'), '4,910.8 (S&P, link n/a)'],
            ['Adj. EBITDA (co.)', '1,052.1', '1,474.8', '1,609.8', '1,700.1', '1,740.1'],
            ['Adj. EBITDA margin', '34.5%', '34.2%', '35.2%', '35.4%', '35.4%'],
            ['Cash from operations', sp('Cash from Operations', 'FY2021', '961.6'), sp('Cash from Operations', 'FY2023', '1,325.6'), sp('Cash from Operations', 'FY2024', '1,452.1'), sp('Cash from Operations', 'FY2025', '1,510.6'), '1,486.4 (S&P, link n/a)'],
            ['Capex', sp('Capital Expenditure', 'FY2021', '−552.8'), sp('Capital Expenditure', 'FY2023', '−797.1'), sp('Capital Expenditure', 'FY2024', '−860.8'), sp('Capital Expenditure', 'FY2025', '−864.0'), '−915.8 (S&P, link n/a)'],
            ['Headline diluted EPS (€)', 'n/a', 'n/a', '1.76', '1.85', '1.89'],
            ['Dividend per share (€)', '0.37', sp('Dividend Per Share', 'FY2023', '0.43'), sp('Dividend Per Share', 'FY2024', '0.45'), sp('Dividend Per Share', 'FY2025', '0.48'), ''],
        ]) + NOTE('S&P Capital IQ standardised statements (linked to the Capital IQ document viewer where returned); company-defined adjusted EBITDA and headline EPS from Elis releases via ProntoNLP. FY2021 DPS €0.37 from the FY2021 results via ProntoNLP (source link unavailable in this table). LTM = S&P LTM to 30-Jun-2026.') +
        '<div class="callout" style="margin-top:10px">Capex intensity (~18% of sales) is the price of the moat: linen is an asset that wears out. The equity story is FCF growth, not revenue growth.</div>', '1fr', '1.25fr', 24))

# 6 H1 2026 + sentiment ------------------------------------------------------------------------
add('Latest result and sentiment', 'H1 2026', 'H1 2026: targets confirmed, quality disappointed, tone at a six-year low',
    two(H('H1 2026 (reported 29-Jul-2026)') + table(['Metric', 'H1 2026', 'Change'], [
        ['Revenue', '€2,457.1m', '+4.9%; organic +3.2%'], ['Adjusted EBITDA margin', '34.7%', 'flat'], ['Headline diluted EPS', '€0.89', '+5.1%'],
        ['Free cash flow (after leases)', '−€30.1m', 'seasonal WC, capex peak'], ['Net debt / EBITDA', '2.09x', '+0.34x in six months (buyback)'], ['Buyback', '€466.8m @ €26.25', '7.6% of capital']], right_from=1) +
        NOTE(f'Sources: {H126}; {SR26}. Market reaction: −5.7% on day 1 (z-score −3.6), −18.4% to 9-Oct [calc from ProntoNLP prices].') +
        bullets([f'FY2026 guidance (11-Mar-2026, {FY25}) reaffirmed: organic growth slightly below 3.8%, slight margin expansion, high-single-digit headline EPS growth (≈€1.98–2.02), mid-single-digit FCF growth, leverage ~1.65x.',
                 'Negatives: Mexico tender loss (~€14m), German minimum wage, French hospitality softness, H1 FCF negative.']),
        img('sentiment.png', 340) +
        '<div class="callout">Sentiment is low on margins and cash; the "strategic position" aspect barely moved. We read this as a cyclical, not structural, disappointment.</div>', '1fr', '1fr'))

# 7 Estimates ------------------------------------------------------------------------------------
add('Estimates', 'EPS 2026–28', 'Base case: headline EPS +8% a year to €2.34 in 2028',
    two(table(['EUR m', 'FY2025A', 'FY2026E', 'FY2027E', 'FY2028E'], [
        ['Revenue', sp('Total Revenues', 'FY2025', '4,796.8'), '5,002', '5,242', '5,504'], ['Organic growth', '3.8%', '~3.3%', '3.8%', '4.0%'],
        ['Adj. EBITDA', '1,700.1', '1,773', '1,866', '1,968'], ['Adj. EBITDA margin', '35.4%', '35.4%', '35.6%', '35.8%'], ['Adj. EBIT', '766.6', '798', '849', '903'],
        ['Headline diluted EPS (€)', '1.85', '1.96', '2.14', '2.34'], ['DPS (€)', sp('Dividend Per Share', 'FY2025', '0.48'), '0.51', '0.55', '0.60'],
        ['FCF after leases', '358.6', '~375', '~405', '~440'], ['P/E at €21.26', '11.5x', '10.8x', '9.9x', '9.1x']], hl=(5,)) +
        NOTE('Analyst estimates [e]; model/main_forecast.py. FY2025A from Elis releases via ProntoNLP and S&P Capital IQ.'),
        H('Scenario EPS (headline, diluted)') + table(['', 'FY2026E', 'FY2027E', 'FY2028E'], [['Bear', '€1.91', '€1.91', '€1.95'], ['Base', '€1.96', '€2.14', '€2.34'], ['Bull', '€2.00', '€2.27', '€2.64']], hl=(1,)) +
        bullets(['Building blocks: ~3.5–4% organic growth, +1pt bolt-on M&A, 20–30bp a year of margin, buybacks cutting the share count ~2% a year.',
                 'Versus guidance: FY2026E €1.96 (+5.9%) is ~2% below the guided mid-point because H1 grew only +5.1%. No forward EPS consensus is available in the permitted sources.',
                 'Swing factors: ±1pt organic ≈ ±€1.5/share; ±50bp EBIT margin ≈ ±€1.9/share [calc].']), '1.2fr', '1fr'))

# 8 Capital structure -----------------------------------------------------------------------------
add('Capital structure', 'Balance sheet', 'Investment-grade balance sheet; the OCEANE conversion is the next deleveraging step',
    cards([('€3,670m', 'Net debt excl. leases, 30-Jun-2026'), ('2.09x', 'Leverage (covenant 3.75x)'), ('€1.35bn', 'Liquidity: €447m cash + €900m undrawn RCF'), ('BBB- / Baa3', 'S&P / Moody\'s, both stable'), ('€380m', 'OCEANE 2029, 2.25%; conversion ~€20.8 trigger [calc]')]) +
    two(img('hist_leverage.png', 320) + NOTE('S&P Capital IQ balance sheets (FY2016–25; 30-Jun-2026 interim); leverage on company-adjusted EBITDA [calc].'),
        bullets(['Maturities are well spread: next bond (€300m, May-2027) already pre-funded by the €600m 3.875% EMTN of Mar-2026.',
                 'The soft call can be exercised from 13-Oct-2026 if the share trades above 130% of the conversion price (~€20.8 [calc]); with the stock near the trigger, the convertible holder base is a natural buyer of weakness.',
                 'Management plans to settle conversion with bought-back treasury shares (~16.9m held at 30-Jun-2026): little net dilution and ~€362m (debt component) lower net debt.',
                 'Policy: −0.1x of leverage a year; all excess cash to shareholders. Leases (~€700m, IFRS 16) are excluded from covenant leverage.',
                 f'Cost of debt: the 2019–21 bonds (1.6–2.7%) are being refinanced at 3.4–3.9%; each +100bp on ~€1bn of refinancing ≈ €10m pre-tax [calc]. Sources: {SR26}, {FY25}.'])))

# 9 Valuation vs peers ---------------------------------------------------------------------------
rows = [r for r in PEERS['rows'] if r.get('ev_ebitda') and r.get('ebit_m') is not None]
rows.sort(key=lambda r: -(r['mcap'] or 0) if r['ticker'] != 'ELIS' else -1e12)
def fx(v, suf='x'): return f'{v:.1f}{suf}' if isinstance(v, (int, float)) else 'n/a'
reg = PEERS['regression']
add('Valuation', 'Peers', f'Elis trades at {reg["elis_actual"]:.2f}x sales vs {reg["elis_implied"]:.2f}x implied by its own margin',
    two(img('regression_memo.png', 470) + NOTE(f'EV/Sales = {reg["intercept"]:.2f} + {reg["slope"]:.3f} × EBIT margin (%), R² {reg["r2"]:.2f}, n = {reg["n"]}. S&P Capital IQ LTM financials; market caps from ProntoNLP / S&P [calc].'),
        table(['Company', 'EV/Sales', 'EV/EBITDA', 'P/E', 'EBIT margin'], [[r['name'][:26], fx(r['ev_sales']), fx(r['ev_ebitda']), fx(r.get('pe')), fx(100 * r['ebit_m'], '%')] for r in rows[:14]], hl=(0,)) +
        NOTE('S&P-standardised EBITDA (after IFRS 16 adjustments) differs from company adjusted EBITDA; Elis 5.2x on company basis. Private peers (Alsco, Lindström, CWS, Mewa, Salesianer) not shown.'), '1fr', '1.05fr', 26))

# 10 Valuation history + target ------------------------------------------------------------------
add('Valuation', 'Target price', 'Target €26: three methods on FY2027E, at mid-range multiples',
    two(img('valuation_history.png', 430) + NOTE('Year-end prices (ProntoNLP) on S&P Capital IQ financials [calc]; current = 9-Oct-2026.'),
        table(['Method', 'Multiple', 'Value / share'], [['P/E on FY2027E headline EPS €2.14', '12.5x', '€26.8'], ['EV/EBITDA FY2027E (post-OCEANE)', '5.5x', '€27.2'], ['FCF yield FY2027E', '7.0%', '€23.4'], ['Blended target', '', '€26.0 (+22%)'], ['Takeover value (6.5–7.5x LTM EBITDA)', '', '€30–38']], right_from=1, hl=(3,)) +
        bullets(['Five-year range: 5.0–6.4x EV/adjusted EBITDA (5.1x today); headline P/E 10.5x–12.9x since 2024. We use 5.5x and 12.5x.',
                 'Transactions: Cintas–UniFirst ~19x EBITDA (2026); Elis\'s Indusal / Lavebras at 7–8x; bolt-ons at ~5x EBITDA.',
                 'Every €1 of P/E multiple is worth ~€2.1/share; every 0.5x EBITDA ~€4/share [calc].'])))

# 11 M&A + ownership ------------------------------------------------------------------------------
add('Ownership and M&A', 'Event angle', 'A ~20% family holder, an active sector, and a stock below its holder\'s entry price',
    two(H('Who owns it') + table(['Holder', 'Stake', 'Note'], [['BWSA / BWGI (Moreira Salles)', '≥18.3% (~20% votes)', 'Bought 7.0m CPP shares at €25.00, Feb-2026; 25% standstill; 2 board seats'], ['Invesco', '>10%', 'Crossed 5% Nov-2025, 10% Jul-2026'], ['Treasury shares', '~7.3%', '~16.9m; earmarked for OCEANE conversion'], ['Wellington', '~5%', 'Around the threshold'], ['CPP Investments', '<5%', 'Exiting (11.9% in 2025)'], ['Insiders / employees', '~3.0%', 'FCPE, direct, vested PS']], right_from=9) +
        NOTE(f'AMF threshold declarations, URD and H1 2026 report via ProntoNLP ({URD25}). Full top-10 register and short interest not available in permitted sources. No activist campaign found.'),
        H('Is Elis a target?') + bullets(['Takeover value €30–38 (6.5–7.5x EBITDA); a buyer would pay up for route density in 30 countries.',
            'Obstacles: ~€9.0bn EV, a 25% standstill on BWSA, and 49.7m shares with double voting rights (31-Dec-2025).',
            'More likely: BWSA creeping towards (but not through) 25%, a sale of its block to a strategic, or Elis as a buyer (US entry).',
            'Elis as acquirer: Berendsen (~£2.2bn, 2017), Lavebras / Indusal at 7–8x EBITDA, bolt-ons at ~5x (2025: €91m revenue for €108m). Risk: a large US deal (2024 talks).'])))

# 12 Scenarios -------------------------------------------------------------------------------------
add('Scenario analysis', 'Risk / reward', 'Asymmetric: −19% to the bear case, +22% base, +55% bull; probability-weighted €25',
    two(img('scenarios.png', 440),
        table(['', 'Bear (25%)', 'Base (55%)', 'Bull (20%)'], [['Organic growth 2027E', '~2.0%', '3.8%', '~5.0%'], ['Adj. EBIT margin 2027E', '15.4%', '16.2%', '16.5%'], ['Headline EPS 2027E', '€1.91', '€2.14', '€2.27'], ['OCEANE', 'Not converted', 'Converted Q4-26', 'Converted + €200m buybacks'], ['Multiple', '9.0x P/E', '12.5x P/E', '14.5x P/E'], ['Value per share', '€17.2', '€26.0', '€33.0'], ['vs €21.26', '−19%', '+22%', '+55%']], right_from=1, hl=(5,)) +
        '<div class="callout" style="margin-top:10px">The bear case still assumes no dividend cut and investment-grade financing. Takeover value (€30–38) sits above the bull case.</div>', '1fr', '1.1fr'))

# 13 Risks ----------------------------------------------------------------------------------------
risks = [('Organic growth slows below 3%', 'Pricing normalises after the inflation years while volumes in French hospitality and German industry stay soft. Each 1pt ≈ €1.5/share.'),
         ('Labour and energy outrun indexation', 'Labour is ~60% of costs; 2026 minimum wages +23% in Colombia, +13% in Mexico, a large rise in Germany; energy shocks (2022, 2026) hit margins for 2–3 quarters before price catches up.'),
         ('A large leveraging acquisition', 'US entry ambitions (2024 Vestis talks) cost 21% in four days. A big deal would reset leverage above 3x and pause buybacks.'),
         ('Capital intensity hides low returns', 'ROIC is ~7%: the short-seller view is that cheapness is deserved; FCF after leases is only ~21% of EBITDA.')]
add('Key risks', 'Downside', 'Four risks that could make the stock cheap for a reason',
    '<div class="risks">' + ''.join(f'<div class="risk"><div class="n">0{i + 1}</div><div><div class="rt">{esc(t)}</div><div class="rd">{esc(d)}</div></div></div>' for i, (t, d) in enumerate(risks)) + '</div>' +
    '<div class="callout" style="margin-top:16px"><b>Pre-mortem (Oct-2027, the stock is €15):</b> Q3/Q4 organic growth printed ~2%, Mexico and Germany worsened, the OCEANE was not converted, BWSA stopped buying and a 2027 French election shock cut the multiple to 9x. <b>Mitigant:</b> stop-review below €17.</div>')

# 14 Catalyst calendar -----------------------------------------------------------------------------
cal = [('13-Oct-2026 onwards', 'OCEANE 2029 soft call window opens', 'Conversion into treasury shares: −€362m net debt, leverage ~1.65x', 'High'),
       ('28-Oct-2026', 'Q3 2026 revenue', 'Proof of the H2 organic acceleration; Mexico, France, energy pass-through', 'High'),
       ('21-Oct / 6-Nov-2026', 'UniFirst FY26 and Rentokil Q3 results', 'US and European read-across on demand and pricing', 'Medium'),
       ('From 11-Dec-2026', 'Cintas–UniFirst closing ($5.5bn)', 'US consolidation; re-rating read-across for the sector', 'Medium'),
       ('Q4 2026', 'Annual price / index negotiations', 'Sets the 2027 "super nice price increase" and margin path', 'High'),
       ('Early Mar-2027', 'FY2026 results and 2027 guidance', 'Dividend, new buyback, FCF delivery vs €380–400m guide', 'High'),
       ('Apr–May 2027', 'French presidential election', '~30% of revenue in France; the 2024 snap election cost ~15%', 'Medium'),
       ('Late Jul-2027', 'H1 2027 results', 'Margin recovery and FCF seasonality', 'Medium')]
add('Catalyst calendar', 'Next 12 months', 'Catalysts: the soft call and Q3 revenue come first',
    '<table class="cal">' + ''.join(f'<tr><td class="d">{esc(d)}</td><td class="e">{esc(e)}</td><td class="x">{esc(x)}</td><td class="i">{esc(i)}</td></tr>' for d, e, x, i in cal) + '</table>' +
    NOTE('Dated events from ProntoNLP upcoming-event listings, the H1 2026 report and the FY2025 URD; "early/late" dates are estimates [e] from prior-year patterns (model/D_catalyst_calendar.csv).'))

# 15 Questions -------------------------------------------------------------------------------------
add('Management agenda', 'Questions', 'What we would ask the CEO and the Chairman before sizing up',
    two(H('CEO (Xavier Martiré)') + bullets(['If the share price is below €20.8 on the soft-call date, what is plan B for leverage, the 2027 buyback and the €380m OCEANE?',
        'What organic growth do the record 2026 signings imply for 2027, and how much is price vs volume?',
        'Why did H1 FCF turn negative, and what gets H2 to €390m+?',
        'Under what conditions would you again pursue a large US or European acquisition, at what leverage?',
        'How much of the 2026 minimum-wage increases in Germany, the UK and LatAm is still unrecovered?']),
        H('Chairman of the Supervisory Board') + bullets(['Is BWSA/BWGI a long-term investor capped at 25%, or a potential controlling holder?',
        'What would the board do with an unsolicited bid at €30–35?',
        'How is management\'s long-term incentive linked to ROIC and FCF per share, not revenue?',
        'After the Sep-2026 Management Board renewal and Matthieu Lecharny\'s departure, what is the succession plan?',
        'Would the board support cancelling treasury shares rather than holding ~10% of capital?'], gray=True) +
        NOTE('Full list of 15 questions in Section 21 of the research report.')))

# 16 Recommendation -----------------------------------------------------------------------------------
add('Recommendation', 'Decision', 'Recommendation: BUY a starter position, add on Q3 delivery',
    cards([('BUY', 'Event-driven, medium conviction'), ('€26', 'Target (+22%); takeover €30–38'), ('€17', 'Bear value / stop-review level'), ('+22% / −19%', 'Upside to base vs downside to bear')]) +
    two(H('Position plan') + bullets(['Initial 1.5% of NAV below €22; scale to 3% after a Q3 print with ≥3% organic growth and confirmation of the soft call.',
        'Hedge option: pair against a basket of European business-services peers to isolate the stock-specific event.',
        'Exit / review: target €26; review the thesis below €17 or on a large US acquisition announcement.']),
        H('What would change our mind') + bullets(['Organic growth below 2.5% for two consecutive quarters.', 'Leverage above 2.5x without a matching acquisition.', 'A dividend cut or suspension of the capital-return policy.', 'Evidence that BWSA is selling.'], gray=True)) +
    '<div class="note" style="margin-top:14px">For institutional investors. Data only from S&P Global Capital IQ and ProntoNLP; [calc] analyst calculation, [e] estimate, [u] unverified. Full analysis: Elis_ELIS_FP_Equity_Research_Report.pdf. Every connector call and raw response: ELIS_FP/provenance.</div>')

assert len(slides) == TOTAL, len(slides)
out_html = os.path.join(ROOT, 'build', 'memo.html')
open(out_html, 'w').write(doc(slides, 'Elis SA (ELIS FP) — IC memo'))
pdf = os.path.join(ROOT, 'Elis_ELIS_FP_IC_Memo.pdf')
subprocess.run(['node', os.path.join(ROOT, 'build', 'html2pdf.js'), out_html, pdf], check=True, env={**os.environ, 'NODE_PATH': '/opt/node22/lib/node_modules'})
