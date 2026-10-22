const { readCSV } = require('./util');
const { sp } = require('./refs');
const D = readCSV('model/C_debt_instruments.csv');
const mk = (s) => (s || '').match(/\[#[^\]]+\]\([^)]+\)/g)?.slice(0, 1).join('') || '';
module.exports = [
  { t: 'h1', text: '10. Capital structure, debt, covenants and liquidity' },
  { t: 'kpis', items: [{ v: '€3,670m', l: 'Net financial debt excl. IFRS 16, 30-Jun-2026 (Dec-25: €3,020m)' }, { v: '2.09x', l: 'Leverage (covenant definition); covenant <3.75x' }, { v: '€1.35bn', l: 'Liquidity: €447m cash + €900m undrawn RCF' }, { v: 'BBB- / Baa3', l: 'S&P / Moody\'s, both stable' }] },
  { t: 'p', text: `S&P Capital IQ shows total debt including leases of ${sp('Total Debt', 'FY2026Q2', '€4,816.9m')} and net debt of ${sp('Net Debt', 'FY2026Q2', '€4,370.3m')} at 30-Jun-2026 (of which ~€700m IFRS 16 lease liabilities), against ${sp('Net Debt', 'FY2025', '€3,723.4m')} at Dec-2025. On the company definition (excluding leases) net financial debt was €3,670.3m, up €650m in six months: buyback €466.8m, dividend €105.6m, M&A €36m and negative FCF [#103](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-103) [#104](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-104).` },
  { t: 'table', title: 'Debt instruments', cols: ['Instrument', 'Issued', 'Amount', 'Coupon', 'Maturity', 'Status / terms'], widths: [2.2, 1.2, 0.9, 0.9, 1.0, 3.2], align: ['l', 'l', 'r', 'l', 'l', 'l'], size: 13, rows: D.map(r => [r.instrument, r.issue_date.slice(0, 22), r.principal + ' ' + r.currency, r.coupon.slice(0, 30), r.maturity.slice(0, 22), (r.status + '; ' + r.key_terms).slice(0, 170) + ' ' + mk(r.source)]), source: 'Source: Elis URD 2025 and H1 2026 report via ProntoNLP (worker C, model/C_debt_instruments.csv). Note: sources disagree on which 2026 bond was refinanced early (€350m Feb-2026 per the FY2025 call vs "€600m" in the SR).' },
  { t: 'h2', text: 'Maturities, covenants, cost and liquidity' },
  { t: 'bullets', items: [
    '**Maturity profile** (bonds/USPP): 2027 €300m (4.125%, pre-funded by the March-2026 bond); 2028 €550m (1.625%); 2029 €300m USPP + $40m and the €380m OCEANE; 2030 €400m (3.75%); 2031 €350m (3.375%); 2032 €600m (3.875%) and USD USPP; 2035 USD USPP (5.21% EUR-swapped). Short-term: NEU CP (up to €600m), NEU MTN and a €200m receivables securitisation.',
    '**Covenant:** a single total-net-leverage covenant (<3.75x, tested half-yearly) on the RCF and USPP; headroom is ample at 2.09x [#6796](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6796).',
    '**Cost of debt:** the cheap 2019–21 bonds (1.6–2.7%) are being replaced at 3.4–3.9%; net financial expense rose from €88m (2020) to ~€131m (2025) and €73.9m in H1 2026 alone (+€9m YoY). Guided net interest paid ~€90m for 2026.',
    '**OCEANE 2029:** €380m, conversion ratio 6,256.86 shares per €100k (≈€15.98 per share; 23.8m shares). Soft call from 13-Oct-2026 if the share price exceeds 130% of the conversion price (~€20.8) [calc]; management intends to call and settle with treasury shares. If the stock stays below the trigger, the leverage target slips by ~0.2x [e] and the holder put on 22-Sep-2027 becomes relevant.',
    '**Ratings:** S&P BB+ → BBB- (Nov-2023); Moody\'s Ba1 → Baa3 (Nov-2024); Morningstar DBRS BBB. Keeping investment grade is an explicit policy constraint.',
    '**Liquidity:** €447m cash plus an undrawn €900m sustainability-linked RCF (€870m from Nov-2027 to Nov-2028) cover all maturities to 2028.',
  ] },
  { t: 'img', path: require('./util').IMG('hist_leverage.png'), widthIn: 6.2 },
];
