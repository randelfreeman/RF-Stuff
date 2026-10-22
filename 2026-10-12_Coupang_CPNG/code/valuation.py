"""Scenario valuation at Oct-2027 (12-month view). Per share = (multiple x NTM sales - net debt incl. leases) / FY28E diluted shares.
NTM sales at Oct-2027 = 0.25 x FY27E + 0.75 x FY28E revenue. Inputs: raw/model.json (our estimates [e])."""
import json
m = json.load(open("raw/model.json")); S = m["scen"]
spec = {"bear": (0.45, 1200, 0.25), "base": (0.85, 300, 0.50), "bull": (1.20, -500, 0.25)}  # multiple, net debt US$m, probability
price = 15.82; out = {}; pw = 0.0
for k, (mult, nd, p) in spec.items():
    f27, f28 = S[k]["F27"], S[k]["F28"]
    ntm = 0.25 * f27["rev"] + 0.75 * f28["rev"]
    ev = mult * ntm; eq = ev - nd; ps = eq / f28["sh"]
    out[k] = dict(ntm_sales=ntm, multiple=mult, ev=ev, net_debt=nd, equity=eq, shares=f28["sh"], per_share=ps,
                  upside=ps / price - 1, ev_fy28_ebitda=ev / f28["adj_ebitda"], prob=p)
    pw += p * ps
out["prob_weighted"] = dict(per_share=pw, upside=pw / price - 1)
json.dump(out, open("raw/valuation.json", "w"), indent=1)
for k, v in out.items():
    print(k, {a: round(b, 3) if isinstance(b, float) else b for a, b in v.items()})
