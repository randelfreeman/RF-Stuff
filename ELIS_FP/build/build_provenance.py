"""Compile the data-provenance document from the call logs, raw-file index, model scripts and build scripts."""
import os, re, glob, hashlib, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
P = lambda *a: os.path.join(ROOT, *a)
logs = sorted(glob.glob(P('provenance', 'logs', '*.md')), key=lambda f: (not f.endswith('main.md'), f))
rows = {os.path.basename(f): len([l for l in open(f) if re.match(r'^\| *[A-Za-z_]*-?\d{3}', l)]) for f in logs}
out = ['# Elis SA (ELIS FP) — data-provenance record', '',
       'Companion to `Elis_ELIS_FP_Equity_Research_Report.pdf/.docx` and `Elis_ELIS_FP_IC_Memo.pdf`. Compiled 13-Oct-2026 from the working files in `ELIS_FP/` by `build/build_provenance.py`.', '',
       '## 1. Scope and rules', '',
       '- **Permitted sources:** S&P Global Capital IQ (S&P Deterministic Retrieval connector) and ProntoNLP (S&P transcripts, company filings, prices, consensus, peer graph, sentiment). Nothing else.',
       '- **Web fetches / web searches:** none. **Financial Datasets connector:** not used. **SQL:** none — all calculations are Python scripts listed in Section 4.',
       '- **Client-supplied file:** `Sanken_Electric_6707_IC_Memo_EN.pdf`, used only as a layout template for the IC memo; no data taken from it.',
       '- **Citations:** ProntoNLP sentence/document links (`gam.prontonlp.com/#/ref/...`) and Capital IQ document-viewer links (`capitaliq.spglobal.com/.../docviewer?mid=...`) are copied verbatim from tool responses. S&P statement-level calls returned empty `sources` arrays; figures from them are flagged "S&P, link n/a" / "source link unavailable".',
       '- **Labels:** [calc] analyst calculation; [e] estimate; [u] unverified (not confirmed in permitted sources).', '',
       '## 2. Data freshness', '',
       '| Dataset | As of |', '|---|---|',
       '| S&P Capital IQ annual statements | FY2016–FY2025 (FY ends 31-Dec); latest annual = FY2025 (`get_latest`, 12-Oct-2026) |',
       '| S&P interim / LTM | LTM to 30-Jun-2026; Elis reports semi-annually, S&P "quarters" are half-years split evenly |',
       '| Share price | ProntoNLP daily close 9-Oct-2026 (€21.26); retrieved 12-Oct-2026 |',
       '| Latest company documents | H1 2026 semi-annual report and call (29-Jul-2026); ProntoNLP upcoming-event listings for Q3 2026 (28-Oct-2026) |',
       '| Peer financials | S&P Capital IQ LTM to each peer\'s latest reported period (e.g. Cintas Aug-2026, Sodexo Feb-2026) |',
       '| Connector calls | 12-Oct-2026 ~22:08 UTC to 13-Oct-2026 (timestamps in each log) |', '',
       '## 3. Connector calls by workstream', '',
       '| Log | Workstream | Logged calls |', '|---|---|---|']
names = {'main.md': 'Lead analyst: identifiers, S&P statements, line items with links', 'A_earnings.md': 'Earnings calls, sentiment, results vs consensus', 'B_governance.md': 'Management, board, shareholders, returns', 'C_mna_capital.md': 'M&A, debt, capital structure, stakes, strategy', 'D_price_catalysts.md': 'Prices, ±10% moves, timeline, catalyst calendar', 'E_peers_valuation.md': 'Peers, multiples, regression', 'F_segments_kpis.md': 'Segments, geographies, KPIs', 'G_business_model.md': 'Business model, macro, moat, supply chain'}
for f in logs:
    b = os.path.basename(f); out.append(f'| `provenance/logs/{b}` | {names.get(b, "")} | {rows[b]} |')
out += [f'| **Total** | | **{sum(rows.values())}** |', '',
        'Workers B, C, E and F stopped before finishing because of connector rate limits (HTTP 429). Their logs contain every call that completed, but only B_governance.md notes the rate limit itself. The lead analyst used their saved raw data and completed the peer multiples (`model/E_compute_lead.py`) and the remaining write-ups.', '',
        '## 4. Model calculations (no SQL)', '', '| Script | Inputs | Outputs | What it computes |', '|---|---|---|---|',
        '| `model/main_history.py` | `provenance/raw/main/006–009` | `main_history.csv/.json` | Margins, FCF, leverage, returns, working-capital days from S&P statements |',
        '| `model/main_forecast.py` | history + company guidance (A_*) | `main_forecast.json` | FY2026–28 base/bear/bull P&L, EPS, FCF, scenario values |',
        '| `model/main_valuation.py` | history, ProntoNLP year-end prices | `main_valuation_history.json` | Historical EV/Sales, EV/EBITDA, EV/EBIT, P/E |',
        '| `model/E_compute_lead.py` | `provenance/raw/E_peers_valuation/*` | `E_peer_multiples_lead.json` | Peer LTM multiples; OLS EV/Sales on EBIT margin (n = 12, R² 0.86) |',
        '| `model/D_compute.py` | `provenance/raw/D_price_catalysts/*` | `D_*.csv/json` | Daily returns, ±10% episodes (1–20 trading days), relative moves, z-scores |',
        '| `charts/*.py` | model outputs | `charts/*.png` | All charts in the report and memo |', '',
        'Key formulas: EV = market cap (S&P shares × ProntoNLP close) + S&P net debt incl. leases + minorities; leverage (company) = net financial debt excl. IFRS 16 / adjusted EBITDA; FCF yield = FCF after leases / market cap; target = average of 12.5x FY2027E headline EPS, 5.5x FY2027E adjusted EBITDA (post-OCEANE share count) and a 7% FY2027E FCF yield.', '',
        '## 5. Raw-response index', '', '| Folder | Files | Size (KB) |', '|---|---|---|']
for d in sorted(glob.glob(P('provenance', 'raw', '*'))):
    fs = [f for f in glob.glob(d + '/*') if os.path.isfile(f)]
    out.append(f'| `provenance/raw/{os.path.basename(d)}/` | {len(fs)} | {sum(os.path.getsize(f) for f in fs) // 1024:,} |')
out += ['', 'Findings write-ups: `provenance/A_earnings_findings.md`, `provenance/D_price_catalysts_findings.md`, `provenance/G_business_model_findings.md`. Worker protocol: `provenance/AGENT_PROTOCOL.md`.', '',
        '## 6. Build pipeline', '', '- Report: `build/report/s*.js` (section modules) → `build/build_report.js` (docx-js) → DOCX → LibreOffice → PDF. Contents page numbers from a first-pass PDF (`build/make_toc.py`).',
        '- IC memo: `build/build_memo.py` (HTML slides, `memo_lib.py`) → Chromium (`html2pdf.js`) → PDF.', '',
        '## 7. Full call logs', '']
for f in logs:
    out += [f'### {os.path.basename(f)}', '', open(f).read().strip(), '']
open(P('Elis_ELIS_FP_Data_Provenance.md'), 'w').write('\n'.join(out))
print(sum(rows.values()), 'calls')
