const fs = require('fs');
const { P, H1, H2, H3, B, N, SRC, BR, img, table, SP, doc, d, FONT } = require('./lib');
const { Paragraph, TextRun, Packer } = d;
const C = 'charts/';
const SP_ = '/tmp/claude-0/-home-user-RF-Stuff/0d9de77d-b330-5dee-8336-04e1e971011c/scratchpad/';
const peers = JSON.parse(fs.readFileSync(SP_ + 'peer_rows.json'));
const reg = JSON.parse(fs.readFileSync(SP_ + 'reg_data.json'));
const f1 = (x) => (x === null || x === undefined) ? 'n.m.' : x.toFixed(1);
const fx = (x) => (x === null || x === undefined || x < 0) ? 'n.m.' : x.toFixed(1) + 'x';
const k = [];

// ---------------- COVER ----------------
k.push(new Paragraph({ style: 'Title', children: [new TextRun({ text: 'Impax Asset Management Group plc (IPX LN)', font: FONT })] }));
k.push(P('**Institutional equity research — deep dive, special-situations lens**', { run: { size: 24, color: '2E5597' } }));
k.push(P('Report date: 27 November 2026  |  Price: 89.3p (close 26-Nov-2026)  |  Market: AIM  |  Sector: specialist sustainable/transition asset management'));
k.push(table(['Market data', 'Value', 'Valuation (FactSet consensus)', 'Value'], [
  ['Share price / 52-wk range', '89.3p / 78.8p–173.8p', 'P/E FY26A adj. / FY27E / FY28E', '7.3x / 9.3x / 7.3x'],
  ['Market cap (FactSet)', '£108.5m', 'P/E FY27E ex-net cash', '~4.0x'],
  ['Net cash (Sep-26, FactSet; co. “cash reserves” £63.8m)', '~£62m (57% of mkt cap)', 'EV / EBIT FY27E', '3.3x'],
  ['Enterprise value', '~£46m', 'EV / Sales FY27E', '0.47x'],
  ['AUM (30-Sep-2026)', '£20.05bn', 'Mkt cap / AUM (EV / AUM)', '0.54% (0.23%)'],
  ['Shares (approx.)', '~121.5m', 'Dividend yield (FY26 DPS 6.7p)', '7.5%'],
  ['Peak-to-current (Dec-21 → now)', '1,482p → 89.3p (−94%)', 'Consensus target / ratings', '152p mean (95–200p); 3 Buy, 1 Hold'],
], [30, 20, 28, 22]));
k.push(SRC('Source: FactSet Global Prices, Fundamentals (FY26 preliminary), EstimatesConsensus (accessed 27-Nov-2026); Impax FY26 results (25-Nov-2026) via StreetAccount and CallStreet transcript.'));

k.push(H2('Investment summary'));
k.push(P('**View: cash-backed deep value with operating leverage and a latent strategic option — Accumulate. Base value ~110p (+23%); strategic value ~165p (+85%); bear ~70p (−22%). Probability-weighted ~112p (+25%), plus a ~7.5% yield.**'));
k.push(B('**What it is:** the world’s best-known listed specialist in “transition to a more sustainable economy” investing (founded 1998 by CEO Ian Simm). AUM £20.05bn, ~75% in listed equities (thematic and systematic), plus fixed income and private-markets infrastructure. Distribution is global: North America (ex-Pax World), BNP Paribas AM (a 14.4% shareholder and distribution partner), Europe and the UK.'));
k.push(B('**What went wrong:** AUM has halved from a £40.1bn peak (Mar-2023). FY25 lost £13.0bn of net flows including the St James’s Place mandate (£6.2bn); FY26 lost a further £7.8bn including most of the Impax Environmental Markets trust after Saba Capital’s attack. Revenue fell from £181m (FY23) to £113m; adjusted operating margin from >30% to ~15%; DPS from 27.6p to 6.7p; the share price fell 94%.'));
k.push(B('**Why now:** (1) the cost base has been reset (run-rate £86.5m vs £108m in FY25) and management says restructuring is complete; (2) investment performance has turned sharply in 2026 as market leadership broadened (energy security, resilience); (3) FY26 beat consensus (adj. EPS 12.2p vs 11.0p) and FY27 revenue guidance of £100–103m is above consensus (£98.7m); (4) net cash of ~£62m is 57% of market cap — the operating business trades at ~£46m, or 0.23% of AUM.'));
k.push(B('**Valuation:** cheapest UK listed manager on EV/AUM. EV/AUM-vs-E/AUM regression (R² 0.69) implies ~110p; PBR-vs-ROE regression (R² 0.94) says fair (~87–97p); TEV/Sales-vs-margin says the market gives zero value to operations at today’s depressed 14% margin — i.e., the upside depends on margin recovery, which is now in management’s hands via operating leverage.'));
k.push(B('**Ownership and event path:** ~50% of shares sit with four holders — BNP Paribas AM 14.4%, Liontrust funds 10.7%, Ian Simm 7.5% (management ~18% collectively), the EBT 5.1%. GAM special-situations funds disclosed ~2.2% (Jul-2026) citing deep undervaluation. BNPP is the natural acquirer; management has said it is not interested in merging or being acquired (May-2025).'));
k.push(B('**Key risks:** continued outflows (structural ESG backlash, US politics), concentration on BNPP distribution, founder key-person risk, related-party governance (BNPP nominee on board), and the possibility that management uses the cash pile for acquisitions rather than returns.'));
k.push(P('**Disclosure:** funds managed by GAM Investments’ special-situations team hold ~2.2% of Impax (StreetAccount, 14-Jul-2026). Readers should weigh this accordingly; limitations are listed in Section 23.', { run: { italics: true, size: 17 } }));

k.push(H2('Layman’s guide: what Impax does and how it makes money'));
k.push(P('Impax is a fund manager that invests other people’s money in companies and assets that benefit from the shift to a cleaner, more resource-efficient economy — water utilities, energy-efficiency technology, grid and power equipment, recycling, sustainable food, and similar. Clients are mainly pension funds, insurers and wealth managers around the world, plus retail investors via US mutual funds and BNP Paribas’ fund range.'));
k.push(P('Impax charges an annual fee of about **0.48% of assets** (£4.80 per £1,000). Revenue therefore depends on how much money clients have with Impax (flows), how its markets perform, and the fee rate. Most costs are staff, so when assets fall profits fall much faster — and when assets rise, profits rebound quickly (management targets a 30% margin at £27–28bn of AUM).'));
k.push(table(['Division (company-reported)', 'What it does', 'FY25 revenue', 'Contribution'], [
  ['Listed Equities', 'Thematic “transition” strategies (Leaders, Water, Specialists, Climate, Sustainable Infrastructure), US Pax funds, and systematic (lower tracking error) equity', '£124.4m (88%)', 'Core profit engine; ~75% of AUM; systematic rising to 13% of AUM'],
  ['Fixed Income', 'Sustainable/transition credit incl. high yield (ex-Absalon, ex-SKY Harbor teams)', '£8.0m (6%)', 'Growth/diversification area; first significant credit mandate won Q2 FY26'],
  ['Private Markets', 'New Energy infrastructure funds (renewables, storage, EV charging)', '£9.5m (7%)', 'Long-dated, sticky fees; small; timing-dependent'],
], [20, 46, 14, 20]));
k.push(SRC('Source: FactSet segments (BUS SALES, FY25 — latest available); company presentations. Segment operating profit is not disclosed.'));
k.push(H2('Contents'));
k.push(P('1. Stock price history & catalysts · 2. Business model · 3. Macro influences · 4. Competitive position & moats · 5. Supply chain map · 6. KPIs & segment metrics · 7. Recent earnings & sentiment · 8. Forward EPS · 9. Capital structure · 10. Valuation, peers & regressions · 11. M&A · 12. Management · 13. Board · 14. Shareholders, activism & short interest · 15. Strategic initiatives · 16. Stakes held · 17. Dividends & buybacks · 18. Bull vs bear · 19. Scenarios · 20. Management questions · 21. Devil’s advocate / red flags · 22. Timeline & catalysts · 23. Audit trail & limitations', { run: { size: 17 } }));
k.push(BR());

// ---------------- 1 ----------------
k.push(H1('1. Stock price history and catalysts (5 years)'));
k.push(img(C + 'price.png', 7.0, 3.3));
k.push(P('Impax was a 2020–21 ESG “winner” trading at >40x earnings at its 1,482p peak (9-Dec-2021). Five years later it trades at 89.3p (−94%). The fall has three drivers: (i) de-rating from growth multiple to value multiple (2022–23, rising rates); (ii) the end of the ESG flow cycle, US anti-ESG politics and narrow, mega-cap-led markets in which Impax’s strategies lagged (2023–25); (iii) specific client losses — St James’s Place (Dec-2024) and the Impax Environmental Markets exit tender forced by Saba Capital (Apr-2026).'));
k.push(table(['#', 'Date', 'Move', 'Catalyst'], [
  ['1', '9 Dec 2021', 'Peak 1,482p', 'FY21 results (record AUM ~£37bn, net inflows); ESG peak'],
  ['–', 'Jan–Jun 2022', '−16% (5d, Jan); −20% (5d, Mar & Jun)', 'Rates shock and growth/ESG de-rating; Ukraine war'],
  ['2', '8 Mar 2022', '−8%, then +12% (9 Mar)', 'Ukraine sell-off and rebound'],
  ['–', 'Oct–Nov 2022', '+17% to +24% (5d)', 'Post mini-budget and US CPI relief rally'],
  ['3', '6 Dec 2022', '−12.3% (1d)', 'FY22 results: outflows and cautious outlook'],
  ['4', '13 Mar 2023', '−10.8% (1d)', 'SVB/banking stress sell-off'],
  ['–', '31 May–6 Jun 2023', '−19% (5d)', 'H1 FY23 results: profit decline, flows softening'],
  ['5', '9 Oct 2023', '−12.4% (1d)', 'Q4 FY23 AUM update: AUM −5.8% q/q to £37.4bn'],
  ['6', '29 May 2024', '−14.7% (1d), −19% (5d)', 'H1 FY24 results: lower profits, net outflows'],
  ['7', '10 Jul 2024', '−10.8% (1d)', 'Q3 FY24 AUM update: outflows'],
  ['8', '13–19 Dec 2024', '−23.1% (1d), −30% (5d)', 'St James’s Place terminates the large Sustainable & Responsible Equity mandate (~£6.2bn, effective Feb-2025), following Oct-2024 loss of a smaller £774m mandate'],
  ['–', 'Jan–Feb 2025', '−15% to −18% (5d)', 'Q1 FY25 outflows; US anti-ESG executive actions'],
  ['9', '4–9 Apr 2025', '−19.8% (1d), −34% (5d)', 'US tariff shock plus Q2 FY25 AUM update'],
  ['10', '22 May 2025', '+8.3%; +19% (5d to 13 May)', 'H1 FY25 results with £10m buyback launched'],
  ['11', '1–3 Dec 2025', '−10.0% (1d), −16% (5d)', 'FY25 results: net outflows £13.0bn; DPS cut to 12.0p (from 27.6p)'],
  ['12', '10 Apr 2026', '−25.1% (1d)', 'Q2 FY26 AUM £22.3bn; IEM exit tender to cost most of trust assets; revenue guidance £109–113m; further cost cuts'],
  ['13', '10–16 Jul 2026', '+21.1% (1d), +23% (5d)', 'Q3 AUM £23.3bn (+4% q/q) on strong performance; GAM funds disclose ~2.2% stake (14 Jul)'],
  ['14', '13 Oct 2026', '−9.4% (1d)', 'Q4 AUM £20.05bn (−14% q/q): IEM exit and outflows'],
  ['15', '25 Nov 2026', '+9.6% (1d)', 'FY26 results beat (adj. EPS 12.2p vs 11.0p); FY27 revenue guidance £100–103m; cost reset complete'],
], [4, 16, 22, 58]));
k.push(SRC('Source: FactSet daily prices (computed moves); StreetAccount; CallStreet transcripts; press. 5-day moves shown where a single-day move was below 10%.'));

// ---------------- 2 ----------------
k.push(H1('2. Business model'));
k.push(P('Revenue ≈ average AUM × average fee margin (48bp in FY26) + small performance/carry income in private markets. FY26 revenue £113.1m on average AUM of ~£23bn (down from ~£39bn two years earlier). Costs £96m in FY26 (from £108m), with an exit run-rate of £86.5m after a 30-head reduction; FY27 costs guided +1–2%. At the Sep-26 run-rate (£20bn AUM) revenue would be ~£96m; management guides £100–103m for FY27 on performance-led recovery.'));
k.push(table(['Driver', 'Mechanism', 'Current direction'], [
  ['Volume (AUM)', 'Institutional mandates, BNPP-distributed funds, US mutual funds, UK/EU wholesale', 'Outflows slowing (Q1 FY27 “considerably” slower per mgmt), not yet positive'],
  ['Pricing (fee margin)', 'Thematic equity 50–70bp; systematic/fixed income lower; sub-advisory lower', '48bp, “resilient” — mix shift to systematic and credit is dilutive'],
  ['Performance', 'Thematic transition strategies vs MSCI ACWI', 'Strong 2026 outperformance after 2023–25 lag; flows typically lag performance 12–24 months'],
  ['Regulation/politics', 'SFDR/SDR labels, US anti-ESG laws, EU taxonomy', 'Headwind in US; supportive in Europe/Asia; energy-security framing helps'],
  ['Cost base', '~70% staff; deferred/variable comp; EBT purchases', 'Reset; operating leverage now high'],
  ['Capital', 'Seed capital (£8.6m), acquisitions, buybacks', 'Cash £63.8m; dividend policy 55% of adj. profit after tax'],
], [18, 44, 38]));
k.push(B('**Customers:** institutional asset owners (Europe, North America, Asia-Pacific), wealth managers, retail via BNPP AM, US mutual funds (Impax Funds, ex-Pax World) and UCITS on platforms. UK share of AUM fell from 7% to 2% after IEM.'));
k.push(B('**Suppliers:** talent, sustainability/market data (MSCI, ISS, Bloomberg, FactSet), administrators/custodians, brokers. **Competitors:** Pictet (thematic), BNPP AM (also a partner), Nordea, Candriam, Schroders/Nuveen, Jupiter, Liontrust Sustainable, WHEB, Calvert (Morgan Stanley), Parnassus (AMG), passive ESG ETFs.'));
k.push(B('**Geographies (revenue by client domicile, FY25):** North America £48.9m (34%), Luxembourg £32.9m (23% — BNPP funds), UK £19.7m (14%), France £12.3m (9%), Ireland £11.4m (8%), Canada £6.5m, Australia £3.6m, Netherlands £3.3m, other £3.2m.'));
k.push(B('**Contracts/terms:** management fees accrue daily on NAV, paid monthly/quarterly; segregated mandates terminable at short notice (SJP termination took ~2 months); BNPP sub-advisory fee paid quarterly as % of AUM (related-party agreement, Apr-2025); private-equity funds earn committed-capital fees over 10+ years.'));

// ---------------- 3 ----------------
k.push(H1('3. Macro and micro influences'));
k.push(table(['Tailwinds', 'Headwinds'], [
  ['Broadening equity markets after mega-cap concentration; Impax’s mid-cap industrial/utility exposure outperforms', 'US political hostility to ESG; offshore-wind and IRA policy reversals'],
  ['Energy-security investment (grids, efficiency, storage) re-framed as economic, not ethical', 'Persistently high inflation and rates (management cites) pressure long-duration growth stocks'],
  ['Competitors retreating from sustainability (thinner tender fields; mandates being re-tendered)', 'Shift to passive/systematic; fee compression'],
  ['Large asset owners seeking strategic partners (8–10 discussions under way)', 'Distribution concentration (BNPP); wholesale flows volatile'],
  ['Private infrastructure demand (power for data centres)', 'Investment-trust activism (Saba) and discount pressure'],
], [50, 50]));
k.push(P('**Net:** for the first time since 2021, macro (market broadening, energy security) is a tailwind; the main headwinds are political and structural (ESG label stigma, passive).'));

// ---------------- 4 ----------------
k.push(H1('4. Competitive position and moats'));
k.push(P('Impax has the longest track record (since 1998) and arguably the strongest brand in transition-themed investing, a 17-person sustainability centre and a distinctive, research-heavy process. Its positioning (“making money, not saving the world”) differentiates it from generalists that blurred fiduciary and ethical aims. The weakness is that the theme is cyclical and politically exposed, and brand strength has not prevented £20bn of outflows.'));
k.push(table(['Moat category', 'Rating', 'Assessment'], [
  ['Brand', 'Moderate–Strong (niche)', 'Global leader in transition investing; strong with European institutions and BNPP network'],
  ['Hard assets', 'None', 'Asset-light'],
  ['Long-term contracts', 'Weak (listed) / Moderate (private)', 'Listed mandates terminable; PE funds 10-year committed capital'],
  ['Network effect', 'None', '—'],
  ['Regulatory & switching costs', 'Weak–Moderate', 'Institutional re-tendering is slow (inertia) but not a barrier'],
  ['Oligopolistic industry', 'No', 'Fragmented; specialist niche with fewer serious competitors after 2023–25 retreat'],
  ['Cash-flow predictability', 'Low', 'Revenue −38% FY23→FY26'],
  ['Scalability', 'High', '30% margin target at £27–28bn; listed equities already scaled'],
  ['Government interference', 'Moderate–High', 'US anti-ESG laws, EU labelling regimes'],
  ['Bargaining power', 'Weak', 'Large clients (SJP, BNPP) hold power — demonstrated by SJP exit'],
], [22, 22, 56]));
k.push(P('**Conclusion:** a narrow, brand-based niche advantage — real but not durable against cyclical flows. Its most valuable assets are the brand, the process and the BNPP relationship — all attractive to a strategic acquirer.'));

// ---------------- 5 ----------------
k.push(H1('5. Supply chain / value chain map'));
k.push(img(C + 'supply.png', 6.9, 4.85));
k.push(P('Impax sits in the middle (manufacturer) of the chain. Its distribution is unusually dependent on one strategic partner (BNP Paribas AM — also its largest shareholder and a competitor), and on a handful of large institutional/wealth clients. Service-provider names marked “verify” are illustrative and were not re-checked against fund documents in this session.'));

// ---------------- 6 ----------------
k.push(H1('6. Financial KPIs and segment metrics'));
k.push(table(['£m (FY to 30 Sep)', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26'], [
  ['Revenue (FactSet)', '175.9', '181.2', '173.4', '144.7', '114.8'],
  ['  growth y/y', '+23.3%', '+3.0%', '−4.3%', '−16.5%', '−20.7%'],
  ['EBITDA', '70.1', '62.5', '58.6', '38.5', '20.9'],
  ['  margin', '39.9%', '34.5%', '33.8%', '26.6%', '18.2%'],
  ['EBIT (operating income)', '65.9', '57.4', '54.0', '33.4', '15.5'],
  ['  margin', '37.4%', '31.7%', '31.1%', '23.1%', '13.5%'],
  ['Net income', '59.5', '39.2', '36.5', '20.3', '10.0'],
  ['Diluted EPS (p)', '44.7', '29.8', '28.2', '15.8', '8.2'],
  ['Adj. EPS (p; FY26 company)', '44.7', '29.8', '28.8', '18.0', '12.2'],
  ['Company adj. operating profit', 'n.a.', 'n.a.', 'n.a.', 'n.a.', '16.6'],
  ['DPS (p)', '27.6', '27.6', '27.6', '12.0', '6.7'],
  ['Operating cash flow', '71.7', '41.4', '53.9', '26.7', '16.9'],
  ['ROE', '47.8%', '28.8%', '27.5%', '16.5%', '9.0%'],
  ['Cash (FactSet)', '118.2', '104.8', '109.1', '80.3', '70.9'],
], [32, 13, 13, 13, 13, 16]));
k.push(SRC('Source: FactSet Fundamentals (FY26 preliminary); company FY26 results (revenue £113.1m, adj. operating profit £16.6m, adj. EPS 12.2p). FY21: revenue £142.7m, EBIT £47.9m.'));
k.push(img(C + 'fin.png', 7.0, 2.7));
k.push(H2('Segments'));
k.push(table(['Revenue £m', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25'], [
  ['North America', '50.6', '61.9', '54.2', '53.8', '48.9'],
  ['Luxembourg (BNPP funds)', '35.4', '43.4', '49.4', '42.4', '32.9'],
  ['United Kingdom', '26.7', '34.1', '30.7', '30.8', '19.7'],
  ['France', '12.7', '12.3', '11.1', '11.4', '12.3'],
  ['Ireland', '9.4', '13.2', '13.3', '13.4', '11.4'],
  ['Canada / Australia / NL / DK / other', '8.2', '10.6', '19.7', '18.3', '16.6'],
  ['Business segments FY25: Listed Equities / Fixed Income / Private Markets', '—', '—', '—', '—', '124.4 / 8.0 / 9.5'],
], [36, 12, 12, 12, 12, 16]));
k.push(SRC('Source: FactSet segments (GEO and BUS SALES). FY26 segment data not yet in FactSet. Segment profit not disclosed; definitions company-specific.'));
k.push(P('**Trends:** revenue grew strongly to FY23 on AUM of £37–40bn, then fell 38% as AUM halved. Luxembourg (BNPP) and UK revenues fell fastest (SJP, IEM); North America proved stickier. Margins compressed from ~37% EBIT (FY22) to ~14% (FY26), with H2 FY26 adjusted operating margin only ~10% (H1 £11.3m on £58.8m; H2 ~£5.3m on ~£54.3m) — the trough. The cost reset (run-rate £86.5m vs revenue guidance £100–103m) implies FY27 operating margin of ~12–15% before any flow recovery.'));
k.push(img(C + 'aum.png', 7.0, 2.5));
k.push(table(['KPI', 'FY24', 'FY25', 'FY26', 'Trend'], [
  ['Closing AUM (£bn)', '37.2', '26.1', '20.05', 'Down 46% in two years'],
  ['Net flows (£bn)', 'negative (n.d.)', '(13.0)', '(7.8)', 'Improving; H2 FY26 outflows £5.3bn vs inflows £1.2bn'],
  ['Average fee margin', 'n.a.', 'n.a.', '48bp', '“Resilient”; systematic share 8% → 13%'],
  ['Cost base (£m)', 'n.a.', '108', '96 (run-rate 86.5)', 'Reset complete; FY27 +1–2%'],
  ['Adj. operating margin', '~31%', '~23%', '~15%', 'Target ≥30% at £27–28bn AUM'],
  ['Headcount', 'n.a.', 'n.a.', '−30 heads in FY26', 'Restructured'],
  ['Cash reserves (co.)', 'n.a.', '~£60m', '£63.8m', 'Stable despite dividend + £10m buyback'],
  ['Seed capital', 'n.a.', 'n.a.', '£8.6m', 'Selective'],
], [22, 14, 14, 18, 32]));

// ---------------- 7 ----------------
k.push(H1('7. Recent earnings and management sentiment'));
k.push(H2('7.1 FY26 results (year to 30-Sep-2026, reported 25-Nov-2026)'));
k.push(table(['Metric', 'Actual', 'Consensus', 'Surprise', 'Prior year'], [
  ['Revenue', '£113.1m', '£111.8m (5 est.)', '+1.2%', '~£144m'],
  ['Adj. operating profit', '£16.6m', '£16.3m', '+1.8%', 'n.a.'],
  ['Adj. EPS', '12.2p', '11.0p (10.7–11.2p)', '+11%', '18.0p'],
  ['Net flows', '£(7.8)bn', '—', '', '£(13.0)bn'],
  ['DPS (total)', '6.7p (2.0 + 4.7 final)', '—', '', '12.0p'],
  ['Closing AUM', '£20.05bn', 'in line', '', '£26.1bn'],
  ['Cash reserves', '£63.8m', '', '', '~£60m'],
], [20, 20, 22, 12, 26]));
k.push(P('**Drivers:** performance recovery added ~£9m to the revenue bridge; average AUM fell from ~£39bn to ~£23bn over two years. **Margins:** costs fell from £108m to £96m; exit run-rate £86.5m. **Guidance/tone:** FY27 revenue £100–103m (vs FY27 consensus £98.7m — an upgrade); costs +1–2%; “restructuring broadly finished… focus shifts to a phase of growth”; 8–10 strategic-partnership discussions; ≥30% margin achievable at £27–28bn AUM. Q1 FY27 outflows “slowed considerably”. **Balance sheet:** no debt; £63.8m cash after dividends and the £10m buyback; healthy regulatory surplus; seed £8.6m. **Market reaction:** +9.6% on the day (from an all-time low of 78.8p on 20-Nov) — relief that the trough was confirmed and guidance beat; still below the 101p seen before the Q4 AUM update. **Unusual:** H2 FY26 margin ~10%; UK AUM share collapse (7% → 2%) from IEM.'));
k.push(H2('7.2 Sentiment trajectory'));
k.push(table(['Event', 'Management focus', 'Sentiment'], [
  ['H1 FY25 (22/29-May-2025)', 'Political pressures; buyback; M&A in fixed income/private assets; “no interest in merging or being acquired”', 'Defensive (2/5)'],
  ['FY25 (1/3-Dec-2025)', '“Unusual, narrow market”; outflows moderating; compelling valuations; SKY Harbor closed; DPS cut', 'Cautious (2/5)'],
  ['Q2 AUM (10-Apr-2026)', 'IEM exit tender loss; revenue guidance £109–113m; further efficiency', 'Negative (1.5/5)'],
  ['H1 FY26 (20/27-May-2026)', 'Performance turnaround; “flows lag performance”; costs −£8m; management owns ~18%', 'Cautiously optimistic (2.5/5)'],
  ['FY26 (25-Nov-2026)', 'Restructuring complete; phase of growth; competitors retreating; partnerships; 30% margin path', 'Constructive (3.5/5)'],
], [22, 58, 20]));
k.push(SRC('Source: FactSet CallStreet transcripts (1/3-Dec-2025; 20/27-May-2026; 25-Nov-2026), StreetAccount Transcript Intelligence. Sentiment scores are analyst judgement.'));

// ---------------- 8 ----------------
k.push(H1('8. Forward EPS projections (FY27E–FY29E, year to September)'));
k.push(table(['', 'FY26A', 'FY27E', 'FY28E', 'FY29E', 'Consensus FY27/28/29'], [
  ['Average AUM (£bn)', '~23', '~20.5', '~21.8', '~23.5', '—'],
  ['Net flows (£bn)', '(7.8)', '(2.0)', '0.0', '+0.8', '—'],
  ['Market return', '—', '+6%', '+5%', '+5%', '—'],
  ['Fee margin (bp)', '48', '48–49', '47', '47', '—'],
  ['Revenue (£m)', '113.1', '~100', '~102.5', '~110', '98.7 / n.a. / n.a.'],
  ['Costs (£m)', '96', '~88', '~89.5', '~91.5', '—'],
  ['Adj. operating profit (£m)', '16.6', '~12.0', '~13.0', '~18.5', 'EBIT 13.9 (FY27)'],
  ['Interest & other income (£m)', '~2', '~2.5', '~2.5', '~2.5', '—'],
  ['Tax rate', '~25%', '25%', '25%', '25%', '—'],
  ['Diluted shares (m)', '~121', '~119', '~118', '~117', '—'],
  ['**Adj. EPS (p)**', '**12.2**', '**~9.1**', '**~9.9**', '**~13.5**', '**9.6 / 12.3 / 14.6**'],
  ['DPS at 55% payout (p)', '6.7', '~5.0', '~5.4', '~7.4', '—'],
], [26, 12, 13, 13, 13, 23]));
k.push(P('**Assumptions:** industry — flat sustainable-equity demand with improved relative performance; share — modest institutional gains (credit, systematic), continued wholesale attrition in FY27; pricing — stable to slightly dilutive mix; costs — +1–2% p.a. inflation/talent retention; operating leverage — each £1bn AUM ≈ £4.8m revenue at ~80% incremental margin (≈3p EPS); financing — no debt, ~4% on cash; dilution — EBT buys offset awards; no buybacks assumed. **Conclusion:** our FY27–28 EPS are 5–20% below consensus — the recovery is real but back-end-loaded; the stock does not need consensus to be met given ~57% of the market cap is cash.'));

// ---------------- 9 ----------------
k.push(H1('9. Capital structure and liquidity'));
k.push(table(['£m', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26'], [
  ['Cash (FactSet)', '118.2', '104.8', '109.1', '80.3', '70.9'],
  ['Debt (leases)', '9.1', '8.7', '7.8', '5.7', '8.9'],
  ['Net cash', '109.1', '96.0', '101.3', '74.5', '62.0'],
  ['Shareholders’ equity', '138.2', '134.0', '131.1', '115.2', '108.3'],
  ['Goodwill + intangibles', '46.2', '40.0', '35.0', '37.7', '36.3'],
], [30, 14, 14, 14, 14, 14]));
k.push(B('**No financial debt, covenants or interest cost**; lease liabilities only. Company-defined “cash reserves” £63.8m (Sep-26). Regulatory capital: “healthy surplus” (figure not retrieved); management notes the regulatory minimum is a constraint on aggressive cash deployment.'));
k.push(B('**Liquidity:** FY27E dividend ~£6m vs OCF ~£15–20m; EBT purchases £5–8m p.a. Excess cash (after ~£25–30m regulatory/working buffer) ≈ £30–35m, i.e. ~25–30p/share available for buybacks or a special return.'));

// ---------------- 10 ----------------
k.push(H1('10. Valuation, peers and regressions'));
const pr = peers.map(r => [r.n + ' (' + r.t + ')', '£' + Math.round(r.mc), '£' + Math.round(r.ev), fx(r.evs1), fx(r.eveb), fx(r.evebit1), fx(r.pe1), fx(r.pe2), f1(r.nd) + 'x', f1(r.ebm) + '%', f1(r.ebitm) + '%', f1(r.g) + '%', f1(r.ocfy) + '%']);
k.push(table(['Company', 'Mkt cap £m', 'EV £m', 'EV/Sales FY1', 'EV/EBITDA LFY', 'EV/EBIT FY1', 'P/E FY1', 'P/E FY2', 'Net debt/EBITDA', 'EBITDA mgn LFY', 'EBIT mgn LFY', 'Sales g LFY', 'OCF yield'], pr, [17, 7, 7, 7, 7, 7, 6, 6, 8, 7, 7, 7, 7], { size: 13 }));
k.push(SRC('Source: FactSet market values (26-Nov-2026), latest FY fundamentals (Impax FY26 preliminary), FY1/FY2 consensus. Man Group at USD/GBP 1.311; Rathbones EV ex balance-sheet cash; Liontrust EV pro forma Hawksmoor.'));
const rr = reg.map(r => [r.n, r.pb.toFixed(2) + 'x', r.roe.toFixed(1) + '%', r.aum.toFixed(1), r.evaum.toFixed(2) + '%', r.mcaum.toFixed(2) + '%', r.eaum.toFixed(1)]);
k.push(table(['Company', 'P/B', 'Fwd ROE', 'AUM £bn', 'EV/AUM', 'Mkt cap/AUM', 'E/AUM (bp)'], rr, [26, 11, 12, 12, 12, 14, 13]));
k.push(SRC('Fwd ROE = FY1 consensus EPS × shares ÷ latest book equity. E/AUM = FY1 consensus EBIT ÷ latest AUM. AUM: latest company releases (Jun–Sep 2026); Aberdeen AUMA includes platform assets; Ashmore and Man converted from USD.'));
k.push(table(['Metric', 'Impax', 'Peer median', 'Screen'], [
  ['EV/Sales FY1', '0.47x', '1.58x', 'Cheap (but lowest-margin tier)'],
  ['EV/EBIT FY1', '3.3x', '5.1x', 'Cheap'],
  ['P/E FY1 / FY2', '9.3x / 7.3x', '9.6x / 9.3x', 'Fair / cheap'],
  ['EV/AUM', '0.23%', '~0.7%', 'Cheapest in group'],
  ['P/B', '1.00x', '~1.4x', 'Fair for ROE'],
  ['Net cash / market cap', '57%', '~25%', 'Very high'],
], [26, 22, 22, 30]));
k.push(H2('10.1 PBR vs ROE'));
k.push(img(C + 'reg_pbroe.png', 7.0, 3.9));
k.push(P('Linear: ROE = −5.1 + 14.5×P/B (R² 0.94; Polar Capital is influential); log: ROE = 11.4 + 23.0×ln(P/B) (R² 0.73). At Impax’s forward ROE of 10.7% the fitted P/B is 1.09x (linear) / 0.97x (log) vs 1.00x actual — **fair value ~87–97p**. Book-based valuation is not where the discount lies: ROE is depressed by a large, low-yielding cash balance.'));
k.push(H2('10.2 EV/AUM vs E/AUM'));
k.push(img(C + 'reg_evaum.png', 7.0, 3.9));
k.push(P('OLS (ex-Ashmore): EV/AUM (%) = 0.010 + 0.0506 × E/AUM (bp), R² 0.69 — i.e., the sector capitalises operating earnings at ~5x EBIT. Impax earns 6.9bp of EBIT on AUM; the fitted EV/AUM is 0.36% vs 0.23% actual → implied EV ~£72m + £62m net cash = **~£134m, ~110p per share (+23%)**. As margins recover toward 30% (E/AUM ~14bp), the same line implies EV/AUM ~0.72% (~£145m EV at £20bn AUM → ~170p).'));
k.push(H2('10.3 TEV/Sales vs EBIT margin'));
k.push(img(C + 'reg_tevsales.png', 7.0, 3.9));
k.push(P('OLS (ex-Ashmore): EBIT margin = 14.7 + 8.0 × (TEV/Sales), R² 0.34. Impax’s FY1 margin (14.1%) sits at/below the intercept, so the line implies little or no value for the operating business at current margins — the market is valuing Impax as cash plus an option on margin recovery. Each 5ppt of margin recovery is worth ~0.6x EV/Sales (~£60m EV, ~50p/share) on this relationship.'));
k.push(H2('10.4 Historical trading range'));
k.push(img(C + 'histmult.png', 7.0, 2.5));
k.push(table(['At FY-end (Sep) price', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26', 'Now'], [
  ['Share price (p)', '525', '459', '378', '191', '111', '89.3'],
  ['EV (£m)', '570', '492', '382', '164', '71', '46'],
  ['EV/Sales', '3.2x', '2.7x', '2.2x', '1.1x', '0.6x', '0.4x'],
  ['EV/EBITDA', '8.1x', '7.9x', '6.5x', '4.3x', '3.4x', '2.2x'],
  ['P/E', '11.8x', '15.4x', '13.1x', '10.6x', '11.9x', '7.3x'],
  ['P/B', '4.9x', '4.4x', '3.7x', '2.1x', '1.2x', '1.0x'],
], [24, 12, 12, 12, 12, 12, 16]));
k.push(P('Impax trades at the bottom of its range on every measure — EV/EBITDA 2.2x vs a five-year average of ~6x, P/B 1.0x vs ~3.3x.'));
k.push(table(['Competitor', 'Ticker / owner', 'Listed?', 'Overlap'], [
  ['BNP Paribas Asset Management', 'BNP FP (parent)', 'Parent listed', 'Partner, shareholder and competitor (thematic/sustainable)'],
  ['Pictet Asset Management', 'Private partnership', 'No', 'Largest thematic equity franchise (Water, Clean Energy)'],
  ['Nordea Asset Management', 'NDA FI (parent)', 'Parent listed', 'Climate/environment strategies'],
  ['Candriam', 'New York Life (private)', 'No', 'Sustainable equity & credit'],
  ['Schroders (Nuveen/TIAA)', 'Private since Oct-2026', 'No', 'Global sustainable/energy transition'],
  ['Jupiter / Liontrust / Ninety One', 'JUP LN / LIO LN / N91 LN', 'Yes', 'Sustainable & ecology strategies'],
  ['WHEB Asset Management', 'Private', 'No', 'UK sustainable equity boutique'],
  ['Calvert Research & Management', 'Morgan Stanley (MS US)', 'Parent listed', 'US ESG mutual funds — vs Impax/Pax US'],
  ['Parnassus Investments', 'AMG US affiliate', 'Parent listed', 'US ESG funds'],
  ['KBI Global Investors', 'Amundi (AMUN FP)', 'Parent listed', 'Water/energy solutions'],
  ['iShares / Xtrackers / L&G ETFs', 'BLK US / DBK GY / LGEN LN', 'Yes', 'Passive clean-energy, water, ESG indices'],
], [28, 26, 16, 30]));

// ---------------- 11 ----------------
k.push(H1('11. M&A: industry, takeover candidacy and comparables'));
k.push(P('Sector consolidation is accelerating (Nuveen/Schroders £9.9bn; BNPP/AXA IM €5.1bn; Jupiter/CCLA; Liontrust bolt-ons). Specialist brands with global institutional reach are scarce assets for large platforms building “transition” capabilities.'));
k.push(table(['Pros (supporting a bid)', 'Impediments'], [
  ['EV of only ~£46m (0.23% of AUM); net cash £62m', 'Founder-CEO and management (~18%) have said they are not interested in being acquired'],
  ['Natural strategic buyer in BNP Paribas AM (14.4% holder, distributor, board nominee) — could consolidate its own thematic range', 'BNPP stake gives it de facto blocking power and deters third-party bidders'],
  ['Brand and process are unique in transition investing; competitors retreating', 'Key-person dependence (Simm; listed-equity CIO Bruce Jenkyn-Jones, 3.1%)'],
  ['Cost synergies: a large owner could absorb most of £86.5m run-rate costs outside investment teams', 'Political/ESG stigma in the US may deter US buyers'],
  ['Concentrated register (four holders ≈ 50%) makes a negotiated deal executable', 'AIM listing, small free float, illiquid'],
], [50, 50]));
k.push(P('**Potential acquirers:** BNP Paribas AM; Nuveen/Schroders; Amundi; Natixis IM (multi-boutique); AMG (affiliate model, as with Parnassus); Pictet; Liontrust/a UK merger of equals (Liontrust funds already hold 10.7%); private equity seeking a cash-rich platform.'));
k.push(table(['Method', 'Range', 'Implied EV (£m)', 'Value/share'], [
  ['% of AUM (£20bn)', '0.5% – 0.9%', '100 – 180', '~135p – 200p'],
  ['EV/FY28E EBITDA (~£18m)', '6x – 8x', '108 – 144', '~140p – 170p'],
  ['P/E on recovered EPS (~13.5p FY29E)', '12x – 15x', '—', '~160p – 200p'],
  ['Premium to undisturbed (89.3p)', '40% – 80%', '—', '~125p – 160p'],
  ['**Central takeout**', '**~0.6–0.7% AUM**', '**~£130m**', '**~160–165p**'],
], [32, 22, 18, 28]));
k.push(SRC('Per-share values add ~£62m net cash and use ~121.5m shares.'));
k.push(table(['Announced', 'Target', 'Acquirer', 'Value', 'AuM', 'Multiples / notes'], [
  ['Sep-2026', 'Hawksmoor fund mgmt & MPS', 'Liontrust', '£6m + up to £4m', '£1.9bn', '0.32–0.53% of AuM'],
  ['Mar-2026', 'River Global Holdings', 'Liontrust', '£7.6m shares + up to £2.1m', '£3.0bn', '~0.3% of AuM'],
  ['Feb-2026', 'Schroders plc', 'Nuveen (TIAA)', '£9.9bn (590p cash)', '~$1.1tn', '~17x 2025 adj. op. profit after tax; ~1.2% of AuM; 29–34% premium'],
  ['Feb-2026 (compl.)', 'CCLA Investment Management', 'Jupiter', '~£100m (reported)', '£15.0bn', '~0.7% of AuM'],
  ['Aug-2024', 'AXA Investment Managers', 'BNP Paribas', '€5.1bn', '~€850bn', '~0.6% of AuM (approx.)'],
  ['Jul-2023', 'Gresham House', 'Searchlight Capital', '£470m', '~£8.4bn', '~16x EBITDA; 63% premium'],
  ['May-2023', 'GAM Holding (failed)', 'Liontrust', '~CHF 100m (approx.)', '~CHF 23bn', '~0.4–0.5% of AuM'],
  ['Mar-2023', 'Investec W&I UK', 'Rathbones', '£839m', '~£40bn', '~2.1% of AuM'],
  ['Jan-2022', 'Majedie AM', 'Liontrust', 'up to £120m', '£5.8bn', 'up to ~2.1% of AuM'],
], [12, 20, 15, 18, 10, 25]));
k.push(SRC('Source: company RNS/press (see Liontrust report for detail); “approx.” not re-verified.'));
k.push(H2('Impax’s own acquisitions (last 10 years)'));
k.push(table(['Date', 'Target', 'Consideration', 'AuM', 'Outcome'], [
  ['Ann. Sep-2017 / compl. Jan-2018', 'Pax World Management (US) — now Impax Asset Management LLC', 'Not retrieved (initial + contingent; verify)', '~US$4bn (approx.)', 'Gave Impax a US platform; North America now ~34% of revenue — successful'],
  ['2022', 'Absolute Return Partners (UK)', 'Not retrieved', 'n.d.', 'Small; multi-asset/private credit capability — verify'],
  ['Ann. Jan-2024 / compl. Jul-2024', 'Absalon Corporate Credit (Denmark)', 'Undisclosed', '~€405m', 'Integrated into fixed income'],
  ['Ann. 2024 / compl. 1-Apr-2025', 'SKY Harbor Capital Management — European short-duration HY assets (+ Frankfurt distribution entity)', 'Undisclosed', '~£1.1bn at completion (£1.6bn at announcement)', 'Integrated; first significant credit mandate won Q2 FY26'],
], [16, 30, 18, 14, 22]));

// ---------------- 12 ----------------
k.push(H1('12. Management'));
k.push(table(['Executive', 'Role / tenure', 'Track record', 'Skin in the game'], [
  ['Ian Simm', 'Founder & CEO since 1998 (28 yrs)', 'Built Impax from a start-up (ex-McKinsey) into a ~£40bn global specialist; acquired Pax World; listed on AIM. Since 2023 AUM −50%, share price −94%. Director IIGCC', '~9.6m shares (7.5%, ~£8.5m)'],
  ['Karen Cockburn', 'CFO since Jan-2023; board Mar-2023', 'Ex-CFO Virgin Money (investments); Cofunds director; led FY25–26 cost reset', 'n.a.'],
  ['Joe Keefe', 'President (since 2005 in group; ex-Pax World CEO)', 'Led Pax World / US business', 'n.a.'],
  ['Bruce Jenkyn-Jones', 'CIO Listed Equities', 'Long-tenured co-founder-era PM of flagship strategies', '~3.9m shares (3.1%)'],
  ['Darren Johnson', 'Global COO', 'Operations', 'n.a.'],
], [14, 20, 46, 20]));
k.push(P('**Capital allocation:** ROE 48% (FY22) → 9% (FY26). Acquisitions have been small and culturally integrated (Pax, Absalon, SKY Harbor) — a strength. Dividends were held at 27.6p through FY24 even as cover fell (FY24 cover ~1.0x), then cut 57% and 44%. £10m buyback May–Dec 2025 at ~145–180p (above today’s price — in hindsight poorly timed). EBT purchases of £7–15m p.a. to avoid dilution consume a material share of cash flow.'));
k.push(P('**Red flags:** (1) founder entrenchment and stated opposition to a sale despite a 94% share-price fall; (2) related-party relationship with BNPP (shareholder, distributor, board seat, advisory agreement); (3) pay: no 2026 single-figure data retrieved; (4) strategy has been consistent (a positive) but slow to diversify. **Archetype:** founder-led — strong for vision and culture, potentially weak for a value-maximising exit. **Recent changes:** no CEO/CFO changes; Chair changed July 2024.'));

// ---------------- 13 ----------------
k.push(H1('13. Board of Directors'));
k.push(table(['Director', 'Role', 'Since', 'Background', 'Other affiliations'], [
  ['Simon O’Regan', 'Independent Chair', 'NED 2020; Chair Jul-2024', 'Ex-CEO Mercer UK (2005–09); President Retirement, Risk & Finance, Mercer', 'NED Financial Reporting Council; Alexander Forbes Life; Nuclear Liabilities Financing Assurance Board'],
  ['Ian Simm', 'CEO', '1998', 'Founder', 'IIGCC director'],
  ['Karen Cockburn', 'CFO', 'Mar-2023', 'Ex-CFO Virgin Money investments', 'Director Legado Technologies'],
  ['Annette Wilson', 'Senior Independent Director', 'Jun-2022', 'Ex-CFO Palamon Capital; Partner/COO Finch Capital; chartered accountant (SA)', 'NED Tech Nation; Chair ADHD Embrace'],
  ['Arnaud de Servigny', 'Non-Executive Director (BNPP-linked; not independent)', 'Jun-2018', 'Ex-MD Deutsche Bank AM; ex-Global Head DPM Evelyn; Professor of Finance, Imperial College', 'NED BNP Paribas Asset Management Europe SAS; President Queensfield AI'],
  ['Julia Bond', 'Independent NED', 'Nov-2023', 'Former FCDO director; investment-trust governance', 'NED International Public Partnerships; SID European Assets Trust; Strategic Command'],
  ['Lyle Logan', 'Independent NED', 'May-2024', 'Ex-Vice Chairman Northern Trust; CEO Northern Trust International Banking', 'Independent Director Farmer Mac (2026); ex-Heidrick & Struggles board'],
], [14, 16, 12, 30, 28]));
k.push(SRC('Source: FactSet People (company_people, jobs); StreetAccount.'));
k.push(P('**Changes in last five years:** Sally Bridgeland (Chair) retired Jul-2024 → Simon O’Regan; Vince O’Brien (NED, 13 years) retired Mar-2023; Karen Cockburn joined the board Mar-2023; Annette Wilson (Jun-2022), Julia Bond (Nov-2023) and Lyle Logan (May-2024) appointed. **Observations:** reasonably refreshed and independent board, but BNPP’s board link is a structural conflict in any strategic process.'));

// ---------------- 14 ----------------
k.push(H1('14. Shareholders, activism and short interest'));
k.push(table(['#', 'Holder', 'Type', '% held', 'Shares (m)', 'As of'], [
  ['1', 'BNP Paribas Asset Management Europe', 'Strategic institution / distributor', '14.37%', '18.26', 'Oct-2025'],
  ['2', 'Liontrust Investment Partners LLP', 'Institutional (Liontrust funds)', '10.73%', '13.63', 'Feb-2026'],
  ['3', 'Ian Simm (CEO/founder)', 'Insider', '7.53%', '9.57', 'Sep-2025'],
  ['4', 'Impax Group Employee Benefit Trust 2012', 'Insider (EBT)', '5.07%', '6.44', 'Jun-2026'],
  ['5', 'TrinityBridge (ex-Close Brothers AM)', 'Wealth/institutional', '3.13%', '3.98', 'Oct-2026'],
  ['6', 'Bruce Jenkyn-Jones (CIO)', 'Insider', '3.09%', '3.93', 'Oct-2025'],
  ['7', 'Hargreaves Lansdown Asset Mgmt', 'Platform/retail', '2.99%', '3.80', 'Oct-2025'],
  ['8', 'FIL Investment Advisors (UK)', 'Institutional', '2.90%', '3.68', 'Oct-2026'],
  ['9', 'GAM special-situations funds', 'Institutional — activist/engaged', '~2.2%', '~2.7', 'Jul-2026 (StreetAccount)'],
  ['10', 'J O Hambro Capital Management', 'Institutional', '1.87%', '2.38', 'Sep-2026'],
  ['–', 'Octopus Investments; HL Fund Managers; JPMorgan IM', 'Institutional', '1.8% / 1.7% / 1.5%', '', 'Oct-2026'],
], [4, 32, 26, 12, 12, 14]));
k.push(SRC('Source: FactSet Ownership (security_holders FS); GAM stake per StreetAccount 14-Jul-2026 (not in FactSet holder list). % on ~127m share basis used by FactSet.'));
k.push(P('**Activism:** (1) **GAM special-situations funds** disclosed ~2.2% (14-Jul-2026), citing continued engagement and deep undervaluation alongside their Liontrust position; no public letter or demands to Impax were found. (2) **Saba Capital** (indirect): Saba’s campaign at Impax Environmental Markets plc forced an exit tender (78% of shares tendered, Apr-2026), stripping Impax of most of that trust’s AUM — the activist risk to Impax’s closed-end franchise has already crystallised. (3) **Liontrust funds (10.7%)** are passive holders but a potential swing vote. **Short interest:** not retrieved (FCA aggregate regime since Jul-2026); no known short campaign.'));

// ---------------- 15 ----------------
k.push(H1('15. Strategic initiatives (last 10 years)'));
k.push(table(['Initiative', 'Period', 'Status', 'Assessment'], [
  ['US expansion via Pax World', '2017–18', 'Completed', 'Success: diversified client base; NA ~34% of revenue'],
  ['BNP Paribas strategic partnership & shareholding', '2010s–present', 'Ongoing', 'Major distribution channel (Luxembourg revenue £33m FY25); concentration risk'],
  ['Private markets (New Energy funds)', '2000s–present', 'Ongoing', 'Small but sticky; energy storage, EV charging'],
  ['Fixed-income build-out (Absalon, SKY Harbor)', '2024–25', 'Integrated', 'Early success (first significant credit mandate)'],
  ['Systematic equity products', '2023–present', 'Growing', '8% → 13% of AUM; lower fee'],
  ['Cost reset (~30 roles; costs £108m → £86.5m run-rate)', 'FY25–26', 'Complete', 'Restores operating leverage'],
  ['£10m buyback', 'May–Dec 2025', 'Completed (5.6m shares cancelled)', 'Executed above current price'],
  ['US active ETFs / new products (EM, social)', '2025–26', 'In progress', 'Too early'],
  ['Strategic partnerships with large asset owners', '2026–', '8–10 discussions', 'Potential step-change catalyst'],
], [34, 14, 22, 30]));

// ---------------- 16 ----------------
k.push(H1('16. Stakes held'));
k.push(P('Impax holds no strategic stakes in listed companies. It holds **seed capital (~£8.6m)** in its own funds, general-partner/co-investment interests in its private-markets funds (Impax New Energy funds; carried interest potential) and the US/European fund-management subsidiaries. These are financially modest (<10% of market cap) but the private-markets carry is a small upside option. Note the reverse cross-holding: Liontrust funds own 10.7% of Impax.'));

// ---------------- 17 ----------------
k.push(H1('17. Dividends, buybacks and treasury shares'));
k.push(table(['Fiscal year (Sep)', 'Interim (p)', 'Final (p)', 'Total DPS (p)', 'Buyback / EBT purchases (£m)', 'Shares y/e (m)'], [
  ['FY21', 'n.a.', 'n.a.', '20.6', '0.0', '128.5'],
  ['FY22', '4.7', '22.9', '27.6', '8.8', '129.3'],
  ['FY23', '4.7', '22.9', '27.6', '15.1', '128.3'],
  ['FY24', '4.7', '22.9', '27.6', '8.4', '127.8'],
  ['FY25', '4.0', '8.0', '12.0', '6.9 (buyback launched May-25)', '124.7'],
  ['FY26', '2.0', '4.7 (ex ~18-Feb-2027)', '6.7', '7.9 (£10m buyback completed Dec-25; 5.6m shares cancelled)', '120.3'],
], [14, 12, 18, 12, 28, 16]));
k.push(SRC('Source: FactSet Fundamentals (FF_DPS, FF_STK_PURCH_CF, FF_COM_SHS_OUT); StreetAccount (buyback completion 22-Dec-2025; final dividend 4.7p); FactSet calendar (dividend 18-Feb-2027). FY22–24 interim/final split assumed from the 4.7p interim disclosed for H1 FY24 — verify.'));
k.push(P('**Treasury/EBT:** Impax satisfies share awards through its EBT (6.44m shares, 5.07%, Jun-2026) rather than treasury shares; FactSet shows own-shares reserve of £6.8m (FY26). Bought-back shares were cancelled (127.0m in issue at Dec-2025 → ~120–121m by Sep-2026 per FactSet).'));

// ---------------- 18 ----------------
k.push(H1('18. Bull vs bear'));
k.push(H2('Bull case'));
k.push(B('**Cash-backed:** net cash ~£62m = 51p/share; operations valued at ~£46m (0.23% of AUM, ~3x FY27E EBIT).'));
k.push(B('**Operating leverage:** costs reset to £86.5m; every £1bn of net inflow adds ~3p EPS; management targets 30% margin at £27–28bn AUM (FY29–30 EPS potential 20p+ → 200p at 10x).'));
k.push(B('**Performance inflection:** 2026 outperformance in energy security/resilience; competitors exiting the niche; 8–10 strategic-partnership talks.'));
k.push(B('**Strategic value:** unique brand; BNPP partnership could become a bid; concentrated register makes a deal executable.'));
k.push(H2('Bear case'));
k.push(B('**Structural ESG stigma** in the US and among UK wealth managers; outflows persist despite performance (as in 2024–25).'));
k.push(B('**Client concentration:** loss of the BNPP channel or another large mandate (cf. SJP) would cut revenue 20%+.'));
k.push(B('**Founder entrenchment:** no appetite to sell; cash may be spent on sub-scale acquisitions.'));
k.push(H2('Pre-mortem'));
k.push(P('By late 2028 the shares sit at 65p: the 2026 performance rally faded as tech leadership returned; US clients redeemed on political grounds; BNPP rationalised its thematic range in-house after integrating AXA IM; AUM fell to £15bn; revenue ~£72m vs costs £85m; dividend suspended; cash used for an acquisition. The market valued Impax at cash less losses.'));
k.push(H2('Contrarian view'));
k.push(P('The market is pricing Impax as an ESG relic. It is better viewed as a **cash shell with a free, scarce, globally recognised transition-investing franchise** — at the exact point when competitors have withdrawn, energy security has made the theme economic rather than ethical, and performance has turned. The BNPP shareholding, often seen as a constraint, is the most likely route to a control premium.'));

// ---------------- 19 ----------------
k.push(H1('19. Scenario analysis (12–18 months)'));
k.push(table(['Scenario', 'Prob.', 'Key assumptions', 'EPS', 'Valuation basis', 'Value/share', 'vs 89.3p'], [
  ['Bear', '30%', 'Outflows £3bn p.a.; fee 45bp; margin <10%; no deal', '~6p', 'Cash (~£55m) + 3x EBIT', '~70p', '−22%'],
  ['Base', '45%', 'Flows ~flat by FY28; revenue £100–103m; margin 12–15%', '~9–10p', 'EV/AUM regression (0.36%) ≈ 10–11x P/E', '~110p', '+23%'],
  ['Bull / strategic', '25%', 'Sale or merger at ~0.65% of AUM; or flows positive with margin →25%', 'n.a.', 'EV ~£130m + net cash', '~165p', '+85%'],
  ['**Weighted**', '', '', '', '', '**~112p**', '**+25%** (+7.5% yield)'],
], [14, 7, 34, 8, 19, 10, 8]));

// ---------------- 20 ----------------
k.push(H1('20. Questions for the CEO / Chair (by information value)'));
[
  'Under what circumstances would the board consider a sale or merger, and has it received any approach in the last 24 months?',
  'What is BNP Paribas AM’s strategic intention for its 14.4% stake after its AXA IM acquisition, and how is its board representative conflicted in strategic decisions?',
  'What is the regulatory capital requirement, and how much of the £63.8m cash is genuinely surplus?',
  'Why not return surplus cash (special dividend/tender) at 0.23% EV/AUM rather than pursue acquisitions?',
  'What AUM retention rate do you expect from the BNPP channel over the next 24 months?',
  'Of the 8–10 strategic-partnership discussions, how many involve day-one AUM and what is the expected fee rate?',
  'What were Q1 FY27 net flows, and when do you expect a positive quarter?',
  'How much of the IEM AUM switched into the UCITS fund?',
  'What is the incremental margin on new AUM given the cost reset, and is the 30% margin target achievable below £27bn?',
  'What is the succession plan for the founder-CEO and listed-equities CIO?',
  'How has US political risk affected North American client retention, and what share of US AUM is with public pension plans?',
  'What returns have the Absalon and SKY Harbor acquisitions generated relative to consideration?',
  'How is executive variable pay linked to TSR and flows following a 94% share-price decline?',
  'What is the fee-margin trajectory as systematic equity and credit grow?',
  'What role could the Liontrust funds’ 10.7% holding play in any strategic combination?',
].forEach(q => k.push(N(q)));

// ---------------- 21 ----------------
k.push(H1('21. Devil’s advocate / forensic review'));
k.push(P('**What could break the model?** The “transition” theme being politically re-labelled and dropped by mainstream allocators, leaving Impax as a niche with permanently lower AUM. **Concentration:** BNPP-related revenue (Luxembourg + France ≈ £45m, ~32% of FY25 revenue) — if BNPP internalises after absorbing AXA IM, Impax loses a third of revenue. **Most dangerous competitor:** BNPP AM itself (partner and competitor), and Pictet’s scale in thematic equities. **Worst capital allocation:** holding 27.6p DPS through FY24 at ~1x cover; £10m buyback at ~160p vs 89p today. **What must hold for today’s price:** almost nothing — cash covers 57% of the price; the residual £46m requires only ~£10m of sustainable operating profit. **If growth disappoints 20–30%:** FY28E EPS 7–8p, value ~80–90p (≈ current price). **Single impairment scenario:** loss of BNPP distribution — plausibility moderate (20–30% over 3 years).'));
k.push(table(['Check', 'Finding', 'Flag'], [
  ['Quality of earnings', 'Adj. EPS 12.2p vs statutory 8.2p — adjustments (amortisation, restructuring) material in FY26', 'Amber'],
  ['Reporting changes', 'Segment disclosure added FY25 (listed / FI / private) — positive', 'Green'],
  ['Opacity', 'No segment profit; AUM by channel disclosed', 'Amber'],
  ['Organic growth transparency', 'Good quarterly AUM/flow disclosure; acquired AUM separated', 'Green'],
  ['Selective disclosure', 'AIM RNS; timely trading updates', 'Green'],
  ['Adversarial to criticism', 'Constructive tone; but stated no interest in being acquired', 'Amber'],
  ['Dividend vs FCF', 'FY24 DPS 27.6p ≈ £35m vs OCF £54m less EBT buys; covered, then cut', 'Green–Amber'],
  ['Management quality', 'Founder-led, consistent strategy, slow diversification', 'Amber'],
  ['Fads', 'ESG flow boom/bust 2020–25 — business is itself a “fad-exposed” franchise', 'Red'],
  ['Related parties', 'BNPP: 14.4% holder + distributor + advisory agreement + board seat', 'Amber–Red'],
  ['Regulatory risk', 'US anti-ESG, SFDR/SDR labelling', 'Amber'],
  ['Hidden liabilities', 'Seed-capital MTM; deferred comp; leases £8.9m; no contingent consideration disclosed', 'Green'],
  ['Balance sheet', 'Net cash £62m; goodwill+intangibles £36m (34% of equity; Pax-related) — impairment risk if US AUM falls', 'Green–Amber'],
  ['Stock-based comp', 'EBT purchases £7–15m p.a. — real cash cost of SBC', 'Amber'],
], [24, 62, 14]));

// ---------------- 22 ----------------
k.push(H1('22. Timeline and catalyst calendar'));
k.push(table(['Date', 'Past event'], [
  ['1998', 'Impax founded by Ian Simm'], ['Jan-2018', 'Pax World acquisition completed'], ['Dec-2021', 'Share price peak 1,482p'],
  ['Mar-2023', 'AUM peak £40.1bn'], ['Jul-2024', 'Chair change (Bridgeland → O’Regan); Absalon completed'], ['Oct/Dec-2024', 'SJP terminates both mandates (£774m, then ~£6.2bn)'],
  ['Apr-2025', 'SKY Harbor European assets completed; BNPP advisory agreement'], ['May–Dec 2025', '£10m buyback'], ['Dec-2025', 'FY25: DPS cut to 12.0p'],
  ['Apr-2026', 'IEM exit tender (Saba); revenue guidance cut'], ['Jul-2026', 'Performance rebound; GAM ~2.2% stake'], ['25-Nov-2026', 'FY26 results beat; restructuring complete'],
], [20, 80]));
k.push(table(['Expected date', 'Upcoming catalyst', 'Why it matters'], [
  ['Jan-2027', 'Q1 FY27 AUM/flows update', 'Test of “outflows slowed considerably”'],
  ['~Feb/Mar-2027', 'AGM; final dividend 4.7p (ex ~18-Feb-2027)', 'Shareholder engagement point'],
  ['Apr-2027', 'Q2 FY27 AUM update', 'First full quarter post-IEM'],
  ['~27-May-2027', 'H1 FY27 results (FactSet projected)', 'Margin recovery; revenue vs £100–103m guide'],
  ['Jul-2027', 'Q3 FY27 AUM update', ''],
  ['Oct-2027', 'Q4 FY27 AUM update', ''],
  ['~late Nov-2027', 'FY27 results', 'Dividend; capital return decision'],
  ['Any time', 'Strategic partnership announcements; BNPP stake decision; approach', 'Primary re-rating catalysts'],
], [18, 44, 38]));

// ---------------- 23 ----------------
k.push(H1('23. Data audit trail and limitations'));
[
  'Prices (IPX daily): FactSet Global Prices (saved output; audit table available in session).',
  'EPS consensus: https://my.apps.factset.com/mcp-audit-table/51e6276f-45e8-4aa7-a1ce-a4ead56e33da',
  'Price target: https://my.apps.factset.com/mcp-audit-table/0d21e858-b829-4cb0-8dee-ac8774a69b3a',
  'Ratings: https://my.apps.factset.com/mcp-audit-table/aabc027d-4866-43af-bd74-980417615944',
  'Ownership: https://my.apps.factset.com/mcp-audit-table/8bf3dd21-b88a-47b1-a1c6-ac3436587ee5',
  'Officers/directors: https://my.apps.factset.com/mcp-audit-table/fbb3189e-a4c4-42e9-a21b-bff2dfe1877c',
  'Career histories: https://my.apps.factset.com/mcp-audit-table/ff029b0b-77ec-4ebf-8f17-157ed3624d72',
  'Calendar: https://my.apps.factset.com/mcp-audit-table/8890fc77-05f1-4315-bda3-d695365c5923',
  'Peer market values / consensus: see Liontrust report Section 23 (same peer data set).',
  'Fundamentals: per-datapoint FactSet audit cards (FF_* formulas) retrieved with AUDIT_CARD.',
].forEach(t => k.push(B(t)));
[
  'FY26 fundamentals in FactSet are preliminary (results 25-Nov-2026); FY26 segment data not yet available.',
  'Primary filings (annual report PDFs, RNS on Investegate/LSE) could not be fetched due to network policy; company figures from StreetAccount, CallStreet transcripts and press.',
  'Peer AUM from latest company releases (Jun–Sep 2026) via search summaries; Polar (£43.7bn), Jupiter (£75.9bn), Aberdeen (£578.9bn AUMA), Rathbones (£121.1bn FUMA), Brooks (£21.7bn FUMA) mix AUM and AUMA definitions; Ashmore and Man converted at 1.311.',
  'Forward ROE uses FY1 consensus EPS (different fiscal year-ends) over latest book equity; regressions on 10–11 UK listed points — directional only; Ashmore excluded from EV/AUM and TEV/Sales fits as an outlier.',
  'Pax World and Absolute Return Partners consideration, FY24 flows, and FY22–24 interim/final split not verified; GAM stake not in FactSet holder data.',
  'Projections, scenarios and sentiment scores are analyst estimates.',
].forEach(t => k.push(B(t)));

Packer.toBuffer(doc(k, 'Impax Asset Management Group plc (IPX LN) — Equity Research, 27 Nov 2026')).then(b => { fs.writeFileSync('Impax_IPX_Equity_Research_Nov2026.docx', b); console.log('written'); });
