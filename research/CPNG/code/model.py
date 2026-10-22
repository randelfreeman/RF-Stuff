"""Coupang EPS model FY2026E-FY2028E. US$m. [e] = analyst estimate.
Actuals: S&P Capital IQ (statements) + company segment disclosures via ProntoNLP (notes A)."""
import json
M={}
# ---------------- Actuals ----------------
A=dict(
 FY25=dict(rev=34534,pc_rev=29600,do_rev=4934,adj_ebitda=1465,pc_ebitda=2490,do_ebitda=-995,da=517,sbc=475,ebit_gaap=473,net_int=113,other=11,ebt=597,tax=383,ni=208,dil_sh=1855,eps=0.11),
 H1_26=dict(rev=17360,pc_rev=14600,do_rev=2760,adj_ebitda=192,pc_ebitda=740,do_ebitda=-548,da=288,sbc=283,fines=410,ebit_gaap=-798,net_int=48,other=-38,ebt=-788,tax=48,ni=-836,eps=-0.47),
)
# ---------------- FY2026E: H2 build ----------------
q3=dict(pc_rev=8000*(1+0.065-0.050), do_rev=1267*1.20)   # PC +6.5% cc (Barclays Q&A implied 6-7%), FX -5pts [e]; DO +20% reported [e]
q3["rev"]=q3["pc_rev"]+q3["do_rev"]
q3["adj_ebitda"]=q3["rev"]*(0.045-0.033)                # guide: Q3 margin -300 to -400bp vs 4.5% -> use -330bp [e]
q4=dict(pc_rev=7400*(1+0.12-0.04), do_rev=1435*1.18)     # easy comp (Dec-25 incident), PC +12% cc, FX -4pts [e]
q4["rev"]=q4["pc_rev"]+q4["do_rev"]
q4["adj_ebitda"]=q4["rev"]*0.031                          # ~flat YoY vs 3.0% Q4'25 [e]
H2=dict(rev=q3["rev"]+q4["rev"],adj_ebitda=q3["adj_ebitda"]+q4["adj_ebitda"],da=305,sbc=280,fire=-150,net_int=20,other=0,tax=60)
H2["ebit_gaap"]=H2["adj_ebitda"]-H2["da"]-H2["sbc"]+H2["fire"]
H2["ebt"]=H2["ebit_gaap"]+H2["net_int"]+H2["other"]; H2["ni"]=H2["ebt"]-H2["tax"]
F26=dict(rev=A["H1_26"]["rev"]+H2["rev"],adj_ebitda=A["H1_26"]["adj_ebitda"]+H2["adj_ebitda"],da=A["H1_26"]["da"]+H2["da"],sbc=A["H1_26"]["sbc"]+H2["sbc"],
  oneoffs=-410+H2["fire"],ebit_gaap=A["H1_26"]["ebit_gaap"]+H2["ebit_gaap"],net_int=A["H1_26"]["net_int"]+H2["net_int"],other=A["H1_26"]["other"],tax=A["H1_26"]["tax"]+H2["tax"])
F26["ebt"]=F26["ebit_gaap"]+F26["net_int"]+F26["other"]; F26["ni"]=F26["ebt"]-F26["tax"]; F26["sh"]=1796
F26["pc_rev"]=A["H1_26"]["pc_rev"]+q3["pc_rev"]+q4["pc_rev"]; F26["do_rev"]=F26["rev"]-F26["pc_rev"]
# ---------------- FY2027E / FY2028E ----------------
def year(prev_pc,prev_do,pc_g,do_g,pc_m,do_loss,da,sbc,oneoff,net_int,etr,sh,min_tax=0):
    pc=prev_pc*(1+pc_g); do=prev_do*(1+do_g); rev=pc+do
    ebitda=pc*pc_m+do_loss
    ebit=ebitda-da-sbc+oneoff; ebt=ebit+net_int
    tax=max(ebt*etr,min_tax); ni=ebt-tax
    return dict(pc_rev=pc,do_rev=do,rev=rev,pc_ebitda=pc*pc_m,do_ebitda=do_loss,adj_ebitda=ebitda,da=da,sbc=sbc,oneoffs=oneoff,ebit_gaap=ebit,net_int=net_int,ebt=ebt,tax=tax,ni=ni,sh=sh)
S={}
S["base"]=dict(
 F27=year(F26["pc_rev"],F26["do_rev"],0.110,0.18,0.073,-800,680,580,+100,40,0.55,1790),
)
S["base"]["F28"]=year(S["base"]["F27"]["pc_rev"],S["base"]["F27"]["do_rev"],0.100,0.18,0.086,-600,780,620,0,30,0.40,1795)
S["bull"]=dict(F27=year(F26["pc_rev"],F26["do_rev"],0.140,0.22,0.080,-750,680,580,+100,40,0.50,1785))
S["bull"]["F28"]=year(S["bull"]["F27"]["pc_rev"],S["bull"]["F27"]["do_rev"],0.130,0.20,0.100,-450,790,630,0,30,0.33,1790)
S["bear"]=dict(F27=year(F26["pc_rev"],F26["do_rev"],0.055,0.12,0.058,-900,680,580,-150,20,0.80,1800,min_tax=150))
S["bear"]["F28"]=year(S["bear"]["F27"]["pc_rev"],S["bear"]["F27"]["do_rev"],0.055,0.10,0.062,-850,760,620,-100,0,0.70,1810,min_tax=150)
for k in S:
    for y in S[k]: S[k][y]["eps"]=S[k][y]["ni"]/S[k][y]["sh"]
F26["eps"]=F26["ni"]/F26["sh"]
# adjusted EPS ex one-offs (fines non-deductible; fire treated pre-tax at 24.2% Korea rate)
def adj(d):
    one=d.get("oneoffs",0)
    tax_on=0 if one==0 else (0.242*one if one!=-410 else 0)
    return (d["ni"]-one+ (0.242*(one+410) if d is F26 else 0.242*one))/d["sh"]
F26["adj_ni"]=F26["ni"]+410+150-0.242*150; F26["adj_eps"]=F26["adj_ni"]/F26["sh"]
for k in S:
    for y in S[k]:
        d=S[k][y]; d["adj_ni"]=d["ni"]-d["oneoffs"]*(1-0.242); d["adj_eps"]=d["adj_ni"]/d["sh"]
out=dict(actual=A,F26=F26,H2=H2,q3=q3,q4=q4,scen=S)
json.dump(out,open("raw/model.json","w"),indent=1,default=float)
f=lambda v:f"{v:,.0f}"
print("FY26E rev",f(F26["rev"]),"growth",f"{F26['rev']/34534-1:.1%}","adjEBITDA",f(F26["adj_ebitda"]),f"{F26['adj_ebitda']/F26['rev']:.1%}","EBIT",f(F26["ebit_gaap"]),"NI",f(F26["ni"]),"EPS",round(F26["eps"],2),"adjEPS",round(F26["adj_eps"],2))
print("Q3E rev",f(q3["rev"]),"adjEBITDA",f(q3["adj_ebitda"]),"| Q4E rev",f(q4["rev"]),"adjEBITDA",f(q4["adj_ebitda"]))
for k in S:
    for y in S[k]:
        d=S[k][y]; print(k,y,"rev",f(d["rev"]),f"g {d['rev']/(F26['rev'] if y=='F27' else S[k]['F27']['rev'])-1:.1%}","adjEBITDA",f(d["adj_ebitda"]),f"{d['adj_ebitda']/d['rev']:.1%}","EBIT",f(d["ebit_gaap"]),f"{d['ebit_gaap']/d['rev']:.1%}","NI",f(d["ni"]),"EPS",round(d["eps"],2),"adjEPS",round(d["adj_eps"],2))
