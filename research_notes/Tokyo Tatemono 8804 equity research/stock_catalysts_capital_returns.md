# Tokyo Tatemono (8804 JP): share-price history, catalysts behind moves of more than 10%, technicals, dividends, buybacks/treasury shares and short interest (Oct 2021 to Oct 2026)

*Compiled 4 Oct 2026. All money in JPY; TSE Prime prices.*

*How the data was gathered:*
- *This environment's network egress policy blocked every programmatic and primary price source, for both curl and page fetches. Blocked hosts included Yahoo Finance chart API, stooq CSV, kabutan, karauri.net, irbank, JPX, TDnet, EDINET, tatemono.com, minkabu, Matsui and stockanalysis.*
- *The session's shared web-search budget (200 searches) ran out partway through this task.*
- *My own figures therefore come from search-engine extractions of the cited pages. The pages themselves were never opened.*
- *Items marked **†** come from parallel workstream notes in this folder (`earnings_guidance_consensus.md`, `industry_moats_strategy_stakes.md`, `management_board_shareholders.md`, `nav_forensic_risks.md`). Their original source URLs are given, but I did not re-verify them.*

*Companion dataset: `stock_prices_8804.csv` in this folder (32 rows). It contains annual OHLC for 2017–2026 YTD, monthly OHLC for Jan–Sep 2026 and dated price points. Nothing in it is interpolated.*

## 1. Price data: latest close, 52-week/all-time range, annual OHLC 2020–2026 YTD, market cap, share count, liquidity, chart dataset

### Takeaway
- **Latest price:** ¥3,211 on Fri 2 Oct 2026. This comes from a secondary blog, but it ties exactly to the "−26.6% from the high" figure. The last close verified across two sources is ¥3,236 on 18 Sep 2026.
- **Market cap:** about ¥668bn at ¥3,211 (my calculation). Kabutan showed ¥683.4bn on 25 Sep 2026.
- **Shares:** 207,978,574 issued, of which 839,526 were held in treasury at 31 Dec 2025.
- **Range:** all-time high **¥4,374 on 27 Feb 2026**. The 52-week low is ¥2,994 or lower, from 13 Nov 2025 (derived). The 2026 low is ¥3,083 (28 May).
- **Price returns by year:** −4.8% (2022), +32.1% (2023), +23.4% (2024), +36.0% (2025), −9.4% in 2026 to 2 Oct.
- **Missing:** month-end closes before Jan 2026 could not be retrieved.

### Cited Findings
**Latest price points (most recent first)**
- 2 Oct 2026: ¥3,211, described as −26.6% from the ¥4,374 high; the arithmetic ties (blog data as of 2 Oct 2026). — [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) †
- 1 Oct 2026 close of ¥3,255 is **UNVERIFIED**. A search summary said "10月1日の終値は3,255.0円", but the year and page could not be attributed. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) (one of the pages listed)
- 25 Sep 2026, 11:18 JST: ¥3,286, −¥7 (−0.21%). PER 10.5x, PBR 1.12x, forecast yield 3.83%, market cap ¥683.4bn. The search summary printed the market cap as "6,834 billion yen", i.e. 6,834億円. — [Kabutan quote](https://s.kabutan.jp/stocks/8804/)
- 18 Sep 2026: close ¥3,236. This is both the latest data point in Nikkei's annual table and the close of kabutan's partial September bar. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)
- Another source set for 18 Sep 2026 gives: market cap ¥684.9bn, PBR 1.10x, BPS ¥2,930 (1H FY2026), forecast EPS ¥313.3, forward P/E 10.3x. — [IFIS kabuyoho](https://kabuyoho.ifis.co.jp/index.php?action=tp1&sa=report_per&bcode=8804); [Monex Scouter](https://scouter.monex.co.jp/report/theoryDps/8804) †
- 24 Jul 2026: ¥3,427; market cap ¥712.7bn. — [Matsui Securities](https://finance.matsui.co.jp/stock/8804/index); [minkabu](https://minkabu.jp/stock/8804)

**Shares**
- Issued shares at 31 Dec 2025: **207,978,574**. Shares outstanding excluding treasury: **207,139,048**. The Board Benefit Trust (BBT, a stock-compensation trust) holds **351,300** shares, shown under financial institutions rather than as treasury stock. — [j-lic.com](https://j-lic.com/companies/8804) †
- Quote sites show 207,978 thousand issued shares. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Kabutan](https://s.kabutan.jp/stocks/8804/)
- The FY2025 annual securities report (第208期) was filed on 23 Mar 2026. It is the primary source for 自己株式, TSR and highs/lows. — [Nikkei Yuho page](https://www.nikkei.com/nkd/company/ednr/?scode=8804)

**All-time and 52-week range**
- All-time high ¥4,374.0 on 27 Feb 2026. All-time low ¥388.0 on 13 Mar 2009. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [minkabu](https://minkabu.jp/stock/8804)
- 2026 YTD: high ¥4,374.0 (27 Feb), low ¥3,083.0 (28 May). — [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)
- **Late-2025 points:**
  - The 2025 high at that point was ¥3,074, set on 7 Oct 2025.
  - On the trading day after the 13 Nov 2025 upgrade ("most likely 14 Nov 2025"), the shares jumped ¥311 to ¥3,305, implying a prior close of ¥2,994.

  — [f-p.jp (kabutan-sourced)](https://f-p.jp/media/?p=21023); [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-revises-2025-financial-and-dividend-forecasts) †

**Annual OHLC, JPY.** Source: [Nikkei 10-year price history](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804). Kabutan's yearly and monthly pages agree for 2025–2026. The "Close-to-close" column is my calculation.

| Year | Open | High | Low | Close | Close-to-close |
|---|---|---|---|---|---|
| 2019 | 1,101 | 1,740 | 1,078 | 1,709 | +49.9% |
| 2020 | 1,705 | 1,828 | 904 | 1,415 | −17.2% |
| 2021 | 1,415 | 1,852 | 1,367 | 1,680 | +18.7% |
| 2022 | 1,692 | 2,190 | 1,569 | 1,599 | −4.8% |
| 2023 | 1,590 | 2,191 | 1,484 | 2,112 | +32.1% |
| 2024 | 2,097 (4 Jan) | 2,774 | 2,029 | 2,607 (30 Dec) | +23.4% |
| 2025 | 2,594 (6 Jan) | 3,655 (26 Dec) | 2,237.5 (7 Apr) | 3,546 (30 Dec) | +36.0% |
| 2026 YTD (to 18 Sep) | 3,552 | 4,374 (27 Feb) | 3,083 (28 May) | 3,236 (18 Sep) | −8.7% (−9.4% to 2 Oct at ¥3,211) |

- Nikkei also lists 2017 (1,583 / 1,653 / 1,305 / 1,522) and 2018 (1,522 / 1,858 / 1,061 / 1,140). — [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)

**Monthly OHLC for 2026, JPY.** Source: [Kabutan monthly bars](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/), also at [kabutan.jp ashi=mon](https://kabutan.jp/stock/kabuka?code=8804&ashi=mon). The m/m column is my calculation.

| Month | Open | High | Low | Close | m/m |
|---|---|---|---|---|---|
| Jan 2026 | 3,552 | 3,777 | 3,501 | 3,629 | +2.3% |
| Feb 2026 | 3,689 | 4,374 | 3,603 | 4,374 | **+20.5%** |
| Mar 2026 | 4,234 | 4,304 | 3,462 | 3,587 | **−18.0%** |
| Apr 2026 | 3,698 | 3,922 | 3,523 | 3,599 | +0.3% |
| May 2026 | 3,573 | 3,606 | 3,083 | 3,269 | −9.2% |
| Jun 2026 | 3,350 | 3,448 | 3,135 | 3,296 | +0.8% |
| Jul 2026 | 3,300 | 3,542 | 3,223 | 3,387 | +2.8% |
| Aug 2026 | 3,340 | 3,475 | 3,245 | 3,445 | +1.7% |
| Sep 2026 (to 18 Sep only) | 3,424 | 3,481 | 3,236 | 3,236 | −6.1% |

**EPS and an undated snapshot**
- Actual EPS: FY2021 ¥167.35, FY2022 ¥206.15, FY2023 ¥215.82, FY2024 ¥315.49. — [Matsui results page](https://finance.matsui.co.jp/stock/8804/settlement/index); [FISCO](https://web.fisco.jp/platform/companies/0880400)
- An undated aggregator snapshot, of low reliability, shows: price ¥3,688; 52-week range ¥2,237.50–¥4,374.00; 1-yr +21.0%; 3-yr +65.23%; 5-yr +129.79%. — [Simply Wall St](https://www.simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares); [TipRanks](https://www.tipranks.com/stocks/jp:8804)

### Inferences
- **Treasury shares.** At 31 Dec 2025 treasury stock was **839,526 shares** (207,978,574 − 207,139,048), about 0.40% of issued shares. The 351,300 BBT shares are held separately.
- **Market cap cross-check.** Price × 207.978m shares reproduces two of the reported market caps:
  - ¥3,427 gives ¥712.7bn;
  - ¥3,286 gives ¥683.4bn.

  On the same basis, market cap was about ¥909.7bn at the all-time high and about ¥667.8bn at ¥3,211 on 2 Oct. IFIS's ¥684.9bn at ¥3,236 implies about 211.7m shares, which does not tie to any share count found. Treat that figure as an outlier.
- **52-week low.** For roughly Oct 2025 to Oct 2026 the low is **¥2,994 or lower** (13 Nov 2025). The exact value depends on Oct–Nov 2025 prices that were not retrieved.
- **Cross-source consistency.** Nikkei and kabutan agree with each other:
  - 2026 open 3,552 matches the Jan open;
  - the YTD high and low match the Feb high and May low;
  - Dec 2025 close 3,546 matches the Jan 2026 open of 3,552.

  This makes the annual and 2026 monthly series reasonably reliable even though the pages were never opened.
- **Annual swings measured from the prior year-end close:**

  | Year | Prior close to year high | Prior close to year low |
  |---|---|---|
  | 2022 | +30.4% | −6.6% |
  | 2023 | +37.0% | −7.2% |
  | 2024 | +31.3% | −3.9% |
  | 2025 | +40.2% | −14.2% |
  | 2026 YTD | +23.4% | −13.1% |

- **Earnings drove most of the 2021–2024 gain.** Trailing P/E at each year-end (calculated):

  | Year-end | P/E |
  |---|---|
  | 2021 | 10.0x |
  | 2022 | 7.8x |
  | 2023 | 9.8x |
  | 2024 | 8.3x |

  EPS rose 88.5% from FY2021 to FY2024, while the price rose 55.2% from end-2021 to end-2024. The multiple therefore compressed.
- **2025 was a re-rating year (estimate).** FY2025 EPS was about ¥283 (FY2025 net income of ¥58.879bn † over about 208m shares). The price rose 36% while EPS fell, putting the end-2025 P/E at about 12.5x. In 2026 the shares de-rated to about 10.3x forward earnings.
- **The undated snapshot does not hold together.** Its 52-week low (7 Apr 2025) means it was taken no later than 7 Apr 2026. But its 1-yr +21% implies a year-earlier price near ¥3,050, while March 2025 buyback prices averaged about ¥2,450. It is not used.
- **What the CSV contains.** `stock_prices_8804.csv` has columns `date, period, frequency, open, high, low, close, price_type, source_url, notes` and covers:
  - annual rows for 2017–2025 plus 2026 YTD;
  - monthly bars for Jan–Aug 2026 plus a partial September bar;
  - dated points: 7 Apr 2025 low; 7 Oct 2025 high; 13 Nov 2025 (derived) and 14 Nov 2025; 26 Dec 2025 high; 24 Jul, 24 Sep (derived), 25 Sep and 2 Oct 2026; and 1 Oct 2026 (flagged unverified);
  - three "reference" rows giving average buyback prices for Mar 2025, May 2025 and the whole Feb–Aug 2025 programme. These are period averages, **not** closes.

  Month-end dates are the last TSE trading day of each month, inferred from the calendar.

### Gaps
- **Month-end closes Oct 2021–Dec 2025 (51 months) are missing.** Yahoo `query1.finance.yahoo.com`, `stooq.com`, kabutan monthly page 2 onwards and investing.com were all blocked by the egress proxy, and search snippets only exposed 2026. No TOPIX or TOPIX Real Estate series and no peer price series could be obtained.
- **Not verified:**
  - the exact 52-week low;
  - official closes for 1–2 Oct 2026 (the ¥3,211 comes from a blog);
  - the September 2026 month-end close.
- **Not found:**
  - average daily trading volume or value;
  - year-end treasury share counts for FY2021–FY2024;
  - dates of the annual highs and lows for 2021–2024.
- **What would unblock this.** Allowing these hosts in the environment's network settings would close most of these gaps: `query1.finance.yahoo.com`, `stooq.com`, `kabutan.jp`, `karauri.net`, `irbank.net`, `jpx.co.jp`, `release.tdnet.info`, `disclosure2.edinet-fsa.go.jp`, `tatemono.com`.

## 2. Moves of more than 10% (Oct 2021 to Oct 2026) and their causes

### Takeaway
- **The one single-day move of more than 10%:** **+10.4% (+¥311 to ¥3,305)** on the session after the 13 Nov 2025 upgrade to guidance and dividend. It was stock-specific.
- **Other 2025–2026 windows of more than 10%:**
  - the April 2025 tariff-shock low (−13.7% YTD) and +37% rally to 7 Oct 2025;
  - a +22% run from 13 Nov to 26 Dec 2025, even as the BOJ hiked to 0.75%;
  - **+20.5% in Feb 2026** to the all-time high, after FY2025 results and FY2026 guidance that beat consensus (DPS ¥122);
  - **−20.9% from the 27 Feb peak to the March low**, a rate- and oil-driven sector sell-off;
  - −21.4% from the April high to 28 May, after a weak Q1 and a sector low;
  - +14.9% from late May to July.
- **Peers:** in the 2026 sector drawdown 8804 fell less than the large peers: −26.6% against −33.6% to −42.2% for Mitsui, Mitsubishi and Sumitomo.
- **2022–2024:** annual swings were large (2022 high to 2023 low −32%), but without daily data they cannot be dated or tied to BOJ events.

### Cited Findings
**Windows of more than 10%.** Percentages are calculated from the cited prices.

| # | Window | Move | Evidence | Reported or likely cause | Stock-specific vs market |
|---|---|---|---|---|---|
| 1 | 2022 high (date n/a) → 30 Dec 2022 close, extending to the 2023 low (date n/a) | ¥2,190 → ¥1,599 (**−27.0%**); → ¥1,484 (**−32.2%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified. The 2022 close was only 1.9% above the 2022 low, which fits a late-2022 slump such as the BOJ YCC widening on 20 Dec 2022 (inference) | Probably macro/sector (inference) |
| 2 | 2023 low → 2023 high (dates n/a) | ¥1,484 → ¥2,191 (**+47.6%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified | n/a |
| 3 | 2024 low → 2024 high (dates n/a) | ¥2,029 → ¥2,774 (**+36.7%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified. The 2024 low was only 3.9% below the end-2023 close. | n/a |
| 4 | 6 Jan 2025 open → 7 Apr 2025 low | ¥2,594 → ¥2,237.5 (**−13.7%**). Measured from the March-2025 average buyback price of ¥2,451 it is −8.7%. | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [FilingReader](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares) | Mid-January: the new medium-term plan disappointed (see below). 7 Apr 2025 was the global tariff sell-off day (macro date not verified here). | Mixed, mostly market |
| 5 | 7 Apr 2025 → 7 Oct 2025 | ¥2,237.5 → ¥3,074 (**+37.4%**); by May the stock was already about +14% (¥2,560 average buyback price) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [FilingReader May-25](https://filingreader.com/news-wire/tokyo/2025-06-02/tokyo-tatemono-continues-share-repurchase-program-in-may-2025); [f-p.jp](https://f-p.jp/media/?p=21023) † | Post-shock recovery. The ¥3.0bn buyback was executed 13 Feb–31 Aug 2025 (Q5). | Market plus support from the buyback |
| 6 | 13 Nov 2025 → next session (most likely 14 Nov) | ¥2,994 → ¥3,305 (**+10.4% in one day**). Simply Wall St headline: "Is Up 13.4% After Reviewing Dividend…". | [f-p.jp (kabutan)](https://f-p.jp/media/?p=21023) †; [Simply Wall St](https://simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares/news/why-tokyo-tatemono-tse8804-is-up-134-after-reviewing-dividen) | Q3 upgrade on 13 Nov 2025: FY2025 OP guidance +¥6.5bn to ¥92.5bn, NI +¥3.0bn to ¥58.0bn, DPS +¥6 to ¥103, recurring profit +6% to a record. A revised sales policy cut revenue guidance but raised OP. The board also considered cancelling treasury shares. ([Kabutan news](https://kabutan.jp/stock/news?code=8804&b=k202511130214); [Nikkei](https://www.nikkei.com/article/DGXZQOUB132440T11C25A1000000/); [FilingReader](https://filingreader.com/news-wire/tokyo/2025-11-13/tokyo-tatemono-revises-full-year-forecasts-boosts-dividends) †) | **Stock-specific** |
| 7 | 13 Nov 2025 → 26 Dec 2025 | ¥2,994 → ¥3,655 (**+22.1%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Follow-through from the upgrade. The rise came despite the BOJ hike to 0.75% in Dec 2025 and the 10-yr JGB touching 2.1% on 22 Dec 2025 ([NRI](https://www.nri.com/jp/media/column/kiuchi/20251222_2.html) †). | Stock-specific (rose against a rates headwind) |
| 8 | 30 Jan → 27 Feb 2026; February low → 27 Feb | ¥3,629 → ¥4,374 (**+20.5%**); ¥3,603 → ¥4,374 (**+21.4%**). Closed the month at the all-time high. | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | **FY2025 results on 12 Feb 2026:** record OP; DPS ¥105 (12th straight rise). **FY2026 guidance:** NI ¥63.0bn against QUICK consensus of ¥61.25bn; DPS ¥122 (+¥17), a 40.2% payout reached a year ahead of plan ([Nikkei/QUICK](https://www.nikkei.com/article/DGXZRST0554860Q6A210C2000000/) †; [Nikkei](https://www.nikkei.com/article/DGXZQOUB126EM0S6A210C2000000/) †; [japanir](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/)). **Sector:** Nikkei Veritas (28 Feb) said the shares surged "riding the real-estate boom" ([Nikkei company page](https://www.nikkei.com/nkd/company/?scode=8804)). **Asset:** TOFROM YAESU TOWER completion is reported as Feb 2026 ([offisite](https://offisite.jp/discovers/view/39)); an older plan had 31 Jul 2025 ([Kenbiya](https://www.kenbiya.com/ar/ns/region/tokyo/8849.html) †). | Mixed, mainly stock-specific (results and DPS) plus sector boom |
| 9 | 27 Feb → March low (date n/a) | ¥4,374 → ¥3,462 (**−20.9%**); March month −18.0% | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | The 10-yr JGB rose from 2.132% (27 Feb) to 2.366% (31 Mar) on oil-driven inflation worries. Mitsui Fudosan and Mitsubishi Estate fell sharply again on 23 Mar. 8804 "fell with the sector", and there were fears of a repeat of the Aug-2024 "Ueda shock". ([PayPay Securities, 24 Mar 2026](https://media.paypay-sec.co.jp/cat5/jisha260324); [Nomura WealthStyle](https://www.nomura.co.jp/wealthstyle/article/0728/); [kabu.tagu-blog](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026)) | **Sector/macro (rates)** |
| 10 | March low → April high (dates n/a) | ¥3,462 → ¥3,922 (**+13.3%**) | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | Not found. PayPay flagged a possible "double bottom" on 24 Mar. | Probably a sector relief rally (inference) |
| 11 | April high → 28 May 2026 (YTD low); 27 Feb → 28 May | ¥3,922 → ¥3,083 (**−21.4%**); peak to trough **−29.5%** | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | **Q1 FY2026 results (13 May):** NI −60.2% y/y, condo deliveries 235 vs 772 units, guidance and ¥122 DPS kept ([Nikkei](https://www.nikkei.com/article/DGXZQOUB136Z90T10C26A5000000/) †; [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-q1-profit-slumps-but-full-year-outlook-and-dividend-plan-held) †). **Sector:** the TOPIX real-estate index fell 3.0% on 18 May to a YTD low, and the TSE REIT index also fell ([Nikkei, 18 May 2026](https://www.nikkei.com/article/DGXZQOUB184UQ0Y6A510C2000000/) †). | Mixed: weak quarter plus sector lows |
| 12 | 28 May → July high (date n/a) | ¥3,083 → ¥3,542 (**+14.9%**) | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | Not found. The rebound held through the BOJ hike to 1.00% in June 2026 ([DLRI](https://www.dlri.co.jp/report/macro/665928.html) †) and the TSE REIT index's June lows ([Nikkei](https://www.nikkei.com/article/DGKKZO96735190V00C26A6DTC000/) †). | n/a |
| 13 | 27 Feb → 2 Oct 2026 (comparison with peers) | 8804 **−26.6%** (¥3,211). From their Feb–Mar 2026 highs: Mitsubishi Estate −34.1%; Mitsui Fudosan −33.6% (¥1,425 on 18 Aug 2026); Sumitomo Realty −42.2%. | [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) † (blog; method unknown) | Rate-driven sector de-rating | Sector; 8804 outperformed its peers |

**Near-misses and catalysts with no move of more than 10%**
- **16–17 Jan 2025: new medium-term plan (2025–2027).**
  - The plan was published on 16 Jan 2025. Targets: payout ratio raised to 40% by FY2027 (from "30% or more"), ROE 10%, FY2027 business profit ¥95bn, policy shareholdings cut to 10% or less of net assets with at least ¥130bn sold. — [MTP PDF](https://tatemono.com/company/pdf/plan2027_250116_ja.pdf) †; [Nikkei](https://www.nikkei.com/article/DGXZQOUC169A00W5A110C2000000/) †
  - Nikkei then ran "東京建物の株価大幅反落 新中計に「物足りない」の見方も": the shares fell sharply as the plan was seen as underwhelming. — [Nikkei](https://www.nikkei.com/article/DGXZQOFL171HB0X10C25A1000000/)
  - The size of the fall was not found.
- **6 Aug 2026: Q2 results.**
  - FY2026 OP guidance raised from ¥100.0bn to ¥105.5bn and NI from ¥63.0bn to ¥65.0bn (+10.4%); DPS raised from ¥122 to ¥126. Management said the main plan targets would be met a year early. — [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/); [Minkabu](https://minkabu.jp/news/4589327) †; [Logmi](https://finance.logmi.jp/articles/385621) †
  - The August month closed only +1.7%. A parallel note describes a steady three-day rise rather than a gap-up. †
- **Aug 2026:** the 10-yr JGB touched 2.945% intraday. — [Nikkei](https://www.nikkei.com/article/DGXZQOUB1747W0X10C26A8000000/) †
- **17–18 Sep 2026:** the BOJ raised its policy rate to 1.25%, the highest since 1995, by a 7–2 vote. — [NHK](https://news.web.nhk/newsweb/na/nd-20260918de50968) †; [DLRI](https://www.dlri.co.jp/report/macro/665928.html) †
  - 8804 closed at its September low of ¥3,236 on 18 Sep ([Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)).
  - The fall from the July high to 2 Oct is **−9.3%** (¥3,542 → ¥3,211), just under the 10% threshold.
- **2 Jun 2026: Star Mica stake.** Tokyo Tatemono filed a large-holding report showing 13.74% of **Star Mica Holdings (2975)**, held for a capital and business alliance. — [Matsui news](https://finance.matsui.co.jp/news/582338/index); [MAonline](https://maonline.jp/kabuhoyu/sh-s100y6e2)
- **No activist found.** No activist stake in 8804 was found, and all ≥5% filers are passive or asset managers (see Q7). — [itiger/Bloomberg summary](https://www.itiger.com/news/2492267336); management notes †

### Inferences
- **Stock-specific triggers worked; macro set the direction.** The two clearest stock-specific moves of more than 10% were both reactions to raised guidance and dividends:
  - +10.4% in one day on 14 Nov 2025;
  - +20.5% in February 2026, with DPS +16% and FY2026 guidance above consensus.

  The largest falls (March and May 2026) were sector-wide rate moves. In May a weak, timing-driven Q1 made things worse.
- **Defensive within its sector in 2026.** 8804 fell less than its large peers (−26.6% against −33.6% to −42.2%). This fits its higher yield (about 3.8–3.9% against 1.35–2.45% for Mitsubishi and Mitsui †) and its lower P/E.
- **Pre-2025 swings.** The 2022–2024 swings of more than 10% (#1–#3) are real, since the annual high–low gaps are 37–48%. The 2022 close sitting near the year's low points to a slump into late December 2022, which is consistent with the 20 Dec 2022 YCC shock. That attribution is inference only.
- **Policy announcements were not big movers on their own.** The Jan 2025 medium-term plan was a negative ("underwhelming") despite raising the payout target. Before the November upgrade, the 2025 buyback coincided with recovery rather than causing a jump.

### Gaps
- **No daily data.** Without it, single-day moves cannot be ranked, and the 2022–2024 highs and lows cannot be matched to these events: the 20 Dec 2022 YCC widening; the 19 Mar 2024 end of negative rates; the 31 Jul 2024 hike; the 5 Aug 2024 crash and 6 Aug rebound; the 24 Jan 2025 hike.
- **These pre-2025 macro dates are background knowledge, not verified in this session.** The 2025–26 BOJ steps (Dec 2025 to 0.75%, Jun 2026 to 1.00%, Sep 2026 to 1.25%) are sourced via parallel notes.
- **Not found:**
  - the size of the January 2025 medium-term plan reaction;
  - the cause of the Mar→Apr 2026 rebound and the May→Jul 2026 rebound;
  - the exact June 2026 BOJ date;
  - any MSCI, TOPIX or other index-weight events;
  - large property-sale announcements with price reactions.
- **Peer moves are thin.** Only the 2026 drawdowns (from a blog) are available; no peer moves were found for 2022–2025.

## 3. Technical snapshot (as of 2 Oct 2026, with reference to 18–25 Sep)

### Takeaway
At **¥3,211 (2 Oct 2026)** the stock is below all estimated moving averages:
- about 4.5% below the roughly 50- and 100-day levels (≈¥3,360–3,370);
- about 9.7% below the roughly 200-day level (≈¥3,550).

It is **26.6% below its all-time high** and only **4.2% above the 2026 low (¥3,083)**. The lower highs since February continue. The 2 Oct price has slipped below the Jul–Sep floor (¥3,223–3,245), which breaks the rising lows of the June–September triangle. The next support is ¥3,135, then ¥3,083. Kabuyoho's trend signal reads "sell continuation".

### Cited Findings
- **Prices:**
  - ¥3,211 on 2 Oct 2026 ([kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) †);
  - ¥3,286 at 11:18 on 25 Sep 2026 ([Kabutan](https://s.kabutan.jp/stocks/8804/));
  - ¥3,236 close on 18 Sep 2026 ([Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)).
- **Range:** all-time high ¥4,374 (27 Feb 2026); 2026 low ¥3,083 (28 May 2026). — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)
- **Monthly ranges** (low – high). September closed at its low (¥3,236). — [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)

  | Month | Range |
  |---|---|
  | Jun | ¥3,135–3,448 |
  | Jul | ¥3,223–3,542 |
  | Aug | ¥3,245–3,475 |
  | Sep (to 18 Sep) | ¥3,236–3,481 |

- **Kabuyoho technical trend signal:** 売り継続 ("sell continuation"), crawled around Sep 2026. — [kabuyoho trend signal](https://kabuyoho.jp/reportTrendSignal?bcode=8804); [kabuyoho chart](https://kabuyoho.jp/reportChart?bcode=8804)
- **Valuation:**
  - 25 Sep 2026: PER 10.5x, PBR 1.12x, yield 3.83% ([Kabutan](https://s.kabutan.jp/stocks/8804/));
  - 18 Sep 2026: forward P/E 10.3x, PBR 1.10x on BPS ¥2,930 ([IFIS](https://kabuyoho.ifis.co.jp/index.php?action=tp1&sa=report_per&bcode=8804) †).

### Inferences
**Estimated moving averages (all ESTIMATES).** Each is a trading-day-weighted average of monthly mid-ranges ((high+low)/2) from the kabutan bars, because daily data was unavailable. Expect roughly ±2–3% error. They are computed to 18 Sep, and late-September prices (about ¥3,211–3,293) would pull them down slightly. The "vs" columns show where the price stands relative to each average.

| Proxy | Estimate | vs ¥3,211 (2 Oct) | vs ¥3,236 (18 Sep) |
|---|---|---|---|
| ~50-day | ≈ ¥3,367 | −4.6% | −3.9% |
| ~100-day | ≈ ¥3,359 | −4.4% | −3.7% |
| ~200-day | ≈ ¥3,554 (mean of month-end closes Dec 2025–Sep 2026 = ¥3,537) | −9.7% | −8.9% |
| 52-week / all-time high ¥4,374 | n/a | −26.6% | −26.0% |
| 2026 low ¥3,083 | n/a | +4.2% | +5.0% |
| 52-week low (≤ ¥2,994, Nov 2025) | n/a | at least +7.2% | at least +8.1% |

- **Moving-average alignment is bearish.** The short averages (≈¥3,360) sit below the long one (≈¥3,550), a death-cross-type set-up, and the price is below all of them. This is consistent with Kabuyoho's "sell" signal.
- **Trend has two layers.**
  - The primary, multi-year uptrend is intact on annual lows (¥1,484 in 2023, ¥2,029 in 2024, ¥2,237.5 in 2025, ¥3,083 in 2026).
  - The intermediate trend has been down since 27 Feb 2026. Monthly highs keep falling: 4,374 → 3,922 → 3,606 → 3,542 → 3,481.
  - From May to September the stock formed a contracting triangle with rising lows: 3,083 → 3,135 → 3,223 → 3,245 → 3,236.
  - The 2 Oct price of ¥3,211, after the BOJ's 18 Sep hike, is the first break below that rising-low line. This is a bearish signal if it holds (not confirmed by daily closes).
- **Support:** ¥3,135 (June low), then **¥3,083 (28 May low; key)**, then the ¥3,000 round number and the ¥2,994 level from Nov 2025.
- **Resistance:**
  - ¥3,223–3,245 (the broken floor, which should now act as resistance);
  - ¥3,475–3,481 (Aug/Sep highs);
  - ¥3,542–3,554 (July high, 2025 close of ¥3,546, ≈200-day estimate);
  - ¥3,606–3,655 (May high, Dec 2025 high);
  - ¥3,922 (April high);
  - ¥4,304–4,374 (March high and all-time high).

### Gaps
- Not available: RSI(14), MACD, true daily 50/100/200-day or 13/26/52-week averages, volume and trading-value trends.
- Official exchange closes for 1–2 Oct 2026 are also not verified; the ¥3,211 is from a blog.

## 4. Dividends (DPS FY2021–FY2025, FY2026 forecast, payout, policy)

### Takeaway
- **Recent DPS:** ¥95 (FY2024) → ¥105 (FY2025, the 12th consecutive increase) → **¥126 forecast for FY2026**. The FY2026 forecast was ¥122 at the start of the year and raised on 6 Aug 2026.
- **Payout:** about 30% (FY2024) → 37.1% (FY2025) → about 40% (FY2026F). Total payout including the buyback was 42.2% in FY2025.
- **Policy:** the 2025–2027 medium-term plan (16 Jan 2025) raised the payout target from "30% or more" to **40% by FY2027**. The company expects to reach it a year early.
- **Pattern:** both FY2025 and FY2026 saw mid-year dividend increases tied to profit upgrades.
- **Missing:** FY2021–FY2023 DPS were not retrieved. They rose every year but the amounts are unknown.

### Cited Findings
**DPS, JPY.** Sources are given below the table. "n/v" means not verified.

| FY (Dec) | Interim | Year-end | Annual | Payout | Notes |
|---|---|---|---|---|---|
| FY2021 | n/v | n/v | n/v | n/v | EPS ¥167.35 |
| FY2022 | n/v | n/v | n/v | n/v | EPS ¥206.15 |
| FY2023 | n/v | n/v | n/v | n/v | EPS ¥215.82 |
| FY2024 | ¥37 | ¥58 | **¥95** | ≈30.1% (calc. on EPS ¥315.49). Total payout 30.6%. | Policy at the time: "30% or more" |
| FY2025 | ¥48 | ¥57 (derived) | **¥105** (+¥10) | **37.1%** (reported). Total payout 42.2%. | Year-end forecast went from ¥49 to ¥55 on 13 Nov 2025 (annual ¥103), then to the final ¥57. 12th straight increase. |
| FY2026F | ¥61 | ¥65 (raised from ¥61 on 6 Aug 2026) | **¥126** (initial ¥122 on 12 Feb 2026) | 40.2% on initial guidance; ≈40% now | Implied EPS ≈ ¥313 |

- FY2024 and FY2025 DPS and the FY2025 staging — [f-p.jp (kabutan)](https://f-p.jp/media/?p=21023) †; [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-lifts-dividend-as-2025-profit-dips-but-outlook-strengthens) †
- FY2025 ¥105, payout 37.1%, 12th consecutive increase — [Globe and Mail / company release](https://www.theglobeandmail.com/investing/markets/stocks/TYTMF/pressreleases/201050/tokyo-tatemono-lifts-dividend-as-2025-profits-dip-but-2026-outlook-improves/) †; [FY2025 Tanshin](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf)
- 13 Nov 2025 increase: DPS +¥6 to ¥103 — [Kabutan news](https://kabutan.jp/stock/news?code=8804&b=k202511130214); [Nikkei](https://www.nikkei.com/article/DGXZQOUB132440T11C25A1000000/)
- FY2026 ¥122 (+¥17, payout 40.2%) — [Nikkei/QUICK, 12 Feb 2026](https://www.nikkei.com/article/DGXZRST0554860Q6A210C2000000/) †
- FY2026 raised to ¥126, interim ¥61 and year-end ¥65 — [Nikkei, Aug 2026](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/); [Minkabu](https://minkabu.jp/news/4589327) †
- Total payout ratios 42.2% (FY2025) and 30.6% (FY2024) — [Monex Scouter](https://scouter.monex.co.jp/report/dps/8804) †
- EPS FY2021–FY2024 — [Matsui results page](https://finance.matsui.co.jp/stock/8804/settlement/index)

**Policy**
- The 2025–2027 medium-term plan (16 Jan 2025) raised the payout target to **40% by FY2027**, from "30% or more". — [MTP PDF](https://tatemono.com/company/pdf/plan2027_250116_ja.pdf) †; [Nikkei "配当性向40%に引き上げ 新中計で27年に"](https://www.nikkei.com/article/DGXZQOUC169A00W5A110C2000000/) †
- The company expects to reach 40% in FY2026, one year early. Buybacks are "flexible", depending on share price, business environment and financial position. — [Tokyo Tatemono shareholder return policy](https://tatemono.com/ir/stock/returning.html) †; [kabureturn.jp](https://kabureturn.jp/housin/8804-h/) †
- **Forecast yield:** 3.83% at ¥3,286 on 25 Sep 2026 ([Kabutan](https://s.kabutan.jp/stocks/8804/)). That is about 3.9% at ¥3,211 (calculated).

### Inferences
- **The yield-based check confirms ¥126.** Working backwards from the 3.83% yield at ¥3,286 gives ¥125.9, which matches the company's ¥126. Implied FY2026 payout is about 40.2% on EPS of ¥313.3.
- **Policy shift.** Moving from about 30% (FY2024) to 37% (FY2025) to 40% (FY2026F) is the clearest capital-return change of the period. DPS has risen 33% over two years (¥95 → ¥126), faster than EPS.
- **Progressive in practice.** Twelve consecutive increases through FY2025 imply that DPS rose every year from FY2014 (inference). No formal "progressive dividend" or DOE commitment was found.
- **No special dividends.** No special or commemorative dividends were found for FY2021–FY2026.

### Gaps
- **FY2021–FY2023 DPS** (interim, year-end, annual) and payouts were not found. Irbank, the company IR dividend page and the Yuho were all blocked.
- **Background, not verified:** under the "30% or more" policy, FY2021–FY2023 payouts were probably about 30–35%. That would put DPS at roughly ¥50, ¥62 and ¥65–76 respectively. These are **estimates** and must not be presented as actuals.
- **Not found:** record and payment dates; whether a DOE floor or progressive-dividend language exists.

## 5. Buybacks, treasury shares, cancellations and dilution (FY2021–FY2026)

### Takeaway
One buyback programme is verified for 2021–2026:
- authorised for up to 1.5m shares (0.72%) and up to ¥3.0bn, from 13 Feb to 31 Aug 2025;
- executed by open-market purchases on the TSE;
- completed at **1,189,100 shares for ¥2,999,870,100** (average ¥2,523).

These shares were then **cancelled**. Issued shares fell from 209,167,674 to **207,978,574** (−0.57%); the cancellation was considered at the 13 Nov 2025 board meeting. At 31 Dec 2025 the company held **839,526 treasury shares**, and the stock-compensation trust (BBT) held 351,300 shares. FY2024 saw only about ¥0.34bn of repurchases (derived). No FY2026 programme, splits or dilutive issues were found.

### Cited Findings
| Item | Date | Detail | Source |
|---|---|---|---|
| Authorisation | 25 Dec 2024 (per FilingReader/TipRanks; a parallel workstream flags the date as unconfirmed) | Up to 1,500,000 shares (0.72% of outstanding) and up to ¥3.0bn; period 13 Feb–31 Aug 2025 | [FilingReader](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares); [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-announces-share-repurchase-status-2) |
| Method | Throughout | Purchases on the Tokyo Stock Exchange (open market) | [FilingReader](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares) |
| Execution | Mar 2025 | 176,400 shares, ¥432,417,100 | [FilingReader](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares) |
| Execution | May 2025 | 167,300 shares, ¥428,360,750 | [FilingReader](https://filingreader.com/news-wire/tokyo/2025-06-02/tokyo-tatemono-continues-share-repurchase-program-in-may-2025) |
| Execution | To 31 May 2025 | 728,600 shares, ¥1,798,238,350 | [FilingReader](https://filingreader.com/news-wire/tokyo/2025-06-02/tokyo-tatemono-continues-share-repurchase-program-in-may-2025) |
| **Final** | 13 Feb–31 Aug 2025 | **1,189,100 shares, ¥2,999,870,100** | [Convocation notice, Proposal 1 (srdb)](https://s.srdb.jp/8804/content-1-1.html) † |
| Cancellation decision | 13 Nov 2025 board | Board met to consider forecast and dividend revisions and cancellation of treasury shares (自己株式の消却) | [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-announces-share-repurchase-status-2); [Simply Wall St](https://simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares/news/why-tokyo-tatemono-tse8804-is-up-134-after-reviewing-dividen) |
| Issued and treasury shares | 31 Dec 2025 | Issued 207,978,574; outstanding excluding treasury 207,139,048; BBT 351,300 | [j-lic.com](https://j-lic.com/companies/8804) † |
| FY2025 vs FY2024 | FY totals | FY2025 buyback ¥3.0bn, "+773%" vs FY2024; total payout 42.2% (FY2025) vs 30.6% (FY2024) | [Monex Scouter](https://scouter.monex.co.jp/report/dps/8804) † |
| FY2026 | To Oct 2026 | No new buyback programme found (may exist but not captured) | Parallel notes † |

### Inferences
- **How the programme ran (calculated).**
  - Average prices: ¥2,451 in March, ¥2,560 in May, ¥2,523 for the whole programme.
  - The ¥3.0bn amount cap was **99.996%** used, against **79.3%** of the share cap. The yen limit was the binding one.
  - February plus April purchases: 384,900 shares for ¥937.5m (average ¥2,436).
- **Cancellation size (derived).** 207,978,574 + 1,189,100 = **209,167,674**, the pre-cancellation issued count. This strongly suggests exactly the 1,189,100 repurchased shares were cancelled, **0.57%** of pre-cancellation issued shares. The cancellation would fall between 13 Nov and 31 Dec 2025.
- **Treasury after cancellation.** The 839,526 treasury shares at end-2025 are a residual pool, about 0.40% of issued shares. They are probably legacy and odd-lot purchases (inference).
- **FY2024 repurchases.** FY2025's "+773%" implies about ¥0.34bn of repurchases in FY2024. That is consistent with odd-lot or minor purchases rather than a formal programme (inference).
- **Scale.** ¥3bn was about 0.6% of market cap at 2025 prices (about ¥2,500 × 209m ≈ ¥520bn). Capital return is dividend-led.
- **Dilution.** The BBT buys existing shares, so it does not issue new ones (inference from general structure). No equity issuance or convertible bonds were found.

### Gaps
- **Not verified:**
  - buyback authorisations in FY2021–FY2023 and in 2026, including whether anything accompanied the 12 Feb 2026 results;
  - the formal cancellation date, the exact share number and the TDnet notice;
  - treasury shares at year-ends FY2021–FY2024;
  - BBT share counts before 2025 and when the BBT was set up;
  - convertible bonds or new-share issuance;
  - the 25 Dec 2024 authorisation date (a mid-Feb 2025 resolution would be more usual).
- **No evidence of any stock split during 2021–2026 was found.** The Nikkei annual series shows no discontinuity.

## 6. Total shareholder return over 1, 3 and 5 years vs TOPIX and peers

### Takeaway
Price returns from the verified data:

| Period | Price return | CAGR |
|---|---|---|
| End-2020 → end-2025 (5 calendar years) | **+150.6%** | 20.2% |
| End-2022 → end-2025 (3 calendar years) | **+121.8%** | 30.4% |
| CY2025 | **+36.0%** | n/a |

Dividend-inclusive TSR (ex-date basis, no reinvestment) can be computed for:
- **CY2024: +27.9%**
- **CY2025: +40.0%**
- **2026 YTD to 2 Oct: −7.7%**

ESTIMATES for longer periods, which need assumed FY2021–23 DPS, are about **+144–145% over 3 years** and **+195–196% over 5 years** (≈24% a year). The 1-year TSR to 2 Oct 2026 is roughly +8–13% (estimate). There is no verified comparison with TOPIX or peers.

### Cited Findings
- **Year-end closes:** 2020 ¥1,415; 2021 ¥1,680; 2022 ¥1,599; 2023 ¥2,112; 2024 ¥2,607; 2025 ¥3,546. — [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)
- **Latest price:** ¥3,211 on 2 Oct 2026. — [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) †
- **DPS:** FY2024 ¥95; FY2025 ¥105; FY2026 interim ¥61. — [f-p.jp](https://f-p.jp/media/?p=21023) †; [Minkabu](https://minkabu.jp/news/4589327) †
- **2026 drawdowns from Feb–Mar highs:** 8804 −26.6%, Mitsubishi Estate −34.1%, Mitsui Fudosan −33.6%, Sumitomo Realty −42.2%. — [kabu.tagu-blog.com](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026/) †
- **Undated aggregator returns** (1-yr +21.0%, 3-yr +65.23%, 5-yr +129.79%) are internally inconsistent. **Do not use.** — [Simply Wall St](https://www.simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares)

### Inferences
**TSR by year, calculated.** Year-end dividends have their ex-date in late December, so each calendar year receives that fiscal year's DPS.

| Period | Price | TSR |
|---|---|---|
| CY2024 | +23.4% | (2,607+95)/2,112 → **+27.9%** |
| CY2025 | +36.0% | (3,546+105)/2,607 → **+40.0%** |
| 2 yrs (end-2023 → end-2025) | +67.9% | **+79.2%** |
| 2026 YTD to 18 Sep | −8.7% | +¥61 interim → **−7.0%** |
| 2026 YTD to 2 Oct | −9.4% | **−7.7%** |

**ESTIMATES for 3- and 5-year TSR.** These assume ~30% payout for FY2021–22 (DPS ≈ ¥50, ¥62) and 30–35% for FY2023 (¥65–76), consistent with the "30% or more" policy and FY2024's actual ≈30%.

| Window | Estimated TSR |
|---|---|
| 3 yrs (end-2022 → end-2025) | **≈ +144% to +145%** |
| 5 yrs (end-2020 → end-2025) | **≈ +195% to +196%** (≈24.1% p.a.), against +150.6% price-only |

- **1-year TSR to 2 Oct 2026 (ESTIMATE).** This assumes a 2 Oct 2025 base of ¥2,950–3,074, anchored on the 7 Oct 2025 high (¥3,074) and the 13 Nov 2025 close (¥2,994). Price return is +4.5% to +8.8%. Adding dividends of ¥118 (¥57 year-end + ¥61 interim) gives TSR of **about +8% to +13%**.
- **Against peers, 2026 only.** 8804's 2026 drawdown was 7–16 points shallower than Mitsui, Mitsubishi or Sumitomo, and its yield is higher. In 2026 it has outperformed those three peers on both price and TSR (inference from the blog figures).

### Gaps
- **No verified relative performance.** No verified TOPIX, TOPIX Real Estate or peer price/TSR series was obtained.
- **For reference only (UNVERIFIED background; must be checked before use):**
  - TOPIX year-end closes were about 1,804.68 (2020), 1,992.33 (2021), 1,891.71 (2022), 2,366.39 (2023) and 2,784.92 (2024).
  - On those numbers, from end-2020 to end-2024 8804's price rose +84.2% against TOPIX's +54.3%.
  - TOPIX's end-2025 and Oct-2026 levels are unknown.
- **Official TSR table not read.** The Yuho's 5-year table (株主総利回り vs TOPIX dividend-inclusive) is in the FY2025 Yuho filed on 23 Mar 2026. The Yuho was blocked.

## 7. Short interest: JPX ≥0.5% short positions, margin balances, securities lending

### Takeaway
No short-position disclosures, margin balances or lending data could be retrieved. Karauri.net, JPX, kabutan and irbank were blocked, and the search budget ran out.

What is verified:
- 8804 is a 貸借銘柄, so it can be shorted on margin;
- Japan Securities Finance (JSF) is a top-5 holder of record at 2.29% (31 Dec 2025) → 2.17% (30 Jun 2026). This reflects margin-trading collateral, not short interest;
- all ≥5% large-holding filers are passive or institutional managers: BlackRock 6.42% (Dec 2025), Sumitomo Mitsui Trust AM 5.07% (Apr 2026) and Nomura AM;
- no activist and no short-seller report was found.

### Cited Findings
- 8804 is listed as 東証プライム 売建可 (margin short-selling allowed) and as a 貸借銘柄. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [kabuyutai](https://www.kabuyutai.com/kobetu/tatemono.html)
- Japan Securities Finance holds 2.29% (31 Dec 2025, Yuho) and 2.17% (30 Jun 2026; rank 4 in the top 10). — [irbank holders](https://irbank.net/E03859/holder) †; [Yahoo! Finance Japan profile](https://finance.yahoo.co.jp/quote/8804.T/profile) †
- **Large-holding reports:**
  - BlackRock Japan and joint holders: 7.28% → 6.42% (change report filed 3 Dec 2025). — [Kabutan](https://kabutan.jp/news/marketnews/?b=n202512030954) †; [MAonline](https://maonline.jp/kabuhoyu/sh-s100x80j) †
  - Sumitomo Mitsui Trust AM: crossed 5% at 5.10% (8 May 2025), then 5.12% → 5.07% (21 Apr 2026). — [MAonline via docomo](https://topics.smt.docomo.ne.jp/article/maonline/business/maonline-sh-s100vp67) †; [Kabutan](https://kabutan.jp/news/marketnews/?b=n202604210334) †
  - Nomura AM: several change reports, percentages unverified. — [MAonline S100PDT6](https://maonline.jp/kabuhoyu/sh-s100pdt6) †
  - Further filers listed on MAonline with no dates visible: Société Générale Securities ([MAonline](https://maonline.jp/kabuhoyu/sh-s100qevb)), Mitsubishi UFJ Trust ([MAonline](https://maonline.jp/kabuhoyu/sh-s100qbix)), SMBC Nikko ([MAonline](https://maonline.jp/kabuhoyu/sh-s100pxi6)) and Fidelity ([MAonline](https://maonline.jp/kabuhoyu/sh-s1003owh)).
- **No activist or short report.** No activist ≥5% filing and no short-seller report were found. — management notes †; nav notes †

### Inferences
- **JSF's holding is not short interest.** JSF's registered stake (about 4.7m → 4.5m shares, estimated from the percentages) is collateral from 貸借取引 margin financing. It is a rough signal of margin-long positions financed through JSF, and the decline suggests slightly lower margin longs by mid-2026 (inference). It says nothing directly about short positions.
- **Securities-house filings.** SocGen Securities, Nomura Securities and SMBC Nikko file large-holding reports because of securities lending, hedging or inventory. Without the filings, none can be called a directional short or long.
- **No short-seller narrative.** The decline from February to October 2026 is explained by sector rates and is in line with or better than peers. No stock-specific short thesis appeared in the sources found.

### Gaps
- **Not available:**
  - JPX short-position reports for holders of ≥0.5% (names, dates, %), and the trend over time (karauri.net/8804, JPX 空売りの残高に関する情報);
  - weekly margin balances (信用買残, 信用売残, 信用倍率);
  - JSF lending balances (貸借取引残高) and reverse-repo fees (逆日歩);
  - the overall short ratio.
- **Unclear filings:** dates and percentages of the SocGen, MUFG Trust and SMBC Nikko filings.
- **For the report:** short interest should be described as "not verified". Once network access to those hosts is restored, the writer should pull karauri.net and the JPX daily file.
