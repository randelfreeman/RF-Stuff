const { readCSV } = require('./util');
const S = readCSV('model/C_strategic_initiatives.csv'); const K = readCSV('model/C_stakes.csv');
const t = (s, n) => { s = (s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n) + '…' : s; };
const mk = (s) => (s || '').match(/\[#[^\]]+\]\([^)]+\)/g)?.slice(0, 1).join('') || '';
const verdict = { S01: 'Mixed', S02: 'Success', S03: 'Success', S04: 'Success, now volatile', S05: 'Done', S06: 'Success', S07: 'Success', S08: 'Success', S09: 'Ongoing', S10: 'On track', S11: 'Ongoing', S12: 'Behind on organic/EBIT', S13: 'Executed', S14: 'Success (small)', S15: 'Impaired; residual', S16: 'Not pursued / blocked' };
module.exports = [
  { t: 'h1', text: '16. Strategic initiatives over the last ten years' },
  { t: 'table', cols: ['Period', 'Initiative', 'Objective / targets', 'Outcome to date', 'Verdict'], widths: [0.9, 1.8, 2.4, 3.2, 1.0], align: ['l', 'l', 'l', 'l', 'l'], size: 12, rows: S.map(r => [r.period, t(r.initiative, 70), t(r.objective + '; ' + r.key_metrics_or_targets, 170), t(r.outcome_to_date, 220) + ' ' + mk(r.source), verdict[r.initiative_id] || '']), source: 'Source: Elis filings and calls via ProntoNLP (worker C, model/C_strategic_initiatives.csv); verdicts are the analyst\'s.' },
  { t: 'h1', text: '17. Stakes held in other companies' },
  { t: 'p', text: 'Elis holds **no material stakes in listed or unlisted companies** outside its consolidated subsidiaries: equity-accounted associates/JVs are immaterial (S&P long-term investments €0.2m), it bought out the remaining 50% of Casbu (Spain) in Jan-2024, and its other exposures are minority put options and earn-outs (Lavartex in Mexico, Acqua Flash in Brazil). Strategically and financially these are negligible; the relevant cross-holdings run the other way (BWSA, Invesco and CPPIB in Elis).' },
  { t: 'table', cols: ['Item', 'Entity', 'Detail', 'Relevance'], widths: [1.6, 1.8, 4.2, 1.6], align: ['l', 'l', 'l', 'l'], size: 12, rows: K.map(r => [t(r.category, 45), t(r.entity_or_holder, 45), t(r.detail, 230) + ' ' + mk(r.source), t(r.takeover_relevance, 60)]), source: 'Source: worker C (model/C_stakes.csv); S&P Capital IQ balance sheet.' },
];
