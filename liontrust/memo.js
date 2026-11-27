const fs = require('fs');
const { P, H1, H2, B, SRC, img, table, doc, d, FONT } = require('./lib');
const { Paragraph, TextRun, Packer } = d;
const k = [];
k.push(new Paragraph({ style: 'Title', children: [new TextRun({ text: 'IC Memo — Liontrust Asset Management (LIO LN)', font: FONT })] }));
k.push(P('Date: 27-Nov-2026  |  Price 225.5p  |  Mkt cap £139.5m  |  EV ~£96m  |  AuMA £24.1bn (+£1.9bn Hawksmoor)  |  Strategy: event-driven / activist value'));
k.push(table(['Recommendation', 'Base value', 'Event value', 'Bear value', 'Prob.-weighted', 'Yield'], [
  ['ACCUMULATE / ENGAGE', '265p (+18%)', '380p (+68%)', '145p (−36%)', '~264p (+17%)', '~7–8% (FY27E)'],
], [24, 15, 15, 15, 16, 15]));
k.push(P('**Disclosure:** GAM special-situations funds hold ~5.01% and have publicly called for a sale (23-Mar-2026). This memo is prepared on that basis.', { run: { italics: true, size: 17 } }));

k.push(H2('1. Thesis in three lines'));
k.push(B('A debt-free UK active manager trading at **0.40% EV/AuMA, 3.3x EV/EBIT and 6.5x P/E** (consensus FY27E), with net cash ~31% of market cap — the cheapest name in the UK listed peer group and at the bottom of its own 5-year range (EV/EBITDA 3.1x vs ~6.5x average).'));
k.push(B('Organic decay is slowing (annualised net outflows ~8% of AuMA vs ~18–22% in FY24–26); bolt-ons bought at 0.3–0.5% of AuM lift AuMA to ~£26bn; dividend re-based and now ~2x covered.'));
k.push(B('**The value is most likely crystallised by a transaction.** Sector consolidation (Nuveen/Schroders £9.9bn; Jupiter/CCLA; PE take-privates) plus activist pressure and a consolidator (Martin Gilbert) on the board create a credible path to a sale at ~0.75% of AuMA (~380p).'));

k.push(H2('2. Key facts'));
k.push(table(['', 'FY24', 'FY25', 'FY26', 'H1 FY27', 'FY27E cons.', 'FY28E cons.'], [
  ['Revenue (£m)', '198.1', '169.9', '134.4', '63.0', '128.8', '140.8'],
  ['EBIT (£m)', '54.0', '34.0', '20.5', 'n.a.', '28.8', 'n.a.'],
  ['Adj. EPS (p)', 'n.a.', '56.8', '36.7', '14.5', '34.8', '41.4'],
  ['DPS (p)', '72', '72', '19', '7', '~17', '~21'],
  ['Net flows (£bn)', '(6.1)', '(4.9)', '(4.2)', '(0.8)', '—', '—'],
  ['Closing AuMA (£bn)', '27.8', '22.6', '19.6', '24.1', '—', '—'],
], [22, 13, 13, 13, 13, 13, 13]));
k.push(SRC('Source: FactSet Fundamentals & EstimatesConsensus; company results via StreetAccount/press. Our FY27E/FY28E/FY29E EPS: 30.2p / 38.3p / 38.2p (7–17% below consensus).'));

k.push(H2('3. Valuation'));
k.push(B('**Peers:** EV/Sales FY1 0.74x vs median 1.58x; EV/EBIT FY1 3.3x vs 5.1x; P/E FY1 6.5x vs 9.6x. Discount warranted by −21% revenue growth, but excessive.'));
k.push(B('**Regression** (10 UK managers, EBIT margin vs EV/Sales, R² 0.33): fitted EV/Sales 1.00x at Liontrust’s 22% margin → ~275p (+22%).'));
k.push(B('**Takeout:** 0.6–0.9% of AuMA / 5–8x EBITDA / 9–12x FY28E P/E → 315–485p; central ~360–380p. Precedents: River 0.3%, Hawksmoor 0.3–0.5%, CCLA ~0.7%, Schroders ~1.2% AuM / ~17x, Gresham House ~16x EBITDA.'));
k.push(img('charts/regression.png', 6.2, 3.45));

k.push(H2('4. Catalysts (next 12 months)'));
k.push(table(['Date', 'Catalyst'], [
  ['30-Nov-2026', 'Hawksmoor completion (+£1.9bn)'],
  ['20-Jan-2027', 'Q3 FY27 trading update — first quarter with River + Hawksmoor'],
  ['Apr-2027', 'Cash-ISA allowance cut (potential equity-fund flow tailwind); Q4 update 21-Apr'],
  ['23-Jun-2027', 'FY27 results — dividend, impairment review, FY28 outlook'],
  ['~Sep-2027', 'AGM — vote on pay/directors (15–19% dissent in 2026)'],
  ['Any time', 'Strategic review / inbound approach / merger with a UK peer; further sector M&A read-across'],
], [18, 82]));

k.push(H2('5. Key risks and mitigants'));
k.push(table(['Risk', 'Severity', 'Mitigant / monitor'], [
  ['Continued outflows; revenue margin falls toward 40–45bp', 'High', 'Quarterly flows; ±£1bn flows ≈ ±5p EPS'],
  ['Key-person loss (Economic Advantage, Sustainable teams)', 'High', 'LLP/retention structures; would also cut bid value'],
  ['Board resists sale; further dilutive/expensive M&A (River costs £10.3m > £7.6m price)', 'Medium–High', 'Activist engagement; AGM votes; shareholder coalition'],
  ['Intangible impairment (goodwill + intangibles = 87% of equity)', 'Medium', 'Non-cash; limited effect on value but on headlines'],
  ['Consensus too high (H2 FY27 needs ~20p vs 14.5p H1)', 'Medium', 'Our numbers already below consensus; price discounts a 20–30% miss'],
  ['Liquidity of position (retail register; ADV ~£0.5m)', 'Medium', 'Position sizing; block opportunities around events'],
], [44, 14, 42]));

k.push(H2('6. Pre-mortem and what would change our mind'));
k.push(P('We lose money if outflows re-accelerate (>£2bn p.a.), a core team departs and the board continues to acquire rather than sell — leaving a shrinking franchise at 5x P/E (~145p). We would **exit** on (i) a key-team departure, (ii) a share-funded acquisition at or near current prices, or (iii) evidence of no buyer interest after a formal process. We would **add** on (i) two consecutive quarters of positive gross-to-net flow progression, (ii) the board engaging advisers / launching a review, or (iii) further de-rating without fundamental deterioration.'));

k.push(H2('7. Proposed action'));
k.push(B('Maintain/accumulate the position toward a target weight consistent with liquidity (event-driven bucket); target price 265p base / 380p event; stop-review at 175p.'));
k.push(B('Continue engagement: request board meeting on (a) formal strategic review with independent advisers, (b) a hurdle rate for M&A and preference for buybacks at <8x P/E, (c) TSR/sale-value-linked LTIP, (d) CEO/CFO succession.'));
k.push(B('Build a shareholder coalition with long-only holders (UBS AM, Slater, Merseyside PF, Norges) and platform-held retail ahead of the 2027 AGM.'));
k.push(P('Full analysis, data audit links and limitations: see accompanying report “Liontrust_LIO_Equity_Research_Nov2026.docx”.', { run: { italics: true, size: 17 } }));

Packer.toBuffer(doc(k, 'IC Memo — Liontrust Asset Management (LIO LN) — 27 Nov 2026')).then(b => { fs.writeFileSync('Liontrust_LIO_IC_Memo_Nov2026.docx', b); console.log('memo written'); });
