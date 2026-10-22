const { readJSON, readCSV, f1, pct, IMG } = require('./util');
const E = readJSON('model/E_peer_multiples_lead.json'); const V = readJSON('model/main_valuation_history.json');
const x = (v, d = 1) => (v === null || v === undefined || !isFinite(v) || v <= 0) ? 'n/m' : v.toFixed(d) + 'x';
const rows = E.rows.map(r => [r.src_rev ? `[${r.name}](${r.src_rev})` : r.name, r.ticker, r.group.replace(' (uniform/linen rental)', ' – rental').replace('Broader business services', 'Broader').replace('Direct (hygiene services)', 'Direct – hygiene'), x(r.ev_sales, 2), x(r.ev_ebitda), x(r.ev_ebit), x(r.pe), (r.nd_ebitda ?? 0).toFixed(1) + 'x', pct(r.ebitda_m * 100, 1), pct(r.ebit_m * 100, 1), pct((r.growth_1y || 0) * 100, 1, true), pct(r.fcf_yield * 100, 1)]);
const med = (k, g) => { const a = E.rows.filter(r => r.ticker !== 'ELIS' && (!g || r.group.startsWith(g))).map(r => r[k]).filter(v => v !== null && isFinite(v) && v > 0).sort((a, b) => a - b); return a.length ? (a.length % 2 ? a[(a.length - 1) / 2] : (a[a.length / 2 - 1] + a[a.length / 2]) / 2) : null; };
const el = E.rows.find(r => r.ticker === 'ELIS');
const cmp = [['EV/Sales', 'ev_sales', 2], ['EV/EBITDA', 'ev_ebitda', 1], ['EV/EBIT', 'ev_ebit', 1], ['P/E', 'pe', 1], ['EBIT margin', 'ebit_m', 3]].map(([l, k, d]) => { const m1 = med(k, 'Direct'), m2 = med(k); const fmt = (v) => k === 'ebit_m' ? pct(v * 100, 1) : x(v, d); return [l, fmt(el[k]), fmt(m1), fmt(m2), k === 'ebit_m' ? '' : pct((el[k] / m1 - 1) * 100, 0, true), k === 'ebit_m' ? '' : pct((el[k] / m2 - 1) * 100, 0, true)]; });
const rg = E.regression;
module.exports = [
  { t: 'h1', text: '11. Valuation: peers, history and regression' },
  { t: 'h2', text: '11.1 Competitors: listed and private' },
  { t: 'table', cols: ['Company', 'Ticker', 'Listed?', 'Relevance'], widths: [2.6, 1.4, 1.2, 3.8], align: ['l', 'l', 'l', 'l'], size: 14, rows: [
    ['[Cintas Corporation](https://gam.prontonlp.com/#/ref/$COMPANY_260725)', 'CTAS US', 'Listed (Nasdaq)', 'US #1 uniform rental; acquiring UniFirst'],
    ['[UniFirst Corporation](https://gam.prontonlp.com/#/ref/$COMPANY_309966)', 'UNF US', 'Listed (NYSE), being acquired', 'US uniform rental; Cintas deal $5.5bn'],
    ['Vestis Corporation', 'VSTS US', 'Listed (NYSE)', 'Ex-Aramark Uniform; received preliminary proposals (2024)'],
    ['[Johnson Service Group PLC](https://gam.prontonlp.com/#/ref/$COMPANY_876284)', 'JSG LN', 'Listed (LSE)', 'UK linen & workwear — closest direct competitor in the UK'],
    ['[Rentokil Initial plc](https://gam.prontonlp.com/#/ref/$COMPANY_411004)', 'RTO LN', 'Listed (LSE)', 'Hygiene & pest control competitor'],
    ['[Sodexo S.A.](https://gam.prontonlp.com/#/ref/$COMPANY_808038)', 'SW FP', 'Listed (Euronext)', 'Facility services; also an Elis customer'],
    ['[ISS A/S](https://gam.prontonlp.com/#/ref/$COMPANY_26972979)', 'ISS DC', 'Listed (Copenhagen)', 'Facility services (adjacent)'],
    ['[Aramark](https://gam.prontonlp.com/#/ref/$COMPANY_1004106)', 'ARMK US', 'Listed (NYSE)', 'Food/facility services (adjacent)'],
    ['Compass, ABM, Ecolab, Bunzl', 'CPG LN, ABM US, ECL US, BNZL LN', 'Listed', 'Broader business-services / hygiene comparables'],
    ['Alsco', '—', 'Private', 'US/LatAm linen & uniform rental; mentioned as a competitor in Brazil (worker C, I13)'],
    ['Lindström, CWS (Haniel), Mewa, Salesianer Miettex', '—', 'Private [u]', 'Large European textile-service groups; not mentioned in permitted sources — listed from general knowledge [u]'],
    ['Local family laundries; in-house hospital laundries', '—', 'Private', 'Main fragmented competition and bolt-on targets [#1902](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-1902)'],
  ] },
  { t: 'h2', text: '11.2 Current multiples (LTM, S&P-standardised)' },
  { t: 'table', cols: ['Company', 'Ticker', 'Group', 'EV/Sales', 'EV/EBITDA', 'EV/EBIT', 'P/E', 'ND/EBITDA', 'EBITDA m.', 'EBIT m.', 'Sales gr.', 'FCF yld'], widths: [2.4, 0.8, 1.2, 0.8, 0.9, 0.8, 0.7, 0.9, 0.8, 0.8, 0.8, 0.8], size: 12, highlightRows: [0], rows, source: 'Source: S&P Capital IQ LTM line items (revenue, S&P EBITDA/EBIT, net income, net debt incl. leases, CFO, capex; company name links to the Capital IQ source document where returned) and ProntoNLP market capitalisation (getCompanies). Elis market cap = 215.9m shares × €21.26. EV = market cap + net debt + minorities [calc]. S&P EBITDA is not company "adjusted EBITDA". Fiscal periods differ (e.g. Cintas Aug-26, Sodexo Feb-26). No forward consensus was retrievable for these peers.' },
  { t: 'table', title: 'Elis versus peer medians', cols: ['Metric', 'Elis', 'Direct-peer median', 'All-peer median', 'vs direct', 'vs all'], widths: [1.6, 1, 1.3, 1.3, 1, 1], size: 15, rows: cmp },
  { t: 'h2', text: '11.3 Elis versus its own history' },
  { t: 'img', path: IMG('valuation_history.png'), widthIn: 6.3 },
  { t: 'table', cols: ['Year-end', 'Price €', 'EV €m', 'EV/Sales', 'EV/adj. EBITDA', 'EV/EBIT', 'P/E IFRS', 'P/E headline'], widths: [1.4, 0.8, 1, 0.9, 1.1, 0.9, 0.9, 1], size: 14, rows: V.map(v => [String(v.year), v.price.toFixed(2), f1(v.ev, 0), x(v.ev_sales, 2), x(v.ev_adj_ebitda), x(v.ev_ebit), x(v.pe_ifrs), v.pe_headline ? x(v.pe_headline) : 'n/a']), source: 'Year-end ProntoNLP close × S&P shares outstanding + S&P net debt incl. leases; S&P EBIT and diluted EPS; company adjusted EBITDA and headline EPS [calc]. Early-year prices are partly dividend-adjusted, slightly understating 2021–22 multiples. Management cited ~9.6x EV/EBITDA and P/E at the FY2024 call (company definitions).' },
  { t: 'p', text: '**Verdict: cheap versus peers and at the low end of its own range, fair on returns.** At 5.2x EV/adjusted EBITDA Elis is in the bottom half of its five-year range (5.0–6.4x) and ~20–25% below US/UK rental peers on EV/EBIT; on P/E (11x headline, 14x IFRS) it is roughly half the peer median. The discount is partly deserved — EBITDA is inflated by linen depreciation (capex ~18% of sales), ROIC is ~7% and growth has slowed — but on EV/EBIT and FCF yield (~8%) the stock still screens cheap.' },
  { t: 'h2', text: '11.4 Regression: EV/Sales versus EBIT margin' },
  { t: 'img', path: IMG('regression.png'), widthIn: 6.5 },
  { t: 'p', text: `Across 12 listed peers (ex-Elis) the OLS fit is **EV/Sales = ${rg.intercept.toFixed(2)} + ${rg.slope.toFixed(3)} × EBIT margin (%)**, R² = ${rg.r2.toFixed(2)} [calc]. At Elis's LTM S&P EBIT margin of 13.0% the line implies **${rg.elis_implied.toFixed(2)}x** sales against an actual **${rg.elis_actual.toFixed(2)}x** — a ~42% discount, equivalent to ~€50 a share if fully closed [calc]. Caveats: the fit is pulled up by Cintas and Ecolab (high-margin, high-growth US compounders); among direct rental peers alone Elis sits next to Rentokil (1.96x at a similar margin) and above JSG (1.29x). We therefore treat the regression as evidence of relative cheapness, not a target.` },
];
