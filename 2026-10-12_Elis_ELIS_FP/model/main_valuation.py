"""Elis historical multiples (year-end) and current valuation [calc]. Prices: ProntoNLP weekly closes (D); S&P line items (raw)."""
import csv, json, os
B = os.path.dirname(os.path.abspath(__file__))
W = list(csv.DictReader(open(os.path.join(B, 'D_elis_prices_weekly.csv'))))
def ye(y): return float([r for r in W if r['date'] <= f'{y}-12-31'][-1]['close'])
L = json.load(open(os.path.join(B, 'sp_source_links.json')))
def sp(item, p): return float(L[f'C_27989|{item}|{p}']['value']) / 1e6
H = {r['period']: r for r in json.load(open(os.path.join(B, 'main_history.json')))['annual_and_ltm']}
# Elis-reported adjusted EBITDA / headline EPS (worker F/A): FY2021-FY2025
ADJ = {2021: (1052.1, None), 2022: (1259.6, None), 2023: (1474.8, None), 2024: (1609.8, 1.76), 2025: (1700.1, 1.85)}
out = []
for y in range(2021, 2026):
    p = ye(y); sh = sp('Common Shares Outstanding', f'FY{y}') if f'C_27989|Common Shares Outstanding|FY{y}' in L else None
    mcap = p * sh; nd = sp('Net Debt', f'FY{y}'); ev = mcap + nd
    r = dict(year=y, price=p, shares=sh, mcap=mcap, net_debt_incl_leases=nd, ev=ev, ev_sales=ev / H[f'FY{y}']['revenue'],
             ev_ebitda_sp=ev / sp('EBITDA', f'FY{y}'), ev_adj_ebitda=ev / ADJ[y][0], ev_ebit=ev / H[f'FY{y}']['ebit_sp'],
             pe_ifrs=p / (sp('Net EPS - Diluted', f'FY{y}') * 1e6), pe_headline=(p / ADJ[y][1]) if ADJ[y][1] else None)
    out.append(r)
# current: 215.934m shares x 21.26; net debt 3,670.3 + leases 699.9; LTM adj EBITDA = 1700.1 + 853.8 - 813.8
cur_mcap = 215.934 * 21.26; ev = cur_mcap + 3670.3 + 699.9
ltm_adj = 1700.1 + 853.8 - 813.8
cur = dict(year='Current (9-Oct-26)', price=21.26, shares=215.934, mcap=cur_mcap, net_debt_incl_leases=3670.3 + 699.9, ev=ev, ev_sales=ev / 4910.8, ev_ebitda_sp=ev / 1525.7,
           ev_adj_ebitda=ev / ltm_adj, ev_ebit=ev / 639.4, pe_ifrs=21.26 / (0.68 + 1.464 - 0.611), pe_headline=21.26 / (1.85 + 0.89 - 0.85))
out.append(cur)
for r in out: print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()})
json.dump(out, open(os.path.join(B, 'main_valuation_history.json'), 'w'), indent=1)
