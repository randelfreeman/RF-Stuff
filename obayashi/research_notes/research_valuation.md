# Obayashi (1802) valuation research - PARTIAL (tool limits)
CAVEAT: WebFetch and curl were egress-blocked for every finance site (Yahoo, Kabutan, Marketscreener, Stooq, Obayashi IR). Only WebSearch snippets (AI-summarised, partly inconsistent) were available. Nothing below is verified against primary pages. Items not found are marked n/a.

## 1. Current valuation
- Latest close (snippet, kabutan/nikkei-type page): JPY 3,008 on 2026-09-30; market cap JPY 2,080,968m (=> ~692m shares implied); forecast PER 13.1x; actual PBR 1.66x. UNVERIFIED.
- Conflicting datapoints: 3,369 on 2026-07-07 (tradingeconomics); "3,955" (marketscreener snippet, undated); the hinted market cap 1.97tn / EV 1.75tn / P/E 11.8 / 706,951,050 shares (stockanalysis-type) is undated and does not match 3,405 x any share count I can confirm. The 3,405 hint is not verified.
- 52w/YTD: all-time high 4,439 (2026-02-27); YTD low 2,891 (2026-08-19) (kabutan/Yahoo JP snippets). Price is therefore ~32% below ATH, ~4% above YTD low.
- FY3/2026 actual: sales 2,586.3bn, operating income 194.7bn (+36.6%), net income 173.8bn. FY3/2027 company guide: sales 2,945bn, OP 180bn, NI 157bn (-10%), DPS JPY 47 (snippet; likely an interim/partial figure - FY3/26 DPS 88 reported). Sources: stockanalysis.com/quote/tyo/1802, Nikkei 2026-05 article.
- Method (my own, from snippets): EV/Sales = 1.75tn/2,586bn = 0.68x (EV undated); trailing P/E at 3,008 and NI 173.8bn: 2,081/173.8 = 12.0x; forward P/E (guide NI 157bn) = 13.3x (matches 13.1x). Net debt, minorities, EBITDA, EV/EBITDA, EV/EBIT, net debt/EBITDA, dividend yield: n/a - not found with reliability. Dividend yield at 3,008 and DPS 88 would be ~2.9% (computed, DPS unverified).

## 2. Price history
Verified-ish events from snippets:
- 2024-03-05: limit-up (stop-high) on capital policy (ROE >=10% by FY2026, big dividend hike) (Fisco, Diamond Zai, Nikkei Business).
- 2024-11: domestic broker upgrade to Outperform, TP 2,100->2,400.
- ~2025-11-05: full-year forecast raised.
- 2026-05 (FY3/26 results day): intraday drop -304 (-7.76%) to 3,612 on FY3/27 NI guide -10%, after large prior-day gain (Nikkei).
- 2026-02-27: ATH 4,439. 2026-08-19: YTD low 2,891.
- Finasee: stock ~1.8x in 5 yrs at an ATH (undated, 2024-25); tradingeconomics: +56% over 12 months to Jul 2026.
n/a - not found: year/quarter-end closes, Aug 5 2024, Apr 2025 day moves, cause of Aug 2026 slide (no explanation found). Daily series unobtainable; traders.co.jp/stocks/61_1802/historical and nikkei.com/nkd/company/history/yprice/?scode=1802 hold the data but could not be fetched.

## 3. Historical ranges
n/a - not found (irbank.net/1802/pbr is the source to fetch).

## 4. Peers (FY3/26, JPY bn, from marketscreener/stockanalysis snippets; mixed dates)
| Co | Sales | OP | EBIT mgn | Mkt cap | EV | EV/Sales |
|Kajima|3,067.3|237.6|7.7%|2,752.3|3,170.4|1.03x|
|Taisei|2,089.1|188.0|9.0%|2,617.1|2,802.3|1.34x (EV/EBITDA ~10.3x on EBITDA 273bn)|
|Shimizu|2,057.8|118.7|5.8%|~1,766|n/a (882.7bn quoted, implausible)|n/a|
|Obayashi|2,586.3|194.7|7.5%|2,081|1,750(undated)|0.68x|
Other multiples (snippets, basis unclear, 2026): Kajima fwd P/E 15.3x, P/B 1.8x, EV/EBITDA 12.3x; Shimizu fwd P/E 12.9x, EV/EBITDA 13.5x; Vinci P/E 14x EV/EBITDA 6.7x; Bouygues 16.8x/4.4x; Balfour 12.9x/6.6x; Skanska 20x/15.4x; Ferrovial 44.9x/31.8x. Same-basis table for global peers, Penta-Ocean/Toda/Kumagai, Samsung C&T etc: n/a - not found.
Listed status: Takenaka is unlisted (private; well known, not re-verified here). Sumitomo Mitsui Construction (1821), Toda, Haseko, Penta-Ocean, Kumagai, Okumura, Maeda, Nishimatsu listed. Bechtel, Kiewit private; Turner is owned by Hochtief (ACS).

## 5. Regression
Script: regression.py; chart: regression_ev_sales_vs_ebit.png. y = EV/Sales, x = EBIT margin. Only 2 peers (Kajima, Taisei) had usable data -> slope 0.246, intercept -0.872, R2 = 1 by construction (meaningless). Obayashi implied EV/Sales 0.98x vs 0.68x actual (unreliable). Japan-big-4 separate run not possible (Shimizu EV missing). Equity value/share implication not computed (net debt n/a).

## 6. Short interest
JPX margin data (snippets): 2026-06-25 margin short 75,300 sh (+2,400 w/w), long 854,100 (-113,700), ratio 11.34x. Tiny vs ~700m shares. JSF lending balance and FSA >0.5% short disclosures: n/a - not found (not seen in snippets).

## 7. Consensus
kabuyoho.jp (snippet): 7 analysts: 5 strong buy, 1 buy, 1 neutral; avg rating 4.57; mean TP JPY 3,871-3,929 (two snippets differ). Broker-specific ratings/TPs and consensus EPS/DPS FY3/27-29: n/a - not found.
