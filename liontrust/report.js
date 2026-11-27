const fs = require('fs');
const { P, H1, H2, H3, B, N, SRC, BR, img, table, SP, doc, d, FONT, NAVY, TableOfContents } = require('./lib');
const { Paragraph, TextRun, AlignmentType, Packer } = d;
const C = 'charts/';
const peers = JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-RF-Stuff/0d9de77d-b330-5dee-8336-04e1e971011c/scratchpad/peer_rows.json'));
const f1 = (x) => (x === null || x === undefined) ? 'n.m.' : x.toFixed(1);
const f2 = (x) => (x === null || x === undefined) ? 'n.m.' : x.toFixed(2);
const fx = (x) => (x === null || x === undefined || x < 0) ? 'n.m.' : x.toFixed(1) + 'x';

const k = [];
// ---------------- COVER ----------------
k.push(new Paragraph({ style: 'Title', children: [new TextRun({ text: 'Liontrust Asset Management PLC (LIO LN)', font: FONT })] }));
k.push(P('**Institutional equity research — deep dive, special-situations lens**', { run: { size: 24, color: '2E5597' } }));
k.push(P('Report date: 27 November 2026  |  Price: 225.5p (close 26-Nov-2026)  |  Sector: UK traditional active asset management'));
k.push(table(['Market data', 'Value', 'Valuation (FactSet consensus)', 'Value'], [
  ['Share price / 52-wk range', '225.5p / 225.5p–351p', 'P/E FY27E (Mar-27) / FY28E', '6.5x / 5.4x'],
  ['Market cap (FactSet)', '£139.5m', 'EV / EBIT FY27E', '3.3x'],
  ['Net cash (Mar-26, pro forma Hawksmoor)', '~£44m', 'EV / Sales FY27E', '0.74x'],
  ['Enterprise value', '~£96m', 'Mkt cap / AuMA (EV / AuMA)', '0.58% (0.40%)'],
  ['AuMA (30-Sep-26) + Hawksmoor', '£24.1bn + ~£1.9bn', 'Dividend yield (FY27E, 50% payout)', '~7.7%'],
  ['Shares (approx.)', '~61.9m', 'Consensus target / ratings', '386p mean (190–550p); 6 Buy, 2 Sell'],
  ['Peak-to-current (Dec-21 → now)', '2,325p → 225.5p (−90%)', 'FY27E consensus EPS (8 est.)', '34.8p (all 8 revised down)'],
], [26, 18, 30, 26]));
k.push(SRC('Source: FactSet Global Prices, Fundamentals, EstimatesConsensus (accessed 27-Nov-2026); company RNS via press. Net cash = FY26 cash £52.7m less £6.0m Hawksmoor cash consideration, plus £2.7m lease debt; H1 FY27 balance sheet not retrieved (see Audit & Limitations).'));

k.push(H2('Investment summary (one page)'));
k.push(P('**View: deep value with an event path — Accumulate / engage for a strategic outcome. Base value 265p (+18%); event (sale) value ~380p (+68%); bear 145p (−36%). Probability-weighted ~264p (+17%), plus ~7–8% dividend yield.**'));
k.push(B('**What it is:** a UK-centric, retail-distributed active fund manager (AuMA £24.1bn) whose revenue is AuMA × ~50bp. It has suffered five consecutive years of net outflows (c.£20bn cumulative since FY23), a 90% share-price collapse and a 74% dividend cut.'));
k.push(B('**Why it is cheap:** at 0.40% EV/AuMA, 3.3x EV/EBIT and 6.5x P/E it trades at the bottom of the UK peer group and below its own regression-implied value (1.0x EV/Sales for a 22% EBIT margin vs 0.74x actual). Cash is ~31% of market cap and there is no financial debt.'));
k.push(B('**Why it is cheap for a reason:** flows remain negative (H1 FY27 −£0.8bn), the revenue margin is compressing (60bp → 50bp in 18 months), H1 FY27 produced a statutory loss (−£4.2m) and adjusted EPS fell 22%; consensus still embeds a sharp H2 recovery (FY27E 34.8p vs H1 14.5p).'));
k.push(B('**The event:** GAM special-situations funds (5.01%) have publicly called (23-Mar-2026) for a strategic review and sale. Sector consolidation is accelerating (Nuveen/Schroders £9.9bn, Jupiter/CCLA, Liontrust’s own River Global and Hawksmoor bolt-ons). Martin Gilbert, the UK’s best-known asset-management consolidator, joined the board on 1-Jul-2026. A buyer stripping 35–45% of a ~£94m cost base would double earnings.'));
k.push(B('**Key risks:** structural active-to-passive shift; UK retail/ESG concentration; key-person risk; management entrenchment (CEO since 2010, CFO since 1995); value-destructive M&A (Majedie impairment; River costs > consideration).'));
k.push(P('**Disclosure:** funds managed by GAM Investments’ special-situations team are shareholders in Liontrust (~5.01% per RNS, 10-Jul-2026) and have publicly advocated a sale. Readers should weigh this report accordingly; all data are sourced and limitations are listed in Section 23.', { run: { italics: true, size: 17 } }));

k.push(H2('Layman’s guide: what Liontrust does and how it makes money'));
k.push(P('Liontrust is a “fund manager”. Savers — mostly ordinary UK investors buying through platforms such as Hargreaves Lansdown or via their financial adviser — hand money to Liontrust’s investment teams, who pick shares and bonds on their behalf in pooled funds (unit trusts/OEICs), investment trusts, model portfolios and segregated accounts for pension funds.'));
k.push(P('Liontrust charges an annual fee that is a percentage of the money it manages — on average about **0.50% a year** (i.e. £5 for every £1,000). So revenue rises and falls with (1) how much money clients give or withdraw (**net flows**), (2) how markets perform, and (3) the average fee rate (**revenue margin**). Costs are mostly people (fund managers, sales, operations) and are largely fixed in the short term, so profits swing much more than revenue: this is “operating leverage”.'));
k.push(P('Liontrust reports one business segment. Its “divisions” are its investment teams, each with its own process. They contribute roughly in proportion to their assets and fee rates:'));
k.push(table(['Team / process', 'What it does', 'Approx. role in earnings'], [
  ['Economic Advantage (UK equities)', 'UK small/mid-cap “intangible strengths” growth funds (e.g., UK Smaller Companies, Special Situations)', 'Historic profit engine; high fee; in outflow with UK small caps'],
  ['Sustainable Investment', 'Sustainable Future equity, bond and managed funds', 'Was the growth engine 2017–21; £5.3bn (Mar-26) / £5.8bn (Jun-26), down >50% from peak'],
  ['Global Fundamental (ex-Majedie)', 'UK and global value/contrarian equity', 'Acquired 2022; heavy outflows; intangibles impaired'],
  ['Cashflow Solution', 'Systematic cash-flow based European/global equity', 'Mid-sized; mixed flows'],
  ['Global Equity / Innovation', 'Global growth & thematic equity', 'Small-mid; performance-dependent'],
  ['Global Fixed Income', 'Credit and high-yield, sustainable bonds', 'Lower fee; institutional pipeline'],
  ['Multi-Asset (incl. MPS)', 'Fund-of-funds and model portfolio services', '£3.9bn (Dec-25); flows turned slightly positive; Hawksmoor (+£1.9bn) adds scale'],
  ['River Global (from 1-Jul-2026)', 'UK/global value and income, European equities', '+£3.0bn AuMA; broadens style mix'],
], [26, 44, 30]));
k.push(SRC('Source: Liontrust trading statements and results (via press/StreetAccount); FactSet. Team-level revenue/profit is not disclosed by the company.'));

k.push(H2('Contents'));
k.push(P('1. Stock price history & catalysts · 2. Business model · 3. Macro influences · 4. Competitive position & moats · 5. Supply chain map · 6. KPIs & segment metrics · 7. Recent earnings & sentiment · 8. Forward EPS projections · 9. Capital structure · 10. Valuation, peers & regression · 11. M&A · 12. Management · 13. Board of Directors · 14. Shareholders, activism & short interest · 15. Strategic initiatives · 16. Stakes held · 17. Dividends & buybacks · 18. Bull vs bear · 19. Scenario analysis · 20. Management questions · 21. Devil’s advocate / red flags · 22. Timeline & catalysts · 23. Audit trail & limitations', { run: { size: 17 } }));
k.push(BR());

// ---------------- 1 STOCK PRICE ----------------
k.push(H1('1. Stock price history and catalysts (5 years)'));
k.push(img(C + 'price.png', 7.0, 3.3));
k.push(P('The shares have fallen ~90% from the 2,325p peak (3-Dec-2021). The de-rating had three phases: (i) 2022 — rates shock and the collapse of the ESG/growth style that had powered Sustainable Investment flows; (ii) 2023–24 — persistent UK-retail outflows, the failed GAM bid and the Majedie write-down; (iii) 2025–26 — earnings resets, a new payout policy and the 74% dividend cut, partly offset by M&A and activist-driven rallies. Moves of more than 10% (single day or 5-day) are listed below; marker numbers match the chart.'));
k.push(table(['#', 'Date', 'Move', 'Catalyst'], [
  ['1', '1–3 Dec 2021', '+12.5% (1 day); peak 2,325p', 'H1 FY22 results: record AuMA (~£36bn), strong Sustainable flows'],
  ['2', '17–24 Jan 2022', '−19% (5 days)', 'Q3 FY22 trading update, Majedie deal (up to £120m) and violent growth/ESG rotation as rate expectations rose'],
  ['3', '1–9 Mar 2022', '−24% (5d), then +11% (1d)', 'Russia/Ukraine sell-off and rebound'],
  ['–', 'Jun–Sep 2022', '−8.5% (ex-div 30 Jun); −13% (5d to 29 Sep)', '50p ex-dividend; UK gilt/LDI crisis after the mini-budget'],
  ['4', '4 Oct–14 Nov 2022', '+21% (5d), +31% (5d to 11 Nov)', 'Gilt stabilisation; US CPI relief rally; H1 FY23 results (18 Nov)'],
  ['5', '19–24 Apr 2023', '−14% (5 days)', 'Q4 FY23 trading update: heavy net outflows (FY23 −£4.8bn)'],
  ['6', '4 May / 24–29 Aug 2023', '−7% then +13% (5d)', 'All-share offer for GAM Holding announced; offer declared unsuccessful (33.45% acceptance vs 66.7% needed) — relief rally'],
  ['–', '14–20 Dec 2023', '+17.5% (5 days)', 'Rate-pivot rally in UK SMID/asset managers'],
  ['–', '17–24 May 2024', '+14% (5 days)', 'Market rally; sector rebound into FY24 results'],
  ['7', '4 Jul 2024', '−15% (5d)', 'FY24 results aftermath and 50p ex-dividend (≈7.7% of price)'],
  ['–', 'Jan 2025', '−13% (5 days)', 'Q3 FY25 outflows; UK gilt-yield spike'],
  ['8', '3–9 Apr 2025', '−17% (5 days)', 'US “Liberation Day” tariff shock'],
  ['9', '25 Jun 2025', '−13% (1 day)', 'FY25 results: adj. EPS 56.8p vs 59.3p consensus (−4%); revenue £157.7m vs £162.2m; new policy of ≥50% payout implying a large dividend cut'],
  ['–', 'Nov 2025', '−15% (month)', 'H1 FY26: adj. EPS 18.7p (beat 3%) but interim dividend cut to 7p (from 22p); £10m buyback'],
  ['10', '16–23 Mar 2026', '+6% (16 Mar), muted', 'River Global acquisition announced; GAM open letter calling for sale (23 Mar)'],
  ['11', '24–30 Jun 2026', '+12.6% (1d), +19% (5d)', 'FY26 results: outflows easing, dividend cut to 19p well-flagged, River completion; GAM crosses 5% (10 Jul)'],
  ['12', '22–28 Jul 2026', '−15% (5 days)', 'Q1 FY27 trading update: £357m outflows; 12p ex-dividend (2 Jul) preceding'],
  ['13', '30 Sep 2026', '+18.2% (1 day, 3x volume)', 'Hawksmoor fund management & MPS acquisition (£6m + up to £4m; £1.9bn), earnings-enhancing from year 1; director buying reported'],
  ['14', '19–20 Nov 2026', '−6% then −11% (−16% over 2 days)', 'H1 FY27: statutory pre-tax loss £4.2m; adj. EPS 14.5p (−22%); revenue margin 50bp; £16.1m non-recurring costs'],
], [4, 15, 20, 61]));
k.push(SRC('Source: FactSet daily prices (computed moves); StreetAccount/FactSet news; press (AJ Bell, City AM, Sharecast, Shares Magazine, MarketBeat). Ex-dividend effects flagged; not all moves are fundamental.'));
k.push(P('**Read-across:** the stock reacts most violently to (a) flow prints, (b) dividend news and (c) corporate activity. The only sustained positive catalysts in five years were M&A/corporate events (GAM bid failure relief, River, Hawksmoor, activist involvement) — consistent with the market pricing Liontrust as a run-off franchise whose value is most likely to be crystallised by a transaction.'));

// ---------------- 2 BUSINESS MODEL ----------------
k.push(H1('2. Business model'));
k.push(H2('2.1 How the model works'));
k.push(P('Revenue ≈ average AuMA × net revenue margin (+ small performance fees). FY26 gross profit £123.0m on average AuMA of ~£22bn (revenue margin 0.55%, from 0.60% in FY25); H1 FY27 gross profit £57.7m at 0.50%. Administrative costs (FY26 down 16%) are ~70–75% people-related, with variable compensation flexing with profits. The model is capital-light (capex negligible), cash-generative at scale and regulated under the FCA’s IFPR regime.'));
k.push(H2('2.2 Key drivers'));
k.push(table(['Driver', 'Mechanism', 'Current direction'], [
  ['Volume (AuMA)', 'Net flows + market movement + M&A', 'Organic: negative but improving (H1 FY27 −£0.8bn vs −£2.3bn); inorganic: +£3.0bn River, +£1.9bn Hawksmoor'],
  ['Pricing (revenue margin)', 'Fee rates by product/channel; platform & DFM fee pressure; Consumer Duty value assessments', 'Falling: 60bp (FY25) → 55bp (FY26) → 50bp (H1 FY27)'],
  ['Mix', 'Retail UK equities (high fee) vs institutional, fixed income and MPS (low fee)', 'Negative mix shift: growth in institutional/MPS dilutes margin'],
  ['Performance', 'Relative fund performance drives platform/buy-list status and flows', 'Mixed; Sustainable & UK small-cap styles out of favour since 2022'],
  ['Regulation', 'Consumer Duty, SDR anti-greenwashing labels, IFPR capital, UK ISA reform', 'Cost and fee headwind; ISA reform (cash ISA cap from Apr-27) a possible tailwind'],
  ['Cost base', 'Fixed staff, systems, distribution; acquisition integration', 'Transformation saves ~£6m; but River/Hawksmoor add costs'],
  ['Capital cycle', 'Not capex-driven; seed capital and M&A are the “capex”', 'Bolt-ons funded from cash/shares'],
], [18, 42, 40]));
k.push(H2('2.3 Products, customers, suppliers, competitors, geographies'));
k.push(B('**Products:** UK-domiciled OEICs and unit trusts (core), Irish/Luxembourg UCITS for international distribution, investment trusts, segregated institutional mandates, model portfolio services (MPS) and multi-asset funds.'));
k.push(B('**Customers:** predominantly UK retail via platforms and advisers (Hargreaves Lansdown and interactive investor alone hold ~17% of Liontrust’s own register as nominees, illustrating the retail skew), wealth managers/DFMs, IFAs (MPS), UK pension schemes and local-authority pools (institutional), and international wealth (Europe, Latin America, Middle East, South Africa, Australia).'));
k.push(B('**Suppliers:** investment talent (key input), market data/research (FactSet, Bloomberg, MSCI, Morningstar), outsourced fund administration, transfer agency and depositary services, brokers, IT/cloud vendors.'));
k.push(B('**Competitors:** see Section 10 (listed and private). Most direct: Jupiter, Artemis, Premier Miton, Polar, Ninety One, Impax, Baillie Gifford, Royal London AM, Fidelity, Schroders (Nuveen), M&G, plus passive (Vanguard, iShares, L&G).'));
k.push(B('**Geographies:** UK ≈ 99% of revenue (FactSet geographic segments FY26: UK £133.7m; Europe £0.6m; Australia £0.1m).'));
k.push(B('**Contracts and payment terms:** fund management fees accrue daily as a % of fund NAV and are paid monthly from fund assets; segregated mandates under investment-management agreements (typically terminable at short notice, ~30–90 days); MPS on platform fee schedules. No long-term contractual lock-ins. Performance fees are immaterial.'));

// ---------------- 3 MACRO ----------------
k.push(H1('3. Macro and micro influences'));
k.push(table(['Tailwinds', 'Headwinds'], [
  ['UK equity valuations at multi-decade discount; any re-rating lifts AuMA and flows', 'Secular shift from active to passive and to low-cost MPS'],
  ['Cash ISA allowance cut (from Apr-2027) may push savings into equity funds', 'UK retail has been a net seller of UK equity funds for ~9 years'],
  ['Lower interest rates reduce money-market competition', '“Higher for longer” keeps cash/gilts attractive vs equity funds'],
  ['Market concentration risk in US mega-caps → demand for diversification/active', 'Platform and DFM fee pressure; Consumer Duty value assessments'],
  ['Sector consolidation creates bid interest for sub-scale managers', 'ESG backlash and SDR labelling regime weigh on Sustainable flows'],
  ['Institutional/international pipeline (mandates of £250m in Nov-25; >£500m gross institutional inflows in Q to Jun-26)', 'Key-person dependency; star-manager departures across the industry'],
  ['Mansion House / pension reforms favouring UK allocations', 'Wage inflation and tech/AI spend lift fixed costs'],
], [50, 50]));
k.push(P('**Net assessment:** macro is a modest tailwind (cheap UK assets, ISA reform) but micro/structural forces (passive, fee compression, distribution concentration) dominate. The equity therefore behaves like a levered call on UK small/mid-cap sentiment plus a corporate-event option.'));

// ---------------- 4 MOATS ----------------
k.push(H1('4. Competitive position and moats'));
k.push(P('Liontrust’s differentiation is its documented, repeatable team processes, a strong UK retail brand built 2010–21, and good adviser/platform engagement (c.1,000 client meetings per quarter; 85% with tier-1/2 clients). However, brand strength in asset management is performance-contingent and its fund ratings have weakened since 2022. Perceived value has deteriorated as passive and MPS products offer cheaper beta.'));
k.push(table(['Moat category', 'Rating', 'Assessment'], [
  ['Brand', 'Weak–Moderate', 'Recognised UK retail brand (Economic Advantage, Sustainable Future) but eroded by underperformance and outflows; no pricing power'],
  ['Hard assets', 'None', 'Asset-light; value lies in people and client relationships'],
  ['Long-term contracts', 'Weak', 'Daily-dealing funds; mandates terminable at short notice'],
  ['Network effect', 'None', 'No network effects; scale only aids distribution/ops'],
  ['Regulatory & switching costs', 'Weak–Moderate', 'Regulatory licences are a barrier to new entrants but not vs incumbents; retail inertia (CGT on switching, adviser re-papering) slows outflows'],
  ['Oligopolistic industry', 'No', 'Highly fragmented UK market (>100 active managers); consolidating'],
  ['Cash-flow predictability', 'Moderate–Low', 'Recurring fees but AuMA beta to markets and flows; FY22→FY26 EBIT −74%'],
  ['Scalability', 'High (operational), Low (current)', 'Incremental AuMA is high-margin; currently negative operating leverage'],
  ['Government interference risk', 'Moderate', 'FCA Consumer Duty, SDR, fee scrutiny; no direct intervention risk'],
  ['Bargaining power over stakeholders', 'Weak', 'Platforms, DFMs and star managers hold the bargaining power; clients can leave daily'],
], [22, 18, 60]));
k.push(P('**Conclusion:** no durable economic moat. The defensible assets are (i) the team processes and talent, which are portable; (ii) a sticky retail book with slow decay; and (iii) a listed, debt-free platform that is itself a consolidation vehicle or target.'));

// ---------------- 5 SUPPLY CHAIN ----------------
k.push(H1('5. Supply chain / value chain map'));
k.push(img(C + 'supply.png', 6.9, 4.85));
k.push(P('Liontrust sits in the middle (“manufacturer”) of the investment value chain. Economic rent is increasingly captured downstream by platforms (Hargreaves Lansdown — taken private by a CVC-led consortium; AJ Bell; interactive investor, owned by Aberdeen) and by wealth managers/DFMs who build in-house MPS. Upstream, data costs (FactSet, Bloomberg, MSCI) and talent costs are rising. Service-provider names marked “verify” are drawn from fund documentation and not re-checked in this session.'));

// ---------------- 6 KPIs ----------------
k.push(H1('6. Financial KPIs and segment metrics'));
k.push(H2('6.1 Five-year consolidated P&L (FactSet standardised; FY to 31 March)'));
k.push(table(['£m', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26', 'H1 FY27*'], [
  ['Revenue', '245.6', '245.2', '198.1', '169.9', '134.4', '63.0'],
  ['  growth y/y', '+40.1%', '−0.2%', '−19.2%', '−14.2%', '−20.9%', '−8.8%'],
  ['EBITDA', '92.2', '92.3', '68.0', '45.2', '30.5', 'n.a.'],
  ['  margin', '37.5%', '37.7%', '34.3%', '26.6%', '22.7%', 'n.a.'],
  ['EBIT (operating income)', '80.1', '60.9', '54.0', '34.0', '20.5', 'n.a.'],
  ['  margin', '32.6%', '24.8%', '27.2%', '20.0%', '15.3%', 'n.a.'],
  ['Net income', '59.2', '39.3', '(3.5)', '16.7', '9.6', 'n.a.'],
  ['Diluted EPS (p)', '96.6', '61.2', '(5.5)', '26.2', '15.4', 'n.a.'],
  ['EPS pre-unusuals, FactSet (p)', '97.4', '74.3', '55.8', '41.4', '23.1', 'n.a.'],
  ['Company adj. diluted EPS (p)', 'n.a.', 'n.a.', 'n.a.', '56.8', '36.7', '14.5'],
  ['Company adj. PBT', 'n.a.', 'n.a.', 'n.a.', '48.3', '~30.5', '11.9'],
  ['Statutory PBT', 'n.a.', 'n.a.', 'n.a.', '22.3', '14.4', '(4.2)'],
  ['DPS (p)', '72.0', '72.0', '72.0', '72.0', '19.0', '7.0'],
  ['Operating cash flow', '93.6', '43.4', '28.2', '20.6', '14.6', 'n.a.'],
  ['ROE (FactSet)', '34.1%', '19.4%', '−1.8%', '10.8%', '7.8%', 'n.a.'],
], [28, 12, 12, 12, 12, 12, 12]));
k.push(SRC('Source: FactSet Fundamentals (FF_SALES, FF_EBITDA_OPER, FF_EBIT_OPER, FF_NET_INC, FF_EPS_DIL, FF_EPS_DIL_BEF_UNUSUAL, FF_DPS, FF_OPER_CF, FF_ROE); company adjusted figures from results RNS via StreetAccount/press. *H1 FY27 = 6 months to 30-Sep-2026; growth vs H1 FY26 (£69.1m). FY21 revenue £175.3m / EBIT £43.8m for reference.'));
k.push(img(C + 'fin.png', 7.0, 2.7));
k.push(H2('6.2 Segment and geographic disclosure'));
k.push(P('Liontrust reports a **single operating segment** (investment management). It does not disclose revenue, EBITDA, EBIT or net income by investment team, product or channel; divisional profitability therefore cannot be presented. Geographic revenue (FactSet, company-reported):'));
k.push(table(['£m', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26'], [
  ['United Kingdom', '232.2', '226.3', '189.1', '159.1', '133.7'],
  ['Europe', '13.2', '16.9', '8.6', '10.6', '0.6'],
  ['Australia / Canada', '0.2', '0.2', '0.2', '0.1', '0.1'],
  ['UK share of total', '94.6%', '92.3%', '95.5%', '93.6%', '99.5%'],
], [30, 14, 14, 14, 14, 14]));
k.push(SRC('Source: FactSet segments (SALES, GEO). Note: the collapse in “Europe” in FY26 (£10.6m → £0.6m) likely reflects a change in attribution (e.g., Irish/Lux fund revenue booked in UK entities) rather than business loss — flag for management. Segment data are company-defined and not standardised.'));
k.push(P('**Trend commentary:** revenue peaked in FY22–23 (~£245m) on ~£33–36bn AuMA, then fell 45% to £134m in FY26 as AuMA shrank and the revenue margin compressed. Because costs are sticky, EBITDA margin fell from 38% to 23% and EBIT margin from 33% to 15%. Majedie (FY23) added revenue but at lower margins and was later impaired (FY24 net loss). H1 FY27 revenue fell a further 9% despite three months of River Global; the statutory loss reflects £16.1m of non-recurring and acquisition-related charges (£10.3m relating to River).'));
k.push(H2('6.3 Operational KPIs'));
k.push(img(C + 'auma.png', 7.0, 2.5));
k.push(table(['KPI', 'FY24', 'FY25', 'FY26', 'H1 FY27', 'Trend'], [
  ['Closing AuMA (£bn)', '27.8', '22.6', '19.6', '24.1', 'Stabilised via M&A; organic still shrinking'],
  ['Net flows (£bn)', '(6.1)', '(4.9)', '(4.2)', '(0.8)', 'Improving: annualised organic decay ~8% vs ~18–22%'],
  ['Net flows % opening AuMA', '~−19%', '−17.6%', '−18.5%', '−8.3% ann.', 'Improving'],
  ['Revenue margin (bp)', 'n.a.', '60', '55', '50', 'Deteriorating (mix + fees)'],
  ['Gross profit (£m)', 'n.a.', '157.7', '123.0', '57.7', 'Falling'],
  ['Adj. operating margin', 'n.a.', '~29%', '~24%', '~19%', 'Negative operating leverage'],
  ['Institutional wins', '–', '–', '£250m mandates; £330m Q3 inflows', '>£500m gross (Q to Jun-26)', 'Pipeline building'],
  ['Capex intensity', '<1% of revenue', '<1%', '<1%', '<1%', 'Not a driver'],
  ['Dividend cover (adj. EPS/DPS)', '~1.0x', '0.79x', '1.93x', '2.1x (interim)', 'Re-based'],
], [24, 10, 10, 14, 14, 28]));
k.push(SRC('Source: Liontrust trading statements/annual reports via press; FactSet. Adj. operating margin per press summaries (FY26 24.0% vs 29.2%); H1 FY27 approximated as (adj. PBT − est. £1m interest income)/gross profit. Fund-performance quartiles, headcount and comp ratio were not retrievable in this session.'));

// ---------------- 7 RECENT EARNINGS ----------------
k.push(H1('7. Recent earnings and management sentiment'));
k.push(H2('7.1 Latest result: H1 FY27 (six months to 30-Sep-2026, reported 19-Nov-2026)'));
k.push(table(['Metric', 'H1 FY27', 'H1 FY26', 'Change', 'Comment'], [
  ['Revenue', '£63.0m', '£69.1m', '−9%', 'Despite 3 months of River Global'],
  ['Gross profit', '£57.7m', '£63.3m', '−9%', 'Revenue margin 50bp vs 56bp'],
  ['Adjusted PBT', '£11.9m', '£15.7m', '−24%', ''],
  ['Adjusted diluted EPS', '14.5p', '18.7p', '−22%', '≈40% of pre-result FY27E consensus (36.6p) vs ~51% H1 share last year'],
  ['Statutory PBT', '£(4.2)m', '£7.3m', 'n.m.', '£16.1m non-recurring/acquisition charges (£10.3m River)'],
  ['Net flows', '£(816)m', '£(2,324)m', '−65%', 'Q1 −£357m; Q2 −£459m'],
  ['Closing AuMA', '£24.1bn', '—', '', '£24.06bn at 12-Nov-2026; +£1.9bn Hawksmoor due 30-Nov'],
  ['Interim dividend', '7.0p', '7.0p', 'flat', 'Ex 26-Nov-2026; paid 6-Jan-2027'],
], [18, 13, 13, 10, 46]));
k.push(P('**Vs expectations:** FactSet had no explicit H1 consensus; relative to the FY27E consensus held before the print (36.6p, 1-Nov-2026), H1 EPS of 14.5p implies a ~20% shortfall on run-rate. Consensus FY27E has since fallen to 34.8p (all eight analysts cut; range 30.2–36.5p), FY28E to 41.4p. Consensus FY27E revenue is £128.8m (8 est.). We regard H2 expectations (≈20p, +40% h/h) as demanding.'));
k.push(P('**Segment drivers:** River Global (from 1-Jul) and lower outflows in multi-asset/institutional supported AuMA; UK equity retail franchises (Economic Advantage, Global Fundamental) and Sustainable remained in outflow. **Margins:** adjusted operating margin compressed to ~19% on lower fee rate and added River costs. **Guidance/tone:** management is “cautious about the near-term flow environment but increasingly confident in the opportunities over the medium and longer term”; Hawksmoor guided as earnings-enhancing in FY27 with £1.9m exceptional costs (40% in FY27).'));
k.push(P('**Balance-sheet flags:** (1) acquisition-related charges of £10.3m against River consideration of £7.6m initial (+ up to £2.1m contingent) — the integration bill exceeds the purchase price; (2) cash continues to decline (FY23 £131m → FY26 £52.7m) and will fall by a further £6m for Hawksmoor (+ up to £4m contingent); (3) the impairment-trigger language (outflows ≥10% of AuMA) remains live for acquired intangibles (£61m at Mar-26) and goodwill (£32m).'));
k.push(P('**Market reaction:** −6% on the day and −11% the next (−16% over two days, ~4x average volume) to an all-time-low area of ~226p. The market had priced in stabilisation after the 30-Sep Hawksmoor rally (+18%); the statutory loss and margin compression reset that. **Unusual vs history:** first statutory interim loss in the period reviewed; deal costs disproportionate to deal size; revenue margin falling faster than in any prior period.'));
k.push(H2('7.2 Earnings-call summaries and sentiment trajectory'));
k.push(table(['Event', 'Management focus', 'Sentiment'], [
  ['FY25 results (25/30-Jun-2025)', '“More challenging year”; transformation programme (~£6m savings); new Capital Allocation Policy (≥50% payout, buybacks); “outlook for active management more favourable”', 'Defensive / cautious (score 2/5)'],
  ['H1 FY26 (20/25-Nov-2025)', '“Another challenging period for flows… more reasons for optimism”; institutional/international pipeline taking longer; £10m buyback (“shares undervalued”); acknowledged share-price underperformance', 'Cautiously optimistic, defensive on capital allocation (2.5/5)'],
  ['FY26 results (24/30-Jun-2026)', 'Diversification by client, geography and style (River = value/income); multi-asset turned to small inflows; AI/technology; dividend cut “in line with earnings”, executive variable pay down 100%', 'Constructive (3.5/5) — shares +19% in 5 days'],
  ['H1 FY27 (19-Nov-2026)', 'Statutory loss; River and Hawksmoor integration; cautious near term, confident medium term', 'Cautious (2/5)'],
], [20, 58, 22]));
k.push(SRC('Source: FactSet CallStreet corrected transcripts (Q4 2025 30-Jun-2025; Q2 2026 25-Nov-2025; Q4 2026 30-Jun-2026); StreetAccount “Transcript Intelligence”; press. Sentiment scores are analyst judgement (1 = negative, 5 = positive).'));
k.push(P('**Shift over time:** language has moved from “the cycle will turn for active” (2025) to “diversify and acquire scale” (2026). Management now leans on M&A to offset organic decline — a strategic pivot that also raises the question of whether shareholders are better served by Liontrust being the acquired rather than the acquirer.'));

// ---------------- 8 FORWARD ----------------
k.push(H1('8. Forward EPS projections (FY27E–FY29E, year to March)'));
k.push(table(['', 'FY26A', 'FY27E (ours)', 'FY28E (ours)', 'FY29E (ours)', 'Consensus FY27/28/29'], [
  ['Average AuMA (£bn)', '~22.0', '~23.6', '~26.0', '~26.8', '—'],
  ['Net flows (£bn)', '(4.2)', '(1.4)', '(1.0)', '(0.3)', '—'],
  ['Market return assumption', '—', '+2% H2', '+5%', '+5%', '—'],
  ['Revenue margin, net (bp)', '55', '~49', '47', '46', '—'],
  ['Gross profit (£m)', '123.0', '117.9', '122.2', '123.3', '—'],
  ['Revenue (£m, FactSet basis)', '134.4', '~126', '~132', '~134', '128.8 / 140.8 / 148.3'],
  ['Admin costs (£m)', '~94', '94.3', '92.0', '93.5', '—'],
  ['Adj. operating profit (£m)', '~28', '23.6', '30.2', '29.8', 'EBIT 28.8 (FY27)'],
  ['Net interest/other (£m)', '~2.5', '2.0', '2.0', '2.0', '—'],
  ['Adj. PBT (£m)', '~30.5', '25.6', '32.2', '31.8', '—'],
  ['Tax rate', '25%', '25%', '25%', '25%', '—'],
  ['Diluted shares (m)', '~62', '63.5', '63.0', '62.5', '—'],
  ['**Adj. diluted EPS (p)**', '**36.7**', '**30.2**', '**38.3**', '**38.2**', '**34.8 / 41.4 / 46.2**'],
  ['DPS at 50% payout (p)', '19.0', '~15', '~19', '~19', '—'],
], [24, 12, 14, 14, 14, 22]));
k.push(P('**Assumptions and rationale:** (1) **Industry growth:** UK active-fund market flat to negative in real terms; market beta +5% p.a. (2) **Market share:** continued organic share loss, slowing as retail books season; small institutional gains. (3) **Pricing:** no price increases are possible; we assume 1–2bp annual margin erosion plus dilution from lower-fee Hawksmoor MPS and River segregated assets. (4) **Cost pressures:** 3% wage/tech inflation offset by transformation and integration savings (~£4m FY28). (5) **Operating leverage:** each £1bn of AuMA ≈ £4.7m revenue at ~70–80% incremental margin, so flows are the swing factor (±£1bn flow ≈ ±5p EPS). (6) **Financing:** no debt; interest income falls as cash is spent on M&A and dividends. (7) **Dilution:** +2.97m River consideration shares (Jun-26), LTIP awards (~0.6m p.a. to the CEO alone) offset by modest buybacks.'));
k.push(P('**Conclusion:** our FY27–29E EPS sits 13%, 7% and 17% below consensus. Consensus assumes a return to growth that requires positive organic flows by FY29; we see stabilisation rather than growth. Even on our numbers the stock trades on <6x FY28E earnings ex-cash.'));

// ---------------- 9 CAPITAL STRUCTURE ----------------
k.push(H1('9. Capital structure and liquidity'));
k.push(table(['Item', 'FY23', 'FY24', 'FY25', 'FY26', 'Comment'], [
  ['Cash & equivalents (£m)', '131.0', '112.5', '79.8', '52.7', 'Steady decline: dividends > operating cash flow'],
  ['Total debt (£m)', '3.6', '4.1', '2.5', '2.7', 'Lease liabilities only; no bank debt'],
  ['Net cash (£m)', '127.4', '108.4', '77.3', '50.0', '~£44m pro forma Hawksmoor'],
  ['Shareholders’ equity (£m)', '221.0', '171.2', '138.2', '107.9', 'Eroded by impairment and distributions'],
  ['Goodwill / intangibles (£m)', '38.6 / 129.2', '32.1 / 80.6', '32.1 / 71.5', '32.1 / 61.3', 'Tangible equity ≈ £15m at Mar-26'],
], [24, 11, 11, 11, 11, 32]));
k.push(SRC('Source: FactSet Fundamentals (FF_CASH_GENERIC, FF_DEBT, FF_SHLDRS_EQ, FF_GW, FF_INTANG). FactSet Debt Capital Structure holds no bond/loan instruments for Liontrust.'));
k.push(B('**Debt, maturities, covenants, interest:** none — no bonds, term loans or disclosed revolver; therefore no covenants and no interest cost (net interest income ~£2–3m p.a.).'));
k.push(B('**Liquidity:** adequate but no longer abundant. Annual dividend at 19p ≈ £12m vs FY26 operating cash flow £14.6m. Contingent consideration: up to £2.1m (River, in shares) and up to £4m (Hawksmoor, cash, over 2 years).'));
k.push(B('**Regulatory capital:** FCA IFPR applies to regulated subsidiaries; own-funds surplus is published in the IFPR disclosure but could not be accessed in this session. With tangible equity of only ~£15m after intangibles, regulatory headroom is the binding constraint on further cash M&A and buybacks — a key question for management.'));

// ---------------- 10 PEERS ----------------
k.push(H1('10. Valuation and peer analysis'));
k.push(H2('10.1 Listed peer multiples'));
const pr = peers.map(r => [r.n + ' (' + r.t + ')', '£' + Math.round(r.mc), '£' + Math.round(r.ev), fx(r.evs1), fx(r.eveb), fx(r.evebit1), fx(r.pe1), fx(r.pe2), f1(r.nd) + 'x', f1(r.ebm) + '%', f1(r.ebitm) + '%', f1(r.g) + '%', f1(r.ocfy) + '%']);
k.push(table(['Company', 'Mkt cap £m', 'EV £m', 'EV/Sales FY1', 'EV/EBITDA LFY', 'EV/EBIT FY1', 'P/E FY1', 'P/E FY2', 'Net debt/EBITDA', 'EBITDA mgn LFY', 'EBIT mgn LFY', 'Sales g LFY', 'OCF yield'], pr,
  [17, 7, 7, 7, 7, 7, 6, 6, 8, 7, 7, 7, 7], { size: 13 }));
k.push(SRC('Source: FactSet market values (26-Nov-2026), FactSet Fundamentals (latest reported FY), FactSet consensus FY1/FY2 (sales, EBIT, EPS). Man Group converted at USD/GBP 1.311 (implied from FactSet prices). Rathbones EV excludes balance-sheet cash (banking-licence cash). Liontrust EV pro forma Hawksmoor. Negative net debt = net cash. Ashmore sales exclude seed/investment gains, inflating its ratios.'));
k.push(table(['Metric', 'Liontrust', 'Peer median', 'Liontrust vs median', 'Screen'], [
  ['EV/Sales FY1', '0.74x', '1.58x', '−53%', 'Cheap'],
  ['EV/EBITDA LFY', '3.1x', '4.9x', '−36%', 'Cheap'],
  ['EV/EBIT FY1', '3.3x', '5.1x', '−35%', 'Cheap'],
  ['P/E FY1 / FY2', '6.5x / 5.4x', '9.6x / 9.3x', '−33% / −42%', 'Cheap'],
  ['Net debt/EBITDA', '−1.4x (net cash)', '−1.6x', 'In line', 'Fair'],
  ['EBITDA / EBIT margin LFY', '22.7% / 15.3%', '28.3% / 25.7%', '−6 / −10 ppts', 'Below peers'],
  ['Sales growth LFY', '−20.9%', '−1.0%', '−20 ppts', 'Worst in group with Impax'],
  ['OCF yield', '10.5%', '11.2%', 'In line', 'Fair'],
], [22, 18, 18, 22, 20]));
k.push(P('**Verdict:** Liontrust screens **cheap** on every earnings and sales multiple — but its revenue decline is the worst in the group, so a discount is warranted. The question is the size of the discount. Adjusting for margin, it trades ~25% below where the peer regression would place it.'));
k.push(H2('10.2 Regression: TEV/Sales vs EBIT margin'));
k.push(img(C + 'regression.png', 7.0, 3.9));
k.push(P('OLS across ten listed UK asset/wealth managers (Ashmore excluded as an outlier because FactSet sales exclude its investment gains): **EBIT margin = 14.1 + 8.2 × (EV/Sales), R² = 0.33.** At Liontrust’s FY1 consensus EBIT margin of 22.4%, the fitted EV/Sales is **1.00x** versus 0.74x actual — implying EV of ~£129m, equity of ~£173m and **~275p per share (+22%)**. The modest R² reflects style/fee-mix dispersion (Polar, Ninety One and Man earn premium margins); results should be read as directional.'));
k.push(H2('10.2a Additional regressions: PBR vs ROE and EV/AUM vs E/AUM'));
k.push(img(C + 'reg_pbroe.png', 7.0, 3.9));
k.push(P('Linear: ROE = −5.1 + 14.5×P/B (R² 0.94); log: ROE = 11.4 + 23.0×ln(P/B) (R² 0.73). Liontrust’s forward ROE of ~20% (FY27E consensus EPS on Mar-26 book equity of £108m) implies a fitted P/B of 1.73x (linear) / 1.45x (log) vs 1.29x actual — **~255–300p per share (+13% to +34%)**. Book value is mostly acquired intangibles, so this measure flatters slightly.'));
k.push(img(C + 'reg_evaum.png', 7.0, 3.9));
k.push(P('OLS ex-Ashmore: EV/AUM (%) = 0.010 + 0.0506 × E/AUM (bp), R² 0.69 — the market capitalises operating earnings at ~5x EBIT. Liontrust earns ~12bp of FY27E EBIT on AUM; the fitted EV/AUM is 0.61% vs 0.40% actual → EV ~£148m + ~£44m net cash ≈ **£192m, ~300–310p per share (+35%)**. Impax (IPX LN), shown for reference, screens similarly cheap (0.23% actual vs 0.36% fitted).'));
k.push(SRC('Source: FactSet market values/prices (26-Nov-2026), book equity (latest FY), FY1 consensus EPS and EBIT; AUM from latest company releases (Jun–Sep 2026; Aberdeen AUMA incl. platform; USD AUM at 1.311). E/AUM = FY1 EBIT ÷ AUM.'));
k.push(H2('10.3 Historical trading range'));
k.push(img(C + 'histmult.png', 7.0, 2.5));
k.push(table(['At FY-end price', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26', 'Now'], [
  ['Share price (p)', '1,420', '1,274', '1,022', '672', '371', '241.5', '225.5'],
  ['EV (£m)', '789', '649', '525', '321', '155', '96', '96'],
  ['EV/Sales', '4.5x', '2.6x', '2.1x', '1.6x', '0.9x', '0.7x', '0.7x'],
  ['EV/EBITDA', '14.9x', '7.0x', '5.7x', '4.7x', '3.4x', '3.2x', '3.1x'],
  ['EV/EBIT', '18.0x', '8.1x', '8.6x', '5.9x', '4.6x', '4.7x', '4.7x (3.3x FY27E)'],
  ['P/E (FactSet pre-unusual EPS)', '25.1x', '13.1x', '13.8x', '12.0x', '9.0x', '10.5x', '9.8x (6.5x FY27E adj.)'],
], [24, 10, 10, 10, 10, 10, 10, 16]));
k.push(P('Liontrust is at the very bottom of its five-year range on every multiple (EV/EBITDA 3.1x vs 5-yr average ~6.4x). Relative to listed peers it moved from a premium (FY21: growth/ESG darling) to a ~35–50% discount.'));
k.push(H2('10.4 Competitor universe (listed and private)'));
k.push(table(['Competitor', 'Ticker / owner', 'Listed?', 'Overlap'], [
  ['Jupiter Fund Management', 'JUP LN', 'Yes (LSE)', 'UK retail active equity; acquirer (CCLA 2026)'],
  ['Polar Capital', 'POLR LN', 'Yes (AIM)', 'Specialist equity, global tech/healthcare'],
  ['Ninety One', 'N91 LN / NY JN', 'Yes', 'Active equity/FI; absorbed Sanlam UK active business'],
  ['Premier Miton', 'PMI LN', 'Yes (AIM)', 'UK retail equity & multi-asset — closest small-cap analogue'],
  ['Impax Asset Management', 'IPX LN', 'Yes (AIM)', 'Sustainable/environmental — Sustainable Investment rival'],
  ['Ashmore', 'ASHM LN', 'Yes', 'EM specialist (style peer)'],
  ['Aberdeen Group (incl. interactive investor)', 'ABDN LN', 'Yes', 'Active AM; owns ii platform (distributor & competitor)'],
  ['Man Group', 'EMG LN', 'Yes', 'Alternatives/systematic'],
  ['Rathbones', 'RAT LN', 'Yes', 'Wealth + Rathbone Asset Management funds; MPS'],
  ['Brooks Macdonald', 'BRK LN', 'Yes', 'Wealth/MPS (Hawksmoor-type competitor)'],
  ['M&G', 'MNG LN', 'Yes', 'UK retail funds'],
  ['Janus Henderson', 'JHG US', 'Yes (NYSE)', 'UK retail equity, investment trusts'],
  ['Columbia Threadneedle', 'Ameriprise (AMP US)', 'Parent listed', 'UK retail equity'],
  ['Schroders', 'Nuveen / TIAA', 'No (delisted 2-Oct-2026)', 'Full-range UK manager'],
  ['Artemis Investment Management', 'Affiliated Managers Group (AMG US) majority', 'Parent listed', 'UK retail equity — direct rival'],
  ['Baillie Gifford', 'Partnership', 'No', 'Growth equity, investment trusts'],
  ['Fidelity International', 'Private (FIL)', 'No', 'Retail funds and platform'],
  ['Royal London Asset Management', 'Mutual', 'No', 'UK equity, sustainable, fixed income'],
  ['Fundsmith / Evenlode / Slater / Troy / Ruffer', 'Private', 'No', 'Retail quality-growth and multi-asset boutiques'],
  ['Gresham House', 'Searchlight Capital (PE)', 'No', 'UK smaller companies & real assets'],
  ['Vanguard / BlackRock iShares / L&G', 'Private / BLK US / LGEN LN', 'Mixed', 'Passive substitutes'],
], [30, 26, 16, 28]));

// ---------------- 11 M&A ----------------
k.push(H1('11. M&A: industry, takeover candidacy and comparables'));
k.push(H2('11.1 Industry M&A context'));
k.push(P('UK asset management is in a consolidation phase driven by fee compression, passive substitution, rising regulatory/technology fixed costs and depressed public valuations. 2026 has seen the largest UK deal in the sector’s history (Nuveen’s £9.9bn take-private of Schroders, completed 1-Oct-2026), Jupiter’s purchase of CCLA (£15bn AuM) and two bolt-ons by Liontrust itself. Private equity (Searchlight/Gresham House; CVC/Hargreaves Lansdown; Pollen Street/Mattioli Woods) and US/European strategics are active buyers of UK distribution and retail franchises.'));
k.push(H2('11.2 Is Liontrust a takeover target?'));
k.push(table(['Pros (supporting a bid)', 'Impediments'], [
  ['Valuation: 0.40% EV/AuMA, 3.3x EV/EBIT, net cash ~31% of market cap', 'Continuing outflows: acquirer buys a shrinking book; client attrition on change of control'],
  ['Cost synergies: ~£94m admin base; a consolidator could remove 35–45% (operations, distribution, listing, back office)', 'Key-person risk: investment teams may leave (LLP structure, retention payments required)'],
  ['UK retail distribution, platform relationships and brand have strategic value to a US/European manager seeking UK access', 'Management/board stance: board has rejected a strategic review; CEO/CFO long-tenured'],
  ['Activist pressure (GAM 5.01%) and retail-heavy register — low price anchoring', 'Small size (£140m) may be below the radar of large strategics'],
  ['Board now includes Martin Gilbert (architect of Aberdeen’s consolidation); River and Hawksmoor deals show a willingness to transact', 'Intangible-heavy balance sheet; deal costs (River £10.3m) show integration is expensive'],
  ['No debt, no change-of-control financing issues; simple capital structure', 'Takeover Code process complexity; potential partial-sale/merger-of-equals rather than cash bid'],
], [50, 50]));
k.push(P('**Potential acquirers (illustrative):** UK consolidators (Jupiter, Premier Miton merger-of-equals, Polar, Ninety One), European/US managers seeking UK retail access (e.g., Nuveen-Schroders bolt-on, Amundi, Natixis IM, AMG/Artemis-style affiliate model), private equity (Searchlight, Pollen Street, Bridgepoint-type investors), and wealth managers seeking manufacturing/MPS (Rathbones, Brooks Macdonald, Evelyn, Quilter).'));
k.push(H2('11.3 Potential takeout valuation'));
k.push(table(['Method', 'Range', 'Implied EV (£m)', 'Implied value/share'], [
  ['% of AuMA (~£26bn incl. Hawksmoor)', '0.6% – 0.9%', '156 – 234', '~315p – 440p'],
  ['EV / FY28E adj. EBITDA (~£33m)', '5x – 8x', '165 – 264', '~330p – 485p'],
  ['P/E on FY28E EPS (38p)', '9x – 12x', '—', '~340p – 455p'],
  ['Premium to undisturbed (225.5p)', '30% – 60%', '—', '~295p – 360p'],
  ['**Central takeout estimate**', '**~0.75% AuMA / ~6x EBITDA**', '**~195**', '**~360p – 380p**'],
], [32, 22, 18, 28]));
k.push(SRC('Per-share values add pro forma net cash of ~£44m and use ~63.5m diluted shares. Ranges reflect precedent multiples below; distressed/run-off books trade at 0.3–0.7% of AuM, growing quality franchises at 1–2%+.'));
k.push(H2('11.4 Comparable industry transactions (last ~5 years)'));
k.push(table(['Announced', 'Target', 'Acquirer', 'Value', 'AuM', 'Multiples / notes'], [
  ['Sep-2026', 'Hawksmoor fund mgmt & MPS', 'Liontrust', '£6m + up to £4m cash', '£1.9bn', '0.32–0.53% of AuM'],
  ['Mar-2026', 'River Global Holdings', 'Liontrust', '£7.6m shares + up to £2.1m', '£3.0bn', '~0.25–0.32% of AuM; £10.3m acquisition costs'],
  ['Feb-2026', 'Schroders plc', 'Nuveen (TIAA)', '£9.9bn (590p + up to 22p divs)', '~$1.1tn', '~17x 2025 adj. op. profit after tax; 29–34% premium (42% to VWAP); ~1.2% of AuM'],
  ['Late 2025 / Feb-2026 (compl.)', 'CCLA Investment Management', 'Jupiter', '~£100m (reported; unconfirmed)', '£15.0bn', '~0.7% of AuM; ≥£16m cost synergies'],
  ['Aug-2024', 'Hargreaves Lansdown (platform)', 'CVC / Nordic Capital / ADIA', '£5.4bn (1,140p incl. div)', '~£155bn AuA', '~3.5% of AuA; ~22x P/E (approx.)'],
  ['Aug-2024', 'AXA Investment Managers', 'BNP Paribas', '€5.1bn', '~€850bn', '~0.6% of AuM (approx.)'],
  ['Mar-2024', 'Mattioli Woods', 'Pollen Street Capital', '£432m', '~£15bn AuMA', 'Wealth; ~2.9% of AuMA (approx.)'],
  ['Jul-2023', 'Gresham House', 'Searchlight Capital', '£470m equity / £441m EV', '~£8.4bn', '~16x EBITDA; 63% premium'],
  ['May-2023', 'GAM Holding (failed)', 'Liontrust', 'All-share offer ~CHF 100m (approx.)', '~CHF 23bn', '~0.4–0.5% of AuM; 33.45% acceptance; lapsed Aug-2023'],
  ['Mar-2023', 'Investec Wealth & Investment UK', 'Rathbones', '£839m (all-share)', '~£40bn', '~2.1% of AuM'],
  ['Apr-2022', 'Brewin Dolphin', 'RBC Wealth Management', '£1.6bn', '~£59bn', '~2.7% of AuM; ~63% premium (approx.)'],
  ['Jan-2022', 'Majedie Asset Management', 'Liontrust', 'Up to £120m (£80m + £40m deferred)', '£5.8bn', 'Up to ~2.1% of AuM (later impaired)'],
], [12, 18, 15, 18, 10, 27]));
k.push(SRC('Source: company RNS and press (Sharecast, Trustnet, Slaughter and May, Portfolio Adviser, City AM, Bloomberg); FactSet M&A not queried deal-by-deal. “Approx.” = figures recalled from public reporting and not re-verified in this session.'));
k.push(H2('11.5 Liontrust’s own acquisitions (last 10 years)'));
k.push(table(['Date', 'Target', 'Consideration', 'AuM acquired', 'Price / AuM', 'Outcome'], [
  ['2017 (Apr)', 'Alliance Trust Investments (Sustainable team)', '~£30–31m', '~£2.5bn', '~1.2%', 'Highly successful initially — seeded Sustainable Investment growth to >£10bn; since reversed'],
  ['2019 (Oct)', 'Neptune Investment Management', '~£38–40m (shares + earn-out)', '~£2.7bn (reported)', '~1.4%', 'Mixed; Neptune funds largely merged/outflowed'],
  ['2020–21', 'Architas UK multi-asset business (AXA)', '~£72–75m', '~£5.7bn', '~1.3%', 'Formed Multi-Asset/MPS base; outflowed then stabilised'],
  ['2022 (Jan ann. / Apr compl.)', 'Majedie Asset Management', '£80m initial (3.7m shares + cash) + up to £40m deferred', '£5.8bn', 'up to ~2.1%', 'Poor: heavy outflows; intangibles impaired (FY24 statutory loss)'],
  ['2023 (May–Aug)', 'GAM Holding AG (Swiss-listed)', 'All-share (~CHF 100m) + CHF 20m loan facility', '~CHF 23bn', '~0.4–0.5%', 'Failed (33.45% acceptance); costs expensed; loan replaced by Rock/NewGAMe'],
  ['2026 (Mar ann. / 30-Jun compl.)', 'River Global Holdings', '2.97m shares at 255.9p (£7.6m) + up to £2.1m', '£3.0bn', '~0.3%', 'Too early; £10.3m acquisition costs; Martin Gilbert joins board'],
  ['2026 (30-Sep ann. / exp. 30-Nov)', 'Hawksmoor fund management & MPS', '£6m cash + 2 × up to £2m', '£1.9bn', '0.3–0.5%', 'Pending; guided earnings-enhancing; £1.9m exceptional costs'],
], [14, 20, 22, 11, 10, 23]));
k.push(SRC('Source: Liontrust RNS and results; Wikipedia/ShareScope/Trustnet summaries where primary filings could not be fetched. Sources differ by £1–5m on some historical considerations.'));

// ---------------- 12 MANAGEMENT ----------------
k.push(H1('12. Management assessment'));
k.push(table(['Executive', 'Role / tenure', 'Track record', 'Skin in the game'], [
  ['John Ions', 'CEO since Feb-2010 (16+ yrs); exec director', 'Built Liontrust from a small boutique (~£2bn AuM) to ~£36bn+ peak via process-driven teams and acquisitions (ATI, Neptune, Architas, Majedie). Prior: distribution/leadership roles at Aberdeen, SG Asset Management, Man Fund Management. Since 2021: AuMA −45%, shares −90%, failed GAM bid', '~1.0m shares (1.59%, ~£2.3m); GAM letter cites ~£40m cumulative pay since 2010'],
  ['Vinay Abrol', 'CFO & exec director since 1995 (31 yrs)', 'Long-standing finance lead; oversaw capital-allocation policy and dividend history', 'Participates in SIP/LTIP; position not retrieved'],
  ['Edward Catton', 'COO', 'Operations, transformation programme', 'n.a.'],
  ['David Boyle', 'Chief Strategy Officer (since 2020)', 'Corporate development (M&A incl. Majedie, GAM, River, Hawksmoor)', 'n.a.'],
  ['Simon Hildrey', 'Chief Marketing Officer', 'Brand, distribution communications', 'n.a.'],
  ['Martin Kearney / Sally Buckmaster', 'CRO / General Counsel & Co. Sec.', 'Risk and governance', 'n.a.'],
], [14, 18, 44, 24]));
k.push(P('**Capital allocation history:** ROE fell from 34% (FY22) to 8% (FY26). Of ~£270m deployed on acquisitions (incl. share consideration) since 2017, the ATI deal created substantial value; Majedie (up to £120m at the 2022 peak, partly in shares at ~1,500p+) destroyed value. Dividends of 72p were maintained through FY25 despite cover falling below 1x and cash falling ~£80m — i.e., the dividend was funded from the balance sheet. The £10m buyback (Nov-25 to Jun-26) was executed at ~230–300p, accretive at current prices.'));
k.push(P('**Red flags:** (1) pay-for-performance misalignment — cumulative CEO pay versus a 90% share-price decline; 2026 LTIP of 566,203 nil-cost options (284% of salary) despite the dividend cut, though capped and variable pay for FY26 was zero; (2) AGM Sept-2026: remuneration report 81.3% and CEO re-election 85.0% support — material dissent; (3) strategy pivots: organic growth → ESG leader → large M&A (GAM) → bolt-on consolidation; (4) promotional tone around the buyback (“shares undervalued”) while declining a sale process; (5) no CEO/CFO succession despite sustained underperformance.'));
k.push(P('**Founder vs professional manager:** Ions is a “re-founder” — a professional manager who has run the business for 16 years and shaped its identity. Founder-type managers excel in growth phases; in a mature, shrinking, consolidating industry, a capital-allocator mindset (cost-out, sale or merger) is typically more value-accretive. **Recent changes:** no changes to the CEO/CFO; Martin Gilbert joined the board (1-Jul-2026).'));

// ---------------- 13 BOARD ----------------
k.push(H1('13. Board of Directors'));
k.push(table(['Director', 'Role', 'On LIO board since', 'Background', 'Other affiliations'], [
  ['Luke Savage', 'Non-Executive Chair', 'Chair from 20-Sep-2024', 'Chartered accountant; CFO Standard Life Aberdeen (2014–17); CFO Lloyd’s of London (2004–14); CFO Equities Deutsche Bank; Morgan Stanley', 'Chair Chesnara plc; INED DWF Group; director Numis; Treasurer QMUL'],
  ['John Ions', 'CEO', '2010', 'See Section 12', 'Liontrust subsidiaries'],
  ['Vinay Abrol', 'CFO', '1995', 'Liontrust finance since founding era', 'Liontrust subsidiaries'],
  ['Miriam Greenwood OBE', 'Senior Independent Director', '16-Nov-2023', 'Corporate finance (Spark Advisory Partners; Brewin Dolphin / Nplus1 debt advisory); ex-NED Ofgem/GEMA; ex-Chair Smart Metering Systems', 'Chair Parvus Energy Efficiency Trust; NED Canopius, Gulf International Bank (UK), Encyclis; previously NED River & Mercantile Group'],
  ['Mandy Donald', 'Independent NED', '1-Oct-2019', 'Chartered accountant; professional-services and finance leadership', 'INED Mortgage Advice Bureau (2025–); SID JPMorgan US Smaller Cos IT; NED Punter Southall Group, BTG; Gowling WLG; Institute of Cancer Research'],
  ['Martin Gilbert', 'Independent NED', '1-Jul-2026', 'Co-founder/CEO Aberdeen Asset Management (1983–2017); Vice-Chair Standard Life Aberdeen (to 2020); Exec Chair River Global (ex-AssetCo) since 2021; ex-Deputy Chair River & Mercantile', 'Chair Revolut; NED Glencore; Chair Flotation Energy; SID Toscafund; PRA Practitioner Panel'],
], [15, 13, 13, 31, 28]));
k.push(SRC('Source: FactSet People (company_people, jobs), Liontrust RNS (directorate change 1-Jul-2026), press.'));
k.push(P('**Changes in the last five years:** Alastair Barbour stepped down as Chair and was succeeded by Luke Savage (Sept-2024); Miriam Greenwood appointed (Nov-2023, now SID); Martin Gilbert appointed on completion of River Global (Jul-2026). Several longer-serving NEDs left during 2021–25 (former directors included George Yeandle, Sophia Tickell, Quintin Price and Rebecca Shelley — exact dates not verified in this session). **Governance observations:** a small board (4 NEDs) with three finance-trained NEDs; Gilbert’s “independence” is arguable given he is Executive Chair of River Global plc, which received ~2.97m Liontrust consideration shares and is owed contingent consideration — a related-party sensitivity. Conversely, his consolidation pedigree may make the board more receptive to strategic options.'));

// ---------------- 14 SHAREHOLDERS ----------------
k.push(H1('14. Shareholders, activism and short interest'));
k.push(table(['#', 'Holder', 'Type', '% held', 'Shares (m)', 'As of'], [
  ['1', 'Hargreaves Lansdown Fund Managers', 'Platform / fund manager (retail nominee)', '9.77%', '6.15', 'May-2026'],
  ['2', 'Interactive Investor (Aberdeen)', 'Retail platform nominee', '7.53%', '4.74', 'May-2026'],
  ['3', '“Lamprell plc” (FactSet attribution — likely mis-mapped)', 'Unverified', '5.24%', '3.30', 'May-2026'],
  ['4', 'GAM Holding AG (GAM special-situations funds)', 'Institutional — activist', '5.01%', '3.16', 'Aug-2026'],
  ['5', 'Canaccord Genuity Wealth', 'Wealth manager', '4.92%', '3.10', 'May-2025 (stale)'],
  ['6', 'UBS Asset Management (UK)', 'Institutional', '3.29%', '2.07', 'May-2026'],
  ['7', 'Merseyside Pension Fund', 'Pension fund', '2.43%', '1.53', 'Sep-2026'],
  ['8', 'Slater Investments', 'Institutional (UK boutique)', '2.40%', '1.51', 'Sep-2026'],
  ['9', 'CACEIS Bank (custodian)', 'Nominee', '2.21%', '1.39', 'Sep-2026'],
  ['10', 'Norges Bank Investment Management', 'Sovereign wealth', '2.05%', '1.29', 'Sep-2026'],
  ['11', 'John Ions (CEO)', 'Insider', '1.59%', '1.00', 'Aug-2026'],
], [4, 34, 24, 10, 12, 16]));
k.push(SRC('Source: FactSet Ownership (security_holders, holderType FS). Percentages on FactSet share basis (~63m); dates differ by holder. River Global plc (~2.97m consideration shares, ~4.7%) intended to distribute shares to its own shareholders (Jul/Aug-2026) and does not appear separately. Treat row 3 as a data anomaly pending TR-1 verification.'));
k.push(H2('14.1 Activist campaign: GAM special-situations funds (2026)'));
k.push(table(['Date', 'Event'], [
  ['23-Mar-2026', 'Open letter from Albert Saporta and Randel Freeman (portfolio managers, GAM Global Opportunities and GAM Global Special Situations funds; ~3.6% / 2.195m shares) to CEO John Ions calling for an immediate strategic review with the objective of selling the business to the highest bidder'],
  ['23-Mar-2026', 'Liontrust board response: focused on “clear strategic objectives”; noted GAM had not sought dialogue beforehand and that it would welcome a discussion; cited the River Global acquisition'],
  ['10-Jul-2026', 'GAM Holding discloses 5.01% holding (TR-1); GAM release (14-Jul) cites continued engagement and deep undervaluation'],
  ['Jun–Sep 2026', 'Company actions: 74% dividend cut, FY26 executive variable pay cut to zero, 2026 LTIP capped; River completed; Gilbert joins board; Hawksmoor announced'],
  ['17-Sep-2026', 'AGM: remuneration report 81.3% for; CEO re-election 85.0% for'],
], [16, 84]));
k.push(P('**Central tenets of the activist case:** (1) valuation — shares −85% from Sept-2021 peak; AuM £42.3bn → ~£22bn; market value ~0.68% of AuM; (2) strategic failure — over-concentration in UK retail and ESG, small alternatives offering, no credible plan to reverse outflows; (3) governance/pay — CEO pay of ~£40m since 2010 against ~1m shares owned; loss of credibility; (4) solution — run a sale process given rapid sector consolidation.'));
k.push(P('**Success to date: partial.** No formal strategic review or sale process has been launched, and the board continues to pursue a buy-and-build strategy. However, pay outcomes were curtailed, dissent at the AGM was material (15–19%), the board added a consolidator, and the market-cap/AuM ratio has fallen further (0.58%), strengthening the case. Historical context: Liontrust was itself on the other side of an activist contest in 2023 when NewGAMe/Rock Investment (Xavier Niel) defeated Liontrust’s offer for GAM.'));
k.push(H2('14.2 Short interest'));
k.push(P('Short interest is low. The last named disclosure under the old UK regime was JPMorgan Asset Management (UK) at 0.69% (Feb-2026). Since 13-Jul-2026 the FCA publishes only aggregate net short positions (≥0.2% notifications, anonymised); no evidence of a material short campaign was found. Borrow is likely constrained by the retail-heavy register. No key short sellers identified.'));

// ---------------- 15 STRATEGIC ----------------
k.push(H1('15. Strategic initiatives (last 10 years)'));
k.push(table(['Initiative', 'Period', 'Status', 'Assessment'], [
  ['Acquisitive growth (ATI, Neptune, Architas, Majedie)', '2017–22', 'Completed', 'Scaled AuMA to ~£36bn; Majedie & Neptune value largely lost — mixed'],
  ['Sustainable investment leadership', '2017–present', 'Ongoing', 'Major success to 2021; reversed by ESG de-rating/SDR; AuMA ~£5.3–5.8bn'],
  ['International & institutional distribution (Lux/Irish UCITS; LatAm, Middle East, Australia, SA hires)', '2019–present', 'Ongoing', 'Early wins (mandates £250m+, >£500m gross Q to Jun-26) but revenue still ~99% UK'],
  ['GAM Holding takeover', '2023', 'Failed', 'Costly distraction; damaged credibility'],
  ['Transformation programme & new Capital Allocation Policy', '2025–26', 'Implemented', '~£6m savings; dividend re-based to ≥50% payout; buybacks'],
  ['£10m share buyback', 'Nov-25 – Jun-26', 'Completed (per plan)', 'Accretive at ~230–300p'],
  ['Liontrust ESG Trust plc (listed vehicle)', '2021–22', 'Discontinued (per FactSet record ends Sept-2022)', 'Did not achieve scale — verify'],
  ['River Global acquisition (value/income, European equities)', '2026', 'Integrating', 'Style diversification; expensive integration (£10.3m)'],
  ['Hawksmoor MPS/multi-asset acquisition', '2026', 'Completing 30-Nov-2026', 'Adds MPS scale; low price (0.3–0.5% AuM)'],
  ['Technology/AI and data-driven distribution', '2024–present', 'Ongoing', 'Supports efficiency; unquantified'],
], [34, 12, 18, 36]));

// ---------------- 16 STAKES ----------------
k.push(H1('16. Stakes held'));
k.push(P('Liontrust holds **no strategically significant stakes** in listed or unlisted companies. Its investments consist of seed/co-investment holdings in its own funds and units held to hedge deferred staff awards (amounts not retrieved; immaterial relative to cash). In 2023 it provided GAM Holding with a CHF 20m loan facility during its failed bid, subsequently replaced by Rock Investment financing. Contingent consideration rights relate to River (payable by Liontrust in shares) and Hawksmoor (payable in cash). Note: the interest in Parmenion (valued at £75–90m by River Global plc) stayed with River Global plc and was **not** acquired by Liontrust.'));

// ---------------- 17 DIVIDENDS ----------------
k.push(H1('17. Dividends, buybacks and treasury shares'));
k.push(table(['Fiscal year', 'Interim (p) / ex-date', 'Second interim/final (p) / ex-date', 'Total DPS (p)', 'Buyback cash (£m)', 'Shares in issue y/e (m)'], [
  ['FY21 (Mar-21)', '11 / 3-Dec-20', '36 / 1-Jul-21', '47', '0.8', '60.40'],
  ['FY22 (Mar-22)', '22 / 9-Dec-21', '50 / 30-Jun-22', '72', '5.0', '60.48'],
  ['FY23 (Mar-23)', '22 / 8-Dec-22', '50 / 29-Jun-23', '72', '7.1', '63.79 (Majedie shares)'],
  ['FY24 (Mar-24)', '22 / 23-Nov-23', '50 / 4-Jul-24', '72', '0.0', '63.91'],
  ['FY25 (Mar-25)', '22 / 28-Nov-24', '50 / 3-Jul-25', '72', '5.1', '62.74'],
  ['FY26 (Mar-26)', '7 / 27-Nov-25', '12 / 2-Jul-26', '19', '5.1 (£10m programme to Jun-26)', '60.61'],
  ['FY27 (Mar-27)', '7 / 26-Nov-26 (paid 6-Jan-27)', 'tbc (~Jul-27)', '≥50% of adj. EPS', '—', '+2.97m River shares (Jun-26)'],
], [14, 18, 20, 12, 18, 18]));
k.push(SRC('Source: FactSet corporate actions (cash dividends), FactSet Fundamentals (FF_STK_PURCH_CF; FF_COM_SHS_OUT), FactSet shares outstanding. Buyback cash may include Employee Benefit Trust purchases.'));
k.push(P('**Treasury shares and cancellations:** FactSet carries a treasury/own-shares balance of ~£1.1m (FF_TREAS_SHS, FY26), consistent with shares held by the EBT for employee awards rather than a large treasury holding. Shares in issue fell by ~1.2m in FY25 and ~2.1m in FY26, consistent with cancellation of repurchased shares; the River consideration (+2.97m) reversed this in FY27. Exact treasury counts and cancellation dates should be confirmed against the total-voting-rights RNSs, which could not be fetched in this session.'));

// ---------------- 18 BULL BEAR ----------------
k.push(H1('18. Bull vs bear — adversarial analysis'));
k.push(H2('18.1 Bull case'));
k.push(B('**Asymmetric valuation:** EV £96m for a £26bn franchise; a buyer needs only ~£25m of synergies to justify a 50%+ premium. Cash (~£44m) and a ~7–8% yield limit downside.'));
k.push(B('**Flow inflection:** organic decay slowed from ~18–22% to ~8% annualised; multi-asset in modest inflow; institutional pipeline converting. Positive flows on a fixed cost base would lift EPS sharply (each £1bn ≈ 5p).'));
k.push(B('**Secular tailwinds:** UK equity re-rating, cash-ISA reform (Apr-2027), and demand for diversification away from US mega-caps.'));
k.push(B('**Corporate catalyst:** activist (5%), consolidator on the board, peers being taken out at 1%+ of AuM; scale bolt-ons make Liontrust a more meaningful target.'));
k.push(B('**Capital allocation reset:** dividend now covered ~2x; buybacks at ~6x earnings are highly accretive.'));
k.push(H2('18.2 Bear case'));
k.push(B('**Structural impairment:** UK retail active equity is in secular decline; passive/MPS and DFM in-housing cap fees. Liontrust’s 50bp margin could fall toward 40bp.'));
k.push(B('**Key-person and style risk:** franchise value sits with a few teams (Economic Advantage, Sustainable); a departure could trigger multi-billion outflows.'));
k.push(B('**Value-destructive M&A:** management prefers to buy run-off books (River costs > price); integration consumes cash and attention, delaying a sale.'));
k.push(B('**Expectations still high:** consensus FY27–29E EPS (34.8p/41.4p/46.2p) assumes recovery; we are 7–17% below. Further misses (cf. H1 FY27) would push the stock lower before any bid.'));
k.push(H2('18.3 Pre-mortem (it is Nov-2028 and the investment lost 40%)'));
k.push(P('Net outflows persisted at ~£2bn p.a. as UK small caps lagged again; a senior Economic Advantage manager retired; River and Hawksmoor books shrank 30%; revenue margin fell to 44bp; EPS dropped to ~22p and the dividend was cut again; the board embarked on another acquisition funded by shares at the lows; the activist sold after failing to force a review; no bidder emerged because the franchise was perceived as melting. The shares de-rated to 5x P/E (~110–145p).'));
k.push(H2('18.4 Are multiples too high?'));
k.push(P('No — on headline multiples the stock is optically very cheap. The risk is not multiple compression but **earnings compression**: if the earnings base keeps shrinking 15–20% p.a., today’s 6.5x P/E is a 10x P/E on two-year-forward reality.'));
k.push(H2('18.5 Contrarian view: what the market refuses to see'));
k.push(P('The market values Liontrust as a melting ice cube run by management, but it is better viewed as a **cash-backed option on control**: (a) organic decay has more than halved; (b) the bolt-ons were bought at 0.3–0.5% of AuM — below Liontrust’s own valuation — making them accretive on paper even if they shrink; (c) the register is retail and activist-influenced, so a credible bid at a 50–70% premium would likely succeed; (d) the appointment of Martin Gilbert is a tell that the board’s optionality is widening. The H1 FY27 sell-off (−16% to an all-time low) was driven by non-cash, acquisition-related charges.'));

// ---------------- 19 SCENARIOS ----------------
k.push(H1('19. Scenario analysis (12–18 month view)'));
k.push(table(['Scenario', 'Prob.', 'Key assumptions', 'FY28E EPS', 'Multiple', 'Value/share', 'vs 225.5p'], [
  ['Bear — continued melt', '25%', 'Net outflows ~£2bn p.a.; margin 45bp; no bid; further dividend cut', '~24p', '6x P/E', '~145p', '−36%'],
  ['Base — stabilisation', '50%', 'Outflows ~£1bn FY28; margin 47bp; cost saves; 50% payout', '~38p', '7x P/E (≈1.0x EV/Sales regression)', '~265p', '+18%'],
  ['Bull — strategic sale / merger', '25%', 'Sale at ~0.75% of £26bn AuMA (~6x EBITDA pre-synergy)', 'n.a.', 'EV ~£195m + net cash', '~380p', '+68%'],
  ['**Probability-weighted**', '', '', '', '', '**~264p**', '**+17%** (+~7% yield)'],
], [18, 7, 33, 9, 15, 10, 8]));
k.push(P('**Sensitivity:** ±£1bn annual flows ≈ ±5p EPS ≈ ±35p/share at 7x; ±2bp revenue margin ≈ ±4p EPS. A 20–30% growth disappointment vs consensus (FY28E 41.4p → 29–33p) at 6–7x implies 175–230p — roughly today’s price, i.e., the current price already discounts a material miss.'));

// ---------------- 20 QUESTIONS ----------------
k.push(H1('20. Questions for the CEO / Chair (ordered by information value)'));
[
  'What is the board’s own estimate of Liontrust’s intrinsic value per share, and at what premium would it recommend an offer to shareholders?',
  'Has the board received any approach (formal or informal) in the past 24 months, and has it engaged financial advisers to evaluate strategic alternatives?',
  'What level of annual organic net flows is embedded in your medium-term plan, and in which year do you expect organic flows to turn positive?',
  'What is the IFPR own-funds surplus today, and how much distributable cash is available after Hawksmoor and contingent consideration?',
  'Why did River Global incur £10.3m of acquisition costs on an initial consideration of £7.6m, and what are the retention arrangements and expected synergies?',
  'What is the revenue margin trajectory by channel after River and Hawksmoor, and what is the floor?',
  'Which three teams generate the majority of profit, and what retention mechanisms (equity, LLP economics) lock in their key managers?',
  'How do you reconcile CEO cumulative pay (~£40m since 2010, per activist) with the 90% share-price decline, and will future LTIPs be tied to TSR versus a sale value?',
  'What is the succession plan for the CEO (16 years) and CFO (31 years)?',
  'Why is buying run-off books better for shareholders than returning capital or merging with a larger peer?',
  'What institutional pipeline (in £bn and expected funding dates) do you currently have, and what is the win rate?',
  'How does Martin Gilbert’s role as Executive Chair of River Global plc (a recipient of Liontrust shares) affect his independence?',
  'What was the cause of the FY26 collapse in Europe-attributed revenue (£10.6m → £0.6m)?',
  'What is the cost base after full integration, and what fixed-cost reduction would you implement if AuMA fell another 20%?',
  'Given the share price, would the board prioritise buybacks over further acquisitions, and is there a hurdle rate for M&A?',
].forEach(q => k.push(N(q)));

// ---------------- 21 DEVIL ----------------
k.push(H1('21. Devil’s advocate / forensic red-flag review'));
k.push(P('**What could structurally break the model?** A fee war led by platforms (in-house MPS, “best-buy” lists using passive) plus Consumer Duty value assessments could push UK retail active fees from ~70bp toward 40–50bp; Liontrust has no low-cost product line to absorb this. **Concentration:** ~99% UK revenue, majority UK retail via a handful of platforms; Hargreaves Lansdown (now PE-owned) and interactive investor (Aberdeen) are both distributors and competitors (own funds/MPS). **Most dangerous underestimated competitor:** the platforms themselves and DFM in-house MPS (e.g., Hargreaves, Quilter, Rathbones), followed by low-cost passive MPS (Vanguard). **Worst capital allocation:** Majedie at the 2022 peak (up to £120m, impaired within two years); maintaining 72p DPS through FY25 while cover fell below 1x and cash fell ~£80m; the GAM bid. **Single permanent-impairment scenario:** loss of the Economic Advantage team (the profit core) — plausibility low-to-moderate (~10–15% over 3 years) but devastating.'));
k.push(table(['Forensic check', 'Finding', 'Flag'], [
  ['1. Quality of earnings', 'Large gap between adjusted and statutory profit (FY26 adj. PBT ~£30.5m vs statutory £14.4m; H1 FY27 £11.9m vs −£4.2m); recurring “non-recurring” items (amortisation, acquisition, restructuring) every year', 'Amber–Red'],
  ['2. Reporting changes / restatements', 'Adjusted metric definitions stable; geographic revenue attribution shifted in FY26; no restatements found', 'Amber'],
  ['3. Opaque reporting', 'Single segment; no team-level revenue/profit or fund-performance P&L', 'Amber'],
  ['4. Organic growth transparency', 'Good: flows and AuMA reported quarterly by process; M&A AuMA separately identified', 'Green'],
  ['5. Selective disclosure', 'UK issuer (RNS, not 8-K); trading updates timely; H1 consensus not guided', 'Green'],
  ['6. Adversarial to criticism', 'Response to GAM letter noted lack of prior dialogue; no strategic review; IR frames buyback as proof of value', 'Amber'],
  ['7. Dividend vs FCF', 'FY25: 72p DPS (~£45m) vs OCF £20.6m; FY26 dividends ~£36m + buyback £5m vs OCF £14.6m; corrected by FY26 cut', 'Red (historic)'],
  ['8. Management quality', 'Long tenure, no succession; strong distribution skills; weak capital allocation post-2021', 'Amber'],
  ['9. Nomadic financiers / fads', 'ESG fad exposure (Sustainable flows reversed); acquisitions timed at cycle peak (Majedie)', 'Amber'],
  ['10. Related parties', 'Martin Gilbert (River Global plc Exec Chair) joined board on a deal where River Global plc received LIO shares and contingent consideration; LLP member arrangements for investment staff', 'Amber'],
  ['11. Regulatory risk', 'Consumer Duty value assessments, SDR labelling, FCA scrutiny of fees; IFPR capital limits', 'Amber'],
  ['12. Hidden liabilities', 'Contingent consideration (River ≤£2.1m shares; Hawksmoor ≤£4m); deferred staff/LLP awards; seed capital market risk; leases small', 'Green–Amber'],
  ['13. Terminally challenged balance sheet', 'No: no debt, net cash ~£44m; but tangible equity only ~£15m (Mar-26) — constrains cash M&A', 'Green'],
  ['Revenue recognition', 'Management fees accrue on NAV daily — low risk; performance fees immaterial', 'Green'],
  ['Leases', 'Lease liabilities £2.7m (London HQ, 2 Savoy Court)', 'Green'],
  ['Stock-based comp', 'LTIP/DBVA awards and EBT purchases; 2026 CEO LTIP 566,203 nil-cost options; dilution ~1–1.5% p.a. incl. staff', 'Amber'],
  ['Goodwill / intangibles', 'Goodwill £32.1m + intangibles £61.3m = 87% of equity; outflow-based impairment trigger (≥10% of AuMA) remains live; River/Hawksmoor add more', 'Red'],
  ['Cash-flow statement', 'FactSet free cash flow negative in FY23–26 (classification of investment/seed purchases); OCF down 84% FY22→FY26', 'Amber'],
], [24, 62, 14]));
k.push(P('**What must hold for today’s price to be justified?** Very little: at 225.5p the market implies ~6x our FY28E EPS of 38p with no credit for cash; the price is justified even if flows stay mildly negative, provided the revenue margin stabilises ~45–47bp and no key team leaves. **If growth disappoints by 20–30%** vs consensus, fair value is ~175–230p (Section 19) — limited downside versus current price, which is why the risk/reward is skewed positively despite the many red flags.'));

// ---------------- 22 TIMELINE ----------------
k.push(H1('22. Timeline and catalyst calendar'));
k.push(H2('22.1 Key past events'));
k.push(table(['Date', 'Event'], [
  ['Feb-2010', 'John Ions becomes CEO'],
  ['Apr-2017', 'Alliance Trust Investments acquired (Sustainable Investment team)'],
  ['Oct-2019', 'Neptune acquired'],
  ['2020–21', 'Architas UK multi-asset acquired'],
  ['Dec-2021', 'Share price peaks at 2,325p'],
  ['Jan/Apr-2022', 'Majedie announced/completed'],
  ['May–Aug-2023', 'GAM Holding offer launched and fails'],
  ['FY24', 'Majedie intangibles impaired; statutory net loss'],
  ['Sep-2024', 'Luke Savage becomes Chair'],
  ['Jun-2025', 'New Capital Allocation Policy (≥50% payout)'],
  ['Nov-2025', 'Interim dividend cut to 7p; £10m buyback'],
  ['16/23-Mar-2026', 'River Global deal announced; GAM open letter'],
  ['24-Jun-2026', 'FY26 results: DPS cut to 19p'],
  ['30-Jun/1-Jul-2026', 'River completed; Martin Gilbert joins board'],
  ['10-Jul-2026', 'GAM crosses 5%'],
  ['17-Sep-2026', 'AGM: 81% for remuneration report'],
  ['30-Sep-2026', 'Hawksmoor acquisition announced'],
  ['1-Oct-2026', 'Nuveen completes Schroders take-private (sector read-across)'],
  ['19-Nov-2026', 'H1 FY27 results: statutory loss'],
], [20, 80]));
k.push(H2('22.2 Upcoming catalysts'));
k.push(table(['Date (expected)', 'Event', 'Why it matters'], [
  ['30-Nov-2026', 'Hawksmoor completion (+~£1.9bn AuMA)', 'AuMA ~£26bn; first MPS scale step'],
  ['6-Jan-2027', 'Payment of 7p interim dividend', 'Income support'],
  ['20-Jan-2027', 'Q3 FY27 trading update (FactSet confirmed)', 'Flow trend post-River/Hawksmoor'],
  ['Apr-2027', 'UK cash-ISA allowance reduction takes effect', 'Potential flow tailwind for equity funds'],
  ['21-Apr-2027', 'Q4 FY27 trading update', 'Full-year flows; AuMA'],
  ['23-Jun-2027', 'FY27 results (FactSet confirmed)', 'Second interim dividend; FY28 outlook; impairment review'],
  ['~30-Jun-2027', 'River contingent consideration test (12 months)', 'Indicator of acquired-book retention'],
  ['21-Jul-2027', 'Q1 FY28 trading update', 'Flows'],
  ['~Sep-2027', 'AGM', 'Shareholder vote on pay/directors — activist leverage point'],
  ['20-Oct-2027', 'Q2 FY28 trading update', 'Flows'],
  ['18-Nov-2027', 'H1 FY28 results (FactSet confirmed)', ''],
  ['~Nov-2027', 'Hawksmoor first contingent payment test', 'Retention of MPS revenue'],
  ['Ongoing', 'Activist engagement; potential strategic review / approaches; sector M&A', 'Primary re-rating catalyst'],
], [16, 44, 40]));
k.push(SRC('Source: FactSet CalendarEvents (earnings and trading-update dates), company announcements.'));

// ---------------- 23 AUDIT ----------------
k.push(H1('23. Data audit trail and limitations'));
k.push(H2('23.1 FactSet audit records'));
[
  'Daily/monthly prices (LIO): https://my.apps.factset.com/mcp-audit-table/47ea1d7f-f4cf-48bd-ada7-bd8143c63a8b',
  'Market value (LIO): https://my.apps.factset.com/mcp-audit-table/650f4712-fd45-4658-9e30-292448d0c661',
  'Consensus EPS FY26–FY29: https://my.apps.factset.com/mcp-audit-table/6adb0039-898b-4f1a-aa57-e3b47232f480',
  'Consensus sales: https://my.apps.factset.com/mcp-audit-table/c6471710-e99b-4f3f-abff-194bf632bd42',
  'Peer consensus EPS: https://my.apps.factset.com/mcp-audit-table/7353bee8-e116-4ad0-b35f-976aadd3a5b7',
  'Peer consensus EBIT: https://my.apps.factset.com/mcp-audit-table/5162442d-4e47-4403-9e94-8effa7f7ab02',
  'Peer consensus sales: https://my.apps.factset.com/mcp-audit-table/0d8c63b6-0806-480e-9158-73551aafe94d',
  'Peer market values: https://my.apps.factset.com/mcp-audit-table/7686f78d-45ae-43d8-9952-4527943b5aa0',
  'Ownership (top holders): https://my.apps.factset.com/mcp-audit-table/9139ec3f-e39a-44e4-8e9d-55460bda4696',
  'Officers & directors: https://my.apps.factset.com/mcp-audit-table/15644cbf-4b9d-4c41-b9ca-4a185474d776',
  'Director career histories: https://my.apps.factset.com/mcp-audit-table/c7f61101-c0f7-44ba-a99e-d10af2cd8c02',
  'Dividends (corporate actions): https://my.apps.factset.com/mcp-audit-table/2b338319-5112-42e6-8fc7-b9ea4dfe8c83',
  'Shares outstanding: https://my.apps.factset.com/mcp-audit-table/651b51ce-fc51-4c28-9743-177d62013d76',
  'Price target consensus: https://my.apps.factset.com/mcp-audit-table/281f48d5-ac2c-4e40-8714-f990b1ba434a',
  'FY27 EPS consensus history: https://my.apps.factset.com/mcp-audit-table/89008cf5-2ef1-4790-9feb-da20022a6070',
  'Earnings calendar: https://my.apps.factset.com/mcp-audit-table/11852e4b-3538-472b-8fd4-c0605e2aa724',
  'Fundamentals: per-datapoint FactSet audit cards (FF_* formulas, e.g. FF_SALES(ANN,…,GBP)) retrieved with AUDIT_CARD.',
].forEach(t => k.push(B(t)));
k.push(H2('23.2 Limitations'));
[
  'Primary filings could not be opened directly: company PDFs (liontrust sitecorecloud), Investegate, TradingView/Reuters RNS, GlobeNewswire and several trade-press sites were blocked by the session’s network policy. Company-reported figures (adjusted PBT/EPS, gross profit, flows, AuMA) were taken from FactSet StreetAccount, CallStreet transcripts and press/search summaries.',
  'H1 FY27 balance sheet (cash at 30-Sep-2026), IFPR capital surplus, team-level AuMA (except Sustainable and Multi-Asset), fund-performance quartiles, headcount and the 2026 single-figure remuneration were not retrieved.',
  'Liontrust discloses a single segment; divisional revenue/EBITDA/EBIT/net income do not exist in public data.',
  'FactSet “revenue” (£134.4m FY26) differs from company gross profit (£123.0m) because of cost-of-sales treatment; FactSet free cash flow is negative FY23–26 due to classification of investment purchases — OCF used instead.',
  'FactSet ownership includes a 5.24% holding attributed to “Lamprell plc” (likely a mapping error) and a stale Canaccord position (May-2025).',
  'Peer EVs use latest fiscal-year balance sheets (different year-ends); Man Group converted at an implied USD/GBP 1.311; Rathbones balance-sheet cash excluded; Ashmore excluded from the regression.',
  'H1 FY27 consensus was not available in FactSet; the “miss” is measured against the pre-results FY27E run-rate.',
  'Several historical transaction values (pre-2023 Liontrust deals, BNP/AXA IM, RBC/Brewin, Mattioli Woods, Hargreaves Lansdown) and some former NED names are from public reporting/memory and marked “approx.”/“verify”.',
  'Projections, scenario values and sentiment scores are analyst estimates, not company guidance.',
].forEach(t => k.push(B(t)));

const document = doc(k, 'Liontrust Asset Management PLC (LIO LN) — Equity Research, 27 Nov 2026');
Packer.toBuffer(document).then(buf => { fs.writeFileSync('Liontrust_LIO_Equity_Research_Nov2026.docx', buf); console.log('written'); });
