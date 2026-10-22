import sys; sys.path.insert(0, '.')
from chartkit import *
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
OUT = "/home/user/RF-Stuff/reports/figures/"

# ---- fig03: segment profit FY2023-FY2025 + 1H ----
segs = ["Building /\nCommercial", "Residential", "Asset\nService", "Other"]
fy23 = [40.1, 27.1, 12.9, 4.4]      # business-profit basis
fy24 = [41.4, 38.2, 11.5, 2.1]      # restated OI basis (Other ≈)
fy25 = [67.1, 25.6, 11.5, 4.2]      # OI
fig, axs = plt.subplots(2, 1, figsize=(8.6, 6.8), gridspec_kw={"height_ratios": [1.15, 1], "hspace": 0.42})
ax = axs[0]; x = np.arange(4); w = 0.26
for k, (vals, col, lab) in enumerate([(fy23, PEER, "FY2023 (business-profit basis)"), (fy24, BLUE, "FY2024 (restated OI)"), (fy25, NAVY, "FY2025 (OI)")]):
    xs = x + (k - 1) * (w + 0.02)
    ax.bar(xs, vals, width=w, color=col, label=lab)
    for xi, v in zip(xs, vals):
        ax.text(xi, v + 1, f"{v:.1f}", ha="center", fontsize=7, color=INK2)
ax.set_xticks(x, segs, fontsize=8); ax.set_ylim(0, 80); clean(ax)
ax.set_title("Segment profit by year (¥bn)"); ax.legend(fontsize=7.5, loc="upper right")
ax = axs[1]
h1 = [("Building OI", 18.0, 40.1), ("Residential OI", 17.3, 2.95), ("Group OI", 34.0, 39.9)]
x2 = np.arange(3); w2 = 0.36
ax.bar(x2 - w2/2 - 0.01, [a for _, a, _ in h1], width=w2, color=PEER, label="1H FY2025")
ax.bar(x2 + w2/2 + 0.01, [b for _, _, b in h1], width=w2, color=NAVY, label="1H FY2026")
for xi, (_, a, b) in zip(x2, h1):
    ax.text(xi - w2/2, a + 0.8, f"{a:.1f}", ha="center", fontsize=7, color=INK2)
    ax.text(xi + w2/2, b + 0.8, f"{b:.1f}", ha="center", fontsize=7, color=INK2)
ax.set_xticks(x2, [n for n, _, _ in h1], fontsize=8); ax.set_ylim(0, 56); clean(ax)
ax.set_title("1H FY2026 vs 1H FY2025: sales up, condos in trough (¥bn)"); ax.legend(fontsize=7.5, loc="upper center", ncol=2)
source(fig, "FY2024 segment figures implied by FY2025 YoY changes; FY2023 on the company's business-profit basis; 1H FY2025 segment values derived from reported 1H FY2026 growth rates. Source: company materials via search extracts.", y=-0.06)
save(fig, OUT + "fig03_segment_profit.png")

# ---- fig09: EPS path ----
yrs = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26E", "FY27E", "FY28E"]
eps = [167.35, 206.15, 215.82, 315.49, 283.08, 315, 323, 330]
fig, ax = plt.subplots(figsize=(8.8, 3.6))
cols = [NAVY] * 5 + [BLUE] * 3
ax.bar(range(8), eps, width=0.55, color=cols)
for i, v in enumerate(eps):
    ax.text(i, v + 5, f"¥{v:,.0f}", ha="center", fontsize=8, color=INK, fontweight="bold")
from matplotlib.lines import Line2D
for xi, v, c in [(5, 313, ORANGE), (5, 320, AQUA), (6, 311, YELLOW)]:
    ax.plot([xi + 0.32, xi + 0.52], [v, v], color=c, lw=3, solid_capstyle="butt", zorder=4)
hand = [Line2D([0], [0], color=ORANGE, lw=3), Line2D([0], [0], color=AQUA, lw=3), Line2D([0], [0], color=YELLOW, lw=3)]
ax.legend(hand, ["Company guidance FY26 (≈¥313)", "Consensus FY26 (≈¥320)", "Toyo Keizai FY27 (≈¥311)"], fontsize=7.5, loc="upper left", ncol=1, frameon=False)
ax.set_xticks(range(8), yrs); ax.set_ylim(0, 420); ax.set_xlim(-0.6, 7.7); clean(ax)
ax.set_title("EPS (¥): actuals FY2021–25 and our FY2026–28 estimates")
source(fig, "Estimates: this report (Section 8). FY2024 includes ≈¥20–25bn of extraordinary gains; FY2025 includes a −¥6.9bn equity-method loss.", y=-0.07)
save(fig, OUT + "fig09_eps_path.png")

# ---- fig10: valuation football field ----
rows = [
    ("52-week trading range", 2994, 4374, None),
    ("Own 3-yr P/E band (7.0–9.9x) on FY26E EPS", 2190, 3090, None),
    ("P/NAV 0.50–0.85x on NAV ¥4,937", 2469, 4196, None),
    ("Peer EV/Sales regression (variants)", 2376, 4477, 3271),
    ("Scenario range: bear – bull", 2300, 4400, 3400),
    ("Sell-side target prices (range; avg ¥3,985)", 3680, 4480, 3985),
    ("Takeout zone (30–50% premium)", 4174, 4816, None),
]
fig, ax = plt.subplots(figsize=(9.5, 4.2))
for i, (lab, lo, hi, mid) in enumerate(rows[::-1]):
    ax.barh(i, hi - lo, left=lo, height=0.5, color=BLUE if "Scenario" in lab else PEER)
    ax.text(lo - 40, i, f"¥{lo:,}", ha="right", va="center", fontsize=7.5, color=INK2, bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none"), zorder=5)
    ax.text(hi + 40, i, f"¥{hi:,}", ha="left", va="center", fontsize=7.5, color=INK2, bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none"), zorder=5)
    if mid:
        ax.plot([mid, mid], [i - 0.25, i + 0.25], color=NAVY, lw=2.5)
ax.set_yticks(range(len(rows)), [r[0] for r in rows[::-1]], fontsize=8)
ax.axvline(3211, color=ORANGE, lw=1.5); ax.text(3195, len(rows) - 0.45, "Price ¥3,211 ", color=INK, fontsize=8, va="bottom", ha="right")
ax.axvline(3400, color=NAVY, lw=1.5); ax.text(3415, len(rows) - 0.45, " Target ¥3,400", color=INK, fontsize=8, va="bottom", ha="left")
ax.set_xlim(1700, 5400); ax.set_ylim(-0.6, len(rows) + 0.1)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"¥{v:,.0f}"))
clean(ax, grid_axis="x")
ax.set_title("Valuation football field (¥ per share)")
source(fig, "Dark ticks = central values (regression base ¥3,271; probability-weighted ¥3,400; consensus average ¥3,985). Source: this report, Sections 10, 11 and 19.", y=-0.06)
save(fig, OUT + "fig10_football_field.png")
print("ok")
