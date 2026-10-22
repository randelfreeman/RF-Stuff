import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from style import *
setup()
BASE = os.path.dirname(os.path.abspath(__file__))
fig = plt.figure(figsize=(11.0, 7.4)); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 110); ax.set_ylim(0, 74); ax.axis('off')
def box(x, y, w, h, title, body='', fc='#ffffff', ec=AXIS, tc=INK, fs=7.2, bfs=6.3, lw=0.9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.25,rounding_size=0.8', fc=fc, ec=ec, lw=lw))
    ax.text(x + 0.9, y + h - 0.9, title, fontsize=fs, fontweight='bold', color=tc, va='top', ha='left')
    if body: ax.text(x + 0.9, y + h - 3.1, body, fontsize=bfs, color=INK2 if tc == INK else '#dfe6f3', va='top', ha='left', linespacing=1.25)
def arrow(x1, y1, x2, y2, label=None, col=MUTED):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=9, color=col, lw=0.9, shrinkA=1, shrinkB=1))
    if label: ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.6, label, fontsize=5.6, color=MUTED, ha='center')
# column headers
for x, t in [(1, 'UPSTREAM INPUTS'), (31, 'ELIS (PRODUCT-AS-A-SERVICE)'), (63, 'CUSTOMERS (4 END-MARKETS)'), (94, 'END USERS')]:
    ax.text(x, 72.4, t, fontsize=8, fontweight='bold', color=BLUE)
# upstream column
up = [
 ('Fibres & raw materials', 'Cotton, polyester (incl. recycled)'),
 ('Textile & garment makers', 'External mills; names undisclosed.\nSourcing: Europe 37%, Asia 36%,\nAfrica ~14%, LatAm 7.5%'),
 ('Elis own manufacturing', 'Le Jacquard Français (FR); Kennedy\nHygiene (UK); garment plants in Estonia,\nBrazil, Mexico, Colombia, Malaysia'),
 ('Hygiene & well-being products', 'Dispensers, paper, soap, fountains;\nMalongo (coffee, "captive" partner)'),
 ('Laundry & traceability equipment', 'Tunnel washers, dryers, ironers, RFID;\n"captive"/oligopolistic suppliers (unnamed)'),
 ('Chemicals, energy & water', 'Detergents; gas & electricity\n(6-7% of revenue, layered hedges);\nmunicipal water / wastewater'),
 ('Vehicles & fuel; labour', '~11,800 vehicles; 58,445 employees;\nlabour ~60% of costs'),
]
y = 70.0; ys = []
for t, b in up:
    h = 7.4 if b.count('\n') >= 2 else 6.2
    box(1, y - h, 25, h, t, b); ys.append(y - h / 2); y -= h + 1.0
arrow(13.5, 70.0 - 6.2, 13.5, 70.0 - 6.2 - 0.9)  # fibres -> textile makers
# Elis column
box(31, 50.5, 27, 19.0, 'Elis operations', 'Central purchasing (PCO/PLO suppliers, 1-yr\nfixed textile prices) -> warehouses\n\n>373 laundries / processing centres\n(incl. cleanroom plants), 30-100 km from clients\n\n>6,000 routes a day, 5m km a week;\nclean delivered, soiled collected on same truck\n\nSales, key accounts, customer care (HiFi)', fc=NAVY, ec=NAVY, tc='#ffffff', fs=8, bfs=6.5)
box(31, 39.5, 27, 9.0, 'Specialty & circular services', 'Pest control (~€80m), cleanroom (~€275m),\nmedical waste; repair/refurbishment;\n>87% of used flat linen recycled', fc='#eef3fb', ec=BLUE)
for yy in ys: arrow(26.6, yy, 30.6, 60 if yy > 50 else 55)
# customers column
cust = [
 ('Healthcare ~30%', 'Hospitals, clinics, care homes; public tenders\n(France, UK, Brazil, Mexico federal system);\na leading German private healthcare group'),
 ('Hospitality 27%', 'Hotels & restaurants (France share >50%);\n€5-10 of linen per room vs €200+ room rate'),
 ('Industry ~26% [calc]', 'Food, chemicals & pharma, industrial services;\nsemiconductor multinationals (cleanroom)'),
 ('Trade & Services ~18% [calc]', 'Retail, services, facility managers;\nSodexo (German catering accounts)'),
]
y = 70.0; cys = []
for t, b in cust:
    box(63, y - 8.6, 26, 8.6, t, b); cys.append(y - 4.3); y -= 10.0
for cy in cys:
    arrow(58.6, 60, 62.6, cy + 0.6); arrow(62.6, cy - 0.8, 58.6, 56, col=AXIS)
ax.text(60.6, 67.0, '4-yr contracts,\nauto-renewal;\nretention ~94%', fontsize=5.8, color=MUTED, ha='center')
box(94, 44, 15, 22, 'End users', 'Hotel guests &\ndiners\n\nPatients, residents\n& care staff\n\nWorkers wearing\nuniforms / PPE\n\nVisitors, retail\nstaff')
for cy in cys: arrow(89.4, cy, 93.6, 55)
# stakeholders band
box(1, 2.6, 108, 11.6, 'Other stakeholders and competitive context', '', fc='#f6f7f9', ec=AXIS)
stake = [
 ('Shareholders', 'BWGI (25% standstill, 10 yrs);\nCPP Investments (anti-dilution ≥8%)'),
 ('Lenders', 'EMTN bonds, OCEANE 2029, USPP,\nRCF €870m (undrawn), NEU CP,\nreceivables securitisation'),
 ('Employees', '58,445 staff; European Works\nCouncil (28 members, 22 countries)'),
 ('Regulators', 'Environmental permits; French\nCompetition Authority (07-D-21);\nBrazil public-contract probes'),
 ('Industry bodies', 'AFEP, GEIST, ETSA'),
 ('Competitors', 'Cintas, UniFirst, Vestis (N. America);\nJohnson Service Group, Rentokil;\nlocal players & in-house laundries'),
]
x = 2.0
for t, b in stake:
    w = 17.2
    ax.text(x, 10.3, t, fontsize=6.8, fontweight='bold', color=INK)
    ax.text(x, 8.6, b, fontsize=5.9, color=INK2, va='top', linespacing=1.25)
    x += w + 0.8
ax.text(1, 0.6, 'Source: Elis FY2025 URD, CMD (27-May-2025), FY2025 and H1 2026 calls via ProntoNLP (see report citations); S&P Capital IQ (employees). Supplier names beyond those shown are not disclosed in permitted sources.', fontsize=5.8, color=MUTED)
fig.savefig(os.path.join(BASE, 'supply_chain.png')); print('ok')
