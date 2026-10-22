# Shared numbers (JPY bn unless noted). All derived values computed here to keep report consistent.
PRICE=3008.0; MCAP=2081.0; SHARES=MCAP/PRICE*1000/1000  # bn JPY / JPY -> m shares
SHARES_M=MCAP*1000/PRICE   # 691.8m
NETCASH=84.2; EQUITY=1316.5; SALES26=2586.3; OP26=194.7; NI26=173.8; DA_EST=50.0
SEC=288.8
EV=MCAP-NETCASH; EBITDA26=OP26+DA_EST
M=dict(ev=EV, ev_sales=EV/SALES26, ev_sales27=EV/2945.0, ev_ebitda=EV/EBITDA26, ev_ebit=EV/OP26,
       ev_adj=EV-SEC, ev_ebitda_adj=(EV-SEC)/EBITDA26, ev_ebit_adj=(EV-SEC)/OP26,
       pe_t=MCAP/NI26, pe_g=MCAP/157.0, pb=MCAP/EQUITY, dy=88/PRICE*100, dy27=94/PRICE*100,
       fcf=252.9-84.4, fcfy=(252.9-84.4)/MCAP*100, ebitda=EBITDA26, ebitda_m=EBITDA26/SALES26*100,
       nd_ebitda=-NETCASH/EBITDA26)
# EPS model: (sales, OP, non-op, extraordinary gains, tax, shares m)
def eps(sales,op,nonop,gain,shares,tax=0.30):
    ordi=op+nonop; pbt=ordi+gain; ni=pbt*(1-tax); return dict(sales=sales,op=op,ordi=ordi,gain=gain,ni=ni,eps=ni*1000/shares,shares=shares,opm=op/sales*100)
BASE=[eps(2945,192,5,40,686),eps(3030,197,5,20,680),eps(3120,206,5,15,672)]
BULL=[eps(2990,205,6,40,686),eps(3150,225,6,20,678),eps(3320,245,6,15,668)]
BEAR=[eps(2900,170,4,35,688),eps(2900,150,3,10,684),eps(2900,140,3,5,680)]
def val(ebitda,mult,shares=680): 
    eq=ebitda*mult+NETCASH+0.75*SEC; return eq, eq*1000/shares
SC={"Bear":(200,6.5),"Base":(247,8.5),"Bull":(295,9.5)}
SCV={k:val(*v) for k,v in SC.items()}
PROB={"Bear":0.30,"Base":0.50,"Bull":0.20}
PW=sum(PROB[k]*SCV[k][1] for k in SC)
if __name__=="__main__":
    print({k:round(v,2) for k,v in M.items()}); print(round(SHARES_M,1))
    for n,s in (("base",BASE),("bull",BULL),("bear",BEAR)): print(n,[ (round(x['ni'],1),round(x['eps'],1)) for x in s])
    print({k:(round(v[0]),round(v[1])) for k,v in SCV.items()}, round(PW))
