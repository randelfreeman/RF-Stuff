# -*- coding: utf-8 -*-
"""Full research report content for TOTO Ltd (5332 JP)."""
I = 'img/'
B = []
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def p(t): B.append(('p', t))
def bl(*t): B.append(('bullets', list(t)))
def tb(h, r, cap=None, w=None): B.append(('table', h, r, cap, w))
def img(path, cap, frac=1.0): B.append(('img', I + path, cap, frac))
def co(t): B.append(('callout', t))
def pb(): B.append(('pagebreak',))

# ------------------------------------------------------------------
h1('1. Investment Summary')
co('<b>Rating: BUY (moderate conviction, event-driven sizing). 12-month target ¥7,200 (+18% vs ¥6,097 close on 2 Oct 2026); probability-weighted value ~¥6,975 (+14%).</b> TOTO is no longer a toilet company with a ceramics hobby: in FY3/26 Advanced Ceramics (electrostatic chucks for NAND cryogenic etch) generated ¥28.9bn of operating profit on ¥67.4bn of sales (42.9% margin), exceeding the entire ¥670bn housing business for the first time. The stock has round-tripped from ¥9,500 (23 Jun 2026) to ¥6,097 on a Q1 miss, giving a second entry point into a business mix shift that the consolidated P&L still obscures.')
tb(['Market data (2 Oct 2026)', 'Value', 'Valuation', 'FY3/26A', 'FY3/27E', 'FY3/28E'],
   [['Share price', '¥6,097', 'P/E', '25.1x', '21.8x', '17.3x'],
    ['52-week range', '¥3,766 – ¥9,500', 'EV/Sales', '1.27x', '1.22x', '1.17x'],
    ['Shares outstanding (ex-treasury)', '~164.4m', 'EV/EBITDA', '10.6x', '9.8x', '8.1x'],
    ['Market cap', '~¥1.00tn (~US$6.7bn)', 'EV/EBIT', '17.4x', '15.6x', '12.0x'],
    ['Net cash (e)', '~¥65bn', 'Dividend yield', '1.8%', '2.0%', '2.1%'],
    ['Enterprise value (e)', '~¥937bn', 'Net debt/EBITDA', '-0.7x', '-0.7x', '-0.7x'],
    ['Consensus target (8 analysts)', '~¥7,785–7,955', 'ROE', '7.7%', '~8.6%', '~10.3%']],
   'Sources: company filings (FY3/26 results 30 Apr 2026; Q1 FY3/27 31 Jul 2026), Kabuyoho/Minkabu/TipRanks consensus; FY3/27E–FY3/28E are our estimates. (e) = estimate, balance sheet not directly verified — see Data Notes.', [3, 2.4, 2, 1.3, 1.3, 1.3])
h2('Thesis in five points')
bl('<b>Hidden compounder inside a mature franchise.</b> Ceramics OP has grown from ~¥9bn (FY3/22e) to ¥28.9bn (FY3/26) and is guided to ~58% of group OP in FY3/27. Replacement demand (~80% of segment sales per Palliser) and Lam Research\'s cryo-etch installed base (expected to triple in 3–5 years) underpin a multi-year growth runway; capacity +20% from Jan 2027 (Buzen) and a ~¥30bn (FY28) / reported ~¥80bn (5-year) investment programme.',
   '<b>Housing at a cyclical and structural trough, with self-help.</b> Japan new-build starts fell 12.9% in FY2025 to ~711k; China lost ¥6.9bn in FY3/26. But two China plants are closed (~¥7bn profit improvement targeted for FY3/27), US capacity +150% (Georgia), and an 8–13% Japan price increase lands 1 Dec 2026 — the largest in a decade.',
   '<b>Activist has already won the first round.</b> Palliser Capital (Feb 2026) asked for ceramics disclosure, more ceramics investment, housing/China restructuring and capital efficiency. TOTO adopted the substance on 30 Apr 2026 (Palliser statement, 7 May 2026). Round two — cross-shareholding sell-down, excess cash, balance-sheet efficiency (equity ratio 63.8%) — is the likely content of the next mid-term plan (STAGE3, ~Apr 2027).',
   '<b>Valuation reset.</b> At ¥6,097 the market implies ~¥615bn for ceramics (≈19x FY3/27E EBIT, ~15x FY3/28E) if housing is valued on the peer margin regression — not demanding for a ~43%-margin, sole/dual-source semiconductor consumable versus NGK Insulators at 22x forward P/E.',
   '<b>The bear case is real and cyclical, not existential.</b> FY3/24 showed ceramics OP can fall ~35% in a memory capex downturn; customer concentration (Lam) is high; Q1 FY3/27 showed shipment lumpiness. Our bear value of ~¥3,500 reflects a full memory downturn plus housing de-rating.')
h2('What has to go right / what would make us wrong')
tb(['Must go right (next 2–3 quarters)', 'Would change our view'],
   [['H1 FY3/27 (~30 Oct 2026) shows Q1 ESC shipment slip was timing, ceramics H1 OP ≥ ¥15bn', 'Ceramics H1 OP down y/y with no customer-timing explanation; guidance for ceramics sales (¥85.5bn) cut'],
    ['China returns to near break-even as plant closures flow through', 'China losses persist beyond FY3/27, implying further impairment'],
    ['Dec 2026 Japan price hike sticks (TOTO ~60% toilet share; LIXIL follows)', 'Volume loss > price; LIXIL/Panasonic do not follow'],
    ['STAGE3 plan (Apr 2027) adds capital-allocation targets: ROE ≥10–12%, cross-holding exit, buybacks', 'Cash hoarded, no ROE/cross-holding targets; Palliser disengages'],
    ['NAND WFE continues to recover (GS: $11bn/15bn/22bn for 2026/27/28)', 'Memory capex cut; TEL cryo-etch wins displace Lam/TOTO']], None, [1, 1])

# ------------------------------------------------------------------
h1('2. Layman\'s Guide: What TOTO Does and How It Makes Money')
p('<b>In one sentence:</b> TOTO makes the toilets, heated "Washlet" bidet seats, taps, bathtubs and vanity units that sit in roughly six out of ten Japanese bathrooms — and, in a small but very profitable side business, makes ultra-precise ceramic "chucks" that hold silicon wafers in place inside the machines that etch memory chips.')
tb(['Division', 'What it sells', 'Who pays', 'FY3/26 sales', 'FY3/26 OP', 'Share of OP'],
   [['Japan Housing Equipment', 'Toilets, Washlet, unit baths, kitchens, vanities, faucets; ~72% is remodelling/replacement', 'Plumbing wholesalers → contractors, homebuilders, remodelers, homeowners', '¥479.7bn (65%)', '¥20.3bn (4.2%)', '~36%'],
    ['Overseas Housing – China', 'Premium toilets/Washlet in mainland China', 'Distributors, developers', '¥53.8bn (7%)', '-¥6.9bn', 'loss'],
    ['Overseas Housing – Americas', 'Washlet, high-end toilets (NEOREST); plants in Georgia (US), Mexico', 'Plumbing distributors, showrooms, retail', '¥75.6bn (10%)', '~¥4.7bn', '~8%'],
    ['Overseas Housing – Asia/Oceania', 'Sanitary ware, faucets; Vietnam, Thailand, India plants', 'Distributors, hotels, developers', '¥54.9bn (7%)', '¥10.2bn', '~18%'],
    ['Advanced Ceramics (New Domain)', 'Electrostatic chucks (ESCs) for 3D NAND cryo-etch; aerosol-deposition chamber parts; LCD parts', 'Semiconductor equipment makers — principally Lam Research', '¥67.4bn (9%)', '¥28.9bn (42.9%)', '~51%'],
    ['Group', '', '', '¥737.4bn', '¥53.8bn (7.3%)', '100%']],
   'Segment OP before ~¥3bn of corporate costs/eliminations; share computed on segment total ¥56.8bn. China/Americas/Asia from FY3/26 results commentary; "Other overseas" (~¥5.7bn sales) not shown.', [2.2, 3.6, 3, 1.5, 1.5, 1])
bl('<b>How the toilet business makes money:</b> a mature, oligopolistic replacement market. Japanese toilets are replaced every ~15–20 years and Washlet seats every ~10; TOTO earns a premium price for brand and reliability, sells through wholesalers on standard trade credit, and supports demand via ~100 showrooms and a network of "Remodel Club" contractors. Margins are thin (~4%) because of high fixed costs, rising materials/labour and a shrinking new-build market.',
   '<b>How the ceramics business makes money:</b> an electrostatic chuck is the "table" inside an etch chamber that grips the wafer with static electricity and controls its temperature to within fractions of a degree, at –60°C to –100°C in cryogenic NAND etch. It wears out and is replaced roughly annually, so most revenue is recurring. TOTO has co-developed chucks with Lam Research since ~1990 and is reported to be the #2 global ESC maker; margins are >40%.',
   '<b>Why it matters:</b> 9% of sales now produce over half the profit — and the market values those two businesses very differently.')

# ------------------------------------------------------------------
h1('3. Historical Share-Price Catalysts (Moves >10%, 2021–2026)')
img('price.png', 'TOTO share price, key levels Feb 2021 – Oct 2026 (JPY). Reconstructed from annual OHLC and reported event closes; intermediate points are illustrative.')
tb(['Date', 'Move', 'Catalyst', 'Read-across'],
   [['Feb–Oct 2021', '¥7,380 → ¥4,995 (-32%)', 'Post-COVID housing peak unwinds; Evergrande/China property contagion fears (Nikkei: "TOTO plunges on China risk")', 'China was ~15% of sales and the growth engine — the start of a 4-year de-rating'],
    ['Jan–Jun 2022', '¥5,380 → ¥4,105 (-24%)', 'Material/energy inflation, China lockdowns, global growth-to-value rotation', 'Margin squeeze; FY3/23 OP fell 6%'],
    ['10 Jan 2023', 'Up to +10% intraday', 'China reopening hopes', 'Short-lived'],
    ['Jul–Aug 2023', 'Slide to ¥3,831 (3-yr low)', 'China property slump; weak China sales', '—'],
    ['30–31 Oct 2023', 'Sharp fall', 'FY3/24 OP guidance cut to ¥47bn; China OP guided -30% to ¥5.7bn (half plan)', 'First explicit China earnings reset'],
    ['Feb–Oct 2024', '¥3,642 → ¥5,530 (+52%)', 'China stimulus rally; early ceramics recovery', 'Proved China-beta still dominated the stock'],
    ['29 Oct 2024', '<b>-12.5%</b> (-¥614)', 'H1 FY3/25: China swung to a ¥4.4bn operating loss; ~¥34bn China impairment; NI guidance cut', 'Capitulation on China'],
    ['2–9 Apr 2025', 'To ¥3,269 (5-yr low)', 'US "Liberation Day" tariffs (Vietnam, Mexico, Thailand, Malaysia sourcing)', 'Low point of the cycle'],
    ['28 Apr 2025', 'Positive', 'FY3/25 results; ¥20bn (4.7%) buyback, later cancelled; China plant closures', 'First large buyback in years'],
    ['25 Aug 2025', '+8.4%', 'Americas plan: ¥100bn sales by FY3/31 (+40%); US local production >50%', '—'],
    ['Nov 2025 – Jan 2026', 'Steady re-rating', 'H1 FY3/26 ceramics OP ~¥12.9bn; AI/NAND narrative', 'Market starts to price ceramics'],
    ['22 Jan 2026', '<b>+11% intraday</b> (+8.8% close)', 'Goldman Sachs upgrade Neutral → Buy on NAND ESC thesis', 'Largest daily gain since Feb 2021 at the time'],
    ['17 Feb 2026', '+5% day; ~+40% YTD by late Feb', 'Palliser Capital discloses stake; "Value Enhancement Plan" (>55% upside, ~¥8,800 intrinsic)', 'Activism catalyses SOTP framing'],
    ['1 May 2026', '<b>Limit-up, ~+18%</b> to ¥6,425', 'Record FY3/26; ceramics disclosure; ¥30bn ceramics capex; DPS ¥110 → ¥120 guide; buyback', 'Record single-day gain'],
    ['19–23 Jun 2026', '<b>~+9–11%</b>; ATH ¥9,500', 'Nikkei: ~¥80bn 5-year chip-parts investment incl. 1nm-era R&D', 'Peak "AI beneficiary" multiple'],
    ['3 Aug 2026', '<b>-11.4%</b> to ¥6,209', 'Q1 FY3/27 miss (sales ¥168.6bn vs ~¥176.5bn cons.; EPS ¥42 vs ¥45.6); ESC shipment timing; Middle East (-¥3bn OP); yen strength', 'Momentum broken; broker target cuts (MS ¥5,900, Nomura ¥6,820)']],
   'Sources: Nikkei price history, Nikkei/Bloomberg/Japan Times/Kabutan/Zaikei reporting. Exact daily moves not all verifiable from primary exchange data.', [1.4, 1.5, 3.8, 2.4])

# ------------------------------------------------------------------
h1('4. Business Model, Key Drivers, Customers and Competitors')
h2('4.1 Key drivers')
tb(['Driver', 'Housing equipment', 'Advanced Ceramics'],
   [['Volume', 'Japan remodel (~¥347bn, ~72% of Japan sales) driven by ageing stock (~15–20yr replacement); new-build (¥133bn) tied to starts (711k in FY2025, -12.9%); overseas: US Washlet adoption, Asia urbanisation, China property', '3D NAND layer count (→ ~1,000 layers by 2030), cryo-etch tool installations (Lam), ESC replacement cycle (~1 year), logic etch AD-coated parts'],
    ['Pricing', 'Annual Japan list-price rises: Aug-23 (3–8%), Aug-24 (2–11%), Oct-25 (2–5%), Dec-26 (8–13%, Washlet ~10%). US +~10% Jun-2025 (tariffs)', 'Engineered, qualified-in parts; price set per tool generation; strong pricing given ~5-yr technology lead claimed by Palliser'],
    ['Mix', 'Washlet/NEOREST premium mix, remodel vs new-build, overseas high-end', 'Cryo-NAND ESC (highest margin) vs LCD parts; new AD parts for logic'],
    ['Costs', 'Brass/copper, resin, energy (kilns), logistics, wages (Japan labour shortage); tariffs on US imports', 'Alumina/AlN powders, yield, depreciation from new kilns'],
    ['Capex cycle', 'Strategic capex ¥175bn under STAGE2 (FY24–26): global ¥72bn, ceramics ¥29bn, domestic ¥32bn, IT ¥42bn', 'WFE cycle: SEMI 300mm fab equipment +18% (2026) / +14% (2027); GS NAND WFE $11bn/15bn/22bn (2026–28)'],
    ['Regulation', 'Japan building-code/energy rules (Apr 2025) depressed starts; water-efficiency standards favour premium fixtures; US tariffs', 'Export controls (China fabs), FEFTA designation of semiconductor parts as core sector']], None, [1.1, 3, 3])
h2('4.2 Customers, suppliers, competitors, geographies')
bl('<b>Customers (housing):</b> plumbing/building-material wholesalers (e.g. Hashimoto Sogyo, Watanabe Pipe — channel partners, TOTO-specific volumes not disclosed), homebuilders (Sekisui House, Daiwa House, Sumitomo Forestry, Iida Group), condo developers, remodel contractors (TOTO Remodel Club, TDY alliance with Daiken and YKK AP), home centres; overseas: US plumbing distributors/showrooms (e.g. Ferguson) and e-commerce, Asian distributors and hotel projects.',
   '<b>Customers (ceramics):</b> Lam Research (primary; co-development since ~1990; Supplier Excellence Award 2023 and 2024). Applied Materials and Tokyo Electron are potential/partial customers (not confirmed). End users: Samsung, SK hynix, Kioxia/SanDisk, Micron, YMTC (subject to export rules).',
   '<b>Suppliers:</b> ceramic raw materials (kaolin/ball clay, feldspar, silica), brass and copper alloys (faucets), resins (seats/lids), electronic components and PCBs (Washlet), packaging; for advanced ceramics, high-purity alumina and aluminium nitride powders (Tokuyama is the global AlN leader — TOTO\'s supplier list is not disclosed).',
   '<b>Competitors:</b> Japan — LIXIL (INAX; #2 in toilets), Panasonic Housing Solutions (Alauno), Takara Standard and Cleanup (kitchens/baths). Global — Kohler (private), Roca (private, owns Laufen), Geberit (Duravit is private), Masco (Hansgrohe/Delta), LIXIL (American Standard, Grohe), Villeroy & Boch (+Ideal Standard), Jomoo, Arrow Home, Huida, Hegii (China). ESC — Applied Materials and Lam in-house, Shinko Electric (JIC-owned since 2025), NGK Insulators, Kyocera, Niterra/NTK Ceratec, Entegris, Sumitomo Osaka Cement, MiCo (Korea), CoorsTek (private).',
   '<b>Geographies:</b> Japan ~65% of sales; Americas ~10%; China ~7% (from ~15% in FY3/22); Asia/Oceania ~7%; ceramics (shipped globally, mostly to US/Asian tool makers) ~9%.',
   '<b>Contracts and payment terms:</b> not disclosed in detail. Housing sales are spot/annual-price-list sales to wholesalers on Japanese trade-credit terms (typically 60–120 days incl. notes); ceramics sold under qualified-supplier agreements with OEMs; revenue recognised on shipment/delivery (relevant to the Q1 FY3/27 "timing" miss).')

# ------------------------------------------------------------------
h1('5. Macro and Micro Factors: Tailwinds and Headwinds')
tb(['Tailwinds', 'Headwinds'],
   [['AI-driven NAND upgrade cycle; cryo-etch tool base to triple in 3–5 yrs (Lam); WFE "low-$150bn" in 2026', 'Memory capex cyclicality — FY3/24 ceramics OP fell ~35% (e); single-customer concentration'],
    ['ESC replacement demand (~80% of segment revenue recurring per Palliser)', 'TEL entering cryogenic etch could shift chuck sourcing'],
    ['Japan remodel market ~¥8–9tn, ageing housing stock; Washlet replacement cycle', 'Japan housing starts at post-war lows (711k FY2025; NRI ~610k by 2040)'],
    ['Price increases (Dec 2026: 8–13%) in a ~60%-share oligopoly', 'Labour and materials inflation in Japan; Q1 FY3/27 Japan OP -46%'],
    ['China restructuring: ~40% capacity removed, ~¥7bn improvement targeted', 'China property deflation; local competitors (Jomoo, Arrow, Hegii) gaining at lower price points'],
    ['US Washlet adoption, Georgia plant (+150% capacity), Americas ¥100bn target', 'US tariffs on Vietnam (20%), Mexico, Thailand/Malaysia (Washlet sourcing)'],
    ['Weak yen supports overseas profit translation and ceramics exports', 'Yen strength after intervention (Aug 2026); Middle East disruption (-¥3bn Q1 OP)'],
    ['Corporate-governance reform in Japan (TSE P/B push, cross-holding unwind, activism)', 'Large stable-shareholder base slows change']], None, [1, 1])

# ------------------------------------------------------------------
h1('6. Competitive Position and Economic Moats')
p('TOTO is the Japanese category-defining brand ("Washlet" is a TOTO trademark that became the generic term). In Japan it holds ~60% of toilets against LIXIL; Japanese household penetration of warm-water bidet seats exceeds 80%. Overseas it is a premium niche brand with high awareness among travellers to Japan but small share against Kohler, American Standard and local champions. In ceramics, TOTO is reported as the #2 global ESC maker and a primary supplier for Lam\'s cryogenic dielectric etch tools.')
tb(['Moat category', 'Housing equipment', 'Advanced Ceramics', 'Strength'],
   [['Brand', 'Very strong in Japan (Washlet generic); premium perception in US/Asia', 'B2B — reputation for quality/yield with Lam', '<b>Strong</b>'],
    ['Hard assets', '~20 plants worldwide; kilns and casting know-how; logistics/showroom network', 'Proprietary sintering/bonding; new Buzen kiln, Nakatsu, Chigasaki R&D', 'Moderate–Strong'],
    ['Long-term contracts', 'None (price-list sales)', 'Qualified-supplier positions — designed into tool platforms for a generation', 'Moderate'],
    ['Network effect', 'Remodel Club contractor network, showroom footfall', 'Co-development loop with Lam', 'Weak–Moderate'],
    ['Regulatory / switching costs', 'Low for end user; moderate for builders (spec standardisation)', '<b>High</b>: requalification of a chuck takes 12–24 months; process-of-record risk for fabs', '<b>Strong (ceramics)</b>'],
    ['Oligopoly / monopoly', 'Japan duopoly (TOTO ~60%, LIXIL), Panasonic third', 'Top-4 ESC suppliers ~90% of market', '<b>Strong</b>'],
    ['Cash-flow predictability', 'High (replacement-led), but low margin', 'Medium — recurring replacement but WFE cyclical', 'Moderate'],
    ['Scalability', 'Low — capital-intensive, mature', 'Medium — capacity-constrained; each +20% requires a new kiln', 'Moderate'],
    ['Government interference risk', 'Low in Japan; tariffs in US; China policy', 'Export controls; FEFTA protects from foreign takeover', 'Moderate'],
    ['Bargaining power', 'Strong vs wholesalers; weak vs large homebuilders; price leadership in Japan', 'Balanced — Lam is concentrated buyer but TOTO is hard to replace', 'Moderate–Strong']],
   'Our assessment.', [1.6, 2.6, 2.6, 1.1])
p('<b>Product comparison.</b> TOTO\'s Washlet/NEOREST line carries a 20–40% price premium over LIXIL/INAX and Panasonic equivalents in Japan, justified by reliability, self-cleaning glaze (CeFiONtect), Tornado flush and service network. In the US, TOTO is positioned above Kohler/American Standard in bidet seats but with smaller distribution; Kohler out-spends it on marketing. In China, local brands now match features at 30–50% lower prices, eroding TOTO\'s premium — the root cause of the China impairment.')

# ------------------------------------------------------------------
h1('7. Supply Chain Map')
tb(['Stage', 'Activities', 'Stakeholders (named where known)', 'TOTO\'s power'],
   [['1. Raw materials', 'Kaolin, ball clay, feldspar, silica; brass/copper rod; resins; electronic components; high-purity Al2O3/AlN powders', 'Mining/minerals suppliers (domestic and imported); copper alloy mills; chemical makers; AlN/alumina powder makers (e.g. Tokuyama, Denka, Sumitomo Chemical — industry leaders, TOTO-specific not disclosed)', 'Moderate — commodity inputs; specialty powders more concentrated'],
    ['2. Manufacturing', 'Casting, glazing, kiln firing (sanitary); faucet machining; Washlet assembly; ceramic sintering, electrode embedding, bonding (ESC)', 'TOTO plants: Kitakyushu/Kokura, Chigasaki, Shiga, Oita (Nakatsu – TOTO Fine Ceramics), Buzen (Fukuoka); Vietnam (4 plants incl. faucet plant Vinh Phuc), Thailand, Malaysia, India (Halol), China (Zhangzhou, Dalian; Beijing/Shanghai closed 2025), USA (Morrow & Lakewood, GA), Mexico', 'High — vertically integrated, proprietary process'],
    ['3a. Distribution – housing', 'Wholesale, logistics, showroom, specification', 'Japan: plumbing/building wholesalers (e.g. Hashimoto Sogyo, Watanabe Pipe), home centres; US: plumbing distributors (e.g. Ferguson), showrooms, e-commerce; China/Asia: regional distributors', 'Strong in Japan (category leader); weaker overseas'],
    ['3b. Distribution – ceramics', 'Direct to OEMs, co-design, qualification', 'Lam Research (primary); potentially Applied Materials, Tokyo Electron', 'Balanced — concentrated customer'],
    ['4. Installers / integrators', 'Construction, remodelling, system-bath integration', 'Homebuilders (Sekisui House, Daiwa House, Sumitomo Forestry, Iida Group), general contractors, TOTO Remodel Club, TDY alliance (Daiken, YKK AP)', 'Moderate'],
    ['5. End customers', 'Homeowners, hotels, offices, public facilities; memory and logic fabs', 'Households; hospitality chains; Samsung, SK hynix, Kioxia/SanDisk, Micron, (YMTC)', 'Brand pull in Japan; derived demand in chips'],
    ['Competing suppliers at each stage', '', 'LIXIL, Panasonic, Takara Standard, Cleanup, Kohler, Roca, Geberit, Masco, V&B; ESC: AMAT/Lam in-house, Shinko (JIC), NGK, Kyocera, Niterra, Entegris, MiCo, CoorsTek', '']],
   'Named distribution partners/customers are industry participants identified from public sources; TOTO does not disclose a supplier or customer list.', [1.3, 2.2, 4, 1.6])

# ------------------------------------------------------------------
h1('8. Financial Analysis: Five-Year Review by Division and Geography')
img('sales_op.png', 'Net sales (bars, JPY bn) and operating margin (line). FY3/27E–FY3/29E are our estimates.', 0.95)
h2('8.1 Consolidated P&L (JPY bn, FY ending March)')
tb(['', 'FY3/22', 'FY3/23', 'FY3/24', 'FY3/25', 'FY3/26', '5-yr CAGR / comment'],
   [['Net sales', '645.3', '701.2', '702.3', '724.5', '737.4', '+3.4% (FY22–26)'],
    ['  growth', '—', '+8.7%', '+0.2%', '+3.2%', '+1.8%', 'Price-led, volume flat'],
    ['Gross profit', '236.9', '243.0', '239.0', '254.1', '262.6', 'GM 36.7% → 35.6%'],
    ['EBITDA', '80e', '79e', '75e', '83.5', '88.1', 'D&A ¥34–35bn'],
    ['  EBITDA margin', '12.4%e', '11.3%e', '10.7%e', '11.5%', '11.9%', ''],
    ['Operating income (EBIT)', '52.2', '49.1', '42.8', '48.5', '53.8', 'Record in FY3/26'],
    ['  OP margin', '8.1%', '7.0%', '6.1%', '6.7%', '7.3%', 'Trough FY3/24'],
    ['Ordinary income', 'n/a', '54.8', '51.5', '50.4', '60.7', 'FX & dividend income'],
    ['Net income (attrib.)', '40.1', '38.9', '37.2', '12.2', '40.3', 'FY3/25: ¥34.1bn China impairment'],
    ['EPS (¥)', '~237e', '~230e', '~220e', '~73e', '243.0', ''],
    ['DPS (¥)', '~90e', '~100e', '~100e', '100', '110', 'FY3/27 guide ¥120'],
    ['ROE', '~8.5%e', '~8.0%e', '~7.3%e', '~2.3%e', '7.7%', 'Target ≥12% by 2030']],
   'Source: TOTO kessan tanshin, results presentations (via secondary reporting). e = our reconstruction from reported growth rates/ratios; verify against EDINET before external use.', [2.4, 1, 1, 1, 1, 1, 2.6])
h2('8.2 Segment / geographic sales and operating profit (JPY bn)')
tb(['Segment', 'FY3/22e', 'FY3/23e', 'FY3/24e', 'FY3/25', 'FY3/26', 'Comment'],
   [['<b>Sales</b>', '', '', '', '', '', ''],
    ['Japan Housing', '~423', '~451', '~468', '~481', '479.7', 'Remodel ¥346.8bn (+1%); new-build ¥132.9bn (-3%)'],
    ['China', '~100', '~100', '~84', '~67', '53.8', '-46% from peak; 2 plants closed'],
    ['Americas', '~45', '~52', '~59', '70.5', '75.6', 'CAGR ~14%; Georgia plant'],
    ['Asia/Oceania', '~38', '~45', '~48', '~50', '54.9', 'Taiwan, Vietnam, India'],
    ['Advanced Ceramics', '~36', '~50', '~42', '50.3', '67.4', '+34% FY3/26; ¥85.5bn FY3/27 plan'],
    ['<b>Operating profit</b>', '', '', '', '', '', ''],
    ['Japan Housing', '~24', '~15', '~18', '~21.8', '20.3', 'Margin 4.2%; cost inflation > price'],
    ['China', '~14', '~8', '~4', '~-4', '-6.9', 'From best to worst region'],
    ['Americas', '~3', '~3.5', '~4.5', '~5.1', '~4.7', 'Tariffs, ramp-up costs'],
    ['Asia/Oceania', '~5', '~6', '~7', '~8.2', '10.2', 'Margin 18.6%'],
    ['Advanced Ceramics', '~9', '19.4', '~13', '20.4', '28.9', 'Margin 42.9%'],
    ['Corporate/elim.', '~-3', '~-3', '~-3', '~-2.8', '~-3.0', ''],
    ['<b>Group OP</b>', '52.2', '49.1', '42.8', '48.5', '53.8', '']],
   'FY3/22–FY3/24 segment/regional splits are reconstructions (old three-segment basis: Japan Residential / Global Residential / New Domain) and are approximate; FY3/25 partly derived from FY3/26 growth rates. From FY3/26 TOTO reports Housing (Japan + overseas) and Ceramics.', [2, 1, 1, 1, 1, 1, 3.2])
img('seg_mix.png', 'Segment OP mix: housing vs Advanced Ceramics, with ceramics share of segment OP.', 0.95)
h2('8.3 Trends and drivers')
bl('<b>Revenue:</b> group sales grew only ~3.4% p.a. over five years and almost entirely through price. Japan volumes are flat to down (new-build structurally shrinking), China halved, Americas and Asia compounded at ~10–14%, and ceramics nearly doubled.',
   '<b>Margins:</b> OP margin fell from 8.1% to 6.1% (FY3/24) on China collapse, materials and energy inflation, and the FY3/24 memory downturn; it recovered to 7.3% purely on ceramics. Housing margin has fallen from ~11% to ~4.2%.',
   '<b>Net income:</b> FY3/25 was hit by the ¥34.1bn China impairment; FY3/26 included a further ~¥15bn China restructuring loss but benefited from FX/non-operating gains (ordinary income ¥60.7bn vs OP ¥53.8bn) and cross-holding sales.',
   '<b>EBITDA</b> ~¥88bn; D&A broadly flat at ~¥34–35bn but will rise with the ceramics and US capex programme.')
img('ceramics.png', 'Advanced Ceramics: sales (bars) and OP margin (line). FY3/22e–FY3/24e reconstructed; FY3/27E–FY3/29E our estimates.', 0.95)
h2('8.4 Operational KPIs')
tb(['KPI', 'Latest', 'Trend / comment'],
   [['Japan remodel share of Japan housing sales', '~72% (¥346.8bn)', 'Rising — structural; supports pricing'],
    ['Japan housing starts (FY2025)', '~711k (-12.9%)', 'Post-war low; building-code change pulled demand forward'],
    ['Japan price increases', '2023, 2024, 2025, Dec-2026 (8–13%)', 'Accelerating — cost pass-through test'],
    ['Washlet cumulative shipments', '>60m (Aug 2022)', 'Japan household penetration >80%'],
    ['China sales / OP', '¥53.8bn / -¥6.9bn', '~40% of capacity closed; ~¥7bn improvement targeted'],
    ['Americas sales', '¥75.6bn (+7%)', 'Target ¥100bn by FY3/31; US local production >50%'],
    ['Ceramics sales / OP margin', '¥67.4bn / 42.9%', 'FY3/27 plan ¥85.5bn; Q1 +6% (timing)'],
    ['ESC capacity', '+20% from Jan 2027 (Buzen)', '~¥30bn capex to FY2028; reported ~¥80bn 5-year'],
    ['Capex intensity', '~¥36.5bn PP&E (5% of sales)', 'Rising with ceramics + US'],
    ['Overseas share of sales', '~33%', 'WILL2030 target >40%'],
    ['OP margin vs WILL2030 target', '7.3% vs ≥12%', 'Gap closing only via ceramics']], None, [2.4, 1.8, 3])

# ------------------------------------------------------------------
h1('9. Earnings Calls, Sentiment and the Latest Result')
h2('9.1 What management has focused on — sentiment tracker')
tb(['Event', 'Management focus', 'Sentiment (1–5)', 'Shift'],
   [['Q2 FY3/24 (30 Oct 2023)', 'China property, guidance cut, cost control', '2 – defensive', '↓'],
    ['Q2 FY3/25 (Oct 2024)', 'China loss, ¥34bn impairment, structural reform', '1.5 – capitulation', '↓'],
    ['FY3/25 (28 Apr 2025)', 'China plant closures, ¥20bn buyback, US capacity', '2.5 – reset', '↑'],
    ['Q1 FY3/26 (31 Jul 2025)', 'Weak Japan new-build, tariffs', '2 – cautious', '↓'],
    ['Aug 2025 Americas briefing', '¥100bn Americas target, US localisation', '3 – constructive', '↑'],
    ['H1 FY3/26 (31 Oct 2025)', 'Ceramics surge, China reform near-complete; FY OP guide trimmed to ~¥50bn', '3 – mixed', '→'],
    ['Q3 FY3/26 (30 Jan 2026)', 'Ceramics drives 9M OP +2%', '3.5 – improving', '↑'],
    ['FY3/26 (30 Apr 2026)', 'Record OP, ceramics disclosure, capex, dividends, capital efficiency (post-Palliser)', '4.5 – confident', '↑↑'],
    ['Q1 FY3/27 (31 Jul 2026)', 'ESC shipment timing, Middle East, Japan cost; full-year guide held; Dec price hike', '3 – "on track" but defensive', '↓']],
   'Our qualitative scoring based on disclosed results and press coverage of briefings; full transcripts not available to us.', [2, 4, 1.6, 0.6])
p('<b>Theme migration:</b> 2023–24 was about China damage control; 2025 about restructuring and the Americas; from H2 2025 the narrative became ceramics/AI-NAND; after Palliser (Feb 2026) management adopted capital-efficiency language (segment disclosure, ROE, returns). The Q1 FY3/27 tone was steadier than the share price implied — guidance unchanged.')
h2('9.2 Latest result: Q1 FY3/27 (Apr–Jun 2026, reported 31 Jul 2026)')
tb(['Item', 'Actual', 'y/y', 'Consensus', 'Variance'],
   [['Net sales', '¥168.6bn', '+1.7%', '~¥176.5bn', '<b>-4.5% miss</b>'],
    ['Operating income', '¥8.07bn', '-1.6%', '~¥9.5bn (e)', '~-15% miss (e)'],
    ['Ordinary income', '¥9.37bn', '+7.3%', 'n/a', 'FX gain ¥1.1bn'],
    ['Net income', '¥6.9bn', '+9.5%', 'n/a', ''],
    ['EPS', '¥42.0', '+~11%', '¥45.6', '<b>-8% miss</b>'],
    ['Ceramics sales / OP', '~¥15.9bn / ~¥6.5bn', '+6% / +10%', '', 'Shipment timing'],
    ['Housing OP (incl. corporate)', '~¥1.6–2.2bn', 'Japan -46%', '', 'Middle East ~-¥3bn']], None, [2, 1.6, 1, 1.4, 1.6])
bl('<b>Drivers:</b> ceramics grew but slower than the +27% full-year plan because of chuck shipment timing; Japan housing profit almost halved on procurement/labour costs and weak new-build; overseas housing OP -9% (Middle East order suspension, tariffs).',
   '<b>Margins:</b> group OPM 4.8% (Q1 seasonally weakest). Ceramics margin ~41%.',
   '<b>Guidance:</b> FY3/27 unchanged — sales ¥785bn, OP ¥60bn (+11.6%), NI ¥46bn, EPS ¥279.8, DPS ¥120. Q1 progress 13.5% of OP guide is below the ~18–20% normal pattern. Consensus (~¥62bn OP; EPS ~¥295) sits above guidance — downside risk to consensus, not necessarily to guidance.',
   '<b>Balance sheet flags:</b> none disclosed; watch ceramics inventory (shipment slip) and working capital ahead of the 1 Dec price rise (pre-buying in Q3, payback in Q4).',
   '<b>Market reaction:</b> -11.4% on 3 Aug. Combined with the ~¥9,500 June peak, this shows the stock was priced for uninterrupted ceramics acceleration; a modest timing slip removed ~¥140bn of value. That is a signal of momentum ownership — and of the opportunity if H1 confirms the slip was timing.')

# ------------------------------------------------------------------
h1('10. Earnings Forecasts: FY3/27E–FY3/29E')
tb(['JPY bn', 'FY3/26A', 'FY3/27E', 'FY3/28E', 'FY3/29E', 'Key assumptions'],
   [['Ceramics sales', '67.4', '77.5', '95.0', '110.0', '+15% / +23% / +16%: NAND cryo upgrade; Buzen +20% capacity Jan-27'],
    ['Ceramics OP (margin)', '28.9 (42.9%)', '32.5 (42%)', '40.4 (42.5%)', '46.2 (42%)', 'Pricing holds; depreciation step-up absorbed'],
    ['Japan housing sales', '479.7', '485', '495', '500', 'Dec-26 price +8–13% offsets ~-5–7% volume'],
    ['Japan housing OP', '20.3', '17.0', '22.0', '23.0', 'FY27 hit by costs/Q1; FY28 full price benefit'],
    ['China OP', '-6.9', '-1.5', '+1.5', '+2.5', '~¥7bn restructuring benefit (partial)'],
    ['Americas OP', '~4.7', '5.0', '6.0', '7.0', 'Tariff pass-through; Georgia utilisation'],
    ['Asia/Oceania OP', '10.2', '11.0', '12.0', '13.0', 'Mid-single-digit growth'],
    ['Corporate/other', '~-3.5', '-3.8', '-4.0', '-4.2', ''],
    ['<b>Group sales</b>', '737.4', '765', '800', '833', 'Below ¥785bn guide in FY27'],
    ['<b>Group OP</b>', '53.8', '60.0', '78.0', '87.5', 'In line with guide FY27'],
    ['OP margin', '7.3%', '7.8%', '9.8%', '10.5%', ''],
    ['Non-operating, net', '+6.9', '+4.0', '+3.0', '+3.0', 'Dividends, interest; FX neutral'],
    ['Extraordinary, net', '~-9', '+1.0', '0', '0', 'Cross-holding gains vs restructuring'],
    ['Tax rate', '~30%', '29%', '29%', '29%', ''],
    ['<b>Net income</b>', '40.3', '45.7', '57.0', '63.8', ''],
    ['Avg shares (m)', '165.7', '163.5', '162.0', '161.0', 'Buybacks ~1% p.a.'],
    ['<b>EPS (¥)</b>', '243.0', '<b>280</b>', '<b>352</b>', '<b>396</b>', 'Cons.: ¥295 / ¥353 / n/a'],
    ['DPS (¥)', '110', '120', '140', '160', 'Payout ~40–45%']],
   'Our estimates. Financing costs negligible (net cash). Biggest swing factor: ceramics sales — each ±10% = ±~¥3.5bn OP (±~¥15/share).', [2, 1.2, 1.2, 1.2, 1.2, 4])
bl('<b>Industry growth:</b> Japan housing equipment market flat to -1% real; Americas +5–7%; NAND etch equipment +20–30% p.a. 2026–28.',
   '<b>Market share:</b> stable in Japan; small gains in US; ceramics share held (risk: TEL cryo-etch).',
   '<b>Price/cost:</b> Dec-26 price rise worth ~¥25–35bn annualised gross; ~60% offset by cost inflation/volume.',
   '<b>Operating leverage:</b> ceramics incremental margin ~40%; housing incremental ~25% on price-led growth.',
   '<b>Dilution:</b> none (no converts/meaningful SBC); buybacks reduce share count ~1% p.a.')

# ------------------------------------------------------------------
h1('11. Capital Structure, Debt and Liquidity')
tb(['Item (Mar 2026)', 'Value', 'Comment'],
   [['Equity ratio', '63.8%', 'Reported — very conservative'],
    ['Total equity (e)', '~¥530bn', 'Implied from ROE 7.67% and NI ¥40.3bn'],
    ['Total assets (e)', '~¥830bn', 'Implied from equity ratio'],
    ['Cash & equivalents (e)', '~¥110bn', 'Palliser cites ~¥76bn "excess cash"'],
    ['Interest-bearing debt incl. leases (e)', '~¥45bn', 'Mostly local borrowings/leases; no material bond maturities identified'],
    ['Net cash (e)', '~¥65bn', 'Net debt/EBITDA ≈ -0.7x'],
    ['Investment securities / cross-holdings (e)', '~¥60–76bn', '~11% of net assets FY24; target <10% FY25, <5% by FY30'],
    ['Interest cost', '<¥1bn', 'Interest cover >50x'],
    ['Credit rating', 'R&I: A+ area (to verify)', 'No covenants of note expected'],
    ['Seasonal working capital', 'Moderate', 'Q3 build ahead of Dec price rise']],
   'Balance-sheet line items could not be retrieved directly from the FY3/26 filing in this research environment; (e) items are estimates derived from reported ratios and third-party commentary and should be verified. Conclusions (net cash, under-levered) are robust to the uncertainty.', [2.5, 1.6, 4])
p('<b>Assessment:</b> TOTO is materially under-levered. A move to an equity ratio of ~50% (still conservative) would free ~¥110bn of capacity; together with cross-holdings (~¥60–76bn) and excess cash, TOTO could return ~¥200bn (~20% of market cap) over 3–4 years without impairing its rating or ceramics capex. This is the core of the "round two" activist agenda.')

# ------------------------------------------------------------------
h1('12. Valuation: Peers, History and Regression')
h2('12.1 Peer comparison')
tb(['Company', 'Ticker', 'Listed', 'Mkt cap (US$bn)', 'EV/Sales', 'EV/EBITDA', 'EV/EBIT', 'P/E (fwd)', 'EBITDA mgn', 'EBIT mgn', 'Sales g', 'ND/EBITDA'],
   [['<b>TOTO</b>', '5332 JP', 'TSE', '6.7', '<b>1.27x</b>', '<b>10.6x</b>', '<b>17.4x</b>', '<b>21.8x</b>', '11.9%', '7.3%', '+1.8%', 'net cash'],
    ['LIXIL', '5938 JP', 'TSE', '3.1', '0.66x', '9.0x', '~26x', '57x (t)', '~7%', '2.5%', '+0.4%', '~4x'],
    ['Takara Standard', '7981 JP', 'TSE', '1.1', '0.41x', 'n/a', '5.4x', '13.8x', 'n/a', '7.5%', 'n/a', 'net cash'],
    ['Cleanup', '7955 JP', 'TSE', '0.2', '~0.15x', 'n/a', 'n/a', '8.7x', 'n/a', '2.9%', 'n/a', 'net cash'],
    ['Rinnai', '5947 JP', 'TSE', '3.4', '0.75x', '5.3x', '~7x', '13.6x', '14.1%', '10.7%', 'n/a', 'net cash'],
    ['Geberit', 'GEBN SW', 'SIX', '23', '6.9x', '23.5x', '~29x', '29.8x', '29.4%', '~24%', '+2.5%', '~1.0x'],
    ['Masco', 'MAS US', 'NYSE', '13.4', '2.1x', '11.6x', '~12.5x', '14.6x', '~19%', '16.8%', '-3%', '~1.9x'],
    ['Fortune Brands Innov.', 'FBIN US', 'NYSE', '4.9', '1.71x', '16.2x', '10.9x adj', '12.7x', '~19%', '15.7% adj', '-3.2%', '2.9x'],
    ['Villeroy & Boch', 'VIB3 GY', 'XETRA', '0.6', '0.47x', '4.4x', '~7x', 'n/m', '~11%', '6.8%', '+1.8%', '~1x'],
    ['Arrow Home', '001322 CH', 'SZSE', '0.9', 'n/a', 'n/a', 'n/a', '~136x (t)', 'n/a', '~1%', '-9.2%', 'n/a'],
    ['Huida Sanitary', '603385 CH', 'SSE', '0.3', 'n/a', 'n/a', 'loss', 'n/m', 'n/a', '-6.4%', '-15%', 'n/a'],
    ['NGK Insulators', '5333 JP', 'TSE', '11', '~2.5x', '12.0x', '~17x', '22.3x', '~21%', '14.2%', 'n/a', 'low'],
    ['Kyocera', '6971 JP', 'TSE', '30–34', '~1.1x', '7.8x', '~20x', '16.7x', '~13%', '5.2%', '+2.8%', 'net cash'],
    ['Niterra', '5334 JP', 'TSE', '12.5', '~2.3x', '9.5x', '~12x', '~16x', '~24%', '18.9%', 'n/a', 'net cash'],
    ['Ferrotec', '6890 JP', 'TSE', '~1.0', '~1.15x', '7.0x', '~13x', '9.1x', '~16%', '8.8%', '+4%', '~1x'],
    ['MiCo', '059090 KS', 'KOSDAQ', '0.35', 'n/a', 'n/a', 'n/a', '~16–18x', 'n/a', '~10%', 'n/a', 'n/a'],
    ['Kohler', '—', 'Private', '—', '', '', '', '', '', '', '', ''],
    ['Roca (incl. Laufen)', '—', 'Private', '—', '', '', '', '', '', '', '', ''],
    ['Duravit', '—', 'Private', '—', '', '', '', '', '', '', '', ''],
    ['Jomoo / Hegii', '—', 'Private', '—', '', '', '', '', '', '', '', ''],
    ['Panasonic Housing Solutions', '(6752 JP parent)', 'Subsidiary', '—', '', '', '', '', '', '', '', ''],
    ['Shinko Electric (ESC)', '(delisted 2025)', 'Private (JIC)', '—', '', '', '', '', '', '', '', ''],
    ['CoorsTek', '—', 'Private', '—', '', '', '', '', '', '', '', '']],
   'Peer data from company releases and data aggregators (Jul–Sep 2026; mixed dates); several EV/EBITDA and margin figures derived (~). TOTO EV/EBITDA on FY3/26A; P/E on our FY3/27E. Treat peer figures as indicative.', [2.2, 1.3, 1, 1, 0.9, 1, 1, 1, 0.9, 0.9, 0.8, 0.9])
h2('12.2 TOTO versus its own history')
tb(['Metric', '5-/10-yr low', '5-/10-yr high', 'Median / average', 'Current', 'Read'],
   [['P/E (trailing)', '14.0x (Mar 2025)', '54x (2025, impairment-distorted)', '~28x (5-yr avg)', '25.1x', 'Fair'],
    ['P/E (forward)', '~16x', '~35x', '~22x', '21.8x', 'Fair'],
    ['EV/EBITDA', '6.1x (Dec 2024)', '42x (10-yr)', '13.7x (10-yr median)', '10.6x', 'Cheap vs history'],
    ['P/B', '1.36x (Dec 2023)', '~3.0x (2021)', '~2.0x', '~1.9–2.0x', 'Fair'],
    ['Dividend yield', '~1.3%', '~2.9%', '~2.0%', '2.0%', 'Fair']],
   'Sources: companiesmarketcap, GuruFocus (TOTDY), YCharts; our calculations.', [1.5, 1.6, 2, 1.7, 1, 1.2])
h2('12.3 Regression: EV/Sales vs EBIT margin')
img('regression.png', 'EV/Sales vs latest-FY EBIT margin for 12 listed peers (building products and technical ceramics). Dashed = all peers; dotted = ex-Geberit.', 0.95)
p('<b>Result.</b> Across 12 listed peers EV/Sales = 0.225 × EBIT margin – 0.84 (R² 0.70); excluding the Geberit outlier EV/Sales = 0.124 × margin – 0.04 (R² 0.75). At TOTO\'s consolidated 7.3% margin the regressions imply 0.81x–0.87x EV/Sales versus an actual 1.27x: on a consolidated basis TOTO screens <b>~45–55% expensive</b>.')
p('<b>Why the consolidated read is misleading — the SOTP regression.</b> Valuing the housing segment alone on the ex-Geberit line (4.2% margin → 0.48x sales → ~¥320bn EV) leaves ~¥615bn of EV for ceramics: ~9x ceramics sales, ~21x FY3/26 EBIT, ~19x FY3/27E and ~15x FY3/28E EBIT. For a 43%-margin, high-switching-cost consumable growing 15–25% p.a., that is reasonable against NGK (~17x EBIT, 14% margin) and Niterra (~12x, 19% margin). <b>Verdict: expensive as a housing company, fair-to-cheap as a SOTP.</b> The re-rating thesis therefore depends on investors continuing to capitalise ceramics separately — which better disclosure (Palliser\'s ask) supports.')
h2('12.4 Sum-of-the-parts (12-month target derivation)')
tb(['Component', 'Metric', 'Multiple', 'Value (¥bn)', '¥/share', 'Rationale'],
   [['Advanced Ceramics', 'FY3/28E EBIT ¥40.4bn', '18x EV/EBIT', '727', '4,460', 'Discount to NGK on concentration; premium on margin/growth'],
    ['Housing equipment', 'FY3/28E EBIT ¥41.0bn', '9x EV/EBIT', '369', '2,264', 'In line with Rinnai/Masco-ex-premium; China drag'],
    ['Corporate costs', '-¥4.0bn', '9x', '-36', '-221', ''],
    ['Net cash (e)', '', '', '65', '399', ''],
    ['Cross-holdings, after tax (e)', '', '', '45', '276', ''],
    ['<b>Equity value</b>', '', '', '<b>1,170</b>', '<b>~7,180</b>', '÷ ~163m shares'],
    ['Cross-check: P/E', 'FY3/28E EPS ¥352', '20.5x', '', '7,216', 'Peer blend NGK 22x / Japan housing 14x'],
    ['<b>12-month target</b>', '', '', '', '<b>¥7,200</b>', '+18% upside']], None, [2, 1.8, 1.2, 1, 1, 3])

# ------------------------------------------------------------------
h1('13. M&A: Industry Deals, Takeover Potential and Takeout Multiples')
h2('13.1 Comparable transactions (2021–2026)')
tb(['Date', 'Target', 'Acquirer', 'Value', 'EV/Sales', 'EV/EBITDA'],
   [['Sep 2023 (closed early 2024)', 'Ideal Standard (ops)', 'Villeroy & Boch', '~€600m', '~0.81x', '8.1x (5.5x post-synergy)'],
    ['Jun 2023', 'Emtek/Schaub + Yale/August residential', 'Fortune Brands (from ASSA ABLOY)', '~$800m', '~2.3x', 'n/a'],
    ['Feb 2022', 'Elkay Manufacturing', 'Zurn (all-stock)', '$1.56bn', 'n/a', '14.2x (9.8x post-synergy)'],
    ['Late 2021', 'EZ-Flo International', 'Reliance Worldwide', '$325m', 'n/a', '12x (~7x post-synergy)'],
    ['Aug 2023', 'Bradley Corp.', 'Watts Water', '$303m', '~1.5x', '<8x post-synergy'],
    ['Sep 2024', 'Kichler Lighting', 'Kingswood Capital (from Masco)', '~$125m', 'n/a', 'n/a (Masco paid ~$550m in 2018)'],
    ['Dec 2023', 'KLAFS (saunas)', 'Kohler (from Egeria)', 'n/d', '', ''],
    ['May 2024', 'Kohler Energy (majority)', 'Platinum Equity', 'up to ~$3bn', '', ''],
    ['2021', 'Royo bathroom furniture; Sanit', 'Roca', 'n/d', '', ''],
    ['Jan–Jul 2025', 'Fujitsu General', 'Paloma Rheem', '~¥256bn', 'n/a', '39% premium (6-m avg)'],
    ['Dec 2023 – Jun 2025', 'Shinko Electric (ESCs, substrates)', 'JIC consortium (JIC/DNP/Mitsui Chem.)', '~¥685–700bn', '~3x (e)', '~12–13x (e)'],
    ['2022', 'CMC Materials', 'Entegris', '~$6.5bn', '~5.4x', '~17x (e)'],
    ['2020', 'Permasteelisa', 'Atlas Holdings (from LIXIL)', 'undisclosed', '', '']],
   'Sources: company releases and press (Börsen-Zeitung, Cleary Gottlieb, Watts 8-K, JIC). (e) = our estimate from reported financials.', [1.8, 2.2, 2.4, 1.2, 0.9, 1.8])
h2('13.2 TOTO\'s own acquisitions/investments (2016–2026)')
tb(['Date', 'Target / project', 'Type', 'Cost', 'Multiple / outcome'],
   [['Jul 2022', 'Vietnam 4th sanitary plant', 'Greenfield', 'n/d (~1m units/yr)', 'Successful — Asia OP +24% FY3/26'],
    ['Mar 2024', 'Vinh Phuc (Vietnam) faucet plant', 'Greenfield', '~¥10bn', 'Ramping'],
    ['Nov 2024 / 2025', 'Morrow, Georgia (US) plant', 'Greenfield', 'US$224m (~¥30bn)', '+150% US capacity'],
    ['Apr 2025', 'China restructuring (Beijing, Shanghai closures)', 'Exit', '~¥15bn extraordinary loss (+¥34bn prior impairment)', 'Value-destructive legacy'],
    ['Dec 2025 – Apr 2028', 'Buzen ESC kiln, Chigasaki R&D (~¥17bn), Nakatsu', 'Greenfield', '~¥30bn (to FY2028); ~¥80bn 5-yr reported', 'High-return (segment ROIC well above WACC)'],
    ['2016–2026', 'Acquisitions of companies', 'M&A', 'None material identified', 'TOTO is an organic grower']],
   'Pre-2016 consolidations (TOTO Washlet Techno 2007, Pagette 2009, TOTO Sanitechno 2011, TOTO Thailand 2013) for context.', [1.5, 2.8, 1, 2.2, 2.6])
h2('13.3 Is TOTO a takeover target?')
tb(['Pros', 'Impediments'],
   [['Under-levered balance sheet (equity ratio 64%, net cash) — LBO-able housing cash flows', 'FEFTA: semiconductor parts are a "core" sector — foreign bidders face prior screening'],
    ['Visible SOTP gap; ceramics asset scarce (Shinko taken private by JIC at ~12–13x EBITDA)', 'Stable shareholders: life insurers (~9%), employees, Japanese trust banks; Morimura-group culture'],
    ['Japan M&A climate (METI guidelines, record take-privates, activism)', 'Size (~US$7bn equity) and conglomerate structure — buyers want one half, not both'],
    ['Activist presence (Palliser) can catalyse a strategic review', 'Management/brand heritage (founded 1917); no history of M&A; likely to resist hostile approach'],
    ['Strategic logic for a ceramics carve-out to JIC/Japanese consortium or NGK/Kyocera', 'Lam Research dependency — buyer must underwrite customer change-of-control']], None, [1, 1])
p('<b>Probability of whole-company takeover in 24 months: low (~5–10%).</b> More plausible special-situation paths: (1) ceramics IPO/spin or minority sale (10–15%); (2) a large buyback/cross-holding unwind in STAGE3 (50%+). <b>Indicative takeout multiples:</b> whole company at 13–14x FY3/27E EBITDA (~¥1.25–1.35tn EV, ¥8,000–8,600/share, +30–40%); ceramics alone at 12–15x EBITDA / 18–22x EBIT (Shinko/CMC precedents and growth premium) = ¥600–800bn; housing at 8–10x EBITDA (V&B/Ideal Standard, Watts/Bradley).')

# ------------------------------------------------------------------
h1('14. Management Assessment')
tb(['Executive', 'Role / tenure', 'Track record', 'Skin in the game'],
   [['Shinya Tamura', 'President & Representative Director since Apr 2025 (age ~58)', 'Career TOTO; ran US and Vietnam subsidiaries (Vietnam capacity build-out successful); tasked with China rebuild; first year delivered record OP and adopted Palliser plan', 'Negligible personal stake (typical); pay ~¥172m incl. bonus (reported)'],
    ['Noriaki Kiyota', 'Chairman since Apr 2025; President Apr 2020 – Mar 2025', 'Launched WILL2030 (2021); presided over China collapse and ¥34bn impairment but also ceramics rise and US investment', 'Negligible; ~¥139m pay (reported)'],
    ['Tomoyuki Taguchi', 'Senior Managing Exec. Officer & CFO; Director', 'Led ¥20bn buyback (2025), segment disclosure upgrade (2026)', 'Negligible'],
    ['Ryosuke Hayashi', 'Senior Managing Exec. Officer & CTO; Director', 'Oversees business divisions incl. Advanced Ceramics; ceramics OP 3x under watch', 'Negligible'],
    ['Hiroshi Masumoto', 'Head of Ceramics Business Division', 'Ceramics capacity expansion; Lam supplier awards', 'n/d'],
    ['Madoka Kitamura', 'Former Chairman (President 2014–2020); now senior adviser', 'Approved China expansion era', '—']],
   'Sources: TOTO press releases (31 Jan 2025, 25 Feb 2026), annual securities reports via secondary sources. Pay figures reported, not verified against the yuho.', [1.5, 2.2, 3.8, 1.8])
bl('<b>Archetype:</b> professional, lifetime-employee managers in a 109-year-old company; no founder or controlling family. Implication: continuity and risk aversion — good for the franchise, slow on capital efficiency. External pressure (Palliser, TSE) is what moved capital allocation.',
   '<b>Capital allocation:</b> mixed. <i>Good:</i> long-term commitment to ceramics R&D (since 1976) now paying off; Vietnam/US greenfields; first sizeable buyback (¥20bn, cancelled). <i>Poor:</i> China over-investment (Beijing/Shanghai plants) leading to ~¥49bn of impairment/restructuring; persistent over-capitalisation (equity ratio 64%, cross-holdings).',
   '<b>ROE trend:</b> ~8.5% (FY3/22e) → ~7.3% (FY3/24e) → ~2.3% (FY3/25e) → 7.7% (FY3/26) → ~8.6% guided; WILL2030 target ≥12%. ROIC on ceramics is far above WACC; housing ROIC ~3–4%, below WACC.',
   '<b>Red flags:</b> no related-party issues or accounting concerns identified. Compensation is moderate (bonus capped at ~0.6% of prior-year OP; little equity-linked pay — misaligned with share-price outcomes). Recurring product-safety recalls (Washlet fire risk series, faucets). Strategy is stable rather than pivot-prone; the 2026 "AI" framing came from an activist, not from promotional management.',
   '<b>Recent changes:</b> President change Apr 2025 (Kiyota → Tamura); 11 new executive officers and two R&D "Fellows" from Apr 2026; board cut from 13 to 10 at the June 2026 AGM (50% outside directors).')

# ------------------------------------------------------------------
h1('15. Board of Directors')
tb(['Director', 'Position', 'Independent', 'Board tenure', 'Background / affiliations'],
   [['Noriaki Kiyota', 'Chairman, Chair of the Board', 'No', 'Long-serving (President 2020–25)', 'Career TOTO'],
    ['Shinya Tamura', 'President', 'No', 'Director since ≤2023', 'Career TOTO; ex-head of US and Vietnam subsidiaries'],
    ['Tomoyuki Taguchi', 'Director, CFO', 'No', 'n/d', 'Career TOTO; finance, legal, HR'],
    ['Ryosuke Hayashi or Naomiki Takeuchi', 'Director (inside)', 'No', 'n/d', 'Career TOTO (to confirm against 2026 AGM notice)'],
    ['Junji Tsuda', 'Outside director', 'Yes', 'Several years', 'Former Chairman, Yaskawa Electric (to verify)'],
    ['Kenji Yoshida', 'Outside director', 'Yes', 'New – Jun 2026', 'n/d'],
    ['Masayuki Yoshioka', 'Director, full-time Audit & Supervisory Committee member', 'No', 'n/d', 'Career TOTO'],
    ['Yukari Ienaga', 'Outside director, A&S Committee', 'Yes', 'n/d', 'n/d'],
    ['Chiho Naganuma', 'Outside director, A&S Committee', 'Yes', 'n/d', 'n/d'],
    ['Hidekazu Horikoshi', 'Outside director, A&S Committee', 'Yes', 'New – Jun 2026', 'n/d']],
   'Company with an Audit & Supervisory Committee. Post-23 Jun 2026 AGM: 10 directors, 5 independent. n/d = not determinable from sources available to us — complete from the 2026 Notice of Convocation before external use.', [2, 2.2, 0.9, 1.6, 3])
h3('Board changes, 2021–2026')
bl('Jun 2025: Naomiki Takeuchi joins (inside). Madoka Kitamura and Satoshi Shirakawa relinquish representative rights (Apr 2025) and step back to adviser roles.',
   'Jun 2026: Articles amended to reduce board size; board shrinks 13 → 10. Outside directors Shigenori Yamauchi and Yasushi Marumori retire; Kenji Yoshida and Hidekazu Horikoshi join. Independence rises to 50%. President re-elected with ~94% support (reported).',
   '2021–2024 changes: routine rotation of inside directors; not fully reconstructable from available sources.')

# ------------------------------------------------------------------
h1('16. Shareholders, Activism and Short Interest')
tb(['#', 'Shareholder', 'Type', '% (Mar 2026, approx.)'],
   [['1', 'Master Trust Bank of Japan (trust a/c)', 'Custodian – domestic passive/active funds', '~17–19%'],
    ['2', 'Custody Bank of Japan (trust a/c)', 'Custodian – domestic funds/pensions', '~9.8%'],
    ['3', 'Meiji Yasuda Life Insurance', 'Life insurer – stable/cross-holder', '~6.1%'],
    ['4', 'Nippon Life Insurance', 'Life insurer – stable holder', '~3.2%'],
    ['5', 'State Street Bank & Trust 505001', 'Foreign custodian (institutional)', '~2.2%'],
    ['6', 'TOTO Employee Stock Ownership Association', 'Insider / employees', '~2.0%'],
    ['7', 'State Street Bank & Trust 505103', 'Foreign custodian', '~1.7%'],
    ['8', 'BNYM as Agent / Clients Non-Treaty JASDEC', 'Foreign custodian', '~1.5%'],
    ['9', 'John Hancock Disciplined Value Int\'l Fund', 'Foreign active fund', '~1.4% (older list)'],
    ['10', 'Other (JPM / Morgan Stanley custodial a/c)', 'Foreign custodian', '~1%'],
    ['—', 'Nomura AM group (5% report)', 'Institutional', '8.0% (Jul 2025)'],
    ['—', 'BlackRock Japan group (5% report)', 'Institutional', '~4–6% (2024)'],
    ['—', 'Palliser Capital', 'Activist hedge fund', '"Top-20"; <5% (no large-holding report)']],
   'Sources: TOTO stock information page, half-year/annual securities reports, large-holding reports (via Kabutan). Directors\' holdings are de minimis.', [0.4, 3.2, 3, 1.8])
h2('16.1 Activism: Palliser Capital (2026)')
tb(['Palliser demand (Feb 2026)', 'TOTO response (30 Apr 2026)', 'Success'],
   [['Disclose Advanced Ceramics properly (ESC for NAND cryo-etch, AD parts)', 'Two-segment reporting; ceramics sales/OP/margin disclosed; FY3/27 ceramics plan', '<b>Achieved</b>'],
    ['Invest more in Advanced Ceramics', '~¥30bn capex to FY2028; Buzen +20% capacity; Chigasaki R&D; ~¥80bn 5-yr (reported Jun 2026)', '<b>Achieved</b>'],
    ['Restructure low-profit housing, especially China', 'China plant closures (pre-dated campaign); ~¥7bn improvement targeted', 'Partially (already under way)'],
    ['Capital efficiency: appropriate equity ratio; review ~¥76bn excess cash and ~¥76bn cross-holdings', 'DPS ¥110 → ¥120; buyback (size unverified); cross-holding target <10% of net assets', 'Partial – the open item'],
    ['Implied: unlock >55% upside (¥8,800+/share)', 'Stock peaked at ¥9,500 (Jun 2026); now ¥6,097', 'Achieved then reversed']], None, [3, 3.5, 1.3])
p('Palliser publicly welcomed TOTO\'s "adoption of the Value Enhancement Plan" (7 May 2026). No shareholder proposals were filed at the June 2025 or June 2026 AGMs. Whether Palliser still holds the stake after the June peak is not disclosed; a renewed campaign around the STAGE3 plan (spring 2027) is plausible.')
h2('16.2 Short interest')
bl('JPX short-position reports (≥0.5%) have listed Barclays Capital Securities, Merrill Lynch International, Morgan Stanley MUFG, Nomura International, UBS AG, Integrated Core Strategies (Millennium) and Qube Research & Technologies at various dates — consistent with quant/market-maker and long-short pair trades (long ceramics peers/short TOTO or vice versa) rather than a fundamental short campaign.',
   'Margin long balance ~0.53m shares with a long/short ratio of ~5.1x (5 Jun 2026) — low relative to free float. We estimate total short interest at ~1–2% of shares; verify via JPX/karauri.net before trading.',
   'No published activist short report on TOTO identified.')

# ------------------------------------------------------------------
h1('17. Strategic Initiatives (2016–2026)')
tb(['Initiative', 'When', 'What', 'Outcome / status'],
   [['TOTO Vplan2017', 'to FY2017', 'Prior long-term plan: global growth, China/Asia expansion', 'China expansion later reversed'],
    ['TOTO WILL2030', 'Apr 2021 –', 'Sales ≥¥1tn, OPM ≥12%, ROE/ROIC ≥12%, overseas >40% by FY2030', 'Off-track: sales ¥737bn, OPM 7.3%, ROE 7.7%'],
    ['WILL2030 STAGE1', 'FY2021–23', 'Growth in China/Asia, ceramics, DX', 'Missed (China, memory downturn)'],
    ['WILL2030 STAGE2', 'FY2024–26', '¥175bn strategic capex; FY3/27 sales ¥785bn, OP ¥60bn', 'Ceramics ahead; housing behind; ends Mar 2027'],
    ['China structural reform', '2024–2025', '¥34bn impairment; Beijing & Shanghai plants closed (~2,000 staff); consolidate Zhangzhou/Dalian', 'Execution done; profit recovery pending'],
    ['Americas expansion', '2024–2031', 'Georgia plant (US$224m); ¥100bn sales by FY3/31; US production >50%', 'On track; tariff headwinds'],
    ['Asia manufacturing hub', '2014–2024', 'India (Halol), Vietnam 4th plant (2022), faucet plant (2024)', 'Successful — Asia OPM ~19%'],
    ['Advanced Ceramics scale-up', '2023–2028', 'Buzen kiln (+20% Jan 2027), Chigasaki R&D (Apr 2028), ~¥80bn 5-yr', 'Strong success; key value driver'],
    ['Japan pricing discipline', '2023–2026', 'Four consecutive price rises incl. 8–13% Dec 2026', 'Partial offset of cost inflation'],
    ['Environmental building materials (Hydrotect)', '1990s–', 'Photocatalytic tiles/coatings', 'Sub-scale; limited contribution'],
    ['Morimura SOFC JV', '2019 –', 'Solid-oxide fuel cells with NGK, Niterra, Noritake', 'Small, pre-commercial'],
    ['Capital-efficiency push', '2025–2026', '¥20bn buyback (cancelled), DPS growth, cross-holding reduction, segment disclosure', 'Under way — next step STAGE3 (Apr 2027)']], None, [1.8, 1.1, 3.6, 2.4])

# ------------------------------------------------------------------
h1('18. Stakes in Other Companies')
tb(['Holding', 'Type', 'Stake', 'Strategic relevance', 'Financial relevance'],
   [['Noritake (5331 JP)', 'Listed – Morimura group', '~1–3% (e)', 'Group heritage; ceramics know-how', 'Low'],
    ['Niterra (5334 JP)', 'Listed – Morimura group', '~1% (e)', 'Group heritage; ceramics peer', 'Low–moderate (mark-to-market)'],
    ['NGK Insulators (5333 JP)', 'Listed – Morimura group', 'small (unconfirmed)', 'Group heritage; ESC competitor', 'Low'],
    ['Banks / insurers / distributors / homebuilders', 'Listed cross-holdings', 'various', 'Relationship holdings', 'Total ~¥60–76bn (e); being reduced'],
    ['Morimura SOFC Technology', 'Unlisted JV', 'minority', 'Fuel-cell R&D', 'Negligible'],
    ['TDY alliance (Daiken, YKK AP)', 'Commercial alliance', 'No equity', 'Remodel channel', 'n/a']],
   'Specified-investment details to be confirmed from the FY3/26 yuho ("株式の保有状況"). Policy: cross-holdings <10% of net assets (FY2025), <5% by FY2030; proceeds to be redeployed.', [2.2, 1.8, 1.3, 2, 2.2])
p('<b>Relevance:</b> strategically minor; financially, the portfolio (~6–8% of market cap) is a source of cash for buybacks — the most likely near-term "self-help" catalyst.')

# ------------------------------------------------------------------
h1('19. Shareholder Returns: Dividends, Buybacks and Treasury Shares')
tb(['Fiscal year', 'DPS (¥)', 'Payout', 'Buyback', 'Cancellation', 'Comment'],
   [['FY3/22', '~90 (e)', '~38%', '—', '—', ''],
    ['FY3/23', '~100 (e)', '~43%', '—', '—', ''],
    ['FY3/24', '~100 (e)', '~45%', '—', '—', 'Held flat'],
    ['FY3/25', '100', '~137% (impairment year)', '—', '—', 'Maintained despite NI -67%'],
    ['FY3/26', '110', '45.3% (DOE 3.47%)', 'Up to ¥20bn / 8m shares (4.7%), announced 28 Apr 2025; completed Aug 2025', 'Cancelled (2025)', 'First large buyback'],
    ['FY3/27E', '120 (¥60 + ¥60)', '~43%', 'Announced Apr 2026 (size unverified; one source: up to 7.5m shares / ¥13bn)', 'n/d', 'Policy: payout ≥40%, progressive']],
   'Treasury shares: issued ~169.6m vs ~164.4m outstanding implies ~5m held (e). (e) items to be verified against TOTO\'s shareholder-return page and tanshin.', [1.1, 1.2, 1.6, 3, 1.3, 2])

# ------------------------------------------------------------------
h1('20. Adversarial Deep Dive: Bull, Bear, Pre-Mortem, Contrarian View')
h2('20.1 Bull case')
bl('<b>Moat sustainability:</b> ESCs are process-of-record parts; requalification takes 12–24 months and risks yield. TOTO\'s 35+ years with Lam create a co-design loop; Palliser cites a ~5-year lead in cryo-ESC.',
   '<b>Growth levers:</b> NAND layer race (cryo-etch is the only economic path beyond ~300 layers), logic AD-coated parts (1nm-era R&D), replacement annuity, capacity +20% (Jan 2027) then more; US Washlet; China break-even; Dec 2026 price rise.',
   '<b>Earnings surprise potential:</b> FY3/28E EPS could reach ¥380–400 if ceramics hits ¥100bn+ and the price rise sticks (~+10% vs consensus).',
   '<b>Capital allocation:</b> ¥200bn of returnable capital (excess equity, cross-holdings, cash) could fund ~20% of market cap in buybacks over 3–4 years.')
h2('20.2 Bear case')
bl('<b>1. Memory capex downturn (permanent-impairment risk: medium).</b> FY3/24 showed ceramics OP can fall ~35%; at peak margins, a 2027–28 NAND digestion would cut group OP by ~20% and the multiple simultaneously.',
   '<b>2. Customer/technology displacement.</b> Lam is the dominant customer; TEL\'s cryogenic etch, Lam dual-sourcing (NGK, Kyocera, in-house) or a shift to non-cryo architectures would permanently impair the segment\'s economics.',
   '<b>3. Housing structural decline.</b> Japan starts falling toward ~600k, labour shortages and Chinese competitors overseas could keep housing margins at ~3–4% indefinitely — and the housing business is still ~90% of capital employed.',
   '<b>High expectations?</b> Consensus EPS (~¥295 FY3/27) is above guidance (¥280) after a Q1 miss; the share price at ¥9,500 discounted ~30x FY3/28E. At ¥6,097 expectations are lower but not washed out (21.8x FY3/27E).')
h2('20.3 Pre-mortem: "It is October 2027 and TOTO is ¥3,800 — what happened?"')
bl('H1 FY3/27 confirmed ceramics stagnation, not timing; Lam guided NAND customers to pause after 2026 pull-forward.',
   'The Dec 2026 price rise triggered share loss to LIXIL/Panasonic and a Q4 volume air-pocket; Japan housing OP fell below ¥15bn.',
   'China break-even slipped again; another impairment was taken.',
   'STAGE3 (Apr 2027) focused on capex and ¥1tn sales, with no ROE or buyback target; Palliser exited; the stock de-rated to a housing multiple (~14x P/E on ~¥270 EPS).')
h2('20.4 Are multiples too high?')
p('On consolidated metrics, yes (regression: ~50% premium to margin-implied EV/Sales; 21.8x FY3/27E P/E vs ~14x for Japanese housing peers). On SOTP, no: housing at peer multiples leaves ceramics at ~15x FY3/28E EBIT. The question is therefore not "is TOTO expensive" but "is the ceramics growth durable" — a cyclical-semiconductor question being underwritten by investors who mostly own TOTO as a defensive housing name.')
h2('20.5 Contrarian view: what the market refuses to see')
co('<b>The market is debating ceramics growth; it is ignoring the housing optionality and the balance sheet.</b> Housing earned ~¥31bn of OP in FY3/25 even with China losing money; China at break-even plus the largest Japan price increase in a decade could add ~¥12–15bn of OP by FY3/28 — worth ~¥700/share at 9x — and that is not cyclical semiconductor exposure. Meanwhile ~¥200bn of excess capital is a call option on Japanese governance reform. Even if ceramics stalls, the downside is cushioned by self-help that the momentum-driven sell-off in August ignored.')

# ------------------------------------------------------------------
h1('21. Scenario Analysis')
tb(['Scenario (prob.)', 'Ceramics sales FY3/29E', 'Ceramics margin', 'Housing OP FY3/29E', 'Group EPS FY3/29E', 'Multiple', 'Value / share', 'vs price'],
   [['<b>Bull (25%)</b>', '¥125bn (+23% CAGR)', '44%', '¥50bn', '~¥470', 'Ceramics 22x EBIT; housing 12x', '<b>~¥10,000</b>', '+64%'],
    ['<b>Base (50%)</b>', '¥110bn (+18% CAGR)', '42%', '¥41bn (FY28)', '~¥396', 'SOTP: 18x / 9x (FY3/28E)', '<b>~¥7,200</b>', '+18%'],
    ['<b>Bear (25%)</b>', '¥60bn (flat, downturn)', '35%', '¥26bn', '~¥220', 'Ceramics 12x; housing 8x; P/E ~16x', '<b>~¥3,500</b>', '-43%'],
    ['<b>Probability-weighted</b>', '', '', '', '', '', '<b>~¥6,975</b>', '<b>+14%</b>']], None, [1.6, 1.6, 1, 1.3, 1.2, 2.2, 1.2, 0.8])
img('football.png', 'Valuation range ("football field"), JPY per share.', 0.95)
p('<b>Positioning implication:</b> the asymmetry (+64% / -43%) is acceptable but not compelling at full size; we would size as a mid-weight event-driven position into H1 results (~30 Oct 2026) and add on confirmation of ceramics re-acceleration or a STAGE3 capital-return framework.')

# ------------------------------------------------------------------
h1('22. Questions for the CEO / Chairman (ordered by information value)')
qs = ['What share of Advanced Ceramics revenue comes from Lam Research, and do you hold sole-source or dual-source positions on Lam\'s current cryogenic etch platforms?',
      'Was the Q1 FY3/27 ESC shortfall purely shipment timing — what is the H1 order intake and book-to-bill for ceramics?',
      'How do you see Tokyo Electron\'s cryogenic etch entry affecting your position — are you qualified, or in qualification, with TEL?',
      'What return-on-capital hurdle and payback do you apply to the ~¥80bn ceramics programme, and what demand visibility underwrites capacity beyond Buzen?',
      'Will the next mid-term plan (STAGE3) include explicit ROE (≥10–12%), equity-ratio and total-shareholder-return targets?',
      'What is your target equity ratio, and how much of the ~¥60–76bn cross-shareholding portfolio will be sold by FY3/29?',
      'Would the board consider structural options for ceramics (separate listing, tracking disclosure, minority partner) if the SOTP gap persists?',
      'What is your realistic early read on volume elasticity to the 1 Dec 2026 price rise, and will LIXIL and Panasonic follow?',
      'What exactly must happen for China to break even in FY3/27, and what is the remaining capital at risk there?',
      'How much of US Washlet/toilet supply is now tariff-exposed, and what is the margin target for the Americas once Georgia is at full utilisation?',
      'How do you allocate corporate costs between housing and ceramics, and what is the standalone ROIC of each segment?',
      'What is the replacement-cycle share of ceramics revenue and how resilient was it in the FY3/24 downturn?',
      'How will executive pay be linked to ROE/TSR rather than operating profit?',
      'Is the ¥1tn sales target for FY3/31 still the right North Star, or should the company target profit and capital efficiency instead?',
      'What is your engagement status with Palliser and other large shareholders after the June 2026 AGM?']
tb(['#', 'Question'], [[str(i + 1), q] for i, q in enumerate(qs)], None, [0.4, 9])

# ------------------------------------------------------------------
h1('23. Short-Seller / Forensic View')
h2('23.1 Dismantling the bull case')
bl('<b>Structural break:</b> the profit pool now depends on one technology (cryo-ESC), one customer (Lam) and one end market (NAND). A shift in etch architecture, a Lam dual-source decision or TEL share gains would hit >50% of group OP — with no offset from a ~4%-margin housing business.',
   '<b>Concentration shift:</b> if Lam moved 25% of its cryo-ESC volume to a second source, we estimate ceramics OP would fall ~¥8–10bn (-30%) and the SOTP would lose ~¥1,000/share.',
   '<b>Weaker moat than bulls think:</b> AMAT and Lam both have in-house ESC capability; Shinko is now JIC-backed with deep pockets; NGK and Kyocera have scale in AlN. Margins of 43% invite competition and customer push-back on price.',
   '<b>Most underestimated competitor:</b> Tokyo Electron — not as an ESC maker, but as a cryo-etch tool maker whose success would re-allocate the installed base away from Lam\'s platform where TOTO is embedded.',
   '<b>Worst capital allocation:</b> China (two plants built in 1995/2001, ~¥49bn written off 2024–26); decades of over-capitalisation (equity ratio ~64%, ROE <8%).',
   '<b>Incentives:</b> bonuses tied to operating profit and sales growth (¥1tn target), not ROE/TSR — encourages capex over buybacks.',
   '<b>What must hold for ¥6,097:</b> ceramics compounding ~18% p.a. at >40% margins through FY3/29 and housing margins recovering to ~5–6%. <b>If growth disappoints 20–30%</b> (ceramics FY3/29E ~¥80–90bn, EPS ~¥300–320), fair value on a 17x P/E is ~¥5,100–5,400 (-12% to -16%); with a cyclical de-rating to 14x, ~¥4,300 (-30%).',
   '<b>Single permanent-impairment scenario:</b> NAND makers adopt a non-cryogenic high-aspect-ratio etch route (or TEL wins the next node) while Lam qualifies a second ESC source — plausibility ~10–15% over 3 years.')
h2('23.2 Red flags and accounting risks')
tb(['Area', 'Observation', 'Risk level'],
   [['Revenue recognition', 'Ceramics recognised on shipment; Q1 FY3/27 "timing" miss shows lumpiness — watch for channel/stock-building at the customer', 'Medium'],
    ['Segment reporting', 'FY3/26 change from three to two segments merges Japan and overseas housing — reduces visibility of China losses; corporate-cost allocation to ceramics opaque', 'Medium'],
    ['Impairments', '¥34.1bn (FY3/25) + ~¥15bn (FY3/26) China charges: recurring "one-offs"; remaining China assets and the Americas plant are the next tests', 'Medium'],
    ['Non-operating income', 'Ordinary income exceeded OP by ¥6.9bn in FY3/26 (FX gains, dividends) — NI quality lower than headline', 'Low–Medium'],
    ['Leases', 'Showrooms/logistics leases (J-GAAP: limited on-balance recognition) — understate EV slightly', 'Low'],
    ['Related parties', 'None material identified; Morimura group JV is small', 'Low'],
    ['Contingencies / provisions', 'Product-safety recalls (Washlet 96Z series fire risk; faucet leaks) — warranty provisions could rise', 'Low–Medium'],
    ['Pensions', 'Japanese DB obligations; discount-rate sensitivity', 'Low'],
    ['Stock-based compensation', 'Minimal; pay mostly cash bonus — no dilution, but weak alignment', 'Low'],
    ['Goodwill / intangibles', 'Minimal (organic grower) — positive', 'Low'],
    ['Cash flow', 'FCF ~¥35bn (OCF ¥71bn – capex ¥36bn); capex rising to ¥45–55bn will compress FCF as dividends rise', 'Medium'],
    ['Cross-holding gains', 'Gains on sale flatter extraordinary income during the unwind', 'Low']], None, [1.6, 6, 1])

# ------------------------------------------------------------------
h1('24. Timeline and Catalyst Calendar')
h2('24.1 Key past events')
tb(['Date', 'Event'],
   [['1917', 'Toyo Toki founded in Kokura (Kitakyushu) — Morimura group'], ['1976', 'Fine-ceramics research begins'],
    ['1980', 'Washlet launched'], ['1988', 'Mass production of electrostatic chucks'], ['c.1990', 'Co-development with Lam Research begins'],
    ['1995 / 2001', 'TOTO Beijing / TOTO East China (Shanghai) established'], ['2007', 'Renamed TOTO Ltd.'], ['2014', 'India plant (Halol, Gujarat)'],
    ['Apr 2021', 'TOTO WILL2030 long-term vision'], ['Jul 2022', 'Vietnam 4th plant'], ['Oct 2023', 'FY guidance cut (China)'],
    ['Apr 2024', 'WILL2030 STAGE2 (¥175bn strategic capex)'], ['Oct 2024', '¥34bn China impairment; stock -12.5%'],
    ['Apr 2025', 'Tamura becomes President; China plant closures; ¥20bn buyback'], ['Fall 2025', 'Georgia (US) plant production'],
    ['Jan 2026', 'Goldman upgrade; stock +11%'], ['Feb 2026', 'Palliser Capital Value Enhancement Plan'],
    ['Apr–May 2026', 'Record FY3/26; ceramics disclosure; limit-up'], ['Jun 2026', 'ATH ¥9,500; board cut to 10'],
    ['Jul–Aug 2026', 'Q1 miss (-11.4%); Dec 2026 price rise announced']], None, [1.3, 8])
h2('24.2 Upcoming catalysts')
tb(['Date', 'Event', 'Importance'],
   [['Oct–Nov 2026', 'Japan pre-buying ahead of 1 Dec price increase', 'Medium'],
    ['21 Oct 2026', 'Lam Research Sep-quarter results (NAND/cryo commentary)', '<b>High</b>'],
    ['~30 Oct 2026', '<b>TOTO H1 FY3/27 results</b> — ceramics timing, guidance', '<b>Critical</b>'],
    ['~mid-Nov 2026', 'Applied Materials results; Japan housing starts (monthly)', 'Medium'],
    ['1 Dec 2026', 'Japan price increase effective (8–13%)', 'High'],
    ['Jan 2027', 'Buzen ESC kiln complete (+20% capacity)', 'High'],
    ['~29 Jan 2027', 'TOTO Q3 FY3/27 results', 'High'],
    ['~late Apr 2027', '<b>FY3/27 results + WILL2030 STAGE3 mid-term plan</b> (capital allocation, ROE, returns)', '<b>Critical</b>'],
    ['Jun 2027', 'AGM — possible activist engagement', 'Medium'],
    ['Ongoing', 'US tariff decisions; Palliser/large-holding filings; cross-holding sales', 'Medium'],
    ['Apr 2028', 'Chigasaki ceramics R&D building complete', 'Low']], None, [1.4, 6, 1.2])

# ------------------------------------------------------------------
h1('25. Data Notes and Disclaimer')
p('This report was prepared on 4 October 2026 using publicly reported information (company press releases, results summaries and presentations as reported by Nikkei, Bloomberg, Reuters, Japan Times, Kabutan, Data-Max, Reform Online, LIMO, BusinessWire and data aggregators). Direct access to TDnet, EDINET and the TOTO IR site was not available in the research environment, so several items — notably the five-year segment history (FY3/22–FY3/24), balance-sheet line items, board backgrounds, treasury shares and short interest — are reconstructions or estimates and are marked "e", "~" or "n/d". Forecasts, valuations, scenario probabilities and the regression are the author\'s own. Peer data are indicative and dated Jul–Sep 2026. Verify all marked figures against primary filings before relying on them. This document is for professional investors, is not investment advice and does not constitute an offer to buy or sell securities.')
