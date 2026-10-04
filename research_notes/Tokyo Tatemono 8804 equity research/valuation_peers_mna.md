# Tokyo Tatemono (8804 JP): Valuation vs Peers, Peer Regression, Japanese Real-Estate M&A and Takeover Assessment

> **Research conditions (as of 4 Oct 2026), which matter for how far these notes can be relied on.**
> (1) Direct page fetching was blocked by the session's network egress policy for every finance and IR host I tried: stockanalysis.com, MarketScreener, Kabutan, Yahoo! Finance Japan, Google Finance, Investing.com, companiesmarketcap, TradingEconomics, Simply Wall St, irbank, tatemono.com, pdf.irpocket.com, www2.jpx.co.jp, Wikipedia and Reuters. The Financial Datasets MCP covers SEC tickers only and had zero credit.
> (2) After about 25 searches by this workstream, the session-wide WebSearch budget (200 calls shared across all researchers) ran out. That happened before the historical-multiple, M&A and acquisitions workstreams could be searched.
> (3) As a result, every "Cited Finding" below comes from a **search-engine extraction** of the cited page; I could not open the page or PDF to cross-check it. Figures marked **S** are sourced, **D** are derived arithmetically from sourced figures, and **E** are analyst **estimates** (assumptions, unverified).
> (4) Money is in JPY bn unless stated. "LTFY" means the last reported full fiscal year. The input dataset is in `peer_valuation_8804.csv`, saved in the same folder.

## 1. Competitor list: public and private, with tickers and listed/unlisted status

### Takeaway
Tokyo Tatemono's closest listed comparables are the five integrated Tokyo developers (Mitsui Fudosan 8801, Mitsubishi Estate 8802, Sumitomo Realty 8830, Tokyu Fudosan HD 3289, Nomura RE HD 3231), plus Hulic 3003 and two smaller office landlords, Heiwa RE 8803 and Keihanshin Building 8818. Sekisui House 1928, Daito Trust 1878 and Open House 3288 are useful only as housing and condo cross-checks. The unlisted competitors are Mori Building, Mori Trust, Nippon Steel Kowa and NTT UD, plus the condo subsidiaries of the majors.

### Cited Findings
- Tokyo Tatemono is listed on the TSE Prime market under code 8804 — [Matsui Securities quote page](https://finance.matsui.co.jp/stock/8804/index)
- Listed peers whose quote pages were retrieved in this session (status and ticker confirmed by the quote pages):
  - Mitsui Fudosan 8801 — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=8801)
  - Mitsubishi Estate 8802, TSE Prime — [Matsui](https://finance.matsui.co.jp/stock/8802/index), [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8802)
  - Sumitomo Realty & Development 8830, TSE Prime, real-estate sector — [Monex Scouter](https://scouter.monex.co.jp/report/index/8830)
  - Tokyu Fudosan HD 3289, a comprehensive developer covering urban development, strategic investment, property management and brokerage — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=3289)
  - Nomura Real Estate HD 3231 — [kabuyoho](https://kabuyoho.jp/sp/reportTop?bcode=3231)
  - Hulic 3003, TSE Prime — [Matsui](https://finance.matsui.co.jp/stock/3003/index)
  - Heiwa Real Estate 8803, landlord of the Tokyo, Osaka, Nagoya and Fukuoka stock-exchange buildings, with Kabutocho and Sapporo redevelopments — [traders.co.jp](https://www.traders.co.jp/stocks/41_8803/)
  - Keihanshin Building 8818, TSE Prime, Osaka-centred mid-size offices plus data-centre buildings, retail/logistics and off-track betting facilities — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8818), [Matsui](https://finance.matsui.co.jp/stock/8818/index)
  - Sekisui House 1928 — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=1928)
  - Daito Trust Construction 1878 — [Monex Scouter](https://scouter.monex.co.jp/report/index/1878)
  - Open House Group 3288, TSE Prime — [Matsui](https://finance.matsui.co.jp/stock/3288/index)
- Fiscal year-ends confirmed from the results headings:
  - March: Mitsui Fudosan ("2026年3月期"), Mitsubishi Estate, Sumitomo Realty, Tokyu Fudosan HD, Nomura RE HD, Heiwa RE and Keihanshin. Sources: [Mitsui tanshin](https://www.mitsuifudosan.co.jp/corporate/ir/presentation/pdf/tanshin260513.pdf), [MEC tanshin](https://www.mec.co.jp/ir/library/2026/4Q/summary_2025_4.pdf), [Sumitomo tanshin](https://www.sumitomo-rd.co.jp/uploads/8830_FY2025_4Q.pdf), [Tokyu tanshin](https://www2.jpx.co.jp/disc/32890/140120260511521611.pdf), [Nomura tanshin](https://www.nomura-re-hd.co.jp/ir/pdf/renketsu_20260424.pdf), [Heiwa summary](https://japanir.jp/company/company-8803/ir/8803-20260430-02_wp_financial_summary/), [Keihanshin via Matsui](https://finance.matsui.co.jp/stock/8818/settlement/index)
  - December: Tokyo Tatemono and Hulic. Sources: [TT FY12/2025 tanshin](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf), [Hulic FY12/2025 tanshin](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260129/20260128539955.pdf)
  - January: Sekisui House (DPS labels "2026年1月" and "2027年1月") — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=1928)
  - September: Open House (DPS labels "2025年9月" and "2026年9月予想") — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=3288)

### Inferences

**Competitor table.** "Verified" means listing status was confirmed in this session.

| Company | Ticker / status | Why included / role | Verified |
|---|---|---|---|
| Mitsui Fudosan | 8801, listed (TSE Prime) | #1 integrated developer: office, retail, condos, hotels; Nihonbashi/Yaesu neighbour of TT | Yes |
| Mitsubishi Estate | 8802, listed | Marunouchi office landlord; adjacent to TT's Yaesu/Otemachi assets | Yes |
| Sumitomo Realty & Development | 8830, listed | Tokyo office landlord and condo developer; high margin | Yes |
| Tokyu Fudosan HD | 3289, listed | Shibuya-centred developer, condos, brokerage; similar size to TT | Yes |
| Nomura Real Estate HD | 3231, listed | "Proud" condos plus office; closest condo-mix and size match | Yes |
| Hulic | 3003, listed | Central-Tokyo office/retail landlord; Fuyo/Mizuho lineage (unverified); a possible strategic party | Yes |
| Heiwa Real Estate | 8803, listed | Small office landlord, Kabutocho redevelopment | Yes |
| Keihanshin Building | 8818, listed | Small Osaka office/data-centre landlord; widens the margin range | Yes |
| Sekisui House | 1928, listed | Housing/condo cross-check (used in the P/B-ROE fit only) | Yes |
| Daito Trust Construction | 1878, listed | Rental-housing cross-check (P/B-ROE only) | Yes |
| Open House Group | 3288, listed | Condo/detached-housing cross-check (P/B-ROE only) | Yes |
| Daiwa House 1925; Haseko 1808; MIRARTH HD 8897; Ichigo 2337 | listed | Possible extra housing/condo or asset-light comps; not priced in this session | No |
| Mori Hills REIT 3234; Japan Prime Realty 8955 (TT-sponsored, unverified) | listed J-REITs | REITs excluded from the EV/Sales fit (pass-through structure); NAV references only | No |
| Mori Building | unlisted (private) | Roppongi/Toranomon/Azabudai mega-projects; direct office competitor | No |
| Mori Trust | unlisted | Office/hotel landlord (Toranomon, Shiroyama) | No |
| Nippon Steel Kowa Real Estate | unlisted | Office developer (Akasaka, Otemachi) | No |
| NTT Urban Development / NTT Urban Solutions | unlisted (NTT UD delisted after the 2020 NTT TOB; unverified) | Office/condo developer within the NTT group | No |
| Tokyu Land Corp | unlisted, 100% subsidiary of 3289 | Operating developer of Tokyu Fudosan HD | No |
| Mitsubishi Jisho Residence | unlisted, subsidiary of 8802 | Condo competitor to TT's "Brillia" brand | No |
| Sumitomo Fudosan Hanbai | unlisted, subsidiary of 8830 | Brokerage competitor | No |
| Mitsui Fudosan Residential; Nomura RE Development | unlisted subsidiaries of 8801 / 3231 | Condo competitors | No |

**Inclusion logic.** The regression peer set is the eight listed developers/landlords, all of which report operating income on J-GAAP like TT. The three housing names are added only where the data exist (P/B, ROE, P/E), because their P&L and balance sheets were not retrieved. REITs are excluded from EV/Sales: they distribute nearly all their income and are asset-pure, so the multiple is not comparable.

### Gaps
- I did not re-verify the status of the unlisted companies in this session: NTT UD's 2020 delisting, the subsidiary ownership percentages, and whether TT sponsors Japan Prime Realty. These come from analyst background knowledge.
- I could not retrieve Daito Trust's fiscal year-end (believed to be March, unverified), or prices and fundamentals for Daiwa House, Haseko, MIRARTH, Ichigo and Mori Hills REIT.

## 2. Current valuation comparison: Tokyo Tatemono vs listed peers (prices 6 Aug–30 Sep 2026)

### Takeaway
On equity multiples Tokyo Tatemono looks cheap. Its forward P/E of 10.5x is about 21% below the median of the eight developers (13.35x), and its P/B of 1.12x is about 10% below their median (1.245x). Its dividend yield of 3.83% is about 18% above the median.

On enterprise-value multiples it is roughly in line with the median: EV/Sales is 4.51x vs 4.47x, and EV/EBIT is 22.3x vs 20.9x. The reason is leverage: net debt/EBIT is about 15.1x for TT against a peer median of about 10.7x. In other words, the P/E and P/B discount is mostly a leverage discount, not a cheap enterprise.

### Cited Findings
**Tokyo Tatemono (8804)**
- Market data on 25 Sep 2026:
  - Price ¥3,286.0; market cap 6,834億円, i.e. ¥683.4bn (the snippet rendered this as "6,834 billion yen").
  - PER 10.5x, PBR 1.12x, forecast dividend yield 3.83%.
  - ROA 2.70%, ROE 10.45%, equity ratio 26.0%.
  - kabuyoho also showed a forecast FY2026 DPS of ¥122 (payout 40.2%). That figure predates the August raise to ¥126 (see 1H FY2026 below).
  - Sources: [kabuyoho report](https://kabuyoho.jp/report?bcode=8804), [kabuyoho top](https://kabuyoho.jp/sp/reportTop?bcode=8804), [kabuyoho DPS](https://kabuyoho.jp/reportDps?bcode=8804)
- FY12/2025 actual results (released 12 Feb 2026):
  - Operating revenue ¥474.6bn (+2.3%), operating profit ¥95.8bn (+20.2%), ordinary profit ¥78.2bn (+9%), net profit attributable to owners ¥58.9bn (−10.6%).
  - DPS ¥105 vs ¥95, a 12th consecutive increase.
  - Sources: [japanir.jp summary](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/), [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-lifts-dividend-as-2025-profit-dips-but-outlook-strengthens), [Globe and Mail](https://www.theglobeandmail.com/investing/markets/stocks/TYTMF/pressreleases/201050/tokyo-tatemono-lifts-dividend-as-2025-profits-dip-but-2026-outlook-improves/), [TT FY2025 tanshin](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf)
- FY2025 business profit: the sources conflict.
  - A BigGo headline says "Record ¥102 Billion Business Profit, Achieving Medium-Term Plan Target One Year Early" — [BigGo Finance](https://finance.biggo.com/news/JP_8804.T_2026-02-16)
  - Another search extraction gave "¥89.4bn, up ¥10bn". This is probably the FY2024 figure; unverified.
- 1H FY2026 (Jan–Jun 2026, released 6 Aug 2026):
  - Operating revenue ¥194.4bn (−¥14.3bn YoY), operating income ¥39.8bn (+¥5.8bn), interim net profit ¥23.4bn (+13.7%), business profit ¥41.3bn (+20.0%).
  - Full-year FY2026 forecast raised to operating income ¥105.5bn and net profit ¥65.0bn.
  - DPS forecast: interim ¥61 + year-end ¥65 = ¥126, i.e. +¥4.
  - Sources: [TT 1H FY2026 highlights PDF](https://pdf.irpocket.com/C8804/xoA3/ieAo/gkiS/BBY6.pdf), [logmi](https://finance.logmi.jp/articles/385621), [Nikkei: "26年12月期10%増、年間配4円積み増し"](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/)
- Balance sheet at 30 Jun 2026:
  - Interest-bearing debt ¥1,536.6bn, up ¥191.1bn vs end-Dec 2025 (excluding lease obligations, per the extraction).
  - Net assets ¥619.0bn (+¥15.8bn); cash and deposits ¥94.2bn (vs ¥152.3bn at FY-end).
  - Total liabilities ¥1,857.2bn (+11.2%); equity ratio 24.5% (vs 26.0%).
  - Sources: search extraction of TT's 1H FY2026 disclosures — [logmi](https://finance.logmi.jp/articles/385621), [BigGo 1H supplementary](https://finance.biggo.jp/news/jpx_tdnet_140120260806512179). The extraction did not attribute each figure to a specific page.

**Mitsui Fudosan (8801)**
- Market data on 7 Sep 2026: price ¥1,507.5; market cap ¥4.06tn; PER 14.3x; PBR 1.25x; yield 2.45%; ROE 8.68%; equity ratio 32.4% — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=8801)
- FY3/2026 actual: revenue ¥2,709.747bn (+3.2%), operating income ¥397.788bn (+6.7%), net income ¥278.684bn (+12.0%).
- FY3/2027 forecast: revenue ¥2,800bn, operating income ¥410bn, net income ¥285bn.
- Interest-bearing debt ¥4,632.547bn at 31 Mar 2026 (+¥216.4bn), forecast ¥4,800bn at Mar-2027.
- Sources: [Mitsui FY3/2026 tanshin](https://www.mitsuifudosan.co.jp/corporate/ir/presentation/pdf/tanshin260513.pdf), [Mitsui forecast page](https://www.mitsuifudosan.co.jp/corporate/ir/finance/forecast/)

**Mitsubishi Estate (8802)**
- Market data on 28 Sep 2026: price ¥3,630.0; market cap ¥4,396.3bn; forecast PER 18.6x; PBR 1.61x; yield 1.35%; FY3/2027 DPS forecast ¥49; ROE 8.47%; equity ratio 31.4% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8802)
- FY3/2026 actual: revenue ¥1,746.148bn (+10.5%), operating income ¥329.730bn (+6.6%), net income ¥222.507bn (+17.5%); total assets ¥8,566.247bn.
- FY3/2027 forecast: operating income ¥370bn, net income ¥235bn.
- Sources: [MEC FY3/2026 tanshin](https://www.mec.co.jp/ir/library/2026/4Q/summary_2025_4.pdf), [R.E.port](https://www.re-port.net/article/news/0000081803/)

**Sumitomo Realty & Development (8830)**
- Market data on 14 Sep 2026: price ¥3,226.0; market cap 30,195億円 (¥3,019.5bn); forecast PER 13.4x; PBR 1.16x; yield 1.61%; ROE 9.16%; equity ratio 34.4% — [Monex Scouter](https://scouter.monex.co.jp/report/index/8830)
- FY3/2026 actual: revenue ¥1,057.765bn (+4.3%), operating income ¥299.155bn (+10.2%), ordinary ¥289.233bn, net income ¥212.535bn (+10.9%).
- FY3/2027 forecast: revenue ¥1,070bn, operating income ¥320bn, ordinary ¥300bn, net income ¥223bn (+4.9%).
- Sources: [Sumitomo FY3/2026 tanshin](https://www.sumitomo-rd.co.jp/uploads/8830_FY2025_4Q.pdf), [Nikkei](https://www.nikkei.com/article/DGXZRST0520680Y6A500C2000000/)
- 2-for-1 stock split effective 1 Jan 2026, with a buyback of up to ¥30bn — [Nikkei](https://www.nikkei.com/article/DGXZQOUB1181D0R11C25A1000000/), [Nikkei](https://www.nikkei.com/article/DGKKZO92526800R11C25A1DTD000/)

**Tokyu Fudosan HD (3289)**
- Market data on 7 Aug 2026 (stale): price ¥1,312.5; market cap ¥944.8bn; PER 9.4x; PBR 1.03x; yield 3.81%; DPS ¥48 (FY3/2026) and ¥50 forecast (FY3/2027); ROE 11.24%; equity ratio 26.3% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=3289)
- FY3/2026 actual: revenue ¥1,246.048bn (+8.3%), operating income ¥166.882bn (+18.6%), ordinary ¥147.803bn, net income ¥96.697bn (+24.7%).
- FY3/2027 plan: revenue ¥1,400bn, operating income ¥190bn, ordinary ¥161bn, net income ¥100bn.
- Interest-bearing debt ¥1,826.9bn at Mar-2026 (+¥79.1bn), plan ¥1,905bn at Mar-2027; D/E 2.0x; "EBITDA倍率" 7.4x planned; ROE about 11%.
- Sources: [Tokyu tanshin](https://www2.jpx.co.jp/disc/32890/140120260511521611.pdf), [kessan_db](https://x.com/kessan_db/status/2053997871553482815), [investalk](https://investalk.jp/3289/tokyu-fudosan-2026-03-earnings/)

**Nomura Real Estate HD (3231)**
- Market data on 4 Sep 2026: price ¥926.0; market cap ¥850.0bn; PER 9.2x; PBR 0.99x; yield 4.75%; ROE 10.68%; equity ratio 28.5% — [kabuyoho](https://kabuyoho.jp/sp/reportTop?bcode=3231)
- FY3/2026 actual: revenue ¥942.505bn (+24.4%), operating income ¥138.242bn (+16.2%), business profit ¥147.3bn, net income ¥82.880bn (+10.8%).
- FY3/2027 forecast: revenue ¥1,080bn, operating income ¥140bn, ordinary ¥125bn, net income ¥86bn.
- Interest-bearing debt ¥1,696.5bn at end of 1Q (30 Jun 2026).
- Sources: [Nomura FY3/2026 tanshin](https://www.nomura-re-hd.co.jp/ir/pdf/renketsu_20260424.pdf), [Nomura 1Q FY3/2027 deck](https://www.nomura-re-hd.co.jp/ir/pdf/2027/1Q/20260730_kessan.pdf), [logmi](https://finance.logmi.jp/articles/384360)

**Hulic (3003)**
- Market data on 25 Sep 2026: price ¥1,734.0; market cap ¥1,331.6bn; forecast PER 10.9x; PBR 1.39x; yield 3.86%; ROE 13.09%; equity ratio 26.0% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=3003)
- FY12/2025 actual: revenue ¥727.447bn (+22.9%), operating income ¥186.826bn (+14.3%), net income ¥114.334bn (+11.7%), a 14th straight record.
- FY12/2026 forecast: operating income ¥210bn, ordinary ¥185bn, net income ¥121bn.
- Sources: [Nikkei](https://www.nikkei.com/article/DGXZQOUB2927X0Z20C26A1000000/), [Hulic tanshin](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260129/20260128539955.pdf)

**Heiwa Real Estate (8803)**
- Market data on 30 Sep 2026: price ¥2,320.0; market cap 1,648億円 (¥164.8bn); PER 13.3x; PBR 1.24x; yield 4.44%; ROE 9.01%; equity ratio 28.1% — [traders.co.jp](https://www.traders.co.jp/stocks/41_8803/), [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8803)
- FY3/2026 actual: revenue ¥50.855bn (+20.9%), operating income ¥15.109bn (+14.5%), net income ¥11.032bn (+15.3%).
- FY3/2027 forecast: revenue ¥63.8bn, operating income ¥15.8bn, ordinary ¥13.0bn, net income ¥11.5bn.
- Interest-bearing debt ¥261.338bn (+6.37%); the date was not stated and is assumed to be FY-end.
- 2-for-1 split with a 30 Jun 2025 record date.
- Sources: [japanir.jp](https://japanir.jp/company/company-8803/ir/8803-20260430-02_wp_financial_summary/), [catr tanshin](https://catr.jp/tss/2b4bd/214516), [Nikkei on split](https://www.nikkei.com/article/DGXZQOFL191930Z10C25A5000000/)

**Keihanshin Building (8818)**
- Market data on 11 Sep 2026: price ¥1,118.0; market cap ¥109.1bn; forecast PER 15.2x; PBR 1.26x; yield 2.68%; ROE 5.93%; equity ratio 43.8% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8818)
- FY3/2026 actual: revenue ¥20.255bn (+3.4%), operating income ¥5.646bn (+13.3%), net income ¥4.675bn (+6.5%) — [Matsui](https://finance.matsui.co.jp/stock/8818/settlement/index), [nikkeiyosoku](https://nikkeiyosoku.com/stock/tanshin/081220260512527150/)

**Housing cross-checks**
- Sekisui House 1928, on 6 Aug 2026 (stale): price ¥3,415.0; market cap ¥2,225.2bn; PER 10.2x; PBR 1.03x; yield 4.25%; ROE 11.32%; equity ratio 42.7%; forecast ordinary profit ¥314.0bn (−4.2%); DPS ¥144 (FY1/2026) and ¥145 forecast — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=1928)
- Daito Trust 1878, on 29 Sep 2026: price ¥3,143.0; market cap ¥1,083.1bn; PER 9.5x; PBR 2.06x; yield 5.19%; ROE 20.45%; equity ratio 36.5%; forecast ordinary profit ¥140.0bn — [Monex Scouter](https://scouter.monex.co.jp/report/index/1878)
- Open House 3288, on 29 Sep 2026: price ¥7,362.0; market cap ¥859.7bn; PER 6.9x; PBR 1.38x; yield 2.78%; DPS ¥205 forecast (FY9/2026) vs ¥178; ROE 20.10%; equity ratio 38.1%; forecast ordinary profit ¥170.0bn (+21.9%) — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=3288)

**Sector context**
- Nikkei reported that all five majors guided to record net profit for FY3/2027, absorbing higher interest rates — [Nikkei](https://www.nikkei.com/article/DGXZQOUB124ZH0S6A510C2000000/)

### Inferences
**How the table is built.**
- EV = market cap + interest-bearing debt (IBD) − cash + non-controlling interests (NCI).
- Shares = market cap / price (D). Book equity = market cap / P/B (D). Total assets = book equity / equity ratio (D).
- TT's NCI is about ¥12.3bn (D): net assets ¥619.0bn minus 24.5% × total assets of ¥2,476.2bn (= ¥606.7bn shareholders' equity).
- Hybrid bonds and loans are treated as **100% debt** for EV. The 50% equity credit that rating agencies give is a credit-ratio convention; hybrids remain claims ahead of common equity.
- Cross-checks of market cap against PER × forecast net income agree within about 1% for TT, Mitsubishi, Sumitomo, Tokyu and Hulic. The gap is about 7% for Nomura (¥791bn vs ¥850bn) and Heiwa (¥153bn vs ¥165bn), possibly because treasury shares are included in kabuyoho's market cap (unverified). Using ¥791bn for Nomura moves its EV/Sales by only 0.06x.

**Table A: capital structure and EV (¥bn).** E = estimate; see the method under "Estimates used" below.

| Company | Price ¥ (date) | Shares m (D) | Mkt cap (S) | IBD [flag, date] | Cash [flag] | NCI [flag] | Net debt | EV |
|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | 3,286 (25-Sep-26) | 208.0 | 683.4 | 1,536.6 [S, 30-Jun-26] | 94.2 [S] | 12.3 [D] | 1,442.4 | **2,138.1** |
| Mitsui Fudosan | 1,507.5 (7-Sep-26) | 2,693 | 4,060.0 | 4,632.5 [S, 31-Mar-26] | 370.6 [E] | 0 [E] | 4,261.9 | 8,321.9 |
| Mitsubishi Estate | 3,630 (28-Sep-26) | 1,211 | 4,396.3 | 3,854.8 [E] | 308.4 [E] | 0 [E] | 3,546.4 | 7,942.7 |
| Sumitomo Realty | 3,226 (14-Sep-26) | 936 | 3,019.5 | 3,480.8 [E] | 278.5 [E] | 0 [E] | 3,202.3 | 6,221.8 |
| Tokyu Fudosan HD | 1,312.5 (7-Aug-26) | 720 | 944.8 | 1,826.9 [S, 31-Mar-26] | 146.2 [E] | 0 [E] | 1,680.8 | 2,625.5 |
| Nomura RE HD | 926 (4-Sep-26) | 918 | 850.0 | 1,696.5 [S, 30-Jun-26] | 135.7 [E] | 0 [E] | 1,560.8 | 2,410.8 |
| Hulic | 1,734 (25-Sep-26) | 768 | 1,331.6 | 2,026.5 [E] | 162.1 [E] | 0 [E] | 1,864.4 | 3,196.0 |
| Heiwa RE | 2,320 (30-Sep-26) | 71.0 | 164.8 | 261.3 [S, FY-end assumed] | 20.9 [E] | 0 [E] | 240.4 | 405.2 |
| Keihanshin Bldg | 1,118 (11-Sep-26) | 97.6 | 109.1 | 79.1 [E] | 6.3 [E] | 0 [E] | 72.7 | 181.8 |

**Table B: P&L (¥bn).** Last reported fiscal year (LTFY) actuals and current-year **company forecasts**. Broker consensus could not be retrieved; kabuyoho's "予" PERs are forecast-based.

| Company | LTFY | Revenue | EBIT (OI) | Net income | Fcst year | Rev fcst | OI fcst | NI fcst | Rev growth 1y (S) | EBIT margin LTFY | EBIT margin fcst |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | FY12/25 | 474.6 | 95.8 | 58.9 | FY12/26 | n/a | 105.5 | 65.0 | +2.3% | 20.2% | n/a |
| Mitsui Fudosan | FY3/26 | 2,709.7 | 397.8 | 278.7 | FY3/27 | 2,800 | 410 | 285 | +3.2% | 14.7% | 14.6% |
| Mitsubishi Estate | FY3/26 | 1,746.1 | 329.7 | 222.5 | FY3/27 | n/a | 370 | 235 | +10.5% | 18.9% | n/a |
| Sumitomo Realty | FY3/26 | 1,057.8 | 299.2 | 212.5 | FY3/27 | 1,070 | 320 | 223 | +4.3% | 28.3% | 29.9% |
| Tokyu Fudosan HD | FY3/26 | 1,246.0 | 166.9 | 96.7 | FY3/27 | 1,400 | 190 | 100 | +8.3% | 13.4% | 13.6% |
| Nomura RE HD | FY3/26 | 942.5 | 138.2 | 82.9 | FY3/27 | 1,080 | 140 | 86 | +24.4% | 14.7% | 13.0% |
| Hulic | FY12/25 | 727.4 | 186.8 | 114.3 | FY12/26 | n/a | 210 | 121 | +22.9% | 25.7% | n/a |
| Heiwa RE | FY3/26 | 50.9 | 15.1 | 11.0 | FY3/27 | 63.8 | 15.8 | 11.5 | +20.9% | 29.7% | 24.8% |
| Keihanshin Bldg | FY3/26 | 20.3 | 5.6 | 4.7 | FY3/27 | n/a | n/a | n/a | +3.4% | 27.9% | n/a |

TT LTM to Jun-2026 (D): revenue 474.6 − 208.7 + 194.4 = ¥460.3bn; operating income 95.8 − 34.0 + 39.8 = ¥101.6bn (22.1% margin); net income 58.9 − 20.6 + 23.4 = ¥61.7bn.

**Table C: multiples.** EV is at the latest price and latest balance sheet. P/E LTFY = market cap / LTFY net income (D). P/E forecast, P/B, yield and ROE are sourced (S).

| Company | EV/Sales LTFY | EV/Sales fcst | EV/EBIT LTFY | EV/EBIT fcst | P/E LTFY | P/E fcst | P/B | Div yield | ROE | ND/EBIT | ND/Equity |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | **4.51x** | n/a | **22.3x** | **20.3x** | **11.6x** | **10.5x** | **1.12x** | **3.83%** | **10.45%** | **15.1x** | **2.36x** |
| Mitsui Fudosan | 3.07x | 2.97x | 20.9x | 20.3x | 14.6x | 14.3x | 1.25x | 2.45% | 8.68% | 10.7x | 1.31x |
| Mitsubishi Estate | 4.55x | n/a | 24.1x | 21.5x | 19.8x | 18.6x | 1.61x | 1.35% | 8.47% | 10.8x | 1.30x |
| Sumitomo Realty | 5.88x | 5.81x | 20.8x | 19.4x | 14.2x | 13.4x | 1.16x | 1.61% | 9.16% | 10.7x | 1.23x |
| Tokyu Fudosan HD | 2.11x | 1.88x | 15.7x | 13.8x | 9.8x | 9.4x | 1.03x | 3.81% | 11.24% | 10.1x | 1.83x |
| Nomura RE HD | 2.56x | 2.23x | 17.4x | 17.2x | 10.3x | 9.2x | 0.99x | 4.75% | 10.68% | 11.3x | 1.82x |
| Hulic | 4.39x | n/a | 17.1x | 15.2x | 11.6x | 10.9x | 1.39x | 3.86% | 13.09% | 10.0x | 1.95x |
| Heiwa RE | 7.97x | 6.35x | 26.8x | 25.6x | 14.9x | 13.3x | 1.24x | 4.44% | 9.01% | 15.9x | 1.81x |
| Keihanshin Bldg | 8.98x | n/a | 32.2x | n/a | 23.3x | 15.2x | 1.26x | 2.68% | 5.93% | 12.9x | 0.84x |
| Sekisui House | n/a | n/a | n/a | n/a | n/a | 10.2x | 1.03x | 4.25% | 11.32% | n/a | n/a |
| Daito Trust | n/a | n/a | n/a | n/a | n/a | 9.5x | 2.06x | 5.19% | 20.45% | n/a | n/a |
| Open House | n/a | n/a | n/a | n/a | n/a | 6.9x | 1.38x | 2.78% | 20.10% | n/a | n/a |
| **Core-8 median** (ex-TT) | 4.47x | — | 20.9x | 19.4x | 14.4x | 13.35x | 1.245x | 3.25% | 9.09% | 10.7x | — |
| **TT vs core-8 median** | +1% | — | +7% | +4% | −19% | −21% | −10% | +18% | +1.4pp | +40% | — |
| Big-5 median (8801/8802/8830/3289/3231) | 3.07x | — | 20.8x | — | — | 13.4x | 1.16x | 2.45% | — | — | — |
| TT vs Big-5 median | +47% | — | +7% | — | — | −22% | −3% | +56% | — | — | — |

**Reading the tables**
- TT's forward P/E discount (−21%) and P/B discount (−10%) sit alongside a higher ROE (10.45% vs 9.09% median) and the highest leverage in the group after Heiwa (ND/EBIT 15.1x vs 10.7x). The market is pricing equity risk from leverage.
- On EV/EBIT, TT is slightly above the median (22.3x vs 20.9x LTFY; 20.3x vs 19.4x forward).
- Several balance-sheet dates make a difference:
  - TT's 1H balance sheet is seasonally heavy: net debt rose about ¥249bn in 1H26 (IBD +¥191.1bn, cash −¥58.1bn).
  - On the Dec-2025 balance sheet, TT's EV would be about ¥1,888.9bn (D) and EV/Sales 3.98x, below the median.
  - The peers' balance sheets are mostly dated Mar-2026.

**Value implied by peer medians (D)**

| Basis | Calculation | Implied price per share | vs current |
|---|---|---|---|
| Forward P/E | 13.35x × FY2026E EPS ¥312.5 (= ¥65.0bn / 208.0m) | ¥4,172 | +27% |
| P/B | 1.245x × BPS ¥2,934 (= ¥3,286 / 1.12) | ¥3,653 | +11% |
| EV/Sales | 4.47x | ¥3,208 | −2% |
| EV/EBIT | 20.9x | ¥2,614 | −20% |

**Other metrics**
- EBITDA and EV/EBITDA could not be computed for any company, because D&A was not retrievable.
- Illustrative estimate for TT only: if D&A is ¥15–25bn, FY2025 EBITDA is ¥110.8–120.8bn. That gives EV/EBITDA of 17.7–19.3x and net debt/EBITDA of 11.9–13.0x (E).
- Tokyu's planned "EBITDA倍率" of 7.4x implies EBITDA of about ¥257bn if it means IBD/EBITDA (definition unverified), or EV/EBITDA of about 10x.
- EBITDA margin: n/a.
- Implied DPS (D): TT ¥125.9 (matches ¥126); Mitsui ¥36.9; Mitsubishi ¥49.0; Sumitomo ¥51.9; Tokyu ¥50.0; Nomura ¥44.0; Hulic ¥66.9; Heiwa ¥103.0; Keihanshin ¥30.0.

**Estimates used (E), and why**
- **IBD** for Mitsubishi Estate, Sumitomo, Hulic and Keihanshin = r × derived total assets.
  - The anchors are sourced peers' IBD/total-asset ratios: Mitsui 46.2%, Tokyu 52.4%, Nomura 56.3%, Heiwa 55.3%, TT 62.1% (Jun-26).
  - r chosen: Mitsubishi Estate 0.45 (equity ratio similar to Mitsui), Sumitomo 0.46, Hulic 0.55 (equity ratio 26%, like Tokyu/Nomura/TT), Keihanshin 0.40 (equity ratio 43.8%).
  - These are consistent with analyst recollection of pre-2026 filings: Sumitomo about ¥3.4–3.5tn, Mitsubishi Estate about ¥3.7–3.9tn, Hulic about ¥2.0–2.2tn. All unverified.
- **Cash** for peers = 8% of IBD. TT's own ratio was 6.1% in Jun-26 and 11.3% in Dec-25.
- **NCI** for peers = 0. Mitsubishi Estate's NCI is believed to be material (unverified). Leaving it out understates Mitsubishi's EV/Sales and biases the peer line downward, which is conservative for TT's implied value.

### Gaps
- None of the following could be retrieved because the search budget ran out and fetch was blocked:
  - Consensus (broker) forecasts, as distinct from company guidance.
  - D&A, EBITDA, operating cash flow and FCF for every company.
  - Cash and NCI for every peer, and IBD for Mitsubishi Estate, Sumitomo, Hulic and Keihanshin.
  - Hybrid bond and loan amounts for TT, Hulic and Tokyu.
  - TT's FY2026 revenue guidance.
  - Revenue three years ago, needed for the 3-year CAGR.
  - P&L and balance sheets for Sekisui House, Daito Trust and Open House.
- Prices are not all on one date. Tokyu (7 Aug) and Sekisui House (6 Aug) are about 8 weeks old; Mitsui (7 Sep) and Nomura (4 Sep) about 4 weeks.
- Treasury-share adjustments to market cap could not be verified (see the Nomura and Heiwa cross-check above).

## 3. Tokyo Tatemono's historical multiple ranges and premium/discount to peers

### Takeaway
I could not build a verified 5–10-year history of P/E, P/B, EV/EBITDA or dividend yield: every historical-price and EPS/BPS source was blocked or out of search budget.

What can be said from sourced data:
- TT currently trades at a 10% P/B discount and a 21% forward P/E discount to the developer median.
- Its DPS has compounded at about 15% a year from FY2024 to FY2026E (¥95 → ¥105 → ¥126).
- An undated 2026 aggregator snapshot suggests the stock traded around ¥3,560 earlier in 2026, about 8% above the current ¥3,286 (unverified).

### Cited Findings
- FY12/2025 vs FY12/2024: revenue +2.3%, operating profit +20.2%, net profit −10.6% (to ¥58.9bn). DPS ¥105 vs ¥95, a 12th consecutive increase — [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-lifts-dividend-as-2025-profit-dips-but-outlook-strengthens), [japanir.jp](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/)
- FY12/2026 DPS forecast ¥126 (¥61 interim + ¥65 year-end), raised by ¥4 in August 2026 — [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/), [TT 1H highlights](https://pdf.irpocket.com/C8804/xoA3/ieAo/gkiS/BBY6.pdf)
- An undated aggregator snapshot returned by search (Google Finance / TradingEconomics) showed price ¥3,374 (prior close ¥3,378), market cap ¥740.2bn, P/E 12.57x, yield 2.95% and a 52-week range of ¥2,416–¥4,374 — [Google Finance](https://www.google.com/finance/quote/8804:TYO), [TradingEconomics](https://zh.tradingeconomics.com/8804:jp). The snapshot is internally inconsistent; see Inferences.

### Inferences
- **FY2024 history (D)** back-solved from the FY2025 growth rates: revenue about ¥463.9bn, operating profit about ¥79.7bn, net profit about ¥65.9bn.
- **EPS at about 208.0m shares (D, approximate):** FY2024 about ¥317; FY2025 ¥283; LTM to Jun-26 ¥297; FY2026E ¥312.5.
- **Current P/E on each basis (D):** FY2025A 11.6x; LTM 11.1x; FY2026E 10.5x.
- **DPS (D):** CAGR FY2024–FY2026E = (126/95)^(1/2) − 1 = 15.2% a year. FY2026E payout = 126 / 312.5 = 40.3%.
- **The aggregator snapshot does not hold together:**
  - ¥740.2bn / ¥3,374 = 219m shares, which conflicts with about 208m.
  - However, the market cap, P/E and yield agree with one another at a price of about ¥3,559: 12.57 × FY2025 EPS of ¥283 ≈ ¥3,557, and ¥105 / 2.95% ≈ ¥3,559.
  - So TT probably traded around ¥3,550 at some point after the Feb-2026 results, roughly 8% above the 25 Sep 2026 close. The ¥4,374 52-week high is unverified and may be an error.
- **Premium/discount today (D):** P/B −10% and forward P/E −21% vs the core-8 median; P/B −3% and forward P/E −22% vs the Big-5 median.

### Gaps
- None of the following could be computed or sourced: the 2016–2026 annual or daily price history, historical EPS/BPS/DPS (FY2016–FY2023), historical EV/EBITDA, historical peer-average P/E and P/B, and therefore TT's historical premium or discount.
- To fill this, compute year-end price × FY EPS/BPS from TT's Yuho (EDINET code **E03859**, per the [irbank path](https://irbank.net/E03859/reports)) and the peers' Yuho, or use MarketScreener/stockanalysis history pages once reachable.
- **Unverified indicative recollection; do not publish without checking:**
  - TT traded mostly **below 1.0x P/B** (roughly 0.7–1.0x) through 2018–2023, with P/E mostly about 8–13x and yield about 2–3.5%.
  - It re-rated toward or above 1.0x P/B in 2024–2026 alongside the sector after the TSE's March-2023 cost-of-capital/P/B request.
  - If correct, the current 1.12x would sit near the top of TT's 10-year P/B range, while its P/E (10.5x) would be mid-range.

## 4. Statistical regression: EV/Sales vs EBIT margin (peer set), and Tokyo Tatemono's implied valuation

### Takeaway
Across the eight listed developers/landlords (TT excluded from the fit), EV/Sales is strongly explained by EBIT margin: slope 0.32x per percentage point of margin, R² 0.78, n = 8, p = 0.004.

TT's fitted EV/Sales of 4.47x almost exactly matches its actual 4.51x. The base-case implied equity value is about **¥3,209/share (−2% vs ¥3,286)**.

Because net debt is about two-thirds of TT's EV, the implied equity value is very sensitive to specification:
- Across reasonable variants it ranges from about **¥2,000 to ¥4,400**.
- The supplementary P/B-vs-ROE fit (fully sourced, n = 11, R² 0.30) implies about **¥3,713 (+13%)**.

Overall, the regressions show TT priced roughly fairly on an enterprise basis, with modest upside on equity-based measures.

### Cited Findings
- All regression inputs come from the sourced figures in Section 2 (market cap, revenue, operating income, P/B, ROE, and IBD where flagged S). The dataset, with S/D/E flags per field and source URLs per row, is saved as `peer_valuation_8804.csv` in this folder.

### Inferences
**Method**
- OLS with numpy (`lstsq`), with standard errors from the residual variance. A 95% two-sided t is used for confidence and prediction intervals.
- y = EV/Sales: current EV (latest price and latest balance sheet) / LTFY revenue.
- x = EBIT margin: LTFY operating income / revenue, in %.
- Sample: Mitsui 8801, Mitsubishi 8802, Sumitomo 8830, Tokyu 3289, Nomura 3231, Hulic 3003, Heiwa 8803 and Keihanshin 8818. TT is excluded from the fit. The housing comps are excluded because their P&L could not be retrieved.
- TT valuation bridge: fitted EV/Sales × revenue → implied EV, minus net debt ¥1,442.4bn and NCI ¥12.3bn → implied equity ÷ 207.97m shares.

**R1, primary (n = 8): EV/Sales = −1.978 + 0.3195 × EBIT margin(%)**

| Statistic | Value |
|---|---|
| Intercept | −1.978 (SE 1.556, t −1.27) |
| Slope | 0.3195 (SE 0.0688, t 4.64, p 0.0035) |
| R² / adjusted R² | 0.782 / 0.746 |
| Residual SE | 1.26x |
| Observations | 8 |
| TT x (FY2025 EBIT margin) | 20.19% |
| TT fitted EV/Sales | **4.47x** |
| TT actual EV/Sales | **4.51x** (residual +0.03x, +0.8%) |
| Implied EV | ¥2,122.2bn |
| Implied equity | ¥667.4bn |
| **Implied value per share** | **¥3,209** (−2.3% vs ¥3,286) |
| 95% CI of the fitted mean | 3.35–5.59x, i.e. ¥651–¥5,767/share |
| 95% prediction interval | 1.18–7.76x, i.e. <¥0 to ¥10,718/share |

The prediction interval is uninformative at single-company level: each 0.1x of EV/Sales is worth about ¥47.5bn, or about ¥228 per share.

**Monte Carlo on the estimated (E) inputs** (20,000 draws):
- Inputs varied: IBD/TA uniform within 0.40–0.50 (Mitsubishi Estate), 0.42–0.50 (Sumitomo), 0.50–0.60 (Hulic) and 0.30–0.50 (Keihanshin); peers' cash 4–12% of IBD; peers' NCI 0–5% of market cap.
- Result: implied TT price P5 **¥3,101**, P50 **¥3,327**, P95 **¥3,563**; slope 0.306–0.342; R² 0.73–0.83.
- So the uncertainty in the estimated inputs moves the answer by only about ±7%. The specification choices below matter far more.

**Robustness variants**

| Variant | n | Slope | R² | TT fitted EV/Sales | TT actual | Implied ¥/share | vs price |
|---|---|---|---|---|---|---|---|
| R1 base (above) | 8 | 0.320 | 0.78 | 4.47x | 4.51x | 3,209 | −2% |
| R1a: TT on LTM (rev ¥460.3bn, margin 22.1%) | 8 | 0.320 | 0.78 | 5.07x | 4.65x | 4,236 | +29% |
| R1b: TT on Dec-25 balance sheet (net debt ¥1,193.2bn) | 8 | 0.320 | 0.78 | 4.47x | 3.98x | 4,407 | +34% |
| R1c: excluding Keihanshin | 7 | 0.270 | 0.84 | 4.21x | 4.51x | 2,606 | −21% |
| R1d: large caps only (excl. Heiwa, Keihanshin) | 6 | 0.207 | 0.84 | 3.95x | 4.51x | 2,021 | −38% |
| R1e: only peers with sourced IBD (Mitsui, Tokyu, Nomura, Heiwa) | 4 | 0.350 | 0.99 | 4.65x | 4.51x | 3,619 | +10% |

**Supplementary fits (fully sourced equity-market data)**

| Model | n | Intercept | Slope (t, p) | R² | TT fitted | TT actual | Implied ¥/share |
|---|---|---|---|---|---|---|---|
| R2: P/B on ROE(%), all 11 peers incl. housing | 11 | 0.885 | 0.0364 (t 1.96, p 0.08) | 0.30 | 1.27x | 1.12x | **3,713 (+13%)**; 95% PI 0.62–1.91x, i.e. ¥1,817–¥5,609 |
| R2b: P/B on ROE, core-8 developers | 8 | 1.406 | −0.017 (t −0.47, p 0.66) | 0.04 | 1.23x | 1.12x | 3,595 (+9%); no meaningful relationship |
| R3: forward P/E on forecast NI growth | 7 | 9.64 | 0.72 (t 0.65, p 0.55) | 0.08 | 17.1x | 10.5x | Not meaningful (R² ≈ 0) |

**Interpretation**
1. EBIT margin is a strong driver of EV/Sales across Japanese developers. Margin is effectively a proxy for leasing intensity: pure landlords (Heiwa, Keihanshin, Sumitomo, Hulic) have high margins and high EV/Sales, while condo- and brokerage-heavy groups (Tokyu, Nomura, Mitsui) have low margins and low EV/Sales.
2. TT sits on the line, so on an EV basis it is fairly valued relative to peers given its mix. Its apparent cheapness on P/E (−21%) and P/B (−10%) is largely explained by higher leverage (ND/EBIT 15.1x vs 10.7x).
3. The implied value per share is unusually sensitive (¥2,000–¥4,400) because equity is only about 32% of EV. The balance-sheet date alone (Jun-26 vs Dec-25) moves the answer by about ¥1,200/share.
4. Within the developer group, P/B is not explained by ROE (R² 0.04). This suggests the market prices asset quality, location and NAV rather than ROE; Mitsubishi Estate, for example, has the highest P/B with the lowest ROE.

### Gaps
- Forward-basis EV/Sales regressions were not run: revenue guidance is missing for TT, Mitsubishi Estate, Hulic and Keihanshin (n would have been 5).
- EV/EBITDA vs ROE could not be run because EBITDA is unavailable.
- Four of the eight regression observations rely on estimated IBD, and all peers' cash and NCI are estimated. The Monte Carlo bounds this effect at about ±7%, but the results should be labelled indicative until the balance sheets are verified.
- The housing comps could not enter the EV/Sales fit.

## 5. M&A in Japanese real estate, 2019–2026: precedents, multiples and TOB-premium norms

### Takeaway
No M&A precedent data could be verified in this session: the search budget ran out before this workstream, and all M&A, news and TDnet hosts were egress-blocked. The precedent list below comes from analyst background knowledge, carries confidence labels, and **must be verified** (TDnet TOB filings, press releases, MARR/RECOF) before use.

From memory, the pattern is:
- Strategic parent buyouts and white-knight deals (Tokyo Dome, NTT UD, Daibiru, Unizo) cleared at large premiums, often 40–100% for contested or underpriced targets.
- Foreign PE and sovereign money has been most active in carve-outs and asset deals (hotels, landmark offices, AM platforms), not in whole-company take-privates of large developers.

### Cited Findings
- None retrieved in this session (see Gaps).
- Related capital-policy signals from peers (context for M&A and activism pressure):
  - Mitsubishi Estate announced a ¥100bn buyback alongside FY3/2026 guidance, and later a further buyback with its upgraded forecast — [Nikkei](https://www.nikkei.com/article/DGXZQOUC125QV0S5A510C2000000/), [Nikkei](https://www.nikkei.com/article/DGXZQOUB095TZ0Z00C26A2000000/)
  - Sumitomo Realty did a 2-for-1 split plus a buyback of up to ¥30bn (Nov 2025) — [Nikkei](https://www.nikkei.com/article/DGKKZO92526800R11C25A1DTD000/)
  - Heiwa RE raised its MTP final-year targets to EPS of at least ¥160 and operating income of at least ¥15bn — [japanir.jp](https://japanir.jp/company/company-8803/ir/8803-20260130-01_wp_business_update/)

### Inferences
- The relevant reference points for a TT bid are:
  - (a) Japanese TOB premiums, which are commonly about 30–50% over the 1-month average (unverified).
  - (b) Contested real-estate deals (Unizo), where competition pushed the final price to roughly double the first bid.
  - (c) Asset-level pricing for prime Tokyo offices, which would underpin a NAV-based bid.
- Section 6 applies 20–60% premium scenarios to TT.

### Gaps
**Precedent table from analyst background knowledge. Unverified; confidence in brackets.** Deal value, premium, P/B, P/NAV and cap rates are left blank where I am not confident.

| Target | Acquirer | Announced | Price / value | Premium | Notes |
|---|---|---|---|---|---|
| Unizo Holdings (3258) | Employee buyout backed by Lone Star (after H.I.S. hostile bid, Fortress white knight, Blackstone interest) | 2019–2020 | ¥6,000/share final [high]; first H.I.S. bid ¥3,100 [medium] | About 2x the first bid [medium] | Benchmark for contested Japanese RE takeovers |
| NTT Urban Development | NTT (parent, ~67% before) | May 2020 [medium-high] | ¥1,400/share TOB [medium-high] | n/v | Parent-subsidiary buyout; NTT UD delisted |
| Tokyo Dome | Mitsui Fudosan (Yomiuri took 20% afterwards) | Nov 2020 [medium-high] | ¥1,300/share; about ¥120bn [medium] | n/v (large) | Activist-influenced (Oasis) [medium] |
| Daibiru | Mitsui O.S.K. Lines (~51% before) | 2021–22 [low] | About ¥1,700/share [low] | n/v | Parent buyout of an office landlord |
| Kenedix | ARA (later part of ESR) | 2021 [medium] | n/v | n/v | RE asset-manager take-private |
| ARA Asset Management | ESR Cayman | 2021–22 [medium] | About US$5.2bn [medium] | n/a (private) | Platform deal |
| 31 Seibu Prince hotels/assets | GIC | Feb 2022 [medium-high] | About ¥150bn [medium] | n/a (asset) | Sale-and-operate structure |
| M.D.C. Holdings (US) | Sekisui House | Jan 2024 [high] | US$63/share; about US$4.9bn [high] | About 18% [medium] | Japanese housebuilder outbound |
| Mitsubishi Corp.-UBS Realty (J-REIT AM) | KKR | Dec 2024–2025 [medium] | About ¥230bn [low-medium] | n/a | AM platform for JMF/IIF |
| Tokyo Garden Terrace Kioicho | Blackstone (from Seibu HD) | 2025 [low-medium] | About ¥400bn [low] | n/a (asset) | Landmark office/hotel asset sale |
| Sapporo HD real-estate business (Yebisu Garden Place etc.) | KKR & PAG consortium | 2025 [low-medium] | n/v | n/a | Carve-out under activist pressure |
| Aeon Mall (and Aeon Delight) | Aeon (share exchange) | 2025 [medium] | n/v | n/v | Parent buyout of a listed mall developer |
| KDX Realty + Kenedix Residential Next + Kenedix Retail | J-REIT merger | Effective Nov 2023 [medium-high] | n/v | n/v | J-REIT consolidation |
| Mori Trust Sogo REIT + Mori Trust Hotel REIT | J-REIT merger | 2023 [medium] | n/v | n/v | J-REIT consolidation |
| Star Asia Investment + Sakura Sogo REIT | J-REIT merger | 2020 [medium] | n/v | n/v | Activist-contested merger |
| Daikyo | ORIX | 2019 [medium] | n/v | n/v | Condo developer take-private |

- **Real-estate-related activism (unverified):** Elliott vs Tokyo Gas (real-estate holdings, 2024–25), and Dalton/Rising Sun vs Fuji Media HD (Sankei Building real estate, 2025).
- **Not verified at all:** the 2025–2026 TOBs and MBOs named in the brief (Tosei, Sun Frontier, Starts, MIRARTH/Takara Leben, Ichigo, Shinoken) and any Hulic transactions. I cannot confirm whether any occurred or on what terms.
- **Not available:** TOB-premium statistics (MARR/RECOF/Nikkei median premiums 2023–2026), transaction EV/EBITDA, P/B, P/NAV and cap rates for every deal.

## 6. Takeover assessment: is Tokyo Tatemono a plausible target?

### Takeaway
TT is a plausible but **not probable** whole-company target.

In its favour as a target:
- P/B of 1.12x and forward P/E of 10.5x are both below peers.
- Earnings momentum is strong: 1H26 business profit +20%, FY26 net income guidance raised to ¥65bn, and medium-term-plan (MTP) targets a year early.
- Its central-Tokyo (Yaesu/Kyobashi/Nihonbashi) land bank would be strategic for the majors.
- Japan's 2023 takeover guidelines and TSE pressure make boards more open to offers.

Against a takeover:
- An outright bid needs about ¥0.9–1.0tn of equity plus ¥1.4–1.5tn of net debt to assume (EV about ¥2.3–2.5tn at a 30–50% premium).
- Leverage is already high (ND/EBIT about 15x, net D/E about 2.4x), leaving little room for LBO debt.
- Likely stable Fuyo/Yasuda-lineage shareholders (unverified).

More likely outcomes are activism (asset sales, buybacks, REIT drop-downs) or a friendly strategic combination. An indicative takeout range is **¥4,270–¥4,930/share**: a 30–50% premium, 1.46–1.68x P/B, 13.7–15.8x FY26E P/E and 22–24x FY26E EV/EBIT.

### Cited Findings
- **TT market data (25 Sep 2026):** price ¥3,286; market cap about ¥683.4bn; PER 10.5x; PBR 1.12x; yield 3.83%; ROE 10.45% — [kabuyoho](https://kabuyoho.jp/report?bcode=8804)
- **TT balance sheet (30 Jun 2026):** IBD ¥1,536.6bn; cash ¥94.2bn; net assets ¥619.0bn; equity ratio 24.5% — [logmi](https://finance.logmi.jp/articles/385621) (search extraction)
- **Earnings momentum:**
  - 1H FY2026 business profit ¥41.3bn (+20%) and interim net profit ¥23.4bn (+13.7%).
  - FY2026 operating income guidance ¥105.5bn and net profit ¥65.0bn (raised); DPS ¥126.
  - Headline that the main quantitative targets of the current MTP are expected to be met one year early.
  - Sources: [logmi](https://finance.logmi.jp/articles/385621), [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/), [TT 1H highlights](https://pdf.irpocket.com/C8804/xoA3/ieAo/gkiS/BBY6.pdf)
- **FY2025 business profit:** a record ¥102bn, reaching the MTP target one year early (headline) — [BigGo](https://finance.biggo.com/news/JP_8804.T_2026-02-16)
- **Size of potential strategic acquirers:** Mitsui Fudosan market cap ¥4.06tn, Mitsubishi Estate ¥4,396.3bn, Sumitomo Realty ¥3,019.5bn, Hulic ¥1,331.6bn — [kabuyoho 8801](https://kabuyoho.jp/reportTarget?bcode=8801), [kabuyoho 8802](https://kabuyoho.jp/reportTop?bcode=8802), [Monex 8830](https://scouter.monex.co.jp/report/index/8830), [kabuyoho 3003](https://kabuyoho.jp/reportTop?bcode=3003)
- **Acquirers' own leverage:** Mitsui Fudosan IBD ¥4,632.5bn at Mar-2026, forecast ¥4.8tn at Mar-2027 — [Mitsui tanshin](https://www.mitsuifudosan.co.jp/corporate/ir/presentation/pdf/tanshin260513.pdf)
- **Interest-rate backdrop:** the majors' FY3/2027 plans "absorb higher rates" — [Nikkei](https://www.nikkei.com/article/DGXZQOUB124ZH0S6A510C2000000/)

### Inferences
**Takeout arithmetic (D).** Uses 207.97m shares, BPS ¥2,934, FY26E EPS ¥312.5, net debt ¥1,442.4bn + NCI ¥12.3bn (Jun-26), FY26E OI ¥105.5bn and LTM OI ¥101.6bn.

| Premium | Price ¥ | Equity ¥bn | EV ¥bn | P/B | P/E FY26E | P/E FY25A | EV/EBIT FY26E | EV/EBIT LTM | EV/Sales FY25 |
|---|---|---|---|---|---|---|---|---|---|
| 0% | 3,286 | 683 | 2,138 | 1.12x | 10.5x | 11.6x | 20.3x | 21.0x | 4.51x |
| 20% | 3,943 | 820 | 2,275 | 1.34x | 12.6x | 13.9x | 21.6x | 22.4x | 4.79x |
| 30% | 4,272 | 888 | 2,343 | 1.46x | 13.7x | 15.1x | 22.2x | 23.1x | 4.94x |
| 40% | 4,600 | 957 | 2,411 | 1.57x | 14.7x | 16.2x | 22.9x | 23.7x | 5.08x |
| 50% | 4,929 | 1,025 | 2,480 | 1.68x | 15.8x | 17.4x | 23.5x | 24.4x | 5.23x |
| 60% | 5,258 | 1,093 | 2,548 | 1.79x | 16.8x | 18.6x | 24.2x | 25.1x | 5.37x |

**Peer-anchored cross-checks (D):**
- Mitsubishi Estate's P/B of 1.61x × TT BPS = ¥4,724 (+44%).
- Peer-median forward P/E of 13.35x = ¥4,172 (+27%).
- Mitsubishi Estate's forward P/E of 18.6x = ¥5,813 (+77%, the ceiling of the peer range).

**NAV / P/NAV (ILLUSTRATIVE ONLY).** TT's unrealised gains on rental properties were not retrievable. The grid below assumes a 30.62% tax rate on the gains:

| Assumed pre-tax unrealised gain | NAV/share | P/NAV at ¥3,286 | P/NAV at a 40% premium |
|---|---|---|---|
| ¥400bn | ¥4,268 | 0.77x | 1.08x |
| ¥600bn | ¥4,936 | 0.67x | 0.93x |
| ¥800bn | ¥5,603 | 0.59x | 0.82x |
| ¥1,000bn | ¥6,270 | 0.52x | 0.73x |

If TT's disclosed gain is about ¥600bn or more (to be verified from the Yuho "賃貸等不動産" note), even a 40% premium bid would still be below NAV. That is the core of a PE or strategic investment case.

**Reasons TT could be a target**
1. The discount to peers on equity multiples (P/B −10%, forward P/E −21%) and a probable NAV discount.
2. A visible earnings ramp: OI +20% in FY2025, +10% guided for FY2026, and MTP targets met early.
3. A 3.83% yield and 40% payout leave room for re-leveraging by a buyer with a lower cost of capital.
4. Japan's pro-M&A governance shift. METI's "Guidelines for Corporate Takeovers" (Aug 2023) ask boards to give sincere consideration to bona fide offers, and the TSE pressures companies below 1x P/B. Both are unverified in this session.
5. Continued unwinding of cross-shareholdings reduces the stable-shareholder block (TT-specific data unverified).
6. Strategic scarcity: a large central-Tokyo land bank and redevelopment pipeline next to Mitsui's Nihonbashi and Mitsubishi's Marunouchi.

**Impediments**
1. **Size.** EV of about ¥2.1tn today (¥2.3–2.5tn at a 30–50% premium) would make this the largest Japanese real-estate take-private by a wide margin, if the precedent list in Section 5 is right.
2. **Leverage.**
   - ND/EBIT is 15.1x vs a 10.7x peer median; IBD/equity is about 2.5x at Jun-26.
   - A PE buyer could add little acquisition debt, so it would need a large equity cheque plus asset sales or recapitalisation (e.g. drop-downs to a sponsored J-REIT; JPR sponsorship unverified).
   - Rising JGB yields raise the bar.
3. **Earnings mix.** Condo and property-sale gains are cyclical, and FY2025 net income fell 10.6%.
4. **Shareholder structure.** Yasuda/Fuyo lineage: TT was founded by Zenjiro Yasuda, with group links to Mizuho, Meiji Yasuda and Sompo. All unverified, as is the current register. The Banking Act's 5% rule limits any single bank's stake.
5. **Unknowns.** Any takeover-defence plan and FEFTA screening exposure are unverified. Real estate is generally not a designated core sector, but data-centre or infrastructure-adjacent assets could trigger prior notification.
6. **Precedent.** Japanese majors have not historically made hostile bids for one another.

**Plausible acquirers, ranked (inference)**
1. Activist-driven partial outcomes, the most likely path: buybacks, asset recycling, REIT spin-out.
2. A friendly strategic tie-up with Hulic. Similar Tokyo focus and possible Fuyo/Mizuho kinship, but Hulic's 26% equity ratio limits a cash bid, so a merger or share exchange is more plausible.
3. A domestic major (Mitsui, Mitsubishi or Sumitomo). They have the balance-sheet scale, but cultural and antitrust-optics barriers and their own leverage (Mitsui IBD guided to ¥4.8tn) make this low probability.
4. A global PE or sovereign club deal (e.g. Blackstone, KKR, Brookfield, GIC, PAG; all active in Japanese real-estate carve-outs per unverified recollection). Feasible only with heavy asset monetisation.
5. Trading houses or insurers as white knights or anchor holders rather than lead bidders.

**Indicative bid range.** A friendly bid would likely need a 30–50% premium, i.e. ¥4,270–¥4,930 (1.46–1.68x P/B, 13.7–15.8x FY26E P/E, about 22–24x FY26E EV/EBIT). A contested process (Unizo-type) could exceed this toward the NAV-based value.

### Gaps
- TT's shareholder register: top holders, the Fuyo/Mizuho group stake and the cross-shareholdings TT holds or is subject to.
- Whether TT has a takeover defence (poison pill) and its status at the AGM.
- Hybrid bond and loan amounts and their terms.
- Disclosed fair value and unrealised gains of rental properties (the key NAV input).
- The exact METI guideline text and Japanese TOB-premium statistics.
- FEFTA classification of TT's businesses.
- Whether any 2025–2026 press reports linked TT to activists or bidders. None were seen in this session's limited searches; that is not evidence of absence.

## 7. Tokyo Tatemono's own acquisitions, 2016–2026

### Takeaway
I could not compile a verified acquisition table: the search budget ran out and TT's IR, EDINET and TDnet were blocked.

The only sourced signal is that TT's net debt rose about ¥249bn in 1H FY2026 (IBD +¥191.1bn, cash −¥58.1bn), consistent with heavy property or land investment in the half. Whether this includes any corporate acquisition is unverified.

### Cited Findings
- **1H FY2026 balance-sheet movement:**
  - Interest-bearing debt +¥191.1bn to ¥1,536.6bn; cash and deposits ¥152.3bn → ¥94.2bn.
  - Total liabilities +11.2% to ¥1,857.2bn; equity ratio 26.0% → 24.5%.
  - Source: search extraction of TT's 1H FY2026 disclosures — [logmi](https://finance.logmi.jp/articles/385621)
- **TT's EDINET filer code is E03859** (from the irbank path), for retrieving Yuho business-combination notes — [irbank](https://irbank.net/E03859/reports)

### Inferences
- The 1H FY2026 investment burst of about ¥249bn of net-debt increase is large: about 36% of TT's market cap and about 21% of Dec-2025 net debt (¥1,193.2bn). Its composition should be checked against the 1H cash-flow statement:
  - Property and land acquisitions (inventories and fixed assets), versus
  - Equity investments (overseas JV stakes, data-centre or logistics platforms).

### Gaps
- **The full 2016–2026 acquisition table** (target, date, cost, multiples) needs TT's Yuho "企業結合等関係" notes for FY2016–FY2025, TT news releases (tatemono.com/news), and the MARR/RECOF databases.
- **Areas to check (analyst background knowledge, unverified):**
  - The parking business (Nihon Parking group company: acquisition date and cost).
  - Overseas residential/office JV investments via TT's Asia platform (China, Thailand, Vietnam, Indonesia, Singapore stakes).
  - Logistics (T-LOGI) and data-centre development entries.
  - Asset-management capabilities (sponsorship of Japan Prime Realty; private-REIT/fund AM entities).
  - Major single-asset acquisitions tied to Yaesu/Kyobashi/Nihonbashi redevelopment.
- **Transaction multiples** for any TT acquisition are not available.
