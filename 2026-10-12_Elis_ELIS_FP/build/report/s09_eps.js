const { readJSON, f1, pct } = require('./util');
const F = readJSON('model/main_forecast.json');
const b = F.results.base;
const row = (lab, k, fmt) => [lab, ...b.map(r => fmt(r[k]))];
const scen = ['bear', 'base', 'bull'].map(s => [s[0].toUpperCase() + s.slice(1), ...F.results[s].map(r => `€${r.headline_eps_dil.toFixed(2)} (${pct(r.eps_growth * 100, 1, true)})`)]);
module.exports = [
  { t: 'h1', text: '9. EPS estimates, FY2026E–FY2028E' },
  { t: 'p', text: 'We forecast **headline diluted EPS** (the company\'s KPI, excluding amortisation of acquired customer relationships, IFRS 2 charges and non-recurring items) and reconcile to IFRS EPS. No forward EPS consensus is available for Elis in S&P Capital IQ or ProntoNLP, so our estimates are compared with company guidance and the 2025–28 Capital Markets Day framework.' },
  { t: 'table', title: 'Base-case forecast (EUR m unless stated)', cols: ['', 'FY2025A', 'FY2026E', 'FY2027E', 'FY2028E'], widths: [2.8, 1, 1, 1, 1], size: 15, highlightRows: [10], rows: [
    ['Revenue', '4,796.8', ...b.map(r => f1(r.revenue, 0))],
    ['  growth (organic + M&A + FX)', '+4.9%', ...b.map(r => pct(r.rev_growth * 100, 1, true))],
    ['Adj. EBITDA', '1,700.1', ...b.map(r => f1(r.adj_ebitda, 0))],
    ['  margin', '35.4%', ...b.map(r => pct(r.ebitda_margin * 100, 1))],
    ['Adj. EBIT', '766.6', ...b.map(r => f1(r.adj_ebit, 0))],
    ['  margin', '16.0%', ...b.map(r => pct(r.ebit_margin * 100, 1))],
    ['Net financial expense (headline)', '~131', ...b.map(r => f1(r.net_fin_exp, 0))],
    ['Tax rate (headline)', '~26.5%', ...b.map(r => pct(r.tax_rate * 100, 1))],
    ['Headline net income', '467.3', ...b.map(r => f1(r.headline_ni, 0))],
    ['Diluted shares (m)', '259.1', ...b.map(r => f1(r.diluted_shares, 1))],
    ['Headline diluted EPS (€)', '1.85', ...b.map(r => r.headline_eps_dil.toFixed(2))],
    ['  growth', '+5.2%', ...b.map(r => pct(r.eps_growth * 100, 1, true))],
    ['IFRS diluted EPS (€) [e]', '1.46', '1.58', '1.77', '1.97'],
    ['P/E (headline) at €21.26', '11.5x', ...b.map(r => r.pe_at_price.toFixed(1) + 'x')],
  ], source: 'FY2025A: Elis (adj. EBITDA €1,700.1m [#5321](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-5321); headline NI €467.3m [#279](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-279); headline diluted EPS €1.85 [#28](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-28)); diluted shares S&P weighted average 259.1m. Estimates [e]: model/main_forecast.py.' },
  { t: 'h2', text: 'Building blocks' },
  { t: 'bullets', items: [
    '**Industry growth and market share:** European textile services grow roughly with GDP plus outsourcing; Elis targets ~4% organic (CMD). We model organic +3.3% in 2026 (H1 +3.2%; Mexico −€14m), 3.8% in 2027 (record signings, German healthcare contract ~€20m [#108](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-108)) and 4.0% in 2028, plus ~1pt of bolt-on M&A a year (budget €50–150m at ~1.2x sales) and neutral FX after 2026.',
    '**Price increases vs cost pressure:** wages ~+4% a year (~60% of costs) need ~1.7% price to neutralise; end-2026 indices are "strong". We assume price slightly above cost inflation from 2027, giving +15–20bp a year of EBITDA margin (CMD target ~20bp).',
    '**Operating leverage:** D&A stays ~19.4–19.6% of revenue, so adjusted EBIT margin rises only from 16.0% to 16.4% by 2028. 2026 includes €20–25m of Middle East energy/commodity costs, half offset.',
    '**Financing costs:** net financial expense rises from ~€131m (2025) to ~€155m (2026) on buyback debt and the €600m 3.875% March-2026 bond, then ~€150m as the OCEANE converts (removing ~€362m of debt) and the 4.125% 2027 bond is refinanced.',
    '**Share count:** the €466.8m buyback (17.8m shares at €26.25) cuts the diluted count ~5% on average in 2026 and ~7% in 2027; the OCEANE\'s 23.8m shares are already in the diluted count and will be delivered largely from treasury. We assume €100m a year of buybacks in 2027–28.',
  ] },
  { t: 'table', title: 'Scenario EPS paths (headline diluted)', cols: ['Scenario', 'FY2026E', 'FY2027E', 'FY2028E'], widths: [1.5, 1.5, 1.5, 1.5], size: 15, rows: scen },
  { t: 'callout', title: 'Versus guidance', text: 'Management guides "high single-digit" headline EPS growth for 2026 (≈€1.98–2.02). Our €1.96 (+5.9%) is ~2% below the mid-point because H1 grew only +5.1% and H2 carries higher interest and energy costs. Our 2027–28 numbers (+9–10% a year) sit within the CMD ambition that EPS grows faster than revenue, helped by the buyback.' },
];
