import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#13213d"; BLUE="#2f6fd0"; RED="#b83a3a"; GREEN="#2e8b57"; GREY="#9aa3b2"; MUTED="#6b7280"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.edgecolor":"#c9ced6","axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"axes.axisbelow":True,"grid.color":"#eceff3"})
m=json.load(open("raw/model.json")); F=m["F26"]; B=m["scen"]["base"]["F28"]
pc26=F["pc_rev"]; pcm26=(F["adj_ebitda"]+975)/pc26; do26=-975
margin=(B["pc_ebitda"]/B["pc_rev"]-pcm26)*pc26
growth=(B["pc_rev"]-pc26)*(B["pc_ebitda"]/B["pc_rev"])
dol=B["do_ebitda"]-do26
start=F["adj_ebitda"]; end=B["adj_ebitda"]
resid=end-(start+margin+growth+dol)
steps=[("FY26E adj.\nEBITDA",start,"total"),("PC margin\nrecovery",margin,"up"),("PC volume\ngrowth",growth,"up"),("DO loss\nreduction",dol,"up"),("Other",resid,"up" if resid>=0 else "down"),("FY28E adj.\nEBITDA",end,"total")]
steps=[s for s in steps if not (s[0]=="Other" and abs(s[1])<1)]
fig,ax=plt.subplots(figsize=(8.2,4.3)); run=0
for i,(lab,v,k) in enumerate(steps):
    if k=="total":
        ax.bar(i,v,color=NAVY if i==0 else GREEN,width=0.6); run=v; ax.text(i,v+40,f"{v:,.0f}",ha="center",fontsize=9.5,weight="bold")
    else:
        col=BLUE if v>=0 else RED; b=run if v>=0 else run+v
        ax.bar(i,abs(v),bottom=b,color=col,width=0.6); ax.text(i,run+max(v,0)+40,f"{v:+,.0f}",ha="center",fontsize=9.5); run+=v
ax.set_xticks(range(len(steps)),[s[0] for s in steps],fontsize=9)
ax.set_ylabel("US$m"); ax.set_title("Base case: adjusted EBITDA bridge FY26E to FY28E (US$m) [e]",fontsize=11,loc="left")
fig.tight_layout(); fig.savefig("out/charts/bridge.png",dpi=200); plt.close()
print(round(start),round(margin),round(growth),round(dol),round(resid),round(end), round(pcm26*100,1))
