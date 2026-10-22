import json, sys, datetime as dt, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as mdates
sys.path.insert(0,"raw"); from cpng_weekly import series
NAVY="#13213d"; BLUE="#2f6fd0"; RED="#b83a3a"; GREY="#9aa3b2"; INK="#1f2937"; MUTED="#6b7280"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.edgecolor":"#c9ced6","axes.labelcolor":INK,"xtick.color":MUTED,"ytick.color":MUTED,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"axes.axisbelow":True,"grid.color":"#eceff3","grid.linewidth":0.8})
O="out/charts/"
# Sentiment per call (ProntoNLP getDocuments sentimentScore, -1..1)
calls=["4Q23","1Q24","2Q24","3Q24","4Q24","1Q25","2Q25","3Q25","4Q25","1Q26","2Q26"]
sent=[0.85,0.87,0.80,0.81,0.83,0.85,0.86,0.81,0.42,0.34,0.53]
neg=[15,10,20,17,24,13,14,22,64,71,64]; pos=[211,187,175,164,249,189,210,207,193,166,254]
fig,axs=plt.subplots(1,2,figsize=(10,3.1))
axs[0].bar(calls,sent,color=[NAVY]*8+[RED,RED,BLUE],width=0.6); axs[0].set_ylim(0,1)
for i,v in enumerate(sent): axs[0].text(i,v+0.02,f"{v:.2f}",ha="center",fontsize=7.5)
axs[0].set_title("ProntoNLP call sentiment score (-1 to +1)",fontsize=10,loc="left")
share=[n/(n+p)*100 for n,p in zip(neg,pos)]
axs[1].plot(calls,share,color=RED,lw=2,marker="o",ms=5)
for i,v in enumerate(share): axs[1].text(i,v+1.2,f"{v:.0f}%",ha="center",fontsize=7.5)
axs[1].set_ylim(0,40); axs[1].set_title("Negative events as % of polar events",fontsize=10,loc="left")
for a in axs: a.tick_params(axis="x",labelsize=7.5)
fig.tight_layout(); fig.savefig(O+"sentiment.png",dpi=200); plt.close()
# Price chart with events (events file optional)
ev=json.load(open("raw/events.json")) if len(sys.argv)>1 else []
d=[s[0] for s in series]; c=[s[1] for s in series]
for fname,fs in [("price.png",(10.5,4.4)),("price_memo.png",(9.4,6.2))]:
  fig,ax=plt.subplots(figsize=fs)
  ax.plot(d,c,color=NAVY,lw=1.6); ax.fill_between(d,c,0,color="#eef1f6")
  for e in ev:
      x=dt.date.fromisoformat(e["date"]); y=e.get("y")
      yy=min(c,key=lambda v:0) # placeholder
      # find close at that week
      idx=min(range(len(d)),key=lambda i:abs((d[i]-x).days)); py=c[idx]
      ax.annotate(e["label"],(d[idx],py),xytext=(d[idx]+dt.timedelta(days=e.get("dx",0)),e["ty"]),fontsize=7.2,color=RED if e.get("neg") else BLUE,ha="center",
          arrowprops=dict(arrowstyle="-",color="#9aa3b2",lw=0.7))
  ax.set_ylabel("US$ per share (weekly close)"); ax.set_ylim(0,72); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
  ax.set_title("Coupang share price since IPO (weekly close, US$) with key catalysts",fontsize=10,loc="left")
  fig.tight_layout(); fig.savefig(O+fname,dpi=200); plt.close()
print("ok")
