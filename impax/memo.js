const fs = require('fs');
const { P, H2, B, SRC, img, table, doc, d, FONT } = require('./lib');
const { Paragraph, TextRun, Packer } = d;
const k = [];
k.push(new Paragraph({ style: 'Title', children: [new TextRun({ text: 'IC Memo — Impax Asset Management (IPX LN)', font: FONT })] }));
k.push(P('Date: 27-Nov-2026  |  Price 89.3p  |  Mkt cap £108.5m  |  Net cash ~£62m  |  TEV ~£46m  |  AUM £20.05bn  |  Strategy: event-driven / deep value  |  TEV = total enterprise value = market cap + net debt (or − net cash). '));
k.push(table(['Recommendation', 'Base value', 'Strategic value', 'Bear value', 'Prob.-weighted', 'Yield'], [
  ['ACCUMULATE / ENGAGE', '~110p (+23%)', '~165p (+85%)', '~70p (−22%)', '~112p (+25%)', '7.5% (FY26 DPS 6.7p)'],
], [22, 15, 16, 15, 16, 16]));
k.push(P('**Disclosure:** GAM special-situations funds hold ~2.2% (Jul-2026).', { run: { italics: true, size: 17 } }));
k.push(H2('1. Thesis'));
k.push(B('**Cash covers 57% of the price.** Net cash ~£62m (51p/share); the operating franchise — the global leader in transition investing with £20bn AUM — is valued at ~£46m (0.23% of AUM, ~3x FY27E EBIT). Cheapest UK listed manager on TEV/AUM.'));
k.push(B('**Trough confirmed.** FY26 beat (adj. EPS 12.2p vs 11.0p consensus); costs reset to a £86.5m run-rate; FY27 revenue guided £100–103m (above £98.7m consensus); outflows “slowed considerably” in Q1 FY27; 2026 investment performance strong.'));
k.push(B('**Operating leverage + optionality.** ~80% incremental margin; 30% margin target at £27–28bn AUM. Concentrated register (BNPP 14.4%, Liontrust funds 10.7%, management ~18%, EBT 5.1%) makes a negotiated outcome executable; BNPP is the natural buyer.'));
k.push(H2('2. Key numbers'));
k.push(table(['', 'FY24', 'FY25', 'FY26', 'FY27E cons.', 'FY28E cons.'], [
  ['Revenue (£m)', '173.4', '144.7', '114.8 (co. 113.1)', '98.7 (guide 100–103)', 'n.a.'],
  ['EBIT (£m)', '54.0', '33.4', '15.5 (adj. 16.6)', '13.9', 'n.a.'],
  ['Adj. EPS (p)', '28.8', '18.0', '12.2', '9.6', '12.3'],
  ['DPS (p)', '27.6', '12.0', '6.7', '~5', '~7'],
  ['Net flows (£bn)', 'neg.', '(13.0)', '(7.8)', '—', '—'],
  ['Closing AUM (£bn)', '37.2', '26.1', '20.05', '—', '—'],
], [20, 13, 13, 18, 20, 16]));
k.push(H2('3. Valuation and regressions'));
k.push(B('**TEV/AUM vs E/AUM** (R² 0.69, ex-Ashmore; sector ≈ 5x EBIT): fitted 0.36% vs 0.23% actual → ~110p. At a 30% margin the same line implies ~170p.'));
k.push(B('**PBR vs ROE** (linear R² 0.94; log 0.73): fair at ~87–97p — ROE is diluted by cash. **TEV/Sales vs EBIT margin** (R² 0.34): market ascribes ~zero value to operations at the current 14% margin — upside is the margin recovery.'));
k.push(B('**Takeout:** 0.5–0.9% of AUM / 6–8x FY28E EBITDA → 135–200p; central ~160–165p.'));
k.push(img('charts/reg_evaum.png', 6.2, 3.45));
k.push(H2('4. Catalysts'));
k.push(table(['Date', 'Catalyst'], [
  ['Jan-2027', 'Q1 FY27 AUM/flows — confirmation of slower outflows'],
  ['Feb/Mar-2027', 'AGM; 4.7p final dividend (ex ~18-Feb-2027)'],
  ['H1 2027', 'Strategic-partnership announcements (8–10 under discussion)'],
  ['~27-May-2027', 'H1 FY27 results — margin recovery vs £100–103m revenue guide'],
  ['Any time', 'BNPP strategic decision on 14.4% stake post AXA IM; inbound approach; capital return'],
], [18, 82]));
k.push(H2('5. Risks'));
k.push(table(['Risk', 'Severity', 'Monitor / mitigant'], [
  ['Renewed outflows (ESG/US politics)', 'High', 'Quarterly flows; cash floor ~51p/share'],
  ['BNPP channel loss (~32% of revenue via Lux/France)', 'High', 'BNPP AUM in quarterly breakdown'],
  ['Founder resists any sale; cash spent on M&A', 'Medium–High', 'Engagement; capital-return policy'],
  ['Key-person (Simm, Jenkyn-Jones)', 'Medium', 'Succession disclosure'],
  ['Liquidity (AIM; ADV ~£0.4m)', 'Medium', 'Position sizing; block trades'],
], [44, 14, 42]));
k.push(H2('6. Proposed action'));
k.push(B('Accumulate within liquidity limits; target 110p base / 165p strategic; review below 70p (cash-plus-minimal value).'));
k.push(B('Engage with the board on: (a) return of surplus cash above the regulatory buffer (~£30–35m, ~25–30p/share); (b) clarity on BNPP’s intentions and conflict management; (c) a formal process if strategic interest emerges; (d) TSR-linked incentives.'));
k.push(B('Coordinate with the Liontrust position: Liontrust funds own 10.7% of Impax — a UK combination or BNPP-led outcome are both plausible routes to value.'));
k.push(P('Full analysis, data audit and limitations: “Impax_IPX_Equity_Research_Nov2026.docx”.', { run: { italics: true, size: 17 } }));
Packer.toBuffer(doc(k, 'IC Memo — Impax Asset Management (IPX LN) — 27 Nov 2026')).then(b => { fs.writeFileSync('Impax_IPX_IC_Memo_Nov2026.docx', b); console.log('memo written'); });
