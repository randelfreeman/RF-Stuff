import json, statistics as st
# Year-end closes: ProntoNLP getStockPrices interval=quarter (Q4 bar close = Dec close); S&P annual revenue, net debt, diluted shares (local ccy, millions)
yrs=[2021,2022,2023,2024,2025]
D={
"Amazon":dict(px=[166.72,84,151.94,219.39,230.82],rev=[469822,513983,574785,637959,716924],nd=[43708,99912,74794,54199,55518],sh=[10296,10189,10492,10721,10827]),
"MercadoLibre":dict(px=[1348.4,846.24,1571.54,1700.44,2014.26],rev=[7069,10780,15107,20777,28893],nd=[1189,2399,-686,-250,5107],sh=[49.803,51.336,51.007,50.697,50.697]),
"Sea Ltd":dict(px=[223.71,52.03,40.5,106.1,127.57],rev=[9955.19,12449.7,13063.56,16819.87,22938.47],nd=[-5896.99,-2393.95,-896.32,-4496.44,-7196.33],sh=[532.71,558.12,594.41,604.71,638.23]),
"NAVER":dict(px=[374550.34,176452.16,224000,198900,242500],rev=[6817600,8220079,9670644,10737719,12035007],nd=[20448,-416279,-448742,-3105038,-4337437],sh=[150.004,150.418,150.853,151.003,150.132]),
"E-MART":dict(px=[143796.1,95163.53,74382.92,63400,81300],rev=[24932681,29332414,29472248,29020897,28970388],nd=[8434432,9254556,9090618,10380117,9801736],sh=[27.619,27.043,26.788,26.788,26.787]),
"Lotte Shopping":dict(px=[80095.29,86730.86,75000,54100,72500],rev=[15573550,15476036,14555864,13986578,13738355],nd=[11451762,11954497,11623189,12164181,11689969],sh=[28.271]*5),
}
cp=json.load(open("raw/hist_mult.json"))["evs"][:5]
out={}
for n,d in D.items():
    out[n]=[(p*s+nd)/r for p,s,nd,r in zip(d["px"],d["sh"],d["nd"],d["rev"])]
med=[st.median([out[n][i] for n in out]) for i in range(5)]
print("year  CPNG  peer-median  rel")
for i,y in enumerate(yrs): print(y, round(cp[i],2), round(med[i],2), f"{cp[i]/med[i]-1:+.0%}", {n:round(out[n][i],2) for n in out})
cur_peers={"Amazon":3.85,"MercadoLibre":2.94,"Sea Ltd":2.07,"NAVER":1.88,"E-MART":0.41,"Lotte Shopping":1.05}
cm=st.median(cur_peers.values()); print("current", 0.79, cm, f"{0.79/cm-1:+.0%}")
json.dump(dict(years=yrs,peers=out,median=med,cpng=cp,current=dict(cpng=0.79,median=cm,peers=cur_peers)),open("raw/hist_rel.json","w"),indent=1)
