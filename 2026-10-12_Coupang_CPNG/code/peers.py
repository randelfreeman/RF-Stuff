import json
CNY=7.10  # [e] analyst FX assumption CNY per USD - not sourced from S&P/Pronto
# name: (ticker, listed?, exchange, price, price_ccy, shares_m (S&P diluted wtd latest Q), fin_ccy, rev_ltm, rev_ltm_yago, ebitda, ebit, ni, netdebt) all fin in millions local
P={
"Coupang":("CPNG",True,"NYSE",15.82,"USD",1799,"USD",35462,32263,-46,-603,-767,-477),
"Amazon":("AMZN",True,"NasdaqGS",262.43,"USD",10903,"USD",775680,670038,168912,93712,135281,128647),
"MercadoLibre":("MELI",True,"NasdaqGS",1889.85,"USD",50.697,"USD",35182,24096,3892,2907,1863,7462),
"Sea Ltd":("SE",True,"NYSE",95.25,"USD",654.45,"USD",27723.16,19379.25,2682.9,2284.5,1637.9,-4972.4),
"PDD Holdings":("PDD",True,"NasdaqGS",81.35,"USD",1473.5,"CNY",450775.7,409621.5,99101,98553,92075.5,-451570),
"Alibaba":("BABA",True,"NYSE/HKEX",107.0,"HKD",2415.5*8,"CNY",1044971,1000763,99513,47614,73557,-119167),
"JD.com":("JD",True,"NasdaqGS",27.09,"USD",1408,"CNY",1313438,1265115,11798,2190,14794,-154749),
"Vipshop":("VIPS",True,"NYSE",12.90,"USD",488.1,"CNY",105126.3,105974.7,9613.9,8029.7,10322.4,-21296),
"NAVER":("035420 KS",True,"KRX",183800,"KRW",150.727,"KRW",12962955,11303046,3024539,2243350,2023538,-3356823),
"E-MART":("139480 KS",True,"KRX",70000,"KRW",26.788,"KRW",28750949,29016096,1706997,232836,21216,9870057),
"Lotte Shopping":("023530 KS",True,"KRX",97800,"KRW",28.271,"KRW",13998510,13851929,1738978,651283,181088,11917224),
"Rakuten":("4755 JP",True,"TSE",659.6,"JPY",2240.4,"JPY",2646554,2387398,451701,148281,-64392,-65433),
"Zalando":("ZAL GY",True,"XETRA",23.80,"EUR",252,"EUR",13512.1,10942.5,654,418.8,94.8,-94.4),
"Allegro":("ALE PW",True,"WSE",51.75,"PLN",1021.27,"PLN",12303.4,10580.8,3425.4,2383.9,1705.2,2567.8),
"Jumia":("JMIA",True,"NYSE",6.28,"USD",123.97,"USD",209.6,164.0,-53.8,-54.3,-57.7,-34.4),
"Walmart":("WMT",True,"NasdaqGS",111.35,"USD",7978,"USD",735840,693153,44073,28980,22076,63563),
}
# HKD->CNY: derive HKD per USD from Pronto BABA USD mktcap? use peg 7.80 HKD/USD [e]
HKD=7.80
rows=[]
for n,(t,l,ex,px,pc,sh,fc,rev,rev0,ebitda,ebit,ni,nd) in P.items():
    mc=px*sh  # in price ccy, millions
    # convert market cap into financial currency
    if pc==fc: mcf=mc
    elif pc=="USD" and fc=="CNY": mcf=mc*CNY
    elif pc=="HKD" and fc=="CNY": mcf=mc/HKD*CNY
    ev=mcf+nd
    r=dict(name=n,ticker=t,exchange=ex,ccy=fc,mcap_local=round(mcf),ev_local=round(ev),
      ev_sales=ev/rev, ev_ebitda=(ev/ebitda if ebitda>0 else None), ev_ebit=(ev/ebit if ebit>0 else None),
      pe=(mcf/ni if ni>0 else None), nd_ebitda=(nd/ebitda if ebitda>0 else None),
      ebitda_m=ebitda/rev*100, ebit_m=ebit/rev*100, growth=(rev/rev0-1)*100)
    # USD mcap
    usd={"USD":1,"CNY":CNY,"KRW":1356,"JPY":157.6,"EUR":0.878,"PLN":3.84}[fc]
    r["mcap_usd_bn"]=mcf/usd/1000; r["ev_usd_bn"]=ev/usd/1000
    rows.append(r)
for r in rows:
    f=lambda x:"n.m." if x is None else f"{x:.1f}"
    print(f"{r['name']:15s} MC${r['mcap_usd_bn']:7.1f}bn EV/S {r['ev_sales']:.2f} EV/EBITDA {f(r['ev_ebitda'])} EV/EBIT {f(r['ev_ebit'])} PE {f(r['pe'])} ND/EBITDA {f(r['nd_ebitda'])} EBITDAm {r['ebitda_m']:.1f} EBITm {r['ebit_m']:.1f} g {r['growth']:.1f}")
json.dump(rows,open("raw/peers_calc.json","w"),indent=1)
