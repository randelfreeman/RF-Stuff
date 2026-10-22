import csv, os, datetime as dt
import matplotlib.pyplot as plt, matplotlib.dates as mdates
from style import *
setup()
BASE = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(BASE, '..', 'model')
R = [r for r in csv.DictReader(open(os.path.join(M, 'A_sentiment_timeseries.csv'))) if r['documentType'] in ('Earnings Calls', 'Sales/Trading Statement Calls', 'Analyst/Investor Day') and r['sentimentScore']]
d = [dt.date.fromisoformat(r['date']) for r in R]; s = [float(r['sentimentScore']) for r in R]
typ = [r['documentType'] for r in R]
fig, ax = plt.subplots(figsize=(7.0, 2.9))
ax.plot(d, s, color=AXIS, linewidth=1.0, zorder=2)
for kind, col, lab in [('Earnings Calls', BLUE, 'Results call (FY / H1)'), ('Sales/Trading Statement Calls', ORANGE, 'Quarterly sales call'), ('Analyst/Investor Day', AQUA, 'Capital Markets Day')]:
    xs = [a for a, t in zip(d, typ) if t == kind]; ys = [b for b, t in zip(s, typ) if t == kind]
    ax.scatter(xs, ys, s=34, color=col, edgecolor='white', linewidth=1.2, zorder=4, label=lab)
for a, b, lab, dy in [(dt.date(2020, 10, 20), 0.03, 'H1-20: 0.03', 0.0), (dt.date(2026, 3, 11), 0.81, 'FY-25: 0.81', 0.08), (dt.date(2026, 7, 29), 0.52, 'H1-26: 0.52', -0.13), (dt.date(2024, 1, 30), 0.82, 'FY-23 sales: 0.82', 0.08)]:
    ax.annotate(lab, xy=(a, b), xytext=(a + dt.timedelta(days=(150 if lab.startswith('H1-20') else 0)), b + dy), fontsize=7, color=INK2, ha='center', va='center')
ax.set_ylim(-0.05, 1.12); ax.set_ylabel('ProntoNLP document sentiment (-1 to +1)')
ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.set_title('Earnings-call sentiment, 2020–2026')
ax.legend(loc='upper left', ncol=3, bbox_to_anchor=(0.0, 1.0))
source_note(fig, 'Source: ProntoNLP getDocuments document-level sentimentScore for Elis SA calls (companyId 27989); see provenance M-005 and A_earnings.')
fig.savefig(os.path.join(BASE, 'sentiment.png')); print('ok')
