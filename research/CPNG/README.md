# Coupang, Inc. (NYSE: CPNG): research pack, 12 October 2026

**Recommendation: BUY (event-driven, medium conviction).** 12-month target US$21 (+33% vs US$15.82 on 9-Oct-2026). Scenario values: bear US$9.5, base US$21.0, bull US$31.7, probability-weighted US$20.8.

The request named "CPHG US". The only Coupang match in S&P Capital IQ (CIQ C_704377650) and ProntoNLP (704377650) is NYSE: CPNG, which this pack covers.

| File | What it is |
|---|---|
| `Coupang_CPNG_Research_Report.pdf` | Full research report (28 pages, 27 sections plus appendix), with about 670 source links |
| `Coupang_CPNG_Research_Report.docx` | The same report in Word format |
| `Coupang_CPNG_IC_Memo.pdf` | Investment committee memo, 15 slides, in the format of the Sanken Electric memo |
| `Coupang_CPNG_Dashboard.html` | Interactive dashboard (standalone copy). Analyst commentary is editable in place; in this copy, edits are kept in your browser only |
| `Coupang_CPNG_Data_Provenance.pdf` / `.md` | Every connector call, data cut-off, calculation and known gap |
| `mcp_call_log.csv` | The 379 connector calls: arguments, payload size and SHA-256 of each result |
| `charts/` | Chart images used in the report and memo |
| `code/` | Model, valuation, chart, dashboard and provenance scripts |
| `source/` | Report Markdown, memo HTML and stylesheets |

The hosted dashboard is at https://claude.ai/artifact/MTptuuQt9Fd6zH14nXyEYL. It is private to its owner until shared. There, commentary edits are saved for everyone with access and attributed to the editor.

## Data

- **Sources:** S&P Global Capital IQ and ProntoNLP only, through their connectors. No web browsing and no SQL.
- **Citations:** each figure links to its Capital IQ document or ProntoNLP sentence. ‡ marks a figure the tool returned without a link; [d] = derived; [e] = estimate; [u] = unverified.
- **Raw data:** the connector payloads, compacted transcripts and research notes are not in this public repository, because they reproduce licensed S&P Capital IQ and ProntoNLP content. They were delivered privately. The SHA-256 values in the provenance document and the call log let you verify any copy.

## Rebuilding

The scripts in `code/` read the raw data files listed in section 6 of the provenance document. They use the working paths of the session that produced them, so adjust the paths before running.
