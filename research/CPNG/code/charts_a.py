import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#13213d"; BLUE="#2f6fd0"; RED="#b83a3a"; GREY="#9aa3b2"; INK="#1f2937"; MUTED="#6b7280"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.edgecolor":"#c9ced6","axes.labelcolor":INK,"xtick.color":MUTED,"ytick.color":MUTED,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"axes.axisbelow":True,"grid.color":"#eceff3","grid.linewidth":0.8})
O="out/charts/"
rows=json.load(open("raw/peers_calc.json"))
# 1 regression EV/Sales vs EBIT margin (LTM), exclude Jumia (outlier, sub-scale) and JD (net cash > distorts) kept? keep all except Jumia
pts=[r for r in rows if r["name"] not in ("Coupang","Jumia")]
x=np.array([r["ebit_m"] for r in pts]); y=np.array([r["ev_sales"] for r in pts])
b,a=np.polyfit(x,y,1); yhat=a+b*x; r2=1-((y-yhat)**2).sum()/((y-y.mean())**2).sum()
reg={"intercept":a,"slope":b,"r2":r2,"n":len(pts)}
json.dump(reg,open("raw/regression.json","w"))
fig,ax=plt.subplots(figsize=(8.2,4.6))
xs=np.linspace(-4,24,50); ax.plot(xs,a+b*xs,ls="--",color=BLUE,lw=1.5)
ax.scatter(x,y,s=46,color=GREY,edgecolor="white",linewidth=1.5,zorder=3)
for r in pts: ax.annotate(r["name"],(r["ebit_m"],r["ev_sales"]),xytext=(5,3),textcoords="offset points",fontsize=8,color=MUTED)
cp=[r for r in rows if r["name"]=="Coupang"][0]
ax.scatter([cp["ebit_m"]],[cp["ev_sales"]],s=80,color=RED,edgecolor="white",linewidth=1.5,zorder=4)
ax.annotate(f"Coupang LTM\n({cp['ebit_m']:.1f}% EBIT, {cp['ev_sales']:.2f}x)",(cp["ebit_m"],cp["ev_sales"]),xytext=(-4.6,1.35),textcoords="data",fontsize=8.5,ha="left",color=RED,arrowprops=dict(arrowstyle="-",color=RED,lw=0.8),weight="bold")
fy25m=498/34534*100; ev=cp["ev_local"]; evs25=ev/34534
ax.scatter([fy25m],[evs25],s=80,color=NAVY,edgecolor="white",linewidth=1.5,zorder=4)
ax.annotate(f"Coupang on FY25 (pre-breach) {fy25m:.1f}% EBIT, {evs25:.2f}x",(fy25m,evs25),xytext=(6,6),textcoords="offset points",fontsize=8.5,color=NAVY,weight="bold")
ax.text(14,0.15,f"OLS: EV/Sales = {a:.2f} + {b:.3f} x EBIT margin\nR² = {r2:.2f} (n={len(pts)} listed peers, ex-Jumia)",color=BLUE,fontsize=8.5)
ax.set_xlabel("EBIT margin, LTM (%)"); ax.set_ylabel("EV / Sales, LTM (x)"); ax.axhline(0,color="#c9ced6",lw=0.8)
fig.tight_layout(); fig.savefig(O+"regression.png",dpi=200); plt.close()
print(reg, "implied at FY25 margin", a+b*fy25m, "at 3%", a+b*3, "at 5%", a+b*5)

# 2 annual revenue + margins small multiples
yrs=["FY21","FY22","FY23","FY24","FY25"]; rev=[18406,20583,24383,30268,34534]; ebit=[-1198,-112,473,388,498]; ebitda=[-997,119,748,821,1015]; ni=[-1543,-92,1360,154,208]; gp=[3109,4710,6190,8715,10141]
fig,axs=plt.subplots(1,3,figsize=(10,3.2))
axs[0].bar(yrs,[v/1000 for v in rev],color=NAVY,width=0.6); axs[0].set_title("Revenue (US$bn)",fontsize=10,color=INK,loc="left")
for i,v in enumerate(rev): axs[0].text(i,v/1000+0.4,f"{v/1000:.1f}",ha="center",fontsize=8,color=INK)
axs[1].plot(yrs,[g/r*100 for g,r in zip(gp,rev)],color=NAVY,lw=2,marker="o",ms=5); axs[1].set_title("Gross margin (%)",fontsize=10,color=INK,loc="left")
for i,(g,r) in enumerate(zip(gp,rev)): axs[1].text(i,g/r*100+0.6,f"{g/r*100:.1f}",ha="center",fontsize=8)
axs[2].plot(yrs,[e/r*100 for e,r in zip(ebitda,rev)],color=BLUE,lw=2,marker="o",ms=5,label="EBITDA margin")
axs[2].plot(yrs,[e/r*100 for e,r in zip(ebit,rev)],color=RED,lw=2,marker="o",ms=5,label="EBIT margin")
axs[2].axhline(0,color="#c9ced6"); axs[2].set_title("EBITDA & EBIT margin (%)",fontsize=10,color=INK,loc="left"); axs[2].legend(frameon=False,fontsize=8)
fig.tight_layout(); fig.savefig(O+"annual.png",dpi=200); plt.close()

# 3 quarterly revenue and GAAP operating income (two panels)
q=["3Q24","4Q24","1Q25","2Q25","3Q25","4Q25","1Q26","2Q26"]; qr=[7866,7965,7908,8524,9267,8835,8504,8856]; qe=[117,179,154,149,162,8,-242,-556]
fig,axs=plt.subplots(1,2,figsize=(10,3.2))
axs[0].bar(q,[v/1000 for v in qr],color=NAVY,width=0.6); axs[0].set_title("Quarterly revenue (US$bn)",fontsize=10,loc="left")
for i,v in enumerate(qr): axs[0].text(i,v/1000+0.1,f"{v/1000:.2f}",ha="center",fontsize=7.5)
axs[0].set_ylim(0,10.5)
axs[1].bar(q,qe,color=[NAVY if v>=0 else RED for v in qe],width=0.6); axs[1].axhline(0,color="#c9ced6"); axs[1].set_title("GAAP operating income (US$m)",fontsize=10,loc="left")
for i,v in enumerate(qe): axs[1].text(i,v+(12 if v>=0 else -40),f"{v}",ha="center",fontsize=7.5)
fig.tight_layout(); fig.savefig(O+"quarterly.png",dpi=200); plt.close()

# 4 historical EV/Sales and EV/EBITDA (year-end) + current
lab=["Dec-21","Dec-22","Dec-23","Dec-24","Dec-25","Oct-26 (LTM)"]
px=[29.38,14.71,16.19,22.42,23.37,15.82]; sh=[1752.2,1793.5,1810,1837,1826,1799]
nd=[-1366.6,-1107,-2456,-2154,-1683,-477]; sales=[18406,20583,24383,30268,34534,35462]
evs=[(p*s+n)/sl for p,s,n,sl in zip(px,sh,nd,sales)]
json.dump(dict(lab=lab,evs=evs,ev=[p*s+n for p,s,n in zip(px,sh,nd)]),open("raw/hist_mult.json","w"))
fig,ax=plt.subplots(figsize=(8,3.2))
ax.bar(lab,evs,color=[GREY]*5+[RED],width=0.55)
for i,v in enumerate(evs): ax.text(i,v+0.05,f"{v:.2f}x",ha="center",fontsize=8.5)
ax.axhline(np.mean(evs[:5]),ls="--",color=BLUE,lw=1.2); ax.text(4.6,np.mean(evs[:5])+0.06,f"5-yr year-end avg {np.mean(evs[:5]):.2f}x",color=BLUE,fontsize=8,ha="right")
ax.set_title("Coupang EV / Sales at each year-end vs today",fontsize=10,loc="left")
fig.tight_layout(); fig.savefig(O+"hist_evsales.png",dpi=200); plt.close()
print([round(v,2) for v in evs])
