import csv, os, json, datetime as dt
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from style import *
setup()
BASE = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(BASE, '..', 'model')
W = list(csv.DictReader(open(os.path.join(M, 'D_elis_prices_weekly.csv'))))
d = [dt.date.fromisoformat(r['date']) for r in W]; c = [float(r['close']) for r in W]
def nearest(date):
    i = min(range(len(d)), key=lambda k: abs((d[k] - date).days)); return d[i], c[i]
EVENTS = [
 ('2020-03-23', 'MAR 2020', 'Covid crash: -58% peak-to-trough; FY2019 dividend withdrawn', 'down'),
 ('2022-03-07', 'FEB-MAR 2022', 'Ukraine war / gas-price shock: -29% in four weeks', 'down'),
 ('2022-09-26', 'SEP 2022', '5-year low €9.91; OCEANE 2029 convertible issued (€380m, 2.25%)', 'down'),
 ('2023-11-20', 'NOV 2023', 'S&P upgrade to investment grade (BBB-)', 'up'),
 ('2024-06-17', 'JUN 2024', 'French snap election: about -15%', 'down'),
 ('2024-09-09', 'SEP-OCT 2024', 'Exploratory US M&A talks (incl. Vestis): -21%, then +17% when terminated', 'down'),
 ('2025-03-06', 'MAR 2025', 'New capital-allocation policy + €150m buyback: +9% on the day', 'up'),
 ('2026-03-09', 'MAR 2026', 'Mid-East energy shock; €500m buyback (to Jul-26); Cintas-UniFirst deal', 'down'),
 ('2026-07-03', 'JUL 2026', 'All-time high €28.20 (3-Jul) as buyback completes', 'up'),
 ('2026-07-30', 'JUL-SEP 2026', 'H1-26: targets only confirmed, Mexico loss, FCF negative: -25% from high', 'down'),
]
def draw(path, figsize=(7.4, 3.5), title=True):
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(d, c, color=NAVY, linewidth=1.6, zorder=3)
    ax.fill_between(d, c, 0, color=NAVY, alpha=0.06, linewidth=0)
    for i, (ds, _, _, pos) in enumerate(EVENTS, 1):
        x0, y0 = nearest(dt.date.fromisoformat(ds))
        yl = y0 + 3.0 if pos == 'up' else y0 - 3.0
        ax.plot([x0, x0], [y0, yl], color=MUTED, linewidth=0.6, zorder=2)
        ax.scatter([x0], [yl], s=110, color='white', edgecolor=BLUE, linewidth=1.2, zorder=6)
        ax.text(x0, yl, str(i), ha='center', va='center', fontsize=6.6, color=INK, fontweight='bold', zorder=7)
    ax.annotate(f'€{c[-1]:.2f}', xy=(d[-1], c[-1]), xytext=(d[-1] + dt.timedelta(days=45), c[-1]), fontsize=7.2, color=INK, va='center')
    ax.set_ylim(0, 33); ax.set_ylabel('EUR per share (weekly close)')
    ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.set_xlim(dt.date(2019, 1, 1), dt.date(2026, 12, 31))
    if title: ax.set_title('Elis share price since 2019 with numbered catalysts (see list)')
    source_note(fig, 'Source: ProntoNLP getStockPrices (Elis, companyId 27989, weekly closes; series partly dividend-adjusted); event dates from Elis filings and transcripts via ProntoNLP.')
    fig.savefig(path); plt.close(fig)
draw(os.path.join(BASE, 'price_catalysts.png'))
draw(os.path.join(BASE, 'price_catalysts_memo.png'), figsize=(8.2, 4.1), title=False)
json.dump(EVENTS, open(os.path.join(BASE, 'price_catalysts_events.json'), 'w'), indent=1)
print('ok')
