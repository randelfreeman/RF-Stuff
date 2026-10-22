import json, os, csv, numpy as np
import matplotlib.pyplot as plt
from style import *
setup(); B = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(B, '..', 'model')
E = json.load(open(os.path.join(M, 'E_peer_multiples_lead.json'))); rows = E['rows']; rg = E['regression']
def regchart(path, figsize):
    fig, ax = plt.subplots(figsize=figsize)
    xs = np.linspace(0, 26, 50); ax.plot(xs, rg['intercept'] + rg['slope'] * xs, '--', color=BLUE, lw=1.4, zorder=2)
    for r in rows:
        x, y = r['ebit_m'] * 100, r['ev_sales']
        if r['ticker'] == 'ELIS':
            ax.scatter([x], [y], s=90, color=CRITICAL, edgecolor='white', lw=1.5, zorder=5)
            ax.annotate(f"Elis {y:.2f}x (implied {rg['elis_implied']:.2f}x)", (x, y), xytext=(10, -22), textcoords='offset points', fontsize=7.5, color=INK, fontweight='bold')
        else:
            col = NAVY if 'Direct' in r['group'] else PEER_GRAY
            ax.scatter([x], [y], s=46, color=col, edgecolor='white', lw=1.2, zorder=4)
            ax.annotate(r['ticker'], (x, y), xytext=((5, -10) if r['ticker'] in ('SW','ISS','BNZL','JSG') else (5, 3)), textcoords='offset points', fontsize=7, color=INK2)
    ax.text(0.98, 0.05, f"OLS (12 listed peers, ex-Elis): EV/Sales = {rg['intercept']:.2f} + {rg['slope']:.3f} x EBIT margin (%)\nR² = {rg['r2']:.2f}", transform=ax.transAxes, ha='right', fontsize=7, color=BLUE)
    ax.set_xlabel('EBIT margin, LTM (%)'); ax.set_ylabel('EV / Sales, LTM (x)'); ax.set_xlim(0, 26); ax.set_ylim(0, 8)
    ax.grid(axis='both')
    source_note(fig, 'Source: S&P Capital IQ LTM financials (S&P-standardised EBIT, net debt incl. leases); ProntoNLP market caps; analyst regression [calc]. Navy = direct textile/hygiene-service peers; grey = broader services.')
    fig.savefig(path); plt.close(fig)
regchart(os.path.join(B, 'regression.png'), (6.8, 3.8)); regchart(os.path.join(B, 'regression_memo.png'), (7.6, 4.2))
# valuation history
V = json.load(open(os.path.join(M, 'main_valuation_history.json')))
fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.6))
lab = [str(v['year'])[:4] if v['year'] != 'Current (9-Oct-26)' else 'Now' for v in V]
for ax, k, t in [(axs[0], 'ev_adj_ebitda', 'EV / Elis adjusted EBITDA (x)'), (axs[1], 'ev_ebit', 'EV / S&P EBIT (x)')]:
    y = [v[k] for v in V]; ax.bar(range(len(y)), y, color=[BLUE] * (len(y) - 1) + [ORANGE], width=0.6, zorder=2)
    for i, val in enumerate(y): ax.text(i, val + 0.2, f'{val:.1f}', ha='center', fontsize=7.5, color=INK2)
    ax.set_xticks(range(len(y)), lab); ax.set_title(t, fontsize=9); ax.set_ylim(0, max(y) * 1.2)
source_note(fig, 'Year-end price x shares + S&P net debt incl. leases; current = 215.9m shares x €21.26 + net debt €3,670m + leases €700m [calc]. Early-year prices partly dividend-adjusted.')
fig.savefig(os.path.join(B, 'valuation_history.png')); plt.close(fig)
# segment margins FY2021-25
S = list(csv.DictReader(open(os.path.join(M, 'F_segments_annual.csv'))))
segs = ['France', 'Central Europe', 'Scandinavia & Eastern Europe', 'UK & Ireland', 'Latin America', 'Southern Europe']
fig, ax = plt.subplots(figsize=(6.8, 2.9))
yrs = ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025', 'H1 2026']
for i, sname in enumerate(segs):
    y = []
    for p in yrs:
        m = [r for r in S if r['segment'].startswith(sname[:12]) and r['period'] == p and r['ebitda_margin']]
        y.append(float(m[0]['ebitda_margin']) * 100 if m else np.nan)
    ax.plot(range(len(yrs)), y, marker='o', markersize=4, color=CAT[i], label=sname, markeredgecolor='white')
ax.set_xticks(range(len(yrs)), yrs); ax.set_ylabel('Adj. EBITDA margin (%)'); ax.set_ylim(24, 45)
ax.legend(ncol=3, fontsize=7, loc='lower left'); ax.set_ylim(18, 45)
source_note(fig, 'Source: Elis annual/semi-annual reports and calls via ProntoNLP (worker F, model/F_segments_annual.csv). H1 margins are seasonally lower than full-year.')
fig.savefig(os.path.join(B, 'segment_margins.png')); plt.close(fig)
# scenarios
sc = [('Bear (25%)', 17.2, CRITICAL), ('Base (55%)', 26.0, BLUE), ('Bull (20%)', 33.0, GOOD), ('Takeout range', 34.0, VIOLET)]
fig, ax = plt.subplots(figsize=(6.4, 2.6))
for i, (l, v, c) in enumerate(sc):
    ax.bar(i, v, color=c, width=0.55, zorder=2); ax.text(i, v + 0.6, f'€{v:.1f}\n({(v/21.26-1)*100:+.0f}%)' if i < 3 else '€30–38\n(+41% to +79%)', ha='center', fontsize=7.5, color=INK2)
ax.axhline(21.26, color=INK, lw=1, ls='--'); ax.text(3.45, 21.6, 'Price €21.26', fontsize=7, ha='right', color=INK)
ax.set_xticks(range(4), [s[0] for s in sc]); ax.set_ylim(0, 42); ax.set_ylabel('EUR per share'); ax.set_title('12-month scenario values (probability-weighted ≈ €25)')
source_note(fig, 'Analyst estimates [e]; see Section 20.')
fig.savefig(os.path.join(B, 'scenarios.png')); plt.close(fig)
print('ok')
