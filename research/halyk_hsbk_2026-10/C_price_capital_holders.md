# Halyk Bank (HSBK LI / KASE: HSBK / AIX: HSBK): price history, catalysts, capital returns, shareholders, activism, short interest, indices

**Research dossier C. Prepared 23 Oct 2026.**

## Research constraints (read first)
- **WebFetch failed on every domain tried.** Each attempt returned DNS errors (`getaddrinfo ENOTFOUND`) for stockanalysis.com, londonstockexchange.com, sharecast.com, investing.com, halykbank.com and wikipedia.org. As a result, no page could be read directly. All facts below come from summarised WebSearch results, which show page snippets.
- **The shared WebSearch budget ran out partway through.** The cap is 200 calls per turn across all agents. Several planned lookups were not run: the monthly price series, ADTV, top-10 GDR holders, index membership, FCA short positions, rating actions, and the tax-code and base-rate catalysts. These items are marked **NOT FOUND**, or are flagged as background knowledge that still needs verifying.
- **Tags used in this file:**
  - **[u]** means a single, unconfirmed source.
  - **[d]** means a figure I derived or calculated, with the method shown.
  - **[bk]** means analyst background knowledge that was **not re-verified in this session**. Verify it before publishing.
- **No prices are invented.** The CSV block contains only observed price points. Derived year-end estimates sit in a separate table and are labelled as estimates.

---

## 1. Price history and market data

### 1.1 Latest market data (as of mid-October 2026)

| Item | Value | Source / note |
|---|---|---|
| Last LSE GDR price (Reg S, HSBK) | **US$32.75** (−0.91%), at 15 Oct 2026, 09:58 BST | LSE company page [u, via search snippet] https://www.londonstockexchange.com/stock/HSBK/jsc-halyk-bank/company-page |
| Previous close | US$33.05 (14 Oct 2026) | same |
| Price 30 Sep 2026 | US$34.00 (16:35) | Sharecast [u] https://www.sharecast.com/equity/JSC_Halyk_Bank_GDR_Reg_S/share-prices |
| Price 20–23 Oct 2026 | **NOT FOUND** | WebFetch was down and the search budget was exhausted |
| 52-week high / low (LSE) | **US$36.45 / US$22.90** | LSE page. On 18 Aug 2026 the range was 22.90–36.20 (Investing.com / Edison). The 36.45 high was therefore set between 19 Aug and 15 Oct 2026 [d]. The 22.90 low falls around the Nov-2025 ALMEX placement [d]. |
| 144A GDR (37QB) | US$20.25 | LSE page [u]. This line is illiquid and should not be used. |
| KASE share (HSBK), latest seen | **KZT 368.30** (close 8 Oct 2026) | Investing.com KASE history snippet [u] https://www.investing.com/equities/halyk-bank-ao-historical-data |
| Market cap (USD) | **≈ US$8.93bn** | Morningstar and companiesmarketcap. 272.73m GDR-equivalents × $32.75 = $8.93bn [d check] https://companiesmarketcap.com/jsc-halyk-bank/marketcap/ |
| Market cap (KZT) | **≈ KZT 4.02trn** [d] | 10,909,361,466 shares × KZT 368.30 (8 Oct 2026) |
| Authorised common shares | 25,000,000,000 | KASE notice, 1 Jul 2025 https://kase.kz/en/information/news/show/1548425 |
| Issued (placed) common shares | **13,447,544,782** | same (unchanged at end-2025 per Yahoo balance-sheet data) |
| Treasury (repurchased) shares | **2,533,546,317** (1 Jul 2025); ≈2,548.0m (31 Dec 2025, Yahoo [u]); **≈2,538,183,316 (30 Jun 2026)** [d = issued − outstanding] | KASE; Yahoo https://finance.yahoo.com/quote/H4L1.F/balance-sheet/ |
| Outstanding common shares | 10,913,998,465 [d] (1 Jul 2025); ≈10,899.6m (31 Dec 2025, Yahoo [u]); **10,909,361,466 (30 Jun 2026)** | Halyk "About us" page https://halykbank.com/about-us and Global Gambit initiation https://www.theglobalgambit.com/p/initiation-of-coverage-halyk-bank |
| GDR-equivalent shares (÷40) | **272.73m** | Morningstar and Edison |
| GDRs outstanding (actual DRs) | **NOT FOUND** directly. Estimates: ≈76.2m GDRs on 1 Jul 2025 [d: BNY nominee 27.92% × 10.914bn ÷ 40]; ≈95m GDRs after the Nov-2025 placement [d: 35% GDR holders × 10.909bn ÷ 40]. In 2020 the figure was 2,969,178,640 shares in GDR form, about 74.2m GDRs (25.4% of shares in circulation). | Annual Report 2020 https://halykbank.com/storage/794/2020.pdf |
| Average daily volume / value (LSE, KASE) | **NOT FOUND** | |
| USD/KZT now | **NOT FOUND** (no direct quote). Implied rates: ≈519–520 at the Nov-2025 placement [d: KZT 298.66 vs $23/40 = $0.575]; ≈470 for the May-2026 dividend [d: Halyk's table converts KZT 30.10/share to $2.56/GDR, so 1,204 ÷ 2.56]. Do not use without checking against NBK. | |

### 1.2 Observed GDR price points (CSV, observed only, USD per Reg S GDR)

```csv
date,close_usd,type,source
2019-10-01,11.75,secondary offering price (Oct 2019 GDR offering by selling shareholder),Halyk Finance / Edison https://halykfinance.kz/novosti/gdr-offering-of-jsc-halyk-bank-has-been-succesfully-completed.html?lang=en
2020-03-11,11.00,close (LSE mobile summary snapshot; [u] search tool flagged as possibly stale),https://m.londonstockexchange.com/exchange/mobile/stocks/summary.html?tidm=HSBK
2022-02-23,12.50,prior close implied [d] from -15.28% to 10.59,Kursiv 24-Feb-2022
2022-02-24,10.59,close (-15.28% on Russia's invasion of Ukraine),https://kz.kursiv.media/en/2022-02-24/shares-of-kaspi-halyk-bank-and-kazatomprom-in-sharp-decline-on-lse/
2022-02-28,10.20,approx. start-of-March level (Feb = -21.2%),https://kz.kursiv.media/en/2022-03-04/kazakhstan-equities-continue-to-plunge-on-lse/
2022-03-04,8.60,price (-15.7% since start of March),https://kz.kursiv.media/en/2022-03-04/kazakhstan-equities-continue-to-plunge-on-lse/
2022-12-30,10.40,year-end price per Annual Report 2022 (= KZT 4840.06 per GDR),https://www.annualreports.com/HostedData/AnnualReportArchive/j/jsc-halyk-bank_2022.pdf
2023-12-29,15.16,year-end price per Annual Report 2023 ([u] unit label ambiguous),https://kase.kz/files/emitters/HSBK/hsbkp_2023_eng.pdf
2024-12-13,17.84,intraday (ex-dividend week; -5.3% on 12-Dec),https://kz.kursiv.media/en/2024-12-13/engk-tank-freedom-broker-explains-why-halyk-banks-gdr-value-dropped-on-the-lse/
2025-11-05,25.56,buyback average purchase price ([u] year inferred),https://www.investing.com/news/company-news/halyk-bank-purchases-own-gdrs-worth-114-million-in-buyback-program-93CH-4344594
2025-11-14,25.74,buyback daily weighted averages 25.64-25.84 over 10-14 Nov (midpoint),same
2025-11-21,23.00,ALMEX fully-marketed placement price,https://en.orda.kz/almex-sells-76-stake-in-halyk-bank-for-475-million-9397/
2025-11-28,24.47,buyback weighted average late Nov 2025,https://www.investing.com/news/company-news/halyk-bank-purchases-over-107000-gdrs-in-buyback-program-93CH-4374300
2025-12-05,25.30,price quoted in Edison note,https://www.edisongroup.com/research/7-nim-likely-to-be-sustained-into-2026/BM-2469/
2026-07-16,30.70,buyback weighted average 14-16 Jul 2026,https://kalkinemedia.com/uk/news/announcements/halyk-bank-finalizes-purchase-of-30853-gdrs-on-london-and-european-exchanges-in-july-2026
2026-08-17,35.10,close before H1-2026 results,https://www.investing.com/news/transcripts/earnings-call-transcript-halyk-bank-h1-2026-profit-falls-as-margins-tighten-93CH-4865705
2026-08-18,34.05,close on H1-2026 results day (-2.9/-3.0%),same
2026-09-30,34.00,price 16:35,https://www.sharecast.com/equity/JSC_Halyk_Bank_GDR_Reg_S/share-prices
2026-10-14,33.05,close,https://www.londonstockexchange.com/stock/HSBK/jsc-halyk-bank/company-page
2026-10-15,32.75,intraday 09:58 BST,same
```

**Monthly closes for Jan 2016 to Oct 2026: NOT FOUND.** No monthly table was retrievable.

### 1.3 KASE local-share price points (KZT per common share)

| Date | KZT | Source |
|---|---|---|
| 31 Dec 2020 | 123.37 (KASE official market price) | Annual Report 2020 |
| 29 Dec 2023 | 160.5 | Annual Report 2023 [u] |
| 13 Dec 2024 | 242.95 (−1.68% on the day) | Kursiv |
| ~20 Nov 2025 | 298.66 (ALMEX placement price for local shares) | Orda.kz / Edison |
| 8 Oct 2026 | 368.30 | Investing.com [u] |

The KASE shares have traded close to GDR parity. For example, on 13 Dec 2024, 242.95 × 40 ÷ $17.84 implies about 545 KZT/USD, against a spot rate of roughly 525 [bk]. That points to a small premium on KASE [d].

### 1.4 Derived year-end GDR estimates (NOT observed prices; use only as orientation)

- **Method A** scales companiesmarketcap's USD year-end market caps (Frankfurt line H4L1, converted to USD) to the official year-end 2022 price: US$10.40 corresponds to US$2.96bn, so US$3.51 per GDR for each US$1bn of market cap.
- **Method B** divides the same market caps by a constant 272.73m GDR-equivalents.
- **Cross-checks** use KASE prices or market caps.

| Year-end | Mkt cap US$bn (companiesmarketcap) | Est. GDR price, Method A | Method B | Cross-check |
|---|---|---|---|---|
| 2016 | 1.64 | ~5.8 | ~6.0 | none |
| 2017 | 2.71 | ~9.5 | ~9.9 | none |
| 2018 | 3.06 | ~10.8 | ~11.2 | none |
| 2019 | 3.96 | ~13.9 | ~14.5 | Oct-2019 SPO at $11.75 |
| 2020 | 3.41 | ~12.0 | ~12.5 | KASE 123.37 × 40 ÷ 420.9 [bk NBK rate] = **$11.72** |
| 2021 | 4.63 | ~16.3 | ~17.0 | Portfolioslab TR −25.3% in 2022 implies ~$15.4; stockanalysis KASE m-cap KZT 1.98trn |
| 2022 | 2.96 | **10.40 (official)** | 10.85 | AR 2022 |
| 2023 | n/a | **15.16 (official)** | n/a | AR 2023 |
| 2024 | ~5.59 (8.66 ÷ 1.5499) | ~19.6 | ~20.5 | stockanalysis KASE m-cap KZT 2.77trn ÷ 10.91bn = KZT 254, which is about $19.3 at ~525 [bk] |
| 2025 | 8.66 (+54.99% y/y) | ~30.4 | ~31.8 | stockanalysis KASE m-cap KZT 4.14trn ÷ 10.90bn = about KZT 380 |

> **Open issue:** both aggregators imply a year-end 2025 price of about $30–32. The observed prices were $23–25.5 in mid-November to early December 2025. That would mean a roughly 20–25% rally in December 2025, which no source confirms. An alternative reading is that stockanalysis used the issued share count, giving KZT 308 and about $24. **Verify the 31 Dec 2025 close before using it.**

**Portfolioslab annual total returns** (dividend-adjusted; currency not stated) [u] https://portfolioslab.com/symbol/HSBK.L:

| Year | Total return |
|---|---|
| 2016 | +21.0% |
| 2017 | +64.9% |
| 2018 | +11.5% |
| 2019 | +41.8% |
| 2020 | +0.7% (Jan +9.0%, Feb −3.8%, **Mar −34.3%** COVID) |
| 2021 | +59.8% |
| 2022 | −25.3% |
| 2023 | +65.9% |
| 2024 | +51.2% |
| 2025 (partial year, apparently through about Oct) | +65.2% |

The 2023 figure is consistent with the official prices: $10.40 to $15.16 is +46% on price, plus about a 21% dividend.

**Annual highs and lows by year: NOT FOUND**, except the current 52-week range of $22.90–36.45.

---

## 2. Catalysts, Oct 2021 – Oct 2026 (moves of roughly ±10% or more)

| # | Date / window | Move | Price before → after | Cause | Sources |
|---|---|---|---|---|---|
| 1 | 4–6 Jan 2022 | **GDR −16%** (Wikipedia); **−17.6%** on LSE (KASE official quoted by Azernews); **~−20%** intraday (Kazakhstan Association of Minority Shareholders via AKIpress); about −7% at one intraday point (Royal.inc) | ~$15.4–16.3 at end-2021 [d] → ~$12.9 at end-Jan 2022 [d: end-Feb $10.20 ÷ (1−0.212)] | **"Bloody January" unrest** (2–11 Jan 2022). Protests over LPG prices, CSTO deployment, internet blackout. Also a political shock for the Nazarbayev family, which owns the controlling stake through ALMEX. | https://en.wikipedia.org/wiki/Halyk_Bank ; https://akipress.com/news:666690:Kaspi_shares_declined_by_30_,_Halyk_Bank_-_by_20_,_Kazatomprom_-_7__in_London_amid_situation_in_Kazakhstan/ ; https://www.azernews.az/region/190347.html ; https://www.royal.inc/blog/kazakhstan-stocks-and-bonds-fall-in-moscow-and-london-due-to-protests |
| 2 | 24 Feb 2022 | **GDR −15.28%** (KASE share −13.05%); full-month Feb 2022 −21.2% | ~$12.50 → $10.59 | **Russia's invasion of Ukraine**: fear of sanctions spillover, rouble/tenge contagion, and Halyk's Russian subsidiary | Kursiv 24 Feb 2022 |
| 3 | 1–4 Mar 2022 | **GDR −15.7%** | $10.20 → ~$8.60 | Sanctions escalation and Russia/CIS asset sell-off. Cumulative fall from end-2021 was about −45% [d]. The 2022 trough was around $8.6 (exact low NOT FOUND). | Kursiv 4 Mar 2022 |
| 4 | Mar–Dec 2022 | Partial recovery to $10.40 at year-end (+21% from trough) [d] | ~$8.6 → $10.40 | Recovery, including the **FY2021 dividend reinstatement**. The Apr-2022 AGM proposal was zero; KZT 12.71 was later paid (ex-date 24 Oct 2022). Halyk also agreed to sell **100% of its Russian subsidiary** (announced Dec 2022). Price reaction to the sale: NOT FOUND. | AGM materials https://halykbank.com/storage/95/03.03.2022_-Materials--for-shareholders%E2%80%99-consideration-at-the-AGM-of-JSC-Halyk-Bank-to-be-held-on-22-April-2022.PDF ; https://www.marketscreener.com/quote/stock/HALYK-BANK-8382832/news/JSC-Halyk-Bank-On-the-sale-of-100-shares-of-subsidiary-bank-in-Russian-Federation-42603728/ |
| 5 | CY2023 | **+46% price** ($10.40 → $15.16); about +66% total return | | Re-rating on record earnings and a payout of KZT 25.38 (50%). Single-day triggers NOT FOUND. | AR 2022 / AR 2023 |
| 6 | CY2024 | about +29% price (to roughly $19.5–20.5 [d]); +51% total return | | Payout extended with a second, Dec-2024 tranche (KZT 9.57); GDR buyback started in Sept 2024 | Portfolioslab; derived |
| 7 | 12–13 Dec 2024 | GDR −5.3% (below the 10% threshold; listed for context) | → $17.84 | **Ex-dividend gap** for the KZT 9.57 dividend (about $0.75 per GDR), per Freedom Broker | Kursiv 13 Dec 2024 |
| 8 | Jan–Oct 2025 | Strong rally (Portfolioslab TR about +65% YTD, apparently through about Oct 2025 [u]) | ~$20 → ~$30? [d, unverified] | FY2024 payout of KZT 50.64 (60%); new $50m buyback (1 Oct 2025). Specific triggers NOT FOUND. | |
| 9 | Early–late Nov 2025 | Probable **double-digit drawdown**: buyback prints of $25.56 (5 Nov) and $24.47 (late Nov), placement at **$23.00**, 52-week low **$22.90** | ~$29–30? [d, unverified] → $23–25 | **ALMEX stake-sale overhang.** Reuters/Bloomberg reported on 4 Nov 2025 that ALMEX was weighing a partial sale. Fully-marketed offering launched with at least 12m GDRs. Priced at about 20–21 Nov at $23 per GDR and KZT 298.66 per share; 7.6% sold for **$475.4m**. Settlement on LSE 25 Nov, AIX/KASE trading from 26 Nov 2025. | https://www.tradingview.com/news/reuters.com,2025:newsml_L8N3WG0WW:0-main-shareholder-in-halyk-bank-kazakhstan-s-largest-bank-weighs-a-partial-stake-sale/ ; https://news.bloomberglaw.com/mergers-and-acquisitions/billionaire-owners-of-biggest-kazakh-bank-halyk-weigh-stake-sale ; https://kase.kz/en/information/news/show/1555361 ; Orda.kz |
| 10 | Dec 2025 – Aug 2026 | **+50–58%** from the placement price to the 52-week high | $23.00 / $22.90 → $36.20 (by 18 Aug 2026) → **$36.45** (high, Aug–Oct 2026) | Post-placement re-rating: larger free float (about 38%), overhang removed, and a 365-day ALMEX lock-up. FY2025 payout of KZT 58.19 (+15%); buybacks at $29–31 in June–July 2026. Possible index-weight increase from the higher free float (NOT VERIFIED). | Edison; Kalkine; LSE |
| 11 | 18 Aug 2026 | −2.9/−3.0% (below threshold) | $35.10 → $34.05 | **H1-2026 results.** Net income KZT 447.6bn (−15.3% y/y); Q2 KZT 212.8bn (−16.1%); NIM 6.8% vs 7.3%, hit by **new NBK minimum reserve requirements**; fee income −19.6%; 90+ day NPLs reportedly 5.3% vs 3.0%. FY26 guidance kept at about KZT 1trn net income and 29% ROAE. | https://halykbank.com/storage/830/Press-Release.pdf ; Investing.com transcript |
| 12 | Late Aug → mid-Oct 2026 | **about −10% from the 52-week high** | $36.45 → $32.75 | Partly the **ex-dividend date of 25 Aug 2026** (KZT 28.09 = KZT 1,124 per GDR, about $2.4 [d]), plus the weaker earnings trend. EGM held 25 Sep 2026 (agenda NOT FOUND). | stockanalysis div page; LSE |

**Catalysts checked but not confirmed (search budget exhausted; verify before publishing):**
- **Tax:** the new Kazakhstan Tax Code effective 1 Jan 2026 reportedly raised corporate income tax for banks to 25% from 20%, with carve-outs for lending to the real economy [bk].
- **Base rate:** NBK base-rate hikes in 2025, reportedly to 18% in Oct 2025 [bk].
- **Rating actions:** Moody's, S&P and Fitch actions on Halyk or the sovereign: **NOT FOUND**.
- **Index events:** MSCI or FTSE events: **NOT FOUND**.
- **Late 2021:** whether there was a move of 10% or more in Oct–Dec 2021 (the TR was +60% in 2021): **NOT FOUND**.

---

## 3. Dividends (FY2016–FY2025)

**Policy.** Management said on the Q2-2026 call that the bank will "strive to stick to its dividend policy of a **50%+ payout ratio**". Analysts refer to a "usual 60%". Since FY2023 the bank pays **two tranches per fiscal year**: a final approved at the AGM (Apr/May) and a second tranche from retained earnings approved at an EGM (Sep/Dec). Management said the second FY2025 payment was brought forward to Q3. https://finance.yahoo.com/markets/stocks/articles/halyk-bank-kazakhstan-jsc-fra-230138783.html

Halyk's IR page cites a **5-year DPS CAGR of 23.0%**, a **5-year average dividend yield of 14.1%** and a **5-year TSR CAGR of 20.1%**. https://halykbank.com/for-shareholders/dividends

| Fiscal year | Tranche | DPS (KZT / common share) | Per GDR (KZT, ×40) [d] | Per GDR (USD) | Total (KZT bn) | Payout ratio | Approval / record / payment dates | Sources |
|---|---|---|---|---|---|---|---|---|
| FY2015 | n/a | **Nil** (no payment in CY2016 per aggregators) [d] | 0 | 0 | 0 | 0% | n/a | companiesmarketcap dividends |
| FY2016 | n/a | **Nil** (no payment in CY2017) [d] | 0 | 0 | 0 | 0% | n/a | same; Divvydiary has no 2017 entry |
| FY2017 | Final | **6.31** | 252.4 | NOT FOUND (about $0.76 per Stock Events [u]) | NOT FOUND (~70 rough [d]) | NOT FOUND | AGM Apr 2018; paid 2018 | Divvydiary https://divvydiary.com/en/halyk-bank-of-kazakhstan-jsc-stock-KZ000A0LE0S4 |
| FY2018 | Final | **10.78** | 431.2 | NOT FOUND | NOT FOUND (~125 rough [d]) | NOT FOUND | AGM Apr 2019; paid 2019 | Divvydiary |
| FY2019 | Final | **17.08** | 683.2 | NOT FOUND | NOT FOUND (~200 rough [d]) | NOT FOUND | AGM 2020; paid 2020 | Divvydiary |
| FY2020 | Final | **18.00** | 720.0 | NOT FOUND | NOT FOUND (~210 rough [d]) | NOT FOUND | AGM 2021; paid 2021 | Divvydiary (one search summary flagged 17.08 vs 18.00 confusion; 18.00 is the CY2021 payment) |
| FY2021 | Final (delayed) | **12.71** | 508.4 | ~$1.08 [u] | **138** | **30%** | AGM 22 Apr 2022 proposed **no** dividend (retain earnings). Later approved; ex-date 24 Oct 2022; paid 27 Oct 2022 (shares) / 7 Nov 2022 (GDR) [u] | Halyk IR table; AGM 2022 materials; aggregators |
| FY2022 | Final | **25.38** | 1,015.2 | NOT FOUND | **276** | **50%** | AGM 2023; dates NOT FOUND | Halyk IR table |
| FY2023 | Final | **25.43** | 1,017.2 | NOT FOUND | **277** | **40%** | AGM 2024; dates NOT FOUND | Halyk IR table |
| FY2023 | 2nd (retained earnings) | **9.57** | 382.8 | **$0.75** (Kursiv) | **104** | **15%** | EGM Dec 2024 (absentee); record 10 Dec 2024; payment from 12 Dec 2024; GDR ex-div gap 12–13 Dec 2024 | https://www.investing.com/news/company-news/halyk-bank-announces-dividend-payment-and-audit-firm-selection-93CH-3761233 ; Kursiv |
| **FY2023 total** | | **35.00** | 1,400 | | **381** | **55%** | | [d] |
| FY2024 | Final | **29.64** | 1,185.6 | NOT FOUND | **323** | **35%** | AGM Apr 2025; payable **23 Jun 2025** | https://www.marketscreener.com/quote/stock/HALYK-BANK-8382832/news/Halyk-Bank-of-Kazakhstan-Joint-Stock-Company-announces-Annual-dividend-payable-on-June-23-2025-49730507/ ; https://kase.kz/en/information/news/show/1551381 |
| FY2024 | 2nd (retained earnings) | **21.00** | 840.0 | NOT FOUND | **229** | **25%** | **EGM 22 Sep 2025**; paid (completion reported) | https://halykbank.com/storage/79/22.09.2025-_Resolution-about-second-dividend-payment-for-2024-adopted-at-the-EGM-on-22-September-2025.pdf ; https://www.investing.com/news/company-news/halyk-bank-to-pay-kzt-21-per-share-dividend-from-past-earnings-93CH-4248220 |
| **FY2024 total** | | **50.64** | 2,025.6 | | **552** | **60%** | | [d] |
| FY2025 | Final | **30.10** | 1,204.0 | **$2.56** (Halyk IR) | **329** | **31%** | **AGM 23 Apr 2026** (RNS 24 Apr; 7,611,002,540 of 7,904,221,264 voting shares participated); **record 30 Apr 2026; payment from 18 May 2026** | https://kase.kz/en/information/news/show/1565078 ; https://www.investormeetcompany.com/companies/jsc-halyk-bank/rns/4669043/view |
| FY2025 | 2nd (retained earnings) | **28.09** | 1,123.6 | ~$2.4 [d at ~470] | ~**306** [d: × 10.909bn] | ~29% [d] | **EGM 20 Aug 2026** (absentee); **ex-date 25 Aug 2026; record 26 Aug 2026; payment from 7 Sep 2026** | https://kase.kz/en/information/news/show/1573861 ; https://www.investing.com/news/company-news/halyk-bank-declares-dividend-of-kzt-2809-per-common-share-93CH-4869073 |
| **FY2025 total** | | **58.19** (+15% y/y) | 2,327.6 | ~$4.9–5.0 [d] | ~**635** [d] | **~60%** (Edison) | | Edison |

**Notes on the dividend table:**
- **Yield.** FY2025 DPS of 58.19 against the KZT 368.30 share price gives a trailing yield of about **15.8%** [d]. On the GDR, about $4.9 against $32.75 gives about 15% [d].
- **FY2026.** An **EGM was held on 25 Sep 2026** (absentee). Its agenda is NOT FOUND and should be checked for any interim FY2026 dividend. https://halykbank.kz/en/about/shareholders_investors/akcioneram
- **Ratios for FY2017–FY2020.** Payout ratios are NOT FOUND. The rough totals assume about 11.0–11.7bn shares outstanding and should not be quoted.

---

## 4. Buybacks, treasury shares, placements

### 4.1 Buyback programmes

| Programme | Dates | Size / cap | Executed (found) | Price range | Counterparty / venue | Sources |
|---|---|---|---|---|---|---|
| **GDR Repurchase Programme 2024** | Announced **18 Sep 2024**; ran about 1 year | **NOT FOUND.** Kursiv says "valued at $1.1 million" [u, likely misreported] | Tranches found: 46,853 GDRs (3 days, Dec 2024); 203 GDRs (Jan 2025); 17,988 GDRs (4 Apr 2025). **Cumulative total NOT FOUND** | ~$17–21 [d] | Open market, executed by **Citigroup Global Markets Ltd** on XLON / BATE / CHIX | RNS https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/announcement-of-gdr-repurchase-programme/9141705 ; https://www.investing.com/news/company-news/halyk-bank-executes-buyback-of-global-depositary-receipts-93CH-3776131 ; https://www.investing.com/news/company-news/halyk-bank-completes-gdr-buyback-transactions-93CH-3796487 ; https://www.investing.com/news/company-news/halyk-bank-executes-gdr-buyback-through-citigroup-93CH-3969733 ; Kursiv |
| **GDR Buyback 2025–26** | **1 Oct 2025 → no later than 1 Oct 2026** (expired; extension or replacement NOT FOUND) | **Up to US$50m**, capped at **1% of issued common shares** (about 134.5m shares, or 3.36m GDRs [d]). Purpose: capital-structure optimisation | Found: 44,636 GDRs ≈ $1.14m (Nov 2025, avg $25.65); 107,413 GDRs at $24.47 ≈ $2.63m [d] (late Nov 2025); one week ">$1.5m"; 27,358 GDRs (2026); 30,853 GDRs ≈ $947k at $30.70 (14–16 Jul 2026); 2,432 GDRs for $74,782 (~$30.75). **Sum of tranches found ≈ $7m** [d], a small fraction of the $50m cap. **Total utilisation NOT FOUND.** | $24.47–31 | Citi on XLON / BATE / CHIX (open market) | https://www.marketscreener.com/news/halyk-bank-of-kazakhstan-joint-stock-company-announces-an-equity-buyback-for-50-million-worth-of-it-ce7d5bd9db8bf525 ; https://www.investing.com/news/company-news/halyk-bank-purchases-own-gdrs-worth-114-million-in-buyback-program-93CH-4344594 ; https://www.investing.com/news/company-news/halyk-bank-purchases-over-107000-gdrs-in-buyback-program-93CH-4374300 ; https://za.investing.com/news/company-news/halyk-bank-purchases-own-gdrs-worth-over-15-million-in-buyback-93CH-3987382 ; https://www.investing.com/news/company-news/halyk-bank-purchases-27358-gdrs-in-buyback-programme-93CH-4778260 ; https://www.investing.com/news/company-news/halyk-bank-buys-back-2432-gdrs-for-74782-93CH-4787730 ; Kalkine ; TradingView RNS 7 Jul 2026 https://www.tradingview.com/news/reuters.com,2026-07-07:newsml_RSG3063La:0-reg-jsc-halyk-bank-jsc-halyk-bank-37qb-transaction-in-own-securities/ |
| Programmes 2016–2023 | **NOT FOUND** | | | | | |
| Purchases from ALMEX or the Kazakh government (Samruk-Kazyna, UAPF) | **NOT FOUND** in this session | | | | | |

### 4.2 Treasury shares over time

| Date | Issued | Treasury | Outstanding | Source |
|---|---|---|---|---|
| end-2020 | NOT FOUND (13.45bn if unchanged [d]) | ≈1.76bn [d] | ≈11.69bn [d: 2,969,178,640 GDR-form shares = 25.4% of circulation] | AR 2020 |
| 1 Jul 2025 | 13,447,544,782 | **2,533,546,317** | 10,913,998,465 [d] | KASE |
| 31 Dec 2025 | 13,447.5m | ≈2,548.0m | ≈10,899.6m | Yahoo [u] |
| 30 Jun 2026 | 13,447,544,782 (assumed unchanged) | ≈2,538.2m [d] | **10,909,361,466** | Halyk website / Global Gambit |
| Other year-ends (2016–2019, 2021–2024) | NOT FOUND | NOT FOUND | NOT FOUND | |

**Points to note:**
- **Treasury rose by about 0.77bn shares between 2020 and mid-2025** [d], equal to about 19m GDRs or roughly 6–7% of outstanding. The source of these shares (open market, a block from a holder, or the Kazkommertsbank merger mechanics) is **NOT FOUND**. It is worth checking.
- **The small H1-2026 increase in outstanding shares** (about +9.8m [d]) is consistent with the **Dec-2024 EGM authorisation**. That authorisation allows up to **1% of shares** to be allotted to directors and employees, without pre-emptive rights, over 5 years for incentive plans.
- **Cancellations: NOT FOUND.** No evidence was found that treasury shares were cancelled. Issued shares were unchanged at 13.4475bn in 2025–26.

### 4.3 Secondary placements

| Date | Seller | Size | Price | Notes | Sources |
|---|---|---|---|---|---|
| **Oct 2019** | "Selling shareholder" (identity not confirmed in this session; possibly a treasury or subsidiary holding [bk]) | NOT FOUND | **$11.75 per GDR** | SPO with book-building on AIX (notice 30 Sep 2019) and LSE | https://halykfinance.kz/novosti/gdr-offering-of-jsc-halyk-bank-has-been-succesfully-completed.html?lang=en ; https://aix.kz/aix-market-notices/2019-09-30_01_aix-book-building-announcement-eqipousd-board/ |
| **Nov 2025** (launched about 4–10 Nov; priced about 20–21 Nov; settled 25 Nov; KASE/AIX trading 26 Nov) | **ALMEX** (Bank received no proceeds) | **17,625,000 GDRs** (17.42m international + 0.205m domestic) **+ 121,800,000 common shares** = 826.8m share-equivalents = **7.6%** of outstanding | **$23.00 / GDR; KZT 298.66 / share.** Total **US$475.41m** (GDR leg ≈ $405m [d]). About a 10% discount to early-November levels [d, approx.] | Fully marketed offering, not an ABB. Base size at least 12m GDRs was upsized. ALMEX held 69.5% before and **~62% after**. **365-day lock-up** on ALMEX's remaining stake (to about Nov 2026), subject to exceptions. Pre-deal intention to keep at least 51%. | KASE https://kase.kz/en/information/news/show/1555361 ; Orda.kz ; Investing.com https://www.investing.com/news/company-news/halyk-banks-major-shareholder-sells-76-stake-for-475-million-93CH-4373108 ; Edison https://www.edisongroup.com/research/majority-owner-eyes-the-sale-of-a-minority-stake/BM-2463/ |

---

## 5. Shareholders

### 5.1 Current structure (mid-2026)

| Holder | Type | % of outstanding | Shares (approx.) | Source |
|---|---|---|---|---|
| **JSC Holding Group ALMEX** (Timur Kulibayev and Dinara Kulibayeva, daughter of ex-President Nazarbayev) | Insider / controlling | **61.9%** (Halyk website); **62.4%** (Edison, citing NBK data at 1 Mar 2026 / end-Dec 2025) | ≈6.76bn [d: 7.583bn − 0.1218bn − 0.705bn] | https://halykbank.com/about-us ; https://www.edisongroup.com/research/top-player-in-an-important-frontier-market/BM-3138/ |
| **GDR holders** (The Bank of New York Mellon as depositary/nominee) | Institutional (foreign) | **35.0%** (Halyk) / 34.5% (Edison) | ≈3.8bn (≈95m GDRs) [d] | same |
| Domestic shareholders (local institutions including UAPF/ENPF, KASE retail, others) | Institutional, state pension, retail | **3.1%** | ≈0.34bn | same |
| **Free float** | | **≈38%** (vs ≈30.5% before the Nov-2025 sale) [d] | | |

The Halyk "About us" page also shows a 30 Jun 2026 block with zero values, which looks like a display glitch [u].

### 5.2 Comparison with 2021 and mid-2025

| Holder | ~2020/21 | 1 Jul 2025 | Mid-2026 |
|---|---|---|---|
| ALMEX | **64.5%** (Wikipedia, as of Jan 2020; basis unclear) [u] | **69.48%** of outstanding (56.39% of placed) | ~62% |
| BNY (GDR nominee) | GDRs = **25.4%** of circulation (AR 2020) | **27.92%** of outstanding (22.66% of placed) | ~35% |
| Others / domestic | ~10% [d] | ~2.6% [d] | ~3.1% |

ALMEX's percentage **rose** between 2020 and 2025 without any purchase being found. This is most likely because the bank's treasury buybacks reduced the share count [d]. Buybacks of about 0.77bn shares would lift 7.58bn ÷ 11.69bn = 64.9% to 69.5%, which fits.

### 5.3 Top-10 named holders
**NOT FOUND.** The top-10 named institutional GDR holders and their percentages could not be retrieved. This includes UAPF/ENPF, BlackRock, Vanguard, Lazard, Templeton, Wellington, East Capital, Prosperity, Ashmore and Norges. MarketScreener's shareholder page (https://www.marketscreener.com/quote/stock/HALYK-BANK-9059697/company/) lists the Kulibayev family at 61.94%, but its fund list was not visible. **Recommended next step:** pull the 13F/N-PORT, Morningstar or Refinitiv ownership lists and the KASE quarterly shareholder notice for 1 Jul 2026.

### 5.4 Lock-ups
ALMEX agreed a **365-day lock-up** from the Nov-2025 offering, expiring around **late Nov 2026**. Exceptions were not detailed. This expiry is a near-term technical overhang to flag. No other lock-ups were found.

---

## 6. Activism
- **No activist campaigns found.** No proxy fights or public disputes by funds, minorities or the government against Halyk were found for 2016–2026.
- **Governance pressures noted:**
  - **Control and politics.** Controlling ownership by the Kulibayev–Nazarbayeva family through ALMEX brings political and related-party sensitivity, which rose after the Jan-2022 events.
  - **Minority shareholders' voice.** The **Kazakhstan Association of Minority Shareholders** is a public commentator on market moves (it was cited for the Jan-2022 drop), not an activist in Halyk.
  - **Dividend reversal in 2022.** The board first proposed **no FY2021 dividend** (AGM, 22 Apr 2022), then paid KZT 12.71 in Oct 2022. Evidence of minority pressure behind the reversal was NOT FOUND.
  - **Free-float pressure.** The ALMEX sell-down in Nov 2025 was framed as boosting liquidity and free float, which addresses a long-standing investor concern.
  - **Dilution authority.** The Dec-2024 EGM approved allotting up to 1% of shares to directors and employees **without pre-emptive rights**. This is a minor dilution consideration.

---

## 7. Short interest
- **FCA net short positions: NOT FOUND.** No disclosed net short positions in Halyk were found. **Background [bk]:** the UK short-selling regime generally covers shares admitted to UK trading venues. Halyk has only **depositary receipts** admitted in London, while its underlying shares trade on KASE/AIX, so it may sit outside the FCA notification list. Verify against the FCA's list of exempted and covered shares.
- **Securities-lending or utilisation data: NOT FOUND.**
- **Short-seller reports:** none found on Halyk. The peer **Kaspi.kz** was targeted by a short seller (Culper Research, Sept 2024) over its Russia links (https://www.intellinews.com/short-seller-argues-nasdaq-listed-kazakh-fintech-heavyweight-kaspi-misled-market-over-russia-links-344492/). That is relevant only as sector sentiment.

---

## 8. Index membership
**NOT VERIFIED in this session** because the search budget was exhausted. Background [bk] to confirm:
- **MSCI.** Halyk GDR is believed to be a constituent of the **MSCI Frontier Markets** and **MSCI Kazakhstan** indices, in which Kazakhstan has Frontier status. The higher free float after Nov 2025 should have raised its index weight (check the MSCI Feb/May 2026 reviews).
- **FTSE Russell.** Kazakhstan's FTSE classification and Halyk's FTSE Frontier membership are to be confirmed.
- **Planned changes.** Any MSCI or FTSE reclassification or watch-list action for Kazakhstan, and any role for AIX/KASE market-access reforms, are **NOT FOUND**.

---

## 9. Key gaps to close in a follow-up
- Full monthly LSE GDR closes for 2016–2026, from LSE, Investing.com or Sharecast CSV downloads. This was blocked by the WebFetch DNS failure.
- The 20–23 Oct 2026 price, LSE/KASE ADTV, and the current NBK USD/KZT rate.
- The 31 Dec 2025 GDR close, which resolves the Dec-2025 discrepancy.
- Top-10 institutional holders.
- MSCI/FTSE index membership.
- FCA short-position list status.
- Rating actions, tax-code and base-rate catalysts.
- The size and execution total of the Sept-2024 buyback, and whether the Oct-2025 programme was extended after 1 Oct 2026.
- The 2019 offering's seller and size.
- The agenda of the 25 Sep 2026 EGM.

## Other sources consulted
- Edison notes: https://www.edisongroup.com/research/leading-central-asian-player-with-a-30-roe/BM-1213/ ; https://static.lse.co.uk/research/download/3138.pdf
- Reuters (via MarketScreener), on ALMEX weighing a stake sale: https://www.marketscreener.com/news/main-shareholder-in-halyk-bank-kazakhstan-s-largest-bank-weighs-a-partial-stake-sale-ce7d5cdede8bff24
- Stockanalysis KASE market cap: https://stockanalysis.com/quote/kase/HSBK/market-cap/
- Stockanalysis LSE dividends: https://stockanalysis.com/quote/lon/HSBK/dividend/
- Companiesmarketcap dividends: https://companiesmarketcap.com/jsc-halyk-bank/dividends/
- H1-2026 report (Investegate): https://www.investegate.co.uk/announcement/rns/jsc-halyk-bank--37qb/half-year-financial-report/9726112
- Wikipedia, 2022 Kazakh unrest: https://en.wikipedia.org/wiki/2022_Kazakh_unrest
