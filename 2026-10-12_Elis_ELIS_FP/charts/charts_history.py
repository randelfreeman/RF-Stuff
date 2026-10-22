import json, os, numpy as np
import matplotlib.pyplot as plt
from style import *
setup()
BASE = os.path.dirname(os.path.abspath(__file__))
H = json.load(open(os.path.join(BASE, '..', 'model', 'main_history.json')))['annual_and_ltm']
per = [r['period'].replace('FY', '') for r in H]
per[-1] = 'LTM\nJun-26'
x = np.arange(len(per))
SRC = 'Source: S&P Capital IQ (Elis SA, C_27989) — source link unavailable; analyst calculations [calc].'

def save(fig, name):
    fig.savefig(os.path.join(BASE, name)); plt.close(fig); print('saved', name)

# 1. Revenue
fig, ax = plt.subplots(figsize=(6.6, 2.6))
rev = [r['revenue'] for r in H]
cols = [BLUE] * (len(x) - 1) + [SEQ[2]]
ax.bar(x, rev, width=0.6, color=cols, zorder=2)
for xi, v in zip(x, rev):
    ax.text(xi, v + 60, f'{v/1000:.2f}', ha='center', va='bottom', fontsize=7.5, color=INK2)
ax.set_xticks(x, per); ax.set_ylim(0, max(rev) * 1.15); ax.set_ylabel('EUR m')
ax.set_title('Revenue, FY2016–LTM Jun-2026 (labels in EUR bn)')
source_note(fig, SRC); save(fig, 'hist_revenue.png')

# 2. Margins
fig, ax = plt.subplots(figsize=(6.6, 2.7))
series = [('EBITDA (EBIT + D&A) [calc]', 'ebitda_margin_calc', BLUE), ('EBITA (EBIT + PPA amortisation) [calc]', 'ebita_margin', ORANGE), ('EBIT (S&P operating income)', 'ebit_margin_sp', AQUA)]
for lab, k, c in series:
    y = [r[k] * 100 for r in H]
    ax.plot(x, y, color=c, label=lab, marker='o', markersize=4, markeredgecolor='white', markeredgewidth=1.2)
    ax.text(x[-1] + 0.25, y[-1] + (1.2 if k == 'ebita_margin' else (-1.2 if k == 'ebit_margin_sp' else 0)), f'{y[-1]:.1f}%', va='center', fontsize=7.5, color=INK2)
ax.set_xticks(x, per); ax.set_ylim(0, 46); ax.set_ylabel('% of revenue'); ax.set_xlim(-0.5, len(x) - 0.2)
ax.set_title('Margin history')
ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.0), fontsize=7.5)
source_note(fig, SRC); save(fig, 'hist_margins.png')

# 3. Cash flow
fig, ax = plt.subplots(figsize=(6.6, 2.7))
w = 0.27
cfo = [r['cfo'] for r in H]; capex = [r['capex'] for r in H]; fcf = [r['fcf_pre_lease'] for r in H]
ax.bar(x - w, cfo, width=w, color=BLUE, label='Cash from operations', zorder=2)
ax.bar(x, capex, width=w, color=ORANGE, label='Capex (incl. linen)', zorder=2)
ax.bar(x + w, fcf, width=w, color=AQUA, label='FCF before leases & M&A [calc]', zorder=2)
ax.axhline(0, color=AXIS, linewidth=0.8)
ax.set_xticks(x, per); ax.set_ylabel('EUR m'); ax.set_title('Operating cash flow, capex and free cash flow')
ax.legend(loc='upper left', ncol=3)
ax.set_ylim(min(fcf) - 100, max(cfo) * 1.25)
source_note(fig, SRC); save(fig, 'hist_cashflow.png')

# 4. Leverage
fig, ax = plt.subplots(figsize=(6.6, 2.5))
for lab, k, c in [('Net debt / EBITDA excl. leases [calc]', 'nd_ebitda_ex_leases', BLUE), ('Net debt / EBITDA incl. IFRS 16 leases [calc]', 'nd_ebitda_incl_leases', ORANGE)]:
    y = [r[k] for r in H]
    ax.plot(x, y, color=c, label=lab, marker='o', markersize=4, markeredgecolor='white', markeredgewidth=1.2)
    ax.text(x[-1] + 0.25, y[-1], f'{y[-1]:.2f}x', va='center', fontsize=7.5, color=INK2)
ax.set_xticks(x, per); ax.set_ylim(0, 5.5); ax.set_xlim(-0.5, len(x) - 0.2); ax.set_ylabel('x EBITDA')
ax.set_title('Leverage (S&P-based EBITDA = EBIT + total D&A)')
ax.legend(loc='upper right')
source_note(fig, SRC); save(fig, 'hist_leverage.png')

# 5. Returns
fig, ax = plt.subplots(figsize=(6.6, 2.5))
fy = [r for r in H if r['period'].startswith('FY') and r.get('roe') is not None]
xx = np.arange(len(fy)); lab = [r['period'].replace('FY', '') for r in fy]
for l, k, c in [('ROE (net income / avg. equity)', 'roe', BLUE), ('ROIC (EBITA after tax / avg. equity + net debt incl. leases)', 'roic_ebita', ORANGE)]:
    y = [r[k] * 100 for r in fy]
    ax.plot(xx, y, color=c, label=l, marker='o', markersize=4, markeredgecolor='white', markeredgewidth=1.2)
    ax.text(xx[-1] + 0.2, y[-1], f'{y[-1]:.1f}%', va='center', fontsize=7.5, color=INK2)
ax.set_xticks(xx, lab); ax.set_ylim(0, 12); ax.set_xlim(-0.4, len(xx) - 0.3); ax.set_ylabel('%')
ax.set_title('Returns on capital [calc]')
ax.legend(loc='upper left')
source_note(fig, SRC); save(fig, 'hist_returns.png')

# 6. Uses of cash
fig, ax = plt.subplots(figsize=(6.6, 2.7))
comp = [('Capex (net of disposals)', lambda r: r['capex'] - r['sale_ppe'] + r['intangibles_capex'], BLUE), ('Acquisitions', lambda r: r['acquisitions'], ORANGE), ('Dividends', lambda r: r['dividends_paid'], AQUA), ('Buybacks', lambda r: r['buybacks'], YELLOW)]
bottom = np.zeros(len(x))
for l, f, c in comp:
    y = np.array([max(f(r), 0) for r in H])
    ax.bar(x, y, bottom=bottom, width=0.6, color=c, label=l, zorder=2, edgecolor='white', linewidth=0.8)
    bottom += y
ax.set_xticks(x, per); ax.set_ylabel('EUR m'); ax.set_title('Uses of cash: reinvestment, M&A and shareholder returns')
ax.legend(loc='upper left', ncol=4)
ax.set_ylim(0, bottom.max() * 1.18)
source_note(fig, SRC); save(fig, 'hist_uses_of_cash.png')
