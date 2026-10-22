import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#13213d"; BLUE="#2f6fd0"; RED="#b83a3a"; GREY="#9aa3b2"; INK="#1f2937"; MUTED="#6b7280"; LBLUE="#8fb3ea"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.edgecolor":"#c9ced6","axes.labelcolor":INK,"xtick.color":MUTED,"ytick.color":MUTED,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"axes.axisbelow":True,"grid.color":"#eceff3","grid.linewidth":0.8})
O="out/charts/"
# Segment history (company disclosures via ProntoNLP notes A)
yrs=["FY22","FY23","FY24","FY25"]
pc=[20.0,23.6,26.7,29.6]; do=[0.6,0.789,3.6,4.934]; pcE=[0.60,1.5,2.0,2.49]; doE=[-0.225,-0.466,-0.631,-0.995]
fig,axs=plt.subplots(1,2,figsize=(10,3.3))
x=np.arange(len(yrs)); w=0.38
axs[0].bar(x-w/2,pc,w,color=NAVY,label="Product Commerce"); axs[0].bar(x+w/2,do,w,color=LBLUE,label="Developing Offerings")
for i,(a,b) in enumerate(zip(pc,do)): axs[0].text(i-w/2,a+0.4,f"{a:.1f}",ha="center",fontsize=7.5); axs[0].text(i+w/2,b+0.4,f"{b:.1f}",ha="center",fontsize=7.5)
axs[0].set_xticks(x,yrs); axs[0].set_title("Segment revenue (US$bn)",fontsize=10,loc="left"); axs[0].legend(frameon=False,fontsize=8,loc="upper left")
axs[1].bar(x-w/2,pcE,w,color=NAVY,label="PC adj. EBITDA"); axs[1].bar(x+w/2,doE,w,color=RED,label="DO adj. EBITDA")
for i,(a,b) in enumerate(zip(pcE,doE)): axs[1].text(i-w/2,a+0.05,f"{a:.2f}",ha="center",fontsize=7.5); axs[1].text(i+w/2,b-0.18,f"{b:.2f}",ha="center",fontsize=7.5)
axs[1].axhline(0,color="#c9ced6"); axs[1].set_xticks(x,yrs); axs[1].set_title("Segment adj. EBITDA (US$bn)",fontsize=10,loc="left"); axs[1].legend(frameon=False,fontsize=8,loc="upper left")
fig.text(0.01,0.005,"FY22 PC adj. EBITDA derived from 3.0% margin x US$20.0bn; FY22 DO revenue = total less PC. Source: company releases via ProntoNLP.",fontsize=6.5,color=MUTED)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig(O+"segments.png",dpi=200); plt.close()
# Quarterly segment margins
q=["3Q25","4Q25","1Q26","2Q26"]; pcm=[8.8,7.7,5.0,5.1]; cons=[4.5,3.0,0.3,1.8]
fig,ax=plt.subplots(figsize=(6.2,3.0))
ax.plot(q,pcm,color=NAVY,lw=2,marker="o",ms=6,label="Product Commerce adj. EBITDA margin")
ax.plot(q,cons,color=BLUE,lw=2,marker="o",ms=6,label="Consolidated adj. EBITDA margin")
for i,(a,b) in enumerate(zip(pcm,cons)): ax.text(i,a+0.35,f"{a:.1f}%",ha="center",fontsize=8); ax.text(i,b-0.75,f"{b:.1f}%",ha="center",fontsize=8)
ax.set_ylim(-1,10.5); ax.legend(frameon=False,fontsize=7.5,loc="upper right"); ax.set_title("Margin reset after the Nov-25 data incident (%)",fontsize=10,loc="left")
fig.tight_layout(); fig.savefig(O+"margins_q.png",dpi=200); plt.close()
# Scenario chart
sc=[("Bear (25%)",9.5,RED),("Base (50%)",21.0,BLUE),("Bull (25%)",31.7,NAVY)]
fig,ax=plt.subplots(figsize=(6.2,3.0))
ax.bar([s[0] for s in sc],[s[1] for s in sc],color=[s[2] for s in sc],width=0.55)
for i,s in enumerate(sc): ax.text(i,s[1]+0.6,f"${s[1]:.1f} ({s[1]/15.82-1:+.0%})",ha="center",fontsize=8.5)
ax.axhline(15.82,ls="--",color=MUTED,lw=1.2); ax.text(-0.42,16.5,"Price $15.82",ha="left",fontsize=8,color=MUTED)
ax.axhline(20.8,ls=":",color=BLUE,lw=1.2); ax.text(-0.3,21.6,"Prob.-weighted $20.8",ha="left",fontsize=8,color=BLUE)
ax.set_ylim(0,38); ax.set_title("12-month value per share by scenario (US$)",fontsize=10,loc="left")
fig.tight_layout(); fig.savefig(O+"scenarios.png",dpi=200); plt.close()
print("ok")
