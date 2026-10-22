const { readCSV } = require('./util');
const B = readCSV('model/B_board.csv'); const C = readCSV('model/B_board_changes.csv');
const t = (s, n) => { s = (s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n) + '…' : s; };
const mk = (s) => (s || '').match(/\[#[^\]]+\]\([^)]+\)/g)?.slice(0, 1).join('') || '';
const cur = B.filter(r => /current/.test(r.status_as_of_2026_10));
module.exports = [
  { t: 'h1', text: '14. Supervisory Board' },
  { t: 'table', cols: ['Member', 'Role', 'Independence', 'Since', 'Term to', 'Background and other affiliations'], widths: [1.7, 1.3, 1.3, 0.9, 1.1, 3.6], align: ['l', 'l', 'l', 'l', 'l', 'l'], size: 12, rows: cur.map(r => [t(r.name, 70), t(r.board_role, 45), t(r.independence, 45), t(r.first_appointed, 22), t(r.term_expiry, 26), t(r.main_activity_and_background, 230) + ' ' + mk(r.source)]), source: 'Source: Elis URD 2025 and H1 2026 report via ProntoNLP (worker B, model/B_board.csv).' },
  { t: 'h2', text: 'Changes over the last five years' },
  { t: 'table', cols: ['Date', 'Body', 'Who', 'Change'], widths: [1.1, 2.0, 3.0, 2.0], align: ['l', 'l', 'l', 'l'], size: 12, rows: C.filter(r => r[Object.keys(r)[0]] >= '2021').map(r => { const v = Object.values(r); return [v[0], t(v[1], 50), t(v[2], 90), t(v[3], 50) + ' ' + mk(r.source)]; }) },
  { t: 'p', text: '**Read-across:** the board has shifted from representatives of CPP Investments, Predica (Crédit Agricole) and Bpifrance to the Moreira Salles family (BWGI and BWSA hold two seats plus a censor), while CPPIB\'s last representative resigned in Feb-2026. Long tenures (Chair Thierry Morin since 2014, Philippe Delleur since 2015) are a governance watch-point; the 2025 additions (Isabelle Wege, CFO of Straumann; Kelly Becker of Schneider Electric) strengthened finance and international experience.' },
];
