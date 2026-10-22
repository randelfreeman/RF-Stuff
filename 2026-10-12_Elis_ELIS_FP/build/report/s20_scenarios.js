const { IMG } = require('./util');
module.exports = [
  { t: 'h1', text: '20. Scenario analysis' },
  { t: 'table', cols: ['', 'Bear (25%)', 'Base (55%)', 'Bull (20%)'], widths: [2.2, 2.2, 2.2, 2.2], align: ['l', 'l', 'l', 'l'], size: 15, highlightRows: [6], rows: [
    ['Organic growth 2027E', '~2.0% (+0.5pt M&A)', '3.8% (+1pt M&A)', '~5.0% (+1pt M&A)'],
    ['Adj. EBIT margin 2027E', '15.4%', '16.2%', '16.5%'],
    ['Headline EPS 2027E', '€1.91', '€2.14', '€2.27'],
    ['OCEANE', 'Not converted; leverage >2x', 'Converted Q4-26; ~1.65x', 'Converted; buybacks €200m+ a year'],
    ['Multiple applied', '9.0x P/E (≈4.5x EBITDA)', '12.5x P/E / 5.5x EBITDA / 7% FCF yield', '14.5x P/E (≈6.3x EBITDA)'],
    ['Value per share', '€17.2', '€26.0', '€33.0'],
    ['Up/downside vs €21.26', '−19%', '+22%', '+55%'],
  ], source: 'Analyst estimates [e]; model/main_forecast.py. Probability-weighted value ≈ €25 (+18%). Takeover value (6.5–7.5x LTM adj. EBITDA) €30–38 (Section 12).' },
  { t: 'img', path: IMG('scenarios.png'), widthIn: 6.0 },
  { t: 'p', text: '**Asymmetry:** downside to the bear case (−19%) is smaller than upside to the base (+22%) and bull (+55%) cases; the bear case still assumes no dividend cut and investment-grade financing. Key swing factors: organic growth (±1pt ≈ ±€1.5/share), EBIT margin (±50bp ≈ ±€1.9/share) and the P/E multiple (±1x ≈ ±€2.1/share) [calc].' },
];
