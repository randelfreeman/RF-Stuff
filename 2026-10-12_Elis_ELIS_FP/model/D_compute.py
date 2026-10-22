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
# Citation links are copied verbatim from ProntoNLP responses saved in provenance/raw/D_price_catalysts/.
L_US = ("[#1](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000232051849-1) (Q3 2024 release: exploratory talks with two US players in Q3, terminated early Oct); "
        "[#3277](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-3277) (CMD: 'ready to evaluate ... major targets like Vestis'); "
        "[#458](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-458) (FY2024 call: 'U.S. negotiation'); "
        "[#127](https://gam.prontonlp.com/#/ref/$SENTID_T000003316682-127) (Vestis: 'preliminary proposals received')")
L_US_END = "[#1](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000232051849-1) (both discussions terminated at the beginning of October 2024)"
L_FY24 = ("[#4](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000257201966-4) (EUR150m buyback from 6-Mar-2025 + EUR0.45 dividend); "
          "[#377](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-377) (valuation 'does not fully reflect' strengths); "
          "[#2](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000257201966-2) (new cash allocation policy, 2025 outlook)")
L_H126 = ("[#330](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-330) (Mexico volume losses brought organic growth back in line with March indication); "
          "[#342](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-342) (2026 objectives confirmed, not raised); "
          "[#27](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-27) (negative H1 FCF called working-capital timing); "
          "[#36](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-36) (EUR500m buyback completed mid-July; OCEANE soft call planned)")
L_FR24 = ("[#81](https://gam.prontonlp.com/#/ref/$SENTID_T000003194583-81) (H1 2024 call: 'stock price lost around 15% since the dissolution of the French National Assembly'); "
          "[#155](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000227525215-155) (30% of revenue in France)")
L_ME = ("[#424](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-424); [#453](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-453) (FY2025 call 11-Mar-2026 on Middle East situation/energy); "
        "[#10](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259598338-10) (Q1 2026: temporary March hospitality effect); "
        "[#73](https://gam.prontonlp.com/#/ref/$SENTID_T000003774119-73) (gas/electricity spot +50% since start of conflict); "
        "[#77](https://gam.prontonlp.com/#/ref/$SENTID_SEC000259980508-77) (Vestis 8-K: 'military conflict among the United States, Israel and Iran')")
L_UKR = ("[#3392](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000180181407-3392) (2022 EBITDA margin ~33.5% at EUR100/MWh gas vs <=EUR30/MWh 2010-Jul-2021); "
         "[#2927](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000180181407-2927) (conflicts: Ukraine and impact on energy prices); "
         "[#293](https://gam.prontonlp.com/#/ref/$SENTID_T000002520475-293) (FY2021 call: +1% price per EUR30/MWh above EUR100)")
L_OMI = "[#29](https://gam.prontonlp.com/#/ref/$SENTID_T000002606072-29) (H1 2022 call: slight impact from Omicron in first weeks of 2022)"
L_H122 = ("[#20](https://gam.prontonlp.com/#/ref/$SENTID_T000002606072-20) (guidance raised); "
          "[#302](https://gam.prontonlp.com/#/ref/$SENTID_T000002606072-302) (EBIT guidance to >EUR530m); "
          "[#18](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000187028716-18) (gas purchases secured for H2)")
L_EN22 = ("[#455](https://gam.prontonlp.com/#/ref/$SENTID_T000002606072-455) (H1 2022 call: 'crazy' power prices, French nuclear outages); "
          "[#19](https://gam.prontonlp.com/#/ref/$SENTID_T000002666115-19) (Q3 2022 call: bulk of inflation from energy)")
L_Q322 = ("[#25](https://gam.prontonlp.com/#/ref/$SENTID_T000002666115-25) (guidance update: FY organic growth >+20%); "
          "[#211](https://gam.prontonlp.com/#/ref/$SENTID_T000002666115-211) (sharp energy cost decrease in Oct-2022)")
L_JAN23 = "[#23](https://gam.prontonlp.com/#/ref/$SENTID_T000002725290-23) (30-Jan-2023: 2023 organic growth of at least +10%, no slowdown)"
L_H123 = "[#366](https://gam.prontonlp.com/#/ref/$SENTID_T000002859132-366) (26-Jul-2023: organic guidance specified at c.12%; HNI target raised)"
L_SP23 = ("[#244](https://gam.prontonlp.com/#/ref/$SENTID_T000002901783-244) (EBITDA margin improvement guidance ~+70bps vs +50bps); "
          "[#428](https://gam.prontonlp.com/#/ref/$SENTID_T000002901783-428) (SBTi/climate roadmap context: the 4-Sep-2023 special call was a CSR call, not M&A)")
L_Q323 = ("[#293](https://gam.prontonlp.com/#/ref/$SENTID_T000002988271-293) (2023 outlook confirmed, organic c.12%); "
          "[#324](https://gam.prontonlp.com/#/ref/$SENTID_T000002988271-324) (no precise 2024 target)")
L_JAN24 = "[#18](https://gam.prontonlp.com/#/ref/$SENTID_T000003007279-18) (FY2023 organic +11.8%, Q4 +8.1%)"
L_FY23 = "[#307](https://gam.prontonlp.com/#/ref/$SENTID_T000003054377-307) (2024 outlook: organic c.+5%)"
L_VS24 = "[#191](https://gam.prontonlp.com/#/ref/$SENTID_T000003106889-191) (Vestis margin guidance cut, 2-May-2024)"
L_FRBUD = "[#407](https://gam.prontonlp.com/#/ref/$SENTID_T000003394029-407) (analyst question on impact of new French budget)"
L_TAR = ("[#6](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000247046060-6) (Q1 2025: no direct US-tariff impact, objectives confirmed); "
         "[#2993](https://gam.prontonlp.com/#/ref/$SENTID_T000003468571-2993) (CMD: tariff uncertainty shook the market)")
L_BB26 = ("[#693](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-693) (2026 buyback up to EUR500.0m); "
          "[#695](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000256665099-695) (buyback period began 6-Jan-2026)")
L_FY25 = ("[#507](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-507) (dividend EUR0.48 proposed); "
          "[#519](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-519) (buyback up to EUR500m in 2026)")
L_CTUNF = "[#32](https://gam.prontonlp.com/#/ref/$SENTID_T000003676456-32) (Cintas to acquire UniFirst, $5.5bn, 11-Mar-2026)"
NI = "cause not identified in permitted sources"

CAUSES = {  # key = (type, start_date, end_date)
    ("single_day", "2021-11-25", "2021-11-26"): dict(category="macro", cause="Broad sell-off: peer median -3.5%, Sodexo USD line -5.8% [calc]. ProntoNLP only confirms Omicron hit hospitality in early 2022; linking this day to the Omicron variant news is [u].", source=L_OMI),
    ("single_day", "2022-02-25", "2022-02-28"): dict(category="macro", cause="Russia-Ukraine war onset -> European gas/energy price shock for an energy-intensive laundry operator (US peers flat, Sodexo -3.1%) [calc]; war-start date [u].", source=L_UKR),
    ("single_day", "2022-02-28", "2022-03-01"): dict(category="macro", cause="Continuation of Ukraine-war energy shock (Sodexo -5.5%, US peers ~flat) [calc].", source=L_UKR),
    ("single_day", "2022-03-08", "2022-03-09"): dict(category="earnings/guidance; macro", cause="FY2021 results (call 9-Mar-2022): 2022 EBITDA margin ~33.5% at EUR100/MWh gas plus explicit price pass-through mechanism; same-day broad rebound (peer median +4.05%) [calc].", source=L_UKR),
    ("single_day", "2022-03-15", "2022-03-16"): dict(category="macro", cause=NI + "; broad rally (peer median +2.5%) [calc].", source=""),
    ("single_day", "2022-04-04", "2022-04-05"): dict(category="not identified", cause=NI + "; stock-specific vs US peers (~0%), Sodexo -2.2% [calc].", source=""),
    ("single_day", "2022-06-10", "2022-06-13"): dict(category="macro", cause=NI + "; broad sell-off (peer median -4.0%) [calc].", source=""),
    ("single_day", "2022-06-28", "2022-06-29"): dict(category="not identified", cause=NI + "; stock-specific (US peers ~flat, Sodexo -2.0%) [calc].", source=""),
    ("single_day", "2022-09-14", "2022-09-15"): dict(category="macro", cause="Energy-crisis backdrop (power/gas prices) per management commentary; specific trigger for the day not identified; peer median -1.5% [calc].", source=L_EN22),
    ("single_day", "2022-10-03", "2022-10-04"): dict(category="macro", cause=NI + "; broad rally (peer median +4.4%) [calc].", source=""),
    ("single_day", "2024-06-13", "2024-06-14"): dict(category="macro (French politics)", cause="French snap-election shock after dissolution of the National Assembly; management attributed ~15% share-price fall to it; Sodexo -2.3%, Rentokil -3.7% [calc].", source=L_FR24),
    ("single_day", "2024-09-05", "2024-09-06"): dict(category="M&A", cause="Market learned of Elis' exploratory talks with US players (incl. Vestis per CEO at CMD); Vestis +11.7% in the 5-Sep US session, Elis -15.7% next morning (open -9%) [calc]. Exact news item not available (News corpus not licensed).", source=L_US),
    ("single_day", "2024-10-03", "2024-10-04"): dict(category="M&A", cause="Termination of US talks at the beginning of October (financial discipline); intraday high +15% [calc].", source=L_US_END),
    ("single_day", "2025-03-05", "2025-03-06"): dict(category="earnings/guidance; capital markets", cause="FY2024 results + new capital allocation policy: EUR150m buyback starting 6-Mar-2025, dividend EUR0.45 (+5%), 2025 outlook; peers -0.6% [calc].", source=L_FY24),
    ("single_day", "2025-04-07", "2025-04-08"): dict(category="macro", cause="Rebound after the US-tariff sell-off (US peers +5% to +10% in the following session) [calc]; Elis later said no direct US-tariff impact; tariff timeline [u].", source=L_TAR),
    ("single_day", "2025-08-22", "2025-08-25"): dict(category="macro", cause=NI + "; broad decline (peers -1.6% to -4.2%) [calc]; [u] coincided with French government confidence-vote announcement.", source=""),
    ("single_day", "2026-03-02", "2026-03-03"): dict(category="macro (geopolitics/energy)", cause="Outbreak of Middle East (US/Israel/Iran) conflict -> energy price spike; Rentokil -5.2%, Vestis -3.1% [calc]; management stressed energy hedging on 11-Mar-2026.", source=L_ME),
    ("single_day", "2026-07-29", "2026-07-30"): dict(category="earnings/guidance; sector (partial)", cause="H1 2026 results (29-Jul after close): objectives only confirmed; Mexico volume loss; negative H1 FCF; EUR500m buyback already completed mid-July; peer median -2.5% [calc]. Same morning Rentokil's H1 2026 results (ADR -17.6%) flagged slower Q2 commercial growth - possible sector read-across [inference].", source=L_H126 + "; [#73](https://gam.prontonlp.com/#/ref/$SENTID_T000003774329-73) (Rentokil H1 2026: slower commercial growth in Q2)"),
    ("single_day", "2026-09-18", "2026-09-21"): dict(category="not identified", cause=NI + "; stock-specific (peers flat); close at session low EUR20.98 then +5.6% next day [calc] - pattern suggests technical/closing-auction effect [inference]; no Elis document after 30-Jul-2026 in ProntoNLP.", source=""),
    ("single_day", "2026-09-21", "2026-09-22"): dict(category="not identified", cause="Reversal of the 21-Sep drop; " + NI + ".", source=""),
    ("episode_1to20d", "2021-11-05", "2021-11-30"): dict(category="macro", cause="Late-2021 Covid/Omicron risk to hospitality (peer median -6.0%) [calc]; Omicron impact confirmed only for early 2022; specific attribution partly [u].", source=L_OMI),
    ("episode_1to20d", "2021-12-20", "2022-01-13"): dict(category="not identified", cause=NI + "; rebound after Nov-2021 sell-off, stock-specific vs peers (-4.1%) [calc].", source=""),
    ("episode_1to20d", "2022-02-10", "2022-03-08"): dict(category="macro (energy)", cause="Ukraine war -> gas price spike; Elis unhedged on energy at the time (management, 11-Mar-2026); peer median -10.3% [calc].", source=L_UKR + "; [#424](https://gam.prontonlp.com/#/ref/$SENTID_T000003676656-424) (not hedged in 2022)"),
    ("episode_1to20d", "2022-03-08", "2022-03-29"): dict(category="earnings/guidance; macro", cause="FY2021 results/2022 guidance with energy pass-through + market rebound (peer median +16.4%) [calc].", source=L_UKR),
    ("episode_1to20d", "2022-03-29", "2022-04-06"): dict(category="not identified", cause=NI + " (includes 5-Apr-2022 -6.3%).", source=""),
    ("episode_1to20d", "2022-04-06", "2022-05-05"): dict(category="not identified", cause=NI + "; Q1 2022 revenue document not in ProntoNLP list; stock-specific vs peers (-3.2%) [calc].", source=""),
    ("episode_1to20d", "2022-05-09", "2022-05-30"): dict(category="not identified", cause=NI + ".", source=""),
    ("episode_1to20d", "2022-05-30", "2022-06-16"): dict(category="macro", cause=NI + "; broad sell-off (peer median -10.2%) [calc].", source=""),
    ("episode_1to20d", "2022-06-30", "2022-07-27"): dict(category="macro; earnings/guidance", cause="Broad rebound (peer median +10.5%) [calc] into H1 2022 results (27-Jul, guidance raised).", source=L_H122),
    ("episode_1to20d", "2022-08-10", "2022-09-06"): dict(category="macro (energy)", cause="European energy-price crisis (gas, French power prices); peer median -8.5% [calc].", source=L_EN22),
    ("episode_1to20d", "2022-09-12", "2022-09-29"): dict(category="macro (energy/rates)", cause="Energy crisis peak and broad de-rating (peer median -9.0%) [calc]; specific trigger not identified; 29-Sep-2022 = 5-year closing low EUR9.91 [calc].", source=L_EN22),
    ("episode_1to20d", "2022-09-29", "2022-10-27"): dict(category="macro; earnings/guidance", cause="Rebound (peer median +12.5%) [calc] + Q3 2022 update (26-Oct): FY organic growth guidance raised to >+20%, energy costs falling.", source=L_Q322),
    ("episode_1to20d", "2022-11-02", "2022-11-11"): dict(category="macro", cause=NI + "; broad rally (peer median +7.5%) [calc].", source=""),
    ("episode_1to20d", "2022-11-16", "2022-12-13"): dict(category="not identified", cause=NI + "; stock-specific vs peers (+3.7%) [calc].", source=""),
    ("episode_1to20d", "2022-12-20", "2023-01-18"): dict(category="not identified", cause=NI + "; stock-specific vs peers (+1.8%) [calc]; continued into FY2022 revenue release (30-Jan-2023).", source=""),
    ("episode_1to20d", "2023-01-19", "2023-02-15"): dict(category="earnings/guidance", cause="FY2022 revenue (30-Jan-2023): 2023 organic growth of at least +10%, no slowdown seen; peers +1.0% [calc].", source=L_JAN23),
    ("episode_1to20d", "2023-07-06", "2023-07-24"): dict(category="not identified", cause=NI + "; pre-H1 2023 results run-up (results 26-Jul raised guidance, after window); peers +3.6% [calc].", source=L_H123),
    ("episode_1to20d", "2023-08-29", "2023-09-25"): dict(category="not identified", cause=NI + ". NB: the 4-Sep-2023 special call was a climate/CSR roadmap call recapping raised 2023 margin guidance, not an M&A call; peers -4.3% [calc].", source=L_SP23),
    ("episode_1to20d", "2023-10-11", "2023-10-30"): dict(category="earnings/guidance (partial)", cause="Q3 2023 revenue (25/26-Oct): 2023 outlook confirmed but no 2024 target (framed as decelerating price effect) [inference]; peers -1.9% [calc].", source=L_Q323),
    ("episode_1to20d", "2023-10-30", "2023-11-27"): dict(category="macro", cause=NI + "; broad rally (peer median +9.6%) [calc].", source=""),
    ("episode_1to20d", "2024-01-03", "2024-01-31"): dict(category="earnings/guidance", cause="FY2023 revenue (30-Jan-2024): organic +11.8%; peers +4.1% [calc].", source=L_JAN24),
    ("episode_1to20d", "2024-03-20", "2024-04-03"): dict(category="not identified", cause=NI + "; follows FY2023 results (7-Mar-2024, 2024 outlook organic c.+5%); peers ~0% [calc].", source=L_FY23),
    ("episode_1to20d", "2024-04-12", "2024-05-07"): dict(category="not identified", cause=NI + "; Q1 2024 revenue date not in ProntoNLP; Vestis guidance cut (2-May-2024, VSTS -45%) had no visible negative read-across (Elis 0.0% that day) [calc].", source=L_VS24),
    ("episode_1to20d", "2024-06-06", "2024-06-28"): dict(category="macro (French politics)", cause="French snap election/dissolution of the National Assembly; peers +2.7% -> France-specific [calc].", source=L_FR24),
    ("episode_1to20d", "2024-08-08", "2024-09-05"): dict(category="not identified", cause=NI + "; rebound after early-Aug-2024 sell-off; peers +5.2% [calc].", source=""),
    ("episode_1to20d", "2024-09-05", "2024-09-10"): dict(category="M&A", cause="US acquisition talks (incl. Vestis) feared as large/leveraging deal; peers +0.2% [calc].", source=L_US),
    ("episode_1to20d", "2024-10-02", "2024-10-18"): dict(category="M&A", cause="US talks terminated at the beginning of October 2024; peers +2.7% [calc].", source=L_US_END),
    ("episode_1to20d", "2024-10-30", "2024-11-08"): dict(category="earnings/guidance", cause="Q3 2024 revenue (29-Oct): FY2024 objectives confirmed, US talks formally disclosed as terminated; peers +5.1% [calc].", source=L_US_END),
    ("episode_1to20d", "2024-11-08", "2024-12-05"): dict(category="not identified", cause=NI + "; stock-specific (peers -1.7%) [calc]; Q3 release flagged disappointing hospitality (France/UK); French budget concerns raised by analysts at FY2024 results; [u] French government crisis.", source=L_FRBUD + "; " + L_US_END),
    ("episode_1to20d", "2025-02-19", "2025-03-18"): dict(category="earnings/guidance; capital markets", cause="FY2024 results, new capital allocation policy and EUR150m buyback; peers -7.1% -> stock-specific [calc].", source=L_FY24),
    ("episode_1to20d", "2025-03-18", "2025-04-07"): dict(category="macro (US tariffs)", cause="Global tariff sell-off (peer median -20.2%) [calc]; Elis less hit than peers.", source=L_TAR),
    ("episode_1to20d", "2025-04-07", "2025-05-02"): dict(category="macro; earnings/guidance", cause="Rebound (peer median +11.0%) [calc] + Q1 2025 revenue: objectives confirmed, no direct tariff impact.", source=L_TAR),
    ("episode_1to20d", "2025-08-15", "2025-09-02"): dict(category="not identified", cause=NI + "; peers -2.9% [calc]; [u] French political instability (Aug-Sep 2025).", source=""),
    ("episode_1to20d", "2026-01-21", "2026-02-20"): dict(category="sector; capital markets", cause="Sector rally (peer median +15.1%) [calc] + execution of the up-to-EUR500m 2026 buyback (from 6-Jan-2026).", source=L_BB26),
    ("episode_1to20d", "2026-02-20", "2026-03-20"): dict(category="macro (geopolitics/energy)", cause="Middle East conflict -> energy price spike (peer median -9.2%) [calc]; FY2025 results 11-Mar (dividend EUR0.48, buyback up to EUR500m) and Cintas-UniFirst deal did not reverse the trend.", source=L_ME + "; " + L_FY25 + "; " + L_CTUNF),
    ("episode_1to20d", "2026-03-20", "2026-04-17"): dict(category="macro", cause=NI + "; rebound (peer median +5.5%) [calc].", source=""),
    ("episode_1to20d", "2026-07-03", "2026-07-30"): dict(category="earnings/guidance; capital markets", cause="H1 2026 results (guidance only confirmed, Mexico volume loss) after the EUR500m buyback ended mid-July (end of buyback support = [inference]); peer median +7.3% -> stock-specific [calc], although Rentokil (ADR -19.1% in window) also disappointed on 30-Jul.", source=L_H126 + "; [#73](https://gam.prontonlp.com/#/ref/$SENTID_T000003774329-73) (Rentokil H1 2026: slower commercial growth in Q2)"),
    ("episode_1to20d", "2026-08-26", "2026-09-21"): dict(category="not identified", cause=NI + "; partly sector (UNF -8.3%, RTO -8.9%, CTAS -4.3%) [calc]; includes unexplained 21-Sep -6.4% day; possible OCEANE soft-call/arbitrage overhang = [inference].", source=""),
    ("calendar_month", "2021-10-29", "2021-11-30"): dict(category="macro", cause="See Nov-2021 episode (Omicron/Covid risk; partly [u]).", source=L_OMI),
    ("calendar_month", "2022-01-31", "2022-02-28"): dict(category="macro (energy)", cause="Ukraine war energy shock (last week of Feb-2022).", source=L_UKR),
    ("calendar_month", "2022-04-29", "2022-05-31"): dict(category="not identified", cause=NI + ".", source=""),
    ("calendar_month", "2022-05-31", "2022-06-30"): dict(category="macro", cause="Broad June-2022 sell-off plus unexplained 29-Jun -5.7% day; " + NI + " for the stock-specific part.", source=""),
    ("calendar_month", "2022-06-30", "2022-07-29"): dict(category="macro; earnings/guidance", cause="Market rebound + H1 2022 guidance raise (27-Jul).", source=L_H122),
    ("calendar_month", "2022-07-29", "2022-08-31"): dict(category="macro (energy)", cause="Energy price crisis.", source=L_EN22),
    ("calendar_month", "2022-08-31", "2022-09-30"): dict(category="macro (energy/rates)", cause="Energy crisis peak; 5-year low 29-Sep-2022 [calc].", source=L_EN22),
    ("calendar_month", "2022-09-30", "2022-10-31"): dict(category="macro; earnings/guidance", cause="Rebound + Q3 2022 guidance raise.", source=L_Q322),
    ("calendar_month", "2022-11-30", "2022-12-30"): dict(category="not identified", cause=NI + ".", source=""),
    ("calendar_month", "2022-12-30", "2023-01-31"): dict(category="earnings/guidance", cause="FY2022 revenue / 2023 organic growth >=+10% (30-Jan-2023).", source=L_JAN23),
    ("calendar_month", "2023-05-31", "2023-06-30"): dict(category="not identified", cause=NI + ".", source=""),
    ("calendar_month", "2023-10-31", "2023-11-30"): dict(category="macro", cause=NI + "; broad rally [calc].", source=""),
    ("calendar_month", "2024-04-30", "2024-05-31"): dict(category="not identified", cause=NI + " (Q1 2024 revenue period).", source=""),
    ("calendar_month", "2024-05-31", "2024-06-28"): dict(category="macro (French politics)", cause="French snap election.", source=L_FR24),
    ("calendar_month", "2024-08-30", "2024-09-30"): dict(category="M&A", cause="US acquisition talks.", source=L_US),
    ("calendar_month", "2024-09-30", "2024-10-31"): dict(category="M&A; earnings/guidance", cause="US talks terminated + Q3 2024 revenue.", source=L_US_END),
    ("calendar_month", "2026-01-30", "2026-02-27"): dict(category="sector; capital markets", cause="Sector rally + EUR500m buyback execution.", source=L_BB26),
    ("calendar_month", "2026-02-27", "2026-03-31"): dict(category="macro (geopolitics/energy)", cause="Middle East conflict energy shock.", source=L_ME),
    ("calendar_month", "2026-08-31", "2026-09-30"): dict(category="not identified", cause=NI + "; partly sector [calc].", source=""),
}
for col in ("category", "cause", "source"):
    moves[col] = ""
for k, v in CAUSES.items():
    t, s, e = k
    m = (moves.type == t) & (moves.start_date == s) & (moves.end_date == e)
    for col in ("category", "cause", "source"):
        moves.loc[m, col] = v.get(col, "")
missing = moves[moves.category == ""]
assert missing.empty, f"unclassified moves: {missing[['type','start_date','end_date']].values.tolist()}"
moves["price_source"] = "ProntoNLP getStockPrices (27989 + peers), [calc] in model/D_compute.py"
moves.to_csv(f"{OUT}/D_big_moves.csv", index=False)

stats["counts"] = {"single_day_ge5pct": int((moves.type == "single_day").sum()),
                   "episodes_ge10pct_1to20d": int((moves.type == "episode_1to20d").sum()),
                   "months_ge10pct": int((moves.type == "calendar_month").sum())}
stats["peer_split_check"] = {t: round(float(peers[t].pct_change().abs().max()) * 100, 1) for t in tics}

# ---------------------------------------------------------------- 5. peer-relative performance [calc]
pc = {"ELIS (EUR)": {}}
for n in (1, 3, 5):
    d0, p0 = close_on_or_before(c, yrs_back(last_dt, n))
    pc["ELIS (EUR)"][f"{n}y_pct"] = round((last_px / p0 - 1) * 100, 1)
for t in tics:
    s_ = peers[t]
    pc[t] = {}
    for n in (1, 3, 5):
        if s_.index[0] > yrs_back(last_dt, n) + timedelta(days=7):
            pc[t][f"{n}y_pct"] = "n/a (listed " + s_.index[0].strftime("%Y-%m-%d") + ")"
            continue
        d0, p0 = close_on_or_before(s_, yrs_back(last_dt, n))
        pc[t][f"{n}y_pct"] = round((float(s_.iloc[-1]) / p0 - 1) * 100, 1)
stats["peer_price_change"] = {"note": "CTAS/UNF/VSTS in USD; RTO = NYSE ADR in USD; SW = USD line (FX included); end date = last close in each series (2026-10-09)", **pc}

# ---------------------------------------------------------------- 6. dividend-adjustment test vs filing-quoted closes
REFS = [  # (date, filing close EUR, citation)
    ("2021-05-21", 14.93, "[#318](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000163792445-318) (2021 employee plan: closing price on subscription closing date)"),
    ("2021-12-31", 15.22, "[#4455](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000180181407-4455); [#4014](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000180181407-4014)"),
    ("2022-12-30", 13.82, "[#5365](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000202465426-5365) (another AR 2022 sentence [#4828](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000202465426-4828) says 15.22 - apparent copy error)"),
    ("2023-12-29", 18.39, "[#625](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000219356666-625) (garbled extraction)"),
    ("2024-12-31", 18.93, "[#4110](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000239166805-4110) (also 18.90 in [#4661](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000239166805-4661))"),
    ("2025-12-31", 24.26, "[#6050](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6050); [#6682](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6682) (another AR 2025 sentence [#6325](https://gam.prontonlp.com/#/ref/$SENTID_NONSEC000259591248-6325) says 21.64 - apparent typo)"),
]
dchk = []
for dt, ref, cite in REFS:
    ser = c if pd.Timestamp(dt) >= c.index[0] else wc
    if ser is wc:  # weekly bar dated Monday; Friday close of that week
        wk = wc[wc.index <= pd.Timestamp(dt)]
        d_used, px = wk.index[-1], float(wk.iloc[-1])
        basis = "weekly close (week of " + d_used.strftime("%Y-%m-%d") + ")"
    else:
        d_used, px = close_on_or_before(c, pd.Timestamp(dt))
        basis = "daily close " + d_used.strftime("%Y-%m-%d")
    dchk.append({"date": dt, "filing_close_eur": ref, "pronto_close_eur": px, "pronto_basis": basis,
                 "ratio_pronto_to_filing": round(px / ref, 4), "filing_source": cite})
stats["dividend_adjustment_check"] = {
    "observations": dchk,
    "conclusion": ("Inconsistent/partial adjustment: ProntoNLP equals filing closes at end-2024 and end-2025 (no back-adjustment for "
                   "the EUR0.45 (May-2025) and EUR0.48 (May-2026) dividends), but is 6.7% below filings in 2021 and 4.2% below at end-2022, "
                   "consistent with back-adjustment for dividends paid 2022-2024 (EUR0.37/0.41/0.43); the end-2023 filing value (EUR18.39, garbled text) "
                   "does not fit. Treat pre-mid-2024 levels as approximately dividend-adjusted and later levels as raw prices. [calc]"),
    "price_return_5y_on_filing_basis_pct": round((last_px / (close_on_or_before(c, yrs_back(last_dt, 5))[1] / 0.933) - 1) * 100, 1),
    "price_return_5y_note": "5y anchor (2021-10-08) divided by the 2021 ratio 0.933 to approximate the raw quoted price [calc, approximate]",
}
stats["source"] = SRC_ELIS_D + "; " + SRC_ELIS_W + "; all figures [calc]"
with open(f"{OUT}/D_price_stats.json", "w") as fh:
    json.dump(stats, fh, indent=2)

if __name__ == "__main__":
    pd.set_option("display.width", 250, "display.max_columns", 40, "display.max_rows", 300)
    print(json.dumps(stats, indent=1))
    print(moves.drop(columns=["price_source", "source", "cause"]).to_string())
