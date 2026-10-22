---
title: "Coupang, Inc. (NYSE: CPNG): data provenance"
subtitle: "Every connector call, raw data file, calculation and data cut-off behind the research pack"
date: "12 October 2026"
lang: en-GB
---

## 1. Scope and rules applied

| Item | What was used |
|---|---|
| Data sources | S&P Global Capital IQ through the *S&P - Deterministic Retrieval* connector, and ProntoNLP through the *Pronto* connector. Nothing else. |
| Web fetches | **None.** The session and agent transcripts contain no WebFetch or WebSearch calls (checked across all six transcripts). |
| SQL | **None.** No database queries were written or run. |
| User-supplied material | The Sanken Electric IC memo PDF, used only as a layout template. The *Asian Century Stocks* newsletter text (11-Oct-2026) pasted into the chat, treated as claims to verify, not as data (report section 27). |
| Other network use | React 18.3.1, ReactDOM 18.3.1 and htm 3.1.1 were downloaded from the npm registry to render the dashboard locally for checking; probes of cdnjs and jsDelivr were refused by the proxy. One GitHub call checked the target repository's visibility. The published dashboard loads those libraries from cdnjs/jsDelivr and its fonts from Google Fonts. None of these carry research data. |
| Analyst knowledge | A few board biographies are marked [u] (unverified) because the proxy statement is not in the connectors. They are context only. |
| Symbols | ‡ = figure returned without a source link ("source link unavailable"); [d] = derived from cited inputs; [e] = analyst estimate; [u] = unverified. |

## 2. Deliverables covered

| File | Description | SHA-256 (first 16) |
|---|---|---|
| `Coupang_CPNG_Research_Report.pdf` | Research report (PDF, 28 pages) | `b709377ded5c8425` |
| `Coupang_CPNG_Research_Report.docx` | Research report (Word) | `2fc1ee6a74d9ba4d` |
| `Coupang_CPNG_IC_Memo.pdf` | Investment committee memo (15 slides) | `98da7a4e4da469bd` |
| `Coupang_CPNG_Dashboard.html` | Interactive dashboard, standalone copy (repo file `Coupang_CPNG_Dashboard.html`); the same page is published privately on claude.ai | `bbb4287ad03a1bdb` |
| `Coupang_CPNG_Data_Provenance.pdf` / `.md` | This document | n.a. |
| `mcp_call_log.csv` | Machine-readable call log: arguments, result size and SHA-256 of each returned payload | n.a. |

Dashboard link (private to the owner until shared): https://claude.ai/artifact/MTptuuQt9Fd6zH14nXyEYL

## 3. Connector calls

**379 calls** between 2026-10-12 04:24:16 and 2026-10-12 04:42:40 UTC on 12-Oct-2026: **82 to S&P Capital IQ** and **297 to ProntoNLP**. 2 returned errors. Appendix A lists every call; `mcp_call_log.csv` holds the full arguments and a SHA-256 of each returned payload.

**By workstream**

| Workstream | Scope | Output | S&P | ProntoNLP | Total |
|---|---|---|---|---|---|
| Lead | Lead analyst session: identification, core financials, peers, prices, consensus, deals | `report, model` | 37 | 26 | 63 |
| A | Earnings, segments, data incident, guidance, call sentiment | `notes/A_earnings_segments.md` | 0 | 44 | 44 |
| B | Stock-move attribution, event history, strategy, M&A, capital return | `notes/B_catalysts_history.md` | 7 | 91 | 98 |
| C | Governance, management, ownership, insiders | `notes/C_governance_ownership.md` | 6 | 45 | 51 |
| D | Capital structure, liquidity, forensic accounting | `notes/D_capital_accounting.md` | 32 | 41 | 73 |
| E | Supply chain, competition, markets, regulation, M&A | `notes/E_supplychain_competition.md` | 0 | 50 | 50 |
| **Total** | | | **82** | **297** | **379** |

**By tool**

| Connector | Tool | Calls | What it returned |
|---|---|---|---|
| ProntoNLP | `searchSentences` | 181 | Cited sentences from filings and transcripts |
| ProntoNLP | `getSentenceContext` | 33 | Sentences around a cited sentence |
| ProntoNLP | `readDocuments` | 26 | Full transcript or filing text |
| ProntoNLP | `getStockPrices` | 22 | Daily, weekly or quarterly price bars |
| ProntoNLP | `getCompanies` | 11 | Company resolution (CPNG id 704377650) |
| ProntoNLP | `getDocuments` | 8 | Document lists with sentiment scores |
| ProntoNLP | `getAnalytics` | 6 | Event and topic analytics per call |
| ProntoNLP | `getCompanyPeers` | 4 | Peer and competitor relations |
| ProntoNLP | `getCompanyConsensus` | 3 | Quarterly consensus vs actuals |
| ProntoNLP | `getFilterOptions` | 2 | Valid filter values |
| ProntoNLP | `getSpeakers` | 1 | Executives and analysts on calls |
| S&P Capital IQ | `get_financial_line_item_from_identifiers` | 64 | Line items (revenue, EBITDA, EBIT, net income, net debt, shares, CFO, capex) by period, with doc-viewer links |
| S&P Capital IQ | `get_financial_statement_from_identifiers` | 11 | Full income statement, balance sheet and cash flow by period (statement-level links only) |
| S&P Capital IQ | `get_info_from_identifiers` | 5 | Company identity: CIQ id, ticker, industry, employees |
| S&P Capital IQ | `get_latest` | 1 | Latest available fiscal periods |
| S&P Capital IQ | `get_history_metadata_from_identifiers` | 1 | Listing and identifier history |

**Calls that returned errors**

- #175 `searchSentences` (E): MCP server "Pronto" tool "searchSentences" timed out after 60s
- #177 `searchSentences` (E): MCP server "Pronto" tool "searchSentences" timed out after 60s

**Large results saved to file by the harness:** 14 `readDocuments` results (full transcripts and filings) exceeded the inline limit. They were read in parts by the agents and are retained in the session's tool-results folder; their payload hashes are in the call log.

## 4. Data freshness

| Dataset | Coverage and cut-off | Source |
|---|---|---|
| Coupang annual financials | FY2021-FY2025 (FY2025 10-K filed 26-Feb-2026) | S&P Capital IQ ([FY2025 statements](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=255973354)) |
| Coupang quarterly financials | 3Q24-2Q26 (10-Q for the quarter to 30-Jun-2026) | S&P Capital IQ ([Q2 2026 statements](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=264559057)) |
| S&P 'latest period' check | Latest annual 2025; current date 2026-10-12 (call #3) | S&P Capital IQ |
| Peer financials | LTM to Jun-2026 (Walmart Jul-2026); FY2021-FY2025 history for the core peers | S&P Capital IQ |
| Share prices | Weekly closes 8-Mar-2021 to the week of 5-Oct-2026; reference close US$15.82 on 9-Oct-2026 ‡ | ProntoNLP price series |
| Earnings calls | Q4 2023 to Q2 2026; latest [4-Aug-2026](https://gam.prontonlp.com/#/ref/$DOCID_T000003779883). Next call listed for 3-Nov-2026 | ProntoNLP (S&P transcripts) |
| SEC filings | To the Q2 2026 10-Q ([4-Aug-2026](https://gam.prontonlp.com/#/ref/$DOCID_SEC000264559057)) and 8-Ks through Aug-2026; no proxy, S-1, 13D/G or Form 4 indexed | ProntoNLP |
| Consensus | Quarterly to 2Q26. 3Q26/4Q26 entries carry an effective date of 6-Mar-2025 (stale) and were not used; EPS returned scaled x1e6 ‡ | ProntoNLP getCompanyConsensus |
| Sentiment scores | Per-call document sentiment and event counts, Q4 2023 to Q2 2026 | ProntoNLP getDocuments / getAnalytics |

## 5. Most-cited source documents

| Document | Citations in the report | Link |
|---|---|---|
| Coupang 10-K FY2025 (filed 26-Feb-2026) | 123 | [SEC000255973354](https://gam.prontonlp.com/#/ref/$DOCID_SEC000255973354) |
| Q2 2026 earnings call (4-Aug-2026) | 95 | [T000003779883](https://gam.prontonlp.com/#/ref/$DOCID_T000003779883) |
| Coupang 10-Q Q2 2026 (4-Aug-2026) | 60 | [SEC000264559057](https://gam.prontonlp.com/#/ref/$DOCID_SEC000264559057) |
| Q1 2026 earnings call (5-May-2026) | 30 | [T000003711263](https://gam.prontonlp.com/#/ref/$DOCID_T000003711263) |
| Q4 2025 earnings call (26-Feb-2026) | 28 | [T000003665452](https://gam.prontonlp.com/#/ref/$DOCID_T000003665452) |
| Q3 2025 earnings call (4-Nov-2025) | 23 | [T000003578475](https://gam.prontonlp.com/#/ref/$DOCID_T000003578475) |
| 8-K: Q4/FY2025 results release (26-Feb-2026) | 17 | [SEC000255972090](https://gam.prontonlp.com/#/ref/$DOCID_SEC000255972090) |
| NAVER FY2025 annual report | 15 | [NONSEC000256804358](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000256804358) |
| 8-K: Q4/FY2023 results release | 14 | [SEC000218768452](https://gam.prontonlp.com/#/ref/$DOCID_SEC000218768452) |
| Coupang 10-K FY2021 | 11 | [SEC000177952319](https://gam.prontonlp.com/#/ref/$DOCID_SEC000177952319) |
| Coupang 10-Q Q1 2026 | 11 | [SEC000259645823](https://gam.prontonlp.com/#/ref/$DOCID_SEC000259645823) |
| 8-K: Q4/FY2024 results release | 9 | [SEC000237406755](https://gam.prontonlp.com/#/ref/$DOCID_SEC000237406755) |
| 8-K: Greenoaks/Surpique buyout (Apr-2025) | 9 | [SEC000239328925](https://gam.prontonlp.com/#/ref/$DOCID_SEC000239328925) |
| 8-K: data incident and Korea CEO change (Dec-2025) | 8 | [SEC000253203320](https://gam.prontonlp.com/#/ref/$DOCID_SEC000253203320) |
| Coupang 10-K FY2024 | 7 | [SEC000237408246](https://gam.prontonlp.com/#/ref/$DOCID_SEC000237408246) |
| Q2 2024 earnings call | 6 | [T000003215027](https://gam.prontonlp.com/#/ref/$DOCID_T000003215027) |
| Uber 8-K: Delivery Hero offer (Jul-2026) | 6 | [SEC000263635795](https://gam.prontonlp.com/#/ref/$DOCID_SEC000263635795) |
| 8-K: PIPC fines (Jun-2026) | 5 | [SEC000261784634](https://gam.prontonlp.com/#/ref/$DOCID_SEC000261784634) |
| S&P doc viewer: FY2025 10-K statements | 34 | [mid 255973354](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=255973354) |
| S&P doc viewer: Q2 2026 10-Q statements | 23 | [mid 264559057](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=264559057) |
| S&P doc viewer: Q1 2026 10-Q statements | 5 | [mid 259645823](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=259645823) |
| S&P doc viewer: FY2021 statements | 5 | [mid 218853463](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=218853463) |
| S&P doc viewer: FY2022 statements (FY2024 10-K filing set) | 5 | [mid 237408246](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=237408246) |
| S&P doc viewer: statement document 265578278 | 1 | [mid 265578278](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=265578278) |

The report carries 672 source links in total.

## 6. Raw data and working files

These files hold the data as returned by the connectors and the intermediate results. They are kept with the session and supplied privately. They are **not** committed to the public GitHub repository, because they reproduce licensed S&P Capital IQ and ProntoNLP content. The SHA-256 values let you check any copy against this record.

| File | Contents | Calls | Size | SHA-256 (first 16) |
|---|---|---|---|---|
| `raw/sp_cpng_core.json` | Coupang annual and quarterly statements, EBITDA, EPS, shares, statement links (S&P) | 4-13, 369-374 | 5,866 B | `a7b1c5262e29da61` |
| `raw/pronto_market.json` | Transcript ids, call sentiment scores and event counts, weekly closes at key dates, consensus (ProntoNLP) | lead Pronto calls | 2,746 B | `8e2bc7eb628fc74c` |
| `raw/cpng_weekly.py` | 292 weekly closes, 8-Mar-2021 to 5-Oct-2026 (ProntoNLP getStockPrices) | getStockPrices | 2,040 B | `64f1ed4be38effbd` |
| `raw/peers.py` | Peer inputs: prices, diluted shares, LTM revenue, EBITDA, EBIT, net income, net debt; EV and multiple formulas | 44, 59-73 | 3,200 B | `40cbd2214c597b85` |
| `raw/peers_calc.json` | Peer multiples output | derived | 7,221 B | `a54ce3e0931ede12` |
| `raw/peers2.py` | FCF yield and peer medians | 378-379 | 1,284 B | `9d61ff9a4b031c5a` |
| `raw/peers_final.json` | Peer table with medians (used in the report and dashboard) | derived | 8,389 B | `666760c9944af9a9` |
| `raw/regression.json` | OLS coefficients, EV/Sales on EBIT margin | derived | 99 B | `0a5f203f66d8d4a4` |
| `raw/hist_mult.json` | Coupang year-end EV/Sales history | derived | 279 B | `fb04149ef40b4a42` |
| `raw/hist_rel.py` | Core-peer year-end EV/Sales history | 343-345 | 2,049 B | `c434afda09cfbb8b` |
| `raw/hist_rel.json` | Core-peer medians by year-end | derived | 1,324 B | `c08fcecdf28c0a4f` |
| `raw/deals.json` | Precedent transactions with sources | 362-368 and Pronto | 3,900 B | `b3091f09c1df5a78` |
| `raw/events.json` | Price-chart catalyst annotations | workstream B | 1,020 B | `484efd302b7d62a8` |
| `raw/model.json` | EPS model output, three scenarios | derived | 4,565 B | `5fe0b0da0e23e1ae` |
| `raw/valuation.json` | Scenario valuation output | derived | 931 B | `f0b47845d0c37e7c` |
| `raw/q2_26.txt` | Compacted Q2 2026 call transcript (ProntoNLP readDocuments) | workstream A | 61,866 B | `d5186d6101882654` |
| `raw/q1_26.txt` | Compacted Q1 2026 call transcript | workstream A | 48,500 B | `2e8c8ab30fa92daf` |
| `raw/q4_25.txt` | Compacted Q4 2025 call transcript | workstream A | 45,392 B | `13fd3e7270711f11` |
| `raw/q3_25.txt` | Compacted Q3 2025 call transcript | workstream A | 38,565 B | `564d709fec838cbd` |
| `raw/pr_q4_25.txt` | Q4 2025 results release excerpt | workstream A | 34,516 B | `1cce17228e406b3b` |
| `notes/A_earnings_segments.md` | Workstream A research notes with citations and tool log | agent A | 56,109 B | `d5da534f8cc2dd76` |
| `notes/B_catalysts_history.md` | Workstream B research notes | agent B | 59,666 B | `83c1fff1b910cb29` |
| `notes/C_governance_ownership.md` | Workstream C research notes | agent C | 37,131 B | `0caa739e0093d7d0` |
| `notes/D_capital_accounting.md` | Workstream D research notes | agent D | 63,947 B | `2186fef8855202ed` |
| `notes/E_supplychain_competition.md` | Workstream E research notes | agent E | 44,174 B | `3c4750ae20ffc949` |
| `prov/mcp_calls_full.jsonl.gz` | Every connector call with its full arguments and full returned payload | all 379 | 438,003 B | `a1fd318d9d3cb798` |

**Code used for calculations** (committed to the repository under `research/CPNG/code/`):

- `model.py`: EPS model FY2026E-FY2028E, three scenarios (SHA-256 `35d72bd1ce86932c`)
- `valuation.py`: Scenario valuation and probability weighting (SHA-256 `f98086271ec21b05`)
- `raw/peers.py`: EV and multiples (SHA-256 `40cbd2214c597b85`)
- `raw/peers2.py`: FCF yield, peer medians (SHA-256 `9d61ff9a4b031c5a`)
- `raw/hist_rel.py`: Own-history multiples (SHA-256 `c434afda09cfbb8b`)
- `charts_a.py`: Regression, annual, quarterly and history charts (SHA-256 `aa85ef18e81ffb79`)
- `charts_b.py`: Sentiment and price charts (SHA-256 `04b8a55567dc5eaa`)
- `charts_c.py`: Segment, margin and scenario charts (SHA-256 `f23d6fdf280d964c`)
- `charts_d.py`: EBITDA bridge (SHA-256 `84a32f5796e675f3`)
- `prov/extract.py`: Call-log extraction from the session transcripts (SHA-256 `d35fc0b7263458aa`)

## 7. Calculations

### 7.1 Valuation multiples (report section 13)

- **EV** = share price × S&P weighted-average diluted shares (latest quarter) + S&P net debt including leases, in each company's reporting currency.
- **Coupang:** US$15.82 × 1,799m = US$28,460m market cap; less US$477m net cash including leases = **EV US$27,983m** [d]. LTM revenue US$35,462m gives **EV/Sales 0.79x**.
- **EV/EBITDA, EV/EBIT, P/E, net debt/EBITDA**: LTM S&P EBITDA, operating income and net income; shown as n.m. when the denominator is negative.
- **FCF yield** = (LTM CFO − LTM capex) / market cap, S&P line items (calls #378-379).
- **FX:** Chinese ADRs translated at CNY 7.10/US$ and HKD 7.80/US$ [e] (no FX series in the connectors). US$ market caps for KRW, JPY, EUR and PLN reporters use the FX implied by ProntoNLP's US$ vs local market-cap fields [d]: KRW 1,356, JPY 157.6, EUR 0.878, PLN 3.84 per US$.
- **Peer medians** (15 listed peers, Coupang excluded): EV/Sales 1.29x, EV/EBITDA 9.4x, EV/EBIT 24.2x, P/E 25.6x, EBITDA margin 9.7%, EBIT margin 5.6%, sales growth 10.9%, FCF yield 8.6%.

### 7.2 Regression (report section 13.3)

Ordinary least squares of LTM EV/Sales on LTM EBIT margin (%) across 14 listed peers, Coupang and Jumia excluded: **EV/Sales = 0.623 + 0.1116 × EBIT margin**, R² = 0.307. Implied values: 0.43x at Coupang's LTM -1.7%, 0.78x at its FY2025 1.4%, and 0.92x at our FY2028E base-case margin.

### 7.3 Own history (report section 13.2)

Year-end EV/Sales = (year-end close × S&P diluted shares + S&P net debt) / S&P annual revenue, for Coupang and six core peers (Amazon, MercadoLibre, Sea, NAVER, E-MART, Lotte Shopping). Year-end closes are ProntoNLP quarterly bars ‡.

### 7.4 EPS model, FY2026E-FY2028E (report section 11)

Revenue is built by segment: Product Commerce (PC) and Developing Offerings (DO). Adjusted EBITDA = PC revenue × PC margin + DO adjusted EBITDA. GAAP EBIT = adjusted EBITDA − D&A − SBC + one-offs. Net income = EBIT + net interest and other − tax; EPS = net income / diluted shares.

- **FY2026E** = H1'26 actuals plus a Q3/Q4 build. Q3E revenue US$9,640m: PC +6.5% cc less 5pts FX, DO +20%, margin 4.5% − 330bp (guide: −300 to −400bp). Q4E revenue US$9,685m at a 3.1% margin. One-offs: US$410m PIPC fines and ~US$150m Incheon fire [e]. Output: revenue US$36,686m, adjusted EBITDA US$608m, GAAP EBIT US$-1,117m, net income US$-1,195m, EPS US$-0.67 (adjusted US$-0.37).

| Assumption [e] | Bear FY27 / FY28 | Base FY27 / FY28 | Bull FY27 / FY28 |
|---|---|---|---|
| PC revenue growth (flat FX, so US$ = constant currency) | +5.5% / +5.5% | +11% / +10% | +14% / +13% |
| DO revenue growth | +12% / +10% | +18% / +18% | +22% / +20% |
| PC adj. EBITDA margin | 5.8% / 6.2% | 7.3% / 8.6% | 8.0% / 10.0% |
| DO adj. EBITDA (US$m) | -900 / -850 | -800 / -600 | -750 / -450 |
| D&A / SBC (US$m) | 680, 580 / 760, 620 | 680, 580 / 780, 620 | 680, 580 / 790, 630 |
| One-offs (US$m) | -150 / -100 | +100 / 0 | +100 / 0 |
| Effective tax rate | 80% / 70% (tax floor US$150m) | 55% / 40% | 50% / 33% |
| Diluted shares (m) | 1,800 / 1,810 | 1,790 / 1,795 | 1,785 / 1,790 |
| **Revenue (US$m)** | 39,092 / 41,543 | 41,139 / 45,817 | 42,300 / 48,309 |
| **Adj. EBITDA (US$m)** | 979 / 1,269 | 1,689 / 2,625 | 2,051 / 3,506 |
| **GAAP EPS (US$)** | -0.31 / -0.20 | 0.14 / 0.42 | 0.26 / 0.79 |

### 7.5 Scenario valuation (report section 22; `valuation.py`)

Per share = (multiple × NTM sales − net debt incl. leases) / FY2028E diluted shares. NTM sales at Oct-2027 = 0.25 × FY2027E + 0.75 × FY2028E revenue.

| | NTM sales (US$m) | Multiple | EV (US$m) | Net debt (US$m) | Shares (m) | Per share | vs US$15.82 | EV / FY28E adj. EBITDA | Weight |
|---|---|---|---|---|---|---|---|---|---|
| Bear | 40,930 | 0.45x | 18,419 | +1,200 | 1,810 | US$9.51 | -39.9% | 14.5x | 25% |
| Base | 44,648 | 0.85x | 37,951 | +300 | 1,795 | US$20.98 | +32.6% | 14.5x | 50% |
| Bull | 46,806 | 1.20x | 56,168 | -500 | 1,790 | US$31.66 | +100.1% | 16.0x | 25% |
| **Probability-weighted** | | | | | | **US$20.78** | **+31.4%** | | |

Displayed values round to US$9.5 / US$21.0 / US$31.7 and US$20.8. The 12-month target of US$21 is the base case.

### 7.6 Adjusted EBITDA bridge, FY2026E to FY2028E base case (`charts_d.py`)

Start US$608m. PC margin recovery = (FY28E PC margin 8.6% − FY26E PC margin 5.2%) × FY26E PC revenue = **+US$1,058m**. PC volume growth = (FY28E − FY26E PC revenue) × 8.6% = **+US$584m**. DO loss reduction = −US$600m − (−US$975m) = **+US$375m**. End US$2,625m. FY26E PC margin = (FY26E adjusted EBITDA + US$975m DO loss, the guide mid-point) / FY26E PC revenue.

### 7.7 Takeover value (report section 14.2)

Control value = 1.0-1.3x LTM sales (US$35.5bn) plus US$0.48bn net cash, divided by 1,799m diluted shares = **US$20.0-25.9 a share** [d]. A 30-40% premium to US$15.82 gives US$20.6-22.1. Precedent multiples are target EV / LTM sales at announcement from S&P target financials (calls #362-368) and acquirer filings via ProntoNLP [d].

### 7.8 Other derived figures

- **LTM figures** = sum of the last four reported quarters (S&P), e.g. LTM adjusted EBITDA US$872m = 413 + 267 + 29 + 163.
- **Net cash** = cash US$6,110m − funded debt US$2,603m (US$1,985m short-term + US$618m long-term) = US$3.5bn ex-leases; less US$3,030m operating leases = US$0.48bn, matching S&P net debt of −US$477m.
- **Cash conversion cycle** = DSO + DIO − DPO on year-end S&P balances (receivables / revenue, inventory / COGS and payables / COGS, × 365): −42, −64, −54, −57 days for FY2022-FY2025. FY2025: 3.8 + 33.8 − 94.2 days.
- **Cumulative Korean fines** = US$121m (KFTC, 2024) + US$410m (PIPC, 2026) = US$531m.
- **Negative-event share** = negative / (positive + negative) ProntoNLP event counts per call.
- **Moves of more than 10%** = week-on-week or day-on-day changes in the ProntoNLP price series ‡, attributed to dated company documents where one exists; otherwise marked [u].

## 8. Known gaps and quality notes

- **Source link unavailable (‡):** ProntoNLP price bars and consensus values carry no document link; S&P statement-level calls return statement links rather than line links for some periods.
- **Not in the connectors:** the 2026 proxy (executive pay, top-10 holders, director biographies and committees), 13F/13D/13G and Form 4 filings, short interest and short-seller reports, FX rates, and some Korean deal values. These are flagged in the report rather than estimated.
- **Unverified newsletter claims:** Korean e-commerce share (~28%), the KRW 7,890 WOW fee and the 10km coverage target could not be confirmed in S&P or ProntoNLP; see report section 27.
- **Consensus:** EPS values returned scaled ×1e6, and the 3Q26/4Q26 entries are stale (Mar-2025); no FY2027-28 consensus was available. Forward estimates are ours alone.
- **QA corrections made on 12-Oct-2026 before release:** LTM adjusted EBITDA set to US$872m and EV/adjusted EBITDA multiples recomputed; drawdown from the high corrected to 61%; the bull-case value standardised to the FY2028E share basis used for the other scenarios (US$31.7, +100%; probability-weighted US$20.8, +31%).

## Appendix A. Full connector call log

Times are UTC on 12-Oct-2026. Workstreams: Lead = lead analyst session; A-E = research agents (section 3). The SHA-256 is of the returned payload as logged.

| # | Time | WS | Connector | Tool | Key arguments | Chars | SHA-256 | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | 04:24:16 | Lead | S&P | `get_info_from_identifiers` | ids=CPNG,Coupang | 812 | `9b1823458a` | ok |
| 2 | 04:24:17 | Lead | Pronto | `getCompanies` | companyNameOrTicker=Coupang | 724 | `b44c11e5a9` | ok |
| 3 | 04:24:17 | Lead | S&P | `get_latest` |  | 178 | `807c4a74f8` | ok |
| 4 | 04:24:33 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=income_statement; period_type=annual; start_year=2020; end_year=2025; calendar_type=fiscal | 13,588 | `b5fc2b1974` | ok |
| 5 | 04:24:34 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=balance_sheet; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 15,341 | `386fa99f76` | ok |
| 6 | 04:24:35 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=cashflow; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 12,675 | `f3d7de5433` | ok |
| 7 | 04:24:36 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=income_statement; period_type=quarterly; num_periods=8 | 17,270 | `9ee5791fc0` | ok |
| 8 | 04:24:41 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=balance_sheet; period_type=quarterly; num_periods=2 | 5,778 | `6dac38885e` | ok |
| 9 | 04:24:42 | Lead | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=cashflow; period_type=quarterly; num_periods=6 | 13,260 | `172211ee6c` | ok |
| 10 | 04:24:44 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=ebitda; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,259 | `e94d4cf0ff` | ok |
| 11 | 04:24:45 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=diluted_eps; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,167 | `8f06c2d17e` | ok |
| 12 | 04:24:46 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=weighted_average_diluted_shares_outstanding; period_type=quarterly; num_periods=24 | 8,131 | `1b46cbc4c5` | ok |
| 13 | 04:24:47 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=common_shares_outstanding; period_type=quarterly; num_periods=24 | 1,148 | `82c5cd2a4a` | ok |
| 14 | 04:24:50 | Lead | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2021-03-01", "lte": "now"}; interval=week | 44,727 | `b4d313cd0d` | ok |
| 15 | 04:24:51 | Lead | Pronto | `getDocuments` | companiesIds=704377650; corpus=S&P Transcripts; size=25; dateRange={"gte": "2024-01-01", "lte": "now"} | 6,074 | `5622a4acd6` | ok |
| 16 | 04:24:52 | Lead | Pronto | `getCompanyConsensus` | companiesIds=704377650; dateRange={"gte": "2025-01-01", "lte": "2029-12-3…; timeframeInterval=year; metrics=revenue,netIncomeGaap (+4) | 7,989 | `e74c25cbd9` | ok |
| 17 | 04:24:54 | Lead | Pronto | `getCompanyConsensus` | companiesIds=704377650; dateRange={"gte": "2025-06-01", "lte": "2027-06-3…; timeframeInterval=quarter; metrics=revenue,epsGaap (+2) | 6,828 | `335fe9d680` | ok |
| 18 | 04:27:20 | D | Pronto | `getFilterOptions` | filterNames=documentTypes,sections | 15,212 | `0282f24733` | ok |
| 19 | 04:27:20 | E | Pronto | `getCompanyPeers` | companiesIds=704377650; relations=supplier; size=20 | 6,284 | `b567ef042c` | ok |
| 20 | 04:27:20 | B | Pronto | `searchSentences` | q="Farfetch acquisition consideration Greenoaks bridge loan"; companiesIds=704377650 | 24,655 | `5613a794f5` | ok |
| 21 | 04:27:21 | A | Pronto | `searchSentences` | q="Product Commerce segment revenue growth"; transcriptsIds=T000003779883 | 48,242 | `1a4fb7e6db` | ok |
| 22 | 04:27:21 | C | Pronto | `getFilterOptions` | filterNames=documentTypes,sections | 15,212 | `0282f24733` | ok |
| 23 | 04:27:21 | E | Pronto | `getCompanyPeers` | companiesIds=704377650; relations=customer; size=20 | 15,529 | `72092a0a3c` | ok |
| 24 | 04:27:21 | B | Pronto | `searchSentences` | q="share repurchase program authorized"; companiesIds=704377650 | 27,084 | `56beac5444` | ok |
| 25 | 04:27:21 | A | Pronto | `searchSentences` | q="adjusted EBITDA margin gross profit"; transcriptsIds=T000003779883 | 46,617 | `fe196cbe99` | ok |
| 26 | 04:27:22 | E | Pronto | `getCompanyPeers` | companiesIds=704377650; relations=competitor; size=20 | 12,002 | `72050f2d29` | ok |
| 27 | 04:27:22 | B | Pronto | `searchSentences` | q="data breach unauthorized access customer information"; companiesIds=704377650; dateRange={"gte": "2025-10-01", "lte": "now"} | 33,983 | `77a8df453e` | ok |
| 28 | 04:27:22 | E | Pronto | `getCompanyPeers` | companiesIds=704377650; relations=adjacent; size=20 | 13,434 | `0926d958d1` | ok |
| 29 | 04:27:22 | D | Pronto | `getDocuments` | companiesIds=704377650; documentTypes=10-K,10-Q; size=10 | 5,268 | `1ec104674f` | ok |
| 30 | 04:27:24 | C | Pronto | `getDocuments` | companiesIds=704377650; corpus=SEC Filings; size=60; dateRange={"gte": "2021-01-01", "lte": "now"} | 26,585 | `dab6bdbe27` | ok |
| 31 | 04:27:27 | D | Pronto | `searchSentences` | q="borrowings credit facility interest rate maturity"; transcriptsIds=SEC000264559057 | 28,826 | `7088cbca61` | ok |
| 32 | 04:27:28 | C | Pronto | `readDocuments` | transcriptsIds=SEC000261896065,SEC000261784634 (+3); size=300; excludeMetadata=false | 1,289 | `31a66efda5` | ok |
| 33 | 04:27:28 | B | Pronto | `searchSentences` | q="customer compensation vouchers impact on revenue growth and margin"; transcriptsIds=T000003711263 | 9,491 | `6e92ad4ef7` | ok |
| 34 | 04:27:29 | A | Pronto | `readDocuments` | transcriptsIds=T000003779883; size=500 | 1,290 | `98fd7b6d92` | ok |
| 35 | 04:27:29 | B | Pronto | `searchSentences` | q="Korea Fair Trade Commission fine administrative penalty"; companiesIds=704377650; corpus=SEC Filings | 9,799 | `a1ea7d72fc` | ok |
| 36 | 04:27:30 | B | Pronto | `searchSentences` | q="WOW membership fee increase"; companiesIds=704377650 | 8,631 | `0c39cdc07e` | ok |
| 37 | 04:27:32 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000264559057-130 (+2); before=10, after=10 | 11,519 | `09760299c3` | ok |
| 38 | 04:27:34 | B | Pronto | `searchSentences` | q="membership price change won per month"; transcriptsIds=T000003113152,T000003215027 (+2) | 7,386 | `27dd97eff3` | ok |
| 39 | 04:27:35 | D | Pronto | `searchSentences` | q="administrative fines data breach penalty accrual"; transcriptsIds=SEC000264559057 | 30,123 | `2102d4b2b1` | ok |
| 40 | 04:27:36 | B | Pronto | `searchSentences` | q="Taiwan Rocket Delivery launch growth"; companiesIds=704377650; corpus=S&P Transcripts | 7,329 | `9ee7c6e0f2` | ok |
| 41 | 04:27:37 | B | Pronto | `searchSentences` | q="Developing Offerings Eats Play Taiwan Farfetch description launched"; transcriptsIds=SEC000255973354 | 12,528 | `d8ba4b9e90` | ok |
| 42 | 04:27:37 | E | Pronto | `searchSentences` | q="market share Korean e-commerce"; companiesIds=704377650 | 11,304 | `cfb040e5c7` | ok |
| 43 | 04:27:38 | E | Pronto | `searchSentences` | q="competition Naver Chinese cross-border platforms"; companiesIds=704377650 | 11,124 | `096d604c58` | ok |
| 44 | 04:27:38 | Lead | S&P | `get_info_from_identifiers` | ids=AMZN,MELI,SE (+13) | 6,609 | `aa2c4fe028` | ok |
| 45 | 04:27:38 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000264559057-410 (+3); before=10, after=10 | 16,523 | `befdbed7d3` | ok |
| 46 | 04:27:39 | E | Pronto | `searchSentences` | q="suppliers payment terms inventory"; companiesIds=704377650 | 8,301 | `5b46a61c40` | ok |
| 47 | 04:27:41 | B | Pronto | `getDocuments` | companiesIds=704377650; corpus=SEC Filings; size=60 | 26,585 | `dab6bdbe27` | ok |
| 48 | 04:27:42 | B | Pronto | `getDocuments` | companiesIds=704377650; corpus=News; size=30 | 190 | `70ce90bd37` | ok |
| 49 | 04:27:43 | D | Pronto | `searchSentences` | q="customer compensation vouchers reduction of revenue"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2025-12-01"} | 24,442 | `c92143a583` | ok |
| 50 | 04:27:44 | E | Pronto | `searchSentences` | q="competitors include retailers e-commerce companies"; transcriptsIds=SEC000255973354 | 13,073 | `6eda27956a` | ok |
| 51 | 04:27:45 | E | Pronto | `searchSentences` | q="fulfillment centers logistics network delivery workers"; transcriptsIds=SEC000255973354 | 11,569 | `853984d439` | ok |
| 52 | 04:27:46 | E | Pronto | `searchSentences` | q="Large-Scale Retail Business Act Fair Trade Commission regulation"; transcriptsIds=SEC000255973354 | 12,615 | `de8a54f1ca` | ok |
| 53 | 04:27:46 | B | Pronto | `readDocuments` | transcriptsIds=SEC000253203320,SEC000255152730 (+3); size=150 | 21,255 | `937bece459` | ok |
| 54 | 04:27:46 | C | Pronto | `readDocuments` | transcriptsIds=SEC000242702862,SEC000242375946 (+6); size=400; excludeMetadata=false | 1,291 | `d8067474f4` | ok |
| 55 | 04:27:47 | A | Pronto | `readDocuments` | transcriptsIds=T000003711263; size=500 | 1,290 | `2fb6db895d` | ok |
| 56 | 04:27:47 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000264559057-16 (+2); before=6, after=8 | 8,541 | `0fb15660e2` | ok |
| 57 | 04:27:47 | A | Pronto | `readDocuments` | transcriptsIds=T000003665452; size=500 | 1,290 | `5ce820bf4e` | ok |
| 58 | 04:27:47 | A | Pronto | `readDocuments` | transcriptsIds=T000003578475; size=500 | 1,290 | `7fdf2ea333` | ok |
| 59 | 04:27:48 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=revenue; period_type=ltm; num_periods=5 | 21,691 | `33bdb14c99` | ok |
| 60 | 04:27:49 | E | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-2008 (+2); before=4, after=4 | 4,985 | `aba66cf196` | ok |
| 61 | 04:27:49 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=ebitda; period_type=ltm; num_periods=1 | 6,468 | `383325daa5` | ok |
| 62 | 04:27:50 | B | Pronto | `readDocuments` | transcriptsIds=SEC000242375946,SEC000242143978 (+7); size=200; excludeMetadata=true | 1,290 | `c3bd8c66de` | ok |
| 63 | 04:27:50 | E | Pronto | `searchSentences` | q="data breach personal information leak incident"; transcriptsIds=SEC000255973354 | 8,735 | `ed7a716064` | ok |
| 64 | 04:27:51 | D | Pronto | `searchSentences` | q="term loan collateral land buildings secured"; transcriptsIds=SEC000255973354; sections=10K_Notes | 14,920 | `5c20042933` | ok |
| 65 | 04:27:51 | E | Pronto | `searchSentences` | q="exchange rate Korean won U.S. dollar fluctuations"; transcriptsIds=SEC000255973354 | 8,244 | `20d1dd3139` | ok |
| 66 | 04:27:51 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=operating_income; period_type=ltm; num_periods=1 | 6,625 | `0895650107` | ok |
| 67 | 04:27:53 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=net_income; period_type=ltm; num_periods=1 | 6,642 | `353e6c683e` | ok |
| 68 | 04:27:53 | E | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-222; before=0, after=6 | 1,626 | `b9c40b7d48` | ok |
| 69 | 04:27:54 | E | Pronto | `searchSentences` | q="third-party cloud data center providers"; transcriptsIds=SEC000255973354 | 6,501 | `ef1ebe3913` | ok |
| 70 | 04:27:54 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=net_debt; period_type=quarterly; num_periods=1 | 6,496 | `f24cc8d994` | ok |
| 71 | 04:27:55 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1926 (+2); before=6, after=10 | 6,583 | `fd329b8d4f` | ok |
| 72 | 04:27:55 | E | Pronto | `searchSentences` | q="independent delivery partners Coupang Flex classification employees"; transcriptsIds=SEC000255973354 | 8,041 | `02d4290d5b` | ok |
| 73 | 04:27:56 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=weighted_average_diluted_shares_outstanding; period_type=quarterly; num_periods=1 | 7,213 | `bf0feaa892` | ok |
| 74 | 04:27:57 | C | Pronto | `readDocuments` | companiesIds=704377650; sections=8K_SEC5_I502,8K_SEC5_I507 (+1); size=500; excludeMetadata=false | 1,290 | `f45fc344f8` | ok |
| 75 | 04:27:57 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1931 (+1); before=8, after=5 | 5,364 | `0f0dec2861` | ok |
| 76 | 04:27:59 | E | Pronto | `searchSentences` | q="Farfetch luxury brands boutiques"; transcriptsIds=SEC000255973354 | 8,118 | `7eaff235ce` | ok |
| 77 | 04:27:59 | B | Pronto | `readDocuments` | transcriptsIds=SEC000242143978,SEC000239328925 (+16); sections=8K_SEC1,8K_SEC2 (+4); size=300 | 4,034 | `9d8fddb3ce` | ok |
| 78 | 04:28:00 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-2036 (+1); before=8, after=8 | 6,543 | `cc6a556ed0` | ok |
| 79 | 04:28:00 | E | Pronto | `searchSentences` | q="Rocket Fresh farmers SMEs small business suppliers"; transcriptsIds=SEC000255973354 | 7,928 | `df0b9d919c` | ok |
| 80 | 04:28:01 | E | Pronto | `searchSentences` | q="Coupang Play content licensing sports rights"; transcriptsIds=SEC000255973354 | 6,675 | `afc6817cef` | ok |
| 81 | 04:28:02 | E | Pronto | `searchSentences` | q="WOW membership members fee benefits"; transcriptsIds=SEC000255973354 | 8,265 | `5463ccb4ce` | ok |
| 82 | 04:28:03 | D | Pronto | `searchSentences` | q="Farfetch purchase consideration goodwill intangible assets fair value"; transcriptsIds=SEC000237408246 | 21,654 | `c2890b2d51` | ok |
| 83 | 04:28:04 | B | Pronto | `readDocuments` | transcriptsIds=SEC000242143978,SEC000239328925 (+16); sections=8K_SEC1_I101,8K_SEC2_I201 (+6); size=300; excludeMetadata=false | 1,290 | `e50f393159` | ok |
| 84 | 04:28:05 | E | Pronto | `getSentenceContext` | sentenceIds=T000003578475-151 (+2); before=2, after=8 | 3,462 | `f71a386cb5` | ok |
| 85 | 04:28:06 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000237408246-1872 (+2); before=6, after=8 | 8,443 | `1e6fbe8549` | ok |
| 86 | 04:28:07 | E | Pronto | `readDocuments` | transcriptsIds=T000003711263; size=500 | 1,290 | `59379f3e75` | ok |
| 87 | 04:28:07 | C | Pronto | `readDocuments` | transcriptsIds=SEC000255973354; sections=10K_P3_I10,10K_P3_I11 (+5); size=300 | 8,861 | `fb07d1e61c` | ok |
| 88 | 04:28:08 | A | Pronto | `searchSentences` | q="full year net revenues adjusted EBITDA"; transcriptsIds=T000003384178,T000003041770 | 30,867 | `e9eec33998` | ok |
| 89 | 04:28:09 | D | Pronto | `searchSentences` | q="pledged as collateral against long-term loan facilities"; transcriptsIds=SEC000255973354,SEC000259645823 | 11,191 | `8be076e9b0` | ok |
| 90 | 04:28:09 | A | Pronto | `getDocuments` | companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2021-03-01", "lte": "2023-12-3…; size=30 | 6,070 | `58107e7f7d` | ok |
| 91 | 04:28:11 | C | Pronto | `searchSentences` | q="Class B common stock 29 votes Bom Kim voting power"; transcriptsIds=SEC000255973354 | 19,479 | `b763df056c` | ok |
| 92 | 04:28:12 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000259645823-150 (+1); before=10, after=10 | 6,956 | `1abe403b81` | ok |
| 93 | 04:28:14 | A | Pronto | `searchSentences` | q="full year Product Commerce net revenues growth"; transcriptsIds=T000003384178,T000003041770 (+2) | 30,616 | `e7eea28480` | ok |
| 94 | 04:28:15 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1198 (+2); before=10, after=10 | 10,530 | `4e7bf0b6f7` | ok |
| 95 | 04:28:15 | A | Pronto | `searchSentences` | q="active customers net revenues per active customer"; transcriptsIds=T000003384178,T000003041770 (+4) | 30,456 | `e541e9596a` | ok |
| 96 | 04:28:15 | D | Pronto | `searchSentences` | q="credit ratings downgrade rating agencies"; transcriptsIds=SEC000255973354 | 3,448 | `e114396323` | ok |
| 97 | 04:28:18 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1490 (+1); before=10, after=10 | 7,380 | `270fc0e7c9` | ok |
| 98 | 04:28:18 | C | Pronto | `searchSentences` | q="controlled company exemption NYSE corporate governance"; companiesIds=704377650; corpus=SEC Filings | 8,507 | `f3c47c8e8a` | ok |
| 99 | 04:28:19 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2021-03-01", "lte": "now"}; interval=week | 44,727 | `b4d313cd0d` | ok |
| 100 | 04:28:20 | C | Pronto | `searchSentences` | q="Class B common stock automatic conversion sunset death or incapacity …"; companiesIds=704377650; corpus=SEC Filings | 8,197 | `a3e0368783` | ok |
| 101 | 04:28:20 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1745; before=6, after=10 | 2,702 | `11e457ce3f` | ok |
| 102 | 04:28:21 | Lead | Pronto | `getStockPrices` | companiesIds=18749,34322384 (+13); dateRange={"gte": "2026-10-01", "lte": "now"}; interval=week | 4,942 | `a2e13a3bb8` | ok |
| 103 | 04:28:21 | A | Pronto | `searchSentences` | q="Product Commerce net revenues increased year ended December 31"; companiesIds=704377650; corpus=SEC Filings | 33,555 | `5a2eee580e` | ok |
| 104 | 04:28:21 | E | Pronto | `readDocuments` | transcriptsIds=T000003779883; size=500 | 1,290 | `dd5440a715` | ok |
| 105 | 04:28:21 | C | Pronto | `searchSentences` | q="securities class action IPO derivative lawsuit Bom Kim stock sale"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2025-01-01", "l… | 7,730 | `1992aaef5d` | ok |
| 106 | 04:28:23 | D | Pronto | `searchSentences` | q="Farfetch marketplace commission revenue agent principal boutiques"; transcriptsIds=SEC000255973354; sections=10K_Notes | 7,971 | `b264086ff2` | ok |
| 107 | 04:28:25 | A | Pronto | `readDocuments` | transcriptsIds=SEC000255972090; size=150 | 1,289 | `db9cb78869` | ok |
| 108 | 04:28:26 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1868; before=6, after=10 | 3,110 | `36ebb59be1` | ok |
| 109 | 04:28:26 | C | Pronto | `searchSentences` | q="shares of Class B common stock outstanding"; companiesIds=704377650; corpus=SEC Filings | 12,013 | `d6ecfb372d` | ok |
| 110 | 04:28:26 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-05-01", "lte": "2026-05-0…; interval=day | 946 | `8fe050f0ce` | ok |
| 111 | 04:28:27 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-07-10", "lte": "2026-07-2…; interval=day | 1,710 | `92be82e858` | ok |
| 112 | 04:28:27 | C | Pronto | `searchSentences` | q="Bom Kim beneficially owns Class B voting power percent"; companiesIds=704377650; documentTypes=10-K; dateRange={"gte": "2021-01-01", "lte": "2024-… | 7,637 | `ece57bb874` | ok |
| 113 | 04:28:28 | Lead | Pronto | `getCompanies` | companiesIds=18749,34322384 (+14); size=20 | 10,259 | `e809cad2ac` | ok |
| 114 | 04:28:28 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-10-01", "lte": "2026-10-1…; interval=day | 1,096 | `7c5a69e256` | ok |
| 115 | 04:28:29 | Lead | Pronto | `getCompanyConsensus` | companiesIds=572577901,36273923 (+2); dateRange={"gte": "2026-01-01", "lte": "2026-08-3…; timeframeInterval=quarter; metrics=revenue | 2,504 | `260214c140` | ok |
| 116 | 04:28:29 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2025-10-31", "lte": "2025-11-0…; interval=day | 944 | `756876e760` | ok |
| 117 | 04:28:30 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2025-12-12", "lte": "2025-12-1…; interval=day | 942 | `2d8e3b3616` | ok |
| 118 | 04:28:30 | D | Pronto | `searchSentences` | q="adjusted EBITDA defined as net income excluding"; transcriptsIds=SEC000264559057,SEC000237408246 | 6,876 | `99e43c18e4` | ok |
| 119 | 04:28:30 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2025-09-05", "lte": "2025-09-1…; interval=day | 940 | `8a0449e43e` | ok |
| 120 | 04:28:31 | D | Pronto | `searchSentences` | q="valuation allowance release deferred tax assets Korea"; companiesIds=704377650; documentTypes=10-K | 15,641 | `3d39e8a16c` | ok |
| 121 | 04:28:33 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2024-02-23", "lte": "2024-03-0…; interval=day | 944 | `ca3f0ff516` | ok |
| 122 | 04:28:34 | A | Pronto | `searchSentences` | q="full year Product Commerce segment net revenues segment adjusted EBIT…"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2022-01-01… | 37,965 | `32f209cb1f` | ok |
| 123 | 04:28:34 | C | Pronto | `searchSentences` | q="SoftBank Vision Fund stake Coupang shares sale"; companiesIds=704377650 | 13,986 | `e624e6c48b` | ok |
| 124 | 04:28:34 | E | Pronto | `searchSentences` | q="administrative fines imposed Korean regulators"; transcriptsIds=SEC000264559057 | 8,173 | `7f4a96fe96` | ok |
| 125 | 04:28:34 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2024-04-05", "lte": "2024-04-1…; interval=day | 945 | `080e77670c` | ok |
| 126 | 04:28:34 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1905 (+2); before=7, after=7 | 7,931 | `99b4118bc1` | ok |
| 127 | 04:28:35 | C | Pronto | `searchSentences` | q="Bom Kim founded Coupang Harvard Business School"; companiesIds=704377650 | 14,830 | `c8a7a8857c` | ok |
| 128 | 04:28:35 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2024-08-02", "lte": "2024-08-0…; interval=day | 942 | `af6bb37b79` | ok |
| 129 | 04:28:35 | E | Pronto | `searchSentences` | q="revenue by geography Korea Taiwan other countries percentage"; transcriptsIds=SEC000264559057,SEC000255973354 | 7,499 | `da229c5482` | ok |
| 130 | 04:28:36 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2025-05-02", "lte": "2025-05-1…; interval=day | 1,703 | `9680ba54d6` | ok |
| 131 | 04:28:36 | E | Pronto | `getSentenceContext` | sentenceIds=T000003578475-141; before=0, after=10 | 1,430 | `7cd7728909` | ok |
| 132 | 04:28:37 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2022-05-06", "lte": "2022-05-1…; interval=day | 1,091 | `6542739bfb` | ok |
| 133 | 04:28:37 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2022-03-04", "lte": "2022-03-1…; interval=day | 1,704 | `baf10e1efa` | ok |
| 134 | 04:28:37 | A | Pronto | `readDocuments` | transcriptsIds=SEC000237406755; size=60 | 24,064 | `0a0276d2b8` | ok |
| 135 | 04:28:38 | D | Pronto | `searchSentences` | q="release of valuation allowance benefit to provision for income taxes"; companiesIds=704377650; documentTypes=10-K; dateRange={"gte": "2024-01-01",… | 6,410 | `a724651d74` | ok |
| 136 | 04:28:38 | A | Pronto | `readDocuments` | transcriptsIds=SEC000218768452; size=55 | 22,294 | `26f84449bf` | ok |
| 137 | 04:28:39 | A | Pronto | `readDocuments` | transcriptsIds=SEC000200362169; size=55 | 22,306 | `723bdbcf17` | ok |
| 138 | 04:28:39 | A | Pronto | `readDocuments` | transcriptsIds=SEC000177872792; size=60 | 24,735 | `22ae180a72` | ok |
| 139 | 04:28:39 | C | Pronto | `readDocuments` | companiesIds=704377650; sections=10Q_P2_I5,10K_P2_I9B (+1); size=300; excludeMetadata=false | 1,289 | `48f1322bb5` | ok |
| 140 | 04:28:40 | E | Pronto | `searchSentences` | q="Personal Information Protection Commission fine data incident amount"; transcriptsIds=SEC000264559057 | 7,493 | `58bbf50544` | ok |
| 141 | 04:28:40 | E | Pronto | `getCompanies` | companyNameOrTicker=NAVER; size=5 | 715 | `cb4afb0bd8` | ok |
| 142 | 04:28:41 | E | Pronto | `getCompanies` | companyNameOrTicker=E-MART; size=5 | 33 | `fb43fb2e12` | ok |
| 143 | 04:28:41 | B | Pronto | `getDocuments` | companiesIds=704377650; corpus=S&P Transcripts; size=50; excludeFutureDocuments=false | 12,534 | `870bd21480` | ok |
| 144 | 04:28:41 | D | Pronto | `searchSentences` | q="unrecognized compensation cost RSUs weighted average period"; transcriptsIds=SEC000255973354,SEC000264559057 | 11,058 | `12e98267bc` | ok |
| 145 | 04:28:43 | E | Pronto | `searchSentences` | q="Coupang competition e-commerce market share"; companiesIds=8708896 | 10,874 | `50d38a8876` | ok |
| 146 | 04:28:44 | A | Pronto | `searchSentences` | q="customer compensation program vouchers KRW trillion"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2025-11-01"} | 30,181 | `c8802884fe` | ok |
| 147 | 04:28:44 | E | Pronto | `searchSentences` | q="Naver Plus membership Kurly delivery partnership"; companiesIds=8708896 | 8,161 | `29627199b0` | ok |
| 148 | 04:28:44 | E | Pronto | `getCompanies` | companyNameOrTicker=Shinsegae; size=5 | 33 | `fb43fb2e12` | ok |
| 149 | 04:28:45 | A | Pronto | `searchSentences` | q="administrative fine Personal Information Protection Commission Fair T…"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2025-11-01… | 34,181 | `a8bad8496b` | ok |
| 150 | 04:28:45 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1886; before=6, after=6 | 2,499 | `bda95ba612` | ok |
| 151 | 04:28:46 | B | Pronto | `searchSentences` | q="gross profit margin pressure losses inflation Omicron labor costs"; transcriptsIds=T000002514904 | 6,223 | `6d3a38bcaa` | ok |
| 152 | 04:28:47 | D | Pronto | `searchSentences` | q="payment terms to suppliers regulation Large-Scale Retail Business Act…"; companiesIds=704377650; dateRange={"gte": "2025-01-01"} | 14,370 | `015ee9f7f8` | ok |
| 153 | 04:28:47 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000228328119-298; before=3, after=3 | 934 | `1c810ec299` | ok |
| 154 | 04:28:47 | B | Pronto | `searchSentences` | q="margin improvement adjusted EBITDA progress"; transcriptsIds=T000002563967 | 6,126 | `94a730e3a4` | ok |
| 155 | 04:28:48 | B | Pronto | `searchSentences` | q="adjusted EBITDA positive Product Commerce milestone"; transcriptsIds=T000002626640 | 6,075 | `343ef32b84` | ok |
| 156 | 04:28:48 | C | Pronto | `searchSentences` | q="repurchased shares private transaction from stockholder"; companiesIds=704377650; corpus=SEC Filings | 8,314 | `8624889493` | ok |
| 157 | 04:28:50 | A | Pronto | `searchSentences` | q="class action lawsuits filed related to the Incident"; transcriptsIds=SEC000264559057,SEC000255973354 | 30,844 | `4096c2bf0c` | ok |
| 158 | 04:28:50 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-619; before=5, after=3 | 1,706 | `a07e41b4b8` | ok |
| 159 | 04:28:51 | A | Pronto | `searchSentences` | q="chief executive officer resigned Coupang Corp interim"; companiesIds=704377650; dateRange={"gte": "2025-11-01"} | 23,067 | `6a18fba019` | ok |
| 160 | 04:28:51 | D | Pronto | `searchSentences` | q="material weakness internal control over financial reporting effective"; transcriptsIds=SEC000255973354,SEC000264559057 | 7,064 | `733c3a6558` | ok |
| 161 | 04:28:51 | E | Pronto | `searchSentences` | q="competitor data breach users switching commerce growth"; companiesIds=8708896; corpus=S&P Transcripts; dateRange={"gte": "2025-12-01"} | 9,848 | `4e8579f1d3` | ok |
| 162 | 04:28:52 | C | Pronto | `searchSentences` | q="year ended December 31, 2025 repurchased shares aggregate amount"; transcriptsIds=SEC000255973354 | 3,813 | `159e96a1da` | ok |
| 163 | 04:28:53 | E | Pronto | `searchSentences` | q="Shinsegae Gmarket joint venture Korea AliExpress"; companiesIds=42083601 | 8,156 | `ee96e33c68` | ok |
| 164 | 04:28:53 | E | Pronto | `getCompanies` | companyNameOrTicker=Emart; size=5 | 33 | `fb43fb2e12` | ok |
| 165 | 04:28:53 | C | Pronto | `searchSentences` | q="Farfetch acquisition Limited Partnership Greenoaks investment purchas…"; companiesIds=704377650; corpus=SEC Filings | 12,110 | `d6edf2de30` | ok |
| 166 | 04:28:54 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-1680; before=3, after=6 | 3,480 | `47e452c8d7` | ok |
| 167 | 04:28:54 | B | Pronto | `searchSentences` | q="WOW membership fee increase"; transcriptsIds=T000002514904,T000002563967 (+3) | 6,205 | `c5d8240b56` | ok |
| 168 | 04:28:55 | A | Pronto | `getDocuments` | companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2025-11-15", "lte": "2026-10-1…; size=30 | 4,465 | `09632d9c17` | ok |
| 169 | 04:28:55 | B | Pronto | `searchSentences` | q="Deokpyeong fulfillment center fire impact"; transcriptsIds=T000002374084 | 4,472 | `8d66cced6f` | ok |
| 170 | 04:28:55 | D | Pronto | `searchSentences` | q="Rule 10b5-1 trading arrangement adopted terminated director officer"; companiesIds=704377650; sections=10Q_P2_I5,10K_P2_I9B; dateRange={"gte": "20… | 10,026 | `3ef32209a4` | ok |
| 171 | 04:28:56 | B | Pronto | `searchSentences` | q="Japan exit wind down operations"; companiesIds=704377650; dateRange={"gte": "2021-01-01", "lte": "2024-12-3… | 5,750 | `ad27609714` | ok |
| 172 | 04:28:56 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-2050 (+1); before=3, after=6 | 4,044 | `6bee212b76` | ok |
| 173 | 04:28:57 | E | Pronto | `getSentenceContext` | sentenceIds=T000003646016-298; before=6, after=6 | 1,742 | `3472f4b37b` | ok |
| 174 | 04:28:57 | A | Pronto | `readDocuments` | transcriptsIds=SEC000253203320,SEC000255152730 (+1); size=80 | 15,886 | `7b67ac4b87` | ok |
| 175 | 04:28:59 | E | Pronto | `searchSentences` | q="Gmarket Shinsegae Alibaba joint venture Korea"; corpus=S&P Transcripts,Non-SEC Filings (+1); numberOfCompanies=20 | 62 | `135035901f` | error |
| 176 | 04:28:59 | D | Pronto | `searchSentences` | q="lawsuits filed in Korea by customers damages Incident"; transcriptsIds=SEC000255973354,SEC000264559057 (+1) | 11,503 | `75725bdad3` | ok |
| 177 | 04:29:00 | E | Pronto | `searchSentences` | q="Coupang share of Korean e-commerce market"; corpus=S&P Transcripts,Non-SEC Filings (+1); numberOfCompanies=20 | 62 | `135035901f` | error |
| 178 | 04:29:00 | C | Pronto | `searchSentences` | q="Farfetch acquisition $500 million capital commitment"; companiesIds=704377650; corpus=S&P Transcripts | 6,252 | `69cc26e252` | ok |
| 179 | 04:29:01 | A | Pronto | `searchSentences` | q="voucher won per customer compensation trillion won"; companiesIds=704377650; dateRange={"gte": "2025-11-15"} | 19,176 | `d05be7309f` | ok |
| 180 | 04:29:01 | C | Pronto | `searchSentences` | q="return on invested capital discipline capital allocation"; companiesIds=704377650; corpus=S&P Transcripts | 7,842 | `b8b4dbee40` | ok |
| 181 | 04:29:02 | D | Pronto | `getSentenceContext` | sentenceIds=SEC000259645823-550; before=3, after=8 | 187 | `d11b41ba0f` | ok |
| 182 | 04:29:02 | B | Pronto | `searchSentences` | q="IPO closed shares sold net proceeds initial public offering price per…"; transcriptsIds=SEC000177952319 | 6,286 | `6ed92254a8` | ok |
| 183 | 04:29:03 | C | Pronto | `searchSentences` | q="Taiwan investment losses developing offerings"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2025-01-01", "lte": "now"} | 6,371 | `4588c00f71` | ok |
| 184 | 04:29:03 | B | Pronto | `searchSentences` | q="fulfillment center fire June 2021 losses insurance"; transcriptsIds=SEC000177952319 | 4,538 | `6af0efd7ed` | ok |
| 185 | 04:29:03 | D | Pronto | `searchSentences` | q="labor union workers delivery drivers employment lawsuit Serious Accid…"; transcriptsIds=SEC000255973354,SEC000264559057 | 11,130 | `2356e60742` | ok |
| 186 | 04:29:04 | B | Pronto | `searchSentences` | q="company history founded 2010 Rocket Delivery launched 2014"; companiesIds=704377650; corpus=SEC Filings | 6,520 | `37f29f1e9d` | ok |
| 187 | 04:29:04 | A | Pronto | `readDocuments` | transcriptsIds=SEC000264557825; size=45 | 22,096 | `b05becfc70` | ok |
| 188 | 04:29:07 | D | Pronto | `searchSentences` | q="impairment charges restructuring Farfetch gain on sale divestiture"; transcriptsIds=SEC000255973354 | 12,199 | `413428c366` | ok |
| 189 | 04:29:07 | A | Pronto | `searchSentences` | q="cash and cash equivalents capital expenditures borrowings liquidity"; transcriptsIds=SEC000264559057 | 23,194 | `9f0f33b51d` | ok |
| 190 | 04:29:08 | C | Pronto | `searchSentences` | q="Farfetch transaction investment amount return"; companiesIds=704377650; dateRange={"gte": "2023-12-01", "lte": "2024-06-3… | 7,563 | `0e4de9ce06` | ok |
| 191 | 04:29:09 | A | Pronto | `searchSentences` | q="inventories accounts payable working capital Incheon fire"; transcriptsIds=SEC000264559057 | 23,307 | `2c41391cb6` | ok |
| 192 | 04:29:10 | A | Pronto | `searchSentences` | q="foreign exchange impact KRW weakened revenue growth"; transcriptsIds=SEC000264559057,SEC000259645823 (+1) | 16,300 | `2bdee3f295` | ok |
| 193 | 04:29:10 | C | Pronto | `searchSentences` | q="2026 developing offerings losses guidance Taiwan Eats Farfetch"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2026-02-01", "… | 6,382 | `d153802907` | ok |
| 194 | 04:29:11 | B | Pronto | `searchSentences` | q="SoftBank Vision Fund ownership principal stockholder"; companiesIds=704377650; corpus=SEC Filings | 5,742 | `43a311d225` | ok |
| 195 | 04:29:11 | D | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=cashflow; period_type=annual; start_year=2021; end_year=2025 | 12,675 | `f3d7de5433` | ok |
| 196 | 04:29:12 | B | Pronto | `searchSentences` | q="Rocket Now Japan launch on-demand delivery"; companiesIds=704377650 | 6,249 | `766c0ac32f` | ok |
| 197 | 04:29:13 | B | Pronto | `searchSentences` | q="founded in 2010 Bom Kim founder"; companiesIds=704377650 | 4,092 | `6e9c02647c` | ok |
| 198 | 04:29:14 | A | Pronto | `getAnalytics` | transcriptsIds=T000003779883; analyticsType=eventTypes,aspects (+1) | 21,064 | `4970fa3f38` | ok |
| 199 | 04:29:15 | D | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=cashflow; period_type=quarterly; num_periods=6 | 13,260 | `172211ee6c` | ok |
| 200 | 04:29:15 | C | Pronto | `getSentenceContext` | sentenceIds=T000003041770-213; before=0, after=10 | 1,194 | `bd1c636ce2` | ok |
| 201 | 04:29:15 | A | Pronto | `getAnalytics` | transcriptsIds=T000003711263; analyticsType=eventTypes,aspects (+1) | 19,927 | `f0af87b5a8` | ok |
| 202 | 04:29:16 | A | Pronto | `getAnalytics` | transcriptsIds=T000003665452; analyticsType=eventTypes,aspects (+1) | 19,403 | `7138dedd22` | ok |
| 203 | 04:29:16 | C | Pronto | `searchSentences` | q="data incident customer compensation voucher apology CEO responsibility"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2025-1… | 7,668 | `9b00ecc9b5` | ok |
| 204 | 04:29:17 | D | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=balance_sheet; period_type=quarterly; num_periods=3 | 8,672 | `7325dce2c4` | ok |
| 205 | 04:29:20 | D | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=income_statement; period_type=annual; start_year=2023; end_year=2025 | 7,245 | `32c56f3691` | ok |
| 206 | 04:29:20 | C | Pronto | `getSpeakers` | companiesIds=704377650; speakerCompaniesIds=704377650; entityType=speaker; dateRange={"gte": "2021-01-01", "lte": "now"}; size=25 | 2,012 | `3ca2d4ebf2` | ok |
| 207 | 04:29:20 | B | Pronto | `searchSentences` | q="Developing Offerings adjusted EBITDA losses guidance increased invest…"; transcriptsIds=T000003578475 | 6,102 | `4a5bc06f96` | ok |
| 208 | 04:29:21 | A | Pronto | `getAnalytics` | transcriptsIds=T000003578475; analyticsType=eventTypes,aspects (+1) | 18,212 | `3c339920c8` | ok |
| 209 | 04:29:22 | B | Pronto | `searchSentences` | q="July 2026 events regulatory order investigation lawsuit"; transcriptsIds=SEC000264559057 | 9,424 | `dfa15d5f4f` | ok |
| 210 | 04:29:22 | A | Pronto | `getAnalytics` | transcriptsIds=T000003384178; analyticsType=eventTypes,patternSentiment | 19,108 | `a941f85b2c` | ok |
| 211 | 04:29:23 | A | Pronto | `getAnalytics` | transcriptsIds=T000003299355; analyticsType=eventTypes,patternSentiment | 17,738 | `826f023d91` | ok |
| 212 | 04:29:23 | B | Pronto | `searchSentences` | q="revenue growth outlook net revenue decline operating loss data incide…"; transcriptsIds=T000003779883 | 8,661 | `a48f3ca201` | ok |
| 213 | 04:29:23 | D | S&P | `get_financial_statement_from_identifiers` | ids=CPNG; statement=income_statement; period_type=quarterly; num_periods=4 | 8,530 | `80ea127a3d` | ok |
| 214 | 04:29:26 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=weighted_average_diluted_shares_outstanding; period_type=annual; start_year=2021; end_year=2025 | 2,450 | `969d7f8d79` | ok |
| 215 | 04:29:27 | C | Pronto | `searchSentences` | q="executive officer served as Chief Financial Officer since prior exper…"; companiesIds=704377650; corpus=SEC Filings | 8,236 | `7e952da476` | ok |
| 216 | 04:29:27 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=common_shares_outstanding; period_type=quarterly; num_periods=6 | 505 | `0e4a01e315` | ok |
| 217 | 04:29:27 | B | Pronto | `searchSentences` | q="fire at fulfillment center 2026"; transcriptsIds=T000003779883,SEC000264559057 (+1) | 20,462 | `4c5394edbb` | ok |
| 218 | 04:29:28 | A | Pronto | `searchSentences` | q="WOW membership fee price increase 7,890 won"; companiesIds=704377650 | 14,839 | `9f43c0f5cc` | ok |
| 219 | 04:29:28 | C | Pronto | `searchSentences` | q="Hanseung Kang Park Dae-jun chief executive officer Coupang Corp resig…"; companiesIds=704377650 | 9,890 | `f5ac9d760a` | ok |
| 220 | 04:29:29 | A | Pronto | `searchSentences` | q="square feet of fulfillment and logistics infrastructure"; companiesIds=704377650 | 14,597 | `122b0d1976` | ok |
| 221 | 04:29:30 | A | Pronto | `searchSentences` | q="by 2027 population within 10 kilometers of Coupang logistics center"; companiesIds=704377650 | 10,982 | `27f3f17f02` | ok |
| 222 | 04:29:31 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=stock_based_compensation; period_type=annual; start_year=2021; end_year=2025 | 2,370 | `4dffae4ad1` | ok |
| 223 | 04:29:33 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=cash_from_operations; period_type=annual; start_year=2021; end_year=2025 | 2,333 | `c2776e49be` | ok |
| 224 | 04:29:34 | B | Pronto | `searchSentences` | q="WOW membership price adjustment new members existing members August"; transcriptsIds=T000003113152,T000003215027 | 12,438 | `2350ff119e` | ok |
| 225 | 04:29:34 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=capital_expenditure; period_type=annual; start_year=2021; end_year=2025 | 2,332 | `0a048bc826` | ok |
| 226 | 04:29:35 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=net_income; period_type=annual; start_year=2021; end_year=2025 | 2,316 | `4c0fd8ab84` | ok |
| 227 | 04:29:35 | A | Pronto | `searchSentences` | q="WOW membership price change members fee"; companiesIds=704377650; dateRange={"gte": "2024-01-01", "lte": "2025-06-3… | 14,494 | `2465a7683f` | ok |
| 228 | 04:29:35 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000255973354-2080; before=10, after=10 | 5,734 | `d0e66f2169` | ok |
| 229 | 04:29:36 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=income_tax_expense; period_type=annual; start_year=2021; end_year=2025 | 2,272 | `fe6ed16625` | ok |
| 230 | 04:29:37 | C | Pronto | `searchSentences` | q="Director signature Board of Directors"; transcriptsIds=SEC000177952319,SEC000200458327 (+2); sections=10K_P4_I15 | 19 | `11699945fc` | ok |
| 231 | 04:29:37 | A | Pronto | `searchSentences` | q="expand Rocket Delivery nationwide by 2027 investment 3 trillion won r…"; companiesIds=704377650; dateRange={"gte": "2023-06-01", "lte": "2025-12-3… | 15,788 | `20e6e0c6f5` | ok |
| 232 | 04:29:37 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=interest_expense; period_type=annual; start_year=2021; end_year=2025 | 2,342 | `70618db6c9` | ok |
| 233 | 04:29:38 | A | Pronto | `searchSentences` | q="total square footage of facilities properties leased owned"; transcriptsIds=SEC000255973354,SEC000237408246 | 10,908 | `2fa085b473` | ok |
| 234 | 04:29:39 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=insurance_settlements; period_type=annual; start_year=2023; end_year=2025 | 1,170 | `b9aee9a3fc` | ok |
| 235 | 04:29:39 | B | Pronto | `searchSentences` | q="full year net income revenue growth record results Farfetch rationale"; transcriptsIds=T000003041770 | 6,270 | `6a8d0abc8c` | ok |
| 236 | 04:29:39 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=repurchase_of_common_stock; period_type=quarterly; num_periods=6 | 1,726 | `76df2189a8` | ok |
| 237 | 04:29:40 | B | Pronto | `searchSentences` | q="revenue growth constant currency adjusted EBITDA margin record quarter"; transcriptsIds=T000003215027 | 4,599 | `4e27f13c1f` | ok |
| 238 | 04:29:41 | B | Pronto | `searchSentences` | q="record adjusted EBITDA margin revenue growth constant currency"; transcriptsIds=T000003441812 | 4,687 | `da81857182` | ok |
| 239 | 04:29:41 | C | Pronto | `searchSentences` | q="tax equalization housing allowance assignment benefits"; companiesIds=704377650; corpus=SEC Filings | 7,596 | `a8e21d3462` | ok |
| 240 | 04:29:43 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=cash_from_operations; period_type=quarterly; num_periods=6 | 2,256 | `17fbbbb61c` | ok |
| 241 | 04:29:43 | C | Pronto | `searchSentences` | q="signature Director Chief Executive Officer and Chairman of the Board"; transcriptsIds=SEC000177952319,SEC000200458327 (+2) | 9,646 | `6e22c4f310` | ok |
| 242 | 04:29:44 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=capital_expenditure; period_type=quarterly; num_periods=6 | 2,259 | `9d6bb24235` | ok |
| 243 | 04:29:45 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=total_debt_issued; period_type=quarterly; num_periods=6 | 2,243 | `dfdde99c54` | ok |
| 244 | 04:29:45 | A | Pronto | `getSentenceContext` | sentenceIds=T000003215027-261 (+1); before=4, after=8 | 3,143 | `6c2b1b363d` | ok |
| 245 | 04:29:46 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=total_debt_repaid; period_type=quarterly; num_periods=6 | 2,251 | `f7a0d61922` | ok |
| 246 | 04:29:47 | A | Pronto | `searchSentences` | q="Korean population lives within miles of our logistics centers"; companiesIds=704377650; corpus=SEC Filings | 7,516 | `5406e0b26d` | ok |
| 247 | 04:29:47 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=short_term_borrowings; period_type=quarterly; num_periods=6 | 2,332 | `363e007146` | ok |
| 248 | 04:29:47 | B | Pronto | `searchSentences` | q="impact of data incident on customers growth outlook 2026"; transcriptsIds=T000003665452 | 8,131 | `753ca5e3ea` | ok |
| 249 | 04:29:48 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000251149107-546; before=10, after=6 | 3,747 | `25b72367ff` | ok |
| 250 | 04:29:48 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=stock_based_compensation; period_type=quarterly; num_periods=6 | 2,311 | `431685cd5b` | ok |
| 251 | 04:29:49 | B | Pronto | `searchSentences` | q="net revenues growth decline first quarter results data incident"; transcriptsIds=SEC000259644607 | 9,792 | `c8885800b7` | ok |
| 252 | 04:29:51 | C | Pronto | `searchSentences` | q="Letter of Assignment signature executive name title"; transcriptsIds=SEC000251149107; sections=10Q_Exhibit,10Q_P2_I6 | 8,746 | `4c91adda98` | ok |
| 253 | 04:29:52 | A | Pronto | `searchSentences` | q="long-term free cash flow return on invested capital principles"; companiesIds=704377650 | 9,948 | `116ff1f670` | ok |
| 254 | 04:29:52 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=inventory; period_type=annual; start_year=2022; end_year=2025 | 1,996 | `371a70648c` | ok |
| 255 | 04:29:53 | B | Pronto | `readDocuments` | transcriptsIds=SEC000259644607; size=30 | 11,800 | `189610c652` | ok |
| 256 | 04:29:53 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=accounts_payable; period_type=annual; start_year=2022; end_year=2025 | 2,052 | `113b34e8dd` | ok |
| 257 | 04:29:54 | B | Pronto | `readDocuments` | transcriptsIds=SEC000264557825; size=30 | 11,918 | `80af37b431` | ok |
| 258 | 04:29:54 | B | Pronto | `readDocuments` | transcriptsIds=SEC000251144139; size=25 | 9,720 | `11a3b5bd5d` | ok |
| 259 | 04:29:54 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=cost_of_revenue; period_type=annual; start_year=2022; end_year=2025 | 2,036 | `97c4bbbfef` | ok |
| 260 | 04:29:55 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=accounts_receivable; period_type=annual; start_year=2022; end_year=2025 | 2,056 | `99f3750645` | ok |
| 261 | 04:29:57 | C | Pronto | `readDocuments` | transcriptsIds=SEC000251149107,SEC000255973354 (+3); sections=10Q_Exhibit,10K_Exhibit; size=500; excludeMetadata=false | 1,291 | `4d4a2cc1b6` | ok |
| 262 | 04:29:57 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=total_revenue; period_type=annual; start_year=2022; end_year=2025 | 2,028 | `3cf917eccc` | ok |
| 263 | 04:29:57 | A | Pronto | `searchSentences` | q="full year 2021 net revenues growth adjusted EBITDA loss"; transcriptsIds=T000002514904 | 8,961 | `4de1546705` | ok |
| 264 | 04:29:57 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=long_term_debt; period_type=quarterly; num_periods=6 | 2,286 | `552226db64` | ok |
| 265 | 04:30:01 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=cash_and_equivalents; period_type=quarterly; num_periods=3 | 1,455 | `80969178c8` | ok |
| 266 | 04:30:02 | B | Pronto | `searchSentences` | q="repurchased shares retired treasury stock"; companiesIds=704377650; corpus=SEC Filings; dateRange={"gte": "2024-01-01", "lte": "now"} | 5,747 | `5817ed2824` | ok |
| 267 | 04:30:02 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=long_term_leases; period_type=quarterly; num_periods=3 | 1,443 | `6776674a63` | ok |
| 268 | 04:30:03 | B | Pronto | `searchSentences` | q="never declared or paid cash dividends"; transcriptsIds=SEC000255973354 | 3,380 | `1c3cc465f2` | ok |
| 269 | 04:30:03 | E | Pronto | `searchSentences` | q="e-commerce competition Coupang Lotte ON market share"; companiesIds=5466913 | 7,284 | `caa08dd351` | ok |
| 270 | 04:30:03 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=current_portion_of_leases; period_type=quarterly; num_periods=3 | 1,465 | `d873e03f60` | ok |
| 271 | 04:30:04 | B | Pronto | `searchSentences` | q="delivery workers labor union working conditions deaths night shift re…"; companiesIds=704377650 | 7,185 | `bb9613c79a` | ok |
| 272 | 04:30:04 | E | Pronto | `searchSentences` | q="small share of total retail market room to grow"; companiesIds=704377650; corpus=S&P Transcripts | 9,473 | `36cadb08c0` | ok |
| 273 | 04:30:05 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=goodwill; period_type=annual; start_year=2023; end_year=2025 | 784 | `ee0dd98138` | ok |
| 274 | 04:30:05 | C | Pronto | `searchSentences` | q="insider trading policy prohibits hedging pledging short sales"; companiesIds=704377650; corpus=SEC Filings | 5,943 | `02d5a2e5bd` | ok |
| 275 | 04:30:05 | E | Pronto | `searchSentences` | q="hypermarket early morning delivery regulation Kurly partnership impact"; companiesIds=8708896 | 6,203 | `25b1d56553` | ok |
| 276 | 04:30:06 | D | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=accrued_expenses; period_type=quarterly; num_periods=3 | 1,459 | `e601974d3b` | ok |
| 277 | 04:30:06 | C | Pronto | `searchSentences` | q="Letter of Interim Assignment Hanseung Kang Coupang Corp chief executi…"; transcriptsIds=SEC000251149107 | 10,503 | `39abdac268` | ok |
| 278 | 04:30:08 | B | Pronto | `searchSentences` | q="platform regulation act Korea online platforms payment settlement per…"; companiesIds=704377650; dateRange={"gte": "2024-06-01", "lte": "now"} | 5,290 | `4016b4ace5` | ok |
| 279 | 04:30:09 | D | Pronto | `searchSentences` | q="goodwill balance impairment test reporting unit"; transcriptsIds=SEC000255973354,SEC000237408246 | 7,272 | `65c0cc11eb` | ok |
| 280 | 04:30:10 | B | Pronto | `searchSentences` | q="TMON Wemakeprice collapse Korean e-commerce"; numberOfCompanies=30 | 6,380 | `eed74bc13c` | ok |
| 281 | 04:30:10 | B | Pronto | `searchSentences` | q="Gmarket AliExpress joint venture Shinsegae Alibaba"; numberOfCompanies=30 | 5,950 | `25e18ed522` | ok |
| 282 | 04:30:14 | C | Pronto | `searchSentences` | q="Kevin Warsh director resignation Federal Reserve"; companiesIds=704377650; dateRange={"gte": "2026-02-07", "lte": "now"} | 783 | `26e642905a` | ok |
| 283 | 04:30:15 | C | S&P | `get_info_from_identifiers` | ids=CPNG | 411 | `79d0b38fe3` | ok |
| 284 | 04:30:16 | C | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=repurchase_of_common_stock; period_type=annual; num_periods=5 | 1,474 | `653e322bde` | ok |
| 285 | 04:30:17 | C | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=common_shares_outstanding; period_type=quarterly; num_periods=4 | 505 | `0e4a01e315` | ok |
| 286 | 04:30:20 | E | Pronto | `searchSentences` | q="Poshmark acquisition consideration"; companiesIds=8708896 | 4,442 | `74e43d8347` | ok |
| 287 | 04:30:21 | D | Pronto | `searchSentences` | q="settlement period shortening merchant payment impact working capital"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2025-06-… | 8,850 | `e2171cbb62` | ok |
| 288 | 04:30:21 | E | Pronto | `searchSentences` | q="Farfetch acquisition purchase consideration loan bargain purchase"; transcriptsIds=SEC000255973354 | 6,240 | `d3f3b149a9` | ok |
| 289 | 04:30:22 | E | Pronto | `searchSentences` | q="supplier finance program payment terms days"; transcriptsIds=SEC000255973354 | 5,899 | `7651b6ee02` | ok |
| 290 | 04:30:23 | E | Pronto | `searchSentences` | q="Korean economy consumer spending minimum wage interest rates demograp…"; transcriptsIds=SEC000255973354 | 8,044 | `c7511e5b38` | ok |
| 291 | 04:30:32 | C | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=net_income; period_type=annual; num_periods=5 | 2,316 | `4c0fd8ab84` | ok |
| 292 | 04:30:33 | C | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=total_equity; period_type=annual; num_periods=5 | 2,180 | `2923e51019` | ok |
| 293 | 04:30:34 | C | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=weighted_average_diluted_shares_outstanding; period_type=annual; num_periods=5 | 2,450 | `969d7f8d79` | ok |
| 294 | 04:30:35 | D | Pronto | `searchSentences` | q="voucher redemption impact on revenue and gross margin"; companiesIds=704377650; dateRange={"gte": "2026-01-01"} | 9,067 | `35f97af3c2` | ok |
| 295 | 04:30:36 | E | Pronto | `searchSentences` | q="night delivery dawn delivery worker labor regulation"; companiesIds=704377650; dateRange={"gte": "2025-06-01"} | 7,661 | `d2925ea3d0` | ok |
| 296 | 04:30:38 | E | Pronto | `searchSentences` | q="Eats food delivery competition Baemin market"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2025-01-01"} | 6,370 | `ad38b7df5b` | ok |
| 297 | 04:30:38 | D | Pronto | `getSentenceContext` | sentenceIds=T000003711263-213; before=5, after=4 | 859 | `11f736de3b` | ok |
| 298 | 04:30:39 | B | Pronto | `searchSentences` | q="competition AliExpress Temu Chinese cross-border platforms Naver Gmar…"; companiesIds=704377650; corpus=S&P Transcripts | 8,042 | `0637e34440` | ok |
| 299 | 04:30:39 | C | Pronto | `searchSentences` | q="interim chief executive officer Korean subsidiary Harold Rogers Natio…"; companiesIds=704377650; dateRange={"gte": "2025-12-01", "lte": "now"} | 9,522 | `0bc6848e1d` | ok |
| 300 | 04:30:39 | E | Pronto | `searchSentences` | q="advertising revenue merchants advertisers sellers commissions"; transcriptsIds=SEC000255973354 | 5,784 | `d7ed25b4d6` | ok |
| 301 | 04:30:40 | C | Pronto | `searchSentences` | q="Eats investment Coupang Eats growth profitability"; companiesIds=704377650; corpus=S&P Transcripts | 3,925 | `2a222823a2` | ok |
| 302 | 04:30:45 | E | Pronto | `searchSentences` | q="Korea e-commerce market share Coupang Naver"; dateRange={"gte": "2025-01-01"}; numberOfCompanies=8 | 6,349 | `1b3b67b7aa` | ok |
| 303 | 04:30:46 | C | Pronto | `searchSentences` | q="customer vouchers compensation amount billion won data incident cost"; companiesIds=704377650; dateRange={"gte": "2025-12-01", "lte": "now"} | 4,526 | `107637a302` | ok |
| 304 | 04:30:46 | B | Pronto | `searchSentences` | q="Rocket Growth launched merchants fulfillment service growth"; companiesIds=704377650; corpus=S&P Transcripts | 6,097 | `087d265c24` | ok |
| 305 | 04:30:47 | B | Pronto | `searchSentences` | q="Farfetch adjusted EBITDA positive breakeven turnaround"; companiesIds=704377650; corpus=S&P Transcripts | 6,071 | `7bc841651f` | ok |
| 306 | 04:30:49 | B | Pronto | `searchSentences` | q="Coupang Play streaming content sports launched"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2021-01-01", "lte": "2023-12-3… | 4,800 | `39052c8db7` | ok |
| 307 | 04:30:49 | C | Pronto | `getSentenceContext` | sentenceIds=SEC000264559057-397; before=0, after=10 | 2,370 | `726b4f79ed` | ok |
| 308 | 04:30:55 | B | Pronto | `searchSentences` | q="launched in Japan and Taiwan international expansion pilot"; companiesIds=704377650; dateRange={"gte": "2021-01-01", "lte": "2023-06-3… | 6,100 | `c7b30a6039` | ok |
| 309 | 04:30:56 | E | Pronto | `searchSentences` | q="online channel e-commerce platforms Coupang sales"; companiesIds=43003211; dateRange={"gte": "2024-01-01"} | 6,143 | `7e9d845f13` | ok |
| 310 | 04:30:56 | B | Pronto | `searchSentences` | q="advertising revenue growth retail media ads"; companiesIds=704377650; corpus=S&P Transcripts | 3,746 | `2984391992` | ok |
| 311 | 04:30:57 | B | Pronto | `searchSentences` | q="Coupang Pay fintech credit lending travel offering"; companiesIds=704377650 | 6,541 | `9e3e9e7228` | ok |
| 312 | 04:31:06 | B | Pronto | `searchSentences` | q="securities class action IPO registration statement dismissed appeal N…"; transcriptsIds=SEC000264559057 | 7,026 | `14e7e1ae81` | ok |
| 313 | 04:31:06 | D | Pronto | `searchSentences` | q="KFTC administrative fine excluded from adjusted EBITDA"; transcriptsIds=SEC000237408246,SEC000228328119 | 5,796 | `3e3ab020de` | ok |
| 314 | 04:31:07 | B | Pronto | `searchSentences` | q="administrative litigation KFTC fine appeal Seoul High Court private l…"; transcriptsIds=SEC000264559057 | 7,546 | `3e1385cd4e` | ok |
| 315 | 04:31:08 | B | Pronto | `searchSentences` | q="total purchase consideration Farfetch goodwill fair value amount mill…"; transcriptsIds=SEC000237408246 | 6,341 | `e5e8a2d939` | ok |
| 316 | 04:31:12 | B | Pronto | `getSentenceContext` | sentenceIds=T000003578475-98; before=0, after=3 | 639 | `4655de2c5b` | ok |
| 317 | 04:31:22 | B | Pronto | `searchSentences` | q="Korean government investigations National Assembly prosecution referr…"; transcriptsIds=SEC000255973354 | 9,213 | `f081f401b2` | ok |
| 318 | 04:31:23 | B | Pronto | `searchSentences` | q="full year 2022 results revenue growth first positive adjusted EBITDA …"; transcriptsIds=T000002753730 | 4,198 | `d5d4b0c204` | ok |
| 319 | 04:31:29 | B | Pronto | `searchSentences` | q="new chief executive officer Coupang Corp appointed Korea leadership"; companiesIds=704377650; dateRange={"gte": "2025-12-01", "lte": "now"} | 7,988 | `066b61fd61` | ok |
| 320 | 04:31:31 | B | Pronto | `searchSentences` | q="AI artificial intelligence automation investments GPU cloud"; companiesIds=704377650; corpus=S&P Transcripts; dateRange={"gte": "2025-06-01", "lte… | 6,295 | `177372f276` | ok |
| 321 | 04:31:37 | B | Pronto | `searchSentences` | q="business combination acquired company purchase consideration equity m…"; transcriptsIds=SEC000177952319,SEC000200458327 (+1) | 8,396 | `323017000c` | ok |
| 322 | 04:31:42 | B | S&P | `get_info_from_identifiers` | ids=CPNG | 411 | `79d0b38fe3` | ok |
| 323 | 04:31:42 | B | S&P | `get_history_metadata_from_identifiers` | ids=CPNG | 214 | `bc90d6edbb` | ok |
| 324 | 04:31:43 | B | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=repurchase_of_common_stock; period_type=annual; start_year=2020; end_year=2025 | 1,769 | `04b20a54cd` | ok |
| 325 | 04:31:44 | B | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=dividends_paid; period_type=annual; start_year=2020; end_year=2025 | 784 | `ee0dd98138` | ok |
| 326 | 04:31:48 | B | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=repurchase_of_common_stock; period_type=quarterly; num_periods=6 | 1,726 | `76df2189a8` | ok |
| 327 | 04:31:49 | B | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=common_shares_outstanding; period_type=quarterly; num_periods=6 | 505 | `0e4a01e315` | ok |
| 328 | 04:31:50 | B | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=treasury_stock; period_type=quarterly; num_periods=6 | 505 | `0e4a01e315` | ok |
| 329 | 04:31:53 | B | Pronto | `searchSentences` | q="repurchased shares retired upon repurchase excess over par value accu…"; transcriptsIds=SEC000255973354,SEC000264559057 | 4,749 | `57100b72a3` | ok |
| 330 | 04:31:54 | B | Pronto | `searchSentences` | q="shares of Class A and Class B common stock outstanding as of"; transcriptsIds=SEC000264559057 | 2,934 | `39a02499e6` | ok |
| 331 | 04:32:04 | B | Pronto | `getSentenceContext` | sentenceIds=SEC000264559057-147 (+1); before=3, after=1 | 2,295 | `0c5ad4afdf` | ok |
| 332 | 04:32:04 | B | Pronto | `searchSentences` | q="second quarter outlook guidance revenue growth margin expectations"; transcriptsIds=T000003711263 | 6,084 | `2f5a63bd4e` | ok |
| 333 | 04:32:24 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2022-02-25", "lte": "2022-03-0…; interval=day | 941 | `7a6cea6430` | ok |
| 334 | 04:32:25 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2021-08-06", "lte": "2021-08-1…; interval=day | 941 | `7df6474d53` | ok |
| 335 | 04:32:26 | B | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2021-03-10", "lte": "2021-03-1…; interval=day | 1,090 | `9d5359411f` | ok |
| 336 | 04:32:27 | B | Pronto | `searchSentences` | q="net loss fire related losses inventory write-off quarter"; transcriptsIds=T000002374084 | 4,578 | `f55afc212d` | ok |
| 337 | 04:32:33 | B | Pronto | `searchSentences` | q="material weakness internal control over financial reporting"; transcriptsIds=SEC000177952319 | 4,267 | `25e29b4984` | ok |
| 338 | 04:32:34 | B | Pronto | `searchSentences` | q="first quarter 2022 outlook gross margin adjusted EBITDA guidance grow…"; transcriptsIds=T000002514904 | 4,433 | `00c9a7a91e` | ok |
| 339 | 04:32:37 | B | Pronto | `getSentenceContext` | sentenceIds=SEC000177952319-1671; before=4, after=3 | 1,605 | `9a15bbf70c` | ok |
| 340 | 04:32:42 | Lead | Pronto | `getStockPrices` | companiesIds=18749,34322384 (+6); dateRange={"gte": "2021-12-01", "lte": "2025-12-3…; interval=quarter | 21,659 | `5ed53f68ce` | ok |
| 341 | 04:32:42 | B | Pronto | `searchSentences` | q="lock-up agreements expiration shares eligible for sale"; transcriptsIds=SEC000177952319 | 3,948 | `c46e86cc27` | ok |
| 342 | 04:32:43 | B | Pronto | `searchSentences` | q="third quarter guidance revenue growth Q3 outlook"; transcriptsIds=T000003779883 | 4,723 | `405ba4127a` | ok |
| 343 | 04:32:43 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=AMZN,MELI,SE (+4); line_item=revenue; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 12,893 | `ce22bda2a1` | ok |
| 344 | 04:32:45 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=AMZN,MELI,SE (+4); line_item=net_debt; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 11,862 | `436daace7a` | ok |
| 345 | 04:32:46 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=AMZN,MELI,SE (+4); line_item=weighted_average_diluted_shares_outstanding; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 13,688 | `42d64569a0` | ok |
| 346 | 04:33:47 | B | Pronto | `searchSentences` | q="net loss widened COVID costs labor shortage investments adjusted EBIT…"; transcriptsIds=T000002437086 | 4,593 | `3877436fbd` | ok |
| 347 | 04:33:48 | B | Pronto | `searchSentences` | q="results quarter revenue growth adjusted EBITDA net income"; transcriptsIds=T000002682334 | 3,762 | `45623af60b` | ok |
| 348 | 04:37:02 | Lead | Pronto | `getCompanies` | companyNameOrTicker=DoorDash; size=3 | 740 | `49ee7273b3` | ok |
| 349 | 04:37:02 | Lead | Pronto | `getCompanies` | companyNameOrTicker=Uber Technologies; size=3 | 732 | `8835658fae` | ok |
| 350 | 04:37:03 | Lead | Pronto | `getCompanies` | companyNameOrTicker=Poshmark; size=3 | 702 | `549cd7a056` | ok |
| 351 | 04:37:03 | Lead | Pronto | `getCompanies` | companyNameOrTicker=Delivery Hero; size=3 | 738 | `b043e50cad` | ok |
| 352 | 04:37:07 | Lead | Pronto | `searchSentences` | q="acquisition of Deliveroo purchase price per share"; companiesIds=243735719; dateRange={"gte": "2025-04-01", "lte": "now"} | 16,226 | `a99d1fe70c` | ok |
| 353 | 04:37:08 | Lead | Pronto | `searchSentences` | q="Foodpanda Taiwan acquisition purchase price terminated"; companiesIds=144524848; dateRange={"gte": "2024-04-01", "lte": "now"} | 17,212 | `34e8e6f7a7` | ok |
| 354 | 04:37:09 | Lead | Pronto | `searchSentences` | q="merger agreement NAVER acquire Poshmark per share cash consideration"; companiesIds=144130423 | 33 | `25e43ca357` | ok |
| 355 | 04:37:10 | Lead | Pronto | `searchSentences` | q="sale of Yogiyo proceeds"; companiesIds=140687018 | 14,273 | `d2266363cc` | ok |
| 356 | 04:37:24 | Lead | Pronto | `searchSentences` | q="offer price per Delivery Hero share cash tender offer"; companiesIds=144524848; dateRange={"gte": "2026-06-01", "lte": "now"} | 17,166 | `7731e8fdf2` | ok |
| 357 | 04:37:24 | Lead | Pronto | `getCompanies` | companyNameOrTicker=Prosus; size=2 | 708 | `0307e17ccd` | ok |
| 358 | 04:37:24 | Lead | Pronto | `searchSentences` | q="sale of Korean business eBay Korea Emart proceeds"; companiesIds=27862; dateRange={"gte": "2021-05-01", "lte": "2022-12-3… | 13,303 | `6ff4425cbe` | ok |
| 359 | 04:37:25 | Lead | Pronto | `searchSentences` | q="Ceconomy acquisition offer price"; companiesIds=36273923; dateRange={"gte": "2025-06-01", "lte": "now"} | 12,521 | `57a4c60a44` | ok |
| 360 | 04:37:26 | Lead | Pronto | `searchSentences` | q="About You acquisition offer price consideration"; companiesIds=97997549; dateRange={"gte": "2024-11-01", "lte": "now"} | 9,227 | `def0a4315c` | ok |
| 361 | 04:37:38 | Lead | Pronto | `searchSentences` | q="Just Eat Takeaway acquisition offer price per share total considerati…"; companiesIds=22355012; dateRange={"gte": "2025-02-01", "lte": "now"} | 9,414 | `3e69ec9775` | ok |
| 362 | 04:37:39 | Lead | S&P | `get_info_from_identifiers` | ids=Delivery Hero SE,Deliveroo plc,CECONOMY AG (+4) | 3,026 | `b7ba6a81fe` | ok |
| 363 | 04:37:47 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018,C_266895252,C_875173 (+4); line_item=revenue; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 9,629 | `26d70c6b36` | ok |
| 364 | 04:37:49 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018,C_266895252,C_875173 (+4); line_item=ebitda; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 9,386 | `bdfd4236e0` | ok |
| 365 | 04:37:50 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018,C_266895252,C_875173 (+4); line_item=net_debt; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 9,007 | `046e0aa5ce` | ok |
| 366 | 04:37:51 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018; line_item=revenue; period_type=ltm; num_periods=1 | 877 | `efdc0dbb63` | ok |
| 367 | 04:37:53 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018; line_item=ebitda; period_type=ltm; num_periods=1 | 867 | `84123f5595` | ok |
| 368 | 04:37:53 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=C_140687018; line_item=net_debt; period_type=quarterly; num_periods=1 | 869 | `004b9b396d` | ok |
| 369 | 04:40:41 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=revenue; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,315 | `0bff182d1b` | ok |
| 370 | 04:40:42 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=gross_profit; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,297 | `bd4bf5c975` | ok |
| 371 | 04:40:43 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=operating_income; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,311 | `1cce919baa` | ok |
| 372 | 04:40:45 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=net_income; period_type=annual; start_year=2021; end_year=2025; calendar_type=fiscal | 2,316 | `4c0fd8ab84` | ok |
| 373 | 04:40:46 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=revenue; period_type=quarterly; num_periods=8 | 2,845 | `16cf852607` | ok |
| 374 | 04:40:47 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG; line_item=operating_income; period_type=quarterly; num_periods=8 | 2,849 | `01caca4a9c` | ok |
| 375 | 04:42:26 | Lead | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-07-29", "lte": "2026-08-1…; interval=day | 1,709 | `a023a419eb` | ok |
| 376 | 04:42:26 | Lead | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-02-23", "lte": "2026-03-0…; interval=day | 1,251 | `9bd5c9e15c` | ok |
| 377 | 04:42:27 | Lead | Pronto | `getStockPrices` | companiesIds=704377650; dateRange={"gte": "2026-09-28", "lte": "now"}; interval=day | 1,557 | `78d91b4e2d` | ok |
| 378 | 04:42:39 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=cash_from_operations; period_type=ltm; num_periods=1 | 6,443 | `2d7f6b430e` | ok |
| 379 | 04:42:40 | Lead | S&P | `get_financial_line_item_from_identifiers` | ids=CPNG,AMZN,MELI (+13); line_item=capital_expenditure; period_type=ltm; num_periods=1 | 6,435 | `7fd7cd8843` | ok |
