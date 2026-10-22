"""Build dash/data.json for the Coupang dashboard from the report fragment and logged tool results."""
import gzip, json, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "raw")
from cpng_weekly import series  # noqa: E402

S = "https://gam.prontonlp.com/#/ref/$SENTID_"
D = "https://gam.prontonlp.com/#/ref/$DOCID_"
C = "https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid="

# ---------- logged S&P results (for per-point chart links) ----------
calls = {}
with gzip.open("prov/mcp_calls_full.jsonl.gz", "rt") as fh:
    for line in fh:
        u = json.loads(line)
        calls[u["seq"]] = u


def sp_periods(seq, ticker):
    """{period: (value, url)} for one identifier of a logged S&P line-item call."""
    res = json.loads(calls[seq]["result"])["results"][ticker]["data"]["periods"]
    out = {}
    for p, v in res.items():
        li = v["line_item"]
        src = li.get("sources") or []
        out[p] = (float(li["value"]) / 1e6, src[0]["url"] if src else None)
    return out


# ---------- report sections ----------
soup = BeautifulSoup(open("dash/report_fragment.html").read(), "lxml")
FIG = {"price.png": "price", "annual.png": "annual", "quarterly.png": "quarterly", "segments.png": "segments",
       "margins_q.png": "margins", "sentiment.png": "sentiment", "regression.png": "regression",
       "hist_evsales.png": "hist", "scenarios.png": "scenarios", "supplychain.png": "supplychain",
       "bridge.png": "bridge"}

sections = []
cur = {"id": "cover", "num": "", "title": "Cover and key data", "blocks": []}
sections.append(cur)
buf = []
cidx = 0


def flush():
    global buf, cidx
    if buf:
        cidx += 1
        cur["blocks"].append({"t": "c", "id": f"{cur['id']}--{cidx}", "html": "".join(buf)})
        buf = []


def inner(el):
    return "".join(str(c) for c in el.contents).strip()


def handle(el):
    global cur, cidx
    name = el.name
    if name == "h1":
        flush()
        title = el.get_text(" ", strip=True)
        m = re.match(r"^(\d+)\.\s*(.*)$", title)
        cur = {"id": el.get("id"), "num": m.group(1) if m else "", "title": m.group(2) if m else title, "blocks": []}
        sections.append(cur)
        cidx = 0
    elif name in ("h2", "h3", "h4"):
        flush()
        cur["blocks"].append({"t": "h", "level": int(name[1]), "id": el.get("id"), "text": el.get_text(" ", strip=True)})
    elif name in ("p", "ul", "ol", "blockquote"):
        img = el.find("img")
        if img is not None and not el.get_text(strip=True):
            flush()
            cur["blocks"].append({"t": "chart", "key": FIG.get(os.path.basename(img["src"])), "caption": img.get("alt", "")})
        else:
            buf.append(str(el))
    elif name == "table":
        flush()
        head = [inner(th) for th in el.select("thead tr th")]
        rows = [[inner(td) for td in tr.find_all(["td", "th"])] for tr in el.select("tbody tr")]
        cur["blocks"].append({"t": "table", "head": head, "rows": rows})
    elif name == "figure":
        flush()
        img = el.find("img")
        cap = el.find("figcaption")
        cur["blocks"].append({"t": "chart", "key": FIG.get(os.path.basename(img["src"])),
                              "caption": cap.get_text(" ", strip=True) if cap else ""})
    elif name == "div":
        if "pagebreak" in (el.get("class") or []):
            return
        for ch in el.children:
            if getattr(ch, "name", None):
                handle(ch)


for ch in soup.body.children:
    if getattr(ch, "name", None):
        handle(ch)
flush()
missing = [b for s in sections for b in s["blocks"] if b["t"] == "chart" and not b["key"]]
assert not missing, missing

# ---------- chart data ----------
charts = {}

# Price (ProntoNLP weekly closes; no source link returned) + catalysts with their citations
ev_links = {
    "2021-03-08": (S + "SEC000177952319-1284", "IPO priced at US$35; day-one close US$49.25 (+41%)", 1),
    "2021-08-09": (S + "T000002374084-174", "Q2'21 absorbed the Deokpyeong FC fire: US$158m inventory and US$138m asset write-offs (wk -12.7%)", -1),
    "2022-01-17": (None, "-38% in three weeks with no company document in the window; growth-stock de-rating [u]", -1),
    "2022-05-09": (S + "T000002563967-92", "Intraday low US$8.98 (11-May); Q1'22 loss narrowed and Product Commerce turned positive: +38% in two days", 1),
    "2022-08-08": (S + "T000002626640-46", "Q2'22: first positive consolidated adjusted EBITDA (Jul-Aug +67%)", 1),
    "2024-02-26": (S + "T000003041770-30", "Q4'23: record net income and FCF; Farfetch closed (wk +15.5%)", 1),
    "2024-08-05": (S + "T000003215027-36", "Q2'24: constant-currency revenue +30% (wk +11.4%)", 1),
    "2025-05-05": (S + "SEC000259645823-296", "Q1'25: +21% cc revenue and the first US$1bn buyback (+10.8% on the day)", 1),
    "2025-09-15": (None, "All-time post-IPO high of US$34.08 (intraday); no company document [u]", 1),
    "2025-12-15": (S + "SEC000253203320-2", "8-K on the data incident (up to 33m accounts); Korea CEO resigned; ~US$1.2bn vouchers (wk -9.5%)", -1),
    "2026-05-04": (S + "T000003711263-132", "Q1'26: operating loss of US$242m; adj. EBITDA margin 0.3% (-13.8% on the day)", -1),
    "2026-07-13": (S + "SEC000264559057-470", "Incheon FC fire: ~US$246m of assets and obligations at the site (wk -11.6%)", -1),
    "2026-09-28": (None, "52-week low of US$13.35, then +14.8% in the week of 5-Oct [u cause]", -1),
}
charts["price"] = {
    "series": [[d.isoformat(), c] for d, c in series],
    "events": [{"date": d, "url": u, "text": t, "dir": s} for d, (u, t, s) in ev_links.items()],
    "source": "ProntoNLP weekly closes (source link unavailable ‡)",
}

# Annual P&L (S&P Capital IQ; per-value links returned by the tools)
ann = {k: sp_periods(seq, "CPNG") for k, seq in
       {"rev": 369, "gp": 370, "ebit": 371, "ni": 372}.items()}
ebitda = sp_periods(10, "CPNG")
years = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
charts["annual"] = {
    "years": ["FY21", "FY22", "FY23", "FY24", "FY25"],
    "rev": [ann["rev"][y] for y in years],
    "gp": [ann["gp"][y] for y in years],
    "ebitda": [ebitda[y] for y in years],
    "ebit": [ann["ebit"][y] for y in years],
    "ni": [ann["ni"][y] for y in years],
}

# Quarterly revenue and GAAP operating income (S&P Capital IQ)
qrev = sp_periods(373, "CPNG")
qop = sp_periods(374, "CPNG")
qkeys = sorted(qrev.keys())
lab = lambda p: f"{p[-1]}Q{p[4:6]}".replace("Q20", "Q")  # FY2025Q3 -> 3Q25
charts["quarterly"] = {"q": [f"{p[-1]}Q{p[4:6]}" for p in qkeys],
                       "rev": [qrev[p] for p in qkeys], "op": [qop[p] for p in qkeys]}

# Segments (company disclosures via ProntoNLP; links as cited in the report)
charts["segments"] = {
    "years": ["FY22", "FY23", "FY24", "FY25"],
    "pc_rev": [[20.0, S + "SEC000200362169-28"], [23.6, S + "SEC000218768452-34"], [26.7, S + "SEC000237406755-49"], [29.6, S + "SEC000255972090-50"]],
    "do_rev": [[0.58, None], [0.789, S + "SEC000218768452-37"], [3.6, S + "SEC000237406755-51"], [4.9, S + "SEC000255972090-55"]],
    "pc_ebitda": [[0.60, S + "SEC000200362169-29"], [1.5, S + "SEC000218768452-35"], [2.0, S + "SEC000237406755-50"], [2.5, S + "SEC000255972090-54"]],
    "do_ebitda": [[-0.225, S + "SEC000218768452-38"], [-0.466, S + "SEC000218768452-38"], [-0.631, S + "SEC000237406755-53"], [-0.995, S + "SEC000255972090-56"]],
    "notes": "FY22 DO revenue is derived (total less PC) [d]; FY22 PC adj. EBITDA derived from the 3.0% margin [d].",
}

# Quarterly segment margins (ProntoNLP transcripts)
charts["margins"] = {
    "q": ["3Q25", "4Q25", "1Q26", "2Q26"],
    "pc": [[8.8, S + "T000003578475-86"], [7.7, S + "T000003665452-151"], [5.0, S + "T000003711263-106"], [5.1, S + "T000003779883-169"]],
    "cons": [[4.5, S + "T000003578475-122"], [3.0, S + "T000003665452-183"], [0.3, S + "T000003711263-134"], [1.8, S + "T000003779883-201"]],
}

# Call sentiment (ProntoNLP document scores)
pm = json.load(open("raw/pronto_market.json"))
order = ["Q4_2023", "Q1_2024", "Q2_2024", "Q3_2024", "Q4_2024", "Q1_2025", "Q2_2025", "Q3_2025", "Q4_2025", "Q1_2026", "Q2_2026"]
tr = pm["transcripts"]
sent_rows = []
for k in order:
    if k in tr:
        t = tr[k]
        sent_rows.append({"call": k[1] + "Q" + k[-2:], "id": t["id"], "date": t.get("date"), "sent": t["sent"],
                          "pos": t.get("pos"), "neg": t.get("neg"), "url": D + t["id"]})
charts["sentiment"] = {"rows": sent_rows}

# Regression (S&P LTM; EBIT links from the logged LTM operating-income call)
peers = json.load(open("raw/peers_final.json"))["rows"]
op_ltm = json.loads(calls[66]["result"])["results"]
tick_map = {"CPNG": "CPNG", "AMZN": "AMZN", "MELI": "MELI", "SE": "SE", "PDD": "PDD", "BABA": "BABA", "JD": "JD", "VIPS": "VIPS",
            "035420": "KOSE:A035420", "139480": "KOSE:A139480", "023530": "KOSE:A023530", "4755": "TSE:4755",
            "ZAL": "XTRA:ZAL", "ALE": "WSE:ALE", "JMIA": "JMIA", "WMT": "WMT"}
pts = []
for r in peers:
    key = tick_map.get(r["ticker"]) or tick_map.get(str(r["ticker"]).split()[0])
    url = None
    if key and key in op_ltm:
        per = op_ltm[key]["data"]["periods"]
        p = list(per.values())[0]["line_item"]
        url = (p.get("sources") or [{}])[0].get("url")
    pts.append({"name": r["name"], "ticker": r["ticker"], "x": round(r["ebit_m"], 2), "y": round(r["ev_sales"], 3), "url": url})
reg = json.load(open("raw/regression.json"))
cp = [p for p in pts if p["name"] == "Coupang"][0]
fy25 = {"name": "Coupang FY25 (pre-incident)", "x": round(498 / 34534 * 100, 2), "y": round(27983 / 34534, 3),
        "url": C + "255973354&uctSearch=498.000000"}
charts["regression"] = {"points": [p for p in pts if p["name"] not in ("Coupang",)], "cpng": cp, "fy25": fy25,
                        "a": reg["intercept"], "b": reg["slope"], "r2": reg["r2"], "n": reg["n"], "excluded": ["Jumia"]}

# Own history (derived)
hm = json.load(open("raw/hist_mult.json"))
charts["hist"] = {"lab": hm["lab"], "cpng": [round(v, 2) for v in hm["evs"]], "peer": [6.00, 2.00, 2.34, 3.03, 2.95, 1.97]}

# Scenarios and bridge (our model)
model = json.load(open("raw/model.json"))
charts["scenarios"] = {"price": 15.82, "rows": [
    {"k": "bear", "label": "Bear", "v": 9.5, "p": 25, "why": "KFTC unbundling; night-delivery ban; settlement drain; permanent share loss"},
    {"k": "base", "label": "Base", "v": 21.0, "p": 50, "why": "PC margin back to 8.6% by FY28; DO losses fall to US$0.6bn"},
    {"k": "bull", "label": "Bull", "v": 31.7, "p": 25, "why": "KRW recovery; 10% PC margin; Taiwan inflects; PIPC appeal win"}]}
charts["bridge"] = {"steps": [["FY26E adj. EBITDA", 608, "total"], ["PC margin recovery", 1058, "up"], ["PC volume growth", 584, "up"],
                               ["DO loss reduction", 375, "up"], ["FY28E adj. EBITDA", 2625, "total"]]}

# Supply chain (from the authored map)
sc = BeautifulSoup(open("supplychain.html").read(), "lxml")
stages = []
for col in sc.select(".flow .col"):
    stages.append({"title": col.find("h2").get_text(" ", strip=True), "core": "core" in col.get("class", []),
                   "items": [inner(i) for i in col.select(".item")]})
boxes = [{"title": b.find("h3").get_text(" ", strip=True), "html": inner(b).split("</h3>", 1)[1]} for b in sc.select(".row2 .box")]
charts["supplychain"] = {"stages": stages, "boxes": boxes,
                         "legend": sc.select_one(".legend").get_text(" ", strip=True)}

meta = {
    "company": "Coupang, Inc.", "ticker": "NYSE: CPNG", "asOf": "12 October 2026", "price": 15.82, "priceDate": "9-Oct-2026",
    "rating": "BUY", "conviction": "event-driven, medium conviction", "target": 21.0, "pw": 20.8,
    "tiles": [
        {"k": "Price (9-Oct-26)", "v": "US$15.82", "s": "52-wk US$13.35-32.35 ‡", "url": None},
        {"k": "12-mo target", "v": "US$21", "s": "+33%; prob.-weighted US$20.8 [e]", "url": None},
        {"k": "LTM EV/Sales", "v": "0.79x", "s": "Peer median 1.29x; 5-yr low [d]", "url": None},
        {"k": "Active customers", "v": "24.7m", "s": "Q2'26, back above pre-incident", "url": S + "SEC000264557825-29"},
        {"k": "PC adj. EBITDA margin", "v": "5.1%", "s": "Q2'26 vs 8.8% in Q3'25", "url": S + "T000003779883-169"},
        {"k": "Net cash incl. leases", "v": "US$0.48bn", "s": "Ex-leases US$3.5bn [d]", "url": C + "264559057"},
        {"k": "Founder votes", "v": "74.1%", "s": "Bom Kim, all Class B", "url": S + "SEC000255973354-1187"},
        {"k": "Next catalyst", "v": "3-Nov-26", "s": "Q3'26 results", "url": D + "upcoming-doc-704377650"},
    ],
}

# insert the EBITDA bridge after the first table of section 11 (EPS estimates)
for sec in sections:
    if sec["num"] == "11":
        for i, b in enumerate(sec["blocks"]):
            if b["t"] == "table":
                sec["blocks"].insert(i + 1, {"t": "chart", "key": "bridge", "caption": ""})
                break
# supply-chain marker classes -> page classes
for st in charts["supplychain"]["stages"]:
    st["items"] = [it.replace('class="v"', 'class="ok"').replace('class="u"', 'class="unv"') for it in st["items"]]
for bx in charts["supplychain"]["boxes"]:
    bx["html"] = bx["html"].replace('class="v"', 'class="ok"').replace('class="u"', 'class="unv"')
# call counts for the provenance panel
allc = list(calls.values())
meta["calls"] = {"total": len(allc), "sp": sum(1 for u in allc if "S_P_" in u["tool"]),
                 "pronto": sum(1 for u in allc if "__Pronto__" in u["tool"]), "errors": sum(1 for u in allc if u.get("is_error"))}

data = {"meta": meta, "sections": sections, "charts": charts}
json.dump(data, open("dash/data.json", "w"), separators=(",", ":"))
nblocks = sum(1 for s in sections for b in s["blocks"] if b["t"] == "c")
print("sections", len(sections), "commentary blocks", nblocks, "tables", sum(1 for s in sections for b in s["blocks"] if b["t"] == "table"),
      "charts", [b["key"] for s in sections for b in s["blocks"] if b["t"] == "chart"], "bytes", os.path.getsize("dash/data.json"))
print("quarters", charts["quarterly"]["q"])
print("regression pts", [(p["name"], p["x"], p["y"], bool(p["url"])) for p in charts["regression"]["points"]])
