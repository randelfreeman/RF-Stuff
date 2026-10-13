const { readCSV, pct, f1, IMG } = require('./util');
const { sp } = require('./refs');
const S = readCSV('model/F_segments_annual.csv');
const PE = readCSV('model/F_product_endmarket.csv');
const segs = ['France', 'Central Europe', 'Scandinavia & Eastern Europe', 'UK & Ireland', 'Latin America', 'Southern Europe'];
const yrs = ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026'];
const cell = (s, p, k) => { const r = S.find(x => x.segment.startsWith(s.slice(0, 12)) && x.period === p); return r && r[k] !== '' ? r : null; };
const tbl = (k, fmt) => segs.concat(['Group']).map(s => [s].concat(yrs.map(p => { const r = cell(s, p, k); return r ? fmt(+r[k]) : 'n/a'; })));
const mk = (s) => (s || '').match(/\[#[^\]]+\]\([^)]+\)/g)?.slice(0, 1).join('') || '';
const srcRow = segs.map(s => `${s}: ` + yrs.slice(3).map(p => { const r = cell(s, p, 'ebitda_margin'); return r ? mk(r.source) : ''; }).join(' ')).join('; ');
const h1rev = ['H1 2022', 'H1 2023', 'H1 2024', 'H1 2025'];
const revH1 = segs.concat(['Group']).map(s => [s].concat(h1rev.map(p => { const r = S.find(x => x.segment.startsWith(s.slice(0, 12)) && x.period === p); return r && r.revenue_eur_m ? f1(r.revenue_eur_m, 1) : 'n/a'; })).concat([(() => { const r = S.find(x => x.segment.startsWith(s.slice(0, 12)) && x.period === 'H1 2025'); return r && r.ebitda_eur_m ? f1(r.ebitda_eur_m, 1) : 'n/a'; })()]));
const pe = (dim, p) => PE.filter(r => r.dimension === dim && r.period === p && r.scope === 'Group');
const peRows = ['service_line', 'end_market'].flatMap(d => { const a = pe(d, 'H1 2022'), b = pe(d, 'H1 2024'); return b.filter(r => !/Other/.test(r.category)).map(r => { const o = a.find(x => x.category === r.category); return [r.category, o ? f1(o.revenue_eur_m, 1) : 'n/a', f1(r.revenue_eur_m, 1), pct(r.share_of_revenue_calc * 100, 1), o ? pct((r.revenue_eur_m / o.revenue_eur_m - 1) * 100, 1, true) : 'n/a']; }); });
const yr = ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025'];
const L = (i, p, d) => sp(i, p, d);
module.exports = [
  { t: 'h1', text: '7. Financial analysis: five years by segment and geography' },
  { t: 'p', text: 'Elis reports six geographic operating segments plus "Other" (manufacturing entities and holdings). It discloses revenue, organic growth and **adjusted EBITDA** by segment; it does **not** disclose segment EBIT or net income, so those are shown at group level only. Revenue by product line and end-market is disclosed in the half-year notes.' },
  { t: 'h2', text: '7.1 Group P&L, cash flow and balance sheet (S&P Capital IQ, EUR m)' },
  { t: 'table', cols: ['EUR m', ...yr, 'LTM Jun-26'], widths: [2.4, 1, 1, 1, 1, 1, 1.1], size: 14, rows: [
    ['Revenue', ...yr.map(p => L('Total Revenues', p, { FY2021: '3,048.3', FY2022: '3,820.9', FY2023: '4,309.4', FY2024: '4,573.7', FY2025: '4,796.8' }[p])), '4,910.8'],
    ['  growth', '8.6%', '25.3%', '12.8%', '6.1%', '4.9%', '—'],
    ['Gross profit', ...yr.map(p => L('Gross Profit', p, { FY2021: '932.1', FY2022: '1,169.1', FY2023: '1,416.1', FY2024: '1,504.2', FY2025: '1,610.2' }[p])), '1,648.4'],
    ['EBITDA (S&P definition)', ...yr.map(p => L('EBITDA', p, { FY2021: '923.6', FY2022: '1,135.0', FY2023: '1,319.2', FY2024: '1,436.0', FY2025: '1,484.6' }[p])), '1,525.7'],
    ['Adj. EBITDA (company)', '1,052.1', '1,259.6', '1,474.8', '1,609.8', '1,700.1', '1,740.1'],
    ['  margin', '34.5%', '33.0%', '34.2%', '35.2%', '35.4%', '35.4%'],
    ['EBITA (S&P)', ...yr.map(p => L('EBITA', p, { FY2021: '369.4', FY2022: '541.0', FY2023: '664.5', FY2024: '713.3', FY2025: '723.3' }[p])), 'n/a'],
    ['EBIT (S&P operating income)', ...yr.map(p => L('EBIT', p, { FY2021: '270.7', FY2022: '439.1', FY2023: '557.1', FY2024: '605.6', FY2025: '613.9' }[p])), '639.4'],
    ['  margin', '8.9%', '11.5%', '12.9%', '13.2%', '12.8%', '13.0%'],
    ['Net income (IFRS)', ...yr.map(p => L('Net Income - (IS)', p, { FY2021: '114.3', FY2022: '202.6', FY2023: '262.0', FY2024: '337.7', FY2025: '366.6' }[p])), '377.8'],
    ['Cash from operations', ...yr.map(p => L('Cash from Operations', p, { FY2021: '961.6', FY2022: '1,091.2', FY2023: '1,325.6', FY2024: '1,452.1', FY2025: '1,510.6' }[p])), '1,486.4'],
    ['Capex', ...yr.map(p => L('Capital Expenditure', p, { FY2021: '-552.8', FY2022: '-673.3', FY2023: '-797.1', FY2024: '-860.8', FY2025: '-864.0' }[p])), '-915.8'],
    ['  capex / revenue', '18.1%', '17.6%', '18.5%', '18.8%', '18.0%', '18.6%'],
    ['Net debt incl. leases (S&P)', ...yr.map(p => L('Net Debt', p, { FY2021: '3,597.4', FY2022: '3,663.6', FY2023: '3,563.7', FY2024: '3,644.3', FY2025: '3,723.4' }[p])), sp('Net Debt', 'FY2026Q2', '4,370.3')],
    ['Goodwill', ...yr.map(p => L('Goodwill', p, { FY2021: '3,818.3', FY2022: '3,914.1', FY2023: '3,979.2', FY2024: '3,932.0', FY2025: '4,039.6' }[p])), '4,066.0'],
  ], source: 'Source: S&P Capital IQ (values hyperlinked to the Capital IQ document viewer where a link was returned); company adjusted EBITDA from Elis annual reports via ProntoNLP (worker F); LTM = FY2025 + H1-26 − H1-25 [calc]. S&P EBITDA excludes items Elis adds back (IFRS 2, non-recurring), hence the gap to company adjusted EBITDA.' },
  { t: 'img', path: IMG('hist_margins.png'), widthIn: 6.3 },
  { t: 'h3', text: 'Trends and why' },
  { t: 'bullets', items: [
    '**Revenue** rose 57% from FY2021 to FY2025 (+12% CAGR) [calc]: Covid recovery and an exceptional pricing cycle (organic +21% in 2022 incl. ~8 pts price [#178](https://gam.prontonlp.com/#/ref/$SENTID_T000002760050-178), +11.8% in 2023 incl. ~9 pts [#156](https://gam.prontonlp.com/#/ref/$SENTID_T000003054377-156)), then normalisation to +5.2% (2024) and +3.8% (2025); acquisitions added 1–2 pts a year and Mexico (Lavartex, 2022).',
    '**Margins**: adjusted EBITDA margin dipped to 33.0% in 2022 (unhedged energy) and recovered to a record 35.4% in 2025 as price caught up and hedging saved ~€30m [#419](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-419). EBIT margin has stalled at ~13% (S&P) / 16.0% (company) because D&A rose to ~19.6% of revenue with heavy linen capex.',
    '**Net income** tripled from €114m to €367m as Covid-era charges fell away and operating leverage worked; growth has slowed to +8.6% in 2025 as financial costs rose (net interest −€134m vs −€91m in 2022).',
    '**Cash flow**: CFO grew 57% but capex stayed at 18–19% of revenue, so company FCF after leases was only €358.6m in 2025 (21% of adjusted EBITDA).',
  ] },
  { t: 'h2', text: '7.2 Segments: growth and adjusted EBITDA margin, FY2021–H1 2026' },
  { t: 'table', title: 'Organic growth by segment', cols: ['Segment', ...yrs], widths: [2.6, 1, 1, 1, 1, 1, 1], size: 14, rows: tbl('organic_growth', v => pct(v * 100, 1, true)) },
  { t: 'table', title: 'Adjusted EBITDA margin by segment', cols: ['Segment', ...yrs], widths: [2.6, 1, 1, 1, 1, 1, 1], size: 14, rows: tbl('ebitda_margin', v => pct(v * 100, 1)), source: 'Source: Elis annual and semi-annual reports and calls via ProntoNLP (sample citations — ' + srcRow.slice(0, 1400) + '). Full citations per cell in model/F_segments_annual.csv.' },
  { t: 'table', title: 'Half-year revenue and adjusted EBITDA by segment (EUR m) — the only periods where € segment figures are retrievable', cols: ['Segment', 'H1 2022', 'H1 2023', 'H1 2024', 'H1 2025', 'EBITDA H1 2025'], widths: [2.6, 1, 1, 1, 1, 1.1], size: 14, rows: revH1, source: 'Source: Elis semi-annual reports via ProntoNLP (model/F_segments_annual.csv). Full-year € segment revenue is only in non-indexed tables; FY2025 approximations are in Section 1.' },
  { t: 'img', path: IMG('segment_margins.png'), widthIn: 6.3 },
  { t: 'bullets', items: [
    '**France** (≈29% of revenue): low growth (+2–3%) but margin up from 38.4% (2022) to 42.7% in H1 2026 — density, pricing and productivity.',
    '**Central Europe** (≈26%): the turnaround story — Germany margin +450bp in 2024 to ~29% [FY2024 call]; margin 32.9% in 2025 but slipping in H1 2026 on German minimum wages and public healthcare tenders.',
    '**Scandinavia & Eastern Europe**: the "cash cow", but margin has drifted from 38.5% (2021) to 34.5% (H1 2026) with Danish customer losses and weak volumes.',
    '**UK & Ireland**: the Berendsen legacy fixed — margin from ~23% pre-acquisition to 32.4% — but organic growth only ~2% and competition caps further gains.',
    '**Latin America**: highest growth (8–14% organic) but volatile margins (34.9% in 2024 → 30.7% in H1 2026: minimum wages, Mexico tender loss) and FX (−8% in 2025).',
    '**Southern Europe**: best improvement — margin 27.2% (2022) to 33.7% (2025) via density and bolt-ons.',
  ] },
  { t: 'h2', text: '7.3 Revenue by product line and end-market' },
  { t: 'table', cols: ['Category', 'H1 2022 €m', 'H1 2024 €m', 'Share H1 2024', 'Change'], widths: [2.6, 1.2, 1.2, 1.2, 1], size: 14, rows: peRows, source: 'Source: Elis semi-annual report revenue-disaggregation notes via ProntoNLP (worker F, model/F_product_endmarket.csv) [calc shares].' },
  { t: 'h2', text: '7.4 Operating KPIs and trends' },
  { t: 'table', cols: ['KPI', 'Latest', 'Trend / comment'], widths: [2.2, 1.6, 5.0], align: ['l', 'l', 'l'], size: 14, rows: [
    ['Organic growth', 'H1-26 +3.2%', 'Down from +21% (2022) to 3.8% (2025); price ≈ volume; 2027 guided "better"'],
    ['Price contribution', '~half of organic', '~8 pts (2022), ~9 pts (2023), normalising to ~2 pts'],
    ['Customer retention', '~94%', 'Churn ~6% incl. failures; +~1 pt churn in 2023–24 from pricing [#452](https://gam.prontonlp.com/#/ref/$SENTID_T000003054377-452)'],
    ['New signings', 'Record Q1-26', 'Q2 better; 3–4 months to invoice [#497](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-497)'],
    ['Capex intensity', '19.5% (H1-26)', '18.0% (FY2025); guided ~18% for FY2026'],
    ['D&A / revenue', '19.7% (H1-26)', 'Peaked 2025 per management; limits EBIT leverage'],
    ['FCF / adj. EBITDA', '21% (FY2025)', 'H1-26 negative (−€30.1m)'],
    ['DSO (company)', '57 days (Jun-26)', 'vs 54 days a year earlier'],
    ['Leverage', '2.09x (Jun-26)', '1.75x Dec-25; target ~1.65x Dec-26'],
    ['Pre-tax ROCE', '14.7% (FY2025)', 'Target >15% in 2026 [#270](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-270)'],
    ['Network', '>373 laundries; 6,000+ routes/day', '11,800+ vehicles; 58,445 employees (S&P)'],
    ['Energy hedging', '93%/94% (2026)', '81%/87% (2027), 61%/53% (2028) gas/electricity'],
  ], source: 'Sources as cited and in Sections 3–4 and 8.' },
];
