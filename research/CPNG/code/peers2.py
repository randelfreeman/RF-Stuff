import json, statistics as st
rows=json.load(open("raw/peers_calc.json"))
cf={"Coupang":(1425,-1326),"Amazon":(161403,-173028),"MercadoLibre":(13905,-1496),"Sea Ltd":(5215.7,-1008.8),"PDD Holdings":(111894.7,-1145.1),"Alibaba":(78486,-155065),"JD.com":(51117,-22622),"Vipshop":(None,None),"NAVER":(3157422,-1693590),"E-MART":(1572542,-812993),"Lotte Shopping":(1954045,-866218),"Rakuten":(256382,-87256),"Zalando":(1020.6,-108.1),"Allegro":(3311.9,-1055.3),"Jumia":(-38.4,-4.6),"Walmart":(42923,-29414)}
for r in rows:
    c,k=cf[r["name"]]
    r["fcf_yield"]=None if c is None else (c+k)/r["mcap_local"]*100
peers=[r for r in rows if r["name"]!="Coupang"]
def med(key): 
    v=[r[key] for r in peers if r[key] is not None]; return st.median(v)
M={k:med(k) for k in ["ev_sales","ev_ebitda","ev_ebit","pe","nd_ebitda","ebitda_m","ebit_m","growth","fcf_yield"]}
json.dump(dict(rows=rows,median=M),open("raw/peers_final.json","w"),indent=1)
for r in rows:
    f=lambda x,d=1:"n.m." if x is None else f"{x:.{d}f}"
    print(f"{r['name']:15s} {r['mcap_usd_bn']:8.1f} {f(r['ev_sales'],2)} {f(r['ev_ebitda'])} {f(r['ev_ebit'])} {f(r['pe'])} {f(r['nd_ebitda'])} {r['ebitda_m']:.1f} {r['ebit_m']:.1f} {r['growth']:.1f} {f(r['fcf_yield'])}")
print("MEDIAN",{k:round(v,2) for k,v in M.items()})
