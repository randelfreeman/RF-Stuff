import sys; sys.path.insert(0, '.')
from chartkit import *
import numpy as np
OUT = "/home/user/RF-Stuff/reports/figures/"
yrs = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
rev = np.array([340.477, 349.940, 375.946, 463.724, 474.586])
oi = np.array([58.784, 64.478, 70.508, 79.670, 95.763])
ni = np.array([34.965, 43.062, 45.084, 65.882, 58.879])
da = np.array([18.572, 18.796, 20.457, 22.390, 24.316])
ebitda = oi + da

def bar_labels(ax, xs, vals, fmt="{:.0f}", dy=0):
    for x, v in zip(xs, vals):
        ax.text(x, v + dy, fmt.format(v), ha="center", va="bottom", fontsize=7.5, color=INK2)

# ---- fig02: 5-year P&L small multiples ----
fig = plt.figure(figsize=(8.6, 6.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.9], hspace=0.38, wspace=0.22)
axs = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])]
x = np.arange(5)
ax = axs[0]
ax.bar(x, rev, width=0.55, color=NAVY)
bar_labels(ax, x, rev, dy=6)
ax.set_xticks(x, yrs, fontsize=7.5); ax.set_title("Operating revenue (¥bn)"); ax.set_ylim(0, 560); clean(ax)
ax = axs[1]
w = 0.36
ax.bar(x - w/2 - 0.01, ebitda, width=w, color=BLUE, label="EBITDA (OI + D&A)")
ax.bar(x + w/2 + 0.01, oi, width=w, color=NAVY, label="Operating income (EBIT)")
ax.plot(x, ni, color=ORANGE, lw=2, marker="o", ms=5, mec="white", mew=1.5, label="Net income")
for xi, v in zip(x, ebitda): ax.text(xi - w/2, v + 2, f"{v:.0f}", ha="center", fontsize=7, color=INK2)
for xi, v in zip(x, oi): ax.text(xi + w/2, v + 2, f"{v:.0f}", ha="center", fontsize=7, color=INK2)
ax.set_xticks(x, yrs, fontsize=7.5); ax.set_title("Profit lines (¥bn)"); ax.set_ylim(0, 140); clean(ax)
ax.legend(loc="upper left", fontsize=7, ncol=1)
ax = axs[2]
m_oi = oi / rev * 100; m_eb = ebitda / rev * 100; m_ni = ni / rev * 100
for series, col, lab in [(m_eb, BLUE, "EBITDA margin"), (m_oi, NAVY, "EBIT margin"), (m_ni, ORANGE, "Net margin")]:
    ax.plot(x, series, color=col, lw=2, marker="o", ms=5, mec="white", mew=1.5, label=lab)
    ax.text(4.12, series[-1], f"{series[-1]:.1f}%", fontsize=7.5, color=INK2, va="center")
ax.set_xticks(x, yrs, fontsize=8); ax.set_title("Margins (% of revenue)"); ax.set_ylim(0, 30); ax.set_xlim(-0.3, 4.5); clean(ax)
ax.legend(loc="upper left", fontsize=7.5, ncol=3)
source(fig, "Source: Kessan Tanshin / Yuho (J-GAAP, FY = calendar year) via search extracts; D&A from cash-flow statement (stockanalysis/finboard). EBITDA = operating income + D&A.", y=-0.06)
save(fig, OUT + "fig02_five_year_pnl.png")

# ---- fig04: leverage ----
lab = ["FY21", "FY22", "FY23", "FY24", "FY25", "1H26"]
ibd = np.array([976.9, 989.8, 1089.0, 1191.6, 1343.9, 1536.6])
cash = np.array([87.0, 82.4, 127.3, 111.1, 152.3, 94.2])
nd = ibd - cash
nd_eb = np.array([nd[i] / ebitda[i] for i in range(5)] + [nd[5] / ebitda[4]])
fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.7), gridspec_kw={"width_ratios": [1.5, 1]})
x = np.arange(6); w = 0.36
ax = axs[0]
ax.bar(x - w/2 - 0.01, ibd, width=w, color=NAVY, label="Interest-bearing debt")
ax.bar(x + w/2 + 0.01, cash, width=w, color=PEER, label="Cash")
for xi, v in zip(x, ibd): ax.text(xi - w/2, v + 15, f"{v:,.0f}", ha="center", fontsize=7, color=INK2)
ax.set_xticks(x, lab); ax.set_title("Debt and cash (¥bn, period-end)"); ax.set_ylim(0, 1750); clean(ax)
ax.legend(loc="upper left", fontsize=7.5)
ax = axs[1]
ax.plot(x, nd_eb, color=BLUE, lw=2, marker="o", ms=6, mec="white", mew=1.5)
for xi, v in zip(x, nd_eb): ax.text(xi, v + 0.35, f"{v:.1f}x", ha="center", fontsize=7.5, color=INK2)
ax.set_xticks(x, lab); ax.set_title("Net debt / EBITDA (x)"); ax.set_ylim(0, 15); clean(ax)
fig.tight_layout()
source(fig, "1H26 ratio uses 30 Jun 2026 net debt over FY2025 EBITDA (seasonal inventory build inflates mid-year debt). Source: company filings via search extracts; research notes.", y=-0.06)
save(fig, OUT + "fig04_leverage.png")

# ---- fig05: dividends ----
fy = ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26E"]
dps = np.array([46, 51, 65, 73, 95, 105, 126])
payout = [None, None, 31.5, 33.8, 30.1, 37.1, 40.0]
fig, ax = plt.subplots(figsize=(8.5, 3.4))
cols = [NAVY] * 6 + [BLUE]
ax.bar(np.arange(7), dps, width=0.55, color=cols)
for i, (v, p) in enumerate(zip(dps, payout)):
    ax.text(i, v + 2, f"¥{v}", ha="center", fontsize=8, color=INK, fontweight="bold")
    if p: ax.text(i, v / 2, f"{p:.0f}%\npayout", ha="center", va="center", fontsize=7, color="white")
ax.set_xticks(np.arange(7), fy); ax.set_ylim(0, 145); clean(ax)
ax.set_title("Dividend per share (¥) — 13 consecutive increases incl. FY2026E")
source(fig, "FY2026E = company forecast ¥126 (interim ¥61 / year-end ¥65), raised from ¥122 on 6 Aug 2026; payout target 40% by FY2027. Source: company releases via search extracts.", y=-0.07)
save(fig, OUT + "fig05_dividends.png")

# ---- fig07: NAV bridge ----
fig, ax = plt.subplots(figsize=(8.0, 3.6))
bps, gain, nav, price = 2930, 2007, 4937, 3211
ax.bar(0, bps, width=0.5, color=NAVY)
ax.bar(1, gain, bottom=bps, width=0.5, color=BLUE)
ax.bar(2, nav, width=0.5, color=NAVY)
ax.bar(3, price, width=0.5, color=PEER)
for xi, v, top in [(0, bps, bps), (1, gain, bps + gain), (2, nav, nav), (3, price, price)]:
    ax.text(xi, top + 70, f"¥{v:,}", ha="center", fontsize=8.5, color=INK, fontweight="bold")
ax.text(3, price / 2, f"{price/nav:.2f}x\nP/NAV", ha="center", va="center", color=INK, fontsize=8.5)
ax.set_xticks(range(4), ["Book value / share\n(30 Jun 2026)", "After-tax unrealised\ngain on rental property", "NAV / share", "Share price\n(2 Oct 2026)"], fontsize=8)
ax.set_ylim(0, 5600); clean(ax)
ax.set_title("Net asset value bridge (¥ per share)")
source(fig, "Unrealised gain ¥599.9bn at 31 Dec 2025 (fair value ¥1,658.0bn vs book ¥1,058.1bn), taxed at 30.6%, ÷ ~207.5m shares. Source: FY2025 Yuho rental-property note via search extracts.", y=-0.08)
save(fig, OUT + "fig07_nav_bridge.png")
print("ok", [round(v, 1) for v in nd_eb])
