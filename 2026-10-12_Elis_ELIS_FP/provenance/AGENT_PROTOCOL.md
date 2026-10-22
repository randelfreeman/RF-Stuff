# Research-agent protocol — Elis SA (ELIS FP) deep-dive

Read this fully before making any tool call. The client is a hedge fund (event-driven / special situations). Accuracy, sourcing and provenance are non-negotiable.

## 1. Permitted data sources (hard rule)
- ONLY these MCP tools may be used as data sources:
  - S&P Global / Capital IQ: `mcp__S_P_-_Deterministic_Retrieval__*` (financial statements, line items, company info, history metadata, get_latest).
  - ProntoNLP: `mcp__Pronto__*` (S&P transcripts, non-US filings (AR = annual report / universal registration document, SR = semi-annual report, FIN SUPP = results releases/presentations), consensus, stock prices, peers, sentiment analytics).
- Load tool schemas first with ToolSearch, e.g. `select:mcp__Pronto__searchSentences,mcp__Pronto__getDocuments` (deferred tools cannot be called until loaded).
- FORBIDDEN: WebSearch, WebFetch, curl/wget to the internet, `mcp__Financial_Datasets__*`, any other connector, `mcp__Pronto__deepResearch`, `mcp__Pronto__showDocumentMindMap`.
- Do not use your own background knowledge as a data source. If you add context from memory, label it `[u]` (unverified, not from S&P/ProntoNLP) and keep it minimal. Your own calculations are `[calc]`; estimates `[e]`.

## 2. Identifiers (already resolved — do not re-resolve Elis)
- Elis SA: S&P Capital IQ company_id `C_27989` (ticker ENXTPA:ELIS, reporting currency EUR, FY = calendar year). ProntoNLP companyId `"27989"` → always pass `companiesIds: ["27989"]`.
- Elis document IDs (ProntoNLP) are listed in `/home/user/RF-Stuff/ELIS_FP/provenance/raw/main/005_pronto_getDocuments_elis.csv` (earnings calls `T…`, filings `NONSEC…`). Key ones:
  - H1 2026 earnings call (29-Jul-2026): T000003774119 ; H1 2026 semi-annual report: NONSEC000264346860, NONSEC000264324010
  - FY2025 earnings call (11-Mar-2026): T000003676656 ; FY2025 annual report/URD: NONSEC000259591248 ; FY2025 results supp: NONSEC000256665099 ; Q1 2026 supp: NONSEC000259598338
  - Capital Markets Day (27-May-2025): T000003468571
  - H1 2025 call: T000003512646 ; H1 2025 SR: NONSEC000245135173
  - FY2024 call: T000003394029 ; FY2024 AR/URD: NONSEC000239166805 (also NONSEC000237931084)
  - H1 2024 call: T000003194583 ; FY2023 call: T000003054377 ; Special call 4-Sep-2023: T000002901783
  - FY2022 call: T000002760050 ; FY2022 AR: NONSEC000202465426 ; FY2021 call: T000002520475 ; FY2021 AR: NONSEC000180181407
  - FY2020 call: T000002232515 ; H1 2022 call: T000002606072 ; H1 2023 call: T000002859132 ; H1 2021 call: T000002352962
- Today is 2026-10-12. Latest S&P annual = FY2025; latest interim = H1 2026 (30-Jun-2026).

## 3. Provenance logging (mandatory for EVERY MCP call)
- Your agent code is given in your task (e.g. `A_earnings`). Log file: `/home/user/RF-Stuff/ELIS_FP/provenance/logs/<code>.md`. Raw folder: `/home/user/RF-Stuff/ELIS_FP/provenance/raw/<code>/`.
- For every call: sequential id (`<code>-001`, `<code>-002`, …), UTC timestamp (get it with Bash `date -u +%FT%TZ`; one timestamp per batch of parallel calls is fine), tool name, full parameters as JSON, one-line description of the response, and the raw file path.
- Save every response VERBATIM to `raw/<code>/<NNN>_<tool>.json` (or `.txt`). If a response is very large you may save a lossless re-encoding (CSV/JSONL keeping every field and every citation URL) and say so in the log. Never alter values. If a call errors, log the error text too.
- You may write log entries in batches, but every call must appear. Do not overwrite other agents' files.

## 4. Citations
- ProntoNLP results embed links: `text [#N](url)` for sentences, `[Label](url)` for entities/documents. Copy them EXACTLY; never construct or infer URLs; never rename markers.
- Every figure/quote you report from ProntoNLP must carry its link. When paraphrasing several sentences, keep all their markers.
- S&P Capital IQ responses contain empty `sources` arrays → cite as `S&P Capital IQ (C_27989 or the peer id), source link unavailable`.
- If something cannot be found in permitted sources, say so explicitly (`not available in S&P/ProntoNLP`) — never fill gaps with guesses.

## 5. Outputs
- Detailed findings (markdown, with citations, tables): `/home/user/RF-Stuff/ELIS_FP/provenance/<code>_findings.md`.
- Structured data (numbers you extracted or computed) as JSON or CSV in `/home/user/RF-Stuff/ELIS_FP/model/` with a `<code>_` prefix; include a `source` column/field holding the citation link or "S&P Capital IQ, source link unavailable".
- Final message back to the lead analyst: concise but complete summary (target ≤ 2,500 words): key findings, key numbers with citation links, what you could not find, and file paths. The lead will read your files for detail.
- Precision: quote numbers exactly as sourced with units/currency and period; distinguish reported vs organic growth, IFRS vs adjusted/headline metrics, and pre- vs post-IFRS 16.
- ProntoNLP usage tips: `searchSentences` needs a short `topicSearchQuery` (2–4 words); scope with `transcriptsIds` (best) or `companiesIds`; raise `size` (e.g. 50–100) when analysing a document; use `similarityThreshold: "Low"`/`"Very Low"` if results are thin; numeric tables in filings are not indexed but prose around them is, and earnings-call transcripts usually state the key numbers verbally. Try a few phrasings before concluding something is absent.
- Do NOT run git commands (the lead handles git). Work only inside `/home/user/RF-Stuff/ELIS_FP/`.
