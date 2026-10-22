module.exports = [
  { t: 'h1', text: '15. Shareholders, activism and short interest' },
  { t: 'p', text: 'Elis does not publish a full top-10 register in indexed text; the table below combines the last ownership table (30-Jun-2024), threshold declarations to the AMF through Jul-2026 and the Feb-2026 block trade [calc]. Share capital 232,848,588 shares; ~16.9m treasury shares at 30-Jun-2026 (7.3%) [calc].' },
  { t: 'table', cols: ['#', 'Holder', 'Type', 'Latest indication', 'Change'], widths: [0.4, 2.6, 1.6, 2.4, 2.4], align: ['c', 'l', 'l', 'l', 'l'], size: 14, rows: [
    ['1', 'BWSA / BWGI (Moreira Salles family, Brazil) via Kaon E and Kaon V funds', 'Strategic family holding; 2 SB seats', '≥18.3% of capital; ~20% of voting rights (above 20% since 18-Jun-2026)', 'Entered Oct-2023 (bought Predica stake); bought 7.0m shares from CPPIB at €25.00 on 6-Feb-2026; 25% standstill for 10 years'],
    ['2', 'Invesco Ltd', 'Institutional (asset manager)', '>10% of capital (16-Jul-2026)', 'Crossed 5% Nov-2025, 10% Jul-2026'],
    ['3', 'Treasury shares (Elis)', 'Company', '~16.9m (7.3%) at 30-Jun-2026', 'From the €500m 2026 buyback; earmarked for OCEANE conversion'],
    ['4', 'Wellington Management', 'Institutional', '~5% (around the threshold)', 'Crossed 5% up/down several times 2025–26'],
    ['5', 'CPP Investments', 'Pension fund', '<5% (21-Jul-2026)', 'Anchor since 2017 (Berendsen financing); 11.9% in 2025 → exit in progress'],
    ['6', 'Employees and executives (FCPE, direct, vested PS)', 'Insiders', '~3.0% of capital', 'Stable; board & management <1%'],
    ['7–10', 'Other institutions (e.g. Ameriprise, FMR in earlier registers)', 'Institutional', 'Below 5% — not disclosed', 'Bpifrance (Lac1) exited 2025'],
  ], source: 'Source: Elis URD 2024/2025, H1 2026 report and AMF declarations as reported via ProntoNLP (worker B, model/B_shareholders.csv) — e.g. [#6701](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6701) [#166](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-166) [#167](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-167). A complete top-10 list with percentages is not available in permitted sources.' },
  { t: 'h2', text: 'Activism' },
  { t: 'p', text: '**No activist campaign has been launched against Elis** in the period covered by permitted sources: searches of filings and transcripts for activist letters, shareholder proposals, contested resolutions and proxy fights returned nothing beyond the 70% vote on the 2025 executive pay policy. The closest thing to an "activist" is the strategic accumulation by BWSA/BWGI — a long-term family investor with board seats, not a campaign — and the company\'s own 2025 pivot to returning cash, which management framed around the "valuation disconnect" [#358](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-358).' },
  { t: 'h2', text: 'Short interest' },
  { t: 'p', text: '**Not available in S&P Capital IQ or ProntoNLP.** No disclosed net short positions or securities-lending data were found. Structurally, the OCEANE 2029 (€380m, 23.8m underlying shares) implies convertible-arbitrage short positions; these should unwind as the bond is called and converted. We recommend checking the AMF short-position register and lending data before sizing.' },
];
