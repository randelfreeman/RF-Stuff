const fs = require('fs'); const path = require('path');
function parseCSV(text) {
  const rows = []; let row = [], field = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { field += '"'; i++; } else q = false; } else field += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(field); field = ''; }
    else if (c === '\n') { row.push(field); rows.push(row); row = []; field = ''; }
    else if (c === '\r') {}
    else field += c;
  }
  if (field.length || row.length) { row.push(field); rows.push(row); }
  return rows;
}
function readCSV(rel) {
  const p = path.join(__dirname, '..', '..', rel);
  const lines = fs.readFileSync(p, 'utf8').split('\n').filter(l => !l.startsWith('#')).join('\n');
  const rows = parseCSV(lines).filter(r => r.length > 1);
  const head = rows[0];
  return rows.slice(1).map(r => Object.fromEntries(head.map((h, i) => [h, r[i]])));
}
function readJSON(rel) { return JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', rel), 'utf8')); }
const f1 = (v, d = 1) => (v === null || v === undefined || v === '' || isNaN(+v)) ? 'n/a' : (+v).toLocaleString('en-GB', { minimumFractionDigits: d, maximumFractionDigits: d });
const pct = (v, d = 1, sign = false) => (v === null || v === undefined || v === '' || isNaN(+v)) ? 'n/a' : ((sign && +v > 0 ? '+' : '') + (+v).toFixed(d) + '%');
const IMG = (name) => path.join(__dirname, '..', '..', 'charts', name);
module.exports = { readCSV, readJSON, f1, pct, IMG };
