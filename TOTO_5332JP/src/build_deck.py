# -*- coding: utf-8 -*-
from deck import *

FOOT = 'TOTO Ltd | TSE: 5332 | Reference price ¥6,097 (2 Oct 2026 close) | 4 October 2026 | (e) = estimate, see full report data notes'
d = Deck('TOTO_5332JP_IC_Summary.pdf', FOOT)
c = d.c
L, R, CW = 34, 500, 430  # left x, right col x, col width

# 1 Cover
d.dark_bg()
c.setFont('Lib-B', 9.5); c.setFillColor(LB); c.drawString(45, H - 85, 'INVESTMENT COMMITTEE MEMO')
c.setStrokeColor(BLUE); c.setLineWidth(1.5); c.line(45, H - 95, 130, H - 95)
d.para('TOTO Ltd.', 43, H - 120, 440, ps('ct', 36, 'Lib-B', WHITE, 42))
d.para('TSE: 5332 — The Toilet Maker with a Semiconductor Engine', 45, H - 180, 440, ps('cs', 14, 'Lib', colors.HexColor('#C9D3E6'), 18))
c.setFillColor(BLUE); c.rect(45, H - 268, 165, 30, fill=1, stroke=0)
c.setFillColor(WHITE); c.setFont('Lib-B', 10.5); c.drawCentredString(127, H - 257, 'RECOMMENDATION: BUY')
c.setStrokeColor(LB); c.setLineWidth(1); c.rect(218, H - 268, 205, 30, fill=0, stroke=1)
c.drawCentredString(320, H - 257, '12-MO TARGET: ¥7,200 (+18%)')
for i, (a, b) in enumerate([('Reference price ¥6,097', '(2 Oct 2026 close)'), ('52-wk range', '¥3,766–¥9,500'), ('Mkt cap', '~¥1.0tn (~US$6.7bn)'), ('Net cash (e)', '~¥65bn')]):
    c.setFont('Lib', 8.2); c.setFillColor(colors.HexColor('#C9D3E6'))
    c.drawString(45 + i * 105, H - 300, a); c.drawString(45 + i * 105, H - 314, b)
c.setStrokeColor(colors.HexColor('#2B3A55')); c.line(510, 70, 510, H - 45)
for i, (big, small, col) in enumerate([('~51%', 'Ceramics share of FY3/26 segment OP — on 9% of sales', WHITE),
                                       ('42.9%', 'Advanced Ceramics OP margin (electrostatic chucks for NAND cryo-etch)', WHITE),
                                       ('¥7,200', '12-mo target; probability-weighted value ~¥6,975', LB)]):
    y = H - 115 - i * 95
    d.para(big, 545, y, 360, ps('cb', 30, 'Lib-B', col, 34))
    d.para(small, 545, y - 42, 360, ps('csm', 9.5, 'Lib', colors.HexColor('#C9D3E6'), 12))
    if i < 2: c.setStrokeColor(colors.HexColor('#2B3A55')); c.line(545, y - 70, 910, y - 70)
c.setStrokeColor(colors.HexColor('#2B3A55')); c.line(45, 55, W - 45, 55)
c.setFont('Lib', 8); c.setFillColor(SLATE); c.drawString(45, 38, 'Prepared for Investment Committee review | 4 October 2026')
d.next()

# 2 Exec summary
d.header('Executive summary', 'Recommendation', 'Buy: a ~43%-margin chip consumable priced as a toilet company, after a 36% pull-back')
y = d.tiles([('¥28.9bn', 'Ceramics OP FY3/26 (+42%) — first year above the ¥670bn housing business'),
             ('21.8x', 'P/E FY3/27E; 17.3x FY3/28E — vs ¥9,500 peak (~27x)'),
             ('~¥615bn', 'Implied ceramics EV after valuing housing on peer regression (~15x FY3/28E EBIT)'),
             ('¥7,200', '12-mo SOTP target (+18%); P/E cross-check ¥7,216'),
             ('25%', 'Bear-case probability (memory capex downturn) — value ~¥3,500')])
y0 = y - 30
yy = d.col_head('Why now — four forces converging', L, y0, CW)
d.bullets(['<b>Reset entry:</b> Q1 FY3/27 ESC shipment slip took the stock -11.4% on 3 Aug and -36% from the June high; FY guidance (OP ¥60bn) unchanged.',
           '<b>Capacity step-up:</b> Buzen kiln adds >20% ESC capacity in Jan 2027 into an accelerating NAND cryo-etch cycle (Lam: installed base to triple in 3–5 yrs).',
           '<b>Housing self-help:</b> China plants closed (~¥7bn improvement), largest Japan price rise in a decade (8–13%, 1 Dec 2026), Georgia plant ramping.',
           '<b>Activist round two:</b> Palliser won disclosure and capex; capital efficiency (~¥200bn excess capital) is the open item for STAGE3 (Apr 2027).'], L, yy, CW, gap=6)
yy = d.col_head('What has to go right', R, y0, CW)
d.bullets(['H1 FY3/27 (~30 Oct) confirms the ceramics miss was timing — H1 ceramics OP ≥ ¥15bn.',
           'NAND WFE recovery continues (GS: $11bn → $15bn → $22bn, 2026–28) and Lam keeps TOTO as the primary cryo-ESC source.',
           'Japan price rise sticks without share loss to LIXIL/Panasonic; China reaches break-even.',
           'STAGE3 plan sets ROE ≥10–12%, cross-holding exit and buyback framework.'], R, yy, CW, sq=SLATE, gap=6)
d.callout('<b>Position sizing:</b> event-driven, mid-weight. A ¥1tn Japanese large-cap that now behaves like a semiconductor-equipment supplier (±11% days on broker notes and results) — two very different investor bases own it, and the hand-off between them creates the volatility we want to exploit.', L, 98, W - 68, dark=False)
d.next()

# 3 Business overview
d.header('Business overview', 'Context', 'TOTO at a glance: two businesses, one P&L')
yy = d.col_head('What it does', L, H - 110, CW)
yy = d.bullets(['Japan\'s category-defining bathroom brand: ~60% of Japanese toilets; inventor of the Washlet (1980); >80% household bidet-seat penetration in Japan.',
                '~72% of Japan housing sales are remodel/replacement — a steady but ~4%-margin annuity squeezed by costs and falling new-build.',
                'Since 1988 TOTO has made electrostatic chucks — the wafer-holding "table" inside etch tools; co-developed with Lam Research since ~1990; reported #2 globally.'], L, yy, CW, gap=6)
c.setFont('Lib-B', 10.5); c.setFillColor(INK); c.drawString(L, yy - 14, 'Segment mix — FY3/26 (year to 31 Mar 2026)')
d.table(['Segment', 'Sales', 'OP', 'Margin', 'Comment'],
        [['Japan housing', '¥479.7bn', '¥20.3bn', '4.2%', 'Remodel +1%, new-build -3%'],
         ['China', '¥53.8bn', '-¥6.9bn', 'loss', '2 plants closed 2025'],
         ['Americas', '¥75.6bn', '~¥4.7bn', '~6%', 'Georgia plant; tariffs'],
         ['Asia/Oceania', '¥54.9bn', '¥10.2bn', '18.6%', 'Vietnam, Taiwan, India'],
         ['Advanced Ceramics', '¥67.4bn', '¥28.9bn', '42.9%', '+34% sales; ~51% of OP'],
         ['Group', '¥737.4bn', '¥53.8bn', '7.3%', 'Record OP']], L, yy - 24, [105, 62, 58, 48, 157], fs=7.8)
yy = d.col_head('Where the power sits in the supply chain', R, H - 110, CW)
yy = d.bullets(['<b>Upstream:</b> clays, brass, resins, electronics; high-purity alumina/AlN powders — commodity inputs, cost inflation hits Japan margins.',
                '<b>Midstream:</b> vertically integrated kilns and ESC sintering (Kitakyushu, Oita/Nakatsu, Buzen, Chigasaki; Vietnam, Thailand, India, China, US, Mexico).',
                '<b>Downstream:</b> plumbing wholesalers → builders/remodelers (Japan); distributors (US/Asia); Lam Research for ESCs → Samsung, SK hynix, Kioxia, Micron.'], R, yy, CW, sq=BLUE, gap=6)
d.callout('<b>The single most distinctive fact:</b> 9% of revenue now produces over half the profit — and the two halves deserve multiples ~2x apart (housing ~9x EBIT, ceramics ~18x). The consolidated P&L hides this; the 2026 segment disclosure, won by the activist, exposes it.', R, yy - 6, CW)
d.next()

# 4 Setup / price
d.header('The setup', 'Context', 'A five-year round-trip: from China-beta to AI-memory momentum and back to earth')
d.image(I + 'price.png' if False else 'img/price.png', L, H - 100, 560)
c.setFont('Lib-I', 7); c.setFillColor(GREY); c.drawString(L, H - 360, 'JPY/share; levels reconstructed from annual OHLC and reported event closes; illustrative between points.')
yy = d.col_head('Key catalysts', 615, H - 108, 310)
for dt, tx in [('OCT 2024', 'China loss + ¥34bn impairment: -12.5% in a day.'), ('APR 2025', 'US tariff low ¥3,269; ¥20bn buyback; China plant closures.'),
               ('JAN–FEB 2026', 'Goldman upgrade (+11%); Palliser Capital Value Enhancement Plan.'), ('1 MAY 2026', 'Record FY3/26, ceramics disclosure: limit-up +18%.'),
               ('23 JUN 2026', 'ATH ¥9,500 on reported ¥80bn chip-parts programme.'), ('3 AUG 2026', 'Q1 FY3/27 miss on ESC timing: -11.4%; now ¥6,097.')]:
    c.setFont('Lib-B', 8.5); c.setFillColor(BLUE); c.drawString(615, yy, dt)
    h = d.para(tx, 615, yy - 5, 310, ps('kc', 8.6, 'Lib', INK, 11)); yy -= h + 20
    c.setStrokeColor(colors.HexColor('#E3E6EC')); c.line(615, yy + 8, 925, yy + 8)
d.next()

# 5 Two businesses
d.header('Question 1 — what are we actually buying?', 'Mix shift', 'Ceramics went from 16% to ~51% of segment profit in four years')
d.image('img/seg_mix.png', L, H - 100, 520)
yy = d.col_head('Why the ceramics franchise is real', 580, H - 108, 345)
yy = d.bullets(['<b>Replacement annuity:</b> ~80% of segment sales are recurring chuck replacements (~1-year cycle, per Palliser).',
                '<b>Switching costs:</b> process-of-record part; requalification 12–24 months; 35-year Lam co-design loop; Lam Supplier Excellence 2023 and 2024.',
                '<b>Growth:</b> NAND layer counts → ~1,000 by 2030 makes cryo-etch indispensable; Buzen +20% (Jan 2027); ~¥30bn capex to FY2028, ~¥80bn 5-yr reported.',
                '<b>Margin:</b> 42.9% OP margin — 3x NGK Insulators, 2x Niterra.'], 580, yy, 345, gap=6)
d.callout('<b>But note FY3/24 (e):</b> ceramics OP fell ~35% in the last memory downturn. This is a cyclical growth asset, not a bond.', 580, yy - 4, 345, dark=False)
d.next()

# 6 Valuation vs peers
d.header('Question 2 — is TOTO cheap?', 'Valuation', 'Not on consolidated multiples — only once the parts are separated')
d.table(['Metric', 'TOTO', 'LIXIL', 'Rinnai', 'Takara', 'Masco', 'Geberit', 'NGK Ins.', 'Niterra', 'Kyocera'],
        [['EV/Sales', '1.27x', '0.66x', '0.75x', '0.41x', '2.1x', '6.9x', '~2.5x', '~2.3x', '~1.1x'],
         ['EV/EBITDA', '10.6x', '9.0x', '5.3x', 'n/a', '11.6x', '23.5x', '12.0x', '9.5x', '7.8x'],
         ['EV/EBIT', '17.4x', '~26x', '~7x', '5.4x', '~12.5x', '~29x', '~17x', '~12x', '~20x'],
         ['P/E (fwd)', '21.8x', '57x (t)', '13.6x', '13.8x', '14.6x', '29.8x', '22.3x', '~16x', '16.7x'],
         ['EBIT margin', '7.3%', '2.5%', '10.7%', '7.5%', '16.8%', '~24%', '14.2%', '18.9%', '5.2%'],
         ['Net debt/EBITDA', 'net cash', '~4x', 'net cash', 'net cash', '~1.9x', '~1.0x', 'low', 'net cash', 'net cash']],
        L, H - 105, [110] + [88] * 9, hl_col=1)
d.note('TOTO: EV/EBITDA, EV/EBIT on FY3/26A; P/E on our FY3/27E. Peers: latest FY / forward, Jul–Sep 2026, data aggregators; indicative (~ = derived).', L, H - 268, 880)
yy = d.col_head('What the comparison shows', L, H - 300, CW)
d.bullets(['On consolidated metrics TOTO trades at a premium to every Japanese housing peer (P/E 21.8x vs 13–14x) despite lower margins.',
           'It trades in line with technical-ceramics peers (NGK 22x fwd P/E) — yet ~65% of its sales are low-margin housing.',
           'Historical EV/EBITDA (10-yr median 13.7x) says cheap; P/B ~2.0x and P/E ~22x say fair.'], L, yy, CW, gap=6)
yy = d.col_head('The honest counter-read', R, H - 300, CW)
d.bullets(['The "premium" is the market already paying for ceramics — it is not a mispricing of the whole.',
           'At ¥9,500 the stock discounted ~30x FY3/28E: the June peak was momentum, not fundamentals.',
           'Consensus EPS (~¥295) sits above company guidance (¥280) after a Q1 miss — near-term estimate risk remains.'], R, yy, CW, sq=SLATE, gap=6)
d.next()

# 7 Regression
d.header('Question 2 — is TOTO cheap?', 'Valuation', 'The peer regression says expensive as a whole, fair-to-cheap as a sum of parts')
c.setFont('Lib-B', 10.5); c.setFillColor(INK); c.drawString(L, H - 100, 'EV/Sales vs EBIT margin — 12 listed peers')
d.image('img/regression.png', L, H - 110, 520)
d.note('All peers: EV/S = 0.225×margin – 0.84, R² = 0.70; ex-Geberit: EV/S = 0.124×margin – 0.04, R² = 0.75. At TOTO\'s 7.3% consolidated margin the fitted EV/Sales is 0.81–0.87x vs 1.27x actual.', L, H - 372, 520)
yy = d.col_head('Reading the regression', 580, H - 108, 345)
d.bullets(['<b>Consolidated:</b> TOTO sits ~45–55% above the line — the statistical outlier is expensive, not cheap.',
           '<b>SOTP read:</b> housing (4.2% margin) on the line = 0.48x sales ≈ ¥320bn EV. That leaves ~¥615bn for ceramics: ~9x sales, ~19x FY3/27E and ~15x FY3/28E EBIT.',
           '<b>Sanity check:</b> NGK trades ~17x EBIT on a 14% margin; a 43%-margin, 15–25%-growth ceramics consumable at ~15x FY3/28E is undemanding.',
           '<b>Implication:</b> the re-rating case depends on the market continuing to capitalise ceramics separately — which better disclosure (Palliser\'s ask) makes durable.'], 580, yy, 345, gap=7)
d.next()

# 8 Earnings trajectory
d.header('Question 3 — what are we underwriting?', 'Earnings', 'EPS +45% in two years: ceramics capacity plus housing self-help')
d.table(['JPY bn unless stated', 'FY3/26A', 'FY3/27E', 'FY3/28E', 'FY3/29E'],
        [['Net sales', '737.4', '765', '800', '833'], ['Ceramics sales', '67.4', '77.5', '95.0', '110.0'],
         ['Ceramics OP (margin)', '28.9 (42.9%)', '32.5 (42%)', '40.4 (42.5%)', '46.2 (42%)'],
         ['Housing OP (incl. China)', '27.9', '30.5', '41.0', '45.0'], ['Group OP', '53.8', '60.0', '78.0', '87.5'],
         ['OP margin', '7.3%', '7.8%', '9.8%', '10.5%'], ['Net income', '40.3', '45.7', '57.0', '63.8'],
         ['EPS (¥)', '243', '280', '352', '396'], ['Consensus EPS (¥)', '—', '~295', '~353', 'n/a'], ['DPS (¥)', '110', '120', '140', '160']],
        L, H - 105, [170, 105, 105, 105, 105], hl_col=None)
d.note('Our estimates; company FY3/27 guidance: sales ¥785bn, OP ¥60bn, NI ¥46bn, EPS ¥279.8, DPS ¥120 (unchanged at Q1).', L, H - 390, 590)
yy = d.col_head('Reading the trajectory', 660, H - 108, 265)
d.bullets(['FY3/27 is a transition year: Q1 OP -1.6%, Middle East -¥3bn, Japan costs; we sit on guidance, below consensus.',
           'FY3/28 is the inflection: full-year Japan price rise, Buzen capacity, China at break-even.',
           'Sensitivity: ±10% ceramics sales = ±¥3.5bn OP = ±¥15 EPS.',
           'ROE ~7.7% → ~10% by FY3/28E — still below the ≥12% WILL2030 target without buybacks.'], 660, yy, 265, gap=6)
d.next()

# 9 Latest result
d.header('Latest result — Q1 FY3/27 (reported 31 Jul 2026)', 'Earnings', 'A timing miss, punished like a thesis break')
y = d.tiles([('¥168.6bn', 'Sales +1.7% vs ~¥176.5bn consensus (-4.5%)'), ('¥8.07bn', 'OP -1.6%; 13.5% of FY guide (normal ~18–20%)'),
             ('¥42.0', 'EPS vs ¥45.6 consensus (-8%)'), ('-11.4%', 'Share-price reaction, 3 Aug 2026')])
yy = d.col_head('What drove it', L, y - 30, CW)
d.bullets(['Ceramics sales only +6% (OP +10%) vs +27% FY plan — chuck shipment timing.',
           'Japan housing OP -46%: procurement and labour costs, weak new-build.',
           'Middle East order suspension and costs: ~-¥3bn OP; FX gain +¥1.1bn below the line.',
           'Full-year guidance held; Dec 2026 price rise (8–13%) announced.'], L, yy, CW, gap=6)
yy = d.col_head('Sentiment tracker (management tone, 1–5)', R, y - 30, CW)
d.table(['Event', 'Focus', 'Tone'],
        [['Oct 2024 (H1 FY3/25)', 'China loss, impairment', '1.5'], ['Apr 2025 (FY3/25)', 'Restructure, buyback', '2.5'],
         ['Oct 2025 (H1 FY3/26)', 'Ceramics surge', '3.0'], ['Apr 2026 (FY3/26)', 'Record, disclosure, capex', '4.5'],
         ['Jul 2026 (Q1 FY3/27)', 'Timing, costs, guide held', '3.0']], R, yy, [130, 230, 70], fs=7.8)
d.callout('<b>Signal:</b> the stock was priced for uninterrupted acceleration. H1 results (~30 Oct) are the test of whether Q1 was timing (our base case) or the start of a NAND air-pocket.', L, 110, W - 68, dark=True)
d.next()

# 10 Activism
d.header('Is there an activist in here?', 'Catalyst', 'Palliser won round one; capital efficiency is round two')
y = d.tiles([('17 Feb 2026', 'Palliser Capital publishes "Value Enhancement Plan" — top-20 holder (<5%)'), ('>55%', 'Upside claimed; intrinsic value ~¥8,800/share'),
             ('30 Apr 2026', 'TOTO adopts the substance; Palliser "welcomes adoption" (7 May)'), ('~¥200bn', 'Returnable capital (excess equity, ~¥76bn cross-holdings, cash) (e)')])
d.table(['Palliser demand', 'TOTO response', 'Status'],
        [['Disclose Advanced Ceramics', 'Two-segment reporting; ceramics sales/OP/margin and FY plan', 'Achieved'],
         ['Invest more in ceramics', '~¥30bn capex to FY2028; Buzen +20%; ~¥80bn 5-yr reported', 'Achieved'],
         ['Restructure low-profit housing / China', 'Plant closures (pre-dated campaign); ~¥7bn improvement targeted', 'Partial'],
         ['Capital efficiency / equity ratio', 'DPS ¥110 → ¥120; buyback; cross-holdings <10% of net assets', 'Open']], L, y - 22, [230, 520, 142])
d.callout('<b>Assessment:</b> no proxy fight was needed — a dispersed register (trust banks ~28%, life insurers ~9%) and TSE pressure made management receptive. The STAGE3 mid-term plan (~Apr 2027) is the natural venue for round two: ROE target, equity-ratio policy, cross-holding exit and a multi-year buyback. That is the special-situations catalyst.', L, 130, W - 68)
d.next()

# 11 Takeover
d.header('Question 4 — takeover, carve-out or self-help?', 'M&A', 'A whole-company bid is unlikely; a ceramics structural option is not')
d.table(['Path', 'Probability (24m)', 'Indicative value', 'Precedent / logic'],
        [['Whole-company take-private', '5–10%', '13–14x EBITDA → ¥8,000–8,600 (+30–40%)', 'FEFTA screening; stable holders; size ~US$7bn'],
         ['Ceramics IPO / minority sale / spin', '10–15%', 'Ceramics ¥600–800bn (12–15x EBITDA)', 'Shinko → JIC (~¥685–700bn, ~12–13x EBITDA e)'],
         ['Self-help: buybacks + cross-holding exit', '50%+', '+5–10% EPS accretion over 3 yrs', 'TSE P/B reform; Palliser'],
         ['Status quo', 'remainder', 'SOTP ¥7,200', '—']], L, H - 105, [210, 120, 260, 302])
yy = d.col_head('Relevant deal multiples (2021–26)', L, H - 265, CW)
d.bullets(['Villeroy & Boch / Ideal Standard (2023): ~€600m, 8.1x EBITDA.', 'Zurn / Elkay (2022): $1.56bn, 14.2x EBITDA (9.8x post-synergy).',
           'RWC / EZ-Flo (2021): $325m, 12x EBITDA.', 'JIC / Shinko Electric (2023–25): ~¥685–700bn incl. Fujitsu stake.'], L, yy, CW, gap=5)
yy = d.col_head('Impediments', R, H - 265, CW)
d.bullets(['FEFTA: semiconductor parts are a "core" sector — foreign bidders face review.', 'Lam change-of-control risk on the ESC franchise.',
           'Morimura-group heritage, lifetime-employee management, no M&A track record (organic grower since 2016).'], R, yy, CW, sq=SLATE, gap=5)
d.next()

# 12 Scenarios
d.header('Scenario analysis', 'Valuation', 'Asymmetry is acceptable, not compelling: +64% / -43%')
d.table(['Scenario', 'Prob.', 'Key assumptions', 'EPS FY3/29E', 'Multiple', 'Value'],
        [['Bull', '25%', 'Ceramics ¥125bn sales (+23% CAGR), 44% margin; housing OP ¥50bn; buybacks', '~¥470', 'Ceramics 22x EBIT; housing 12x', '~¥10,000 (+64%)'],
         ['Base', '50%', 'Ceramics ¥110bn (+18% CAGR), 42%; China break-even; price rise sticks', '~¥396', 'SOTP 18x / 9x (FY3/28E)', '~¥7,200 (+18%)'],
         ['Bear', '25%', 'NAND capex downturn: ceramics flat ~¥60bn at 35%; housing ¥26bn', '~¥220', 'Ceramics 12x; housing 8x; ~16x P/E', '~¥3,500 (-43%)'],
         ['Prob.-weighted', '', '', '', '', '~¥6,975 (+14%)']], L, H - 105, [80, 45, 380, 80, 170, 137], hl_col=5)
d.image('img/football.png', L, H - 260, 520)
yy = d.col_head('What moves us between cases', 580, H - 268, 345)
d.bullets(['Lam/NAND WFE commentary (21 Oct) and TOTO H1 ceramics (~30 Oct).', 'Japan volumes after the 1 Dec price rise.',
           'STAGE3 capital-return framework (Apr 2027).', 'Any evidence of Lam dual-sourcing or TEL cryo-etch wins.'], 580, yy, 345, gap=6)
d.next()

# 13 Bear / short-seller
d.header('The short-seller\'s case', 'Bear case', 'One technology, one customer, one end market — and a 4%-margin anchor')
yy = d.col_head('Dismantling the bull case', L, H - 108, CW)
d.bullets(['<b>Concentration:</b> >50% of group OP from cryo-ESCs, largely sold to Lam Research for NAND.',
           '<b>Most underestimated competitor:</b> Tokyo Electron — its cryo-etch success would reallocate the installed base away from the Lam platform TOTO is embedded in.',
           '<b>Moat weaker than it looks:</b> AMAT/Lam in-house ESCs; JIC-backed Shinko; NGK/Kyocera scale in AlN. 43% margins invite price pressure.',
           '<b>Worst capital allocation:</b> China — ~¥49bn written off 2024–26; persistent over-capitalisation (equity ratio ~64%, ROE <8%).',
           '<b>Growth -20–30%:</b> EPS ~¥300–320 by FY3/29 → ¥5,100–5,400 at 17x; ~¥4,300 at 14x.'], L, yy, CW, gap=6)
yy = d.col_head('Accounting / forensic flags', R, H - 108, CW)
d.table(['Area', 'Flag', 'Risk'],
        [['Revenue recognition', 'Shipment-based; Q1 "timing" lumpiness', 'Med'], ['Segment reporting', '3 → 2 segments obscures China; cost allocation opaque', 'Med'],
         ['Impairments', '¥34bn + ~¥15bn China "one-offs"', 'Med'], ['Earnings quality', 'Ordinary > OP by ¥6.9bn (FX, dividends)', 'Low–Med'],
         ['Provisions', 'Washlet/faucet recalls', 'Low–Med'], ['Incentives', 'OP-linked cash bonus; little equity pay', 'Med'],
         ['Goodwill / SBC / related parties', 'Minimal / none identified', 'Low']], R, yy, [120, 250, 60], fs=7.6)
d.callout('<b>Single permanent-impairment scenario:</b> NAND moves to a non-cryogenic high-aspect-ratio etch route (or TEL wins the next node) while Lam qualifies a second ESC source. We put this at ~10–15% over three years.', L, 95, W - 68, dark=True)
d.next()

# 14 Balance sheet & ownership
d.header('Balance sheet, capital returns & ownership', 'Capital', 'Under-levered, over-capitalised — the self-help lever')
y = d.tiles([('63.8%', 'Equity ratio (Mar 2026) — reported'), ('~¥65bn', 'Net cash (e); net debt/EBITDA ≈ -0.7x'),
             ('¥60–76bn', 'Cross-shareholdings (e); target <5% of net assets by FY2030'), ('¥120', 'FY3/27 DPS guide (payout ≥40%, progressive); ¥20bn buyback 2025 cancelled')])
yy = d.col_head('Top holders (approx., Mar 2026)', L, y - 30, CW)
d.table(['Holder', 'Type', '%'], [['Master Trust Bank of Japan', 'Custodian', '~17–19%'], ['Custody Bank of Japan', 'Custodian', '~9.8%'], ['Meiji Yasuda Life', 'Life insurer', '~6.1%'],
                                 ['Nippon Life', 'Life insurer', '~3.2%'], ['State Street (2 a/c)', 'Foreign custodian', '~3.9%'], ['Employee Stock Ownership', 'Insider', '~2.0%'],
                                 ['Nomura AM group (5% rpt)', 'Institutional', '~8.0%'], ['Palliser Capital', 'Activist', '<5%']], L, yy, [200, 140, 90], fs=7.4)
yy = d.col_head('Management & board', R, y - 30, CW)
d.bullets(['President Shinya Tamura (since Apr 2025; ex-US/Vietnam head); Chairman Noriaki Kiyota (President 2020–25); CFO Tomoyuki Taguchi.',
           'Professional lifetime managers; negligible insider ownership; pay ~¥140–170m for top executives, OP-linked.',
           'Board cut 13 → 10 at June 2026 AGM, 50% independent.',
           'Short interest low (~1–2% e); reporters mostly quant/market-makers (Millennium, Qube, UBS, MS MUFG).'], R, yy, CW, gap=6)
d.next()

# 15 Catalyst calendar
d.header('Catalyst calendar', 'Catalysts', 'Lam, H1 results and the price rise dominate the next two quarters')
items = [('21 OCT 2026', 'Lam Research Sep-quarter results', 'NAND/cryo-etch demand read-across for ESC orders.', 'HIGH'),
         ('~30 OCT 2026', 'TOTO H1 FY3/27 results', 'Was Q1 timing? Ceramics H1 OP, FY guidance, consensus reset.', 'CRITICAL'),
         ('1 DEC 2026', 'Japan price increase (8–13%)', 'Pre-buying in Oct–Nov; elasticity and competitor follow-through.', 'HIGH'),
         ('JAN 2027', 'Buzen ESC kiln complete; Q3 results (~29 Jan)', '+20% capacity online; seasonal Q3 profit test.', 'HIGH'),
         ('~LATE APR 2027', 'FY3/27 results + STAGE3 mid-term plan', 'ROE, equity ratio, buybacks, cross-holding exit — activist round two.', 'CRITICAL'),
         ('ONGOING', 'US tariffs, Palliser / 5% filings, cross-holding sales', 'Americas margin; activist re-engagement.', 'HIGH')]
y = H - 112
for dt, t1, t2, imp in items:
    c.setFillColor(NAVY); c.rect(L, y - 30, 130, 32, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont('Lib-B', 8.5); c.drawCentredString(L + 65, y - 18, dt)
    c.setFillColor(INK); c.setFont('Lib-B', 10); c.drawString(L + 150, y - 10, t1)
    c.setFillColor(GREY); c.setFont('Lib', 8.6); c.drawString(L + 150, y - 24, t2)
    c.setFillColor(RED if imp == 'CRITICAL' else BLUE); c.rect(W - 34 - 95, y - 27, 95, 26, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont('Lib-B', 8.2); c.drawCentredString(W - 34 - 47.5, y - 17, imp)
    y -= 56
d.next()

# 16 Risks grid
d.header('Key risks', 'Risks', 'What would make this thesis wrong')
risks = [('Memory capex downturn', 'NAND makers pause after the 2026 upgrade wave; ceramics OP falls ~35% as in FY3/24 and the multiple compresses at the same time.'),
         ('Customer concentration', 'Lam qualifies a second ESC source or loses cryo-etch share to Tokyo Electron — the franchise economics reset permanently.'),
         ('Japan housing erosion', 'Starts fall toward ~600k; the Dec 2026 price rise loses share; costs keep Japan margins near 3–4%.'),
         ('China relapse', 'Break-even slips again; further impairments on remaining Zhangzhou/Dalian assets.'),
         ('Capital hoarding', 'STAGE3 prioritises the ¥1tn sales target and capex over ROE and returns; activist disengages.'),
         ('Tariffs and FX', 'US tariffs on Vietnam/Mexico/Thai/Malaysian sourcing; yen strength cuts translation and ceramics export margins.')]
gw, gh = (W - 68) / 3, 165
for i, (t, tx) in enumerate(risks):
    x = L + (i % 3) * gw; yt = H - 105 - (i // 3) * gh
    c.setFillColor(LIGHT); c.rect(x, yt - gh, gw - 1, gh - 1, fill=1, stroke=0)
    c.setFillColor(RED); c.setFont('Lib-B', 10.5); c.drawString(x + 16, yt - 24, '%02d' % (i + 1))
    d.para(t, x + 16, yt - 36, gw - 32, ps('rt', 11, 'Lib-B', INK, 14))
    d.para(tx, x + 16, yt - 58, gw - 32, ps('rx', 8.8, 'Lib', GREY, 12))
d.next()

# 17 Agenda / questions
d.header('If we escalate: our own agenda', 'Our agenda', 'Engage on capital allocation and ceramics transparency, alongside Palliser')
yy = d.col_head('Top questions for the CEO / Chairman', L, H - 108, CW)
d.bullets(['What share of ceramics revenue is Lam, and are you sole- or dual-source on its cryo platforms?',
           'Was the Q1 shortfall purely timing — what are H1 ceramics orders and book-to-bill?',
           'Are you qualified with Tokyo Electron\'s cryogenic etch?',
           'Will STAGE3 include ROE ≥10–12%, equity-ratio and TSR targets?',
           'How much of the cross-shareholding book will be sold by FY3/29?',
           'Would the board consider structural options for ceramics if the SOTP gap persists?'], L, yy, CW, gap=5)
yy = d.col_head('Sizing & monitoring', R, H - 108, CW)
d.bullets(['Mid-weight, event-driven: build into H1 results (~30 Oct); add on confirmation of ceramics re-acceleration.',
           'Hard trigger: reassess if H1 ceramics OP is down y/y with no timing explanation, or FY ceramics plan (¥85.5bn) is cut.',
           'Track Lam (21 Oct) and AMAT (~mid-Nov) commentary on NAND cryo-etch as leading indicators.',
           'Pair option: long TOTO / short Japanese housing basket (LIXIL, Takara) isolates the ceramics re-rating.'], R, yy, CW, sq=SLATE, gap=6)
d.next()

# 18 IC decision
d.dark_bg()
c.setFont('Lib-B', 9.5); c.setFillColor(LB); c.drawString(45, H - 40, 'INVESTMENT COMMITTEE DECISION')
c.setStrokeColor(colors.HexColor('#2B3A55')); c.line(45, H - 52, W - 45, H - 52)
d.para('Recommendation: BUY', 45, H - 70, 700, ps('rb', 30, 'Lib-B', WHITE, 36))
d.tiles([('¥7,200', '12-mo target (+18%); prob.-weighted ~¥6,975'), ('~¥615bn', 'Implied ceramics EV — ~15x FY3/28E EBIT'), ('21.8x', 'P/E FY3/27E; 17.3x FY3/28E'), ('~¥200bn', 'Returnable capital — activist round two')],
        y_top=H - 125, h=78, x0=45, w_total=W - 90, dark=True, hi=3)
d.bullets(['TOTO\'s consolidated multiples look full, but the peer regression shows the premium is the market paying for ceramics — housing alone is worth only ~¥320bn.',
           'At ¥6,097 the ~43%-margin ESC franchise is capitalised at ~15x FY3/28E EBIT, after a timing-driven 36% pull-back from the June high.',
           'Housing self-help (China break-even, Dec 2026 price rise, US ramp) adds non-cyclical earnings the momentum sell-off ignored.',
           'The activist has won disclosure and capex; capital efficiency in the April 2027 STAGE3 plan is the next special-situations catalyst.'], 45, H - 230, 520, style=BULW, sq=LB, gap=9)
c.setFillColor(WHITE); c.rect(600, 95, W - 645, 235, fill=1, stroke=0)
d.para('Sizing & monitoring', 620, 315, 280, ps('sm', 13, 'Lib-B', INK, 16))
c.setStrokeColor(BLUE); c.setLineWidth(1.5); c.line(620, 293, 720, 293)
d.para('Mid-weight, event-driven: a large-cap with semiconductor-style volatility and a 25% bear case (memory downturn, ~¥3,500).', 620, 282, 280, ps('s1', 9, 'Lib', INK, 12))
d.para('Hard trigger: reassess if H1 FY3/27 (~30 Oct) shows ceramics OP down y/y without a timing explanation.', 620, 222, 280, ps('s2', 9, 'Lib', INK, 12))
d.para('Catalyst watch: Lam (21 Oct), H1 results, 1 Dec price rise, Buzen capacity (Jan 2027), STAGE3 plan (Apr 2027).', 620, 162, 280, ps('s3', 9, 'Lib', INK, 12))
c.setStrokeColor(colors.HexColor('#2B3A55')); c.line(45, 55, W - 45, 55)
c.setFont('Lib', 8); c.setFillColor(SLATE)
c.drawString(45, 38, 'TOTO Ltd | TSE: 5332 | Reference price ¥6,097 (2 Oct 2026) | 4 October 2026 | Not investment advice; estimates marked (e) — see full report')
d.next()
d.save()
print('deck ok')
