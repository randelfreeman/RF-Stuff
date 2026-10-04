import sys; sys.path.insert(0, '.')
from chartkit import *
import pandas as pd, numpy as np
NOTES = "/home/user/RF-Stuff/research_notes/Tokyo Tatemono 8804 equity research/"
OUT = "/home/user/RF-Stuff/reports/figures/"
d = pd.read_csv(NOTES + "peer_valuation_8804.csv")
d = d[d.group.isin(["core", "target"])].copy()
short = {8804: "Tokyo Tatemono", 8801: "Mitsui Fudosan", 8802: "Mitsubishi Estate", 8830: "Sumitomo Realty", 3289: "Tokyu Fudosan HD",
         3231: "Nomura RE HD", 3003: "Hulic", 8803: "Heiwa RE", 8818: "Keihanshin Bldg"}
d["nm"] = d.ticker.map(short)
metrics = [("per_f", "Forward P/E (x)", "{:.1f}x"), ("pbr", "P/B (x)", "{:.2f}x"), ("ev_ebitda", "EV/EBITDA (x)", "{:.1f}x"), ("nd_ebitda", "Net debt / EBITDA (x)", "{:.1f}x")]
fig, axs = plt.subplots(2, 2, figsize=(8.6, 6.6))
for ax, (col, title, fmt) in zip(axs.flat, metrics):
    s = d.sort_values(col)
    cols = [BLUE if t == 8804 else PEER for t in s.ticker]
    ax.barh(range(len(s)), s[col], color=cols, height=0.62)
    med = d[d.ticker != 8804][col].median()
    ax.axvline(med, color=INK2, lw=1)
    ax.text(med, len(s) - 0.35, f" median {fmt.format(med)}", fontsize=7, color=INK2, va="bottom")
    for i, v in enumerate(s[col]):
        ax.text(v + (s[col].max() * 0.02), i, fmt.format(v), va="center", fontsize=7, color=INK2, bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none"), zorder=4)
    ax.set_yticks(range(len(s)), s.nm, fontsize=7.8)
    ax.set_xlim(0, s[col].max() * 1.25)
    ax.set_title(title, fontsize=9.5)
    clean(ax, grid_axis="x")
fig.tight_layout()
source(fig, "Median excludes Tokyo Tatemono. Prices 7–30 Sep 2026 (TT ¥3,286 on 25 Sep). Forward = current-year company/consensus forecasts. Source: peer_valuation_8804.csv (Shikiho, kabuyoho, company filings via search extracts).", y=-0.06)
save(fig, OUT + "fig08_peer_multiples.png")
print("ok")
