const { sp } = require('./refs'); const { IMG } = require('./util');
module.exports = [
  { t: 'h1', text: '18. Dividends, buybacks and treasury shares (last five years)' },
  { t: 'table', cols: ['Fiscal year', 'DPS (€)', 'Paid (cash, €m)', 'Buyback (€m)', 'Shares bought', 'Avg price', 'Cancellations / treasury', 'Notes'], widths: [0.9, 0.7, 0.9, 0.9, 1.0, 0.8, 2.0, 2.3], align: ['l', 'r', 'r', 'r', 'r', 'r', 'l', 'l'], size: 13, rows: [
    ['FY2020', 'nil', '—', sp('Repurchase of Common Stock', 'FY2020', '1.3'), 'n/a', 'n/a', 'Liquidity contract only', 'FY2019 €0.39 dividend withdrawn (Covid)'],
    ['FY2021', sp('Dividend Per Share', 'FY2021', '0.37'), '—', '—', '—', '—', '—', 'Reinstated; scrip option (paid 2022)'],
    ['FY2022', sp('Dividend Per Share', 'FY2022', '0.41'), sp('Common Dividends Paid', 'FY2022', '33.2'), '0.1', '—', '—', '—', 'Scrip option; cash paid in year relates to FY2021'],
    ['FY2023', sp('Dividend Per Share', 'FY2023', '0.43'), sp('Common Dividends Paid', 'FY2023', '61.7'), '—', '—', '—', '—', 'Paid in cash 2024'],
    ['FY2024', sp('Dividend Per Share', 'FY2024', '0.45'), sp('Common Dividends Paid', 'FY2024', '101.3'), '2.2', '—', '—', '—', 'Paid 28-May-2025'],
    ['FY2025', sp('Dividend Per Share', 'FY2025', '0.48'), sp('Common Dividends Paid', 'FY2025', '105.1'), sp('Repurchase of Common Stock', 'FY2025', '153.8'), '6,560,820', '€22.87', '€109.1m of repurchased shares cancelled (shares 236.5m → 232.5m)', '€150m programme from 6-Mar-2025; €0.48 = €0.26 return of reserves + €0.22 dividend, paid 28-May-2026'],
    ['2026 YTD', '—', '105.6 (H1)', '466.8 (H1)', '~17.8m [calc]', '€26.25', '~16.9m treasury shares at 30-Jun-2026 (7.3%) [calc]; to settle OCEANE conversion', '€500m programme 6-Jan to 9-Jul-2026'],
  ], source: 'Source: S&P Capital IQ (linked) and Elis FY2025 results/URD and H1 2026 report via ProntoNLP ([#663](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-663) [#695](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-695) [#292](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-292) [#17](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-17)); worker B (model/B_shareholder_returns.csv).' },
  { t: 'img', path: IMG('hist_uses_of_cash.png'), widthIn: 6.2 },
  { t: 'p', text: 'Shareholder returns went from zero (2020–21) to ~€260m in 2025 and ~€570m in H1 2026 alone — 12% of today\'s market cap in eighteen months. The policy (bolt-ons €50–150m, leverage −0.1x a year, the rest to shareholders) implies ~€100–200m a year of buybacks from 2027 on our estimates.' },
];
