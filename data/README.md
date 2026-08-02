# Japan Activist Screen — data pack

Six CSVs supporting *Japan Activist Screen: Twenty Targets* (August 2026).
UTF-8, comma-delimited, quoted where required. Open directly in Excel
(Data > From Text/CSV, delimiter = comma, encoding = UTF-8).

| File | Grain | Rows |
|---|---|---|
| `01_master_screen.csv` | One row per company — all numeric fields | 20 |
| `02_tsr_detail.csv` | TSR and relative performance | 20 |
| `03_valuation_multiples.csv` | Valuation vs peers | 20 |
| `04_margins_leverage.csv` | Profitability and balance sheet | 20 |
| `05_top5_shareholders.csv` | Long format — 5 holders per company | 100 |
| `06_activist_thesis.csv` | Long format — pitch, actions, angles, support, defence | 220 |

`01_master_screen.csv` is the model-ready file: every column is numeric except
identifiers and ratings, with no symbols, thousands separators or approximation
marks. Join the others to it on `ticker`.

## Units and conventions

| Field pattern | Unit | Note |
|---|---|---|
| `*_jpy_bn` | JPY bn | |
| `*_usd_m` | USD m | Converted at 150 JPY/USD |
| `*_pct` | per cent | Stated as a number, e.g. `-25.0` = -25% |
| `*_pp` | percentage points | Relative performance vs benchmark |
| `*_x` | multiple | e.g. `ev_ebit_x = 11.0` |
| `net_cash_jpy_bn` | JPY bn | Positive = net cash, negative = net debt |
| `net_debt_ebitda_x` | multiple | Negative = net cash position |
| `support_score_1_5` | 1–5 | 5 = very high ease of building support |
| `tier` | 1–3 | 1 = flagship, 3 = asset-backed value |
| `crowded_flag` | Y/N | Y = an activist is already public on the register |

Benchmarks: `sector_tsr_*` are broad sub-sector reference returns;
`topix_tsr_5y_pct` is a constant +55% applied to all names as the index
reference for the five-year horizon.

## Data basis

All figures are **indicative analyst estimates** assembled from public sources
as at August 2026. They establish magnitude, direction and relative ranking for
name selection. They are not terminal-grade and are not position-sizing inputs.
Refresh from Bloomberg, FactSet or company filings before committing capital.

Shareholder data is simplified. Japanese registers are dominated by nominee
trust accounts — Master Trust Bank of Japan and Custody Bank of Japan appear at
the top of almost every listed register — which mask beneficial owners.
Percentages are indicative aggregates; beneficial-ownership work is required on
any name that advances.
