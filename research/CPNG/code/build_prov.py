"""Generate the data-provenance document (Markdown) and a CSV call log for the Coupang research pack."""
import csv, gzip, hashlib, json, os, re, collections, datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
S = "https://gam.prontonlp.com/#/ref/$SENTID_"
D = "https://gam.prontonlp.com/#/ref/$DOCID_"
C = "https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid="

calls = [json.loads(l) for l in gzip.open("prov/mcp_calls_full.jsonl.gz", "rt")]
WS = {"main": ("Lead", "Lead analyst session: identification, core financials, peers, prices, consensus, deals", "report, model"),
      "agent-ab36d0a3c8f8282be": ("A", "Earnings, segments, data incident, guidance, call sentiment", "notes/A_earnings_segments.md"),
      "agent-a98d6876ce7312d64": ("B", "Stock-move attribution, event history, strategy, M&A, capital return", "notes/B_catalysts_history.md"),
      "agent-a94d55986aa1175f6": ("C", "Governance, management, ownership, insiders", "notes/C_governance_ownership.md"),
      "agent-a41ad9d7b35f3b845": ("D", "Capital structure, liquidity, forensic accounting", "notes/D_capital_accounting.md"),
      "agent-ad36a039b2d75ed1f": ("E", "Supply chain, competition, markets, regulation, M&A", "notes/E_supplychain_competition.md")}
conn = lambda t: "S&P Capital IQ" if "S_P_" in t else "ProntoNLP"
tool = lambda t: t.split("__")[-1]
sha = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()


def fsha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def short(v, n):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    return s if len(s) <= n else s[: n - 1] + "…"


def ids(v, n=2):
    if isinstance(v, list):
        return ",".join(str(x) for x in v[:n]) + (f" (+{len(v) - n})" if len(v) > n else "")
    return str(v)


def args_of(u):
    a = u["input"] or {}
    t = tool(u["tool"])
    parts = []
    if t == "searchSentences":
        q = a.get("topicSearchQuery") or a.get("searchQueries") or ""
        parts.append('q="' + short(q, 70) + '"')
        for k in ("companiesIds", "transcriptsIds", "sections", "documentTypes", "corpus", "dateRange", "numberOfCompanies"):
            if k in a: parts.append(f"{k}={short(ids(a[k]) if isinstance(a[k], list) else a[k], 40)}")
    elif t == "getSentenceContext":
        parts.append("sentenceIds=" + ids(a.get("sentenceIds", []), 1))
        parts.append(f"before={a.get('beforeSentence')}, after={a.get('afterSentence')}")
    elif t.startswith("get_financial") or t in ("get_info_from_identifiers", "get_history_metadata_from_identifiers"):
        parts.append("ids=" + ids(a.get("identifiers", []), 3))
        for k in ("line_item", "statement", "period_type", "num_periods", "start_year", "end_year", "calendar_type"):
            if k in a: parts.append(f"{k}={a[k]}")
    else:
        for k, v in a.items():
            parts.append(f"{k}={short(ids(v) if isinstance(v, list) else v, 40)}")
    return short("; ".join(parts), 150).replace("|", "\\|")


# ---------- CSV log ----------
with open("prov/mcp_call_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["seq", "timestamp_utc", "workstream", "connector", "tool", "arguments_json", "result_chars", "result_sha256", "status"])
    for u in calls:
        r = u.get("result", "")
        w.writerow([u["seq"], u["ts"], WS[u["agent"]][0], conn(u["tool"]), tool(u["tool"]), json.dumps(u["input"], ensure_ascii=False),
                    u.get("result_chars", 0), sha(r), "error" if u.get("is_error") else "ok"])

# ---------- summaries ----------
by_ws = collections.OrderedDict((k, collections.Counter()) for k in WS)
by_tool = collections.Counter()
for u in calls:
    by_ws[u["agent"]][conn(u["tool"])] += 1
    by_tool[(conn(u["tool"]), tool(u["tool"]))] += 1
errs = [u for u in calls if u.get("is_error")]
persisted = [u for u in calls if "saved to" in (u.get("result") or "")[:400]]
t0, t1 = calls[0]["ts"], calls[-1]["ts"]

# most-cited documents in the report
rep = open("report.md").read()
doc_counts = collections.Counter(re.findall(r"\$SENTID_([A-Z]+\d+)-\d+", rep))
mid_counts = collections.Counter(re.findall(r"docviewer\?mid=(\d+)", rep))
TITLES = {"SEC000255973354": "Coupang 10-K FY2025 (filed 26-Feb-2026)", "SEC000264559057": "Coupang 10-Q Q2 2026 (4-Aug-2026)",
          "SEC000259645823": "Coupang 10-Q Q1 2026", "T000003779883": "Q2 2026 earnings call (4-Aug-2026)",
          "T000003711263": "Q1 2026 earnings call (5-May-2026)", "T000003665452": "Q4 2025 earnings call (26-Feb-2026)",
          "T000003578475": "Q3 2025 earnings call (4-Nov-2025)", "SEC000253203320": "8-K: data incident and Korea CEO change (Dec-2025)",
          "SEC000261784634": "8-K: PIPC fines (Jun-2026)", "SEC000264557825": "8-K: Q2 2026 results release (4-Aug-2026)",
          "SEC000255972090": "8-K: Q4/FY2025 results release (26-Feb-2026)", "SEC000237406755": "8-K: Q4/FY2024 results release",
          "SEC000218768452": "8-K: Q4/FY2023 results release", "SEC000200362169": "8-K: Q4/FY2022 results release",
          "SEC000237408246": "Coupang 10-K FY2024", "SEC000177952319": "Coupang 10-K FY2021", "SEC000239328925": "8-K: Greenoaks/Surpique buyout (Apr-2025)",
          "SEC000263635795": "Uber 8-K: Delivery Hero offer (Jul-2026)", "NONSEC000256804358": "NAVER FY2025 annual report",
          "T000003215027": "Q2 2024 earnings call", "T000003441812": "Q1 2025 earnings call", "T000003041770": "Q4 2023 earnings call"}
MIDS = {"255973354": "FY2025 10-K statements", "264559057": "Q2 2026 10-Q statements", "259645823": "Q1 2026 10-Q statements",
        "237408246": "FY2022 statements (FY2024 10-K filing set)", "218853463": "FY2021 statements", "251149107": "Q3 2024 10-Q statements"}

# raw and working files
FILES = [
    ("raw/sp_cpng_core.json", "Coupang annual and quarterly statements, EBITDA, EPS, shares, statement links (S&P)", "4-13, 369-374"),
    ("raw/pronto_market.json", "Transcript ids, call sentiment scores and event counts, weekly closes at key dates, consensus (ProntoNLP)", "lead Pronto calls"),
    ("raw/cpng_weekly.py", "292 weekly closes, 8-Mar-2021 to 5-Oct-2026 (ProntoNLP getStockPrices)", "getStockPrices"),
    ("raw/peers.py", "Peer inputs: prices, diluted shares, LTM revenue, EBITDA, EBIT, net income, net debt; EV and multiple formulas", "44, 59-73"),
    ("raw/peers_calc.json", "Peer multiples output", "derived"), ("raw/peers2.py", "FCF yield and peer medians", "378-379"),
    ("raw/peers_final.json", "Peer table with medians (used in the report and dashboard)", "derived"),
    ("raw/regression.json", "OLS coefficients, EV/Sales on EBIT margin", "derived"),
    ("raw/hist_mult.json", "Coupang year-end EV/Sales history", "derived"), ("raw/hist_rel.py", "Core-peer year-end EV/Sales history", "343-345"),
    ("raw/hist_rel.json", "Core-peer medians by year-end", "derived"), ("raw/deals.json", "Precedent transactions with sources", "362-368 and Pronto"),
    ("raw/events.json", "Price-chart catalyst annotations", "workstream B"), ("raw/model.json", "EPS model output, three scenarios", "derived"),
    ("raw/valuation.json", "Scenario valuation output", "derived"),
    ("raw/q2_26.txt", "Compacted Q2 2026 call transcript (ProntoNLP readDocuments)", "workstream A"),
    ("raw/q1_26.txt", "Compacted Q1 2026 call transcript", "workstream A"), ("raw/q4_25.txt", "Compacted Q4 2025 call transcript", "workstream A"),
    ("raw/q3_25.txt", "Compacted Q3 2025 call transcript", "workstream A"), ("raw/pr_q4_25.txt", "Q4 2025 results release excerpt", "workstream A"),
    ("notes/A_earnings_segments.md", "Workstream A research notes with citations and tool log", "agent A"),
    ("notes/B_catalysts_history.md", "Workstream B research notes", "agent B"), ("notes/C_governance_ownership.md", "Workstream C research notes", "agent C"),
    ("notes/D_capital_accounting.md", "Workstream D research notes", "agent D"), ("notes/E_supplychain_competition.md", "Workstream E research notes", "agent E"),
    ("prov/mcp_calls_full.jsonl.gz", "Every connector call with its full arguments and full returned payload", "all 379"),
]
CODE = [("model.py", "EPS model FY2026E-FY2028E, three scenarios"), ("valuation.py", "Scenario valuation and probability weighting"),
        ("raw/peers.py", "EV and multiples"), ("raw/peers2.py", "FCF yield, peer medians"), ("raw/hist_rel.py", "Own-history multiples"),
        ("charts_a.py", "Regression, annual, quarterly and history charts"), ("charts_b.py", "Sentiment and price charts"),
        ("charts_c.py", "Segment, margin and scenario charts"), ("charts_d.py", "EBITDA bridge"), ("prov/extract.py", "Call-log extraction from the session transcripts")]
DELIV = [("out/Coupang_CPNG_Research_Report.pdf", "Research report (PDF, 28 pages)"), ("out/Coupang_CPNG_Research_Report.docx", "Research report (Word)"),
         ("out/Coupang_CPNG_IC_Memo.pdf", "Investment committee memo (15 slides)"), ("dash/Coupang_CPNG_Dashboard_standalone.html", "Interactive dashboard, standalone copy (repo file `Coupang_CPNG_Dashboard.html`); the same page is published privately on claude.ai")]

model = json.load(open("raw/model.json"))
val = json.load(open("raw/valuation.json"))
reg = json.load(open("raw/regression.json"))
pf = json.load(open("raw/peers_final.json"))
F26 = model["F26"]
SC = model["scen"]

L = []
w = L.append
w("---\ntitle: \"Coupang, Inc. (NYSE: CPNG): data provenance\"\nsubtitle: \"Every connector call, raw data file, calculation and data cut-off behind the research pack\"\ndate: \"12 October 2026\"\nlang: en-GB\n---\n")
w("## 1. Scope and rules applied\n")
w("| Item | What was used |\n|---|---|")
w("| Data sources | S&P Global Capital IQ through the *S&P - Deterministic Retrieval* connector, and ProntoNLP through the *Pronto* connector. Nothing else. |")
w("| Web fetches | **None.** The session and agent transcripts contain no WebFetch or WebSearch calls (checked across all six transcripts). |")
w("| SQL | **None.** No database queries were written or run. |")
w("| User-supplied material | The Sanken Electric IC memo PDF, used only as a layout template. The *Asian Century Stocks* newsletter text (11-Oct-2026) pasted into the chat, treated as claims to verify, not as data (report section 27). |")
w("| Other network use | React 18.3.1, ReactDOM 18.3.1 and htm 3.1.1 were downloaded from the npm registry to render the dashboard locally for checking; probes of cdnjs and jsDelivr were refused by the proxy. One GitHub call checked the target repository's visibility. The published dashboard loads those libraries from cdnjs/jsDelivr and its fonts from Google Fonts. None of these carry research data. |")
w("| Analyst knowledge | A few board biographies are marked [u] (unverified) because the proxy statement is not in the connectors. They are context only. |")
w("| Symbols | ‡ = figure returned without a source link (\"source link unavailable\"); [d] = derived from cited inputs; [e] = analyst estimate; [u] = unverified. |\n")

w("## 2. Deliverables covered\n")
w("| File | Description | SHA-256 (first 16) |\n|---|---|---|")
for p, d in DELIV:
    w(f"| `{os.path.basename(p).replace('_standalone', '')}` | {d} | `{fsha(p)[:16]}` |")
w("| `Coupang_CPNG_Data_Provenance.pdf` / `.md` | This document | n.a. |")
w("| `mcp_call_log.csv` | Machine-readable call log: arguments, result size and SHA-256 of each returned payload | n.a. |\n")
w("Dashboard link (private to the owner until shared): https://claude.ai/artifact/MTptuuQt9Fd6zH14nXyEYL\n")

w("## 3. Connector calls\n")
w(f"**{len(calls)} calls** between {t0[:19].replace('T', ' ')} and {t1[:19].replace('T', ' ')} UTC on 12-Oct-2026: "
  f"**{sum(1 for u in calls if conn(u['tool']) == 'S&P Capital IQ')} to S&P Capital IQ** and **{sum(1 for u in calls if conn(u['tool']) == 'ProntoNLP')} to ProntoNLP**. "
  f"{len(errs)} returned errors. Appendix A lists every call; `mcp_call_log.csv` holds the full arguments and a SHA-256 of each returned payload.\n")
w("**By workstream**\n")
w("| Workstream | Scope | Output | S&P | ProntoNLP | Total |\n|---|---|---|---|---|---|")
for k, (code, scope, outp) in WS.items():
    c = by_ws[k]
    w(f"| {code} | {scope} | `{outp}` | {c['S&P Capital IQ']} | {c['ProntoNLP']} | {sum(c.values())} |")
w(f"| **Total** | | | **{sum(c['S&P Capital IQ'] for c in by_ws.values())}** | **{sum(c['ProntoNLP'] for c in by_ws.values())}** | **{len(calls)}** |\n")
w("**By tool**\n")
w("| Connector | Tool | Calls | What it returned |\n|---|---|---|---|")
DESC = {"get_financial_line_item_from_identifiers": "Line items (revenue, EBITDA, EBIT, net income, net debt, shares, CFO, capex) by period, with doc-viewer links",
        "get_financial_statement_from_identifiers": "Full income statement, balance sheet and cash flow by period (statement-level links only)",
        "get_info_from_identifiers": "Company identity: CIQ id, ticker, industry, employees", "get_latest": "Latest available fiscal periods",
        "get_history_metadata_from_identifiers": "Listing and identifier history", "searchSentences": "Cited sentences from filings and transcripts",
        "getSentenceContext": "Sentences around a cited sentence", "readDocuments": "Full transcript or filing text",
        "getStockPrices": "Daily, weekly or quarterly price bars", "getDocuments": "Document lists with sentiment scores",
        "getCompanies": "Company resolution (CPNG id 704377650)", "getCompanyConsensus": "Quarterly consensus vs actuals",
        "getCompanyPeers": "Peer and competitor relations", "getAnalytics": "Event and topic analytics per call",
        "getFilterOptions": "Valid filter values", "getSpeakers": "Executives and analysts on calls"}
for (cn, t), n in sorted(by_tool.items(), key=lambda x: (x[0][0], -x[1])):
    w(f"| {cn} | `{t}` | {n} | {DESC.get(t, '')} |")
w("")
w("**Calls that returned errors**\n")
for u in errs:
    w(f"- #{u['seq']} `{tool(u['tool'])}` ({WS[u['agent']][0]}): {short((u.get('result') or '').replace(chr(10), ' '), 220)}")
w(f"\n**Large results saved to file by the harness:** {len(persisted)} `readDocuments` results (full transcripts and filings) exceeded the inline limit. "
  "They were read in parts by the agents and are retained in the session's tool-results folder; their payload hashes are in the call log.\n")

w("## 4. Data freshness\n")
w("| Dataset | Coverage and cut-off | Source |\n|---|---|---|")
w(f"| Coupang annual financials | FY2021-FY2025 (FY2025 10-K filed 26-Feb-2026) | S&P Capital IQ ([FY2025 statements]({C}255973354)) |")
w(f"| Coupang quarterly financials | 3Q24-2Q26 (10-Q for the quarter to 30-Jun-2026) | S&P Capital IQ ([Q2 2026 statements]({C}264559057)) |")
w("| S&P 'latest period' check | Latest annual 2025; current date 2026-10-12 (call #3) | S&P Capital IQ |")
w("| Peer financials | LTM to Jun-2026 (Walmart Jul-2026); FY2021-FY2025 history for the core peers | S&P Capital IQ |")
w("| Share prices | Weekly closes 8-Mar-2021 to the week of 5-Oct-2026; reference close US$15.82 on 9-Oct-2026 ‡ | ProntoNLP price series |")
w(f"| Earnings calls | Q4 2023 to Q2 2026; latest [4-Aug-2026]({D}T000003779883). Next call listed for 3-Nov-2026 | ProntoNLP (S&P transcripts) |")
w(f"| SEC filings | To the Q2 2026 10-Q ([4-Aug-2026]({D}SEC000264559057)) and 8-Ks through Aug-2026; no proxy, S-1, 13D/G or Form 4 indexed | ProntoNLP |")
w("| Consensus | Quarterly to 2Q26. 3Q26/4Q26 entries carry an effective date of 6-Mar-2025 (stale) and were not used; EPS returned scaled x1e6 ‡ | ProntoNLP getCompanyConsensus |")
w("| Sentiment scores | Per-call document sentiment and event counts, Q4 2023 to Q2 2026 | ProntoNLP getDocuments / getAnalytics |\n")

w("## 5. Most-cited source documents\n")
w("| Document | Citations in the report | Link |\n|---|---|---|")
for did, n in doc_counts.most_common(18):
    w(f"| {TITLES.get(did, did)} | {n} | [{did}]({D}{did}) |")
for mid, n in mid_counts.most_common(6):
    w(f"| S&P doc viewer: {MIDS.get(mid, 'statement document ' + mid)} | {n} | [mid {mid}]({C}{mid}) |")
w(f"\nThe report carries {len(re.findall(r'https://gam\.prontonlp\.com|https://www\.capitaliq\.spglobal\.com', rep))} source links in total.\n")

w("## 6. Raw data and working files\n")
w("These files hold the data as returned by the connectors and the intermediate results. They are kept with the session and supplied privately. They are **not** committed to the public GitHub repository, because they reproduce licensed S&P Capital IQ and ProntoNLP content. The SHA-256 values let you check any copy against this record.\n")
w("| File | Contents | Calls | Size | SHA-256 (first 16) |\n|---|---|---|---|---|")
for p, d, cs in FILES:
    if os.path.exists(p):
        w(f"| `{p}` | {d} | {cs} | {os.path.getsize(p):,} B | `{fsha(p)[:16]}` |")
w("\n**Code used for calculations** (committed to the repository under `research/CPNG/code/`):\n")
for p, d in CODE:
    w(f"- `{p}`: {d} (SHA-256 `{fsha(p)[:16]}`)")
w("")

w("## 7. Calculations\n")
w("### 7.1 Valuation multiples (report section 13)\n")
w("- **EV** = share price × S&P weighted-average diluted shares (latest quarter) + S&P net debt including leases, in each company's reporting currency.")
w("- **Coupang:** US$15.82 × 1,799m = US$28,460m market cap; less US$477m net cash including leases = **EV US$27,983m** [d]. LTM revenue US$35,462m gives **EV/Sales 0.79x**.")
w("- **EV/EBITDA, EV/EBIT, P/E, net debt/EBITDA**: LTM S&P EBITDA, operating income and net income; shown as n.m. when the denominator is negative.")
w("- **FCF yield** = (LTM CFO − LTM capex) / market cap, S&P line items (calls #378-379).")
w("- **FX:** Chinese ADRs translated at CNY 7.10/US$ and HKD 7.80/US$ [e] (no FX series in the connectors). US$ market caps for KRW, JPY, EUR and PLN reporters use the FX implied by ProntoNLP's US$ vs local market-cap fields [d]: KRW 1,356, JPY 157.6, EUR 0.878, PLN 3.84 per US$.")
med = pf["median"]
w(f"- **Peer medians** (15 listed peers, Coupang excluded): EV/Sales {med['ev_sales']:.2f}x, EV/EBITDA {med['ev_ebitda']:.1f}x, EV/EBIT {med['ev_ebit']:.1f}x, P/E {med['pe']:.1f}x, EBITDA margin {med['ebitda_m']:.1f}%, EBIT margin {med['ebit_m']:.1f}%, sales growth {med['growth']:.1f}%, FCF yield {med['fcf_yield']:.1f}%.\n")
w("### 7.2 Regression (report section 13.3)\n")
w(f"Ordinary least squares of LTM EV/Sales on LTM EBIT margin (%) across {reg['n']} listed peers, Coupang and Jumia excluded: "
  f"**EV/Sales = {reg['intercept']:.3f} + {reg['slope']:.4f} × EBIT margin**, R² = {reg['r2']:.3f}. "
  f"Implied values: {reg['intercept'] + reg['slope'] * -1.70:.2f}x at Coupang's LTM -1.7%, {reg['intercept'] + reg['slope'] * (498 / 34534 * 100):.2f}x at its FY2025 1.4%, and 0.92x at our FY2028E base-case margin.\n")
w("### 7.3 Own history (report section 13.2)\n")
w("Year-end EV/Sales = (year-end close × S&P diluted shares + S&P net debt) / S&P annual revenue, for Coupang and six core peers (Amazon, MercadoLibre, Sea, NAVER, E-MART, Lotte Shopping). Year-end closes are ProntoNLP quarterly bars ‡.\n")
w("### 7.4 EPS model, FY2026E-FY2028E (report section 11)\n")
w("Revenue is built by segment: Product Commerce (PC) and Developing Offerings (DO). Adjusted EBITDA = PC revenue × PC margin + DO adjusted EBITDA. GAAP EBIT = adjusted EBITDA − D&A − SBC + one-offs. Net income = EBIT + net interest and other − tax; EPS = net income / diluted shares.\n")
w(f"- **FY2026E** = H1'26 actuals plus a Q3/Q4 build. Q3E revenue US${model['q3']['rev']:,.0f}m: PC +6.5% cc less 5pts FX, DO +20%, margin 4.5% − 330bp (guide: −300 to −400bp). Q4E revenue US${model['q4']['rev']:,.0f}m at a 3.1% margin. "
  f"One-offs: US$410m PIPC fines and ~US$150m Incheon fire [e]. Output: revenue US${F26['rev']:,.0f}m, adjusted EBITDA US${F26['adj_ebitda']:,.0f}m, GAAP EBIT US${F26['ebit_gaap']:,.0f}m, net income US${F26['ni']:,.0f}m, EPS US${F26['eps']:.2f} (adjusted US${F26['adj_eps']:.2f}).\n")
w("| Assumption [e] | Bear FY27 / FY28 | Base FY27 / FY28 | Bull FY27 / FY28 |\n|---|---|---|---|")
w("| PC revenue growth (flat FX, so US$ = constant currency) | +5.5% / +5.5% | +11% / +10% | +14% / +13% |")
w("| DO revenue growth | +12% / +10% | +18% / +18% | +22% / +20% |")
w("| PC adj. EBITDA margin | 5.8% / 6.2% | 7.3% / 8.6% | 8.0% / 10.0% |")
w("| DO adj. EBITDA (US$m) | -900 / -850 | -800 / -600 | -750 / -450 |")
w("| D&A / SBC (US$m) | 680, 580 / 760, 620 | 680, 580 / 780, 620 | 680, 580 / 790, 630 |")
w("| One-offs (US$m) | -150 / -100 | +100 / 0 | +100 / 0 |")
w("| Effective tax rate | 80% / 70% (tax floor US$150m) | 55% / 40% | 50% / 33% |")
w("| Diluted shares (m) | 1,800 / 1,810 | 1,790 / 1,795 | 1,785 / 1,790 |")
r = lambda k, y, f: SC[k][y][f]
w(f"| **Revenue (US$m)** | {r('bear','F27','rev'):,.0f} / {r('bear','F28','rev'):,.0f} | {r('base','F27','rev'):,.0f} / {r('base','F28','rev'):,.0f} | {r('bull','F27','rev'):,.0f} / {r('bull','F28','rev'):,.0f} |")
w(f"| **Adj. EBITDA (US$m)** | {r('bear','F27','adj_ebitda'):,.0f} / {r('bear','F28','adj_ebitda'):,.0f} | {r('base','F27','adj_ebitda'):,.0f} / {r('base','F28','adj_ebitda'):,.0f} | {r('bull','F27','adj_ebitda'):,.0f} / {r('bull','F28','adj_ebitda'):,.0f} |")
w(f"| **GAAP EPS (US$)** | {r('bear','F27','eps'):.2f} / {r('bear','F28','eps'):.2f} | {r('base','F27','eps'):.2f} / {r('base','F28','eps'):.2f} | {r('bull','F27','eps'):.2f} / {r('bull','F28','eps'):.2f} |\n")
w("### 7.5 Scenario valuation (report section 22; `valuation.py`)\n")
w("Per share = (multiple × NTM sales − net debt incl. leases) / FY2028E diluted shares. NTM sales at Oct-2027 = 0.25 × FY2027E + 0.75 × FY2028E revenue.\n")
w("| | NTM sales (US$m) | Multiple | EV (US$m) | Net debt (US$m) | Shares (m) | Per share | vs US$15.82 | EV / FY28E adj. EBITDA | Weight |\n|---|---|---|---|---|---|---|---|---|---|")
for k in ("bear", "base", "bull"):
    v = val[k]
    w(f"| {k.title()} | {v['ntm_sales']:,.0f} | {v['multiple']:.2f}x | {v['ev']:,.0f} | {v['net_debt']:+,.0f} | {v['shares']:,.0f} | US${v['per_share']:.2f} | {v['upside']:+.1%} | {v['ev_fy28_ebitda']:.1f}x | {v['prob']:.0%} |")
pwv = val["prob_weighted"]
w(f"| **Probability-weighted** | | | | | | **US${pwv['per_share']:.2f}** | **{pwv['upside']:+.1%}** | | |\n")
w("Displayed values round to US$9.5 / US$21.0 / US$31.7 and US$20.8. The 12-month target of US$21 is the base case.\n")
w("### 7.6 Adjusted EBITDA bridge, FY2026E to FY2028E base case (`charts_d.py`)\n")
w("Start US$608m. PC margin recovery = (FY28E PC margin 8.6% − FY26E PC margin 5.2%) × FY26E PC revenue = **+US$1,058m**. PC volume growth = (FY28E − FY26E PC revenue) × 8.6% = **+US$584m**. DO loss reduction = −US$600m − (−US$975m) = **+US$375m**. End US$2,625m. FY26E PC margin = (FY26E adjusted EBITDA + US$975m DO loss, the guide mid-point) / FY26E PC revenue.\n")
w("### 7.7 Takeover value (report section 14.2)\n")
w("Control value = 1.0-1.3x LTM sales (US$35.5bn) plus US$0.48bn net cash, divided by 1,799m diluted shares = **US$20.0-25.9 a share** [d]. A 30-40% premium to US$15.82 gives US$20.6-22.1. Precedent multiples are target EV / LTM sales at announcement from S&P target financials (calls #362-368) and acquirer filings via ProntoNLP [d].\n")
w("### 7.8 Other derived figures\n")
w("- **LTM figures** = sum of the last four reported quarters (S&P), e.g. LTM adjusted EBITDA US$872m = 413 + 267 + 29 + 163.")
w("- **Net cash** = cash US$6,110m − funded debt US$2,603m (US$1,985m short-term + US$618m long-term) = US$3.5bn ex-leases; less US$3,030m operating leases = US$0.48bn, matching S&P net debt of −US$477m.")
w("- **Cash conversion cycle** = DSO + DIO − DPO on year-end S&P balances (receivables / revenue, inventory / COGS and payables / COGS, × 365): −42, −64, −54, −57 days for FY2022-FY2025. FY2025: 3.8 + 33.8 − 94.2 days.")
w("- **Cumulative Korean fines** = US$121m (KFTC, 2024) + US$410m (PIPC, 2026) = US$531m.")
w("- **Negative-event share** = negative / (positive + negative) ProntoNLP event counts per call.")
w("- **Moves of more than 10%** = week-on-week or day-on-day changes in the ProntoNLP price series ‡, attributed to dated company documents where one exists; otherwise marked [u].\n")

w("## 8. Known gaps and quality notes\n")
w("- **Source link unavailable (‡):** ProntoNLP price bars and consensus values carry no document link; S&P statement-level calls return statement links rather than line links for some periods.")
w("- **Not in the connectors:** the 2026 proxy (executive pay, top-10 holders, director biographies and committees), 13F/13D/13G and Form 4 filings, short interest and short-seller reports, FX rates, and some Korean deal values. These are flagged in the report rather than estimated.")
w("- **Unverified newsletter claims:** Korean e-commerce share (~28%), the KRW 7,890 WOW fee and the 10km coverage target could not be confirmed in S&P or ProntoNLP; see report section 27.")
w("- **Consensus:** EPS values returned scaled ×1e6, and the 3Q26/4Q26 entries are stale (Mar-2025); no FY2027-28 consensus was available. Forward estimates are ours alone.")
w("- **QA corrections made on 12-Oct-2026 before release:** LTM adjusted EBITDA set to US$872m and EV/adjusted EBITDA multiples recomputed; drawdown from the high corrected to 61%; the bull-case value standardised to the FY2028E share basis used for the other scenarios (US$31.7, +100%; probability-weighted US$20.8, +31%).\n")

w("## Appendix A. Full connector call log\n")
w("Times are UTC on 12-Oct-2026. Workstreams: Lead = lead analyst session; A-E = research agents (section 3). The SHA-256 is of the returned payload as logged.\n")
w("| # | Time | WS | Connector | Tool | Key arguments | Chars | SHA-256 | Status |\n|---|---|---|---|---|---|---|---|---|")
for u in calls:
    tm = (u["ts"] or "")[11:19]
    w(f"| {u['seq']} | {tm} | {WS[u['agent']][0]} | {'S&P' if 'S_P_' in u['tool'] else 'Pronto'} | `{tool(u['tool'])}` | {args_of(u)} | {u.get('result_chars', 0):,} | `{sha(u.get('result', ''))[:10]}` | {'error' if u.get('is_error') else 'ok'} |")
open("prov/Coupang_CPNG_Data_Provenance.md", "w").write("\n".join(L) + "\n")
print("written", len(L), "lines; calls", len(calls))
