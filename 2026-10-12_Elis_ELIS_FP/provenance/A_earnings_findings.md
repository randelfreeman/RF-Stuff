# A_earnings — findings (final hand-back report of worker A, saved verbatim by the lead analyst because the harness blocked the worker from writing this file)

Detail and full citations are in model/A_*.json/csv; call log in provenance/logs/A_earnings.md; raw responses in provenance/raw/A_earnings/.

### 1. Sentiment, 2020–2026, and the drop from 0.81 to 0.52
**Series** (`A_sentiment_timeseries.csv`):
- 2020 COVID trough: 0.03–0.15.
- 2021–22: 0.35–0.59.
- 2023 to FY2025: a plateau of 0.62–0.88 (H1 2024 0.70, FY2024 0.78, CMD 0.77, H1 2025 0.67, FY2025 0.81).

The H1 2026 call scored [0.52](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_Scores_$KEY_Sentiment), against [0.81](https://gam.prontonlp.com/#/ref/$DOCID_T000003676656_$GROUPBY_Scores_$KEY_Sentiment) for FY2025. That is the lowest earnings-call score since the FY2020 call (0.35). Its net event ratio (0.33 [calc]) is the lowest of any call since Q3 2022.

**What moved:**
- investmentScore: [0.83](https://gam.prontonlp.com/#/ref/$DOCID_T000003676656_$GROUPBY_Scores_$KEY_Investment) to [0.2](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_Scores_$KEY_Investment).
- [CurrentState](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_Aspects_$KEY_CurrentState) aspect: 0.75 to 0.40. [Forecast](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_Aspects_$KEY_Forecast) aspect: 0.83 to 0.41. StrategicPosition barely moved (0.97 to 0.93).
- Negative events: 54 to 95.

**It was management, not the Q&A.** Executives fell from 0.82 to 0.54, with negative events up from 53 to 90. Analysts stayed neutral (0.31 to 0). These figures come from A-008 to A-011; ProntoNLP returns the speaker-filtered scores under the document-level URL.

Event types that turned negative or weakened:
- New negatives: [OperationalChallenge](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_EventTypes_$KEY_OperationalChallenge) (-0.80) and [CostChallenge](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_EventTypes_$KEY_CostChallenge) (-0.74).
- [Debt](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119_$GROUPBY_EventTypes_$KEY_Debt): 0.96 to 0.13.
- Fewer celebratory events (CSR, "records", capital returns).

**The 55 negative sentences** (`A_sentiment_drivers.json`) cluster as follows:
- **Macro and insolvencies:** [#59](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-59) [#60](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-60)
- **Middle East energy and commodity costs (EUR 20–25m for the year):** [#73](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-73) [#77](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-77) [#464](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-464)
- **Minimum wages not yet passed through (Germany, UK, LatAm):** [#111](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-111) [#131](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-131) [#147](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-147)
- **Mexico tender loss:** [#139](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-139) [#146](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-146) [#377](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-377)
- **Cash and leverage:** [#26](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-26) [#251](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-251) [#266](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-266) [#276](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-276)
- **No 2027 guidance:** [#521](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-521)

### 2. Management focus (`A_management_focus.json`: 46 cited themes; `A_theme_intensity.csv`; `A_theme_evidence.csv` from 26 searchSentences runs)
I read the H1 2026, FY2025, H1 2025 and FY2024 calls in full. H1 2024 and the CMD were covered by keyword extraction plus targeted reading.

**Top themes by event:**
- **H1 2024:** FY2024 guidance raised (organic 5.2–5.5%, EBITDA margin 35.2–35.5%); pricing discipline and churn normalisation; hedging and productivity; workwear momentum; French politics and the Olympics; Mexico at a record 42% margin.
- **FY2024:** record year but a "valuation disconnect" (9.6x); new capital-allocation policy and EUR 150m buyback; FY2025 guided "slightly up"; Germany margin +450bp; pest control and clean room; US deal discipline.
- **CMD:**
  - 2025–28 targets: +5–6% growth at constant FX (~4% organic), ~+20bp EBITDA margin a year, EBIT and EPS growing faster than revenue, ~EUR 1.5bn cumulative FCF ([#3206](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3206) [#3208](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3208) [#3222](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3222) [#3227](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3227) [#3230](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3230)).
  - Also: valuation gap, large-M&A limits (Vestis was evaluated), pricing power.
- **H1 2025:** LatAm margin -220bp; Mexico tender win described as "massive, super profitable"; EBITDA margin up but EBIT margin down on D&A; Denmark weakness; guidance reaffirmed.
- **FY2025:** record 2025; EUR 500m buyback plus the OCEANE soft call; energy hedging, with "no significant" Middle East impact; FY2026 guidance; EUR 91m of acquired revenue bought for EUR 108m; CSR 2030; LatAm margin expected "at least flat".
- **H1 2026:** Mexico and LatAm; macro; Middle East costs met with mostly temporary savings; record signings implying H2 and 2027 acceleration; wage pass-through; FCF and working capital; leverage; an M&A pipeline "significantly higher than usual".

**Shift over time** [calc]:
- Share of sentences on macro/geopolitics rose from ≤1.6% to 5.2%. Mexico rose from 0.45% to 3.8%. FCF/working capital reached 4.0% and wage inflation 2.4%, both series highs.
- CSR fell from 6.1% to 2.2%.
- Analysts spent 11.3% of their sentences on contracts and volumes, against ≤3.8% before.

### 3. H1 2026 deep dive (`A_h1_2026_results.json`, `A_h1_2026_qa.json`)
Results were published 29-Jul-2026 after market. Figures follow the semi-annual report (SR) where available.

**P&L:**
- Revenue EUR 2,457.1m, +4.9% reported, +3.2% organic [#8](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-8) [#20](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-20).
- Q1 organic +3.1% (revenue EUR 1,180.5m) [#1](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259598338-1); Q2 organic 3.2%. M&A +1.1pp, FX +0.6pp [#200](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-200).
- Adjusted EBITDA EUR 853.8m, **margin 34.7%, flat** [#9](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-9) [#10](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-10).
- Adjusted EBIT EUR 370.0m (+4.6%), margin 15.1%, flat [#11](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-11) [#12](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-12).
- IFRS net income EUR 163.6m, +7.3% against a restated EUR 152.4m [#13](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-13) [#86](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-86).
- Headline net income EUR 215.5m (+1.1%) [#14](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-14).
- Headline diluted EPS **EUR 0.89 (+5.1%)** [#15](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-15). Basic EUR 0.96 (+5.3%) [#237](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-237). IFRS diluted EPS per S&P: EUR 0.68 (+11.5% [calc]).

**Cash flow and balance sheet:**
- FCF after leases **EUR -30.1m**, against +EUR 31m in H1 2025 [#16](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-16) [#190](https://gam.prontonlp.com/#/ref/$SENTID_T000003512646-190).
- Net capex EUR 479.1m, 19.5% of revenue against 18.4% [#246](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-246); about 18% expected for the year [#92](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-92).
- Working capital EUR -164.0m; DSO 57 days against 54 [#93](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-93).
- Net debt EUR 3,670.3m. **Leverage 2.09x**, against 1.75x at Dec-25 and 1.92x at Jun-25 [#103](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-103) [#104](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-104).
- Buyback EUR 466.8m at an average EUR 26.25 [#292](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-292); the programme completed 9 July [#17](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-17).

**Regions (revenue growth / organic / adjusted EBITDA margin):**

| Region | Reported | Organic | Margin (change) | Source |
|---|---|---|---|---|
| France | +2.5% | +2.0% | 42.7% (+90bp) | [#93](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-93) [#97](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-97) |
| Central Europe | +5.9% | +3.2% | 32.0% (-30bp) | [#100](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-100) [#111](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-111) |
| Scandinavia & Eastern Europe | +3.4% | +1.6% | 34.5% (+10bp) | [#115](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-115) [#119](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-119) |
| UK & Ireland | -0.8% | +1.6% | 31.8% (-10bp) | [#55](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-55) [#58](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-58) |
| Latin America | +15.4% | +8.0% | **30.7% (-180bp)** | [#59](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-59) [#66](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-66) |
| Southern Europe | +8.1% | +5.7% | 32.1% (+30bp) | [#152](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-152) [#155](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-155) |
| Others | n/a | n/a | n/a | tables not indexed |

**Guidance:**
- FY2026 objectives were confirmed unchanged against 11-Mar-2026 [#342](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-342) [#116](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-116) [#117](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-117) [#118](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-118) [#119](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-119): organic growth slightly below 2025's 3.8%, slight expansion of EBITDA and EBIT margins, high-single-digit diluted headline EPS growth, mid-single-digit FCF growth, and leverage around 1.65x.
- Qualitatively weaker:
  - Organic growth had been "tracking ahead" until Mexico [#330](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-330).
  - The LatAm margin view reversed, from [#580](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-580) to [#558](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-558).
  - The German contract went from ~EUR 30m a year [#625](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-625) to ~EUR 20m of revenue in 2027 [#108](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-108).
  - The 2027 energy saving went from EUR 10–15m [#641](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-641) to slightly below EUR 10m [#599](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-599).
- **Against the CMD:** organic growth has been below 4% two years running, and adjusted EBIT grew slower than revenue in both FY2025 and H1 2026 (+4.6% vs +4.9%) [calc].

**What analysts pushed on** (`A_h1_2026_qa.json`; 7 analysts from MS, DB, Jefferies, Berenberg, BofA, ODDO and Rothschild Redburn):
- Mexico, raised by three of them. Recovery is not in the forecast [#377](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-377).
- Price versus volume.
- How fast new signings convert. Q2 signings were better than Q1 [#497](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-497).
- DSO, which management called "a couple of days" [#429](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-429).
- Capex timing [#424](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-424).
- Cost savings of about EUR 10m, mostly temporary [#460](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-460) [#467](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-467).
- 2027 organic growth, which management said "will be better" [#524](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-524).
- M&A size: bigger than usual, but no "elephant" [#568](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-568) [#588](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-588).

**FY2025** (`A_fy2025_results.json`):
- Revenue EUR 4,796.8m, organic 3.8%. Adjusted EBITDA EUR 1,701m (35.4%, +20bp). Adjusted EBIT EUR 766.6m (16.0%).
- Diluted headline EPS EUR 1.85 (+5.2%). FCF EUR 358.6m. Leverage 1.75x.
- Every FY2025 guidance item was met **except the adjusted EBIT margin**: guided "slightly up", it came in flat [#384](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-384) [#27](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-27).
- FY2026 guidance as issued in March: [#464](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-464) [#469](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-469) [#472](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-472) [#474](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-474) [#477](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-477).

**Q3 2025:** not available in either source, so I derived it at **~EUR 1,248m [calc]**.
- ProntoNLP has no document at all between Aug-2025 and Jan-2026.
- S&P's "quarterly" revenue is just half-year totals split evenly.

### 4. Consensus (`A_consensus.json`)
ProntoNLP returned **only quarterly revenue, actual against expected**:
- Q2 2026: EUR 1,276.6m vs 1,274.8m, +0.14%.
- Q1 2026: EUR 1,180.5m vs 1,183.1m, -0.22%.
- **H1 2026: in line (-0.03%).**
- Q4 2025: +0.90%.
- Q1–Q3 2025: empty.

EBITDA, epsGaap, net income, capex and FCF series were empty under every interval (year, quarter, last-doc, month). There were **no FY2026E–28E forecasts and no revision history**, so I cannot judge an EPS or EBITDA beat or miss.

On "epsGaap": the name implies IFRS-reported EPS. S&P has FY2025 IFRS diluted EPS at [1.46](https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid=256665099), against the company's headline diluted EUR 1.85 (about 26% higher). The two are not comparable.

### 5. Market reaction (`A_results_day_moves.csv`; daily standard deviation 1.59%)
| Event | Reaction day | Day 1 | 5 days |
|---|---|---|---|
| **H1 2026** | 30-Jul-26 | **-5.68%** (gap -4.14%, z -3.6) | -3.91% |
| Q1 2026 | 5-May-26 | +3.23% | +5.38% |
| FY2025 | 11-Mar-26 | +3.19% (gap +7.74% faded) | +2.47% |
| H1 2025 | 31-Jul-25 | -1.54% | -0.81% |
| CMD | 27-May-25 | +2.13% | +1.96% |
| FY2024 | 6-Mar-25 | **+9.05%** (z 5.7) | +8.95% |
| H1 2024 | 25-Jul-24 | +2.27% | +5.53% |

- Revenue surprises are small (17 quarters: mean +0.9%; 11 beats, 6 misses). The stock moves on narrative and capital returns: FY2024 jumped +9% on the new buyback policy despite a 1.1% revenue miss.
- H1 2026 was in line on revenue with guidance confirmed, yet it produced the worst move in three years. The market appears to have repriced quality and H2 risk: flat margins, negative FCF, 2.09x leverage, the Mexico structural loss and the LatAm reversal.
- The stock is down **18.4%** from the pre-results close to EUR 21.26 on 9-Oct, and down 24.6% from its EUR 28.20 peak on 3-Jul. The buyback completed on 9-Jul [calc].

### 6. Flags (`A_flags.json`, 13 items)
- **OCEANE soft call (high):** the ~1.65x YE leverage target and the EUR 500m buyback assume conversion of the OCEANE 2029, whose debt component is EUR 362m [#517](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-517) [#519](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-519). In March the CFO put the trigger at about EUR 21.5 [#514](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-514). The adjusted ratio [#174](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-174) implies about EUR 20.78 [calc]. Last close EUR 21.26, a cushion of about 2%. Without conversion, leverage would be about 0.2x above target [e].
- **First negative H1 FCF in the sample:** a swing of EUR -61m, from capex +47m and working capital -51m [calc].
- **Impairment indicators** in the Mexico and Chile CGUs, with no impairment taken [#329](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-329).
- **Accounting:** an IFRS 3 restatement of H1 2025 [#251](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-251). Securitisation programme of up to EUR 200m [#498](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-498) and a supplier-finance programme [#253](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-253); utilisation not disclosed.
- **FY2025 one-off:** about EUR 25m of insurance compensation [#251](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-251).
- **Sources disagree on the refinanced 2026 bond:** the SR says EUR 600m [#95](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-95); the call says EUR 350m [#329](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-329).
- **Management changes, not discussed on the call:** Lecharny is leaving and Yann Michel joins the Management Board [#139](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-139) [#142](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000264324010-142).
- **H1 2026 transcript errors:** "35.7%" margin, EBIT "EUR 317m", leverage "2.9x", "180 million shares" bought back, net income "+3.3%". SR figures used instead.

### 7. Data gaps
Forward consensus and EPS/EBITDA consensus; standalone Q3 2025 revenue and organic growth; regional and "Others" revenue in EUR (only in non-indexed tables); no Q1/Q3 call transcripts after Jan-2024; exact OCEANE soft-call test terms; volume data; Q1 2025 release timing (inferred).
