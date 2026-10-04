# Tokyo Tatemono (8804) - derived figures and EPS model. All JPY bn unless noted.
# Verified inputs (from search-result data, see notes)
FY25 = dict(rev=474.586, op=95.763, ordi=78.187, ni=58.879, bldg_op=67.05, res_op=25.56, dps=105, payout=0.371)
FY26G0 = dict(rev=524.0, op=100.0, ordi=80.5, ni=63.0, dps=122, payout=0.402)   # Feb-2026 guidance
FY26G1 = dict(op=105.5, ordi=83.5, ni=65.0, dps=126)                              # Aug-2026 revised guidance
H1_25 = dict(rev=208.793, op=34.033, ordi=27.912, ni=20.549)
H1_26 = dict(rev=194.4, op=39.8, bp=41.3, ni=23.364, bldg_op=40.1, res_op=2.9)
Q1_25 = dict(rev=126.665, op=23.706, ordi=20.592, ni=14.347)
Q1_26 = dict(rev=98.619, op=12.645, ordi=9.249, ni=5.717)
M9_25 = dict(rev=298.8, ordi=41.453, ni=29.5)

print("== Derived prior-year (FY2024) from FY2025 YoY % ==")
print("FY24 rev  %.1f" % (FY25['rev']/1.023))
print("FY24 OP   %.1f" % (FY25['op']/1.202))
print("FY24 NI   %.1f" % (FY25['ni']/(1-0.106)))
print("FY24 bldg OP %.1f, res OP %.1f" % (FY25['bldg_op']/1.62, FY25['res_op']/0.67))
print("== Derived 1H FY2024 from 1H FY2025 YoY ==")
for k,p in [('rev',-0.248),('op',-0.336),('ordi',-0.420),('ni',-0.352)]:
    print("1H24 %s %.1f" % (k, H1_25[k]/(1+p)))
print("== FY2025 EPS/shares (derived) ==")
eps25 = FY25['dps']/FY25['payout']; sh25 = FY25['ni']/eps25*1000
print("EPS25 %.1f yen, avg shares %.2f m" % (eps25, sh25))
eps26g = FY26G0['dps']/FY26G0['payout']; sh26 = FY26G0['ni']/eps26g*1000
print("FY26 orig guidance EPS %.1f yen, implied shares %.2f m" % (eps26g, sh26))
print("FY26 revised guidance EPS %.1f yen (at %.2f m sh); payout at DPS126 %.1f%%" % (FY26G1['ni']/sh26*1000, sh26, 126/(FY26G1['ni']/sh26*1000)*100))
print("FY26 consensus NI 66.477 -> EPS %.1f" % (66.477/sh26*1000))
print("== 1H FY2026 vs prior year & guidance ==")
print("1H25 bldg OP %.2f, res OP %.2f (derived)" % (H1_26['bldg_op']/2.227, H1_26['res_op']/(1-0.832)))
print("1H26 BP prior-year %.2f" % (H1_26['bp']/1.2))
for k in ['op','ni']:
    print("progress %s: vs orig %.1f%%, vs revised %.1f%%; FY25 1H share %.1f%%" % (k, H1_26[k]/FY26G0[k]*100, H1_26[k]/FY26G1[k]*100, H1_25[k]/FY25[k]*100))
print("1H26 rev progress vs 524: %.1f%%; FY25 1H rev share %.1f%%" % (H1_26['rev']/524*100, H1_25['rev']/FY25['rev']*100))
print("2H26 implied by revised guidance: OP %.1f (2H25 %.1f, %+.1f%%), NI %.1f (2H25 %.1f, %+.1f%%), rev(orig) %.1f (2H25 %.1f)" % (
    FY26G1['op']-H1_26['op'], FY25['op']-H1_25['op'], ((FY26G1['op']-H1_26['op'])/(FY25['op']-H1_25['op'])-1)*100,
    FY26G1['ni']-H1_26['ni'], FY25['ni']-H1_25['ni'], ((FY26G1['ni']-H1_26['ni'])/(FY25['ni']-H1_25['ni'])-1)*100,
    524-H1_26['rev'], FY25['rev']-H1_25['rev']))
print("== Standalone quarters ==")
print("Q2 FY25: rev %.1f op %.1f ord %.1f ni %.1f" % (H1_25['rev']-Q1_25['rev'], H1_25['op']-Q1_25['op'], H1_25['ordi']-Q1_25['ordi'], H1_25['ni']-Q1_25['ni']))
print("Q2 FY26: rev %.1f op %.1f ni %.1f" % (H1_26['rev']-Q1_26['rev'], H1_26['op']-Q1_26['op'], H1_26['ni']-Q1_26['ni']))
print("Q3 FY25: rev %.1f ord %.1f ni %.1f" % (M9_25['rev']-H1_25['rev'], M9_25['ordi']-H1_25['ordi'], M9_25['ni']-H1_25['ni']))
print("Q4 FY25: rev %.1f ord %.1f ni %.1f" % (FY25['rev']-M9_25['rev'], FY25['ordi']-M9_25['ordi'], FY25['ni']-M9_25['ni']))
print("== Margins ==")
print("OP margin FY24 %.1f%% FY25 %.1f%% FY26G0 %.1f%%" % (FY25['op']/1.202/(FY25['rev']/1.023)*100, FY25['op']/FY25['rev']*100, 100/524*100))
print("OP margin 1H25 %.1f%% 1H26 %.1f%%; Q1 25 %.1f%% Q1 26 %.1f%%; Q2 25 %.1f%% Q2 26 %.1f%%" % (
    H1_25['op']/H1_25['rev']*100, H1_26['op']/H1_26['rev']*100, Q1_25['op']/Q1_25['rev']*100, Q1_26['op']/Q1_26['rev']*100,
    (H1_25['op']-Q1_25['op'])/(H1_25['rev']-Q1_25['rev'])*100, (H1_26['op']-Q1_26['op'])/(H1_26['rev']-Q1_26['rev'])*100))
print("== Net non-operating drag (OP - ordinary) ==")
print("FY25 %.2f; FY26G0 %.2f; FY26G1 %.2f; 1H25 %.2f; Q1 25 %.2f; Q1 26 %.2f; 2H25 %.2f" % (
    FY25['op']-FY25['ordi'], 100-80.5, 105.5-83.5, H1_25['op']-H1_25['ordi'], Q1_25['op']-Q1_25['ordi'], Q1_26['op']-Q1_26['ordi'],
    (FY25['op']-FY25['ordi'])-(H1_25['op']-H1_25['ordi'])))
print("NI/ordinary: FY25 %.1f%% FY26G0 %.1f%% FY26G1 %.1f%%" % (FY25['ni']/FY25['ordi']*100, 63/80.5*100, 65/83.5*100))
TAX=0.306; MI=0.5
def implied_xo(ordi, ni): return (ni+MI)/(1-TAX) - ordi
print("Implied net extraordinary (tax %.1f%%, MI %.1f): FY25 %.1f, FY26G0 %.1f, FY26G1 %.1f" % (TAX*100, MI, implied_xo(FY25['ordi'],FY25['ni']), implied_xo(80.5,63.0), implied_xo(83.5,65.0)))
print("FY25 guidance history: Q3 revised OP 92.5 (orig %.1f), NI 58.0 (orig %.1f); actual vs revised OP %+.1f%%, NI %+.1f%%, ord vs 78.5 %+.1f%%" % (
    92.5-6.5, 58.0-3.0, (FY25['op']/92.5-1)*100, (FY25['ni']/58.0-1)*100, (FY25['ordi']/78.5-1)*100))
print("FY26G0 NI vs QUICK cons 61.25: %+.1f%%" % ((63.0/61.25-1)*100))
print("Cons vs revised guidance: ord 84.467 %+.1f%%, NI 66.477 %+.1f%%; pre-rev ord cons 83.432 vs 80.5 %+.1f%%" % ((84.467/83.5-1)*100, (66.477/65-1)*100, (83.432/80.5-1)*100))
print("TP: cons 3985 vs 3211 %+.1f%%; implied px at +21.08%% = %.0f" % ((3985/3211-1)*100, 3985/1.2108))
print("Condo 1H26: 270 units x 69.11m = %.1f bn rev; GP @27.8%% = %.1f bn" % (270*69.11/1000, 270*69.11/1000*0.278))

print()
print("================ EPS MODEL (estimates) ================")
yrs = ['FY2025A','FY2026E','FY2027E','FY2028E']
bldg = {'FY2025A':67.05}; res={'FY2025A':25.56}; oth={'FY2025A':FY25['op']-67.05-25.56}
d_lease = {'FY2026E':3.5,'FY2027E':5.5,'FY2028E':4.5}
d_sales = {'FY2026E':14.0,'FY2027E':-4.0,'FY2028E':0.0}
res_lvl = {'FY2026E':22.0,'FY2027E':27.0,'FY2028E':28.0}
d_oth = {'FY2026E':-2.7,'FY2027E':-0.5,'FY2028E':-0.5}
nonop = {'FY2025A':FY25['op']-FY25['ordi'],'FY2026E':22.0,'FY2027E':24.0,'FY2028E':26.5}
xo = {'FY2026E':10.0,'FY2027E':8.0,'FY2028E':7.0}
shares = {'FY2025A':sh25,'FY2026E':207.5,'FY2027E':206.6,'FY2028E':205.7}
rows=[]
prev='FY2025A'
out={}
out['FY2025A']=dict(bldg=67.05,res=25.56,oth=oth['FY2025A'],op=FY25['op'],nonop=nonop['FY2025A'],ordi=FY25['ordi'],xo=implied_xo(FY25['ordi'],FY25['ni']),
                    pretax=FY25['ordi']+implied_xo(FY25['ordi'],FY25['ni']),ni=FY25['ni'],sh=sh25,eps=FY25['ni']/sh25*1000,dps=105)
for y in yrs[1:]:
    b = out[prev]['bldg'] + d_lease[y] + d_sales[y]
    r = res_lvl[y]
    o = out[prev]['oth'] + d_oth[y]
    op = b + r + o
    ordi = op - nonop[y]
    pt = ordi + xo[y]
    ni = pt*(1-TAX) - MI
    eps = ni/shares[y]*1000
    out[y]=dict(bldg=b,res=r,oth=o,op=op,nonop=nonop[y],ordi=ordi,xo=xo[y],pretax=pt,ni=ni,sh=shares[y],eps=eps,dps=round(eps*0.40))
    prev=y
hdr = "%-26s" % "" + "".join("%11s" % y for y in yrs)
print(hdr)
for k,lab in [('bldg','Building seg OP'),('res','Residential seg OP'),('oth','Other segs - corporate'),('op','Operating income'),
              ('nonop','Net non-op cost'),('ordi','Ordinary income'),('xo','Net extraordinary'),('pretax','Pre-tax'),('ni','Net income (NI)'),
              ('sh','Avg shares (m)'),('eps','EPS (JPY)'),('dps','DPS @40% (JPY)')]:
    print("%-26s" % lab + "".join("%11.1f" % out[y][k] for y in yrs))
for y in yrs[1:]:
    p = yrs[yrs.index(y)-1]
    print("%s growth: OP %+.1f%%, ordinary %+.1f%%, NI %+.1f%%, EPS %+.1f%%" % (y,(out[y]['op']/out[p]['op']-1)*100,(out[y]['ordi']/out[p]['ordi']-1)*100,(out[y]['ni']/out[p]['ni']-1)*100,(out[y]['eps']/out[p]['eps']-1)*100))
print("FY2026E vs guidance NI %+.1f%%, vs consensus NI %+.1f%%; EPS vs guide-implied %.1f, cons-implied %.1f" % ((out['FY2026E']['ni']/65-1)*100,(out['FY2026E']['ni']/66.477-1)*100, 65/sh26*1000, 66.477/sh26*1000))
print("FY2026E ordinary vs guidance %+.1f%%, vs IFIS cons %+.1f%%" % ((out['FY2026E']['ordi']/83.5-1)*100,(out['FY2026E']['ordi']/84.467-1)*100))
print("2H26E implied: bldg %.1f res %.1f op %.1f" % (out['FY2026E']['bldg']-40.1, out['FY2026E']['res']-2.9, out['FY2026E']['op']-39.8))

print()
print("== Sensitivities (after tax 30.6%, FY2027E shares 206.6m) ==")
def s(pretax_delta, sh=206.6): return pretax_delta*(1-TAX)/sh*1000
print("+/-5bn property-sale profit: +/-%.1f yen EPS" % s(5))
print("+/-1bn: +/-%.1f yen EPS (rule of thumb)" % s(1))
print("+25bp on 1.3tn debt (assumed, full repricing): -%.1f bn pretax, -%.1f yen EPS" % (1300*0.0025, s(1300*0.0025)))
print("+1ppt condo GPM on ~150bn condo revenue (assumed): +%.1f yen" % s(1.5))
print("+1%% leasing revenue on ~150bn (assumed, full drop-through): +%.1f yen" % s(1.5))
print("+/-2bn extraordinary gains: +/-%.1f yen" % s(2))
# Bull / bear FY2027E
base=out['FY2027E']
bull_pt = base['pretax'] + 4.0 + 2.0 + 1.0
bear_pt = base['pretax'] - 8.0 - 3.0 - 2.0
for lab,pt in [('Bull',bull_pt),('Bear',bear_pt)]:
    ni = pt*(1-TAX)-MI
    print("%s FY2027E: pretax %.1f NI %.1f EPS %.0f" % (lab, pt, ni, ni/206.6*1000))
for y,shs in [('FY2027E',206.6),('FY2028E',205.7)]:
    b=out[y]
    for lab,dpt in [('Bull',+4.0+2.0+1.0),('Bear',-8.0-3.0-2.0)]:
        pt=b['pretax']+dpt; ni=pt*(1-TAX)-MI
        print("%s %s: pretax %.1f NI %.1f EPS %.0f" % (lab,y,pt,ni,ni/shs*1000))
print("EPS CAGR FY25A-FY28E: %.1f%%" % (((out['FY2028E']['eps']/out['FY2025A']['eps'])**(1/3)-1)*100))
print("ROE check: NI FY26E %.1f; equity needed for 10%% ROE = %.0f bn" % (out['FY2026E']['ni'], out['FY2026E']['ni']/0.10))
