import sys; sys.path.insert(0, '.')
from chartkit import *
import pandas as pd, numpy as np, datetime as dt
from matplotlib.lines import Line2D
NOTES = "/home/user/RF-Stuff/research_notes/Tokyo Tatemono 8804 equity research/"
OUT = "/home/user/RF-Stuff/reports/figures/"

# ---------- 1. Price history ----------
s = pd.read_csv(NOTES + "stock_prices_8804.csv", parse_dates=["date"])
ann = s[s.frequency == "annual"].copy()
pts = [
    ("2020-12-30", 1415), ("2021-12-30", 1680), ("2022-12-30", 1599), ("2023-12-29", 2112),
    ("2024-12-30", 2607), ("2025-04-07", 2237.5), ("2025-10-07", 3074), ("2025-11-13", 2994),
    ("2025-11-14", 3305), ("2025-12-30", 3546), ("2026-01-30", 3629), ("2026-02-27", 4374),
    ("2026-03-31", 3587), ("2026-04-30", 3599), ("2026-05-29", 3269), ("2026-06-30", 3296),
    ("2026-07-31", 3387), ("2026-08-31", 3445), ("2026-09-18", 3236), ("2026-10-02", 3211),
]
px = pd.DataFrame(pts, columns=["date", "close"]); px["date"] = pd.to_datetime(px.date)
fig, ax = plt.subplots(figsize=(9.0, 4.6))
# annual high-low ranges 2020-2025 as thin translucent bars
for _, r in ann[ann.date.dt.year.between(2021, 2025)].iterrows():
    x0 = pd.Timestamp(f"{r.date.year}-01-01"); x1 = pd.Timestamp(f"{r.date.year}-12-31")
    ax.fill_between([x0, x1], r.low, r.high, color=BLUE, alpha=0.07, lw=0)
    ax.text(x0 + pd.Timedelta(days=183), r.low - 150, f"{int(r.low):,}–{int(r.high):,}", ha="center", fontsize=7, color=MUTED)
ax.fill_between([pd.Timestamp("2026-01-01"), pd.Timestamp("2026-10-02")], 3083, 4374, color=BLUE, alpha=0.07, lw=0)
ax.text(pd.Timestamp("2026-05-15"), 3083 - 150, "3,083–4,374 (YTD)", ha="center", fontsize=7, color=MUTED)
ax.plot(px.date, px.close, color=NAVY, lw=2, solid_joinstyle="round", solid_capstyle="round", zorder=3)
ax.scatter(px.date, px.close, s=14, color=NAVY, zorder=4, edgecolor="white", linewidth=1)
ev = [
    ("2025-04-07", 2237.5, "Apr-2025: US tariff shock — low ¥2,238 (−13.7% YTD), then +37% to Oct"),
    ("2025-11-14", 3305, "14-Nov-2025: FY25 guidance & DPS raised — +10.4% in one session"),
    ("2026-02-27", 4374, "27-Feb-2026: all-time high ¥4,374 (+20.5% in Feb) after FY25 beat / FY26 guide"),
    ("2026-03-31", 3587, "Mar-2026: sector sell-off as 10-yr JGB 2.13%→2.37% — −20.9% from peak"),
    ("2026-05-29", 3269, "May-2026: weak Q1 (NI −60%) — low ¥3,083 on 28 May (−21.4% from Apr high)"),
    ("2026-10-02", 3211, "2-Oct-2026: ¥3,211 after BOJ hike to 1.25% (18 Sep) — −26.6% from peak"),
]
for i, (d, v, lab) in enumerate(ev, 1):
    d = pd.Timestamp(d)
    ax.scatter([d], [v], s=150, color=BLUE, zorder=5, edgecolor="white", linewidth=1.5)
    ax.text(d, v, str(i), color="white", fontsize=7.2, fontweight="bold", ha="center", va="center", zorder=6)
key_y = 4650
for i, (d, v, lab) in enumerate(ev, 1):
    y = key_y - (i - 1) * 205
    ax.scatter([pd.Timestamp("2020-12-01")], [y], s=95, color=BLUE, zorder=5, edgecolor="white", linewidth=1)
    ax.text(pd.Timestamp("2020-12-01"), y, str(i), color="white", fontsize=6.5, fontweight="bold", ha="center", va="center", zorder=6)
    ax.text(pd.Timestamp("2021-01-20"), y, lab, fontsize=7.6, color=INK2, va="center")
ax.set_ylim(1100, 4850)
ax.set_xlim(pd.Timestamp("2020-09-15"), pd.Timestamp("2026-12-15"))
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"¥{v:,.0f}"))
clean(ax)
ax.set_title("Tokyo Tatemono (8804 JP): share price, end-2020 – 2 Oct 2026")
source(fig, "Path joins reported year-end, monthly (2026) and event-day closes; shaded bands = annual high–low range. Source: Nikkei, Kabutan (via search extracts); research notes.", y=-0.04)
save(fig, OUT + "fig01_price_history.png")

# ---------- 2. Regression scatter: EV/Sales vs EBIT margin ----------
d = pd.read_csv(NOTES + "peer_valuation_8804.csv")
core = d[d.group == "core"]
tt = d[d.ticker == 8804].iloc[0]
b, a = np.polyfit(core.ebit_margin, core.ev_sales, 1)
yhat = a + b * core.ebit_margin
r2 = 1 - ((core.ev_sales - yhat) ** 2).sum() / ((core.ev_sales - core.ev_sales.mean()) ** 2).sum()
fig, ax = plt.subplots(figsize=(8.6, 5.0))
xs = np.linspace(10, 32, 50)
ax.plot(xs, a + b * xs, color=MUTED, lw=1.2, zorder=1)
ax.scatter(core.ebit_margin, core.ev_sales, s=70, color=PEER, edgecolor="white", linewidth=2, zorder=3)
short = {8801: "Mitsui Fudosan", 8802: "Mitsubishi Estate", 8830: "Sumitomo Realty", 3289: "Tokyu Fudosan HD",
         3231: "Nomura RE HD", 3003: "Hulic", 8803: "Heiwa RE", 8818: "Keihanshin Bldg"}
offs = {8801: (-0.45, 0.0, "right"), 8802: (-0.45, 0.25, "right"), 8830: (-0.45, 0.0, "right"), 3289: (0.45, -0.05, "left"),
        3231: (0.45, -0.12, "left"), 3003: (0.45, -0.05, "left"), 8803: (0.45, 0.0, "left"), 8818: (-0.45, 0.0, "right")}
for _, r in core.iterrows():
    ox, oy, ha = offs[r.ticker]
    ax.text(r.ebit_margin + ox, r.ev_sales + oy, short[r.ticker], fontsize=8, color=INK2, ha=ha, va="center")
ax.scatter([tt.ebit_margin], [tt.ev_sales], s=110, color=BLUE, edgecolor="white", linewidth=2, zorder=4)
ax.annotate(f"Tokyo Tatemono\nactual {tt.ev_sales:.2f}x vs fitted {a + b * tt.ebit_margin:.2f}x",
            xy=(tt.ebit_margin, tt.ev_sales), xytext=(tt.ebit_margin + 0.6, tt.ev_sales - 2.3), fontsize=8.5,
            color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=BLUE, lw=1))
ax.set_xlabel("EBIT (operating) margin, last fiscal year (%)")
ax.set_ylabel("EV / Sales (x)")
ax.set_xlim(10, 32); ax.set_ylim(0, 10)
clean(ax, grid_axis="both")
ax.set_title("EV/Sales vs EBIT margin: listed Japanese developers")
ax.text(10.4, 9.35, f"OLS (8 peers, TT excluded): EV/Sales = {a:.2f} + {b:.3f} × margin;  R² = {r2:.2f}, t = 5.97",
        fontsize=8.2, color=INK2)
source(fig, "EV = market cap + interest-bearing debt − cash + NCI (hybrids 100% debt). Prices 7–30 Sep 2026; TT at ¥3,286 (25 Sep). Source: peer_valuation_8804.csv (Shikiho/kabuyoho/company filings via search extracts).", y=-0.05)
save(fig, OUT + "fig06_regression_ev_sales_ebit_margin.png")
print("regression", a, b, r2)
