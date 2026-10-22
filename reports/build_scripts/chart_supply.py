import sys; sys.path.insert(0, '.')
from chartkit import *
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import textwrap
OUT = "/home/user/RF-Stuff/reports/figures/"
fig = plt.figure(figsize=(8.3, 11.0))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
def box(x, y, w, h, title, body, fill="#F1F3F7", edge="#D0D5DD", tcol=NAVY, bcol=INK2, wrap=58, fs=7.6, cols=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=0.8", fc=fill, ec=edge, lw=0.8))
    ax.text(x + 1.2, y + h - 1.2, title, fontsize=8.8, fontweight="bold", color=tcol, va="top")
    def fmt(items):
        lines = []
        for b in items:
            wr = textwrap.wrap(b, wrap)
            lines.append("• " + wr[0]); lines += ["   " + t for t in wr[1:]]
        return "\n".join(lines)
    if cols == 1:
        ax.text(x + 1.2, y + h - 3.6, fmt(body), fontsize=fs, color=bcol, va="top", linespacing=1.32)
    else:
        half = (len(body) + 1) // 2
        ax.text(x + 1.2, y + h - 3.6, fmt(body[:half]), fontsize=fs, color=bcol, va="top", linespacing=1.32)
        ax.text(x + w / 2 + 0.6, y + h - 3.6, fmt(body[half:]), fontsize=fs, color=bcol, va="top", linespacing=1.32)
def down(x, y0, y1):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>", mutation_scale=13, color=MUTED, lw=1.4))
ax.text(6, 98.6, "Supply-chain map: from landowners to J-REIT unitholders", fontsize=12.5, fontweight="bold", color=NAVY, va="top")
ax.text(6, 95.6, "UPSTREAM INPUTS", fontsize=8.5, fontweight="bold", color=BLUE, va="top")
box(6, 77.2, 45, 16.6, "1  Land, sites & existing buildings", ["Yaesu 1-chome East A/B redevelopment associations (TOFROM YAESU)", "Kyobashi 3-chome East association (Apr 2024); Shibuya 2-chome West", "Building sellers: Mizuho Bank (Otemachi sites), Blackstone (Hatchobori), Yellow Hat (Iwamotocho HQ)", "Condo landowners (~1,200 units added in 2025)"])
box(53, 77.2, 45, 16.6, "2  Approvals & public partners", ["Tokyo Metropolitan Government (rights-conversion approvals)", "National Strategic Special Zone status", "UR Urban Renaissance Agency (Bus Terminal Tokyo Yaesu)"])
box(6, 58.4, 45, 17.0, "3  Design & construction (outsourced)", ["Taisei — TOFROM block A; Otemachi Tower partner", "Obayashi — TOFROM YAESU TOWER (JV lead, co-specified agent)", "Kajima — Nakano Central Park South"])
box(53, 58.4, 45, 17.0, "4  Capital", ["Main banks: Mizuho, SMBC, MUFG", "Bonds incl. 36th sustainability bond; hybrids rated BBB+ (JCR)", "Issuer rating JCR 'A'; auditor EY ShinNihon", "JV partners: SC Asset/SCX (Thailand), Lendlease & Nippon Steel Kowa (Melbourne), SC Zeus Data Centers (Osaka), PT Farpoint (Jakarta), WHA–KW, Charter Hall/UBS"])
down(52, 57.6, 55.0)
ax.text(6, 54.6, "TOKYO TATEMONO GROUP — orchestrator, developer, landlord, operator", fontsize=8.5, fontweight="bold", color=BLUE, va="top")
box(6, 31.6, 92, 21.4, "Segments and operating subsidiaries (FY2025 operating income)", [
    "Building (Commercial Properties) ¥67.1bn: offices, retail, hotels, T-LOGI logistics, data centres — rent + sales to investors",
    "Residential ¥25.6bn: Brillia condos (landbank ~7,600 units); Tokyo Tatemono Amenity Support (condo management)",
    "Asset Service ¥11.5bn: Tokyo Tatemono Real Estate Sales (brokerage, resales); Nippon Parking / NPC24H (~90,000 spaces)",
    "Other ¥4.2bn: Tokyo Tatemono Resort (golf, onsen, hotels); TRIM (100%, manages JPR); TT Investment Advisors (private REIT); overseas JVs",
    "Building operations: Tokyo Fudosan Kanri, Tokyo Building Service, Prime Place, Expert Office",
    "Flagships: Otemachi Tower, Tokyo Square Garden, TOFROM YAESU (2026); next: Kyobashi 3-chome East (FY2029)",
    "Balance sheet: ¥1.54tn interest-bearing debt; rental portfolio fair value ¥1.66tn vs book ¥1.06tn"],
    fill=NAVY, edge=NAVY, tcol="white", bcol="#E6EBF5", wrap=60, fs=7.7, cols=2)
down(52, 30.8, 28.4)
ax.text(6, 28.0, "DOWNSTREAM: OPERATORS, END USERS, EXIT BUYERS", fontsize=8.5, fontweight="bold", color=BLUE, va="top")
box(6, 8.0, 29.5, 18.6, "5  Operators & anchors", ["Aman (Aman Tokyo, Otemachi Tower)", "Keio Dentetsu Bus (Bus Terminal Tokyo Yaesu)", "Nippon Medical School (TOFROM medical facility)", "Pia / Congres (theatre & conference)"], wrap=37, fs=7.4)
box(37.25, 8.0, 29.5, 18.6, "6  End users", ["Office tenants: Mizuho Bank HQ (Otemachi Tower); TOFROM YAESU tenants", "55 TOFROM retail stores (from 10 Sep 2026)", "Brillia buyers (avg ¥69m; family mix)", "NPC24H parkers; golf & onsen guests; overseas renters"], wrap=37, fs=7.4)
box(68.5, 8.0, 29.5, 18.6, "7  Exit buyers", ["Japan Prime Realty (8955): TT sole sponsor, 3.03% holder; manager TRIM", "TT Private REIT; private funds", "APA Group (Akihabara hotel)", "Star Mica HD (13.74%; pre-owned condo alliance)"], wrap=37, fs=7.4)
# recycle path: exit box bottom -> left gutter -> land box
ax.plot([83.25, 83.25, 2.6, 2.6], [7.6, 4.2, 4.2, 85.5], color=BLUE, lw=1.8, solid_joinstyle="round")
ax.add_patch(FancyArrowPatch((2.6, 85.5), (5.6, 85.5), arrowstyle="-|>", mutation_scale=13, color=BLUE, lw=1.8))
ax.text(5.0, 5.4, "Capital recycling: sale proceeds fund new land and redevelopment; TT keeps AM fees (TRIM/TTIA) and management income after exit",
        ha="left", fontsize=7.0, color=NAVY, fontweight="bold")
ax.text(50, 1.4, "Bargaining power is shifting to contractors (+5.1% construction costs) and lenders (BOJ 1.25%); TT controls the scarce inputs (land rights, approvals) and its exit channel (JPR).",
        ha="center", fontsize=6.9, color=INK2, style="italic")
fig.savefig(OUT + "fig11_supply_chain_map.png", dpi=220, facecolor="white")
print("ok")
