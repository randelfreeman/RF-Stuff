import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
NAVY="#14243f"; BLUE="#2f6bd0"; LG="#eef1f6"
fig,ax=plt.subplots(figsize=(11,6.4),dpi=200); ax.set_xlim(0,110); ax.set_ylim(0,64); ax.axis("off")
import textwrap
def box(x,y,w,h,title,lines,fc=LG,tc=NAVY,ec="#c5ccd8",fs=6.4):
    wrap=int(w*1.18); lines=[textwrap.fill(l,wrap) for l in " ".join(lines).replace(" | ","\n").split("\n")] if False else lines
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.2,rounding_size=1.0",fc=fc,ec=ec,lw=1))
    ax.text(x+w/2,y+h-2.0,title,ha="center",va="top",fontsize=8.2,fontweight="bold",color=tc)
    paras=[]
    for l in lines: paras.append(l)
    txt="\n".join(textwrap.fill(p,wrap) for p in " ".join(paras).split("  ")) if False else "\n".join(textwrap.fill(p,wrap) for p in paras)
    ax.text(x+w/2,y+h-5.4,txt,ha="center",va="top",fontsize=fs,color=tc,linespacing=1.35)
cols=[(1,"1  RAW MATERIALS",["Steel/rebar: Nippon Steel, JFE,","Tokyo Steel, Yamato Kogyo","Cement: Taiheiyo, UBE Mitsubishi,","Sumitomo Osaka","Ready-mix/aggregates (regional)","Glass: AGC | Timber/CLT","Naphtha-based: paint, waterproofing"]),
 (23,"2  EQUIPMENT & SYSTEMS",["Elevators: Mitsubishi Electric,","Hitachi, Toshiba Elevator","HVAC/MEP: Daikin, Takasago,","Taikisha, Kinden","Heavy plant: Komatsu, Hitachi CM,","Kobelco | TBM: Herrenknecht,","Japanese TBM makers"]),
 (45,"3  TRADES & LABOUR",["Specialist subcontractors","(partner association, Rinyukai*)","Skilled trades; foreign technical","trainees","Design: in-house + Nikken Sekkei,","Nihon Sekkei","JV partners: Kajima, Taisei, Shimizu,","Takenaka, Hazama Ando"])]
for x,t,l in cols: box(x,26,20.5,34,t,l)
box(67,26,21,34,"4  OBAYASHI GROUP",["Domestic building, civil","Overseas: Webcor, Kraemer,","E.W. Howell, J.E. Roberts-Obayashi,","MWH, GCON (US); Multiplex","(AU/UK/CA, pending); Asia cos","Real estate: Obayashi Shinseiwa","Renewables, wood (Cypress","Sunadaya)"],fc=NAVY,tc="white",ec=NAVY)
box(90,26,19.5,34,"5  CUSTOMERS",["Public: MLIT, NEXCO, JR Tokai,","JRTT, local govts","Developers: Mitsui Fudosan,","Mitsubishi Estate, Mori Bldg,","Sumitomo Realty, Tokyu","Industrial/tech: manufacturers,","fabs, data-centre operators","US: tech, healthcare, water utilities"])
for x in (21.8,43.8,65.8,88.8): ax.annotate("",xy=(x+1.6,42),xytext=(x-0.2,42),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.6))
box(1,2,52,18,"ENABLERS & FINANCING",["Banks: MUFG, SMBC, Mizuho (typical lenders; not confirmed per filing)","Insurers/holders: Nippon Life, Meiji Yasuda (typical); trust banks hold ~23%","Surety/performance bonding and project insurers (US/AU)","Ratings agencies: JCR, R&I"],fc="#f7f8fb")
box(56,2,53.5,18,"REGULATORS & INDUSTRY BODIES",["MLIT (licensing, public-works rules) | JFTC (bid-rigging, Subcontract Act)","Labour standards (2024 overtime cap) | BOJ (rates)","Industry: Japan Federation of Construction Contractors (Nikkenren)","Competitors: Kajima, Taisei, Shimizu, Takenaka (unlisted), Daiwa House"],fc="#f7f8fb")
ax.text(1,63,"Obayashi supply chain: upstream inputs to end customer",fontsize=11,fontweight="bold",color=NAVY,va="top")
fig.text(0.01,0.005,"Names are typical industry participants; specific Obayashi contracts mostly not disclosed. *Rinyukai membership not verified.",fontsize=6.5,color="#666")
fig.savefig("assets/supply_chain.png",bbox_inches="tight")
