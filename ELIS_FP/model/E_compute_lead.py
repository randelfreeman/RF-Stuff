"""Peer multiples (lead-analyst recomputation from worker E's raw S&P + ProntoNLP files). [calc]
Market cap: ProntoNLP marketCap (USD) and originalCap (trading currency) from getCompanies (E-043);
financials: S&P LTM line items (E-009..041) in reporting currency. Where reporting currency != USD, financials
are converted to USD with the FX implied by marketCap/originalCap when the trading currency equals the reporting
currency (EUR, DKK); GBP reporters quoted in pence are scaled by 100. Elis uses its own share count/price."""
import json, os, csv
R = os.path.join(os.path.dirname(__file__), '..', 'provenance', 'raw', 'E_peers_valuation')
def li(fn):
    d = json.load(open(os.path.join(R, fn))); out = {}
    for cid, v in d['results'].items():
        per = v['data']['periods']
        if not per: continue
        k = sorted(per.keys(), key=lambda p: per[p]['period_end_date'])[-1]
        x = per[k]['line_item']; src = (x.get('sources') or [{}])[0].get('url')
        out[cid] = dict(v=float(x['value']) / 1e6, end=per[k]['period_end_date'], name=v.get('company_name'), tk=v.get('ticker'), cur=v.get('currency') or v['data'].get('currency'), src=src)
    return out
rev = li('009_sp_line_item_revenue_ltm.json'); ebitda = li('026_sp_line_item_ebitda_ltm.json'); ebit = li('027_sp_line_item_ebit_ltm.json')
ni = li('028_sp_line_item_net_income_ltm.json'); nd = li('031_sp_line_item_net_debt_ltm.json'); te = li('038_sp_line_item_total_equity_ltm.json'); tce = li('039_sp_line_item_total_common_equity_ltm.json')
cfo = li('036_sp_line_item_cash_from_operations_ltm.json'); capex = li('037_sp_line_item_capital_expenditure_ltm.json')
reva = json.load(open(os.path.join(R, '008_sp_line_item_revenue_annual.json')))
comp = json.load(open(os.path.join(R, '043_pronto_getCompanies_13ids.json')))['results']
mc = {c['ticker']: c for c in comp}
TICK = {'C_27989': 'ELIS', 'C_260725': 'CTAS', 'C_309966': 'UNF', 'C_694763': 'VSTS', 'C_411004': 'RTO', 'C_876284': 'JSG', 'C_1004106': 'ARMK', 'C_808038': 'SW', 'C_26972979': 'ISS', 'C_692472': 'CPG', 'C_250079': 'ABM', 'C_268799': 'ECL', 'C_410348': 'BNZL'}
GROUP = {'CTAS': 'Direct (uniform/linen rental)', 'UNF': 'Direct (uniform/linen rental)', 'VSTS': 'Direct (uniform/linen rental)', 'JSG': 'Direct (uniform/linen rental)', 'RTO': 'Direct (hygiene services)'}
rows = []
for cid, t in TICK.items():
    if cid not in rev: continue
    cur = rev[cid]['cur']
    if t == 'ELIS':
        mcap_rep = 215.934 * 21.26   # shares outstanding 30-Jun-2026 (215.93m, worker B) x close 9-Oct-2026
        fx = None
    else:
        c = mc.get(t)
        if not c: continue
        usd, orig = c['marketCap'], c['originalCap']
        if cur == 'USD': mcap_rep = usd / 1e6
        else:
            ratio = orig / usd  # local per USD
            # GBP: originalCap may be in GBP; sanity: GBP per USD ~0.7-0.85; if ~70-85 -> pence
            if cur == 'GBP' and ratio > 10: orig = orig / 100
            mcap_rep = orig / 1e6
    def g(d): return d.get(cid, {}).get('v')
    mi = (g(te) or 0) - (g(tce) or 0)
    ev = mcap_rep + (g(nd) or 0) + max(mi, 0)
    r = dict(ticker=t, name=rev[cid]['name'], group=GROUP.get(t, 'Elis' if t == 'ELIS' else 'Broader business services'), currency=cur, ltm_end=rev[cid]['end'],
             mcap=mcap_rep, net_debt=g(nd), minorities=mi, ev=ev, revenue=g(rev), ebitda=g(ebitda), ebit=g(ebit), net_income=g(ni), fcf=(g(cfo) or 0) + (g(capex) or 0))
    r.update(ev_sales=ev / r['revenue'], ev_ebitda=ev / r['ebitda'] if r['ebitda'] else None, ev_ebit=ev / r['ebit'] if r['ebit'] else None,
             pe=mcap_rep / r['net_income'] if r['net_income'] and r['net_income'] > 0 else None, nd_ebitda=(g(nd) or 0) / r['ebitda'] if r['ebitda'] else None,
             ebitda_m=r['ebitda'] / r['revenue'], ebit_m=r['ebit'] / r['revenue'], fcf_yield=r['fcf'] / mcap_rep, capex_sales=-(g(capex) or 0) / r['revenue'])
    pa = reva['results'].get(cid, {}).get('data', {}).get('periods', {})
    ks = sorted(pa.keys(), key=lambda p: pa[p]['period_end_date'])
    if len(ks) >= 4:
        v = [float(pa[k]['line_item']['value']) for k in ks]
        r['growth_1y'] = v[-1] / v[-2] - 1; r['cagr_3y'] = (v[-1] / v[-4]) ** (1 / 3) - 1
    r['src_rev'] = rev[cid]['src']; r['src_ebitda'] = ebitda.get(cid, {}).get('src'); r['src_nd'] = nd.get(cid, {}).get('src')
    rows.append(r)
import statistics as st
for r in rows: print(f"{r['ticker']:5s} {r['currency']} mcap {r['mcap']:>10,.0f} EV/S {r['ev_sales']:.2f} EV/EBITDA {r['ev_ebitda'] or 0:.1f} EV/EBIT {r['ev_ebit'] or 0:.1f} PE {r['pe'] or 0:.1f} ND/EBITDA {r['nd_ebitda'] or 0:.2f} EBITm {r['ebit_m']*100:.1f} g1 {r.get('growth_1y',0)*100:.1f}")
# regression EV/Sales vs EBIT margin (exclude Elis)
import numpy as np
P = [r for r in rows if r['ticker'] != 'ELIS' and r['ebit_m'] > 0]
x = np.array([r['ebit_m'] * 100 for r in P]); y = np.array([r['ev_sales'] for r in P])
b, a = np.polyfit(x, y, 1); yhat = a + b * x; r2 = 1 - ((y - yhat) ** 2).sum() / ((y - y.mean()) ** 2).sum()
E = [r for r in rows if r['ticker'] == 'ELIS'][0]
impl = a + b * E['ebit_m'] * 100
print('OLS EV/S = %.3f + %.4f*EBITm  R2 %.2f n %d; Elis actual %.2f implied %.2f' % (a, b, r2, len(P), E['ev_sales'], impl))
json.dump(dict(rows=rows, regression=dict(intercept=a, slope=b, r2=r2, n=len(P), elis_actual=E['ev_sales'], elis_implied=impl)), open(os.path.join(os.path.dirname(__file__), 'E_peer_multiples_lead.json'), 'w'), indent=1)
