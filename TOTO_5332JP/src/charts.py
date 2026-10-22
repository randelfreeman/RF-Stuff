import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

NAVY = '#16243D'; BLUE = '#2F6FD0'; GREY = '#9AA3B2'; LIGHT = '#C9CED8'; RED = '#B23A2E'; TEAL = '#3E8E7E'
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#5E6878', 'axes.labelcolor': '#1C2433', 'xtick.color': '#5E6878', 'ytick.color': '#5E6878',
                     'axes.grid': True, 'grid.color': '#E3E6EC', 'grid.linewidth': 0.6, 'axes.axisbelow': True})
OUT = 'img/'
import os; os.makedirs(OUT, exist_ok=True)

# 1. Price path (reconstructed from annual OHLC + event closes)
pts = [('Feb-21', 7380), ('Oct-21', 4995), ('Dec-21', 5290), ('Jun-22', 4105), ('Dec-22', 4500), ('Jan-23', 4900),
       ('Aug-23', 3831), ('Dec-23', 3713), ('Feb-24', 3642), ('Oct-24', 5530), ('Oct-24b', 4303), ('Dec-24', 3805), ('Apr-25', 3269),
       ('Aug-25', 4084), ('Dec-25', 4334), ('Jan-26', 5300), ('Feb-26', 6075), ('May-26', 6425), ('Jun-26', 9500),
       ('Jul-26', 7008), ('Aug-26', 6209), ('Oct-26', 6097)]
fig, ax = plt.subplots(figsize=(8.2, 3.6), dpi=200)
y = [p[1] for p in pts]; x = np.arange(len(pts))
ax.plot(x, y, color=NAVY, lw=1.8, marker='o', ms=3.2)
lab = [p[0][:-1] if p[0].endswith('b') and p[0][-2].isdigit() else p[0] for p in pts]
ax.set_xticks(x); ax.set_xticklabels(lab, fontsize=6.2, rotation=45)
ax.set_ylabel('JPY / share')
ann = {9: 'China stimulus\nhigh', 10: 'H1 FY3/25: China\nimpairment -12.5%', 12: 'US tariff\nlow', 15: 'GS upgrade\n+11%',
       16: 'Palliser\nstake', 17: 'FY3/26 results\nlimit-up +18%', 18: 'ATH ¥9,500\n¥80bn capex rpt', 20: 'Q1 miss\n-11.4%'}
for i, t in ann.items():
    off = {16: 2300, 17: 1500, 15: 900, 18: 600}.get(i, 900) if i not in (10, 12, 20) else -1500
    dx = {16: -0.9, 17: 0.2}.get(i, 0)
    ax.annotate(t, (x[i], y[i]), xytext=(x[i] + dx, y[i] + off), fontsize=6.3, ha='center', color='#1C2433',
                arrowprops=dict(arrowstyle='-', color=GREY, lw=0.6))
ax.set_ylim(1200, 11200)
fig.tight_layout(); fig.savefig(OUT + 'price.png'); plt.close()

# 2. Revenue & OP
yrs = ['FY3/22', 'FY3/23', 'FY3/24', 'FY3/25', 'FY3/26', 'FY3/27E', 'FY3/28E', 'FY3/29E']
sales = [645.3, 701.2, 702.3, 724.5, 737.4, 765.0, 800.0, 833.0]
op = [52.2, 49.1, 42.8, 48.5, 53.8, 60.0, 78.0, 87.5]
fig, ax = plt.subplots(figsize=(8.2, 3.3), dpi=200)
cols = [NAVY] * 5 + [BLUE] * 3
ax.bar(yrs, sales, color=cols, width=0.6)
ax.set_ylabel('Net sales (JPY bn)'); ax.set_ylim(0, 950)
ax2 = ax.twinx(); ax2.plot(yrs, [o / s * 100 for o, s in zip(op, sales)], color=RED, marker='o', lw=1.6)
ax2.set_ylabel('Operating margin (%)', color=RED); ax2.set_ylim(0, 12); ax2.grid(False)
ax2.spines['right'].set_visible(True)
for i, (s, o) in enumerate(zip(sales, op)):
    ax.text(i, s + 12, '%.0f\nOP %.1f' % (s, o), ha='center', fontsize=6.5)
fig.tight_layout(); fig.savefig(OUT + 'sales_op.png'); plt.close()

# 3. Segment OP mix
seg_yrs = ['FY3/22', 'FY3/23', 'FY3/24', 'FY3/25', 'FY3/26', 'FY3/27E', 'FY3/28E']
cer = [9.2, 19.4, 13.0, 20.4, 28.9, 32.5, 40.4]
hou = [45.8, 32.5, 32.6, 30.9, 27.9, 30.8, 41.0]
fig, ax = plt.subplots(figsize=(8.2, 3.2), dpi=200)
ax.bar(seg_yrs, hou, color=GREY, width=0.6, label='Housing equipment (Japan + overseas)')
ax.bar(seg_yrs, cer, bottom=hou, color=BLUE, width=0.6, label='Advanced Ceramics')
for i, (h, c) in enumerate(zip(hou, cer)):
    ax.text(i, h + c + 1.2, '%d%%' % round(c / (h + c) * 100), ha='center', fontsize=7.5, color=BLUE, fontweight='bold')
ax.set_ylabel('Segment OP (JPY bn)'); ax.legend(frameon=False, fontsize=7.5, loc='upper left'); ax.set_ylim(0, 95)
ax.text(0.99, 0.95, '% = ceramics share of segment OP\nFY3/22-24 reconstructed (e)', transform=ax.transAxes, ha='right', va='top', fontsize=6.5, color='#5E6878')
fig.tight_layout(); fig.savefig(OUT + 'seg_mix.png'); plt.close()

# 4. Regression: EV/Sales vs EBIT margin
peers = [('LIXIL', 2.5, 0.66), ('Takara Std', 7.5, 0.41), ('Cleanup', 2.9, 0.15), ('Rinnai', 10.7, 0.75), ('Geberit', 24.0, 6.9),
         ('Masco', 16.8, 2.1), ('Fortune Brands', 15.7, 1.71), ('Villeroy & Boch', 6.8, 0.47), ('NGK Insulators', 14.2, 2.5),
         ('Kyocera', 5.2, 1.06), ('Niterra', 18.9, 2.27), ('Ferrotec', 8.8, 1.15)]
toto = ('TOTO', 7.3, 1.27)
xm = np.array([p[1] for p in peers]); ye = np.array([p[2] for p in peers])
b, a = np.polyfit(xm, ye, 1); pred = a + b * xm
r2 = 1 - ((ye - pred) ** 2).sum() / ((ye - ye.mean()) ** 2).sum()
fair = a + b * toto[1]
# ex-Geberit robustness
m = np.array([p[0] != 'Geberit' for p in peers])
b2, a2 = np.polyfit(xm[m], ye[m], 1); pred2 = a2 + b2 * xm[m]
r22 = 1 - ((ye[m] - pred2) ** 2).sum() / ((ye[m] - ye[m].mean()) ** 2).sum()
fair2 = a2 + b2 * toto[1]
# SOTP-consistent: what margin would TOTO need to "deserve" 1.27x
fig, ax = plt.subplots(figsize=(8.2, 4.0), dpi=200)
ax.scatter(xm, ye, s=46, color=LIGHT, edgecolor=GREY, zorder=3)
OFF = {'Villeroy & Boch': (-30, 7), 'Takara Std': (5, -10), 'Ferrotec': (5, -11), 'Niterra': (5, 5), 'Masco': (-12, 7), 'Kyocera': (-10, 7)}
for n, mx, ev in peers:
    ax.annotate(n, (mx, ev), xytext=OFF.get(n, (4, 3)), textcoords='offset points', fontsize=6.8, color='#5E6878')
ax.scatter([toto[1]], [toto[2]], s=70, color=BLUE, zorder=4)
ax.annotate('TOTO (consolidated)', (toto[1], toto[2]), xytext=(-20, 10), textcoords='offset points', fontsize=7.5, color=BLUE, fontweight='bold')
ax.scatter([42.9], [None or 0], alpha=0)
xx = np.linspace(0, 26, 50)
ax.plot(xx, a + b * xx, color=NAVY, lw=1, ls='--', label='All peers: EV/S = %.3f×margin %+.2f, R²=%.2f' % (b, a, r2))
ax.plot(xx, a2 + b2 * xx, color=RED, lw=1, ls=':', label='Ex-Geberit: EV/S = %.3f×margin %+.2f, R²=%.2f' % (b2, a2, r22))
ax.set_xlabel('EBIT margin, latest FY (%)'); ax.set_ylabel('EV / Sales (x)'); ax.legend(frameon=False, fontsize=7, loc='upper left')
ax.set_xlim(0, 27); ax.set_ylim(-0.2, 7.5)
fig.tight_layout(); fig.savefig(OUT + 'regression.png'); plt.close()
json.dump({'b': b, 'a': a, 'r2': r2, 'fair': fair, 'b2': b2, 'a2': a2, 'r22': r22, 'fair2': fair2}, open('reg.json', 'w'), indent=1)
print('reg all', b, a, r2, fair, ' exGeb', b2, a2, r22, fair2)

# 5. Scenario football field
fig, ax = plt.subplots(figsize=(8.2, 2.9), dpi=200)
rows = [('Bear (memory capex downturn)', 3400, 4400), ('Base (SOTP FY3/28E)', 6800, 7800), ('Bull (ceramics compounding)', 9000, 10800),
        ('Peer P/E 18-23x FY3/28E EPS', 6340, 8100), ('Sell-side target range', 5900, 11100), ('52-week range', 3766, 9500)]
for i, (n, lo, hi) in enumerate(rows[::-1]):
    ax.barh(i, hi - lo, left=lo, color=[GREY, BLUE, NAVY, TEAL, BLUE, RED][::-1][i], height=0.55)
    ax.text(hi + 80, i, '¥%s–%s' % (format(lo, ','), format(hi, ',')), va='center', fontsize=7)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows[::-1]], fontsize=7.5)
ax.axvline(6097, color='#1C2433', lw=1, ls='--'); ax.text(6097, len(rows) - 0.4, 'Price ¥6,097', fontsize=7, ha='center')
ax.axvline(7200, color=BLUE, lw=1, ls='-'); ax.text(7200, -0.85, 'Target ¥7,200', fontsize=7, ha='center', color=BLUE)
ax.set_xlim(2500, 12800); ax.set_xlabel('JPY / share')
fig.tight_layout(); fig.savefig(OUT + 'football.png'); plt.close()

# 6. Ceramics sales & margin
cy = ['FY3/22e', 'FY3/23e', 'FY3/24e', 'FY3/25', 'FY3/26', 'FY3/27E', 'FY3/28E', 'FY3/29E']
cs = [36, 49.5, 42, 50.3, 67.4, 77.5, 95, 110]; co = [9.2, 19.4, 13.0, 20.4, 28.9, 32.5, 40.4, 46.2]
fig, ax = plt.subplots(figsize=(8.2, 3.0), dpi=200)
ax.bar(cy, cs, color=[GREY] * 3 + [NAVY] * 2 + [BLUE] * 3, width=0.6); ax.set_ylabel('Ceramics sales (JPY bn)')
ax2 = ax.twinx(); ax2.plot(cy, [o / s * 100 for o, s in zip(co, cs)], color=RED, marker='o'); ax2.set_ylim(0, 55); ax2.grid(False)
ax2.set_ylabel('OP margin (%)', color=RED); ax2.spines['right'].set_visible(True)
for i, s in enumerate(cs): ax.text(i, s + 2, '%.0f' % s, ha='center', fontsize=7)
ax.set_ylim(0, 130)
fig.tight_layout(); fig.savefig(OUT + 'ceramics.png'); plt.close()
