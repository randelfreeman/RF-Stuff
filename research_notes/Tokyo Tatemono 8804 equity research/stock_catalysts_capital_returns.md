# Tokyo Tatemono (8804 JP): share-price history, catalysts behind moves of more than 10%, technicals, dividends, buybacks/treasury shares and short interest (Oct 2021 to Oct 2026)

*Compiled 4 Oct 2026. All money in JPY; TSE Prime prices. **How the data was gathered:** this environment's network egress policy blocked every programmatic and primary source, for both curl and page fetches: Yahoo Finance chart API, stooq CSV, kabutan, karauri.net, irbank, JPX, TDnet, EDINET, tatemono.com, minkabu, Matsui, stockanalysis and others. The session's shared web-search budget (200 searches) also ran out partway through this task. Every figure below therefore comes from a **search-engine extraction of the cited page**. The pages themselves were never opened. Where several independent pages agree, that is noted. Companion dataset: `stock_prices_8804.csv` in this folder. It contains annual OHLC for 2017–2026 YTD, monthly OHLC for Jan–Sep 2026 and dated price points. Nothing in it is interpolated.*

## 1. Price data: latest close, 52-week/all-time range, annual OHLC 2020–2026 YTD, market cap, share count, liquidity, chart dataset

### Takeaway
The latest verified close is **¥3,236 on Fri 18 Sep 2026**. Kabutan showed ¥3,286 intraday on 25 Sep 2026, which implies a previous close of ¥3,293. At that point market cap was **¥683.4bn** on **207.978m issued shares**. The stock is about **26% below its all-time high of ¥4,374, set on 27 Feb 2026**, and 5% above its 2026 low of ¥3,083 (28 May 2026). Calendar-year price returns were −4.8% (2022), +32.1% (2023), +23.4% (2024) and +36.0% (2025), and 2026 is −8.7% YTD. Month-end closes before Jan 2026 could not be retrieved.

### Cited Findings
**Latest price points (most recent first)**
- 1 Oct 2026 close of ¥3,255 is **UNVERIFIED**. A search-engine summary said "10月1日の終値は3,255.0円", but neither the year nor the page could be attributed. Do not use it as the latest close without checking. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) (one of the pages listed)
- 25 Sep 2026, 11:18 JST: ¥3,286, −¥7 (−0.21%). PER 10.5x, PBR 1.12x, forecast dividend yield 3.83%. — [Kabutan quote](https://s.kabutan.jp/stocks/8804/)
- 18 Sep 2026: close ¥3,236. This is both the latest data point in Nikkei's annual table ("2026 data as of 18 Sep") and the close of kabutan's partial September bar. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)
- 24 Jul 2026: ¥3,427. — [Matsui Securities quote](https://finance.matsui.co.jp/stock/8804/index); [minkabu](https://minkabu.jp/stock/8804)

**Market cap and share count**
- Market cap was ¥712.7bn on 24 Jul 2026 and ¥683.4bn on 25 Sep 2026. The search summary printed these as "7,127 / 6,834 billion yen", which means 7,127億円 and 6,834億円. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Kabutan](https://s.kabutan.jp/stocks/8804/); [kabuyoho](https://kabuyoho.jp/report?bcode=8804)
- Issued shares (発行済株式数): 207,978 thousand. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Kabutan](https://s.kabutan.jp/stocks/8804/); [minkabu](https://minkabu.jp/stock/8804)
- The FY2025 annual securities report (第208期, 1 Jan–31 Dec 2025) was filed on 23 Mar 2026. It is the primary source for treasury shares, the TSR table and annual highs/lows. — [Nikkei Yuho page](https://www.nikkei.com/nkd/company/ednr/?scode=8804)

**All-time and 52-week range**
- All-time high (上場来高値) ¥4,374.0 on 27 Feb 2026. All-time low ¥388.0 on 13 Mar 2009. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [minkabu](https://minkabu.jp/stock/8804)
- 2026 YTD high ¥4,374.0 (27 Feb 2026) and low ¥3,083.0 (28 May 2026). — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [Matsui](https://finance.matsui.co.jp/stock/8804/index)
- Nikkei's table confirms ¥4,374 as the highest price in the 10-year window and ties 4,374 to 27 Feb 2026. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)

**Annual OHLC, JPY.** Source: [Nikkei 10-yr price history](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804). Kabutan's yearly and monthly pages agree on 2025–2026. The "Close-to-close" column is my calculation.

| Year | Open | High | Low | Close | Close-to-close |
|---|---|---|---|---|---|
| 2019 | 1,101 | 1,740 | 1,078 | 1,709 | +49.9% |
| 2020 | 1,705 | 1,828 | 904 | 1,415 | −17.2% |
| 2021 | 1,415 | 1,852 | 1,367 | 1,680 | +18.7% |
| 2022 | 1,692 | 2,190 | 1,569 | 1,599 | −4.8% |
| 2023 | 1,590 | 2,191 | 1,484 | 2,112 | +32.1% |
| 2024 | 2,097 (4 Jan) | 2,774 | 2,029 | 2,607 (30 Dec) | +23.4% |
| 2025 | 2,594 (6 Jan) | 3,655 (26 Dec) | 2,237.5 (7 Apr) | 3,546 (30 Dec) | +36.0% |
| 2026 YTD (to 18 Sep) | 3,552 | 4,374 (27 Feb) | 3,083 (28 May) | 3,236 (18 Sep) | −8.7% |

- The dates shown in brackets for 2024 and 2025 come from the source. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)
- Nikkei also lists 2017 (1,583 / 1,653 / 1,305 / 1,522) and 2018 (1,522 / 1,858 / 1,061 / 1,140). — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)

**Monthly OHLC for 2026, JPY.** Source: [Kabutan monthly bars](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/), also at [kabutan.jp ashi=mon](https://kabutan.jp/stock/kabuka?code=8804&ashi=mon). The m/m column is my calculation.

| Month | Open | High | Low | Close | m/m |
|---|---|---|---|---|---|
| Dec 2025 | n/a | n/a | n/a | 3,546 | n/a |
| Jan 2026 | 3,552 | 3,777 | 3,501 | 3,629 | +2.3% |
| Feb 2026 | 3,689 | 4,374 | 3,603 | 4,374 | **+20.5%** |
| Mar 2026 | 4,234 | 4,304 | 3,462 | 3,587 | **−18.0%** |
| Apr 2026 | 3,698 | 3,922 | 3,523 | 3,599 | +0.3% |
| May 2026 | 3,573 | 3,606 | 3,083 | 3,269 | −9.2% |
| Jun 2026 | 3,350 | 3,448 | 3,135 | 3,296 | +0.8% |
| Jul 2026 | 3,300 | 3,542 | 3,223 | 3,387 | +2.8% |
| Aug 2026 | 3,340 | 3,475 | 3,245 | 3,445 | +1.7% |
| Sep 2026 (to 18 Sep only) | 3,424 | 3,481 | 3,236 | 3,236 | −6.1% (source: −¥209) |

**EPS and an undated snapshot**
- Actual EPS: FY2021 ¥167.35, FY2022 ¥206.15, FY2023 ¥215.82, FY2024 ¥315.49. — [Matsui results page](https://finance.matsui.co.jp/stock/8804/settlement/index); [FISCO](https://web.fisco.jp/platform/companies/0880400)
- An undated aggregator snapshot, of low reliability, shows: price ¥3,688; 52-week range ¥2,237.50–¥4,374.00; 1-yr +21.0%; 3-yr +65.23%; 5-yr +129.79%. — [Simply Wall St](https://www.simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares); [TipRanks](https://www.tipranks.com/stocks/jp:8804)

### Inferences
- **Market cap cross-check.** Price × 207.978m shares reproduces both reported market caps: ¥3,427 gives ¥712.7bn and ¥3,286 gives ¥683.4bn. So the 207.978m share count is the one in current use. On the same share count:
  - at the all-time high (¥4,374) market cap was about ¥909.7bn;
  - at the 18 Sep close (¥3,236) it was about ¥673.0bn.
- **Implied 24 Sep close.** Kabutan's 25 Sep quote (¥3,286, −¥7) implies a 24 Sep 2026 close of ¥3,293. This is derived, not reported.
- **Cross-source consistency.** The Nikkei and kabutan figures agree with each other:
  - 2026 open 3,552 matches the Jan open;
  - the YTD high and low match the Feb high and May low;
  - Dec 2025 close 3,546 matches the Jan 2026 open of 3,552.

  This makes the annual and 2026 monthly series reasonably reliable even though the pages were never opened.
- **Annual swings measured from the prior year-end close.** These are useful for spotting moves of more than 10% when daily data is missing.

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
- **2025 was a re-rating year (estimate).** FY2025 net profit fell 10.6% (see Q4), so FY2025 EPS was roughly ¥282. On that basis the price rose 36% while EPS fell, putting the end-2025 P/E at about 12.6x. Both numbers are estimates.
- **The undated snapshot does not hold together.** Its 52-week low (¥2,237.5 on 7 Apr 2025) means it was taken no later than 7 Apr 2026. But its "1-yr +21%" implies a year-earlier price near ¥3,050, while March–May 2025 buyback prices averaged about ¥2,450–2,560 (Q5). It is not used anywhere else in these notes.
- **What the CSV contains.** `stock_prices_8804.csv` has columns `date, period, frequency, open, high, low, close, price_type, source_url, notes` and covers:
  - annual rows for 2017–2025 plus 2026 YTD;
  - monthly bars for Jan–Aug 2026 plus a partial September bar;
  - dated points: 7 Apr 2025 low, 26 Dec 2025 high, 24 Jul, 24 Sep (derived) and 25 Sep 2026, and 1 Oct 2026 (flagged unverified);
  - two "reference" rows giving average buyback prices for Mar and May 2025 as stand-ins for those months' price levels. These are **not** closes.

  Month-end dates are the last TSE trading day of each month, which I inferred from the calendar.

### Gaps
- **Month-end closes Oct 2021–Dec 2025 (51 months) are missing.** The planned sources (Yahoo `query1.finance.yahoo.com`, `stooq.com`, kabutan monthly pages 2 onwards, investing.com) were all blocked by the egress proxy, and search snippets only exposed 2026. No TOPIX or TOPIX Real Estate series and no peer series (8801, 8802, 8830) could be obtained either.
- **The true 52-week low (early Oct 2025 to early Oct 2026) is unknown.** The 2026 YTD low of ¥3,083 is only an upper bound, because Oct–Nov 2025 prices may have been lower.
- **The latest close (2 Oct 2026) and the month-end close for Sep 2026 could not be verified.**
- **Not found:** average daily trading volume or value, treasury share count, and dates of the annual highs and lows for 2021–2024.
- **What would unblock this.** If the environment's network access is widened, the obvious first fetches are:
  - `query1.finance.yahoo.com`, `stooq.com`, `kabutan.jp`, `karauri.net`, `irbank.net`, `jpx.co.jp`, `release.tdnet.info`, `disclosure2.edinet-fsa.go.jp`, `tatemono.com`;
  - the FY2025 Yuho (自己株式の状況, 株主総利回り table, 最高・最低株価).

## 2. Moves of more than 10% (Oct 2021 to Oct 2026) and their causes

### Takeaway
Windows of more than 10% can be dated reliably only for 2025–2026:
- the April 2025 tariff-shock low and the rebound after it;
- a roughly +13% move after the 13 Nov 2025 guidance and dividend upgrade;
- a **+20.5% surge in Feb 2026 to the all-time high** after FY2025 results, amid a "real-estate boom";
- a **−20.9% fall from the 27 Feb peak to the March low**, which hit the whole sector as 10-year JGB yields rose and was macro-driven;
- a further slide to ¥3,083 on 28 May 2026 (−29.5% peak to trough, cause not found);
- a +14.9% rebound into July.

For 2022–2024 the annual ranges show large swings: from the 2022 high to the 2023 low the stock fell 32%. Without daily data, though, those swings cannot be tied to particular BOJ dates or compared with peers.

### Cited Findings
**Windows of more than 10%.** Percentages are calculated from the cited prices.

| # | Window | Move | Evidence | Reported or likely cause | Stock-specific vs market |
|---|---|---|---|---|---|
| 1 | 2022 high (date n/a) → 30 Dec 2022 close, extending to the 2023 low (date n/a) | ¥2,190 → ¥1,599 (**−27.0%**); → ¥1,484 (**−32.2%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified. The 2022 close sits 1.9% above the 2022 low, which fits a late-2022 slump such as the BOJ YCC widening on 20 Dec 2022 (inference). | Probably macro/sector (inference) |
| 2 | 2023 low → 2023 high (dates n/a) | ¥1,484 → ¥2,191 (**+47.6%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified | n/a |
| 3 | 2024 low → 2024 high (dates n/a) | ¥2,029 → ¥2,774 (**+36.7%**) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not verified. 2024's low was only 3.9% below the end-2023 close. | n/a |
| 4 | 6 Jan 2025 open → 7 Apr 2025 low | ¥2,594 → ¥2,237.5 (**−13.7%**). Measured from the March-2025 average buyback price of ¥2,451 it is only −8.7%. | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804); [FilingReader Mar-25](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares) | The low fell on 7 Apr 2025, the day of the global sell-off after the US tariff announcement (macro date not independently verified here) | Market-wide |
| 5 | 7 Apr 2025 → May 2025 | ¥2,237.5 → about ¥2,560 (May-2025 average buyback price) (**≈ +14%**) | [FilingReader May-25](https://filingreader.com/news-wire/tokyo/2025-06-02/tokyo-tatemono-continues-share-repurchase-program-in-may-2025) | Post-shock rebound, with the company's buyback active (see #6) | Market-wide plus support from the buyback |
| 6 | 7 Apr 2025 → 26 Dec 2025 | ¥2,237.5 → ¥3,655 (**+63.4%** over about 8.5 months) | [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Buyback ran 13 Feb–31 Aug 2025. On 13 Nov 2025 the company raised its recurring-profit forecast by 6% (record), raised the dividend by ¥6 and considered cancelling shares ([Kabutan news 13 Nov 2025](https://kabutan.jp/stock/news?code=8804&b=k202511130214); [Nikkei](https://www.nikkei.com/article/DGXZQOUB132440T11C25A1000000/)) | Mixed |
| 7 | Probably mid-Nov 2025 (window not visible) | **+13.4%** per the headline "Why Tokyo Tatemono (TSE:8804) Is Up 13.4% After Reviewing Dividend…" | [Simply Wall St](https://simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares/news/why-tokyo-tatemono-tse8804-is-up-134-after-reviewing-dividen) | Dividend review. Very likely the 13 Nov 2025 upgrade (inference; article date not visible) | Stock-specific |
| 8 | 30 Jan 2026 close → 27 Feb 2026 close; February low → 27 Feb | ¥3,629 → ¥4,374 (**+20.5%**); ¥3,603 → ¥4,374 (**+21.4%**). Closed the month at the all-time high. | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | FY2025 results on 12 Feb 2026: operating profit +20.2%, net profit −10.6% ([japanir](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/); [Tanshin PDF](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf)). Nikkei Veritas (28 Feb): shares surged "riding the real-estate boom" ([Nikkei company page](https://www.nikkei.com/nkd/company/?scode=8804)). The 51-storey TOFROM YAESU TOWER (about 230k m²) was completed in Feb 2026 ([offisite](https://offisite.jp/discovers/view/39)). | Mixed: results plus sector boom |
| 9 | 27 Feb 2026 → March 2026 low (date n/a) | ¥4,374 → ¥3,462 (**−20.9%**); March month −18.0% | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | Sector sell-off as the 10-yr JGB yield rose from 2.132% (27 Feb) to 2.366% (31 Mar) on oil-driven inflation worries. Mitsui Fudosan and Mitsubishi Estate fell sharply again on 23 Mar 2026. Tokyo Tatemono "fell with the sector". ([PayPay Securities media, 24 Mar 2026](https://media.paypay-sec.co.jp/cat5/jisha260324); [Nomura WealthStyle](https://www.nomura.co.jp/wealthstyle/article/0728/); [kabu.tagu-blog](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026)) | **Sector/macro (rates)** |
| 10 | March low → April high (dates n/a) | ¥3,462 → ¥3,922 (**+13.3%**) | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | Not found | n/a |
| 11 | April high → 28 May 2026 low; 27 Feb → 28 May | ¥3,922 → ¥3,083 (**−21.4%**); peak to trough **−29.5%** | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/); [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804) | Not found | n/a |
| 12 | 28 May → July high (date n/a) | ¥3,083 → ¥3,542 (**+14.9%**) | [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/) | Not found. The 6 Aug upgrade (below) came after this rebound. | n/a |

**Other catalysts, with no move magnitude available or no move of more than 10%**
- **New medium-term plan disappointed (date not confirmed).** Nikkei ran the headline "東京建物の株価大幅反落 新中計に「物足りない」の見方も": the shares fell back sharply as the new medium-term plan was seen as underwhelming. — [Nikkei](https://www.nikkei.com/article/DGXZQOFL171HB0X10C25A1000000/)
- **6 Aug 2026 Q2 results.**
  - FY2026 net-profit forecast raised to +10% y/y; annual dividend raised by ¥4. — [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/)
  - Kabutan describes a 4% upward revision to recurring profit, a record. — [Kabutan](https://s.kabutan.jp/stocks/8804/); [Q2 highlights PDF](https://pdf.irpocket.com/C8804/xoA3/ieAo/gkiS/BBY6.pdf)
  - August closed only +1.7% m/m. — [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)
- **2 Jun 2026: Star Mica stake.** Tokyo Tatemono filed a large-holding report showing **13.74% of Star Mica Holdings (2975)**, held for a capital and business alliance. — [Matsui news](https://finance.matsui.co.jp/news/582338/index); [MAonline](https://maonline.jp/kabuhoyu/sh-s100y6e2)
- **Sector worry in March 2026.** Commentators worried about a repeat of the August 2024 "Ueda shock". — [PayPay Securities media](https://media.paypay-sec.co.jp/cat5/jisha260324); [Nomura WealthStyle](https://www.nomura.co.jp/wealthstyle/article/0728/)
- **Inconsistent drawdown figure.** One secondary page says the stock fell 26.6% from the 27 Feb high, which implies about ¥3,210. The March low was ¥3,462, so this must refer to a later, unknown date, probably June 2026 (range ¥3,135–3,448). — [nikkeiyosoku](https://nikkeiyosoku.com/stock/crash/8804/); [kabu.tagu-blog](https://kabu.tagu-blog.com/real-estate-stocks-7-rates-2026)
- **No activist stake found.** A search for activist stakes found Elliott, Oasis and others in other Japanese companies, but none in Tokyo Tatemono. — [itiger/Bloomberg summary](https://www.itiger.com/news/2492267336)

### Inferences
- **Feb–May 2026 round trip.** The stock rose 20% in February to an all-time high and then gave back about 30% by late May. Sources tie the March leg explicitly to sector-wide rate fears. The February leg had both stock-specific triggers (FY2025 results, a flagship completion) and a sector tailwind. Without peer data the split between them cannot be measured.
- **2025 rally.** The 2025 gain (+63% from the April low) combined three things:
  - the market recovery after the tariff shock;
  - support from the buyback (about ¥3bn, around 0.6% of market cap);
  - the November upgrade to guidance and dividend, plus share cancellation.

  Simply Wall St's +13.4% is the only stock-specific move of more than 10% in 2025 for which a magnitude is cited.
- **Pre-2025 swings.** The 2022–2024 moves of more than 10% (#1–#3) are real, since the annual high and low gaps are 37–48%. The year-end close sitting near the 2022 low points to the decline continuing into late December 2022, consistent with the 20 Dec 2022 YCC shock. That attribution is inference only.
- **Q2 2026 results.** The Aug 2026 upgrade (net profit +10%, dividend +¥4) did not cause a move of more than 10% (August +1.7%). The market looks focused on rates rather than earnings revisions.

### Gaps
- **No daily data.** Without it, the largest single-day moves cannot be computed, and the 2022–2024 highs and lows cannot be matched to BOJ events. In particular, the reaction to these events was not quantified: 20 Dec 2022 YCC widening; 19 Mar 2024 end of negative rates; 31 Jul 2024 hike to 0.25%; the 5 Aug 2024 crash and 6 Aug 2024 rebound; the 24 Jan 2025 hike.
- **These macro dates are background knowledge, not verified in this session.** The writer should confirm them before publishing.
- **Peer comparison is missing.** No move data was found for Mitsui Fudosan (8801), Mitsubishi Estate (8802) or Sumitomo Realty (8830), so the "stock-specific vs sector" calls rest only on the qualitative sector reports cited for March 2026.
- **The date and size of the "new medium-term plan disappointment" move were not found.** The Nikkei article ID contains "17…C25", which hints at the 17th of a month in 2025, but this is low-confidence.
- **Causes not found:**
  - the Apr–May 2026 slide to ¥3,083;
  - the May–Jul 2026 rebound;
  - September 2026's −6.1%;
  - whether a BOJ policy change in 2025–2026 coincided with any of these.
- **Not found:**
  - index inclusion or exclusion events (MSCI or TOPIX weightings);
  - large property-sale announcements with price reactions. FY2025 gains on property sales are mentioned only in passing in the results coverage.

## 3. Technical snapshot (as of 18–25 Sep 2026)

### Takeaway
At ¥3,236–3,286 the stock trades below all estimated moving averages:
- about 2–4% below the roughly 50- and 100-day levels (≈¥3,360–3,370);
- about 7.5–9% below the roughly 200-day level (≈¥3,550).

It is 25–26% below the 52-week and all-time high (¥4,374) and only 5–7% above the YTD low (¥3,083). Since the February peak the trend has made lower highs. Since June, however, it has traded in a ¥3,135–3,542 range with rising lows, so it is consolidating rather than breaking down. Kabuyoho's trend signal reads "sell continuation".

### Cited Findings
- Prices: ¥3,236 close on 18 Sep 2026 ([Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)); ¥3,286 intraday on 25 Sep 2026 ([Kabutan](https://s.kabutan.jp/stocks/8804/)).
- 52-week and all-time high ¥4,374 (27 Feb 2026); 2026 low ¥3,083 (28 May 2026). — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Nikkei](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)
- Monthly ranges since June 2026 (low – high):

  | Month | Range |
  |---|---|
  | Jun | ¥3,135–3,448 |
  | Jul | ¥3,223–3,542 |
  | Aug | ¥3,245–3,475 |
  | Sep (to 18 Sep) | ¥3,236–3,481 |

  September closed at its low (¥3,236). — [Kabutan monthly](https://s.kabutan.jp/stocks/8804/historical_prices/monthly/)
- Kabuyoho's technical trend signal (crawled around Sep 2026): 売り継続 ("sell continuation"). — [kabuyoho trend signal](https://kabuyoho.jp/reportTrendSignal?bcode=8804); [kabuyoho chart](https://kabuyoho.jp/reportChart?bcode=8804)
- Valuation on 25 Sep 2026: PER 10.5x, PBR 1.12x, forecast yield 3.83%. — [Kabutan](https://s.kabutan.jp/stocks/8804/)

### Inferences
**Estimated moving averages (all ESTIMATES).** Each is a trading-day-weighted average of monthly mid-ranges ((high+low)/2) from the kabutan bars, because daily closes were unavailable. Expect roughly ±2–3% error. The "vs" columns show where the price stands relative to each average.

| Proxy | Estimate | vs ¥3,236 (18 Sep) | vs ¥3,286 (25 Sep) |
|---|---|---|---|
| ~50-day | ≈ ¥3,367 | −3.9% | −2.4% |
| ~100-day | ≈ ¥3,359 | −3.7% | −2.2% |
| ~200-day | ≈ ¥3,554 (mean of 10 month-end closes Dec 2025–Sep 2026 = ¥3,537) | −8.9% | −7.5% |
| 52-week high ¥4,374 | n/a | −26.0% | −24.9% |
| 2026 low ¥3,083 | n/a | +5.0% | +6.6% |

- **Moving-average alignment is bearish.** The short averages (≈¥3,360) sit below the long one (≈¥3,550), a death-cross-type set-up, and the price is below all of them. This is consistent with Kabuyoho's "sell" signal.
- **Trend has two layers.**
  - The primary, multi-year uptrend is intact: annual lows keep rising (¥1,484 in 2023, ¥2,029 in 2024, ¥2,237.5 in 2025, ¥3,083 in 2026).
  - The intermediate trend has been down since 27 Feb 2026. Monthly highs keep falling (4,374 → 3,922 → 3,606 → 3,542 → 3,481), while lows have risen since May (3,083 → 3,135 → 3,223 → 3,245 → 3,236). That is a contracting range, a triangle, in roughly ¥3,135–3,542.
- **Support:** ¥3,223–3,245 (Jul/Aug lows and the 18 Sep close), then ¥3,135 (June low), then **¥3,083 (28 May low; key)**, then the ¥3,000 round number.
- **Resistance:**
  - ¥3,475–3,481 (Aug/Sep highs);
  - ¥3,542–3,554 (July high, 2025 close of ¥3,546, ≈200-day estimate);
  - ¥3,606–3,655 (May high and Dec 2025 high);
  - ¥3,922 (April high);
  - ¥4,304–4,374 (March high and all-time high).
- **Breakout levels.** A close above about ¥3,550 would put the stock back above its estimated 200-day average and break the series of lower highs. A close below ¥3,083 would confirm a new leg down.

### Gaps
- Not available: RSI(14), MACD, true daily 50/100/200-day or 13/26/52-week averages, volume, trading-value trends, and margin-adjusted measures. Kabutan, Kabuyoho and Yahoo pages were blocked and their snippets did not expose them.
- The early-October 2026 price (1–2 Oct) could not be verified. The ¥3,255 figure for 1 Oct remains unverified.

## 4. Dividends (DPS FY2021–FY2025, FY2026 forecast, payout, policy)

### Takeaway
Only fragments could be verified:
- FY2025's dividend forecast was raised by ¥6 on 13 Nov 2025, alongside a 6% recurring-profit upgrade;
- FY2026's annual dividend forecast was raised by ¥4 on 6 Aug 2026;
- the 3.83–3.89% forecast yields imply an FY2026 DPS of **about ¥126 (estimate)**, roughly a **40% payout (estimate)**.

The DPS history for FY2021–FY2025 (interim and year-end) and the formal policy (payout target, progressive dividend or DOE) could not be retrieved.

### Cited Findings
- **13 Nov 2025:** the company raised this year's recurring-profit forecast by 6% (adding to a record-profit forecast) and raised the dividend by ¥6 (配当も6円増額). — [Kabutan news](https://kabutan.jp/stock/news?code=8804&b=k202511130214)
- **Nikkei on the same revision:** FY12/2025 net profit is now seen −12%, better than before, with the dividend increased (配当積み増し). — [Nikkei](https://www.nikkei.com/article/DGXZQOUB132440T11C25A1000000/)
- **FY2025 actual (results 12 Feb 2026):** operating profit +20.2%, net profit −10.6%. — [japanir](https://japanir.jp/company/company-8804/ir/8804-20260212-01_wp_financial_summary/); [FY2025 Tanshin PDF](https://pdf.irpocket.com/C8804/YpwX/Bm8F/l2Ip.pdf)
- **6 Aug 2026:** FY12/2026 net-profit forecast raised to +10% y/y; annual dividend raised by ¥4 (年間配4円積み増し). — [Nikkei](https://www.nikkei.com/article/DGXZQOUB067LD0W6A800C2000000/); [Kabutan](https://s.kabutan.jp/stocks/8804/)
- **Forecast dividend yield:**
  - 3.83% at ¥3,286 on 25 Sep 2026 ([Kabutan](https://s.kabutan.jp/stocks/8804/));
  - 3.89% with no explicit date, alongside the 18 Sep 2026 price data ([Nikkei Yuho page](https://www.nikkei.com/nkd/company/ednr/?scode=8804); [minkabu](https://minkabu.jp/stock/8804)).
- **PER 10.5x at ¥3,286** on 25 Sep 2026. — [Kabutan](https://s.kabutan.jp/stocks/8804/)
- **Actual EPS:** FY2021 ¥167.35, FY2022 ¥206.15, FY2023 ¥215.82, FY2024 ¥315.49. — [Matsui results page](https://finance.matsui.co.jp/stock/8804/settlement/index)

### Inferences
- **Implied FY2026 DPS forecast ≈ ¥126 (ESTIMATE).** Two independent price/yield pairs give the same answer: 3.83% × ¥3,286 = ¥125.9, and 3.89% × ¥3,236 = ¥125.9. Before the ¥4 increase on 6 Aug 2026, the forecast would therefore have been about ¥122 (estimate).
- **Implied FY2026 EPS ≈ ¥313 (ESTIMATE).** This comes from PER 10.5x, with a range of ¥311–314 allowing for rounding. Implied payout is about 40% (estimate). That is consistent with a payout-ratio-based policy of around 40%, but the policy text itself was not verified.
- **Dividend increases mid-year.** Both FY2025 and FY2026 saw mid-year increases that came with profit upgrades. This suggests a payout-linked policy rather than a fixed DPS: dividends rise with upgraded profit forecasts.

### Gaps
- Interim, year-end and annual DPS for FY2021–FY2025 actuals were not found.
- Also not found:
  - FY2025's final DPS;
  - FY2026's exact interim and year-end split;
  - historical payout ratios;
  - the stated policy (payout ratio, total payout, progressive dividend or DOE) under the 2020–2024 plan and the new medium-term plan;
  - any special or commemorative dividends.

  Primary sources (tatemono.com IR dividend page, Tanshin, Yuho) and irbank were blocked. The search budget ran out before targeted dividend queries could be run.

## 5. Buybacks, treasury shares, cancellations and dilution (FY2021–FY2026)

### Takeaway
One buyback is verified. It was authorised on 25 Dec 2024 for up to 1.5m shares (0.72%) and up to ¥3.0bn, to run 13 Feb–31 Aug 2025, executed by open-market purchases on the TSE. By 31 May 2025, 728,600 shares had been bought for ¥1.80bn, an average of ¥2,468. On 13 Nov 2025 the board considered cancelling treasury shares. Issued shares now stand at 207.978m. About 1.2m shares were probably cancelled (ESTIMATE). No other authorisations, splits or dilutive issues were verified, and treasury share counts could not be retrieved.

### Cited Findings
- **25 Dec 2024 board resolution:** buy back up to 1,500,000 shares (0.72% of shares outstanding) for up to ¥3.0bn, between 13 Feb 2025 and 31 Aug 2025. — [FilingReader, 1 Apr 2025](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares); [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-announces-share-repurchase-status-2)
- **March 2025:** 176,400 shares bought through the Tokyo Stock Exchange for ¥432,417,100. — [FilingReader](https://filingreader.com/news-wire/tokyo/2025-04-01/tokyo-tatemono-executes-share-buyback-program-acquires-176400-shares)
- **May 2025:** 167,300 shares for ¥428,360,750. Cumulative to 31 May 2025: 728,600 shares for ¥1,798,238,350. — [FilingReader, 2 Jun 2025](https://filingreader.com/news-wire/tokyo/2025-06-02/tokyo-tatemono-continues-share-repurchase-program-in-may-2025)
- **13 Nov 2025 board meeting:** considered revisions to the full-year forecast and dividend forecast, and cancellation of treasury shares (自己株式の消却). — [TipRanks](https://www.tipranks.com/news/company-announcements/tokyo-tatemono-announces-share-repurchase-status-2); [Simply Wall St](https://simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares/news/why-tokyo-tatemono-tse8804-is-up-134-after-reviewing-dividen). The search summary did not attribute this to a specific page.
- **Current issued shares:** 207,978 thousand. — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [Kabutan](https://s.kabutan.jp/stocks/8804/)

### Inferences
- **Average prices (calculated):** ¥2,451 in March 2025, ¥2,560 in May 2025, ¥2,468 cumulative.
- **Feb and Apr 2025 purchases (calculated):** 384,900 shares for ¥937.5m, an average of ¥2,436.
- **Progress at 31 May 2025:** 48.6% of the share cap and 59.9% of the yen cap used. ¥1.20bn and 771,400 shares of headroom remained.
- **Size of the completed programme (ESTIMATE).** At the prices prevailing in 2025, the ¥3.0bn cap would have bound before the 1.5m-share cap. The finished programme was therefore probably about 1.15–1.2m shares for about ¥3.0bn. Completion figures were not verified.
- **Size of the cancellation (ESTIMATE).** Comparing today's 207.978m issued shares with a pre-cancellation count of about 209.17m gives about 1.19m shares cancelled, around 0.57% of issued shares. The 209.17m figure is an **unverified recollection**. The result is consistent with the buyback estimate above.
- **Scale.** A ¥3bn buyback was about 0.6% of market cap at 2025 prices (about ¥2,500 × 209m ≈ ¥520bn). That is modest; capital return here is mostly dividend-led.
- **Implied share base.** "1.5m shares = 0.72%" implies about 208m shares outstanding excluding treasury shares at the time of the Dec 2024 resolution. Because of rounding the range is 206.9–209.8m, so the number is not precise.

### Gaps
- **Not verified:**
  - any buyback authorisations in 2021–2024 or 2026, including any announced with FY2025 results on 12 Feb 2026;
  - final execution of the 2025 programme (total shares and amount);
  - the cancellation date, share count and % of issued shares;
  - treasury shares held at each year-end FY2021–FY2025 and the latest count;
  - shares held by any executive stock-compensation trust (BIP or ESOP);
  - convertible bonds or other dilution.
- **No evidence of a stock split during 2021–2026 was found.** The Nikkei annual series shows no discontinuity, but this is not confirmed.
- **Where to look:** the FY2025 Yuho (自己株式の状況, filed 23 Mar 2026), TDnet 自己株式の取得/消却 releases, and irbank. All of these were blocked.

## 6. Total shareholder return over 1, 3 and 5 years vs TOPIX and peers

### Takeaway
Only price returns could be calculated. The dividend-inclusive TSR and the comparisons with TOPIX and peers could not be built because there was no DPS history, no index data and no peer data.

| Period | Price return | CAGR |
|---|---|---|
| End-2020 → end-2025 (5 calendar years) | **+150.6%** | 20.2% |
| End-2022 → end-2025 (3 calendar years) | **+121.8%** | 30.4% |
| CY2025 (1 year) | **+36.0%** | n/a |
| End-2020 → 18 Sep 2026 | +128.7% | n/a |

Dividends would add on top of these figures (see Inferences).

### Cited Findings
- Year-end closes: 2020 ¥1,415; 2021 ¥1,680; 2022 ¥1,599; 2023 ¥2,112; 2024 ¥2,607; 2025 ¥3,546. Latest is ¥3,236 on 18 Sep 2026. — [Nikkei 10-yr prices](https://www.nikkei.com/nkd/company/history/yprice/?scode=8804)
- An undated aggregator snapshot shows 1-yr +21.0%, 3-yr +65.23% and 5-yr +129.79%. It is internally inconsistent (see Q1) and probably price-only. **Do not use.** — [Simply Wall St](https://www.simplywall.st/stocks/jp/real-estate-management-and-development/tse-8804/tokyo-tatemono-shares); [TipRanks](https://www.tipranks.com/stocks/jp:8804)

### Inferences
**Price return to 18 Sep 2026 (¥3,236), by starting point (calculated)**

| Since end of | Price return |
|---|---|
| 2020 | +128.7% |
| 2021 | +92.6% |
| 2022 | +102.4% |
| 2023 | +53.2% |
| 2024 | +24.1% |

- **Dividends (ESTIMATE).** If historical yields were similar to today's forecast yield of about 3.8%, dividends would add roughly 3–4 percentage points a year to the figures above. Historical DPS was not verified, so this is not a TSR figure.
- **Where the gain came from.** Most of the 5-year gain came between 2023 and 2025, with three straight years of more than 20%. 2026 YTD has given back 8.7%.

### Gaps
- No verified TOPIX, TOPIX Real Estate, 8801, 8802 or 8830 data was obtained, so relative performance is not computed.
- **For reference only (UNVERIFIED, from background knowledge; must be checked):**
  - TOPIX year-end closes were about 1,804.68 (2020), 1,992.33 (2021), 1,891.71 (2022), 2,366.39 (2023) and 2,784.92 (2024).
  - On those numbers TOPIX price returns were +10.4%, −5.1%, +25.1% and +17.7% for 2021–2024, against 8804's +18.7%, −4.8%, +32.1% and +23.4%.
  - Cumulatively from end-2020 to end-2024, 8804 rose +84.2% against TOPIX +54.3%.
  - TOPIX's end-2025 level is not known.
- **The official TSR table** (株主総利回り vs TOPIX dividend-inclusive, 5 years) is in the FY2025 Yuho. The Yuho was blocked, and the search snippet did not include the numbers.

## 7. Short interest: JPX ≥0.5% short positions, margin balances, securities lending

### Takeaway
No short-interest, margin-balance or securities-lending data could be retrieved. Karauri.net, JPX, kabutan and irbank were blocked, and the search budget ran out before targeted queries.

What is verified:
- 8804 is a 貸借銘柄, so it can be shorted on margin;
- several institutions have filed ≥5% large-holding reports at undated times: Société Générale Securities, Mitsubishi UFJ Trust and Banking, Nomura Securities, SMBC Nikko and Fidelity;
- no activist holder was identified.

### Cited Findings
- 8804 is listed as "東証プライム 売建可" (margin short-selling allowed) and as a 貸借銘柄 (eligible for loans for margin trading). — [Matsui](https://finance.matsui.co.jp/stock/8804/index); [kabuyutai](https://www.kabuyutai.com/kobetu/tatemono.html)
- Large-holding reports (大量保有報告書) on 8804, dates and percentages not visible in the search results:
  - Société Générale Securities — [MAonline](https://maonline.jp/kabuhoyu/sh-s100qevb)
  - Mitsubishi UFJ Trust and Banking (two filings) — [MAonline 1](https://maonline.jp/kabuhoyu/sh-s100qbix); [MAonline 2](https://maonline.jp/kabuhoyu/sh-s100sz05)
  - Nomura Securities (three filings) — [MAonline a](https://maonline.jp/kabuhoyu/sh-s1009xen); [MAonline b](https://maonline.jp/kabuhoyu/sh-s100ciga); [MAonline c](https://maonline.jp/kabuhoyu/sh-s1008sgt)
  - SMBC Nikko — [MAonline](https://maonline.jp/kabuhoyu/sh-s100pxi6)
  - Fidelity — [MAonline](https://maonline.jp/kabuhoyu/sh-s1003owh)

### Inferences
- **The large-holding filers are probably not directional holders.** Filers such as SocGen Securities, Nomura and SMBC Nikko often report because of securities-lending, hedging or inventory positions. MUFG Trust and Fidelity are mainly asset-management or custody holders. Without the filings, none of these can be classed as short sellers or activists.
- **Sell signal reflects price trend only.** Kabuyoho's "sell continuation" signal reflects price trend and gives no information about short positions.

### Gaps
- **Not available:**
  - JPX short-position disclosures for holders of ≥0.5% (names, dates, %), and the trend over time (karauri.net/8804 and JPX 空売りの残高に関する情報 were blocked);
  - weekly margin balances (信用買残, 信用売残, 信用倍率) and their trend;
  - JSF lending balances (貸借取引残高) and reverse-repo fees (逆日歩);
  - the overall short-selling ratio.
- **Unclear filings:** the dates and holding percentages of the large-holding filings listed above.
- **Next step.** Once access is restored, the writer should pull karauri.net, the JPX daily short-position file and kabutan or Yahoo Japan margin history. Until then, short interest should be described as "not verified".
