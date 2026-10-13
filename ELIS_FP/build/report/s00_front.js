const { IMG } = require('./util');
const { sp, DOC } = require('./refs');
const fs = require('fs'); const path = require('path');
// Static contents table: page numbers come from a first-pass PDF (build/toc_pages.json, written by make_toc.py).
const TOC_F = path.join(__dirname, '..', 'toc_pages.json');
const TOC = fs.existsSync(TOC_F) ? JSON.parse(fs.readFileSync(TOC_F, 'utf8')) : [];
const tocBlock = { t: 'table', title: 'Contents', cols: ['Section', 'Page'], widths: [8, 1], size: 17, rows: TOC.map(r => [r.h, String(r.page)]) };
const cover = [
  { t: 'p', text: ' ', after: 1400 },
  { t: 'p', text: 'INSTITUTIONAL EQUITY RESEARCH  |  EVENT-DRIVEN / SPECIAL SITUATIONS', size: 18, color: '2A78D6', bold: true },
  { t: 'p', text: 'Elis SA (ELIS FP)', size: 64, bold: true, color: '13213F', after: 60, before: 120, line: 780 },
  { t: 'p', text: 'Euronext Paris: ELIS  ·  Textile, hygiene and facility services  ·  12 October 2026', size: 22, color: '52514E', after: 300, line: 300 },
  { t: 'p', text: 'A capital-intensive compounder priced as a value trap: 11x headline earnings, 8% FCF yield and a ~20% Brazilian family holder, with the OCEANE soft call and Q3 revenue as near-term tests', size: 26, color: '13213F', after: 360, line: 340 },
  { t: 'kpis', items: [{ v: 'BUY', l: 'Recommendation (event-driven, medium conviction)' }, { v: '€26', l: '12-month target price (+22%); probability-weighted €25' }, { v: '€21.26', l: 'Reference price, close 9-Oct-2026' }, { v: '€4.6bn', l: 'Market cap (215.9m shares); EV €9.0bn incl. leases' }] },
  { t: 'kpis', items: [{ v: '5.2x', l: 'EV / LTM adjusted EBITDA [calc]' }, { v: '11.3x', l: 'P/E on LTM headline diluted EPS [calc]' }, { v: '2.09x', l: 'Leverage at 30-Jun-2026 (covenant 3.75x)' }, { v: '−25%', l: 'From the 3-Jul-2026 high of €28.20' }] },
  { t: 'p', text: ' ', after: 600 },
  { t: 'p', text: 'Data sources: S&P Global (Capital IQ via the S&P Deterministic Retrieval connector) and ProntoNLP (S&P transcripts, Elis filings, prices, sentiment) only. No web sources. Figures are hyperlinked to their source documents where the connector returned a link; otherwise flagged "S&P, link n/a". [calc] = analyst calculation; [e] = estimate; [u] = unverified. A separate data-provenance document lists every connector call and the raw data.', size: 15, color: '898781' },
  { t: 'pagebreak' },
];
const blocks = [
  tocBlock,
  { t: 'pagebreak' },
  { t: 'h1', text: 'Investment summary' },
  { t: 'p', text: '**Recommendation: BUY, 12-month target €26 (+22%); event-driven, medium conviction.** Elis is Europe\'s leading textile-rental and hygiene-services company: €4.8bn of revenue, an adjusted EBITDA margin of 35.4% and ~87% of revenue from recurring product-as-a-service contracts. After a 25% fall from the July high the shares trade at 5.2x LTM adjusted EBITDA, 11.3x LTM headline EPS and an ~8% FCF yield on equity — the low end of their five-year range and a fraction of US peers (Cintas 26.6x S&P EBITDA). The H1 2026 result disappointed on quality (flat margins, negative H1 free cash flow, Mexico tender loss, leverage 2.09x) but guidance was confirmed, and our base case puts FY2026E headline EPS only ~2% below the guided mid-point.' },
  { t: 'h3', text: 'Why now — four things converge' },
  { t: 'bullets', items: [
    '**De-rating already done.** The stock is −24.6% from the 3-Jul-2026 high and −18.4% since results day; sentiment on the H1 call ([0.52](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_Scores_$KEY_Sentiment)) is the lowest since 2020, yet the strategic-position aspect barely moved.',
    '**Capital returns at scale.** €466.8m of shares (7.6% of capital) were bought back at €26.25 in H1 2026 [#292](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-292); the policy returns all cash beyond €50–150m of bolt-ons and 0.1x a year of deleveraging [#493](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-493).',
    '**OCEANE 2029 soft call (from 13-Oct-2026).** Conversion of the €380m convertible into treasury shares would cut net debt by ~€362m at no cash cost and take leverage towards ~1.65x [#517](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-517); the trigger (~€20.8 [calc]) is only ~2% below the price, so the convertible holder base is a natural buyer of weakness.',
    '**A ~20% strategic holder.** The Moreira Salles family (BWSA/BWGI) bought CPP Investments\' block at €25.00 in Feb-2026 and sits on the Supervisory Board with a 25% standstill [#6728](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6728); its entry price is 18% above today\'s.',
  ] },
  { t: 'h3', text: 'What has to go right' },
  { t: 'bullets', items: [
    'Q3 2026 revenue (28-Oct) shows the H2 organic acceleration management promised from record signings, despite Mexico (~€14m 2026 headwind).',
    'Energy and minimum-wage pass-through restores margin expansion in 2027 ("super nice price increase" from end-2026 indices [#472](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-472)).',
    'The OCEANE converts and FY2026 free cash flow grows mid-single-digit (H2 needs ~€390m+ after the −€30m H1).',
    'Capital allocation stays disciplined: no large US deal (the 2024 talks cost 21% in four days).',
  ] },
  { t: 'table', title: 'Key financials and estimates (EUR m)', cols: ['', 'FY2023', 'FY2024', 'FY2025', 'FY2026E', 'FY2027E', 'FY2028E'], widths: [2.2, 1, 1, 1, 1, 1, 1], size: 15, highlightRows: [5], rows: [
    ['Revenue', sp('Total Revenues', 'FY2023', '4,309.4'), sp('Total Revenues', 'FY2024', '4,573.7'), sp('Total Revenues', 'FY2025', '4,796.8'), '5,002', '5,242', '5,504'],
    ['Organic growth', '11.8%', '5.2%', '3.8%', '~3.3%', '3.8%', '4.0%'],
    ['Adj. EBITDA (company)', '1,474.8', '1,609.8', '1,700.1', '1,773', '1,866', '1,968'],
    ['Adj. EBITDA margin', '34.2%', '35.2%', '35.4%', '35.4%', '35.6%', '35.8%'],
    ['Adj. EBIT (company)', 'n/a', '733', '766.6', '798', '849', '903'],
    ['Headline diluted EPS (€)', 'n/a', '1.76', '1.85', '1.96', '2.14', '2.34'],
    ['IFRS diluted EPS (€)', sp('Net EPS - Diluted', 'FY2023', '1.06'), sp('Net EPS - Diluted', 'FY2024', '1.34'), sp('Net EPS - Diluted', 'FY2025', '1.46'), '1.58', '1.77', '1.97'],
    ['DPS (€)', sp('Dividend Per Share', 'FY2023', '0.43'), sp('Dividend Per Share', 'FY2024', '0.45'), sp('Dividend Per Share', 'FY2025', '0.48'), '0.51', '0.55', '0.60'],
    ['FCF after leases (company)', 'n/a', '346.3', '358.6', '~375', '~405', '~440'],
    ['P/E headline at €21.26', '', '', '11.5x', '10.8x', '9.9x', '9.1x'],
  ], source: 'Actuals: Elis via S&P Capital IQ (linked) and company releases via ProntoNLP (Sections 7–8); FY2024 adj. EBIT and headline EPS derived from reported growth rates [calc]. Estimates: analyst [e] (Section 9).' },
  { t: 'h3', text: 'Valuation and risks in one paragraph' },
  { t: 'p', text: 'Our €26 target blends 12.5x FY2027E headline EPS (€26.8), 5.5x FY2027E adjusted EBITDA (€27.2, post-OCEANE share count) and a 7% FCF yield (€23.4). Bear case €17 (25% probability: organic growth ~2.5%, margins −50bp, 9x P/E); bull case €33 (20%: 6% growth, 14.5x P/E); takeover value €30–38 at 6.5–7.5x EBITDA. The key risks are (1) a structural slowdown in organic growth below 3% as pricing normalises, (2) labour-cost inflation outrunning indexation, (3) a large leveraging acquisition, and (4) refinancing costs; the bear case is that Elis is a 7%-ROIC business whose cheapness is deserved (Sections 19 and 22).' },
  { t: 'img', path: IMG('price_catalysts.png'), widthIn: 6.4 },
];
module.exports = { cover, blocks };
