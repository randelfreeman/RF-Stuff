// Assemble the full report DOCX from section modules, then convert to PDF with LibreOffice.
const path = require('path'); const fs = require('fs');
const { write } = require('./docx_dsl');
const order = (process.env.SECTIONS || 's00_front,s01_layman,s02_catalysts,s03_business,s04_macro,s05_moat,s06_supply,s07_financials,s08_earnings,s09_eps,s10_capital,s11_valuation,s12_mna,s13_management,s14_board,s15_shareholders,s16_strategy,s17_stakes,s18_returns,s19_bullbear,s20_scenarios,s21_questions,s22_short,s23_timeline,s99_appendix').split(',');
const blocks = []; let cover = null;
for (const s of order) {
  const p = path.join(__dirname, 'report', s + '.js');
  if (!fs.existsSync(p)) { console.log('skip (missing)', s); continue; }
  const mod = require(p);
  if (s === 's00_front' && mod.cover) { cover = mod.cover; blocks.push(...mod.blocks); }
  else { if (blocks.length && mod[0] && mod[0].t === 'h1') mod[0] = { ...mod[0], pbb: true }; else if (blocks.length) blocks.push({ t: 'pagebreak' }); blocks.push(...mod); }
}
const out = process.env.OUT || path.join(__dirname, '..', 'Elis_ELIS_FP_Equity_Research_Report.docx');
write({ blocks, cover, title: 'Elis SA (ELIS FP) — Institutional Equity Research', headerText: 'Elis SA (ELIS FP) | Institutional equity research | 12 October 2026', footerText: 'For institutional investors. Data: S&P Capital IQ and ProntoNLP only. [calc] analyst calculation, [e] estimate, [u] unverified.' }, out).then(p => console.log('wrote', p));
