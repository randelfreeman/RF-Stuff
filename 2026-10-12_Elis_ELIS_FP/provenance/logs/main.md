# MCP call log — lead analyst (main thread)

Session date: 2026-10-12 (UTC). Calls M-001..M-005 made ~22:08–22:12 UTC; M-006..M-012 ~22:13–22:25 UTC.
Raw responses: `provenance/raw/main/`. S&P Capital IQ responses carried empty `sources` arrays for every line item → "source link unavailable".

| ID | Approx. UTC | Tool | Parameters | Response summary | Raw file |
|---|---|---|---|---|---|
| M-001 | 22:08 | S&P `get_latest` | `{}` | latest annual FY2025; latest quarterly Q3-2026 (database-wide); current date 2026-10-12 | inline below |
| M-002 | 22:08 | S&P `get_info_from_identifiers` | `{"identifiers":["ELIS","Elis SA","FR0012435121"]}` | Elis SA, Operating, Public Company, Commercial Services and Supplies, 58,445 employees, founded 1883, Saint-Cloud (France), company_id C_27989, ticker ENXTPA:ELIS. ISIN lookup error: "Request user missing IDPermission; cannot resolve identifier: FR0012435121 of type: isin" | inline below |
| M-003 | 22:09 | ProntoNLP `getCompanies` | `{"companyNameOrTicker":"Elis"}` | 2 results: Elisa Oyj (1353107) and **Elis SA (27989)**, ticker ELIS, ENXTPA, ISIN FR0012435121, marketCap 5,354,587,562 (USD), originalCap 4,720,068,936 (local), Industrials / Commercial Services and Supplies. User specified "ELIS SA / ELIS FP Equity" → Elis SA (27989) selected; no ambiguity | inline below |
| M-004 | 22:10 | ProntoNLP `getFilterOptions` | `{"filterNames":["documentTypes","speakerTypes","importance"]}` | enumerations of document types (S&P Transcripts, SEC, Non-SEC incl. AR/SR/FIN SUPP, Macro), speaker types, importance levels | inline below |
| M-005 | 22:11 | ProntoNLP `getDocuments` | `{"companiesIds":["27989"],"size":60,"dateRange":{"gte":"2016-01-01","lte":"now"}}` | total 79 docs; 60 newest returned (2019-04 → 2026-07) with document-level sentiment | `005_pronto_getDocuments_elis.csv` (lossless CSV) |
| M-006 | 22:14 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"income_statement","period_type":"annual","calendar_type":"fiscal","start_year":2016,"end_year":2025}` | FY2016–FY2025 income statements, EUR | `006_spcapiq_income_statement_annual_2016_2025.csv` |
| M-007 | 22:17 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"balance_sheet","period_type":"annual","calendar_type":"fiscal","start_year":2016,"end_year":2025}` | FY2016–FY2025 balance sheets, EUR | `007_spcapiq_balance_sheet_annual_2016_2025.csv` |
| M-008 | 22:19 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"cashflow","period_type":"annual","calendar_type":"fiscal","start_year":2016,"end_year":2025}` | FY2016–FY2025 cash-flow statements, EUR | `008_spcapiq_cashflow_annual_2016_2025.csv` |
| M-009 | 22:21 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"income_statement","period_type":"quarterly","num_periods":6}` | FY2025Q1–FY2026Q2 (semi-annual figures split evenly into quarters) | `009_spcapiq_interim_ltm_statements.csv` |
| M-010 | 22:21 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"income_statement","period_type":"ltm","num_periods":1}` | LTM to 30-Jun-2026 | `009_…csv` |
| M-011 | 22:23 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"balance_sheet","period_type":"quarterly","num_periods":2}` | balance sheet 31-Mar-2026 = 30-Jun-2026 (identical) | `009_…csv` |
| M-012 | 22:23 | S&P `get_financial_statement_from_identifiers` | `{"identifiers":["C_27989"],"statement":"cashflow","period_type":"ltm","num_periods":1}` | LTM cash flow to 30-Jun-2026 | `009_…csv` |

## Inline raw responses (small)

**M-001** `{"annual":{"latest_year":2025},"quarterly":{"latest_quarter":3,"latest_year":2026},"now":{"current_year":2026,"current_quarter":4,"current_month":10,"current_date":"2026-10-12"}}`

**M-002** `{"results":{"ELIS":{"name":"Elis SA","status":"Operating","type":"Public Company","simple_industry":"Commercial Services and Supplies","number_of_employees":"58445.0000","founding_date":"1883-01-01","webpage":"www.fr.elis.com/en","address":"5 Boulevard Louis Loucheur","city":"Saint-Cloud","zip_code":"92210","state":"Ile-de-France","country":"France","iso_country":"FRA","company_id":"C_27989","ticker":"ENXTPA:ELIS"},"Elis SA":{…identical…}},"errors":["Request user missing IDPermission; cannot resolve identifier: FR0012435121 of type: isin"]}`

**M-003** `{"total":2,"results":[{"companyId":"1353107","companyName":"[Elisa Oyj](https://gam.prontonlp.com/#/ref/$COMPANY_1353107)","GVKEY":"234087","marketCap":6242365286,"country":"FI","ticker":"ELISA","CIK":"0001624367","displayName":"[Elisa Oyj (ELISA)](https://gam.prontonlp.com/#/ref/$COMPANY_1353107)","subSector":"Diversified Telecommunication Services","hqCountry":"Finland","ISIN":"FI0009007884","updateFromCorpus":"transcripts","originalCap":5571935254,"collapseKey":"1353107","exchange":"HLSE","webpage":"elisa.com","sector":"Communication Services"},{"companyId":"27989","companyName":"[Elis SA](https://gam.prontonlp.com/#/ref/$COMPANY_27989)","GVKEY":"319230","marketCap":5354587562,"country":"FR","ticker":"ELIS","CIK":"0002127861","displayName":"[Elis SA (ELIS)](https://gam.prontonlp.com/#/ref/$COMPANY_27989)","subSector":"Commercial Services and Supplies","hqCountry":"France","ISIN":"FR0012435121","updateFromCorpus":"transcripts","originalCap":4720068936,"collapseKey":"27989","exchange":"ENXTPA","webpage":"www.fr.elis.com/en","sector":"Industrials"}]}`

**M-004** documentTypes — S&P Transcripts: Earnings Calls, Company Conference Presentations, Shareholder/Analyst Calls, Special Calls, Analyst/Investor Day, M&A Calls, Sales/Trading Statement Calls, Guidance/Update Calls, Interim Management Statement Calls, Operating Results Calls, Fixed Income Calls, Annual General Meeting; SEC Filings: 8-K, 6-K, 10-Q, 10-K, 20-F, 40-F; Non-SEC Filings: QR, SR, Tanshin, Yuho, ARS, FIN SUPP, AR, Other Financials, Sustainability Report; Expert Network: COMMUNITY, FORUM, PRIMER; Macro: frb.* / ecb.* / boe.* series. speakerTypes: Analysts, Operator, Executives, Attendees, Shareholders, Executives_CEO, Executives_CFO, Executives_IR, Executives_Board, Executives_VP, Executives_Director, Executives_COO, Executives_President, Executives_CMO, Executives_CCO, Executives_CSO, Executives_ChiefOfficer, Executives_CIO, Executives_CTO, Executives_CRO, Executives_CLO, Executives_CPO, Executives_CBO, Executives_CDO, Executives_CAO, Executives_CGO. importance: High, Medium, Low.

## Non-MCP inputs
- Client-supplied template: `Sanken_Electric_6707_IC_Memo_EN.pdf` (17 pages) — read for format only (layout/sections of the IC memo). No data from it is used.
- Web browsing: none. Financial_Datasets connector: not used (non-S&P source). SQL: none.

## Line items with Capital IQ doc-viewer source links (~22:55 UTC)
S&P statement-level calls (M-006..M-012) return empty `sources`; the line-item endpoint returns a Capital IQ doc-viewer URL per value (FY2017 onward). These are now used to hyperlink headline S&P figures.

| ID | Tool | Parameters | Response summary | Raw file |
|---|---|---|---|---|
| M-013 | S&P `get_financial_line_item_from_identifiers` | `{"identifiers":["C_27989"],"line_item":"total_revenue","period_type":"annual","calendar_type":"fiscal","start_year":2016,"end_year":2025}` | Total revenues FY2016–FY2025 with doc-viewer links FY2017+ | `013_018_spcapiq_line_items_with_sources.csv` |
| M-014 | same tool | `line_item: "ebita"` (same period params) | EBITA FY2016–FY2025 (S&P standardised) | same |
| M-015 | same tool | `line_item: "ebit"` | EBIT FY2016–FY2025 | same |
| M-016 | same tool | `line_item: "cash_from_operations"` | CFO FY2016–FY2025 | same |
| M-017 | same tool | `line_item: "capital_expenditure"` | Capex FY2016–FY2025 | same |
| M-018 | same tool | `line_item: "gross_profit"` | Gross profit FY2016–FY2025 | same |
