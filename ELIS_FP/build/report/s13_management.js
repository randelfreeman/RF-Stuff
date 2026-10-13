const { readCSV, IMG } = require('./util');
module.exports = [
  { t: 'h1', text: '13. Management assessment' },
  { t: 'p', text: 'Elis has a two-tier structure: a **Management Board** (executive) supervised by a **Supervisory Board**. The Management Board was renewed for four years from 5-Sep-2026: Xavier Martiré (Chairman/CEO), Louis Guyot (CFO) and, new, Yann Michel (Group COO); Matthieu Lecharny did not seek reappointment [#139](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264346860-139) [#140](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264346860-140) [#143](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264346860-143).' },
  { t: 'table', cols: ['Executive', 'Role / tenure', 'Track record', 'Skin in the game & pay'], widths: [1.4, 2.0, 3.4, 2.6], align: ['l', 'l', 'l', 'l'], size: 14, rows: [
    ['Xavier Martiré', 'Chairman of the Management Board (CEO) since 2008; at Elis since 1999 (~27 years); reappointed to 2030', 'Led the 2015 IPO, the Berendsen (2017), Lavebras, Indusal and Lavartex deals; tripled revenue from ~€1.5bn to €4.8bn; rebuilt UK and German margins; navigated Covid and the 2022 energy shock (unhedged); pivoted to capital returns in 2025. Ex-SNCF; Polytechnique/Ponts', 'Variable pay target 100% (cap 170%); LTI = 2.25x pay (121,741 performance shares granted 2025); say-on-pay 93.65% (2025) but only 70% support for the 2025 policy. **Sold 92,825 shares (~€2.3m) in Jan-2026** while the company was buying back [calc]. Holding not retrievable (<1% for all board members)'],
    ['Louis Guyot', 'CFO since 2013, Management Board since 2014; reappointed to 2030', 'Architect of the refinancing from BB to investment grade (BBB-/Baa3), the OCEANE, capital-allocation policy and buybacks. Ex-French Treasury, Dalkia, Korian', 'Target 100% (cap 170%); LTI 1.75x pay; repeated share and FCPE sales in 2025'],
    ['Yann Michel', 'Group COO from 1-Jul-2026; Management Board from Sep-2026; >15 years at Elis', 'Ran France, UK & Ireland as Deputy COO — the two regions with the strongest margin gains', 'Not disclosed'],
    ['Matthieu Lecharny (leaving end-2026)', 'Deputy COO Southern Europe & LatAm, head of M&A; Board 2014–2026', 'Built LatAm (Brazil, Mexico) and Southern Europe; LatAm margin reversal in 2025–26 and Mexico tender loss happened on his watch', 'Target 70% (cap 119%)'],
  ], source: 'Source: Elis FY2025 URD and H1 2026 report via ProntoNLP (worker B, model/B_management.json). Euro amounts of pay and individual holdings are in non-indexed tables and could not be retrieved.' },
  { t: 'h2', text: 'Capital allocation and returns under this management' },
  { t: 'img', path: IMG('hist_returns.png'), widthIn: 6.0 },
  { t: 'bullets', items: [
    '**ROE** rose from 3.9% (2021) to 9.9% (2025); **ROIC** (EBITA after tax / equity + net debt incl. leases) from 3.6% to 7.0% [calc] — improving but still around the cost of capital because ~€4bn of goodwill from Berendsen and LatAm sits in the base. Company pre-tax ROCE (excl. goodwill effects) is 14.7%.',
    '**Good:** disciplined bolt-ons (~1.2x sales, ~5x EBITDA); investment-grade rating; €616m of buybacks in 2025–26 at €22.87 and €26.25; energy hedging adopted after 2022.',
    '**Questionable:** Berendsen (2017) at a full price (equity ~£2.2bn) produced years of low returns; the 2024 US talks; buying back €467m at €26.25 just before the shares fell 19% (and funding it with debt while insiders sold).',
    '**Archetype:** professional, long-tenured insider managers, not founders. Strength: deep operational know-how and continuity; risk: little pressure to rethink the capital-intensive model, and succession now centres on an internal COO.',
  ] },
  { t: 'h3', text: 'Red flags reviewed' },
  { t: 'bullets', items: [
    'Related-party: the Aug-2025 EMTN mandate to HSBC Continental Europe, where the CEO sits on the board and chairs the compensation committee (approved under the related-party procedure) [#1303](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-1303). No other related-party transactions found.',
    'Pay: Supervisory Board chair fee more than doubled (€186k → €400k); only 70% approval of the 2025 Management Board pay policy [#1378](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-1378); 2020 variable-pay criteria changed retrospectively (Covid).',
    'Insider selling during the buyback (above). No loans to executives; severance within AFEP-MEDEF norms; auditors unchanged (PwC since 2007, Forvis Mazars since 2011).',
    'No frequent strategy pivots; the 2025 shift to shareholder returns is the only material change. Messaging is factual rather than promotional, although March-2026 guidance on LatAm margins was reversed within five months.',
  ] },
];
