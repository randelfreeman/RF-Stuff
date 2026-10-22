const { readCSV } = require('./util');
const TL = readCSV('model/D_timeline.csv');
const CAL = readCSV('model/D_catalyst_calendar.csv');
const mk = (s) => (s || '').match(/\[[^\]]+\]\(https?:[^)]+\)/g)?.slice(0, 2).join(' ') || '';
const trim = (s, n) => { s = (s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n) + '…' : s; };
const imp = (r) => /results \(Elis\)|OCEANE|capital markets \(Elis\)|sector M&A|M&A \(Elis\)/.test(r.type + ' ' + r.event) ? 'High' : (/peer|regulatory|macro|accounting/.test(r.type) ? 'Medium' : 'Medium');
module.exports = [
  { t: 'h1', text: '23. Timeline of key events and catalyst calendar' },
  { t: 'h2', text: '23.1 Key past events (2015 to today)' },
  { t: 'table', cols: ['Date', 'Event', 'Category', 'Source'], widths: [1.3, 5.2, 1.5, 1.6], align: ['l', 'l', 'l', 'l'], size: 13,
    rows: TL.map(r => [r.date, trim(r.event, 230), r.category, mk(r.source)]), source: 'Source: Elis filings and transcripts via ProntoNLP; price moves from ProntoNLP prices [calc] (model/D_timeline.csv).' },
  { t: 'h2', text: '23.2 Upcoming catalysts (12-Oct-2026 to end-2027)' },
  { t: 'p', text: 'Dates marked [e] are estimates from prior-year patterns; [u] = not verified in permitted sources. The most actionable near-term items are the **OCEANE 2029 soft call** (exercisable from 13-Oct-2026), **Q3 2026 revenue on 28-Oct-2026**, the end-2026 **price/index negotiations** and the **FY2026 results in early March 2027** (2027 guidance, dividend, next buyback).' },
  { t: 'table', cols: ['When', 'Event', 'Why it matters', 'Impact'], widths: [1.5, 3.2, 4.2, 0.8], align: ['l', 'l', 'l', 'c'], size: 13,
    rows: CAL.map(r => [r.date_or_window, trim(r.event, 170), trim(r.why_it_matters, 230) + (mk(r.source) ? ' ' + mk(r.source) : ''), imp(r)]), source: 'Source: worker D catalyst calendar (model/D_catalyst_calendar.csv), ProntoNLP upcoming-event listings and Elis filings.' },
];
