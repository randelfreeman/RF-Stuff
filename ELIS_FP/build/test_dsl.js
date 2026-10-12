const { write } = require('./docx_dsl');
const blocks = [
 { t: 'h1', text: '1. Test heading' },
 { t: 'p', text: 'Body with **bold**, __italic__, a doc link [Elis SA, H1 2026 Earnings Call, Jul 29, 2026](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119) and a marker [#12](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119).' },
 { t: 'kpis', items: [{ v: '€4.80bn', l: 'FY2025 revenue (S&P, link unavailable)' }, { v: '34.1%', l: 'EBITDA margin [calc]' }, { v: '1.85x', l: 'ND/EBITDA ex leases' }] },
 { t: 'bullets', items: ['One **bold**', { text: 'Two', sub: ['Two-a'] }] },
 { t: 'table', title: 'Table 1', cols: ['EUR m', 'FY2024', 'FY2025'], rows: [['Revenue', '4,573.7', '4,796.8'], ['EBIT', '605.6', '613.9']], widths: [3, 1, 1], source: 'Source: S&P Capital IQ (source link unavailable).' },
 { t: 'callout', title: 'Callout', text: 'Something important.' },
];
write({ blocks, cover: null, headerText: 'Elis SA — test', footerText: 'test footer', title: 'Test' }, '/tmp/claude-0/-home-user-RF-Stuff/385d850d-c3a7-5449-be33-b904bd94defa/scratchpad/test.docx').then(p => console.log('wrote', p));
