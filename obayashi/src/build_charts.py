import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#14243f"; BLUE="#2f6bd0"; GREY="#9aa3b2"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})

# --- Regression: EV/Sales (y) vs EBIT margin % (x), listed peers (indicative, mixed-source) ---
peers = {  # name: (EBIT margin %, EV/Sales x)
 "Vinci":(11.9,1.25),"Skanska":(3.5,0.52),"Balfour Beatty":(2.1,0.27),"Hochtief":(2.6,0.59),
 "Kajima":(7.7,1.03),"Taisei":(9.0,1.34),"Shimizu":(5.8,0.63)}
x=np.array([v[0] for v in peers.values()]); y=np.array([v[1] for v in peers.values()])
n=len(x); b,a=np.polyfit(x,y,1); yhat=a+b*x
r2=1-((y-yhat)**2).sum()/((y-y.mean())**2).sum()
se=np.sqrt(((y-yhat)**2).sum()/(n-2)); sxx=((x-x.mean())**2).sum(); tstat=b/(se/np.sqrt(sxx))
mc=2081; netcash=84; ev=mc-netcash; sales=2586.3
oby_x=7.5; oby_y=ev/sales; implied=a+b*oby_x
print(dict(n=n,slope=b,intercept=a,r2=r2,t=tstat,oby_evs=oby_y,implied=implied,gap=implied/oby_y-1))
fig,ax=plt.subplots(figsize=(7.6,4.8),dpi=200)
xs=np.linspace(0,13,50); ax.plot(xs,a+b*xs,color=NAVY,lw=1.5,ls="--",label="Peer OLS fit")
ax.scatter(x,y,s=55,color=GREY,zorder=3)
for k,(mx,my) in peers.items(): ax.annotate(k,(mx,my),xytext=(5,-10),textcoords="offset points",fontsize=8,color="#444")
ax.scatter([oby_x],[oby_y],s=110,color=BLUE,zorder=4); ax.annotate("Obayashi (actual)",(oby_x,oby_y),xytext=(8,-14),textcoords="offset points",color=BLUE,fontweight="bold",fontsize=9)
ax.scatter([oby_x],[implied],s=90,facecolor="white",edgecolor=BLUE,lw=1.6,zorder=4); ax.annotate("Obayashi (regression-implied)",(oby_x,implied),xytext=(-150,6),textcoords="offset points",color=BLUE,fontsize=8.5)
ax.set_xlabel("EBIT margin, last FY (%)"); ax.set_ylabel("TEV / Sales (x)")
ax.set_title(f"TEV/Sales vs EBIT margin: listed construction peers (n={n})",loc="left",fontsize=11,color=NAVY,fontweight="bold")
ax.text(0.02,0.95,f"EV/Sales = {a:.2f} + {b:.3f} x margin\nR² = {r2:.2f}, t-stat = {tstat:.1f}, n = {n}",transform=ax.transAxes,va="top",fontsize=8.5,color="#333")
for s in("top","right"): ax.spines[s].set_visible(False)
ax.grid(alpha=.25); fig.text(0.01,0.005,"Source: aggregator snippets (Marketscreener, TipRanks, Stockanalysis), mixed dates; indicative. Obayashi EV = mkt cap 2,081bn less net cash 84bn.",fontsize=6.5,color="#666")
fig.tight_layout(rect=(0,0.02,1,1)); fig.savefig("assets/regression.png"); plt.close()

# --- OP and margin trend ---
fy=["FY3/22","FY3/23","FY3/24","FY3/25","FY3/26","FY3/27E\n(guide)"]
op=[41.1,93.8,79.4,142.5,194.7,180.0]; sl=[1922.9,1983.9,2325.2,2590.8,2586.3,2945.0]
mg=[o/s*100 for o,s in zip(op,sl)]
fig,ax=plt.subplots(figsize=(7.6,4.2),dpi=200)
cols=[NAVY]*5+[GREY]; ax.bar(fy,op,color=cols,width=.55)
for i,v in enumerate(op): ax.text(i,v+4,f"{v:.0f}",ha="center",fontsize=8.5)
ax.set_ylabel("Operating income (JPY bn)"); ax2=ax.twinx(); ax2.plot(fy,mg,color=BLUE,marker="o",lw=2); ax2.set_ylim(0,10); ax2.set_ylabel("Operating margin (%)",color=BLUE)
for i,v in enumerate(mg): ax2.text(i,v+.45,f"{v:.1f}%",ha="center",color=BLUE,fontsize=8)
for s in("top",): ax.spines[s].set_visible(False); ax2.spines[s].set_visible(False)
ax.set_title("Operating income and margin, FY3/22-FY3/27E",loc="left",fontsize=11,color=NAVY,fontweight="bold")
fig.tight_layout(); fig.savefig("assets/op_trend.png"); plt.close()

# --- Segment OP FY3/26 ---
seg=["Domestic\nbuilding","Domestic\ncivil","Overseas\nbuilding","Overseas\ncivil","Real estate,\nother (derived)"]
v=[104.0,40.9,11.9,14.7,23.0]; m=[104.0/1138.8*100,40.9/426.6*100,11.9/508*100,14.7/336*100,None]
fig,ax=plt.subplots(figsize=(7.6,4.2),dpi=200)
ax.bar(seg,v,color=[NAVY,NAVY,BLUE,BLUE,GREY],width=.55)
for i,val in enumerate(v):
    lab=f"{val:.1f}"+(f"\n({m[i]:.1f}% margin)" if m[i] else "")
    ax.text(i,val+2,lab,ha="center",fontsize=8.5)
ax.set_ylim(0,125); ax.set_ylabel("Segment operating income (JPY bn)")
for s in("top","right"): ax.spines[s].set_visible(False)
ax.set_title("FY3/26 operating income by segment",loc="left",fontsize=11,color=NAVY,fontweight="bold")
fig.tight_layout(); fig.savefig("assets/segment_op.png"); plt.close()
