"""
Tokyo Tatemono (8804) peer valuation + OLS regressions (v2: balance-sheet items sourced from the
Shikiho Online mirror on GitHub + company results via search extraction).
Money in JPY bn unless stated. Flags: S = sourced, D = derived, E = estimate.
"""
import numpy as np, pandas as pd, math, json

OUT_CSV = "/home/user/RF-Stuff/research_notes/Tokyo Tatemono 8804 equity research/peer_valuation_8804.csv"
SHK = "https://raw.githubusercontent.com/edamame384/stock_selection/HEAD/projects/shikiho_text_parser/data/raw/4Q-2/{}.txt"

R = []
def add(**k): R.append(k)
# ---- core developers / landlords ----
add(ticker="8804", name="Tokyo Tatemono", group="target", fy_end="Dec", ltfy="FY12/2025",
    price=3286.0, price_date="2026-09-25", mktcap=683.4, per_f=10.5, pbr=1.12, yld=3.83, roe=10.45, eqr=26.0,
    rev=474.586, oi=95.763, ni=58.879, rev_g1y=2.3, rev_3y_base=349.940, rev_f=524.0, oi_f=105.5, ni_f=65.0, fcst_flag="S company (Aug-26)",
    ibd=1536.6, ibd_date="2026-06-30", cash=94.2, cash_date="2026-06-30", nci=None,
    da=23.0, da_basis="FY12/25 (Shikiho fcst)", ocf=32.106, icf=None, capex=125.7, cf_basis="OCF FY12/25; capex FY12/24",
    pe_hi_avg=9.9, pe_lo_avg=7.0, pb_mar26=1.33, per_f_mar26=12.52, px_mar26=3795.0, treasury_pct=0.4)
add(ticker="8801", name="Mitsui Fudosan", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=1507.5, price_date="2026-09-07", mktcap=4060.0, per_f=14.3, pbr=1.25, yld=2.45, roe=8.68, eqr=32.4,
    rev=2709.747, oi=397.788, ni=278.684, rev_g1y=3.2, rev_3y_base=2269.103, rev_f=2800.0, oi_f=410.0, ni_f=285.0, fcst_flag="S company",
    ibd=4632.547, ibd_date="2026-03-31", cash=163.2, cash_date="2025-03-31", nci=None,
    da=140.0, da_basis="FY3/26 (Shikiho fcst)", ocf=599.252, icf=-321.9, capex=362.7, cf_basis="FY3/25",
    pe_hi_avg=18.3, pe_lo_avg=11.4, pb_mar26=1.56, per_f_mar26=18.58, px_mar26=1821.0, treasury_pct=None)
add(ticker="8802", name="Mitsubishi Estate", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=3630.0, price_date="2026-09-28", mktcap=4396.3, per_f=18.6, pbr=1.61, yld=1.35, roe=8.47, eqr=31.4,
    rev=1746.148, oi=329.730, ni=222.507, rev_g1y=10.5, rev_3y_base=1377.827, rev_f=2060.0, oi_f=370.0, ni_f=235.0, fcst_flag="OI/NI S company; revenue E (Toyo Keizai est.)",
    ibd=3469.290, ibd_date="2025-09-30", cash=256.8, cash_date="2025-03-31", nci=None,
    da=107.0, da_basis="FY3/26 (Shikiho fcst)", ocf=324.116, icf=-361.5, capex=443.8, cf_basis="FY3/25",
    pe_hi_avg=19.5, pe_lo_avg=12.5, pb_mar26=2.26, per_f_mar26=26.17, px_mar26=4729.0, treasury_pct=2.4)
add(ticker="8830", name="Sumitomo Realty & Development", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=3226.0, price_date="2026-09-14", mktcap=3019.5, per_f=13.4, pbr=1.16, yld=1.61, roe=9.16, eqr=34.4,
    rev=1057.765, oi=299.155, ni=212.535, rev_g1y=4.3, rev_3y_base=939.904, rev_f=1070.0, oi_f=320.0, ni_f=223.0, fcst_flag="S company",
    ibd=3839.626, ibd_date="2025-09-30", cash=98.2, cash_date="2025-03-31", nci=None,
    da=75.0, da_basis="FY3/26 (Shikiho fcst)", ocf=253.171, icf=-143.6, capex=170.2, cf_basis="FY3/25",
    pe_hi_avg=14.2, pe_lo_avg=8.4, pb_mar26=1.84, per_f_mar26=21.34, px_mar26=4790.0, treasury_pct=None)
add(ticker="3289", name="Tokyu Fudosan HD", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=1312.5, price_date="2026-08-07", mktcap=944.8, per_f=9.4, pbr=1.03, yld=3.81, roe=11.24, eqr=26.3,
    rev=1246.048, oi=166.882, ni=96.697, rev_g1y=8.3, rev_3y_base=1005.836, rev_f=1400.0, oi_f=190.0, ni_f=100.0, fcst_flag="S company",
    ibd=1826.9, ibd_date="2026-03-31", cash=157.4, cash_date="2025-03-31", nci=None,
    da=67.2, da_basis="FY3/26 (Shikiho fcst)", ocf=47.426, icf=-139.9, capex=90.6, cf_basis="FY3/25",
    pe_hi_avg=12.3, pe_lo_avg=7.6, pb_mar26=1.15, per_f_mar26=10.99, px_mar26=1374.5, treasury_pct=None)
add(ticker="3231", name="Nomura Real Estate HD", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=926.0, price_date="2026-09-04", mktcap=850.0, per_f=9.2, pbr=0.99, yld=4.75, roe=10.68, eqr=28.5,
    rev=942.505, oi=138.242, ni=82.880, rev_g1y=24.4, rev_3y_base=654.735, rev_f=1080.0, oi_f=140.0, ni_f=86.0, fcst_flag="S company",
    ibd=1696.5, ibd_date="2026-06-30", cash=35.8, cash_date="2025-03-31", nci=None,
    da=20.8, da_basis="FY3/25 (Shikiho actual)", ocf=-133.793, icf=-203.3, capex=174.4, cf_basis="FY3/25",
    pe_hi_avg=10.6, pe_lo_avg=7.4, pb_mar26=1.21, per_f_mar26=12.97, px_mar26=1060.0, treasury_pct=4.8)
add(ticker="3003", name="Hulic", group="core", fy_end="Dec", ltfy="FY12/2025",
    price=1734.0, price_date="2026-09-25", mktcap=1331.6, per_f=10.9, pbr=1.39, yld=3.86, roe=13.09, eqr=26.0,
    rev=727.447, oi=186.826, ni=114.334, rev_g1y=22.9, rev_3y_base=523.424, rev_f=751.0, oi_f=210.0, ni_f=121.0, fcst_flag="OI/NI S company; revenue E (Toyo Keizai est.)",
    ibd=2210.758, ibd_date="2025-09-30", cash=134.3, cash_date="2024-12-31", nci=None,
    da=17.8, da_basis="FY12/24 (Shikiho actual)", ocf=269.239, icf=-602.0, capex=417.1, cf_basis="OCF FY12/25; ICF/capex FY12/24",
    pe_hi_avg=12.0, pe_lo_avg=9.0, pb_mar26=1.57, per_f_mar26=12.04, px_mar26=1899.0, treasury_pct=None)
add(ticker="8803", name="Heiwa Real Estate", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=2320.0, price_date="2026-09-30", mktcap=164.8, per_f=13.3, pbr=1.24, yld=4.44, roe=9.01, eqr=28.1,
    rev=50.855, oi=15.109, ni=11.032, rev_g1y=20.9, rev_3y_base=44.522, rev_f=63.8, oi_f=15.8, ni_f=11.5, fcst_flag="S company",
    ibd=261.338, ibd_date="2026-03-31 (assumed)", cash=25.2, cash_date="2025-03-31", nci=None,
    da=5.6, da_basis="FY3/25 (Shikiho actual)", ocf=16.048, icf=-24.8, capex=24.5, cf_basis="FY3/25",
    pe_hi_avg=17.4, pe_lo_avg=13.7, pb_mar26=1.30, per_f_mar26=16.86, px_mar26=2446.0, treasury_pct=13.6)
add(ticker="8818", name="Keihanshin Building", group="core", fy_end="Mar", ltfy="FY3/2026",
    price=1118.0, price_date="2026-09-11", mktcap=109.1, per_f=15.2, pbr=1.26, yld=2.68, roe=5.93, eqr=43.8,
    rev=20.255, oi=5.646, ni=4.675, rev_g1y=3.4, rev_3y_base=18.879, rev_f=20.1, oi_f=5.53, ni_f=4.22, fcst_flag="E (Toyo Keizai est.)",
    ibd=77.697, ibd_date="2025-09-30", cash=14.0, cash_date="2025-03-31", nci=None,
    da=3.891, da_basis="FY3/25 (Shikiho actual)", ocf=7.294, icf=-8.2, capex=9.75, cf_basis="FY3/25",
    pe_hi_avg=20.3, pe_lo_avg=14.4, pb_mar26=1.16, per_f_mar26=22.63, px_mar26=1947.0, treasury_pct=None)
# ---- housing comps ----
add(ticker="1928", name="Sekisui House", group="housing", fy_end="Jan", ltfy="FY1/2026",
    price=3415.0, price_date="2026-08-06", mktcap=2225.2, per_f=10.2, pbr=1.03, yld=4.25, roe=11.32, eqr=42.7,
    rev=4197.922, oi=341.402, ni=232.095, rev_g1y=3.4, rev_3y_base=2928.835, rev_f=4353.0, oi_f=350.0, ni_f=218.0, fcst_flag="S company (Mar-26)",
    ibd=1944.539, ibd_date="2025-10-31", cash=390.3, cash_date="2025-01-31", nci=None,
    da=35.2, da_basis="FY1/25 (Shikiho actual)", ocf=62.885, icf=-697.6, capex=99.8, cf_basis="FY1/25 (MDC acquisition year)",
    pe_hi_avg=11.0, pe_lo_avg=8.0, pb_mar26=1.07, per_f_mar26=10.58, px_mar26=3544.0, treasury_pct=2.2)
add(ticker="1878", name="Daito Trust Construction", group="housing", fy_end="Mar", ltfy="FY3/2026 (company fcst proxy)",
    price=3143.0, price_date="2026-09-29", mktcap=1083.1, per_f=9.5, pbr=2.06, yld=5.19, roe=20.45, eqr=36.5,
    rev=1980.0, oi=135.0, ni=95.0, rev_g1y=7.5, rev_3y_base=1657.626, rev_f=None, oi_f=None, ni_f=None, fcst_flag="LTFY = company fcst (Jan-26), E",
    ibd=233.101, ibd_date="2025-09-30", cash=223.5, cash_date="2025-03-31", nci=None,
    da=17.3, da_basis="FY3/25 (Shikiho actual)", ocf=85.612, icf=-46.5, capex=27.0, cf_basis="FY3/25",
    pe_hi_avg=14.9, pe_lo_avg=10.7, pb_mar26=2.43, per_f_mar26=13.14, px_mar26=3625.0, treasury_pct=3.2)
add(ticker="3288", name="Open House Group", group="housing", fy_end="Sep", ltfy="FY9/2025",
    price=7362.0, price_date="2026-09-29", mktcap=859.7, per_f=6.9, pbr=1.38, yld=2.78, roe=20.10, eqr=38.1,
    rev=1336.468, oi=145.933, ni=100.670, rev_g1y=3.1, rev_3y_base=952.686, rev_f=1485.0, oi_f=174.5, ni_f=115.5, fcst_flag="S company (Feb-26)",
    ibd=720.061, ibd_date="2025-09-30", cash=407.6, cash_date="2025-09-30", nci=None,
    da=2.053, da_basis="FY9/25 (Shikiho actual)", ocf=29.530, icf=-11.1, capex=None, cf_basis="FY9/25",
    pe_hi_avg=8.4, pe_lo_avg=5.6, pb_mar26=2.02, per_f_mar26=10.15, px_mar26=10050.0, treasury_pct=4.5)

df = pd.DataFrame(R).set_index("ticker")
TT_TA_JUN26 = 1857.2 + 619.0; TT_EQ_JUN26 = 0.245 * TT_TA_JUN26; TT_NCI = 619.0 - TT_EQ_JUN26
df["nci"] = 0.0; df.loc["8804", "nci"] = TT_NCI
df["shares_m"] = df.mktcap / df.price * 1000
df["book_equity"] = df.mktcap / df.pbr
df["bps"] = df.price / df.pbr
df["net_debt"] = df.ibd - df.cash
df["ev"] = df.mktcap + df.net_debt + df.nci
df["ebitda"] = df.oi + df.da
df["ebit_margin"] = df.oi / df.rev * 100
df["ebitda_margin"] = df.ebitda / df.rev * 100
df["ebit_margin_f"] = df.oi_f / df.rev_f * 100
df["ev_sales"] = df.ev / df.rev; df["ev_sales_f"] = df.ev / df.rev_f
df["ev_ebitda"] = df.ev / df.ebitda
df["ev_ebit"] = df.ev / df.oi; df["ev_ebit_f"] = df.ev / df.oi_f
df["pe_actual"] = df.mktcap / df.ni
df["nd_ebitda"] = df.net_debt / df.ebitda
df["nd_equity"] = df.net_debt / df.book_equity
df["rev_cagr_3y"] = ((df.rev / df.rev_3y_base) ** (1 / 3) - 1) * 100
df["rev_g_fcst"] = (df.rev_f / df.rev - 1) * 100
df["ni_g_fcst"] = (df.ni_f / df.ni - 1) * 100
df["fcf"] = df.ocf + df.icf
df["ocf_to_ev"] = df.ocf / df.ev * 100
df["fcf_yield_mktcap"] = df.fcf / df.mktcap * 100
df["pe_mid_hist"] = (df.pe_hi_avg + df.pe_lo_avg) / 2
df["split_factor_since_mar26"] = 1.0
df.loc["8818", "split_factor_since_mar26"] = 2.0   # D: shares 48.8m (Mar-26) -> 97.6m (Sep-26) => 2-for-1 split
df["px_chg_mar_sep"] = (df.price * df.split_factor_since_mar26 / df.px_mar26 - 1) * 100

def ols(x, y, x0=None):
    x = np.asarray(x, float); y = np.asarray(y, float); n = len(x)
    X = np.column_stack([np.ones(n), x]); beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta; sse = float(res @ res); sst = float(((y - y.mean()) ** 2).sum()); dof = n - 2
    s2 = sse / dof; cov = s2 * np.linalg.inv(X.T @ X); se = np.sqrt(np.diag(cov)); t = beta / se
    tc = {2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201}[dof]
    xs = np.linspace(abs(t[1]), abs(t[1]) + 200, 200001)
    pdf = math.gamma((dof + 1) / 2) / (math.sqrt(dof * math.pi) * math.gamma(dof / 2)) * (1 + xs ** 2 / dof) ** (-(dof + 1) / 2)
    o = dict(n=n, intercept=beta[0], slope=beta[1], se_int=se[0], se_slope=se[1], t_int=t[0], t_slope=t[1],
             p_slope=2 * float(np.trapezoid(pdf, xs)), r2=1 - sse / sst, adj_r2=1 - (1 - (1 - sse / sst)) * 0 - (sse / sst) * (n - 1) / dof + 0,
             resid_se=math.sqrt(s2), tcrit=tc)
    o["adj_r2"] = 1 - (sse / sst) * (n - 1) / dof
    if x0 is not None:
        v = np.array([1.0, x0]); fit = float(v @ beta); sm = math.sqrt(float(v @ cov @ v)); sp = math.sqrt(s2 + sm ** 2)
        o.update(x0=x0, fitted=fit, ci_lo=fit - tc * sm, ci_hi=fit + tc * sm, pi_lo=fit - tc * sp, pi_hi=fit + tc * sp)
    return o

TT = df.loc["8804"]; SH = TT.shares_m
ND_JUN = TT.net_debt; ND_DEC = 1343.874 - 152.3      # Dec-25 IBD per coordinator gap-fill (edinetdb), cash back-solved
REV_LTM = 474.586 - 208.793 + 194.415; OI_LTM = 95.763 - 34.033 + 39.852; NI_LTM = 58.879 - 20.549 + 23.364
def px_from_ev(mult, base, nd=None):
    nd = ND_JUN if nd is None else nd
    ev = mult * base; eq = ev - nd - TT.nci; return ev, eq, eq / SH * 1000

core = df[df.group == "core"]; ext = df[df.group != "target"]
res = {}
r1 = ols(core.ebit_margin, core.ev_sales, TT.ebit_margin); e = px_from_ev(r1["fitted"], TT.rev)
r1.update(tt_actual=TT.ev_sales, impl_ev=e[0], impl_eq=e[1], impl_px=e[2],
          px_ci_lo=px_from_ev(r1["ci_lo"], TT.rev)[2], px_ci_hi=px_from_ev(r1["ci_hi"], TT.rev)[2],
          px_pi_lo=px_from_ev(r1["pi_lo"], TT.rev)[2], px_pi_hi=px_from_ev(r1["pi_hi"], TT.rev)[2])
res["R1 EV/Sales~EBITmargin core8 LTFY"] = r1
m_ltm = OI_LTM / REV_LTM * 100; f = r1["intercept"] + r1["slope"] * m_ltm
res["R1a TT LTM basis"] = dict(rev_ltm=REV_LTM, oi_ltm=OI_LTM, margin=m_ltm, actual=TT.ev / REV_LTM, fitted=f, impl_px=px_from_ev(f, REV_LTM)[2])
ev_dec = TT.mktcap + ND_DEC + TT.nci
res["R1b TT Dec-25 BS"] = dict(tt_ev=ev_dec, actual=ev_dec / TT.rev, fitted=r1["fitted"], impl_px=px_from_ev(r1["fitted"], TT.rev, ND_DEC)[2])
for lab, sub in [("R1c ex-Keihanshin", core.drop(index="8818")), ("R1d big-6 (ex Heiwa,Keihanshin)", core.drop(index=["8818", "8803"])),
                 ("R1e extended 11 (incl housing)", ext)]:
    o = ols(sub.ebit_margin, sub.ev_sales, TT.ebit_margin); o.update(impl_px=px_from_ev(o["fitted"], TT.rev)[2], tt_actual=TT.ev_sales)
    res[lab] = o
fw = core.dropna(subset=["rev_f", "oi_f"])
o = ols(fw.ebit_margin_f, fw.ev_sales_f, TT.ebit_margin_f); o.update(impl_px=px_from_ev(o["fitted"], TT.rev_f)[2], tt_actual=TT.ev_sales_f)
res["R1f forward EV/Sales~fwd margin core8"] = o
o = ols(core.roe, core.ev_ebitda, TT.roe); o.update(tt_actual=TT.ev_ebitda, impl_px=px_from_ev(o["fitted"], TT.ebitda)[2]); res["R4 EV/EBITDA~ROE core8"] = o
r2 = ols(ext.roe, ext.pbr, TT.roe); r2.update(tt_actual=TT.pbr, impl_px=r2["fitted"] * TT.bps, px_pi_lo=r2["pi_lo"] * TT.bps, px_pi_hi=r2["pi_hi"] * TT.bps)
res["R2 P/B~ROE all11"] = r2
o = ols(core.roe, core.pbr, TT.roe); o.update(tt_actual=TT.pbr, impl_px=o["fitted"] * TT.bps); res["R2b P/B~ROE core8"] = o

# Monte Carlo: NCI unknown (0-5% of mkt cap; Mitsubishi Estate 0-12%), stale IBD (Sep-25 values x U(1.00,1.08)), stale cash x U(0.7,1.3)
rng = np.random.default_rng(8804); N = 20000; pxs = []; r2s = []; slopes = []
stale_ibd = [t for t in core.index if str(core.loc[t, "ibd_date"]).startswith("2025")]
for _ in range(N):
    d = core.copy()
    nci = pd.Series(rng.uniform(0, 0.05, len(d)), index=d.index) * d.mktcap
    nci.loc["8802"] = rng.uniform(0, 0.12) * d.loc["8802", "mktcap"]
    ibd = d.ibd.copy()
    for t in stale_ibd: ibd.loc[t] = ibd.loc[t] * rng.uniform(1.00, 1.08)
    cash = d.cash * rng.uniform(0.7, 1.3, len(d))
    y = (d.mktcap + ibd - cash + nci) / d.rev
    o = ols(d.ebit_margin, y, TT.ebit_margin); pxs.append(px_from_ev(o["fitted"], TT.rev)[2]); r2s.append(o["r2"]); slopes.append(o["slope"])
pxs = np.array(pxs)
res["MC R1"] = dict(N=N, p5=np.percentile(pxs, 5), p50=np.percentile(pxs, 50), p95=np.percentile(pxs, 95),
                    slope_p5=np.percentile(slopes, 5), slope_p95=np.percentile(slopes, 95), r2_p5=np.percentile(r2s, 5), r2_p95=np.percentile(r2s, 95))

# peer stats
cols_stats = ["per_f", "pe_actual", "pbr", "yld", "roe", "ev_sales", "ev_ebitda", "ev_ebit", "ev_ebit_f", "ebit_margin", "ebitda_margin",
              "nd_ebitda", "nd_equity", "rev_cagr_3y", "pe_hi_avg", "pe_lo_avg", "pe_mid_hist", "pb_mar26", "per_f_mar26", "px_chg_mar_sep", "ocf_to_ev"]
stats = {}
for c in cols_stats:
    v = core[c].dropna(); stats[c] = dict(tt=float(TT[c]), med=v.median(), mean=v.mean(), n=len(v), prem_med=(TT[c] / v.median() - 1) * 100)
big5 = df.loc[["8801", "8802", "8830", "3289", "3231"]]
for c in ["per_f", "pbr", "yld", "ev_sales", "ev_ebitda", "ev_ebit", "pe_mid_hist"]:
    stats[c + "_big5"] = dict(med=big5[c].median(), prem_med=(TT[c] / big5[c].median() - 1) * 100)

eps_f = TT.ni_f / SH * 1000; eps_a = TT.ni / SH * 1000
impl = dict(eps_f=eps_f, eps_a=eps_a, bps=TT.bps,
            px_med_fPE=stats["per_f"]["med"] * eps_f, px_med_PB=stats["pbr"]["med"] * TT.bps,
            px_med_EVEBITDA=px_from_ev(stats["ev_ebitda"]["med"], TT.ebitda)[2], px_med_EVEBIT=px_from_ev(stats["ev_ebit"]["med"], TT.oi)[2],
            px_med_EVSales=px_from_ev(stats["ev_sales"]["med"], TT.rev)[2],
            px_hist_mid_PE_on_fwd=TT.pe_mid_hist * eps_f, px_hist_hi_PE_on_fwd=TT.pe_hi_avg * eps_f, px_hist_lo_PE_on_fwd=TT.pe_lo_avg * eps_f)

# Takeover scenarios incl NAV (FY25 unrealised gain 599.9bn, 30.6% tax -> 2,007/sh; NAV 1H26 = BPS 2,930 + 2,007 = 4,937)
NAV_PS = 2930 + 2007
EBITDA_F = TT.oi_f + 24.0   # E: FY26 D&A assumed 24.0bn (FY24 22.3, FY25 fcst 23.0)
tk = []
for prem in [0, 20, 30, 40, 50, 60]:
    p = TT.price * (1 + prem / 100); eq = p * SH / 1000; ev = eq + ND_JUN + TT.nci
    tk.append(dict(prem=prem, price=p, equity=eq, ev=ev, pb=p / TT.bps, p_nav=p / NAV_PS, pe_f=p / eps_f, pe_a=p / eps_a,
                   ev_ebitda_f=ev / EBITDA_F, ev_ebitda_a=ev / TT.ebitda, ev_ebit_f=ev / TT.oi_f, ev_sales_f=ev / TT.rev_f))
tk = pd.DataFrame(tk)

# TT history (year-end close from sibling CSV / Nikkei; EPS/DPS/BPS Shikiho/Tanshin)
hist = pd.DataFrame([
    dict(fy=2021, px=1680, eps=34965 / 208.8, dps=None, bps=None),
    dict(fy=2022, px=1599, eps=206.2, dps=65, bps=None),
    dict(fy=2023, px=2112, eps=215.8, dps=73, bps=494000 / 208.92),   # BPS estimate (equity ~494bn E)
    dict(fy=2024, px=2607, eps=315.5, dps=95, bps=2568.0),
    dict(fy=2025, px=3546, eps=283.08, dps=105, bps=2846.85),
]).set_index("fy")
hist["pe"] = hist.px / hist.eps; hist["pb"] = hist.px / hist.bps; hist["yld"] = hist.dps / hist.px * 100

pd.set_option("display.width", 260); pd.set_option("display.max_columns", 80)
show = ["name", "price", "price_date", "mktcap", "ibd", "ibd_date", "cash", "cash_date", "net_debt", "ev", "rev", "oi", "da", "ebitda", "ni",
        "ev_sales", "ev_sales_f", "ev_ebitda", "ev_ebit", "ev_ebit_f", "pe_actual", "per_f", "pbr", "yld", "roe", "ebit_margin", "ebitda_margin",
        "ebit_margin_f", "nd_ebitda", "nd_equity", "rev_g1y", "rev_cagr_3y", "rev_g_fcst", "ni_g_fcst", "ocf", "fcf", "ocf_to_ev", "fcf_yield_mktcap"]
print(df[show].round(2).to_string())
print("\nTT: NCI %.1f; ND Jun %.1f; ND Dec %.1f; shares %.2fm; BPS %.0f; EBITDA FY25 %.1f; EPS f %.1f a %.1f" % (TT.nci, ND_JUN, ND_DEC, SH, TT.bps, TT.ebitda, eps_f, eps_a))
for k, v in res.items():
    print("\n==", k); print({a: (round(float(b), 4) if isinstance(b, (float, np.floating, int)) else b) for a, b in v.items()})
print("\nSTATS core-8 (tt, median, mean, n, prem vs median %):")
for k, v in stats.items(): print(" ", k, {a: round(float(b), 3) for a, b in v.items()})
print("\nIMPLIED:", {k: round(float(v), 1) for k, v in impl.items()})
print("\nTAKEOVER:\n", tk.round(2).to_string())
print("\nTT HISTORY:\n", hist.round(2).to_string())
print("\nMar-26 vs Sep-26 price change (%):", df.px_chg_mar_sep.round(1).to_dict())

out = df.copy()
out["shikiho_mirror_url"] = [SHK.format(t) for t in out.index]
out["flags"] = ("JPY bn. IBD/cash per ibd_date/cash_date (Shikiho mirror Sep-25 BS & FY-end cash, or company results for later dates); "
                "NCI: TT derived (net assets 619.0 - 24.5% x TA), peers 0 = ESTIMATE; EBITDA = OI + D&A (da_basis); hybrids counted 100% as debt; "
                "Daito LTFY = company FY3/26 forecast (proxy); rev_f for 8802/3003/8818 = Toyo Keizai estimates (E)")
out["in_R1_core8"] = out.group.eq("core"); out["in_R1e_ext11"] = out.group.isin(["core", "housing"])
out.round(4).to_csv(OUT_CSV, encoding="utf-8")
json.dump({k: {a: (float(b) if isinstance(b, (float, np.floating, int)) else b) for a, b in v.items()} for k, v in res.items()},
          open("/tmp/claude-0/-home-user-RF-Stuff/9f04a836-a396-50f9-b4c0-c80298604801/scratchpad/results_v2.json", "w"), indent=1)
print("\nCSV:", OUT_CSV)
