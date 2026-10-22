# Tokyo Tatemono (8804 JP): Valuation vs Peers and Own History, Peer Regression, Japanese Real-Estate M&A and Takeover Assessment

> **How these notes were researched (as of 4 Oct 2026). Read this first.**
>
> **Access limits.** The session's network egress policy blocked direct page fetches from every finance, IR, TDnet, EDINET and news host I tried, including stockanalysis, MarketScreener, Kabutan, Yahoo! Finance Japan, Google Finance, tatemono.com, irpocket and jpx.co.jp. The session-wide WebSearch budget (200 calls shared by all researchers) ran out after about 25 searches by this workstream.
>
> **Source types and flags.**
> 1. **Search-engine extractions of named pages (S).** I could not open these pages myself.
> 2. **GitHub raw mirrors, which were reachable (S):**
>    - **Shikiho mirror.** The Toyo Keizai 会社四季報オンライン page for each company, mirrored in `edamame384/stock_selection`.
>      - Pages were captured on 12–13 Mar 2026.
>      - Balance sheets are as of Sep/Oct 2025.
>      - Cash flow, D&A and capex are for the last fiscal year.
>      - The "実績PER 高値平均/安値平均" fields are Shikiho's historical P/E band. My understanding is that this is the average P/E at the yearly high and low price over the last 3 fiscal years; that definition is unverified.
>    - **EDINET mirror.** EDINET daily filing indices in `code4fukui/EDINET`, covering Nov 2022–Oct 2026. I scanned all 1,024 business days.
>    - **TDnet cache.** One cached TDnet daily list (13 May 2026).
> 3. **Parallel workstream notes in this folder.** Specifically `nav_forensic_risks.md`, `management_board_shareholders.md`, `industry_moats_strategy_stakes.md`, `financials_kpis_capital_structure.md` and `stock_prices_8804.csv`, cited with the original URLs they give.
> 4. **D** marks figures derived arithmetically by me. **E** marks analyst estimates, which are always labelled.
>
> **Units, file and code.** Money is in JPY bn unless stated. The regression dataset is `peer_valuation_8804.csv` (same folder; 12 companies × 69 fields, with flags and source URL per row). Python/numpy code is kept in the session scratchpad.

## 1. Competitor list: public and private, tickers and listed/unlisted status

### Takeaway
**Core listed comparables:**
- The five integrated Tokyo majors: Mitsui Fudosan 8801, Mitsubishi Estate 8802, Sumitomo Realty 8830, Tokyu Fudosan HD 3289 and Nomura RE HD 3231.
- Hulic 3003.
- Two small office landlords: Heiwa RE 8803 and Keihanshin Building 8818.

**Cross-checks for TT's Brillia condo/residential business:** Sekisui House 1928, Daito Trust 1878 and Open House 3288.

**Main unlisted competitors:**
- Independent developers: Mori Building (which sponsors the listed Mori Hills REIT 3234), Mori Trust and Nippon Steel Kowa.
- Delisted NTT UD.
- The condo and brokerage subsidiaries of the majors.

Hulic stands out as TT's natural "Fuyo/Yasuda-family" peer:
- Hulic's register includes Meiji Yasuda Life, Fuyo General Lease, Yasuda Real Estate and Yasuda Logistics.
- TT and Hulic hold each other's shares.

### Cited Findings
- **TT's market and listing.** TSE Prime 8804; Shikiho describes TT as 「旧安田系の総合不動産。賃貸ビルとマンションが主力」 (a former-Yasuda-group comprehensive developer whose mainstays are rental buildings and condominiums). Shikiho's listed comparison companies are 3231 Nomura RE HD and 3289 Tokyu Fudosan HD. Listed May 1949; founded Oct 1896. — [Shikiho mirror 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **Listed peers.** All were retrieved with quote data. Fiscal year-ends:
  - March: 8801, 8802, 8830, 3289, 3231, 8803, 8818 and 1878.
  - December: TT and Hulic.
  - January: Sekisui House.
  - September: Open House.
  - Sources: [Shikiho mirror 8801](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8801.txt), [8802](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8802.txt), [8830](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8830.txt), [3289](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3289.txt), [3231](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3231.txt), [3003](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3003.txt), [8803](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8803.txt), [8818](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8818.txt), [1928](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/1928.txt), [1878](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/1878.txt), [3288](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3288.txt)
- **Controlling or anchor holders at peers (Shikiho, register dates Jun/Sep 2025):**
  - Tokyu Corp holds 15.9% of Tokyu Fudosan HD.
  - Nomura Holdings holds 35.2% of Nomura RE HD (treasury 4.8%).
  - Taisei Corp holds 17.3% of Heiwa RE; Mitsubishi Estate holds 4.5% of Heiwa; Aya Nomura (野村絢) holds 5.3%; treasury is 13.6%.
  - Founder Masaaki Arai holds 31.6% of Open House; Ichigo Trust holds 12.6%.
  - Ginsen holds 13.1% of Keihanshin; SMBC holds 4.3%.
  - Sources: [Shikiho 3289](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3289.txt), [3231](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3231.txt), [8803](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8803.txt), [3288](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3288.txt), [8818](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8818.txt)
- **Hulic's top holders (Jun 2025):** Master Trust 9.3%, Meiji Yasuda Life 6.2%, Fuyo General Lease 5.2%, Yasuda Real Estate 4.0%, Yasuda Logistics (安田倉庫) 3.7%. — [Shikiho 3003](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3003.txt)
- **TT–Hulic cross-holding:**
  - TT holds 20,374,433 Hulic shares (2.65%), and Hulic holds 2,636k TT shares (1.22%) — [kabutan Hulic holders](https://kabutan.jp/stock/holder?code=3003), [Buffett Code](https://www.buffett-code.com/shareholder/1f2c707ea4a457a113d417a837a2265a) (via `industry_moats_strategy_stakes.md`)
  - TT filed a 変更報告書 (change in large-shareholding) on Hulic (E00523) on 12 Dec 2024, doc S100UWWV — [EDINET index 2024-12-12](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-12-12.csv)
- **Listed REIT links:**
  - Japan Prime Realty (8955): "東京建物がスポンサー" (TT is the sponsor); TT held 2.9% of units at Jun 2025 — [Shikiho 8955](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8955.txt). TT held 3.03% at Mar 2026, and the AM is 100% TT-owned — [JPR 運用体制報告書](https://www.jpr-reit.co.jp/file/ir_library_other_file-e1fd4de66a9a0b87bc1127d8cbab0e2741bf0bb7.pdf) (via `industry_moats_strategy_stakes.md`)
  - Mori Hills REIT (3234): "森ビル母体" (Mori Building is the parent), with Mori Building holding 19.3% — [Shikiho 3234](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3234.txt)
- **NTT Urban Development REIT (8956)** remains listed (¥145,700/unit, market cap ¥213.9bn, Mar 2026) — [Shikiho 8956](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8956.txt)

### Inferences

**Competitor table**

| Company | Ticker / status | Role vs TT | Status verified this session? |
|---|---|---|---|
| Mitsui Fudosan | 8801, listed TSE Prime | #1 integrated developer; Nihonbashi/Yaesu neighbour | Yes |
| Mitsubishi Estate | 8802, listed | Marunouchi landlord; adjacent to TT's Otemachi/Yaesu assets | Yes |
| Sumitomo Realty & Development | 8830, listed | Tokyo office and condo; highest margin among the big 5 | Yes |
| Tokyu Fudosan HD | 3289, listed (Tokyu Corp 15.9%) | Similar size; condos, brokerage | Yes |
| Nomura RE HD | 3231, listed (Nomura HD 35.2%) | Closest condo-mix and size comparable | Yes |
| Hulic | 3003, listed | Central-Tokyo landlord; Fuyo/Yasuda register; cross-holding with TT | Yes |
| Heiwa Real Estate | 8803, listed (Taisei 17.3%) | Small office landlord | Yes |
| Keihanshin Building | 8818, listed | Small Osaka landlord; widens the margin range | Yes |
| Sekisui House / Daito Trust / Open House | 1928 / 1878 / 3288, listed | Housing and condo cross-checks | Yes |
| Daiwa House | 1925, listed | Possible extra comparable; Mar-2026 data only, so not used | Yes (Mar-26 data) |
| Japan Prime Realty / Mori Hills REIT / NTT UD REIT | 8955 / 3234 / 8956, listed J-REITs | Sponsor vehicles of TT / Mori Building / NTT UD; excluded from EV/Sales (REIT structure) | Yes |
| Mori Building | Unlisted (sponsors 3234) | Roppongi, Toranomon and Azabudai mega-projects | Partly (via 3234 page) |
| Mori Trust | Unlisted | Office and hotels | No |
| Nippon Steel Kowa Real Estate | Unlisted | Office developer; TT's JV partner in Australia (with Lendlease), per `business_model_supply_chain.md` | Partly |
| NTT Urban Development / NTT Urban Solutions | Unlisted (NTT UD delisted after the 2020 NTT TOB, unverified) | Office and condo | No |
| Tokyu Land; Mitsubishi Jisho Residence; Sumitomo Fudosan Hanbai; Mitsui Fudosan Residential; Nomura RE Development | Unlisted subsidiaries of 3289 / 8802 / 8830 / 8801 / 3231 | Condo and brokerage competitors | No (background knowledge) |

**Inclusion logic**
- The eight developers and landlords form the regression set because they report J-GAAP operating income on the same basis as TT.
- The housing names are added as a robustness set.
- REITs are excluded from EV/Sales.

### Gaps
- I did not re-verify the subsidiary status of the unlisted condo arms or the 2020 delisting of NTT UD in this session.
- Mori Trust's and Nippon Steel Kowa's financials are unavailable.

## 2. Current valuation: Tokyo Tatemono vs listed peers (prices 6 Aug–30 Sep 2026; TT ¥3,286 on 25 Sep; latest ¥3,211 on 2 Oct)

### Takeaway
On equity multiples TT is cheap:
- Forward P/E 10.5x vs a 13.35x developer median (−21%).
- P/B 1.12x vs 1.245x (−10%).
- Dividend yield 3.83% vs 3.25% (+18%).
- ROE is higher (10.45% vs 9.09%), and 3-year revenue CAGR is faster (10.7% vs 6.7%).

On enterprise multiples TT is in line or slightly rich:
- EV/Sales 4.51x vs 4.52x.
- EV/EBIT 22.3x vs 22.0x.
- EV/EBITDA 18.0x vs 17.0x.

That is because TT is the most levered company in the group: net debt/EBITDA 12.1x vs a 9.2x median, and net debt/equity 2.36x vs 1.61x. The equity discount is a leverage discount, not a cheap enterprise.

At the latest price of ¥3,211 (2 Oct 2026): P/B 1.09x, P/E 10.3x, yield 3.92%, EV ¥2,122.5bn.

### Cited Findings
**Tokyo Tatemono (8804)**
- **25 Sep 2026 market data.** Price ¥3,286; market cap 6,834億円 (¥683.4bn); PER 10.5x; PBR 1.12x; forecast yield 3.83%; ROE 10.45%; equity ratio 26.0% — [kabuyoho](https://kabuyoho.jp/report?bcode=8804)
- **Latest close found.** ¥3,211 on 2 Oct 2026; 2026 high ¥4,374 (27 Feb); low ¥3,083 (28 May) — [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/), [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt) (via `stock_prices_8804.csv`)
- **FY12/2025 results.**
  - Revenue ¥474.586bn (+2.3%); operating income ¥95.763bn (+20.2%); ordinary ¥78.187bn; net income ¥58.879bn (−10.6%).
  - EPS ¥283.08; DPS ¥105 (12th consecutive increase).
  - Business profit (new definition) ¥89.4bn.
  - Sources: [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt), [japanir.jp](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/), [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-lifts-dividend-as-2025-profit-dips-but-outlook-strengthens), [FY2025 tanshin](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf) (business profit via `financials_kpis_capital_structure.md`)
  - A BigGo headline speaks of a "Record ¥102 Billion Business Profit"; that figure is the FY2026 business-profit guidance, not FY2025 actual — [BigGo](https://finance.biggo.com/news/JP_8804.T_2026-02-16)
- **1H FY2026 (6 Aug 2026).**
  - Revenue ¥194.4bn; OI ¥39.8bn (+¥5.8bn); NI ¥23.4bn (+13.7%); business profit ¥41.3bn (+20.0%).
  - FY2026 guidance: OI ¥105.5bn and NI ¥65.0bn (raised); DPS ¥126 (¥61 + ¥65).
  - Sources: [1H highlights](https://pdf.irpocket.com/C8804/xoA3/ieAo/gkiS/BBY6.pdf), [logmi](https://finance.logmi.jp/articles/385621), [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/)
  - FY2026 revenue guidance is ¥524.0bn (set 12 Feb 2026) — [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **30 Jun 2026 balance sheet.** Interest-bearing debt ¥1,536.6bn (+¥191.1bn in the half); cash and deposits ¥94.2bn (vs ¥152.3bn); net assets ¥619.0bn; total liabilities ¥1,857.2bn; equity ratio 24.5% — search extraction of 1H disclosures ([logmi](https://finance.logmi.jp/articles/385621))
- **31 Dec 2025 debt.** IBD ¥1,343.874bn — [edinetdb](https://edinetdb.jp/company/E03859) (via `coordinator_gap_fill.md`)
- **Cash-flow items (Shikiho).**
  - D&A: FY12/2024 ¥22.3bn; FY12/2025 forecast ¥23.0bn.
  - Capex FY2024 ¥125.7bn.
  - Operating CF: FY2025 ¥32.106bn; FY2024 ¥18.9bn.
  - Investing CF FY2024 −¥142.0bn.
  - Sources: [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **Credit and hybrids.**
  - JCR long-term rating upgraded to A — [JCR](https://jcr.co.jp/download/10194f47b690f5b8ad8096559f9868ffb09165b80805048511/25d0289.pdf)
  - On 30 May 2025 JCR rated TT's dated subordinated (hybrid) bonds BBB+: 37-year maturity, callable after 7 years — [matsunosuke.jp](https://matsunosuke.jp/tokyo-tatemono-bond/)
  - The hybrid amount and equity credit were not retrieved. Both items via `coordinator_gap_fill.md`.

**Peers: market data from search extractions of kabuyoho/Monex; fundamentals from company results and the Shikiho mirror**
- **Mitsui Fudosan.**
  - Market (7 Sep 2026): ¥1,507.5; market cap ¥4.06tn; PER 14.3x; PBR 1.25x; yield 2.45%; ROE 8.68% — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=8801)
  - FY3/2026 actual: revenue ¥2,709.747bn; OI ¥397.788bn; NI ¥278.684bn.
  - FY3/2027 guidance: ¥2,800bn / ¥410bn / ¥285bn.
  - IBD ¥4,632.547bn (Mar-26) — [tanshin](https://www.mitsuifudosan.co.jp/corporate/ir/presentation/pdf/tanshin260513.pdf)
  - Shikiho items: cash ¥163.2bn (Mar-25); D&A ¥140.5bn (FY3/25), forecast ¥140bn; OCF ¥599.3bn; ICF −¥321.9bn — [Shikiho 8801](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8801.txt)
- **Mitsubishi Estate.**
  - Market (28 Sep 2026): ¥3,630; market cap ¥4,396.3bn; PER 18.6x; PBR 1.61x; yield 1.35%; ROE 8.47% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8802)
  - FY3/2026 actual: revenue ¥1,746.148bn; OI ¥329.730bn; NI ¥222.507bn.
  - FY3/2027 guidance: OI ¥370bn; NI ¥235bn — [MEC tanshin](https://www.mec.co.jp/ir/library/2026/4Q/summary_2025_4.pdf)
  - Shikiho items: IBD ¥3,469.29bn (Sep-25); cash ¥256.8bn (Mar-25); D&A forecast ¥107bn; OCF ¥324.1bn; Meiji Yasuda 3.3% holder — [Shikiho 8802](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8802.txt)
- **Sumitomo Realty.**
  - Market (14 Sep 2026): ¥3,226; market cap 30,195億円; PER 13.4x; PBR 1.16x; yield 1.61%; ROE 9.16% — [Monex](https://scouter.monex.co.jp/report/index/8830)
  - FY3/2026 actual: revenue ¥1,057.765bn; OI ¥299.155bn; NI ¥212.535bn.
  - FY3/2027 guidance: ¥1,070bn / ¥320bn / ¥223bn — [tanshin](https://www.sumitomo-rd.co.jp/uploads/8830_FY2025_4Q.pdf), [Nikkei](https://www.nikkei.com/article/DGXZRST0520680Y6A500C2000000/)
  - 2-for-1 split effective 1 Jan 2026 — [Nikkei](https://www.nikkei.com/article/DGXZQOUB1181D0R11C25A1000000/)
  - Shikiho items: IBD ¥3,839.63bn (Sep-25); cash ¥98.2bn; D&A forecast ¥75bn; **Elliott International 3.5% holder** — [Shikiho 8830](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8830.txt)
- **Tokyu Fudosan HD.**
  - Market (7 Aug 2026, stale): ¥1,312.5; market cap ¥944.8bn; PER 9.4x; PBR 1.03x; yield 3.81%; ROE 11.24% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=3289)
  - FY3/2026 actual: ¥1,246.048bn / ¥166.882bn / ¥96.697bn.
  - FY3/2027 plan: ¥1,400bn / ¥190bn / ¥100bn.
  - IBD ¥1,826.9bn (Mar-26) — [tanshin](https://www2.jpx.co.jp/disc/32890/140120260511521611.pdf), [investalk](https://investalk.jp/3289/tokyu-fudosan-2026-03-earnings/)
  - Shikiho items: cash ¥157.4bn; D&A forecast ¥67.2bn — [Shikiho 3289](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3289.txt)
- **Nomura RE HD.**
  - Market (4 Sep 2026): ¥926; market cap ¥850.0bn; PER 9.2x; PBR 0.99x; yield 4.75%; ROE 10.68% — [kabuyoho](https://kabuyoho.jp/sp/reportTop?bcode=3231)
  - FY3/2026 actual: ¥942.505bn / ¥138.242bn / ¥82.880bn.
  - FY3/2027 guidance: ¥1,080bn / ¥140bn / ¥86bn.
  - IBD ¥1,696.5bn (Jun-26) — [tanshin](https://www.nomura-re-hd.co.jp/ir/pdf/renketsu_20260424.pdf), [1Q deck](https://www.nomura-re-hd.co.jp/ir/pdf/2027/1Q/20260730_kessan.pdf)
  - Shikiho items: cash ¥35.8bn; D&A ¥20.8bn; OCF −¥133.8bn — [Shikiho 3231](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3231.txt)
- **Hulic.**
  - Market (25 Sep 2026): ¥1,734; market cap ¥1,331.6bn; PER 10.9x; PBR 1.39x; yield 3.86%; ROE 13.09% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=3003)
  - FY12/2025 actual: ¥727.447bn / ¥186.826bn / ¥114.334bn.
  - FY12/2026 guidance: OI ¥210bn; NI ¥121bn — [Nikkei](https://www.nikkei.com/article/DGXZQOUB2927X0Z20C26A1000000/)
  - Shikiho items: IBD ¥2,210.76bn (Sep-25); cash ¥134.3bn (Dec-24); D&A ¥17.8bn (FY24) — [Shikiho 3003](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3003.txt)
- **Heiwa RE.**
  - Market (30 Sep 2026): ¥2,320; market cap ¥164.8bn; PER 13.3x; PBR 1.24x; yield 4.44%; ROE 9.01% — [traders.co.jp](https://www.traders.co.jp/stocks/41_8803/)
  - FY3/2026 actual: ¥50.855bn / ¥15.109bn / ¥11.032bn.
  - FY3/2027 guidance: ¥63.8bn / ¥15.8bn / ¥11.5bn.
  - IBD ¥261.338bn — [japanir.jp](https://japanir.jp/company/company-8803/ir/8803-20260430-02_wp_financial_summary/)
  - Shikiho items: cash ¥25.2bn; D&A ¥5.6bn — [Shikiho 8803](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8803.txt)
- **Keihanshin Building.**
  - Market (11 Sep 2026): ¥1,118; market cap ¥109.1bn; PER 15.2x; PBR 1.26x; yield 2.68%; ROE 5.93% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=8818)
  - FY3/2026 actual: ¥20.255bn / ¥5.646bn / ¥4.675bn — [Matsui](https://finance.matsui.co.jp/stock/8818/settlement/index)
  - Shikiho items: IBD ¥77.70bn (Sep-25); cash ¥14.0bn; D&A ¥3.89bn. The share count doubled from 48.8m (Mar-26) to 97.6m (Sep-26), which implies a 2-for-1 split (D) — [Shikiho 8818](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8818.txt)
- **Sekisui House.**
  - Market (6 Aug 2026, stale): ¥3,415; market cap ¥2,225.2bn; PER 10.2x; PBR 1.03x; yield 4.25%; ROE 11.32% — [kabuyoho](https://kabuyoho.jp/reportTop?bcode=1928)
  - FY1/2026 actual: ¥4,197.922bn / ¥341.402bn / ¥232.095bn.
  - IBD ¥1,944.54bn (Oct-25); cash ¥390.3bn; D&A ¥35.2bn — [Shikiho 1928](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/1928.txt)
- **Daito Trust.**
  - Market (29 Sep 2026): ¥3,143; market cap ¥1,083.1bn; PER 9.5x; PBR 2.06x; yield 5.19%; ROE 20.45% — [Monex](https://scouter.monex.co.jp/report/index/1878)
  - FY3/2026 company forecast (Jan 2026): ¥1,980bn / ¥135bn / ¥95bn.
  - IBD ¥233.1bn; cash ¥223.5bn — [Shikiho 1878](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/1878.txt)
- **Open House.**
  - Market (29 Sep 2026): ¥7,362; market cap ¥859.7bn; PER 6.9x; PBR 1.38x; yield 2.78%; ROE 20.10% — [kabuyoho](https://kabuyoho.jp/reportTarget?bcode=3288)
  - FY9/2025 actual: ¥1,336.468bn / ¥145.933bn / ¥100.670bn.
  - IBD ¥720.06bn; cash ¥407.6bn — [Shikiho 3288](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3288.txt)
- **Sector backdrop.** All five majors guided to record FY3/2027 net profit despite higher rates — [Nikkei](https://www.nikkei.com/article/DGXZQOUB124ZH0S6A510C2000000/)

### Inferences
**Method**
- EV = market cap (S) + IBD (S, latest date available) − cash (S) + NCI.
- NCI: TT ¥12.3bn (D) = net assets ¥619.0bn − 24.5% × total assets ¥2,476.2bn. Peers' NCI is **set to 0 (E)** because it is not retrievable.
- EBITDA = OI + D&A (S; basis per company is in the CSV).
- Hybrids are counted 100% as debt: rating-agency equity credit is a credit convention and does not reduce the claim ahead of common equity.
- Date mismatches: several peers' IBD is from Sep-25 and their cash from the FY-end before. The Monte Carlo in §4 tests this.
- Market cap may include treasury shares (Nomura 4.8%, Heiwa 13.6% at Sep-25). Adjusting Nomura cuts its EV by about ¥41bn, i.e. −0.04x EV/Sales, which does not matter for the regression.

**Table A: capital structure (¥bn)**

| Company | Price ¥ (date) | Mkt cap | IBD (date) | Cash (date) | Net debt | EV | EBITDA (LTFY) | ND/EBITDA | ND/Equity |
|---|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | 3,286 (25-Sep-26) | 683.4 | 1,536.6 (Jun-26) | 94.2 (Jun-26) | 1,442.4 | **2,138.1** | 118.8 | **12.1x** | **2.36x** |
| Mitsui Fudosan | 1,507.5 (7-Sep) | 4,060.0 | 4,632.5 (Mar-26) | 163.2 (Mar-25) | 4,469.4 | 8,529.4 | 537.8 | 8.3x | 1.38x |
| Mitsubishi Estate | 3,630 (28-Sep) | 4,396.3 | 3,469.3 (Sep-25) | 256.8 (Mar-25) | 3,212.5 | 7,608.8 | 436.7 | 7.4x | 1.18x |
| Sumitomo Realty | 3,226 (14-Sep) | 3,019.5 | 3,839.6 (Sep-25) | 98.2 (Mar-25) | 3,741.4 | 6,760.9 | 374.2 | 10.0x | 1.44x |
| Tokyu Fudosan HD | 1,312.5 (7-Aug) | 944.8 | 1,826.9 (Mar-26) | 157.4 (Mar-25) | 1,669.5 | 2,614.3 | 234.1 | 7.1x | 1.82x |
| Nomura RE HD | 926 (4-Sep) | 850.0 | 1,696.5 (Jun-26) | 35.8 (Mar-25) | 1,660.7 | 2,510.7 | 159.0 | 10.4x | 1.93x |
| Hulic | 1,734 (25-Sep) | 1,331.6 | 2,210.8 (Sep-25) | 134.3 (Dec-24) | 2,076.5 | 3,408.1 | 204.6 | 10.1x | 2.17x |
| Heiwa RE | 2,320 (30-Sep) | 164.8 | 261.3 (FY-end) | 25.2 (Mar-25) | 236.1 | 400.9 | 20.7 | 11.4x | 1.78x |
| Keihanshin Bldg | 1,118 (11-Sep) | 109.1 | 77.7 (Sep-25) | 14.0 (Mar-25) | 63.7 | 172.8 | 9.5 | 6.7x | 0.74x |
| Sekisui House | 3,415 (6-Aug) | 2,225.2 | 1,944.5 (Oct-25) | 390.3 (Jan-25) | 1,554.2 | 3,779.4 | 376.6 | 4.1x | 0.72x |
| Daito Trust | 3,143 (29-Sep) | 1,083.1 | 233.1 (Sep-25) | 223.5 (Mar-25) | 9.6 | 1,092.7 | 152.3 | 0.1x | 0.02x |
| Open House | 7,362 (29-Sep) | 859.7 | 720.1 (Sep-25) | 407.6 (Sep-25) | 312.5 | 1,172.2 | 148.0 | 2.1x | 0.50x |

**Table B: operating data, LTFY actual and current-year guidance (¥bn)**

| Company | LTFY | Revenue | EBIT (OI) | NI | EBIT margin | EBITDA margin | Rev growth 1y | Rev CAGR 3y | Rev fcst | OI fcst | NI fcst | Fcst EBIT margin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | FY12/25 | 474.6 | 95.8 | 58.9 | 20.2% | 25.0% | +2.3% | +10.7% | 524.0 | 105.5 | 65.0 | 20.1% |
| Mitsui Fudosan | FY3/26 | 2,709.7 | 397.8 | 278.7 | 14.7% | 19.8% | +3.2% | +6.1% | 2,800 | 410 | 285 | 14.6% |
| Mitsubishi Estate | FY3/26 | 1,746.1 | 329.7 | 222.5 | 18.9% | 25.0% | +10.5% | +8.2% | 2,060 (E, Toyo Keizai) | 370 | 235 | 18.0% |
| Sumitomo Realty | FY3/26 | 1,057.8 | 299.2 | 212.5 | 28.3% | 35.4% | +4.3% | +4.0% | 1,070 | 320 | 223 | 29.9% |
| Tokyu Fudosan HD | FY3/26 | 1,246.0 | 166.9 | 96.7 | 13.4% | 18.8% | +8.3% | +7.4% | 1,400 | 190 | 100 | 13.6% |
| Nomura RE HD | FY3/26 | 942.5 | 138.2 | 82.9 | 14.7% | 16.9% | +24.4% | +12.9% | 1,080 | 140 | 86 | 13.0% |
| Hulic | FY12/25 | 727.4 | 186.8 | 114.3 | 25.7% | 28.1% | +22.9% | +11.6% | 751 (E, Toyo Keizai) | 210 | 121 | 28.0% |
| Heiwa RE | FY3/26 | 50.9 | 15.1 | 11.0 | 29.7% | 40.7% | +20.9% | +4.5% | 63.8 | 15.8 | 11.5 | 24.8% |
| Keihanshin Bldg | FY3/26 | 20.3 | 5.6 | 4.7 | 27.9% | 47.1% | +3.4% | +2.4% | 20.1 (E) | 5.5 (E) | 4.2 (E) | 27.5% |
| Sekisui House | FY1/26 | 4,197.9 | 341.4 | 232.1 | 8.1% | 9.0% | +3.4% | +12.7% | 4,353 | 350 | 218 | 8.0% |
| Daito Trust | FY3/26 (fcst proxy, E) | 1,980 | 135 | 95 | 6.8% | 7.7% | n/a | +6.1% | n/a | n/a | n/a | n/a |
| Open House | FY9/25 | 1,336.5 | 145.9 | 100.7 | 10.9% | 11.1% | +3.1% | +11.9% | 1,485 | 174.5 | 115.5 | 11.8% |

3-year CAGR bases are each company's revenue three fiscal years earlier, per Shikiho (e.g. TT FY12/2022 ¥349.94bn; Mitsui FY3/2023 ¥2,269.1bn).

**Table C: multiples**

| Company | EV/Sales | EV/Sales fcst | EV/EBITDA | EV/EBIT | EV/EBIT fcst | P/E LTFY (D) | P/E fcst (S) | P/B (S) | Yield (S) | ROE (S) | OCF/EV | FCF yield on mkt cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Tokyo Tatemono** | **4.51x** | **4.08x** | **18.0x** | **22.3x** | **20.3x** | **11.6x** | **10.5x** | **1.12x** | **3.83%** | **10.45%** | 1.5% | n/a (FY24: (123)bn) |
| Mitsui Fudosan | 3.15x | 3.05x | 15.9x | 21.4x | 20.8x | 14.6x | 14.3x | 1.25x | 2.45% | 8.68% | 7.0% | +6.8% |
| Mitsubishi Estate | 4.36x | 3.69x | 17.4x | 23.1x | 20.6x | 19.8x | 18.6x | 1.61x | 1.35% | 8.47% | 4.3% | −0.9% |
| Sumitomo Realty | 6.39x | 6.32x | 18.1x | 22.6x | 21.1x | 14.2x | 13.4x | 1.16x | 1.61% | 9.16% | 3.7% | +3.6% |
| Tokyu Fudosan HD | 2.10x | 1.87x | 11.2x | 15.7x | 13.8x | 9.8x | 9.4x | 1.03x | 3.81% | 11.24% | 1.8% | −9.8% |
| Nomura RE HD | 2.66x | 2.32x | 15.8x | 18.2x | 17.9x | 10.3x | 9.2x | 0.99x | 4.75% | 10.68% | −5.3% | −39.7% |
| Hulic | 4.68x | 4.54x | 16.7x | 18.2x | 16.2x | 11.6x | 10.9x | 1.39x | 3.86% | 13.09% | 7.9% | −25.0% |
| Heiwa RE | 7.88x | 6.28x | 19.4x | 26.5x | 25.4x | 14.9x | 13.3x | 1.24x | 4.44% | 9.01% | 4.0% | −5.3% |
| Keihanshin Bldg | 8.53x | 8.60x | 18.1x | 30.6x | 31.2x | 23.3x | 15.2x | 1.26x | 2.68% | 5.93% | 4.2% | −0.8% |
| Sekisui House | 0.90x | 0.87x | 10.0x | 11.1x | 10.8x | 9.6x | 10.2x | 1.03x | 4.25% | 11.32% | 1.7% | −28.5% |
| Daito Trust | 0.55x | n/a | 7.2x | 8.1x | n/a | 11.4x | 9.5x | 2.06x | 5.19% | 20.45% | 7.8% | +3.6% |
| Open House | 0.88x | 0.79x | 7.9x | 8.0x | 6.7x | 8.5x | 6.9x | 1.38x | 2.78% | 20.10% | 2.5% | +2.1% |
| **Core-8 median** | 4.52x | — | 17.0x | 22.0x | 20.7x | 14.4x | 13.35x | 1.245x | 3.25% | 9.09% | 4.1% | — |
| **TT vs core-8 median** | 0% | — | +6% | +1% | −2% | −19% | −21% | −10% | +18% | +1.4pp | — | — |
| Big-5 median | 3.15x | — | 15.9x | 21.4x | — | — | 13.4x | 1.16x | 2.45% | — | — | — |
| **TT vs Big-5** | +43% | — | +14% | +4% | — | — | −22% | −3% | +56% | — | — | — |

- OCF/EV and FCF use each company's last annual cash flow from Shikiho. FCF = OCF + investing CF.

**Value implied for TT at peer medians (D)**
- Forward P/E 13.35x × FY26E EPS ¥312.5 = **¥4,172** (+27%).
- P/B 1.245x × BPS ¥2,934 = **¥3,653** (+11%).
- EV/Sales 4.52x = **¥3,322** (+1%).
- EV/EBIT 22.0x = **¥3,145** (−4%).
- EV/EBITDA 17.0x = **¥2,735** (−17%).
- The implied value falls as the multiple moves "down" the capital structure: equity multiples point to upside, enterprise multiples to fair value or downside.

**Other observations**
- **Cash generation.** TT's OCF/EV of 1.5% is the second-lowest in the core set. Its develop-to-sell model puts land and condo spending through operating CF, as at Nomura (negative) and Tokyu (1.8%).
- **EBITDA basis.** EBITDA for March-FY peers uses the Shikiho FY3/26 D&A forecast; TT uses the FY12/25 forecast of ¥23.0bn. On FY2026E (OI ¥105.5bn + D&A of about ¥24bn, E), TT's EV/EBITDA is about 16.5x.

### Gaps
- **Not available:** sell-side consensus (as distinct from company guidance); NCI for peers; balance sheets at Mar/Jun-2026 for Mitsubishi Estate, Sumitomo, Hulic, Keihanshin and the housing names; FY3/2026 actuals for Daito; TT's hybrid amount and equity credit.
- **Stale prices.** Prices for Tokyu (7 Aug), Sekisui House (6 Aug), Mitsui (7 Sep) and Nomura (4 Sep) are 4–8 weeks old.

## 3. Tokyo Tatemono's historical multiples and its premium/discount to peers

### Takeaway
**Absolute history.** On year-end prices, TT's trailing P/E ranged from about **7.8x (FY2022) to about 12.5x (FY2025)**, averaging about 9.7x over FY2021–FY2025. Its P/B rose from about **0.89x (FY2023, E) to 1.25x (FY2025)**, peaked at about **1.54x at the 27 Feb 2026 all-time high (¥4,374)**, and is **1.12x now**. Year-end dividend yield ranged from 2.96% to 4.07%.

**Relative history.** Over the last three fiscal years, TT traded at a **31–37% P/E discount** to the developer median, using Shikiho's 3-year average P/E band: TT 7.0–9.9x vs a peer median of 10.2–15.8x. That discount narrowed to −29% in March 2026 and to **−21% now**. TT's P/B discount was about −7% in March 2026 and is −10% now.

**Recent moves.** TT is now **above its own 3-year P/E band** (10.5x forward vs 7.0–9.9x). The 2026 sector de-rating hit TT less than the majors: −13% from 13 Mar to 25 Sep vs −17% to −33% for Mitsui, Mitsubishi Estate and Sumitomo.

### Cited Findings
- **Year-end closes for TT** (annual OHLC; Nikkei source):

  | Year-end | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|
  | Close (¥) | 1,522 | 1,140 | 1,709 | 1,415 | 1,680 | 1,599 | 2,112 | 2,607 | 3,546 |

  - 2025: high ¥3,655 (26 Dec), low ¥2,237.5 (7 Apr).
  - 2026 monthly closes: Jan 3,629, Feb 4,374 (all-time high), Mar 3,587, Apr 3,599, May 3,269, Jun 3,296, Jul 3,387, Aug 3,445.
  - Sources: [Nikkei yearly prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804), [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) (via `stock_prices_8804.csv`)
- **EPS and DPS.**

  | | FY2022 | FY2023 | FY2024 | FY2025 |
  |---|---|---|---|---|
  | EPS (¥) | 206.2 | 215.8 | 315.5 | 283.08 |
  | DPS (¥) | 65 | 73 | 95 | 105 |

  - FY2021 NI was ¥34.965bn.
  - BPS: FY2024 ¥2,568; Sep-2025 ¥2,667; FY2025 ¥2,846.85.
  - Sources: [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt), [Nikkei kessan](https://www.nikkei.com/nkd/company/kessan/?scode=8804), [japanir.jp](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/) (via `financials_kpis_capital_structure.md`, `nav_forensic_risks.md`)
- **Snapshot on 13 Mar 2026 (Shikiho).** TT ¥3,795: forward P/E 12.52x, P/B 1.33x, yield 3.21%. Shikiho's 3-year P/E band ("実績PER 高値平均/安値平均") is 9.9x / 7.0x. — [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **Peers' 3-year P/E bands (high-average / low-average) and Mar-2026 multiples (forward P/E, P/B)** — Shikiho mirror pages [8801](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8801.txt), [8802](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8802.txt), [8830](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8830.txt), [3289](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3289.txt), [3231](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3231.txt), [3003](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3003.txt), [8803](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8803.txt), [8818](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8818.txt)

  | Company | 3-yr P/E band (hi / lo) | Fwd P/E (Mar-26) | P/B (Mar-26) |
  |---|---|---|---|
  | Mitsui | 18.3 / 11.4 | 18.58 | 1.56 |
  | Mitsubishi Estate | 19.5 / 12.5 | 26.17 | 2.26 |
  | Sumitomo | 14.2 / 8.4 | 21.34 | 1.84 |
  | Tokyu | 12.3 / 7.6 | 10.99 | 1.15 |
  | Nomura | 10.6 / 7.4 | 12.97 | 1.21 |
  | Hulic | 12.0 / 9.0 | 12.04 | 1.57 |
  | Heiwa | 17.4 / 13.7 | 16.86 | 1.30 |
  | Keihanshin | 20.3 / 14.4 | 22.63 | 1.16 |

- **NAV per share.** TT's NAV was about ¥4,853 at FY2025-end and about ¥4,937 on the 1H26 BPS of ¥2,930. That gives P/NAV of about **0.89–0.90x at the Feb-2026 high** and **about 0.65x at ¥3,211 (2 Oct 2026)**. — [IR Bank 価値算定](https://irbank.net/E03859/value), [FY2025 presentation](https://pdf.irpocket.com/C8804/doF3/FpJe/bqVe.pdf) (via `nav_forensic_risks.md`)

### Inferences
**TT own-history table (D)**
- Year-end P/E = close / FY EPS. P/B = close / BPS. Yield = DPS / close.
- FY2021 EPS ≈ ¥167 (E) = ¥34.965bn / about 208.8m shares.
- FY2023 BPS ≈ ¥2,365 (E) = about ¥494bn estimated equity / 208.9m.

| Point | Price ¥ | P/E | P/B | Div yield | EV/EBITDA |
|---|---|---|---|---|---|
| FY2021 YE | 1,680 | 10.0x (E) | n/a | n/a | n/a |
| FY2022 YE | 1,599 | 7.8x | n/a | 4.07% | n/a |
| FY2023 YE | 2,112 | 9.8x | 0.89x (E) | 3.46% | n/a |
| FY2024 YE | 2,607 | 8.3x | 1.02x | 3.64% | n/a |
| FY2025 YE | 3,546 | 12.5x | 1.25x | 2.96% | 16.3x |
| 27 Feb 2026 (ATH) | 4,374 | 14.4x (on FY26 guidance EPS ¥302.9) | 1.54x | 2.8% (on ¥122) | n/a |
| 13 Mar 2026 (Shikiho) | 3,795 | 12.5x fwd | 1.33x | 3.21% | n/a |
| **25 Sep 2026** | **3,286** | **10.5x fwd / 11.6x LTFY** | **1.12x** | **3.83%** | **18.0x** (Jun-26 net debt) / **15.9x** (Dec-25 net debt) |
| 2 Oct 2026 | 3,211 | 10.3x fwd | 1.09–1.10x | 3.92% | 17.9x |

- FY2025 YE EV/EBITDA basis: EV ¥1,941bn = ¥737.5bn market cap + ¥1,191.6bn net debt (Dec-25) + ¥12.3bn NCI, over EBITDA of ¥118.8bn.

**Ranges (FY2021–FY2025 year-ends plus 2026 points)**
- P/E: min 7.8x (FY22), max 14.4x (Feb-26), average of year-ends about 9.7x; current 10.5x forward.
- P/B: min about 0.89x (FY23, E), max about 1.54x (Feb-26); current 1.12x.
- Dividend yield: min 2.8% (Feb-26), max 4.07% (FY22); current 3.83%.
- EV/EBITDA: only FY2025 (16.3x) and now (16–18x) are computable.
- With 2017–2020 prices and probably sub-¥200 EPS (not retrieved), P/B was very likely below 1x through 2017–2023. This is consistent with Shikiho's 7.0–9.9x three-year P/E band, but unverified.

**Relative history (D)**
- **P/E discount.** TT's 3-year mid-band P/E of 8.45x vs the core-8 median mid-band of 13.1x is **−35%**: −37% on the high band, −31% on the low band. Against the Big-5 the mid-band discount is −25%.
- **Narrowing.** The forward P/E discount narrowed to −29% in March 2026 (12.52x vs 17.72x median) and **−21% now** (10.5x vs 13.35x). TT's relative de-rating has therefore narrowed by about 10–15pp vs its 3-year history. The drivers are faster growth (3-year revenue CAGR 10.7% vs 6.7%), the 40% payout target, and a smaller 2026 sell-off.
- **P/B.** The discount was about −7% in March 2026 (1.33x vs 1.43x median) and is −10% now (1.12x vs 1.245x).
- **The 2026 sector de-rating** (13 Mar → Aug/Sep 2026; Keihanshin split-adjusted, Tokyu and Sekisui prices from early August):

  | TT | Mitsui | Mitsubishi Estate | Sumitomo | Nomura | Hulic | Heiwa | Tokyu | Keihanshin | Core median |
  |---|---|---|---|---|---|---|---|---|---|
  | −13.4% | −17.2% | −23.2% | −32.7% | −12.6% | −8.7% | −5.2% | −4.5% | +14.8% | −10.7% |

  - Measured from the February highs, the NAV workstream reports TT −26.6% vs the majors −34% to −42%: [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) (via `nav_forensic_risks.md`).
- **TT's own band on FY26E EPS.** 7.0x–9.9x gives **¥2,188–¥3,094** (mid ¥2,641). The current ¥3,286 is above even the top of TT's 3-year band. Mean reversion to its own history would therefore not support upside; the re-rating case rests on narrowing the peer discount.

### Gaps
- **Missing fundamentals before FY2021:** EPS, BPS and DPS for FY2016–FY2020, needed for a full 10-year series (2017–2020 prices are available).
- **Missing year-end balance sheets** for FY2021–FY2024 (net debt), so EV/EBITDA history is incomplete.
- **Missing peer history:** peers' year-by-year P/E and P/B. Only Shikiho's 3-year bands and the March-2026 snapshot were retrieved.
- **Definition unverified:** the exact Shikiho definition of 実績PER 高値平均/安値平均.

## 4. Statistical regression: EV/Sales vs EBIT margin, and TT's implied valuation

### Takeaway
**Primary model.** The eight listed developers/landlords, with TT excluded from the fit and balance sheets sourced:
- EV/Sales = −1.974 + 0.3208 × EBIT margin (%).
- **R² 0.856**, adjusted R² 0.832, n = 8, slope t = 5.97 (p = 0.001).

**TT's position.** TT's fitted EV/Sales of **4.50x** equals its actual **4.51x**, implying **¥3,271/share** (−0.5% vs ¥3,286; +1.9% vs ¥3,211).

**Robustness.**
- A Monte Carlo over the unverifiable inputs (NCI, stale debt and cash dates) gives **¥3,439–¥3,642** (P5–P95).
- Specification choices matter more, because equity is only about 32% of TT's EV: the result ranges from **¥2,376 (large caps only) to ¥4,477 (Dec-25 balance sheet)**.
- The 11-company extended fit including housebuilders (R² 0.92) gives ¥3,250.
- The forward-basis fit gives ¥3,833.
- The supplementary P/B-vs-ROE fit (R² 0.30) gives ¥3,713.

TT is fairly valued on an enterprise basis relative to peers, with modest upside only on equity-based or forward-basis measures.

### Cited Findings
- All inputs are the sourced figures in §2.
- The full dataset, with S/D/E flags, dates and a source URL per row (including the Shikiho mirror URL), is saved as **`peer_valuation_8804.csv`** in this folder.
- The columns `in_R1_core8` and `in_R1e_ext11` mark which regression each company enters.

### Inferences
**Method**
- OLS via numpy (`lstsq`); classical standard errors; 95% two-sided t intervals.
- **y** = EV / LTFY revenue. EV uses the latest price and latest sourced balance sheet.
- **x** = LTFY operating income / revenue (%).
- **TT bridge:** fitted EV/Sales × revenue → implied EV; − net debt ¥1,442.4bn − NCI ¥12.3bn → equity; ÷ 207.97m shares.

**R1 primary results (n = 8: 8801, 8802, 8830, 3289, 3231, 3003, 8803, 8818)**

| Statistic | Value |
|---|---|
| Intercept | −1.974 (SE 1.215; t −1.62) |
| Slope (per 1pp EBIT margin) | **0.3208** (SE 0.0538; t 5.97; p 0.001) |
| R² / adjusted R² | **0.856 / 0.832** |
| Residual SE | 0.99x |
| TT EBIT margin (FY2025) | 20.18% |
| TT fitted EV/Sales | **4.50x** |
| TT actual EV/Sales | **4.51x** (residual +0.01x) |
| Implied EV / equity | ¥2,135.1bn / ¥680.3bn |
| **Implied value per share** | **¥3,271** |
| 95% CI of the fitted mean | 3.62–5.37x, i.e. ¥1,273–¥5,269 |
| 95% prediction interval | 1.93–7.07x, i.e. <¥0 to ¥9,134 |

The prediction interval is uninformative for a single company: 0.1x of EV/Sales equals ¥47.5bn of EV, or ¥228 per share.

**Robustness variants**

| Variant | n | Slope | R² | TT fitted | TT actual | Implied ¥/sh | vs ¥3,286 |
|---|---|---|---|---|---|---|---|
| R1 base | 8 | 0.321 | 0.86 | 4.50x | 4.51x | 3,271 | −0.5% |
| R1a TT on LTM (rev ¥460.2bn, margin 22.1%) | 8 | 0.321 | 0.86 | 5.11x | 4.65x | 4,305 | +31% |
| R1b TT on Dec-25 balance sheet (net debt ¥1,191.6bn) | 8 | 0.321 | 0.86 | 4.50x | 3.98x | 4,477 | +36% |
| R1c excluding Keihanshin | 7 | 0.283 | 0.90 | 4.30x | 4.51x | 2,812 | −14% |
| R1d large caps only (excluding Heiwa and Keihanshin) | 6 | 0.236 | 0.90 | 4.11x | 4.51x | 2,376 | −28% |
| R1e extended incl. Sekisui House, Daito, Open House | 11 | 0.318 | 0.92 | 4.49x | 4.51x | 3,250 | −1% |
| R1f forward basis (FY guidance; revenue for 8802/3003/8818 is a Toyo Keizai estimate) | 8 | 0.279 | 0.73 | 4.30x | 4.08x | 3,833 | +17% |

**Monte Carlo (20,000 draws)**
- Inputs varied: peers' NCI uniform 0–5% of market cap (Mitsubishi Estate 0–12%); Sep-2025 IBD grossed up by 0–8% for later asset growth; cash ×0.7–1.3.
- Result: implied TT price P5 **¥3,439**, P50 **¥3,542**, P95 **¥3,642**; R² 0.84–0.87; slope 0.323–0.338.
- Adding plausible NCI and debt growth to peers raises the peer line, so the base case (NCI = 0) is conservative for TT.

**Supplementary fits**

| Model | n | Slope (t, p) | R² | TT fitted vs actual | Implied ¥/sh |
|---|---|---|---|---|---|
| R2: P/B on ROE, all 11 peers | 11 | 0.0364 (1.96, 0.08) | 0.30 | 1.27x vs 1.12x | **3,713 (+13%)**; 95% PI ¥1,817–¥5,609 |
| R2b: P/B on ROE, core 8 | 8 | −0.017 (−0.47, 0.66) | 0.04 | 1.23x vs 1.12x | 3,595 (no meaningful relationship) |
| R4: EV/EBITDA on ROE, core 8 | 8 | −0.551 (−1.32, 0.24) | 0.22 | 16.0x vs 18.0x | 2,170 (weak, wrong-signed; not used) |

**Interpretation**
1. **Margin drives EV/Sales.** EBIT margin, effectively a proxy for leasing intensity versus develop-to-sell, explains about 86% of the cross-section. High-margin landlords (Sumitomo, Heiwa, Keihanshin, Hulic) command high EV/Sales; condo- and brokerage-heavy groups (Tokyu, Nomura, Mitsui) and housebuilders do not.
2. **TT is fairly priced on an EV basis.** It sits exactly on the line. Its equity discounts (P/E −21%, P/B −10%) reflect leverage (ND/EBITDA 12.1x vs 9.2x), not a mispriced enterprise.
3. **Sensitivity of the per-share answer.** It is extreme because net debt is about 68% of EV. The balance-sheet date alone (Jun-26 seasonal peak vs Dec-25) moves the result by about ¥1,200/share. A forward or LTM basis, which captures TT's above-peer profit growth, implies +17% to +31%.
4. **P/B is not explained by ROE among developers (R² 0.04).** The market prices asset quality and NAV rather than accounting returns. Mitsubishi Estate has the highest P/B and the lowest ROE.

### Gaps
- Peers' NCI and Mar/Jun-2026 balance sheets for four of the eight peers are estimates or stale; the Monte Carlo bounds the effect at about ±3%.
- No consensus forecasts were available, so the forward fit uses company guidance and three Toyo Keizai revenue estimates.
- n is small (8–11); treat the coefficients as descriptive, not predictive.

## 5. M&A in Japanese real estate, 2019–2026: precedents, multiples and TOB-premium norms

### Takeaway
A full scan of EDINET filings for Nov 2022–Oct 2026 (mirrored) finds 28 tender offers for Japanese listed real-estate-related companies and J-REITs. They fall into three patterns:
1. **Strategic consolidation of small and mid-cap developers by larger groups:** Open House→Pressance, Daito→Ascot and The Global, Haseko→Wood Friends, Sumitomo Forestry→LeTech, Seibu Real Estate→E-Grand, Hulic→Raysum, Toho→Tokyo Rakutenchi, Keio→Sunwood, Tokyu Land→Renewable Japan.
2. **Financial-sponsor/SPV take-privates:** Song Bidco→Samty HD (Oct 2024), SI→Sun Frontier (Feb 2026), Ursa4→JSB (Jun 2026), Amsterdam1→JPMC (Aug 2026), K891→Leopalace21 (Sep 2026).
3. **Contested or activist bids for J-REITs:** Citco Trustees bids for NTT UD REIT and Hankyu Hanshin REIT (Jan–Feb 2025), and Tiger LPS's bid for Sankei Real Estate REIT (Jan 2026) followed by a competing City Index Fifth bid (28 Sep 2026).

No bid for a large integrated developer appears. The largest listed real-estate targets are about ¥0.2tn (Leopalace21, NTT UD REIT), so a TT bid (equity ¥0.7–1.0tn, EV ¥2.1–2.5tn) would be unprecedented in size.

Activists are already inside the sector: Elliott holds 3.5% of Sumitomo Realty, Aya Nomura 5.3% of Heiwa, Ichigo Trust 12.6% of Open House. Mitsui Fudosan was pressed by an activist in 2024.

Deal prices, premiums and multiples could not be retrieved; the 2019–2022 landmark deals (Unizo, Tokyo Dome, NTT UD, Daibiru, Kenedix) are unverified.

### Cited Findings
**TOBs on real-estate-related targets.** Source for every row: the EDINET daily index file for the filing date (`code4fukui/EDINET/data/documents/YYYY-MM-DD.csv`; doc IDs given). The register shows filing date, acquirer and target only; prices are not included.

| Filed | Acquirer (filer) | Target (code) | EDINET doc | Pre/post-deal size (Shikiho, Mar-26, where available) |
|---|---|---|---|---|
| 2023-11-07 | Keio Corp | Sunwood (8903) | [S100S4WG](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2023-11-07.csv) | n/a |
| 2023-11-13 | K.I.T | Nichiju Service (8854) | [S100S8TD](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2023-11-13.csv) | n/a |
| 2023-12-07 | Toho | Tokyo Rakutenchi (8842) | [S100SF7R](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2023-12-07.csv) | n/a |
| 2024-08-05 | ASN | EL CAMINO REAL (8889) | [S100U5LX](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-08-05.csv) | n/a |
| 2024-09-17 | **Hulic** | Raysum (8890) | [S100UDPU](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-09-17.csv) | n/a |
| 2024-10-15 | Song Bidco GK | Samty HD (187A) | [S100UJBP](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-10-15.csv) | n/a |
| 2024-11-11 | Starts Corp (self-tender) | Starts (8850) | [S100UPCH](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-11-11.csv) | ¥265.4bn, P/B 1.27x ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8850.txt)) |
| 2024-11-15 | Tokyu Land (Tokyu Fudosan HD) | Renewable Japan (9522) | [S100USNW](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-11-15.csv) | n/a |
| 2025-01-14 | **Open House Group** | Pressance (3254) | [S100V36R](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-01-14.csv) | n/a |
| 2025-01-28 | Citco Trustees (UT) Ltd | NTT UD REIT (8956) | [S100V55A](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-01-28.csv) | ¥213.9bn ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8956.txt)) |
| 2025-01-29 | SMFL Mirai Partners | CRE (3458) | [S100V5EQ](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-01-29.csv) | n/a |
| 2025-02-03 | **Daito Trust** | Ascot (3264) | [S100V6AV](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-02-03.csv) | n/a |
| 2025-02-13 | Citco Trustees (UT) Ltd | Hankyu Hanshin REIT (8977) | [S100V8FE](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-02-13.csv) | ¥106.2bn ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8977.txt)) |
| 2025-03-31 and 2025-05-27 | Sumitomo Forestry | LeTech (3497) | [S100VJDV](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-03-31.csv), [S100VTSX](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-05-27.csv) | n/a |
| 2025-04-11 | Haseko | Wood Friends (8886) | [S100VLS8](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-04-11.csv) | n/a |
| 2025-05-28 | Leopalace21 (self-tender) | Leopalace21 (8848) | [S100VU8O](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-05-28.csv) | About 130m shares bought back from the major-shareholder fund and cancelled in Sep 2025 ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8848.txt)) |
| 2025-07-01 | **Hulic** | Canadian Solar Infrastructure Fund (9284) | [S100WA5B](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-07-01.csv) | n/a |
| 2025-11-07 | MM Power GK | Japan Infrastructure Fund (9287) | [S100WZVA](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2025-11-07.csv) | n/a |
| 2026-01-07 | Tiger Investment LPS | Sankei Real Estate Inc. (2972) | [S100XEIP](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-01-07.csv) | ¥59.3bn ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/2972.txt)) |
| 2026-02-26 | SI Co. | **Sun Frontier Fudosan (8934)** | [S100XNI8](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-02-26.csv) | ¥131.4bn, P/B 1.20x, post-announcement ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8934.txt)) |
| 2026-04-01 | Seibu Real Estate | E-Grand (3294) | [S100XW77](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-04-01.csv) | ¥13.4bn, P/B 1.04x, pre-bid ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3294.txt)) |
| 2026-04-07 | **Daito Trust** | THE Global Sha (3271) | [S100XWZU](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-04-07.csv) | ¥25.6bn, P/B 2.45x, pre-bid ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3271.txt)) |
| 2026-05-18 | JTM HD | RISE (8836) | [S100Y4NU](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-05-18.csv) | ¥2.8bn |
| 2026-06-15 | Ursa4 Co. | JSB (3480), student housing | [S100YBSE](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-06-15.csv) | n/a |
| 2026-07-09 | AreaLink | Storage-Oh (2997) | [S100YPRD](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-07-09.csv) | ¥1.7bn |
| 2026-08-04 | Amsterdam1 Co. | JPMC (3276) | [S100YU5H](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-08-04.csv) | ¥23.5bn, P/B 2.40x, pre-bid ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3276.txt)) |
| 2026-09-15 | K891 Co. | **Leopalace21 (8848)** | [S100Z28J](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-09-15.csv) | ¥218.0bn, P/B 6.12x, Mar-26 ([Shikiho](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8848.txt)) |
| 2026-09-28 | City Index Fifth | Sankei Real Estate Inc. (2972), competing bid | [S100Z4GE](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-09-28.csv) | as above |

**Activism inside the peer group (Shikiho registers, Jun/Sep 2025)**
- Elliott International L.P. holds 3.5% of Sumitomo Realty.
- Aya Nomura holds 5.3% of Heiwa RE.
- Ichigo Trust holds 12.6% of Open House.
- Hikari Tsushin holds 5.2% of Daito Trust.
- Sources: [Shikiho 8830](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8830.txt), [8803](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8803.txt), [3288](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/3288.txt), [1878](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/1878.txt)

**Other cited items**
- **Mitsui Fudosan activism (2024).** An activist pressed Mitsui Fudosan to sell its Oriental Land stake and buy back about US$6.7bn of shares (Feb 2024) — [Benzinga](https://benzinga.com/markets/asia/24/02/36946775/None). Mitsui then moved to a total payout of at least 50% — [Mitsui IR 2025](https://www.mitsuifudosan.co.jp/corporate/ir/library/integratedreport/pdf/IR2025_ja_02_04.pdf) (both via `management_board_shareholders.md`)
- **Capital-policy pressure across the sector:**
  - Mitsubishi Estate: ¥100bn buyback (May 2025) and a further buyback with its Feb-2026 upgrade — [Nikkei](https://www.nikkei.com/article/DGXZQOUC125QV0S5A510C2000000/), [Nikkei](https://www.nikkei.com/article/DGXZQOUB095TZ0Z00C26A2000000/)
  - Sumitomo Realty: 2-for-1 split plus a buyback of up to ¥30bn — [Nikkei](https://www.nikkei.com/article/DGKKZO92526800R11C25A1DTD000/)

### Inferences
**Precedent relevance for TT**
- The 2023–2026 flow is overwhelmingly small and mid-cap: most targets are under ¥0.25tn market cap. Strategic buyers have been housebuilders and developers buying condo/renovation platforms (Daito ×2, Open House, Haseko, Sumitomo Forestry, Seibu RE).
- TT itself acted as a buyer in this vein with Star Mica (§7).
- Sponsor-backed SPVs have taken private mid-caps with hard assets (Samty, JSB, JPMC, Leopalace21).
- Contested bids are a live phenomenon in J-REITs: two bids for Sankei REIT within 9 months; the City Index naming suggests a Murakami-affiliated vehicle, which is unverified.

**Indicative terms for a TT bid (D)**
- Japanese practice for TOB premiums is commonly cited as about 30–50% over the 1-month average. This norm is unverified in this session.
- A contested process (e.g. Unizo 2019–20) can roughly double the first bid.
- For TT, a 30–50% premium implies P/B 1.46–1.68x and P/NAV 0.87–1.00x (see §6). That would be at the upper end of where Japanese developers traded even at the Feb-2026 peak: Mitsubishi Estate 2.26x, Sumitomo 1.84x and Mitsui 1.56x P/B in March 2026.

### Gaps
**Unverified precedents (analyst background knowledge, confidence in brackets; verify against TDnet, press releases and MARR/RECOF)**

| Target | Acquirer | Date | Key terms (unverified) |
|---|---|---|---|
| Unizo HD | Employee buyout backed by Lone Star, after an H.I.S. hostile bid and a Fortress white-knight bid | 2019–20 | Final ¥6,000/share vs H.I.S. ¥3,100 initial [medium-high] |
| NTT Urban Development | NTT (about 67% before) | May 2020 | ¥1,400/share [medium] |
| Tokyo Dome | Mitsui Fudosan (Yomiuri took 20%) | Nov 2020 | ¥1,300/share; about ¥120bn [medium] |
| Daibiru | Mitsui O.S.K. Lines | 2021–22 | Parent buyout; price about ¥1,700 [low] |
| Kenedix / ARA AM | ARA (2021) / ESR (2021–22, about US$5.2bn) | 2021–22 | [low-medium] |
| 31 Seibu Prince hotels | GIC | Feb 2022 | About ¥150bn [medium] |
| M.D.C. Holdings (US) | Sekisui House | Jan 2024 | US$63/share; about US$4.9bn; about 18% premium [high / medium] |
| Mitsubishi Corp.-UBS Realty | KKR | Dec 2024–2025 | About ¥230bn [low-medium] |
| Tokyo Garden Terrace Kioicho | Blackstone (from Seibu) | 2025 | About ¥400bn [low] |
| Sapporo HD real-estate business | KKR & PAG | 2025 | n/v [low-medium] |

- **Not retrieved for any EDINET-listed deal:** TOB prices, premiums, deal values and transaction multiples (EV/EBITDA, P/B, P/NAV), and outcomes. Needed: 公開買付届出書 and 意見表明報告書 PDFs, which were blocked.
- **Not identified:** the ultimate sponsors behind the SPVs (Song Bidco, SI Co., Ursa4, Amsterdam1, K891, Tiger LPS, Citco Trustees).
- **Unverified premium statistics:** MARR/RECOF/Nikkei median TOB premiums.
- **No sourced asset-deal cap rates.**
- **Tosei, Starts (other than its self-tender), MIRARTH, Ichigo and Shinoken:** no 2022-11 to 2026-10 TOB was found in the EDINET scan. The scan matched on company and target names, so a miss is possible but unlikely.

## 6. Takeover assessment: should Tokyo Tatemono be considered a target?

### Takeaway
TT is a **credible but low-probability whole-company target**. The more likely outcomes are activist pressure or asset and REIT monetisation.

**Attractions:**
1. About 0.65–0.67x P/NAV and 1.1x P/B, with a forward P/E discount of about 21%.
2. An earnings ramp: FY2026 OI guided +10%, business profit guidance of ¥102bn already above the FY2027 MTP target of ¥95bn, and 40% payout.
3. No controlling or strategic holder. The top-10 register is about 44% custodians and index money. The Fuyo-group insurers hold only about 4.3% (about 5.5% including Hulic's 1.22%). The Fuyo cross-holding web is also being unwound: the Hulic stake was cut in Dec 2024, and the MTP targets at least ¥130bn of policy-share and fixed-asset sales.
4. Japan's pro-M&A governance climate, and activists already present at peers (Elliott, Murakami-linked, Ichigo).

**Impediments:**
1. **Size.** EV of about ¥2.1tn now, ¥2.3–2.5tn at a 30–50% premium; equity of about ¥0.9–1.0tn would be 4–5x the market cap of the largest 2023–26 real-estate TOB targets (about ¥0.2tn: Leopalace21, NTT UD REIT).
2. **Leverage.** ND/EBITDA is 12.1x, the highest among peers. LBO capacity is negligible, and a PE equity cheque would be about 36–46% of EV.
3. **Thin NAV cushion at bid prices.** P/NAV reaches 1.0x at about a 50% premium.
4. **Acquirers' balance sheets.** Pro-forma leverage of 10–14x for any domestic acquirer.

**Indicative friendly takeout:** ¥4,270–¥4,930/share (30–50% premium; 1.46–1.68x P/B; 0.87–1.00x P/NAV; 13.7–15.8x FY26E P/E; 18–19x FY26E EV/EBITDA; 22–24x FY26E EV/EBIT).

### Cited Findings
- **Valuation inputs:**
  - Price ¥3,286 (25 Sep); market cap ¥683.4bn; PBR 1.12x — [kabuyoho](https://kabuyoho.jp/report?bcode=8804)
  - Latest price ¥3,211 (2 Oct) — [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/)
  - Net debt ¥1,442.4bn (Jun-26) — §2 sources
- **NAV.**
  - Rental property at FY2025: book value ¥1,058.1bn, fair value ¥1,658.0bn, unrealised gain ¥599.9bn.
  - After 30.6% tax that is ¥2,007/share, giving NAV of about ¥4,937/share on the 1H26 BPS of ¥2,930. P/NAV is about 0.65x at ¥3,211.
  - Secondary-source peer P/NAVs: Mitsubishi Estate and Mitsui about 0.64x, Sumitomo about 0.47–0.51x.
  - Sources: [IR Bank](https://irbank.net/E03859/value), [FY2025 presentation](https://pdf.irpocket.com/C8804/doF3/FpJe/bqVe.pdf), [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) (via `nav_forensic_risks.md`)
- **Register at 30 Jun 2026.**
  - Master Trust 18.02%; Custody Bank 12.01%; Meiji Yasuda Life 2.27%; Japan Securities Finance 2.17%; State Street 505001 2.16%; Sompo Japan 2.00%; others are foreign custodians. Top-10 total about 44%.
  - Large-holding filers: BlackRock 6.42% (Dec 2025); SMTAM 5.07% (Apr 2026).
  - No activist ≥5% filing found.
  - Sources: [Yahoo! Finance JP profile](https://finance.yahoo.co.jp/quote/8804.T/profile), [irbank holders](https://irbank.net/E03859/holder), [Kabutan](https://kabutan.jp/news/marketnews/?b=n202512030954) (via `management_board_shareholders.md`)
  - Shikiho (Jun 2025): foreign ownership 33.2%; 特定株 (stable/specified holders) 46.6% — [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **Cross-holdings.**
  - TT holds 2.65% of Hulic and 5.53% of Yasuda Logistics; Hulic holds 1.22% of TT — [kabutan](https://kabutan.jp/stock/holder?code=3003), [Buffett Code](https://www.buffett-code.com/shareholder/1f2c707ea4a457a113d417a837a2265a) (via `industry_moats_strategy_stakes.md`)
  - TT filed a change report on its Hulic holding on 12 Dec 2024 (S100UWWV). It also filed material-event 臨時報告書 under Art. 19(2)(xii) on 11 Dec 2024 (S100UXJP) and 26 Dec 2024 (S100V0RC) — [EDINET 2024-12-11](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-12-11.csv), [2024-12-12](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-12-12.csv), [2024-12-26](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2024-12-26.csv)
- **MTP FY2025–27 targets:** business profit ¥95bn, ROE 10% and payout 40% by FY2027. Policy shareholdings ≤10% of net assets by end-2027, with at least ¥130bn sold. — [MTP (JP)](https://tatemono.com/company/pdf/plan2027_250116_ja.pdf) (via `industry_moats_strategy_stakes.md`)
- **FY2026 guidance:** business profit ¥102bn; main targets expected one year early — [logmi](https://finance.logmi.jp/articles/385621), [BigGo](https://finance.biggo.com/news/JP_8804.T_2026-02-16)
- **Credit:** JCR rating A; hybrid bonds rated BBB+ (May 2025) — [JCR](https://jcr.co.jp/download/10194f47b690f5b8ad8096559f9868ffb09165b80805048511/25d0289.pdf), [matsunosuke.jp](https://matsunosuke.jp/tokyo-tatemono-bond/) (via `coordinator_gap_fill.md`)
- **Main banks:** Mizuho, SMBC, MUFG — [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)

### Inferences
**Takeout arithmetic (D)**
- Inputs: 207.97m shares; BPS ¥2,934; NAV ¥4,937; FY26E EPS ¥312.5; FY25 EPS ¥283.1; net debt + NCI ¥1,454.7bn; FY26E OI ¥105.5bn; FY26E EBITDA about ¥129.5bn (D&A ¥24bn, E).

| Premium | ¥/share | Equity ¥bn | EV ¥bn | P/B | P/NAV | P/E FY26E | P/E FY25 | EV/EBITDA FY26E | EV/EBITDA FY25 | EV/EBIT FY26E |
|---|---|---|---|---|---|---|---|---|---|---|
| 0% | 3,286 | 683 | 2,138 | 1.12x | 0.67x | 10.5x | 11.6x | 16.5x | 18.0x | 20.3x |
| 20% | 3,943 | 820 | 2,275 | 1.34x | 0.80x | 12.6x | 13.9x | 17.6x | 19.2x | 21.6x |
| 30% | 4,272 | 888 | 2,343 | 1.46x | 0.87x | 13.7x | 15.1x | 18.1x | 19.7x | 22.2x |
| 40% | 4,600 | 957 | 2,411 | 1.57x | 0.93x | 14.7x | 16.2x | 18.6x | 20.3x | 22.9x |
| 50% | 4,929 | 1,025 | 2,480 | 1.68x | 1.00x | 15.8x | 17.4x | 19.2x | 20.9x | 23.5x |
| 60% | 5,258 | 1,093 | 2,548 | 1.79x | 1.06x | 16.8x | 18.6x | 19.7x | 21.5x | 24.2x |

**Cross-checks (D)**
- Peer-median forward P/E (13.35x) → ¥4,172 (+27%).
- Mitsubishi Estate's P/B (1.61x) → ¥4,724 (+44%).
- NAV parity → ¥4,937 (+50%).
- TT's own Feb-2026 high → ¥4,374 (+33%).
- A **¥4,300–¥4,900** bid zone is consistent with all four.

**Acquirer capacity: pro-forma ND/EBITDA (D)**
- Assumes the equity is bought at a 50% premium (¥1,025bn) and fully debt-funded.

| Acquirer | Standalone ND/EBITDA | Pro forma |
|---|---|---|
| Mitsui Fudosan | 8.3x | 10.6x |
| Mitsubishi Estate | 7.4x | 10.2x |
| Sumitomo Realty | 10.0x | 12.6x |
| Hulic | 10.1x | 14.1x |

- The two strongest balance sheets (Mitsubishi Estate, Mitsui) could finance a deal but would take on substantially more leverage, which pressures their A-range ratings (rating levels unverified). Hulic would need a share exchange.
- For a debt-funded strategic buyer, the earnings yield at a 40% premium (about 6.8% = 1/14.7) exceeds the after-tax cost of yen debt (likely about 1–2%, unverified), so the deal would be EPS-accretive before synergies.

**PE take-private feasibility (D/E)**
- At a 40% premium, EV is ¥2,411bn, or about 18.6x FY26E EBITDA.
- Acquisition debt of 10–12x EBITDA (E) would be about ¥1.3–1.55tn, which is only roughly what TT already owes. The equity cheque would be about ¥0.86–1.12tn (36–46% of EV).
- The exit thesis would rely on selling assets at or above book fair value. With P/NAV of about 0.93x at entry, the NAV discount captured is thin. This makes a classic PE bid economically marginal unless the buyer underwrites cap-rate compression or development profits.

**Reasons TT could be a target**
1. A discounted equity: P/NAV 0.65–0.67x, P/B 1.1x, forward P/E −21% vs peers.
2. Momentum: 1H26 business profit +20%; FY26 guidance raised; MTP targets a year early.
3. Strategic scarcity: a central-Tokyo (Yaesu/Kyobashi/Otemachi) land bank, JPR sponsorship (100%-owned AM) and the parking platform.
4. No blocking holder. Fuyo-lineage holders total about 4.3% (Meiji Yasuda plus Sompo; about 5.5% with Hulic's 1.22%), and the cross-holding web is being dismantled under the MTP (Hulic stake cut in Dec 2024).
5. The market environment: activists are present at peers, and sponsor take-privates of listed real-estate firms have become routine in 2024–26.

**Impediments**
1. **Size.** Unprecedented for Japanese real estate: equity of ¥0.9–1.0tn at a 30–50% premium is 4–5x the largest 2023–26 real-estate TOB target, about ¥0.2tn (Leopalace21, NTT UD REIT); EV would be ¥2.3–2.5tn.
2. Leverage: the highest ND/EBITDA in the group, 12.1x, and IBD/equity of about 2.5x at Jun-26.
3. **Earnings mix.** A material share of profit comes from investor property sales, which are cyclical (see `nav_forensic_risks.md` §2), and FY2025 net income fell 10.6%.
4. Bank relationships: Mizuho, SMBC and MUFG are relationship lenders, and change-of-control terms are unknown.
5. Takeover-defence status and FEFTA treatment are unverified. Real estate is generally not a designated core sector, but data-centre (Zeus OSA1) or infrastructure-adjacent assets may need checking.
6. Cultural precedent: no hostile bid among Japanese majors.

**Plausible acquirers, ranked by likelihood (inference)**
1. **Activist minority** (the Elliott, Murakami-linked or Ichigo playbook): pushing buybacks, faster asset or REIT recycling, and a higher payout.
2. **Friendly combination with Hulic.** Similar Tokyo focus and Yasuda-lineage registers; a share exchange is needed given leverage.
3. **Domestic major** (Mitsubishi Estate or Mitsui). Financially feasible, culturally unlikely.
4. **Global PE or sovereign club** (Blackstone, KKR, Brookfield, GIC, PAG, Lone Star, Fortress; named from background knowledge). Economically marginal, as shown above.
5. **Trading houses, insurers or rail groups as white knights.**

### Gaps
- **Not retrieved:** takeover-defence (poison pill) status; hybrid amount and terms; change-of-control covenants; FEFTA classification; the full list of 特定投資株式 (strategic shareholdings) and remaining cross-holders of TT; METI 2023 takeover guideline text; Japanese TOB-premium statistics; any 2025–26 press linking TT to bidders. No such press was found within the limited searches, which is not proof of absence.
- **FY2026 D&A** is estimated at ¥24bn.

## 7. Tokyo Tatemono's own acquisitions and investments, 2016–2026

### Takeaway
TT is not a serial corporate acquirer. Its verifiable deals are mostly minority stakes, joint ventures and reorganisations:
- **Star Mica Holdings (2975).** The largest identified corporate investment. A capital and business alliance was announced on 13 May 2026, using a third-party allotment plus a secondary sale. TT filed a large-holding report on 2 Jun 2026 showing **13.74%**. The cost was not disclosed in the sources; it is estimated at about ¥7–8bn at Star Mica's March-2026 market cap of ¥57.0bn.
- **Specified-subsidiary change.** A 臨時報告書 (extraordinary report) on 12 Oct 2023 under Art. 19(2)(iii). The subsidiary is unidentified.
- **Parking.** The group reorganised its parking business (Nippon Parking, NPC24H) on 1 Dec 2016.
- **Overseas JVs:** Indonesia (PT Farpoint, Dec 2018), Thailand (SC Asset condos Jan 2025, logistics/factories Sep 2026; WHA–KW Bangkok office), Australia (Charter Hall/UBS industrial; Lendlease and Nippon Steel Kowa).
- **Data centre:** Osaka Zeus OSA1 JV with SC Zeus Data Centers (construction from Dec 2025).

On the disposal side, the Hulic stake was cut (Dec 2024) and an Akihabara hotel was sold to APA. Transaction multiples are not available for any of these.

### Cited Findings
- **Star Mica Holdings (2975).** On 13 May 2026, 16:00, Star Mica disclosed 「東京建物株式会社との資本業務提携契約の締結、第三者割当増資による新株式の発行及び株式の売出し並びに主要株主の異動に関するお知らせ」: a capital and business alliance with TT, issuance of new shares by third-party allotment, a secondary offering of shares, and a change in major shareholder — [TDnet daily list cache 13 May 2026](https://raw.githubusercontent.com/coolait/CrestBreakProject/HEAD/cache/tdnet/daily/20260513_p002.html)
  - TT (E03859) filed a 大量保有報告書 on Star Mica (E34707), doc **S100Y6E2**, on 2 Jun 2026 15:32 — [EDINET index 2026-06-02](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2026-06-02.csv)
  - The holding is **13.74%**, "held for capital and business alliance" — [Matsui news](https://finance.matsui.co.jp/news/582338/index), [MAonline](https://maonline.jp/kabuhoyu/sh-s100y6e2) (via `stock_catalysts_capital_returns.md`)
  - Star Mica's Mar-2026 data: price ¥1,641; market cap ¥57.0bn; P/B 1.88x; FY11/2025 NI ¥4.18bn; FY11/2026 Toyo Keizai NI estimate ¥5.1bn — [Shikiho 2975](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/2975.txt)
- **TT's extraordinary reports, Nov 2022–Oct 2026.** All from the [EDINET mirror](https://raw.githubusercontent.com/code4fukui/EDINET/HEAD/data/documents/2023-10-12.csv) (index files for each date):
  - 12 Oct 2023: S100S096, Art. 19(2)(iii), change in specified subsidiary.
  - 11 Dec 2024: S100UXJP, Art. 19(2)(xii).
  - 26 Dec 2024: S100V0RC, Art. 19(2)(xii).
  - Representative-director changes (9号): 13 Dec 2022 (S100PSEA) and 21 Nov 2024 (S100UTKT).
  - AGM results (9号の2): 1 Apr 2024, 28 Mar 2025 and 30 Mar 2026.
  - TT's only large-holding filings in the period are Hulic (change report, 12 Dec 2024) and Star Mica (new, 2 Jun 2026).
- **Parking.** Group parking business reorganised on 1 Dec 2016 — [TT/NPC release](https://pdf.irpocket.com/C8804/HJXQ/ZXAr/cQ9X.pdf). Nippon Parking had about 1,905 sites and 86,792 spaces at Dec 2024 — [TT recruit page](https://recruit.tatemono.com/recruit/shinsotsu/about/biz05.html) (both via `business_model_supply_chain.md`). Shikiho says the business has about 90,000 spaces and is expanding through large car-park management contracts — [Shikiho 8804](https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/8804.txt)
- **Overseas and data-centre JVs:**
  - Indonesia: PT Farpoint JV, Dec 2018 — [Jakarta Post](https://www.thejakartapost.com/adv/2018/12/15/farpoint-tokyo-tatemono-set-up-joint-venture-company.html)
  - Thailand: SC Asset partnership, Jan 2025 — [TT news](https://tatemono.com/english/news/20250114.html); Sep 2026 — [TT release](https://tatemono.com/english/news/images/a29a639c2992033bba196bc648def8ea_1.pdf)
  - Thailand: WHA–KW Bangkok CBD office JV — [WHA](https://www.wha-group.com/en/news-media/company-news/1612/whakw-alliance-and-tokyo-tatemono-asia-announce-joint-venture-to-invest-in-bangkok-cbd-prime-office-space)
  - Australia: Charter Hall/UBS industrial partnership — [Mingtiandi](https://www.mingtiandi.com/real-estate/logistics/tokyo-tatemono-ubs-form-industrial-partnership-with-charter-hall/)
  - Osaka data centre: Zeus OSA1 with SC Zeus Data Centers, phase 1 of 25MW due 2028 — [DX Magazine](https://dxmagazine.jp/news/wgrf8qx/)
  - Sources via `industry_moats_strategy_stakes.md` and `business_model_supply_chain.md`.
  - FY2025 overseas equity-method loss: ¥6.87bn — [FY2025 tanshin](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf)
- **Subsidiaries named in the FY2022 Yuho** include 東京建物リゾート, 東京不動産管理, エキスパートオフィス, プライムプレイス, 東京建物アメニティサポート, かちどきGROWTH TOWN, イー・ステート・オンライン, 東京建物不動産販売 and 日本パーキング. The group had 61 related companies: 29 consolidated, 22 equity-method — [Yuho FY2022 事業の内容 (GitHub mirror)](https://raw.githubusercontent.com/yuukimiyo/stdata-jp/HEAD/8/88040/2023/DescriptionOfBusiness)
- **Disposals:**
  - Hulic stake reduced (EDINET change report S100UWWV, 12 Dec 2024).
  - APA Group acquired an Akihabara hotel from TT; date and price not retrieved — Nikkei Real Estate Market Report headline (via `coordinator_gap_fill.md`).

### Inferences

**TT acquisitions and investments, 2016–2026**

| Date | Target / investment | Type | Cost | Multiples | Source status |
|---|---|---|---|---|---|
| 1 Dec 2016 | Parking business (Nippon Parking, NPC24H) | Group reorganisation | n/v | n/v | Release sourced; terms not retrieved |
| Dec 2018 | PT Farpoint JV (Indonesia condos) | Overseas JV | n/v | n/v | Sourced |
| 12 Oct 2023 | Unidentified specified subsidiary (Art. 19(2)(iii)) | Subsidiary change; possibly a large capital injection or a new SPC/overseas vehicle | n/v | n/v | Filing sourced; content not retrieved |
| Oct 2024 (partner date) | Australia residential/office with Lendlease and Nippon Steel Kowa | JV | n/v | n/v | Via sibling notes |
| Jan 2025 / Sep 2026 | SC Asset (Thailand): condos, then logistics/factories | JV programme | n/v | n/v | Sourced |
| Dec 2025 | Zeus OSA1 data centre (Osaka) with SC Zeus Data Centers | Development JV | n/v | n/v | Sourced |
| 13 May / 2 Jun 2026 | **Star Mica HD (2975), 13.74%** | Minority strategic stake (new shares plus secondary) | **About ¥7.8bn (E)** = 13.74% × ¥57.0bn Mar-26 market cap | **About 11x FY26E P/E; about 1.9x P/B (E)** at the Mar-26 price | Sourced except cost |

**Reading the record**
- The Star Mica stake gives TT a foothold in pre-owned condo renovation and resale, next to its Brillia and brokerage businesses. It mirrors the 2025–26 sector trend of developers buying condo-renovation platforms: Seibu RE→E-Grand, Daito→The Global.
- **Balance-sheet growth outweighs corporate M&A.** TT's balance-sheet expansion (IBD +¥191bn and net debt +¥249bn in 1H FY2026) is far larger than any corporate deal identified. TT grows mainly through land and asset acquisition and redevelopment, not M&A.

### Gaps
- **Not retrieved:** the Star Mica price per share, total cost, the split between new and secondary shares, and alliance terms. These are in the 13 May 2026 TDnet PDFs, which were blocked.
- **Not identified:** the Oct-2023 specified subsidiary.
- **FY2016–FY2022 business-combination notes (企業結合等関係)** were not retrieved, nor the cost and terms of any overseas JV.
- **Whether TT made other corporate acquisitions in 2016–2022** is unknown. The EDINET mirror starts in Nov 2022, and the TT Yuho 企業結合 notes for FY2016–FY2021 must be checked.
- **Nippon Parking's acquisition history** (a blog says it was an Itochu MBO before joining TT) is unverified.
