# Halyk Bank (HSBK LI / KASE: HSBK) — Financials & Operating KPIs Dossier

Compiled: 23 October 2026. Units: KZT bn unless stated (KZT mn where quoted verbatim from releases). IFRS, consolidated, calendar FY.
GDR ratio: 1 GDR = 40 common shares.

## 0. Read this first: method, limits and tagging

**Research constraints in this session**
- **WebFetch failed for every host** (`getaddrinfo ENOTFOUND` for halykbank.com, kase.kz, investegate.co.uk, tradingview.com, fbroker.kz, investing.com and even en.wikipedia.org). Direct `curl` was also refused by the egress proxy (CONNECT 403) for all external hosts, google.com included.
- **The WebSearch budget ran out** after about 30 queries from this agent. The limit is 200 per turn and is shared by every agent in the turn.
- So **no primary PDF or Excel file (press release, databook, presentation or IFRS statements) could be opened directly.** Every number below comes from search-engine extracts of those documents, most of them quoting the bank's own press-release or RNS tables verbatim.
- **Before any figure is published, verify it against the PDFs listed in section 10.**

**Tags**
- **[v]** Quoted from a primary Halyk table (press release or RNS) in a search extract, and **cross-checked**. The check is an arithmetic tie-out (for example, interest income minus interest expense equals NII, or growth rates reconcile across years) or agreement between two or more sources.
- **[u]** Comes from a single source, a secondary or aggregator summary, or a search summary only. Treat it as unverified.
- **[d]** Derived by me arithmetically from reported figures. This is not a reported number.
- **[m]** Analyst recollection that searching did not verify. Do not use it without checking.
- **NOT FOUND** The figure was not obtained, either because the search budget ran out or because it was not in any extract.

---

## 1. Income statement (KZT bn)

### 1a. Annual

| Line | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Interest income | 733.2 [d] | 879.9 [v] (879,865; +20.0%) | NOT FOUND | 1,669.8 [d] (from FY24 release growth) | 2,170.8 [v] (2,170,786; +30.0%) | 2,695.0 [v] (2,694,957; +24.1%) |
| Interest expense | (333.7) [d] | (366.8) [v] (366,792; +9.9%) | NOT FOUND | (872.6) [v] (872,642, FY24 comparative) | (1,062.9) [v] (1,062,876; +21.8%) | (1,407.2) [v] (1,407,219; +32.4%) |
| Net interest income (before ECL) | 372.6 per AR2020 [u]; 399.6 implied by FY21 growth of +28.4% [d] (definitions differ) | 513.1 [v] (513,073; +28.4%) | 670.2 as originally reported [v]; 669.5 restated under IFRS 17 [v] | 810.5 per FY23 release [u]; 797.1 restated in FY24 release [v] | 1,107.9 [v] (1,107,910; +39.0%) | 1,287.7 [v] (1,287,738; +16.2%) |
| Net fee & commission income | NOT FOUND | NOT FOUND | 84.0 restated [u] (83,967) | 100.4 per FY23 release [u]; about 113.7 restated, implied by FY24 growth of +10.2% [d] | 125.3 [v] (125,284; +10.2%). Gross fee income 211.7 (211,734; +5.8%) | 140.1 [v] (140,149; +11.9%) |
| Net insurance result (IFRS 17) | n/a | n/a | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| FX / trading / securities gains | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Other income | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Total operating income | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Operating expenses | NOT FOUND | NOT FOUND | NOT FOUND | (216.4) [v] (216,405, FY24 comparative) | (263.4) [v] (263,373; +21.7%) | NOT FOUND |
| Credit loss expense / CoR | NOT FOUND | NOT FOUND | CoR 1.2% [u] | CoR 1.0% [v] | CoR 1.2% [v] | CoR 1.4% [u] (9M25 1.4%, versus guidance of 1.4%) |
| Profit before tax | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Income tax | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| **Net income (attributable to common shareholders)** | **352.7** [v] (352,654; 2019: 334,511) | **462.4** [v] (462,377; +31.1%) | **553.8** as originally reported [v] (553,752; +19.8%); **569.5** restated under IFRS 17 [u] (569,478) | **693.4** [v] (693,436; +21.8% versus restated 2022) | **921.0** [v] (920,988 attributable; 920,991 total; +32.8%) | **1,058.4** [v] (1,058,417; +14.9%) |
| EPS, KZT per share | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 97 [d] (net income ÷ about 10.88bn weighted shares; see note) |
| Weighted average shares (bn) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 10.88 [d] |

Notes:
- **Restatements.** IFRS 17 was adopted in 2023 and 2022 was restated: net income 553.8 → 569.5 and NII 670.2 → 669.5. The FY2024 release then re-presented the 2023 figures: NII 810.5 → 797.1, net fees 100.4 → about 113.7, ROAE 32.5% → 32.1% and NIM 6.2% → 6.1%. Use one consistent vintage per series.
- **Share count.** I derived about 10.88bn weighted average shares from 1Q26 EPS of KZT 21.57 (net income 234,809) and 1Q25 EPS of KZT 25.29 (275,016). The EPS values are [u], taken from an aggregator summary of the 1Q26 release. The number of shares issued and outstanding was **NOT FOUND**.
- **Aggregator cross-check** ([u], stockanalysis.com): NII of 513,073 / 669,466 / 797,140 / 1,107,910 / 1,287,738 and net income of 462,377 / 553,751 / 693,435 / 920,988 / 1,058,417 for 2021–25. This matches the figures above. Kalkine shows FY25 net income of 1,029,365 and FY24 NII of 1,122,964, which conflict, so treat those as unreliable.

### 1b. Half-years and quarters

| Line | 1Q25 | 2Q25 | 1H25 | 3Q25 | 9M25 | 4Q25 | 1Q26 | 2Q26 | **1H26** | 1H26 YoY |
|---|---|---|---|---|---|---|---|---|---|---|
| Interest income | NOT FOUND | NOT FOUND | 1,289.3 [v] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | **1,446.2** [v] (1,446,153) | +12.2% |
| Interest expense | NOT FOUND | NOT FOUND | (648.6) [v] | NOT FOUND | NOT FOUND | about (389) [u] (derived in a search summary) | NOT FOUND | NOT FOUND | **(788.5)** [v] (788,530) | +21.6% |
| NII (before ECL) | about 325.9 [d] | about 314.8 [d] | 640.7 [v/d] | NOT FOUND | NOT FOUND | NOT FOUND | 333.4 [u] (+2.3% YoY) | about 324.2 [d] | **657.6** [v] (657,623) | +2.6% |
| Net fee & commission income | about 33.8 [d] | about 34.0 [d] | about 67.8 [d] | NOT FOUND | NOT FOUND | NOT FOUND | 25.0 [u] (−26.1% YoY) | about 29.5 [d] (+18.4% QoQ [u]) | **54.5** [v] (54,513) | −19.6% |
| Operating expenses | NOT FOUND | NOT FOUND | about (146.6) [d] | NOT FOUND | NOT FOUND | NOT FOUND | +7.8% YoY [u] | NOT FOUND | **(154.6)** [u] (154,619) | +5.5% |
| Expected credit loss expense | NOT FOUND | NOT FOUND | about (61.5) [d] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | **(104.0)** [u] (104,029) | +69.1% |
| Net insurance result | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | |
| Profit before tax / income tax | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | |
| **Net income (attributable)** | 275.0 [v] (275,016) | 253.6 [v] (253,586) | 528.6 [v] (528,600; 528,602 total) | 281.3 [v] (+8.3%) | 809.9 [v] (+26.8%) | 248.5 [v] (248,485; −11.9% YoY; 4Q24 282,176) | 234.8 [v] (234,809; −14.6%) | **212.8** [v] (212,759; −16.1% YoY; about −9.4% QoQ [d]) | **447.6** [v] (447,568; 447,567 total) | −15.3% |
| EPS, KZT per share | 25.29 [u] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 21.57 [u] | NOT FOUND | NOT FOUND (about 41.1 [d]) | |

Tie-outs:
- 1H26 interest income minus interest expense gives 1,446,153 − 788,530 = 657,623, which matches. 1H25 gives 1,289,297 − 648,564 = 640,733.
- Quarterly net income sums tie: 1Q25 + 2Q25 = 528.6, plus 3Q25 = 809.9, plus 4Q25 = 1,058.4.
- **Secondary-source errors to ignore:** one Investing.com transcript summary gives about KZT 500bn of 1H26 net income and about KZT 1.27tn of interest income. Both conflict with the release.

Sources:
- 1H26 press release (18 Aug 2026): https://halykbank.com/storage/830/Press-Release.pdf. RNS: https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/half-year-financial-report/9726112
- Kalkine summary: https://kalkinemedia.com/uk/news/announcements/halyk-bank-kazakhstan-37qb-reports-153-decline-in-h1-2026-net-income-amid-regulatory-tightening-and-rising-funding-costs
- 1Q26 press release (18 May 2026): https://halykbank.com/storage/762/Press-Release.pdf. RNS: https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/consolidated-financial-results-for-the-1q-2026/9572733
- FY25 RNS (19 Mar 2026): https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--hsbk/consolidated-financial-results-for-the-fy-2025/9481568 and https://www.investormeetcompany.com/companies/jsc-halyk-bank/rns/4620457/view
- 9M25 (13 Nov 2025): https://kase.kz/files/emitters/HSBK/hsbk_relizs__131125_en.pdf and https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/9m-and-3q-financial-results/9231037
- FY24 (27 Mar 2025): https://halykbank.com/storage/278/Press-Release.pdf, https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/consolidated-financial-results-for-the-fy-2024/8800201 and https://cbonds.com/news/3330461/
- FY23: https://cbonds.com/news/2773309/, https://halykbank.com/storage/306/Presentation.pdf and https://frontier.eninvs.com/company/HALYK/report/2023-12-31/FY/source.pdf
- FY22: https://halykbank.com/storage/330/Presentation.pdf and https://www.annualreports.com/HostedData/AnnualReportArchive/j/jsc-halyk-bank_2022.pdf
- FY21: https://www.marketscreener.com/quote/stock/HALYK-BANK-8382832/news/CORRECTION-JSC-Halyk-Bank-Consolidated-financial-results-for-the-year-ended-31-December-2021-39762908/
- FY20: Annual Report 2020, https://halykbank.com/storage/794/2020.pdf
- Aggregator: https://stockanalysis.com/quote/kase/HSBK/financials/income-statement/

---

## 2. Balance sheet (KZT bn, period end)

| Line | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 31 Mar 2026 | **30 Jun 2026** |
|---|---|---|---|---|---|---|---|---|
| Total assets | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND (30 Jun 2025 was about 19,623 [d], from 1H26 growth of +12.3% YoY) | **20,908.5** [v] (20,908,456; audited by Deloitte) | about 21,200 [u] | **22,036.3** [v] (22,036,296; +5.4% YTD, +12.3% YoY) |
| Gross loans to customers | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 12,041 [d] (from +13.9% YTD in 2025) | **13,714.7** [v] (13,714,721; +13.9%) | 13,410.7 [u] (13,410,654; −2.2% YTD) | **13,958** [v] (+1.8% YTD, +13.2% YoY) |
| – Corporate | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 6,800 [u] (+11.3% YoY) |
| – SME | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 2,400 [u] (+24.7% YoY) |
| – Retail | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | about 4,601 [d] (from +4.2% YTD) | about 4,600 [u] (+8.3% YoY) | **4,794** [u] (+10.7% YoY, +4.2% YTD; 1.83m borrowers) |
| – Consumer / mortgage / car | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND (management says it is shifting toward secured lending such as auto loans [u]) |
| Net loans | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | net loan growth of +14.3% in 2025 [u] | NOT FOUND | NOT FOUND |
| Securities | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Cash & equivalents | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND. Liquid assets were 23.3% of total assets [u] |
| Customer deposits (amounts due to customers) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | **14,338.8** [v] (14,338,804) | legal entities −5.8% QoQ, individuals −1.0% QoQ [u] | **14,871** [u] (+8.2% YoY; +3.7% YTD [d]) |
| – Corporate / legal entities | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | +5.4% YoY [u]; level NOT FOUND |
| – Retail / individuals | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | +10.5% YoY [u]; level NOT FOUND |
| Debt securities issued | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Due to banks / other borrowed funds | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Subordinated debt | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| **Total equity** | 1,493.2 [u] (Wikipedia) | NOT FOUND | NOT FOUND | NOT FOUND | about 3,068 [d] (from +14.1% in 2025) | **3,500.4** [v] (3,500,351; +14.1%) | **3,740.9** [v] (3,740,942) | **3,643.1** [v] (3,643,116; +4.1% YTD, −2.6% QoQ after the dividend) |

Sources:
- 1H26 and 1Q26 press releases and RNS, as in section 1.
- FY25 audited statements as reported by KASE (20 Mar 2026): https://kase.kz/en/information/news/show/1562749
- Segment growth rates from the Investing.com H1 slides article: https://www.investing.com/news/company-news/halyk-bank-h1-2026-slides-digital-strength-amid-margin-squeeze-93CH-4865727
- H1 transcript: https://www.investing.com/news/transcripts/earnings-call-transcript-halyk-bank-h1-2026-profit-falls-as-margins-tighten-93CH-4865705

---

## 3. Ratios

| Ratio | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 1H25 | 1Q26 | 2Q26 | **1H26** |
|---|---|---|---|---|---|---|---|---|---|---|
| NIM | 4.7% [u] (2019: 5.3%) | 5.2% [v] (4Q21 5.0%) | 5.6% [v] | 6.2% per FY23 release [v]; 6.1% restated [v] | 7.2% [v] | 7.1% [v] (3Q25 7.1%, 9M25 7.2%, 4Q25 6.9% [u]) | 7.3% [v] | 7.0% [v] (1Q25 7.5%) | 6.7% [u] | **6.8%** [v]; 7.2% excluding the higher minimum reserve requirements [v] |
| Cost-to-income | 26.8% [u] (2019: 26.0%) | NOT FOUND | NOT FOUND | 19.2% [v] (FY24 comparative) | 17.6% [v] | NOT FOUND | 17.2% [v] | 18.2% [u] | NOT FOUND | **19.2%** [v] |
| Cost of risk (loans) | NOT FOUND | NOT FOUND | 1.2% [v] (4Q22 0.4%) | 1.0% [v] (4Q23 0.7%) | 1.2% [v] | 1.4% [u] (9M25 1.4% versus 9M24 1.3% [v]) | 1.4% [u] | 1.5% [u] | 1.4% [u] | **1.4%** [u] |
| ROAE | 25.5% [u] (2019: 28.8%) | 29.7% [v] | 31.7% as originally reported [v]; 32.4% restated [u] | 32.5% per FY23 release [v]; 32.1% restated [v] (4Q23 27.1%) | 34.0% [v] | 32.6% [v] | NOT FOUND | 25.9% [v] (1Q25 34.6%) | NOT FOUND (consensus expected 26.6%) | NOT FOUND; about 25% annualised [d] |
| ROAA | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 5.5% [v] | 5.4% [v] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Stage 3 ratio | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | **8.6%** [u] (KZT 1,194bn) |
| NPL 90+ ratio | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 2.6% [u] | 4.3% [u] | NOT FOUND | NOT FOUND | — | 5.3% [u] |
| Coverage | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | Stage 3 coverage 73.4% [u] (period ambiguous) | NOT FOUND | NPL 90+ coverage 114.9% [u] | — | Stage 3 coverage 58.0% [u] |
| Loans-to-deposits (gross) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 95.6% [d] | NOT FOUND | NOT FOUND | — | 93.9% [d] |
| k1-1 / k1-2 / k2 (unconsolidated) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | k2 18.9% [u]; k1-1 and k1-2 NOT FOUND | NOT FOUND | 21.0% / 21.0% / 21.0% [u] | — | **19.0% / 19.0% / 19.0%** [v]; minimums including buffers 9.5% / 10.5% / 12.0% |
| Basel CET1 / total CAR | 24.4% / 25.5% [u] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | NOT FOUND |
| LCR / NSFR | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | NOT FOUND |
| RWA density | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | — | NOT FOUND (RWA +3.2% YTD [u]) |

Notes:
- **Regulatory minimums.** These include a 3% conservation buffer and a 1% systemic buffer, per the bank's filing [u].
- **Why capital fell.** The k-ratios dropped from 21.0% to 19.0% in 2Q26 because of the dividend payment [u].
- **Why Stage 3 rose.** Management attributes it to the ongoing moratorium on selling problem retail loans to collectors, plus slower retail loan growth [u].
- **NPL 90+ path.** The 2.6% → 4.3% figures for FY24 → FY25 come from Freedom's 4Q25 note [u]. The 5.3% for 1H26 comes from the Investor Club Research Substack [u].

Sources:
- 1H26 release and RNS; Kalkine summary (above)
- Joshthompson blog: https://joshthompson.co.uk/investing/halyk-bank-half-year-results-2026/
- Freedom 4Q25 note: https://fbroker.kz/en/analytics/analytics-article/narodnyi-bank-otcet-za-4-i-kvartal-2025-goda-ru-2
- Investor Club 2Q26 update: https://investorclubresearch.substack.com/p/2q26-central-asian-banking-update
- Yahoo / GuruFocus 1Q26 call highlights: https://finance.yahoo.com/markets/stocks/articles/halyk-bank-kazakhstan-jsc-stu-010108533.html
- AR2020: https://halykbank.com/storage/794/2020.pdf

---

## 4. Segment reporting (IFRS 8) and geography

| Item | Status |
|---|---|
| Operating income and PBT by business segment (Corporate, SME, Retail, Investment banking, Insurance, Other), FY2021–FY2025 and 1H26 | **NOT FOUND.** Search budget exhausted before these were reached; the IFRS 8 note is in the audited consolidated FS. |
| Geographic split (Kazakhstan versus Georgia, Kyrgyzstan, Uzbekistan, Russia, Tajikistan): revenue, assets, net income | **NOT FOUND** |
| Foreign subsidiaries | Halyk Bank Georgia publishes standalone 2025 audited FS at the National Bank of Georgia: https://nbg.gov.ge/fm/%E1%83%90%E1%83%9C%E1%83%92%E1%83%90%E1%83%A0%E1%83%98%E1%83%A8%E1%83%92%E1%83%94%E1%83%91%E1%83%94%E1%83%91%E1%83%98/english/halyk/afs-eng-2025-halyk.pdf?v=b8vm9 (not read). Other subsidiary numbers: NOT FOUND. |

Suggested next step: open the FY2025 audited FS (KASE news 1562749, or the Halyk IR site) and take the segment note from there.

---

## 5. Operating KPIs

| KPI | Value | Date | Tag / source |
|---|---|---|---|
| Halyk Super-App MAU / DAU / monthly transacting users | 8.6m / 2.8m / 6.1m | 1 Jul 2026 | [u] Investing.com H1 slides article |
| Active B2C clients in the Super-App ecosystem | 11.5m | Jul 2026 | [u] Quartr IR summary |
| Payments and transfers count | 234.7m (+8.1% YoY) | 1H26 | [u] Investing.com H1 slides |
| Payments and transfers volume | KZT 10.5tn (+14.1% YoY) | 1H26 | [u] Investing.com H1 slides |
| B2B payment volumes | +25% YoY | 1H26 | [u] call summary |
| Active salary-card penetration | 39.3% of the employed population | 1H26 | [u] Investing.com H1 slides |
| Onlinebank (B2B) MAU / DAU / MTU | about 325k / about 144k / about 230k | 1Q26 | [u] 1Q26 call, https://halykbank.com/storage/779/Call-Transcript.pdf |
| Digital share of loans issued (by number) | 91% | 1Q26 | [u] 1Q26 call |
| Digital share of new deposits | 94% | 1Q26 | [u] 1Q26 call |
| Retail borrowers | 1.83m | 30 Jun 2026 | [u] |
| Market share in retail loans | 17.8% | 30 Jun 2026 | [u] H1 slides / transcript |
| Market shares in assets, total loans, corporate loans, deposits and retail deposits | NOT FOUND | | |
| Total retail, corporate and SME customer counts | NOT FOUND | | |
| Cards in issue, POS / acquiring terminals | NOT FOUND | | |
| Branches, employees | NOT FOUND | | |
| GDR buyback | Bought back 2,432 GDRs for USD 74,782 (about USD 30.75 per GDR) | date not captured | [u] https://www.investing.com/news/company-news/halyk-bank-buys-back-2432-gdrs-for-74782-93CH-4787730 |

---

## 6. Guidance history

### 6a. FY2025 guidance versus actual

| Metric | Initial (Mar 2025) | Updated during 2025 | Actual FY2025 |
|---|---|---|---|
| Net income | NOT FOUND | more than KZT 1tn, reaffirmed at the 3Q25 call (Nov 2025) [u] | 1,058.4 [v] — met |
| Loan growth | NOT FOUND | cut at 3Q25 to 12–15% [u] (Edison; Freedom also says the loan-growth forecast was lowered) | gross +13.9% [v]; net +14.3% [u] |
| NIM | NOT FOUND | NOT FOUND | 7.1% [v] |
| Cost of risk | NOT FOUND | about 1.4% [u] (Edison) | about 1.4% [u] |
| ROAE | NOT FOUND | more than 30% [u] (Edison) | 32.6% [v] |
| CIR | NOT FOUND | NOT FOUND | NOT FOUND |

The bank says it met all its FY2025 guidance targets [u] (Freedom 4Q25 note).

### 6b. FY2026 guidance and revisions

| Metric | Earliest indication (3Q25 call, Nov 2025) | Initial FY26 guidance (FY25 results, 19 Mar 2026) | 1Q26 (18 May 2026) | **1H26 (18 Aug 2026), current** | 1H26 actual |
|---|---|---|---|---|---|
| Net income | KZT 1.1tn [u] | about KZT 1tn ("trimmed") [u] | reaffirmed [u] | **about KZT 1tn**, unchanged [u, several sources] | 447.6 (H2 needs about 552) |
| ROAE | — | about 29% [u] | reaffirmed | **about 29%** [u] | about 25% annualised [d] |
| Total net loan growth | indicative 12–15% or 12–16% (Edison; ambiguous) [u] | 10–13% [u] (Edison / Investing.com analysis) | — | **9–12%** [u]: retail 8–10%, corporate and SME 10–13% | gross +1.8% YTD, +13.2% YoY |
| NIM | — | about 6.8% [u] | — | about 6.8% [u] | 6.8% |
| Cost of risk | — | 1.4–1.5% [u] (Quartr) | about 1.5% ("normalised") [u] | about 1.5% [u] | 1.4% |
| CIR | — | NOT FOUND | — | 18–20% [u] | 19.2% |
| Net fee and commission income | — | +5–10% growth [u] | fee guidance was to be updated with 2Q results [u] | **about −10% YoY** [u] (Freedom's 2Q26 note and one call summary; another summary still says +10%, so this conflicts) | −19.6% YoY |
| Dividend payout | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | first tranche of the 2025 dividend: KZT 30.1/share [u] |
| Effective tax rate | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |

Sources:
- Quartr: https://quartr.com/companies/halyk-bank-of-kazakhstan-joint-stock-company_15521
- Yahoo 2Q26 call highlights: https://finance.yahoo.com/markets/stocks/articles/halyk-bank-kazakhstan-jsc-fra-230138783.html
- Edison 3Q25 note: https://www.edisongroup.com/research/7-nim-likely-to-be-sustained-into-2026/BM-2469/
- Edison / Investing.com "Top player" note: https://uk.investing.com/analysis/halyk-bank--top-player-in-an-important-frontier-market-200624212
- Freedom 3Q25 note: https://fbroker.kz/en/analytics/analytics-article/halyk-bank-results-for-the-3rd-quarter-2025-en-2
- Freedom 2Q26 note: https://fbroker.kz/en/analytics/analytics-article/narodnyi-bank-otcet-za-2-i-kvartal-2026-goda-ru-2
- GuruFocus 3Q25 call: https://www.gurufocus.com/news/3207795/

---

## 7. Latest reported results: 1H / 2Q 2026 (released 18 Aug 2026), and 9M26 status

**Headline numbers**
- 1H26 net income was KZT 447.6bn, down 15.3% YoY. 2Q26 was KZT 212.8bn, down 16.1% YoY and about 9.4% QoQ [d]. Freedom calls it the weakest quarterly result in two years [u].
- NII rose 2.6% YoY to 657.6bn: interest income +12.2%, interest expense +21.6%.
- NIM was 6.8% for 1H26 versus 7.3% for 1H25, and 6.7% in 2Q26 versus 7.0% in 1Q26 [u]. The higher minimum reserve requirements (MRR) introduced in April cost about 40bp; NIM adjusted for them is 7.2%.
- Net fees fell 19.6% YoY to 54.5bn, mainly because of BNPL regulation and VAT on banking services. 2Q fees were up 18.4% QoQ.
- Opex rose 5.5% to 154.6bn (salary indexation and IT), and CIR rose to 19.2%.
- ECL expense rose 69.1% to 104.0bn [u]. CoR was 1.4%.

**Balance sheet**
- Total assets 22.04tn (+5.4% YTD). Gross loans 13.96tn (+1.8% YTD, +13.2% YoY). Deposits about 14.87tn (+8.2% YoY). Equity 3.64tn.

**Balance-sheet flags**
- Stage 3 rose to 8.6% (KZT 1,194bn), and Stage 3 coverage fell to 58.0% from 73.4% [u].
- NPL 90+ was 5.3% [u], up from 4.3% at FY25 [u].
- The k-ratios fell to 19.0% from 21.0% after the dividend.
- Deposit costs rose as the share of tenge deposits grew.
- Loan growth is subdued YTD (+1.8%) against full-year guidance of 9–12% (net).

**Versus consensus**
- Halyk's company-compiled consensus for 2Q26 net income was an average of KZT 246.5bn (median 243.5bn, range 236.1–263.0bn).
- The actual 212.8bn was about 14% below the average [d].
- Consensus 2Q26 ROAE was 26.6% [u]. Source: https://halykbank.com/results-and-presentations?tab=consensus (via search extract).

**Stock reaction**
- GDR closed USD 34.05, down 2.99% from USD 35.10, per Investing.com on 18 Aug [u]. The timing is uncertain because the article was published at 11:36.
- Ticker widgets in copies of the same article showed +0.73% and +1.11%, so the day's move is **not confirmed**.
- 52-week range USD 22.90–36.20 [u].
- Other data points: −4.92% on 25 Aug 2026 [u] (StockInvest), and USD 32.75 on 14 Oct 2026 (previous close 33.05) [u] (LSE page).
- KASE reaction: NOT FOUND.

**9M / 3Q 2026**
- **No 9M26 release was found** as of 23 Oct 2026, and the date is **NOT FOUND**.
- Prior-year pattern: 9M25 came out on 13 Nov 2025, 1Q26 on 18 May 2026 and 1H26 on 18 Aug 2026. That suggests mid-November 2026, which is an inference, not a confirmed date. Check the IR calendar.

**Management commentary on drivers [u]**
- Higher MRR, tighter retail lending rules (a debt-burden cap and a BNPL change) and higher deposit costs.
- Full-year guidance of about KZT 1tn net income and about 29% ROAE was kept.
- Investor Club Research expects about KZT 900bn for FY26 (−13% YoY).

---

## 8. Consensus estimates, targets, tax

### 8a. Net income, EPS and DPS

| Source (date) | FY2026E | FY2027E | FY2028E | Notes |
|---|---|---|---|---|
| Company guidance | NI about KZT 1,000bn; ROAE about 29% | — | — | |
| Halyk IR company-compiled consensus | 2Q26 NI 246.5 average | NOT FOUND | NOT FOUND | the FY consensus page was not reachable |
| Edison (paid by Halyk), Q1-26 update, about May 2026 | EPS USD 7.31/GDR; DPS USD 3.87/GDR | EPS USD 8.23; DPS USD 4.35 | NOT FOUND | fair value USD 37.0/GDR (from 38.0); 22% sustainable RoTE. https://www.edisongroup.com/research/slower-start-to-the-year-in-q126/BM-3386/ |
| Edison, "Top player" note, about 27 Apr 2026 | EPS USD 7.57; DPS USD 4.01 | EPS USD 8.84; DPS USD 4.68 | NOT FOUND | fair value USD 38.0 at 1.20x FY26 P/TBV. https://www.edisongroup.com/research/top-player-in-an-important-frontier-market/BM-3138/ |
| Edison, 3Q25 note, Nov 2025 | EPS USD 6.73; P/E 3.8x; ROE 28.4% | — | — | basis or FX unclear [u] |
| Investor Club Research, Aug 2026 | NI about KZT 900bn | — | — | Substack |
| Stockopedia consensus | EPS KZT 3,625.30 (next FY; −6.73%) | — | — | [u]; probably per GDR (about KZT 90.6/share [d]) |
| MarketScreener (two snapshots, undated) | NI USD 1,973m or USD 2,162m; DPS USD 3.64 or 3.30 | NI USD 2,179m or USD 2,392m; DPS USD 3.73 or 3.22 | NOT FOUND | [u]; snapshots conflict |
| FY2028 | NOT FOUND | | | |

### 8b. Target prices and ratings

| Source | Rating | Target | Date |
|---|---|---|---|
| Freedom Broker | Hold (downgraded from Buy) | KZT 440/share (from 450); about 15% upside | 2Q26 note, Aug–Sep 2026 [u] |
| Freedom Broker | Buy | KZT 450 (from 470); 20% upside | 1Q26 note, May 2026 [u] |
| Freedom Broker | Buy | KZT 470; 22% upside | 4Q25 note, Mar 2026 [u] |
| Freedom Broker | Buy | KZT 460 | 2Q25 note, Aug 2025 [u] |
| Edison (fair value, not a rating) | — | USD 37.0/GDR | about May 2026 |
| MarketScreener | Buy (2 analysts) | average USD 31.90 | undated [u] |
| Other aggregator | Buy (2 analysts) | KZT 557.50 | undated [u] |

Freedom's 2Q26 cut reflected a lower non-interest income forecast; its net-fee growth assumption went from +5–10% to −10% [u]. Halyk Finance, Renaissance, JPMorgan, Citi and Jefferies notes, and the overall rating distribution: **NOT FOUND**.

Source URLs:
- Freedom 2Q26: https://fbroker.kz/en/analytics/analytics-article/narodnyi-bank-otcet-za-2-i-kvartal-2026-goda-ru-2
- Freedom 1Q26: https://fbroker.kz/en/analytics/analytics-article/halyk-bank-q1-2026-report
- Freedom 4Q25: https://fbroker.kz/en/analytics/analytics-article/narodnyi-bank-otcet-za-4-i-kvartal-2025-goda-ru-2
- MarketScreener consensus: https://www.marketscreener.com/quote/stock/HALYK-BANK-8382832/consensus/
- Stockopedia: https://www.stockopedia.com/share-prices/halyk-bank-ao-LON:HSBK/

### 8c. 2026 Tax Code and bank CIT

**NOT FOUND.** The search budget ran out before this topic was reached. [m] My unverified recollection is that Kazakhstan's new Tax Code, effective 1 Jan 2026, raises CIT for banks above the standard 20% (to 25%, possibly with carve-outs). This **must be verified** before use. Halyk's ETR guidance: NOT FOUND.

---

## 9. Funding, debt and ratings

| Item | Status |
|---|---|
| Outstanding Eurobonds (coupon, currency, size, maturity) | NOT FOUND |
| Local KZT bonds | NOT FOUND |
| Subordinated debt | NOT FOUND |
| Covenants | NOT FOUND |
| Moody's / S&P / Fitch ratings and recent actions | NOT FOUND. Halyk's results presentations carry a ratings panel on the cover (e.g., https://halykbank.com/storage/826/Presentation.pdf), but it was not readable. |

---

## 10. Primary documents to open for verification (not reachable in this session)

| Document | URL | Date |
|---|---|---|
| 1H26 press release | https://halykbank.com/storage/830/Press-Release.pdf | 18 Aug 2026 |
| 1H26 RNS | https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/half-year-financial-report/9726112 | 18 Aug 2026 |
| 1H26 RNS (TradingView mirror) | https://www.tradingview.com/news/reuters.com,2026-08-18:newsml_RSR1073Ra:0-reg-jsc-halyk-bank-jsc-halyk-bank-37qb-half-year-financial-report/ | 18 Aug 2026 |
| 1Q26 press release | https://halykbank.com/storage/762/Press-Release.pdf | 18 May 2026 |
| Interim FS (likely 1Q26) | https://halykbank.com/storage/761/Financial-Statement.pdf | — |
| 1Q26 call transcript | https://halykbank.com/storage/779/Call-Transcript.pdf | May 2026 |
| Presentations (recent) | https://halykbank.com/storage/826/Presentation.pdf and https://halykbank.com/storage/685/Presentation.pdf | — |
| FY25 RNS | https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--hsbk/consolidated-financial-results-for-the-fy-2025/9481568 | 19 Mar 2026 |
| FY25 audited FS (KASE) | https://kase.kz/en/information/news/show/1562749 | 20 Mar 2026 |
| 9M25 press release | https://kase.kz/files/emitters/HSBK/hsbk_relizs__131125_en.pdf | 13 Nov 2025 |
| FY24 press release | https://halykbank.com/storage/278/Press-Release.pdf | 27 Mar 2025 |
| Annual Report 2024 | https://halykbank.com/storage/790/2024.pdf | — |
| FY23 presentation | https://halykbank.com/storage/306/Presentation.pdf | — |
| FY22 presentation | https://halykbank.com/storage/330/Presentation.pdf | — |
| Annual Report 2020 | https://halykbank.com/storage/794/2020.pdf | — |
| 1H21 presentation | https://halykbank.com/storage/366/Presentation.pdf | — |
| 9M24 presentation | https://halykbank.com/storage/286/Presentation.pdf | — |
| IR results and consensus page | https://halykbank.com/results-and-presentations?tab=consensus | — |
| FY2021 consensus PDF (format reference) | https://halykbank.com/storage/224/FY-2021.pdf | — |

## 11. Main data gaps (priority order)

1. 1H26 and FY25 lines between NII and net income: insurance result, FX and trading, other income, total operating income, PBT, tax and ETR, plus FY25 opex and EPS.
2. The IFRS 8 segment note (FY21–FY25, 1H26) and the geographic and subsidiary split.
3. The balance-sheet detail: securities, cash, deposit split levels, debt issued, interbank, sub-debt, and the retail product split. FY20–FY24 balance sheets are almost entirely missing.
4. LCR / NSFR, RWA, the Stage 3 history and the coverage series.
5. Market shares other than retail loans, customer counts, branches and staff, cards and POS.
6. Bonds and ratings.
7. The tax code and bank CIT, and the ETR guidance.
8. The FY27 and FY28 consensus; brokers beyond Freedom and Edison.
9. The 9M26 date.
