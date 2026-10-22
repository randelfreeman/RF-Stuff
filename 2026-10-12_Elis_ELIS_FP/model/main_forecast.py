"""Lead-analyst model, part 2: FY2026E-FY2028E EPS forecast (base / bull / bear), valuation and scenarios.
All outputs are analyst estimates [e] / calculations [calc]. Inputs (FY2025A, H1-2026A, guidance) are sourced in the report:
 FY2025A (Elis-reported): revenue 4,796.8; adj. EBITDA 1,701 (35.4%); adj. EBIT 766.6 (16.0%); headline NI 467.3; headline EPS basic 2.00 / diluted 1.85;
          FCF 358.6; net debt 3,020.2 (ex IFRS16); leverage 1.75x; DPS 0.48 (worker A, ProntoNLP T000003676656 / NONSEC000256665099)
 H1-2026A: revenue 2,457.1 (+3.2% organic); adj. EBITDA 853.8 (34.7%); adj. EBIT 370.0 (15.1%); headline NI 215.5; headline diluted EPS 0.89; FCF -30.1;
          net debt 3,670.3; leverage 2.09x; buyback EUR 466.8m @ EUR 26.25 (worker A, NONSEC000264324010)
 Shares (S&P C_27989): FY2025 shares outstanding 232.48m; weighted diluted 259.08m. OCEANE 2029: EUR380m, ratio 6,256.8564 sh per EUR100k bond -> 23.78m shares (worker D).
"""
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
PRICE = 21.26  # close 9-Oct-2026 (ProntoNLP, worker D)

FY25 = dict(rev=4796.8, ebitda=1701.0, ebit=766.6, hni=467.3, eps_dil=1.85, eps_basic=2.00, fcf=358.6, nd=3020.2, dps=0.48, dil_sh=259.08, basic_sh=467.3 / 2.00)
H1_26 = dict(rev=2457.1, ebitda=853.8, ebit=370.0, hni=215.5, eps_dil=0.89)
H1_25 = dict(rev=2343.1, ebit=370.0 / 1.046, hni=215.5 / 1.011)
H2_25 = dict(rev=FY25['rev'] - H1_25['rev'], ebit=FY25['ebit'] - H1_25['ebit'], hni=FY25['hni'] - H1_25['hni'])
OCEANE_SH = 380e6 / 100000 * 6256.8564 / 1e6   # 23.78m
BUYBACK26_SH = 466.8 / 26.25                      # 17.78m

SCEN = {
 'base': dict(h2_26_growth=0.037, h2_margin_delta=0.0000, g27=0.048, g28=0.050, m26=0.1600, m27=0.1620, m28=0.1640, ebitda_m=(0.3545, 0.3560, 0.3575), fin=(155, 150, 150), tax=0.27, bb27=100, bb28=100, oceane=True),
 'bull': dict(h2_26_growth=0.045, h2_margin_delta=0.0020, g27=0.060, g28=0.062, m26=0.1610, m27=0.1650, m28=0.1690, ebitda_m=(0.3555, 0.3590, 0.3625), fin=(152, 145, 140), tax=0.265, bb27=200, bb28=250, oceane=True),
 'bear': dict(h2_26_growth=0.025, h2_margin_delta=-0.0040, g27=0.025, g28=0.030, m26=0.1570, m27=0.1540, m28=0.1530, ebitda_m=(0.3520, 0.3480, 0.3470), fin=(158, 165, 170), tax=0.275, bb27=0, bb28=0, oceane=False),
}

def run(s):
    """FY2026E = H1-2026 actual + H2-2026E; FY2027E/28E annual."""
    tax = s['tax']
    # ---- FY2026E: H2 build
    h2_rev = H2_25['rev'] * (1 + s['h2_26_growth'])
    h2_margin = H2_25['ebit'] / H2_25['rev'] + s['h2_margin_delta']
    h2_ebit = h2_rev * h2_margin
    h2_fin = s['fin'][0] - 74.8            # H1-2026 implied headline financial expense ~EUR 74.8m [calc]
    h2_hni = (h2_ebit - h2_fin) * (1 - tax)
    h2_sh = 232.48 - BUYBACK26_SH + 1.0 + OCEANE_SH + 1.7          # diluted shares after buyback (OCEANE counted as dilutive) = 241.2m
    h2_eps = (h2_hni + (4.0 if s['oceane'] else 5.7)) / h2_sh
    rev26 = H1_26['rev'] + h2_rev; ebit26 = H1_26['ebit'] + h2_ebit; hni26 = H1_26['hni'] + h2_hni
    eps26 = H1_26['eps_dil'] + h2_eps
    sh26 = (hni26 + 9.0) / eps26
    revs = [rev26, rev26 * (1 + s['g27']), rev26 * (1 + s['g27']) * (1 + s['g28'])]
    ebits = [ebit26, revs[1] * s['m27'], revs[2] * s['m28']]
    price_bb = PRICE * 1.1
    base_sh = 232.48 - BUYBACK26_SH + 1.0 + OCEANE_SH + 1.7
    sh27 = base_sh - (s['bb27'] / price_bb) * 0.5
    sh28 = base_sh - (s['bb27'] / price_bb) - (s['bb28'] / price_bb) * 0.5
    addback_post = 0.0 if s['oceane'] else 362 * 0.043 * (1 - tax)
    rows = []
    for i, yr in enumerate(['FY2026E', 'FY2027E', 'FY2028E']):
        rev = revs[i]; ebitda = rev * s['ebitda_m'][i]; ebit = ebits[i]
        if i == 0:
            hni, sh, eps = hni26, sh26, eps26
        else:
            hni = (ebit - s['fin'][i]) * (1 - tax); sh = [None, sh27, sh28][i]; eps = (hni + addback_post) / sh
        rows.append(dict(year=yr, revenue=rev, rev_growth=rev / (FY25['rev'] if i == 0 else revs[i - 1]) - 1, adj_ebitda=ebitda, ebitda_margin=s['ebitda_m'][i],
                         adj_ebit=ebit, ebit_margin=ebit / rev, net_fin_exp=s['fin'][i], tax_rate=tax, headline_ni=hni, diluted_shares=sh, headline_eps_dil=eps,
                         h2_detail=(dict(h2_rev=h2_rev, h2_margin=h2_margin, h2_ebit=h2_ebit, h2_fin=h2_fin, h2_hni=h2_hni, h2_sh=h2_sh, h2_eps=h2_eps) if i == 0 else None)))
    for i, r in enumerate(rows):
        prev = FY25['eps_dil'] if i == 0 else rows[i - 1]['headline_eps_dil']
        r['eps_growth'] = r['headline_eps_dil'] / prev - 1
        r['pe_at_price'] = PRICE / r['headline_eps_dil']
    return rows

res = {k: run(v) for k, v in SCEN.items()}
json.dump({'price': PRICE, 'scenarios': SCEN, 'results': res, 'inputs': dict(FY25=FY25, H1_26=H1_26, H1_25=H1_25, H2_25=H2_25, OCEANE_SH=OCEANE_SH, BUYBACK26_SH=BUYBACK26_SH)}, open(os.path.join(BASE, 'main_forecast.json'), 'w'), indent=1)
for k, rows in res.items():
    print(k.upper())
    for r in rows:
        print(f"  {r['year']}: rev {r['revenue']:,.0f} ({r['rev_growth']*100:+.1f}%) EBITDA {r['adj_ebitda']:,.0f} ({r['ebitda_margin']*100:.1f}%) EBIT {r['adj_ebit']:,.0f} ({r['ebit_margin']*100:.1f}%) HNI {r['headline_ni']:,.0f} sh {r['diluted_shares']:.1f} EPS {r['headline_eps_dil']:.2f} ({r['eps_growth']*100:+.1f}%) P/E {r['pe_at_price']:.1f}x")
