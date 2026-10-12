#!/usr/bin/env python3
"""D_compute.py - Elis SA (ELIS FP) share-price analytics for agent D_price_catalysts.

All inputs are raw ProntoNLP getStockPrices responses saved verbatim in
  /home/user/RF-Stuff/ELIS_FP/provenance/raw/D_price_catalysts/
    001_getStockPrices.json  Elis (27989) daily, request 2021-09-01 -> now
    002_getStockPrices.json  Elis (27989) weekly, request 2015-01-01 -> now (data starts 2018-12-31)
    011..015                 peers daily (Cintas 260725, UniFirst 309966, Vestis 694763,
                             Rentokil Initial 411004 [NYSE ADR, USD], Sodexo 808038 [USD line])

Outputs (all numbers here are [calc] from ProntoNLP prices):
  model/D_elis_prices_daily.csv, model/D_elis_prices_weekly.csv, model/D_peer_prices_daily.csv
  model/D_price_stats.json      headline statistics
  model/D_big_moves.csv         single-day >=5% moves, 1-20 trading-day episodes >=10%,
                                calendar months >=10%; with peer returns over the same dates and
                                the cause classification (CAUSES dict below, filled from
                                ProntoNLP research - see provenance/D_price_catalysts_findings.md)

Conventions
  * Returns are close-to-close, simple returns, unadjusted for dividends (see findings for the
    dividend-adjustment test).
  * "Last 5 years" = trading days after 2021-10-08 (5y before the latest close 2026-10-09).
  * Episodes: every (start,end) pair with 1<=end-start<=20 trading days and |return|>=10% is a
    candidate; candidates are ranked by |return| and selected greedily so that selected
    intervals do not overlap (they may share an end-point).  Deterministic, documented.
  * Peer returns are taken over the same calendar dates using the last available close on or
    before each date (US calendar).  US peers close after Paris, so a peer "same-day" move can
    post-date the Elis move; we therefore also show the peer move for the window extended by one
    US session (t+1) for single-day moves.
"""
import json
import os
from datetime import date, timedelta

import numpy as np
import pandas as pd

BASE = "/home/user/RF-Stuff/ELIS_FP"
RAW = f"{BASE}/provenance/raw/D_price_catalysts"
OUT = f"{BASE}/model"
SRC_ELIS_D = "ProntoNLP getStockPrices companyId 27989 interval=day (log D_price_catalysts-001; raw/D_price_catalysts/001_getStockPrices.json)"
SRC_ELIS_W = "ProntoNLP getStockPrices companyId 27989 interval=week (log D_price_catalysts-002; raw/D_price_catalysts/002_getStockPrices.json)"

PEERS = {  # companyId: (ticker, name, raw file, log id)
    "260725": ("CTAS", "Cintas Corporation", "011_getStockPrices.json", "D_price_catalysts-011"),
    "309966": ("UNF", "UniFirst Corporation", "012_getStockPrices.json", "D_price_catalysts-012"),
    "694763": ("VSTS", "Vestis Corporation", "013_getStockPrices.json", "D_price_catalysts-013"),
    "411004": ("RTO", "Rentokil Initial plc (NYSE ADR)", "014_getStockPrices.json", "D_price_catalysts-014"),
    "808038": ("SW", "Sodexo S.A. (USD line)", "015_getStockPrices.json", "D_price_catalysts-015"),
}


def load(fname, cid):
    with open(f"{RAW}/{fname}") as fh:
        d = json.load(fh)
    df = pd.DataFrame(d[cid])
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").drop_duplicates("date").reset_index(drop=True)
    return df


# ---------------------------------------------------------------- 1. clean price files
daily = load("001_getStockPrices.json", "27989")
weekly = load("002_getStockPrices.json", "27989")
assert set(daily.stockCurrency) == {"EUR"} and set(weekly.stockCurrency) == {"EUR"}

for df, path, src in [(daily, "D_elis_prices_daily.csv", SRC_ELIS_D), (weekly, "D_elis_prices_weekly.csv", SRC_ELIS_W)]:
    out = df[["date", "open", "high", "low", "close"]].copy()
    out["date"] = out["date"].dt.strftime("%Y-%m-%d")
    out["currency"] = "EUR"
    out["source"] = src
    out.to_csv(f"{OUT}/{path}", index=False)

peer_frames = []
peers = {}
for cid, (tic, name, fn, logid) in PEERS.items():
    p = load(fn, cid)
    peers[tic] = p.set_index("date")["close"]
    q = p[["date", "open", "high", "low", "close", "stockCurrency"]].copy()
    q.insert(1, "ticker", tic)
    q.insert(2, "company", name)
    q.insert(3, "prontoCompanyId", cid)
    q = q.rename(columns={"stockCurrency": "currency"})
    q["date"] = q["date"].dt.strftime("%Y-%m-%d")
    q["source"] = f"ProntoNLP getStockPrices companyId {cid} interval=day (log {logid}; raw/D_price_catalysts/{fn})"
    peer_frames.append(q)
pd.concat(peer_frames).to_csv(f"{OUT}/D_peer_prices_daily.csv", index=False)

# ---------------------------------------------------------------- 2. headline statistics
c = daily.set_index("date")["close"]
last_dt, last_px = c.index[-1], float(c.iloc[-1])


def close_on_or_before(series, dt):
    s = series[series.index <= dt]
    return s.index[-1], float(s.iloc[-1])


def yrs_back(dt, n):
    try:
        return dt.replace(year=dt.year - n)
    except ValueError:  # 29-Feb
        return dt.replace(year=dt.year - n, day=28)


stats = {"latest_close": {"date": last_dt.strftime("%Y-%m-%d"), "close_eur": last_px}}
for n in (1, 3, 5):
    d0, p0 = close_on_or_before(c, yrs_back(last_dt, n))
    stats[f"change_{n}y"] = {"from_date": d0.strftime("%Y-%m-%d"), "from_close": p0, "to_date": last_dt.strftime("%Y-%m-%d"),
                             "to_close": last_px, "pct": round((last_px / p0 - 1) * 100, 2),
                             "cagr_pct": round(((last_px / p0) ** (1 / n) - 1) * 100, 2)}

w52 = daily[daily.date > yrs_back(last_dt, 1)]
stats["52w_close_basis"] = {
    "window": f"{w52.date.iloc[0]:%Y-%m-%d} to {w52.date.iloc[-1]:%Y-%m-%d}",
    "high": float(w52.close.max()), "high_date": w52.loc[w52.close.idxmax(), "date"].strftime("%Y-%m-%d"),
    "low": float(w52.close.min()), "low_date": w52.loc[w52.close.idxmin(), "date"].strftime("%Y-%m-%d")}
stats["52w_intraday_basis"] = {
    "high": float(w52.high.max()), "high_date": w52.loc[w52.high.idxmax(), "date"].strftime("%Y-%m-%d"),
    "low": float(w52.low.min()), "low_date": w52.loc[w52.low.idxmin(), "date"].strftime("%Y-%m-%d")}
stats["latest_vs_52w"] = {"pct_below_52w_close_high": round((last_px / stats['52w_close_basis']['high'] - 1) * 100, 2),
                          "pct_above_52w_close_low": round((last_px / stats['52w_close_basis']['low'] - 1) * 100, 2)}


def max_drawdown(series):
    runmax = series.cummax()
    dd = series / runmax - 1
    trough = dd.idxmin()
    peak = series[:trough].idxmax()
    rec = series[(series.index > trough) & (series >= series[peak])]
    return {"max_drawdown_pct": round(float(dd.min()) * 100, 2), "peak_date": peak.strftime("%Y-%m-%d"),
            "peak_close": float(series[peak]), "trough_date": trough.strftime("%Y-%m-%d"),
            "trough_close": float(series[trough]),
            "recovered_to_peak_on": rec.index[0].strftime("%Y-%m-%d") if len(rec) else "not recovered by latest close",
            "current_drawdown_from_window_high_pct": round(float(dd.iloc[-1]) * 100, 2)}


d5, _ = close_on_or_before(c, yrs_back(last_dt, 5))
c5 = c[c.index >= d5]
stats["max_drawdown_5y_close_basis"] = max_drawdown(c5)
stats["5y_high_low_close_basis"] = {"high": float(c5.max()), "high_date": c5.idxmax().strftime("%Y-%m-%d"),
                                    "low": float(c5.min()), "low_date": c5.idxmin().strftime("%Y-%m-%d")}
lr = np.log(c).diff().dropna()
stats["realised_vol_annualised_pct"] = {
    "1y": round(float(lr[lr.index > yrs_back(last_dt, 1)].std() * np.sqrt(252) * 100), 1),
    "5y": round(float(lr[lr.index > d5].std() * np.sqrt(252) * 100), 1)}

wc = weekly.set_index("date")["close"]
stats["weekly_series_since_2019"] = {
    "first_bar": wc.index[0].strftime("%Y-%m-%d"), "first_close": float(wc.iloc[0]),
    "max_weekly_close": float(wc.max()), "max_week": wc.idxmax().strftime("%Y-%m-%d"),
    "min_weekly_close": float(wc.min()), "min_week": wc.idxmin().strftime("%Y-%m-%d"),
    "max_drawdown_weekly_close_basis": max_drawdown(wc),
    "note": "ProntoNLP weekly data starts 2018-12-31; 2015 IPO to 2018 not available in ProntoNLP"}
# calendar-year returns (weekly closes for 2019-2021, daily closes from 2022)
yr = {}
ye_w = wc.groupby(wc.index.year).last()
ye_d = c.groupby(c.index.year).last()
for y in range(2019, last_dt.year + 1):
    if y - 1 in ye_d.index and y in ye_d.index and y >= 2022:
        yr[str(y)] = {"basis": "daily year-end closes", "pct": round((ye_d[y] / ye_d[y - 1] - 1) * 100, 2)}
    elif y - 1 in ye_w.index and y in ye_w.index:
        yr[str(y)] = {"basis": "last weekly bar of each year", "pct": round((ye_w[y] / ye_w[y - 1] - 1) * 100, 2)}
yr[str(last_dt.year)]["note"] = f"YTD to {last_dt:%Y-%m-%d}"
stats["calendar_year_returns"] = yr
# consistency check weekly vs daily (weekly close should equal the last daily close of that week)
chk = []
for wdt, wcl in wc[wc.index >= daily.date.iloc[0] + timedelta(days=7)].items():
    wk = c[(c.index >= wdt) & (c.index < wdt + timedelta(days=7))]
    if len(wk):
        chk.append(abs(float(wk.iloc[-1]) - wcl) < 0.005)
stats["weekly_vs_daily_consistency"] = {"weeks_checked": len(chk), "weeks_matching_last_daily_close": int(sum(chk))}

# ---------------------------------------------------------------- 3. big moves
ret = c.pct_change()
in5 = c.index > d5


def peer_ret(tic, d_from, d_to):
    s = peers[tic]
    s0 = s[s.index <= d_from]
    s1 = s[s.index <= d_to]
    if len(s0) == 0 or len(s1) == 0 or s0.index[-1] < pd.Timestamp(d_from) - timedelta(days=6):
        return np.nan
    return float(s1.iloc[-1] / s0.iloc[-1] - 1)


def next_bday(dt):
    n = dt + timedelta(days=1)
    while n.weekday() >= 5:
        n += timedelta(days=1)
    return n


rows = []
# (a) single-day moves >= 5%
idx = list(c.index)
for i in range(1, len(idx)):
    if not in5[i]:
        continue
    r = ret.iloc[i]
    if abs(r) >= 0.05:
        d_prev, d_t = idx[i - 1], idx[i]
        row = {"type": "single_day", "start_date": d_prev.strftime("%Y-%m-%d"), "end_date": d_t.strftime("%Y-%m-%d"),
               "trading_days": 1, "start_close": float(c.iloc[i - 1]), "end_close": float(c.iloc[i]),
               "pct_move": round(r * 100, 2)}
        for tic in [v[0] for v in PEERS.values()]:
            pr0 = peer_ret(tic, d_prev, d_t)
            row[f"{tic}_pct_same_dates"] = round(pr0 * 100, 2) if not np.isnan(pr0) else ""
            pr1 = peer_ret(tic, d_prev, next_bday(d_t))
            row[f"{tic}_pct_to_t+1"] = round(pr1 * 100, 2) if not np.isnan(pr1) else ""
        rows.append(row)

# (b) 1-20 trading-day episodes >= 10%, non-overlapping
cv = c.values
n = len(cv)
first5 = int(np.argmax(in5)) - 1  # start index may be the 5y anchor day itself
cands = []
for i in range(max(first5, 0), n - 1):
    for j in range(i + 1, min(i + 20, n - 1) + 1):
        r = cv[j] / cv[i] - 1
        if abs(r) >= 0.10:
            cands.append((abs(r), i, j, r))
cands.sort(key=lambda x: (-x[0], x[1], x[2]))
chosen = []
for a, i, j, r in cands:
    if all(j <= ci or i >= cj for _, ci, cj, _ in chosen):
        chosen.append((a, i, j, r))
chosen.sort(key=lambda x: x[1])
for a, i, j, r in chosen:
    d0, d1 = idx[i], idx[j]
    row = {"type": "episode_1to20d", "start_date": d0.strftime("%Y-%m-%d"), "end_date": d1.strftime("%Y-%m-%d"),
           "trading_days": j - i, "start_close": float(cv[i]), "end_close": float(cv[j]), "pct_move": round(r * 100, 2)}
    for tic in [v[0] for v in PEERS.values()]:
        pr = peer_ret(tic, d0, d1)
        row[f"{tic}_pct_same_dates"] = round(pr * 100, 2) if not np.isnan(pr) else ""
    rows.append(row)

# (c) calendar months >= 10%
me = c.groupby([c.index.year, c.index.month]).last()
me_dates = c.groupby([c.index.year, c.index.month]).apply(lambda s: s.index[-1])
keys = list(me.index)
for k in range(1, len(keys)):
    if me_dates.iloc[k] <= d5:
        continue
    r = me.iloc[k] / me.iloc[k - 1] - 1
    if abs(r) >= 0.10:
        d0, d1 = me_dates.iloc[k - 1], me_dates.iloc[k]
        row = {"type": "calendar_month", "start_date": d0.strftime("%Y-%m-%d"), "end_date": d1.strftime("%Y-%m-%d"),
               "trading_days": int(((c.index > d0) & (c.index <= d1)).sum()), "start_close": float(me.iloc[k - 1]),
               "end_close": float(me.iloc[k]), "pct_move": round(r * 100, 2),
               "month": f"{keys[k][0]}-{keys[k][1]:02d}"}
        for tic in [v[0] for v in PEERS.values()]:
            pr = peer_ret(tic, d0, d1)
            row[f"{tic}_pct_same_dates"] = round(pr * 100, 2) if not np.isnan(pr) else ""
        rows.append(row)

moves = pd.DataFrame(rows)
tics = [v[0] for v in PEERS.values()]
sd = [f"{t}_pct_same_dates" for t in tics]
moves["peer_median_pct_same_dates"] = moves[sd].apply(pd.to_numeric, errors="coerce").median(axis=1).round(2)
moves["elis_minus_peer_median_pp"] = (moves["pct_move"] - moves["peer_median_pct_same_dates"]).round(2)

# ---------------------------------------------------------------- 4. causes (from ProntoNLP research)
CAUSES = {}  # filled below after research: key = (type, start_date, end_date)
for col in ("category", "cause", "source"):
    moves[col] = ""
for k, v in CAUSES.items():
    t, s, e = k
    m = (moves.type == t) & (moves.start_date == s) & (moves.end_date == e)
    for col in ("category", "cause", "source"):
        moves.loc[m, col] = v.get(col, "")
moves.loc[moves.category == "", "category"] = "not yet classified"
moves["price_source"] = "ProntoNLP getStockPrices (27989 + peers), [calc] in model/D_compute.py"
moves.to_csv(f"{OUT}/D_big_moves.csv", index=False)

stats["counts"] = {"single_day_ge5pct": int((moves.type == "single_day").sum()),
                   "episodes_ge10pct_1to20d": int((moves.type == "episode_1to20d").sum()),
                   "months_ge10pct": int((moves.type == "calendar_month").sum())}
stats["peer_split_check"] = {t: round(float(peers[t].pct_change().abs().max()) * 100, 1) for t in tics}
stats["source"] = SRC_ELIS_D + "; " + SRC_ELIS_W + "; all figures [calc]"
with open(f"{OUT}/D_price_stats.json", "w") as fh:
    json.dump(stats, fh, indent=2)

if __name__ == "__main__":
    pd.set_option("display.width", 250, "display.max_columns", 40, "display.max_rows", 300)
    print(json.dumps(stats, indent=1))
    print(moves.drop(columns=["price_source", "source", "cause"]).to_string())
