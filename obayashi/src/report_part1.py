from docx_helpers import _runs
from docx_helpers import *
from model import *

A = "assets/"


def cover(d):
    p = d.add_paragraph()
    _runs(p, "EQUITY RESEARCH | EVENT & SPECIAL SITUATIONS", 9, BLUE, True)
    p = d.add_paragraph()
    _runs(p, "Obayashi Corporation (1802 JT)", 26, NAVY, True)
    p = d.add_paragraph()
    _runs(p, "Japan's #2 super-general contractor: record margins, net cash and a stock 32% off its high", 12.5, GREY)
    para(d, "Report date: 3 October 2026 | Reference price: JPY 3,008 (30 Sep 2026 close†) | Fiscal year ends 31 March (FY3/26 = year to March 2026)", 8.5, False, GREY)
    callout(d, f"**Rating: ACCUMULATE (moderately positive).  12-month target JPY 3,500 (+16%); probability-weighted value JPY {PW:,.0f} ({PW/PRICE-1:+.0%}).**  "
               "Net cash, a guidance record that is deliberately conservative, a regression-implied discount of c.23% to peers on EV/Sales, and an active "
               "capital-return and cross-holding-unwind programme support the shares. Against that: FY3/26 earnings were flattered by securities-sale gains, "
               "the order book is flat-to-down, margin is at a cyclical high, and material and labour inflation plus the Multiplex integration are live risks.")
    table(d, ["Metric", "Value", "Metric", "Value"], [
        ["Price / market cap", f"JPY 3,008 / JPY {MCAP:,.0f}bn", "FY3/26 sales / OP", "JPY 2,586bn / JPY 194.7bn (7.5%)"],
        ["52-wk high / low (YTD)", "JPY 4,439 (27 Feb 26) / 2,891 (19 Aug 26)†", "FY3/26 net income / EPS", "JPY 173.8bn / JPY 249.4"],
        ["Net cash (31 Mar 26)", f"JPY {NETCASH:.0f}bn†", "FY3/27 guidance (sales/OP/NI)", "JPY 2,945bn / 180bn / 157bn"],
        ["EV (mkt cap less net cash)", f"JPY {EV:,.0f}bn", "DPS FY3/26 / FY3/27E", "JPY 88 / JPY 94 (DOE c.5%)"],
        ["EV/Sales | EV/EBITDA* | EV/EBIT", f"{M['ev_sales']:.2f}x | {M['ev_ebitda']:.1f}x | {M['ev_ebit']:.1f}x", "P/E trailing | on guidance | on our FY27E", f"{M['pe_t']:.1f}x | {M['pe_g']:.1f}x | {MCAP/BASE[0]['ni']:.1f}x"],
        ["P/B | dividend yield", f"{M['pb']:.2f}x | {M['dy']:.1f}%", "Our EPS FY27E / 28E / 29E", f"JPY {BASE[0]['eps']:.0f} / {BASE[1]['eps']:.0f} / {BASE[2]['eps']:.0f}"],
    ], widths=[4.2, 4.6, 4.2, 4.2], size=8)
    para(d, "*EBITDA is estimated as operating income plus an assumed JPY 50bn of depreciation and amortisation; D&A could not be retrieved. † = from search-result summaries, not verified against a primary filing. See the Data Confidence note on the last page.", 7.5, True, GREY)
    h2(d, "Read this first: data limitations")
    para(d, "This environment could not open Obayashi's investor-relations site, EDINET, JPX, Kabutan or Yahoo pages (blocked by the network egress policy), and the Financial Datasets feed returned no credits. Every number here comes from web-search result summaries of primary and secondary sources. Where figures conflicted we say so, and where nothing could be found we write 'n/a'. **The most important figures (FY3/26 results, FY3/27 guidance, Q1 FY3/27 results, board and shareholder lists) were corroborated by at least two independent summaries; peer multiples, price history and capital-structure detail were not.** "
              "Before committing capital, tie the flagged items to the FY3/26 tanshin, the 2026 Integrated Report and the securities report (yuho).")


def exec_summary(d):
    h1(d, "1. Investment summary")
    bullets(d, [
        "**What it is:** Japan's second-largest listed general contractor by FY3/25 sales (JPY 2.59tn vs Kajima 2.91tn), building offices, data centres, factories and hospitals, plus tunnels, dams and rail, with a third of sales overseas (US, Asia, and from late 2026 Australia/UK/Canada via Multiplex).",
        "**The earnings reset is real:** operating margin rose from 2.1% (FY3/22) to 7.5% (FY3/26) on selective order-taking, price escalation, change orders on large domestic building jobs, and fewer loss-making legacy projects. Operating income is up 4.7x in four years.",
        f"**But the FY3/26 EPS of JPY 249 flatters:** net income (JPY 173.8bn) was 85% of ordinary income (JPY 204bn). A normal tax-adjusted ratio is c.68-70%, implying roughly JPY 30-35bn of net one-off gains (securities sales), an inference we cannot confirm without the tanshin. Q1 FY3/27 net income (JPY 39bn) again exceeded operating income because of a c.JPY 20bn securities gain.",
        "**Guidance is a sandbag, not a forecast:** for FY3/26 management guided net income down 32% to JPY 100bn (the shares fell c.9% intraday on 13 May 2025); the outcome was JPY 173.8bn. For FY3/27 it guides OP JPY 180bn (-7.5%) and NI JPY 157bn (-9.6%); Q1 delivered 19.9% of full-year ordinary-profit guidance against a five-year average of 16.2%, and consensus ordinary profit (JPY 193bn) already sits 5% above guidance.",
        f"**Valuation is undemanding but no longer cheap against its own history:** {M['pe_t']:.0f}x trailing P/E, {M['ev_ebitda']:.1f}x EV/EBITDA (c.{M['ev_ebitda_adj']:.0f}x after deducting JPY 289bn of cross-held shares), 1.6x P/B, JPY 84bn net cash, c.8% free-cash-flow yield on a CFO+CFI proxy. A seven-peer regression of EV/Sales on EBIT margin (R² 0.86) implies 0.95x vs 0.77x actual, a c.23% discount.",
        "**Capital return is the engine:** DOE target c.5%, JPY 100bn buyback programme through FY3/27 (c.JPY 70bn executed or announced†), cross-holdings of JPY 289bn (21.9% of net assets) being cut to the 20% ceiling by March 2027 with JPY 58bn already contracted, and a successor mid-term plan due around May 2027.",
        "**Key risks:** (1) cost inflation in a fixed-price backlog (Middle East-driven naphtha-material disruption, labour), (2) the Multiplex acquisition (USD 540m for a thin-margin Australian/UK builder with a history of fixed-price disputes), (3) an order book that is not growing (Q1 orders -7.2%), (4) margin mean-reversion after a 4.7x profit recovery, and (5) a regulatory and reputational tail from the Linear bid-rigging legacy.",
    ])
    h2(d, "Our view in one table")
    table(d, ["", "Bear (30%)", "Base (50%)", "Bull (20%)"], [
        ["FY3/28E operating income", "JPY 150bn", "JPY 197bn", "JPY 225bn"],
        ["FY3/28E EPS", f"JPY {BEAR[1]['eps']:.0f}", f"JPY {BASE[1]['eps']:.0f}", f"JPY {BULL[1]['eps']:.0f}"],
        ["EV/EBITDA applied", "6.5x", "8.5x", "9.5x"],
        ["Value per share", f"JPY {SCV['Bear'][1]:,.0f} ({SCV['Bear'][1]/PRICE-1:+.0%})", f"JPY {SCV['Base'][1]:,.0f} ({SCV['Base'][1]/PRICE-1:+.0%})", f"JPY {SCV['Bull'][1]:,.0f} ({SCV['Bull'][1]/PRICE-1:+.0%})"],
    ], widths=[5, 4, 4, 4], size=8.5)
    para(d, f"Probability-weighted value JPY {PW:,.0f} ({PW/PRICE-1:+.0%}). Equity value = EBITDA x multiple + net cash (JPY 84bn) + 75% of cross-held shares (JPY 289bn x 0.75) on 680m shares. Full assumptions in Section 21.", 8, True, GREY)


def laymans(d):
    h1(d, "2. Layman's guide: what Obayashi does and how it makes money")
    para(d, "Obayashi is a builder. Clients (a property developer, a railway company, a government ministry, a chipmaker, a data-centre operator) hire Obayashi to design and construct something. Obayashi usually agrees a price up front, hires hundreds of specialist subcontractors, buys steel, concrete and equipment, and earns the difference between the contract price and what the job really costs. It is paid in stages as the work progresses (progress billings), with government clients often paying a sizeable advance at the start.")
    bullets(d, [
        "**Revenue = contracts won x how much of each job is finished this year.** It is recognised as work proceeds (cost-to-cost percentage of completion), so today's order wins become sales over 2-4 years.",
        "**Profit = contract price - actual cost.** The margin is thin (5-10% operating), and the whole game is pricing jobs properly, controlling costs, and getting paid for changes the client asks for mid-build.",
        "**A small property arm** builds and sells or leases buildings (including data-centre sites); this is lumpy but high-margin.",
        "**Overseas** (c.33% of sales) means mostly US construction through subsidiaries (Webcor, Kraemer, E.W. Howell, James E. Roberts-Obayashi, MWH, GCON) plus Asian subsidiaries; Australia/UK/Canada is being added via the Multiplex deal.",
    ])
    table(d, ["Division", "What it builds", "FY3/26 sales (JPY bn)", "% of sales", "FY3/26 OP (JPY bn)", "OP margin", "% of OP"], [
        ["Domestic building", "Offices, high-rises, factories, data centres, hospitals, logistics", "1,138.8", "44%", "104.0", "9.1%", "53%"],
        ["Domestic civil engineering", "Tunnels, dams, rail, roads, ports, renewables civil", "426.6", "16%", "40.9", "9.6%", "21%"],
        ["Overseas building", "US/Asia commercial, tech, healthcare", "508.0", "20%", "11.9", "2.3%", "6%"],
        ["Overseas civil engineering", "Infrastructure, rail, water", "336.0", "13%", "14.7", "4.4%", "8%"],
        ["Real estate + other (derived)", "Development, leasing, renewables, wood, group services", "177.0", "7%", "23.0", "c.13%", "12%"],
        ["Group total", "", "2,586.3", "100%", "194.7", "7.5%", "100%"],
    ], widths=[3.4, 4.6, 2.2, 1.5, 2.0, 1.6, 1.5], size=7.5, hl_rows=(5,))
    para(d, "Source: BUILT/ITmedia and japanir summaries of the FY3/26 tanshin; segment sales are secondary-source figures†. 'Real estate + other' sales and OP are derived as group total less the four construction segments (construction segment total: sales JPY 2,409.3bn, OP JPY 171.7bn). Overseas segment OP margins are well below Japan's; overseas civil OP is JPY 8.3bn in one summary, so treat that line as uncertain.", 7.5, True, GREY)
    image(d, A + "segment_op.png", 13.5)
    callout(d, "**The one-line version:** Obayashi earns about 9-10 yen of operating profit per 100 yen of Japanese contracts and about 3 yen per 100 yen overseas. Japan is c.67% of sales but c.86% of operating profit, so the investment case is largely a bet on Japanese construction pricing discipline.")


def price_history(d):
    h1(d, "3. What has moved the stock: catalysts since 2021")
    para(d, "We could not retrieve a daily price series, so this table lists events we can date, with the move where a source gave one. Over five years the shares roughly tripled to the February 2026 peak of JPY 4,439 (approx. JPY 1,000 in late 2021; approximate, from memory†) before falling 35% to JPY 2,891 on 19 August 2026. Only one single-session move of more than 10% could be dated (5 March 2024); most of the re-rating came in multi-week legs driven by earnings, not single days.")
    table(d, ["Date", "Event", "Move", "Read-through"], [
        ["7 Nov 2022", "FY3/23 forecast cut: construction-material inflation and delivery delays hit domestic building (gross profit -JPY 9.5bn)", "n/a", "Trough-margin signal; sets up the pricing-discipline pivot"],
        ["28 Jun 2023", "Silchester shareholder proposal (JPY 12 special dividend) gets c.26.8% support", "n/a", "First clear sign of investor pressure on capital returns"],
        ["early Mar 2024", "Capital policy: ROE 10%+ target, DOE c.5%, large dividend increase (formalised in 13 May 2024 plan addendum)", "Limit-up on 5 Mar 2024 (>10%; exact % n/a)", "The re-rating catalyst: dividends, buybacks and cross-holding sales"],
        ["Nov 2024", "Domestic broker upgrade to Outperform (target 2,100 to 2,400)", "n/a", "Sell-side validation of margin recovery"],
        ["10 Feb 2025", "Buyback of up to 20m shares (2.8%) as first tranche of JPY 100bn programme", "n/a", "Capital return begins"],
        ["13 May 2025", "FY3/26 guidance: net income -32% to JPY 100bn", "c.-9% in the afternoon session†", "Over-conservative guidance; recovered as results beat"],
        ["Aug 2025", "Share cancellation and JPY 40bn buyback announced†", "n/a", "Continued return of capital"],
        ["Nov 2025", "FY3/26 forecast raised", "n/a", "Margin upside begins to show"],
        ["27 Feb 2026", "All-time high JPY 4,439 (after Q3 results with ordinary profit +33%, below consensus)", "Peak", "Peak optimism on margins and the capital-return story"],
        ["13 May 2026", "FY3/26 results beat forecast; FY3/27 NI guided -9.6%", "-7.8% intraday (to JPY 3,612) after a large gain the day before", "Market punishes the earnings-down guide despite pattern of beating"],
        ["7 Aug 2026", "Q1 FY3/27: OP +107%, orders -7.2%, guidance unchanged", "n/a (c.JPY 2,990 by 28 Aug)", "Strong profit, soft orders, no raise"],
        ["19 Aug 2026", "YTD low JPY 2,891", "-35% from the February peak", "Cause not identified in our sources; likely sector de-rating plus rate, cost and order worries (inference)"],
    ], widths=[2.2, 6.4, 3.4, 5.0], size=7.5)
    para(d, "What the stock has been pricing: from 2023 to early 2026, margin recovery plus governance reform (cross-holding sales, DOE, buybacks) re-rated the shares from sub-1x book to c.2.3x. Since February, the market has begun to price margin peaking, flat orders and higher rates (the BOJ policy rate was reportedly raised to 1.25% on 18 September 2026†).")


def business(d):
    h1(d, "4. Business model, drivers, customers, suppliers and competitors")
    h2(d, "4.1 Key drivers")
    table(d, ["Driver", "How it works at Obayashi", "Recent trend"], [
        ["Volume (orders, backlog)", "Orders convert to sales over 2-4 years; backlog gives visibility", "FY3/26 orders c.JPY 3.0tn†; FY3/27 target JPY 3.1tn; Q1 orders JPY 577.5bn (-7.2%)"],
        ["Pricing / contract terms", "Selective bidding, negotiated contracts, price-escalation clauses, change orders", "Gross margin on completed works guided at 13.0% for FY3/27 and 'around 13%' beyond"],
        ["Mix", "Domestic building and civil earn 9-10%; overseas 2-4%; real estate gains are lumpy", "Overseas share c.33%; GCON, MWH and Multiplex raise it further"],
        ["Cost inflation", "Steel, cement, ready-mix, naphtha-based finishes, labour", "Cement flat since June 2025; Middle East disruption to naphtha-derived materials†"],
        ["Labour / regulation", "2024 overtime cap, technician shortage, Construction Business Act revisions", "Pushes up unit labour cost; also restrains capacity industry-wide"],
        ["Capex cycle of clients", "Tokyo redevelopment, data centres, semiconductors, logistics, resilience plan", "Resilience plan FY2026-30 'over JPY 20tn'†; Linear Shizuoka agreement signed 18 Jul 2026†"],
        ["Securities and property gains", "Cross-holding sales and property disposals flow into extraordinary income", "JPY 20bn gain in Q1 FY3/27; JPY 285bn sold over five years†"],
    ], widths=[3.2, 7.2, 6.6], size=7.5)
    h2(d, "4.2 Customers, contracts and payment terms")
    bullets(d, [
        "**Public sector:** MLIT, NEXCO, JR Tokai (Linear), the Japan Railway Construction, Transport and Technology Agency, local governments. Awarded via competitive or comprehensive-evaluation tenders; public works commonly carry an advance payment (up to 40% of contract value is standard practice†, not confirmed in a filing).",
        "**Private sector:** developers (Mitsui Fudosan, Mitsubishi Estate, Mori Building, Sumitomo Realty, Tokyu are the typical Tokyo clients†), manufacturers, logistics and data-centre operators. Many are repeat clients on negotiated or limited-competition terms. We could not confirm named Obayashi contracts for TSMC/JASM or others.",
        "**Payment terms:** progress billings against milestones with retention; revenue recognised cost-to-cost; contract assets and receivables are large relative to cash flow (check the yuho for receivable days). Escalation ('slide') clauses exist on many public and some private jobs but typically lag cost moves; this lag is why the FY3/23 margin collapsed.",
        "**Supplier relationships:** Obayashi buys materials and equipment on a per-project basis and relies on an association of partner subcontractors (the 'Rinyukai'†). Supplier names are in Section 7.",
    ], 8.5)
    h2(d, "4.3 Competitors and markets")
    para(d, "Domestic: Kajima, Taisei, Shimizu and the unlisted Takenaka (the 'super general contractors'), with Daiwa House, Sekisui House, Toda, Haseko, Kumagai Gumi, Penta-Ocean, Okumura, Mitsui Sumitomo Construction (being acquired by Infroneer), Fujita and others in segments. FY3/25 sales: Kajima JPY 2,912bn, Obayashi 2,620bn†, Taisei 2,154bn, Shimizu 1,944bn. FY3/26 operating margins: Taisei c.9% (highest), Kajima c.7.7%, Obayashi 7.5%, Shimizu c.5.8%†. Overseas: Hochtief's Turner, Skanska USA, DPR, Gilbane in the US; Samsung C&T and Hyundai E&C in Asia; Webuild and local majors elsewhere†.", 9)
    h2(d, "4.4 Geography")
    para(d, "Japan c.67% of sales (c.JPY 1.74tn), overseas c.33% (JPY 844bn†): mainly North America, with Asia sales c.JPY 271bn†. Overseas operating margin is c.3% versus c.9.6% in Japan (derived). The Multiplex acquisition (Australia, UK, Canada) adds a third overseas leg, though at a very low sales margin (EBITDA c.USD 62m on c.USD 3.8bn revenue).", 9)


def macro(d):
    h1(d, "5. Macro and micro factors: tailwinds and headwinds")
    table(d, ["Tailwinds", "Headwinds"], [
        ["Large backlog and strong private non-residential demand: Tokyo redevelopment, data centres, semiconductor and logistics facilities", "Cost inflation in a fixed-price book: Middle East-driven disruption in naphtha-derived finishes; one estimate cuts Japanese construction investment 2.3% by end-2027 and 3.8% by end-2028†"],
        ["Industry pricing discipline: Big-4 selectively taking orders; Kajima, Taisei, Shimizu orders also guided below prior year", "Order intake: Q1 orders -7.2%; management cautious on the order environment from FY3/28, citing the Middle East"],
        ["National Resilience plan FY2026-30 (over JPY 20tn†) and Linear Shizuoka section agreement (18 Jul 2026†)", "Rates: BOJ policy rate reportedly 1.25% after the 18 Sep 2026 hike†; higher hurdle rates can delay developer capex"],
        ["Weak yen helps translated overseas profit and US data-centre scale-up (GCON, Webcor)", "Labour shortage and the 2024 overtime cap lift unit costs and lengthen schedules"],
        ["Governance reform: cross-holding sales, buybacks, DOE 5%, rising foreign ownership (40%)", "Peak-margin risk: 7.5% OP margin vs 2-5% for most of the prior decade"],
        ["Net cash of JPY 84bn funds M&A (Multiplex USD 540m) without stretching the balance sheet", "Legal/reputational overhang from the Linear bid-rigging cases (JFTC surcharge JPY 3.1bn, JPY 200m court fine, 4-month Tokyo suspension)"],
    ], widths=[8.5, 8.5], size=7.8, first_bold=False)


def moat(d):
    h1(d, "6. Product strength and economic moats")
    para(d, "Obayashi's product is execution on large, complex, safety-critical projects, sold on track record, technical capability (high-rise, tunnelling, seismic, timber, data centres) and relationships. It is not a consumer brand; its 'brand' lives with a few hundred repeat clients, and the Big-4 are close substitutes on most jobs. Obayashi's perceived strengths are tall buildings, tunnelling, wood construction and design-build; Kajima is stronger in civil and overseas scale, Taisei in margin and large infrastructure, Shimizu in housing-adjacent and energy (positioning from industry commentary, not survey data).")
    table(d, ["Moat category", "Rating", "Evidence and assessment"], [
        ["Brand", "Moderate", "Strong with repeat clients and in tall buildings; marked by the Linear scandal in public works; no consumer pricing power"],
        ["Hard assets", "Weak", "Asset-light contractor (plant, depreciation c.JPY 50bn est.); the assets that matter are people, systems and balance sheet"],
        ["Long-term contracts", "Moderate", "Backlog c.1.1x sales† gives 2-3 years of visibility, but contracts are one-off, not recurring, and cancellation/postponement risk exists"],
        ["Network effect", "None", "None, other than JV and subcontractor-network depth"],
        ["Regulatory and switching costs", "Moderate", "Construction licences, public-works eligibility ratings, safety records and capacity limits; clients can switch bidder per project, but repeat negotiated work is sticky"],
        ["Oligopolistic structure", "Strong", "Four super-GCs dominate large Japanese projects; rational pricing since 2023 and consolidation among mid-tier firms (Taisei-Toyo, Infroneer-SMCC, Shimizu-Nippon Road)"],
        ["Cash-flow predictability", "Moderate", "Operating CF swung JPY 50bn to JPY 253bn in five years† on working-capital timing; earnings volatile with cost shocks (FY3/23, FY3/24)"],
        ["Scalability", "Weak-moderate", "Labour-constrained; growth requires technicians, not capital. Overseas growth by acquisition"],
        ["Government interference history", "Weak", "Bid-rigging convictions (Linear), JFTC orders, public-works suspensions; but also a beneficiary of resilience spending"],
        ["Bargaining power vs stakeholders", "Moderate-strong", "Strong over subcontractors and suppliers (scale, payment); moderate vs developers and public clients; capacity constraints currently favour contractors"],
    ], widths=[3.6, 2.2, 11.2], size=7.8)
    callout(d, "**Moat verdict:** a narrow, cyclical moat built on oligopoly structure and capacity scarcity, not on product differentiation. It is strongest in the current up-cycle and weakest when order books thin and bidders discount to fill capacity.")


def supply_chain(d):
    h1(d, "7. Supply chain map")
    image(d, A + "supply_chain.png", 17.0)
    table(d, ["Layer", "Participants (companies)", "Obayashi's position and leverage"], [
        ["Raw materials", "Nippon Steel, JFE Steel, Tokyo Steel, Yamato Kogyo (steel/rebar); Taiheiyo Cement, UBE Mitsubishi Cement, Sumitomo Osaka Cement; AGC (glass); regional ready-mix co-ops; paint and waterproofing chemicals (naphtha-based)", "Price-taker on commodity prices; scale buyer; relies on escalation clauses and fast pass-through"],
        ["Equipment and systems", "Mitsubishi Electric, Hitachi, Toshiba Elevator; Daikin, Takasago Thermal, Taikisha, Kinden (HVAC/MEP); Komatsu, Hitachi Construction Machinery, Kobelco; Herrenknecht (TBM)", "Specifier and integrator; competes on coordination; supplier capacity tight in data centres"],
        ["Trades and labour", "Specialist subcontractors (partner association†); technician and foreign trainee labour pool", "Dominant buyer but labour-short; unit costs rising; 2024 overtime cap"],
        ["Design and JV partners", "In-house design; Nikken Sekkei, Nihon Sekkei; JV partners Kajima, Taisei, Shimizu, Takenaka, Hazama Ando on mega-projects", "Competitor-collaborators; JV risk-sharing on civil mega-projects"],
        ["Obayashi group", "Obayashi (parent); Webcor, Kraemer North America, E.W. Howell, James E. Roberts-Obayashi, MWH Constructors, GCON (US); Multiplex (AU/UK/CA, pending); Thai Obayashi, Obayashi Singapore, Taiwan and Indonesian units; Obayashi Shinseiwa Real Estate; Cypress Sunadaya", "Design-build integrator: where the margin is made and the risk sits"],
        ["Customers", "MLIT, NEXCO, JR Tokai, JRTT, local governments; developers (Mitsui Fudosan, Mitsubishi Estate, Mori Building, Sumitomo Realty, Tokyu†); manufacturers, fabs and data-centre operators; US technology, healthcare and water clients", "Concentrated public clients with leverage on price; repeat private clients"],
        ["Enablers", "Banks (MUFG, SMBC, Mizuho typical†); insurers and surety; JCR/R&I; regulators MLIT, JFTC, labour standards offices", "Net cash means low dependence on lenders"],
    ], widths=[2.8, 8.4, 5.8], size=7.5)
    para(d, "Obayashi's own filings do not name its key suppliers or customers beyond the public sector and standard industry disclosure; named entities above are well-documented industry participants rather than disclosed Obayashi contracts†.", 7.5, True, GREY)


def financials(d):
    h1(d, "8. Financial performance: five years, segments, geography and KPIs")
    h2(d, "8.1 Consolidated (JPY bn, JGAAP, fiscal years ending March)")
    table(d, ["", "FY3/22", "FY3/23", "FY3/24", "FY3/25", "FY3/26", "FY3/27E guide"], [
        ["Net sales", "1,922.9", "1,983.9", "2,325.2", "2,590.8", "2,586.3", "2,945.0"],
        ["growth", "n/a", "+3.2%", "+17.2%", "+11.4%", "-0.2%", "+13.9%"],
        ["Operating income (EBIT)", "41.1", "93.8", "79.4", "142.5", "194.7", "180.0"],
        ["EBIT margin", "2.1%", "4.7%", "3.4%", "5.5%", "7.5%", "6.1%"],
        ["EBITDA (est., D&A c.50)", "c.90", "c.144", "c.129", "c.192", "c.245", "c.230"],
        ["Ordinary income", "49.8", "100.8", "91.5", "152.2", "204.1", "183.0"],
        ["Net income (attributable)", "39.1", "77.7", "75.1", "145.4", "173.8", "157.0"],
        ["Net margin", "2.0%", "3.9%", "3.2%", "5.6%", "6.7%", "5.3%"],
        ["EPS (JPY)", "54.6", "108.3", "104.7", "202.9", "249.4", "c.229"],
        ["DPS (JPY)", "32", "42", "75", "81", "88", "94"],
    ], widths=[4.0, 2.1, 2.1, 2.1, 2.1, 2.1, 2.5], size=8, hl_rows=(2, 3))
    para(d, "Source: search summaries of tanshin data (irbank/Kabutan-type tables for FY3/22-25; BUILT, Nikkei and japanir for FY3/26)†. FY3/27 EPS is guided NI over c.686m shares. EBITDA is an estimate (assumed constant D&A). Conflicts: a summary quoted FY3/25 sales of JPY 2,620bn; the 2,590.8bn figure is consistent with FY3/26 growth of -0.2%.", 7.5, True, GREY)
    image(d, A + "op_trend.png", 13.5)
    h3(d, "Trend commentary")
    bullets(d, [
        "**FY3/22-23 (recovery from trough):** margin 2.1% to 4.7% as COVID disruption faded and legacy losses rolled off; November 2022 saw a forecast cut as materials inflation hit domestic building.",
        "**FY3/24 (inflation squeeze):** sales +17% but OP -15% on material and labour inflation and a weaker gross margin in building (non-consolidated completed-works margin was guided to 6.9%, -1.4pt†); the capital-policy shift in March 2024 came while earnings were weak.",
        "**FY3/25-26 (margin step-up):** OP +79% then +37%. Drivers named by the company: additional and change orders on large domestic building jobs, higher-margin projects, lower costs, real estate sales, and a fall in low-margin legacy backlog. FY3/26 sales were flat; all growth was margin.",
        "**FY3/27E:** sales +13.9% (early-stage projects, GCON consolidation) but OP -7.5% as new, lower-margin work enters the mix; gross margin guided at 13.0%.",
    ], 8.5)
    h2(d, "8.2 Segments and geography")
    para(d, "Only FY3/26 segment data could be retrieved. Prior-year segment tables sit in the tanshin PDFs (links in the Appendix). Obayashi does not disclose net income by segment.")
    table(d, ["FY3/26 (JPY bn)", "Sales", "% sales", "EBIT", "EBIT margin", "EBITDA", "Comment"], [
        ["Domestic building", "1,138.8", "44%", "104.0", "9.1%", "n/a", "Profit engine; change orders and better-margin jobs"],
        ["Domestic civil", "426.6", "16%", "40.9", "9.6%", "n/a", "Public works; Linear and resilience-linked"],
        ["Overseas building", "508.0", "20%", "11.9", "2.3%", "n/a", "US; GCON consolidated from Dec 2025"],
        ["Overseas civil", "336.0", "13%", "14.7†", "4.4%", "n/a", "Expanding; one source gives OP 8.3bn"],
        ["Real estate, other (derived)", "177.0", "7%", "23.0", "c.13%", "n/a", "Includes property sales gains"],
        ["Japan (derived)", "c.1,742", "67%", "c.168", "c.9.6%", "n/a", "Domestic building + civil + real estate/other"],
        ["Overseas", "843.9", "33%", "26.6", "3.2%", "n/a", "North America plus Asia (Asia sales c.JPY 271bn†)"],
    ], widths=[3.5, 1.8, 1.5, 1.6, 2.0, 1.6, 5.0], size=7.5)
    para(d, "Segment EBITDA is not derivable from the data retrieved (segment depreciation is in the yuho notes). Segment net income is not disclosed.", 7.5, True, GREY)
    h2(d, "8.3 Operating KPIs")
    table(d, ["KPI", "Latest", "Trend / comment"], [
        ["Orders received (consolidated)", "FY3/26 c.JPY 3,009bn†; Q1 FY3/27 JPY 577.5bn", "Q1 -7.2% y/y; FY3/27 target JPY 3,100bn"],
        ["Order backlog", "c.JPY 2,911bn at 31 Mar 2026†", "c.1.1x sales; one summary shows a conflicting JPY 788bn (likely garbled)"],
        ["Gross margin on completed works", "Guided 13.0% FY3/27", "Company aims to hold c.13%; up from c.7% on one non-consolidated measure in FY3/24†"],
        ["Operating margin", "7.5% FY3/26; 5.2% Q1 FY3/27 (3.0% a year earlier)", "Seasonally weakest in Q1; Q1 progress vs full-year ordinary guidance 19.9% vs 16.2% five-year average"],
        ["Overseas share of sales", "c.33%", "Rising with GCON and Multiplex"],
        ["ROE / ROIC", "14.4% / 8.4% (company, FY3/26†); guided 12.3% / 7.4% FY3/27", "Above plan targets of 10% / 5%; our calc of ROE is c.13.5%"],
        ["Equity ratio", "40.0%", "Equity JPY 1,316bn (plan target JPY 1tn exceeded)"],
        ["Operating cash flow / investing CF / financing CF", "JPY 252.9bn / -84.4bn / -141.4bn†", "Financing outflow reflects dividends and buybacks"],
        ["Capex, D&A, headcount", "n/a", "Not retrieved; see yuho"],
        ["Cross-holdings (market value)", "JPY 288.8bn = 21.9% of net assets†", "Target 20% by March 2027; 17.5% including agreed sales"],
    ], widths=[4.6, 5.4, 7.0], size=7.6)


def earnings(d):
    h1(d, "9. Earnings calls, sentiment and the latest result")
    para(d, "**Caveat:** Obayashi's briefing Q&A transcripts (JP PDFs on its IR site) could not be opened. The summary below is reconstructed from results headlines, company releases and press summaries, so the sentiment read is qualitative.", 9)
    h2(d, "9.1 What management is focused on")
    bullets(d, [
        "**Profit over volume:** 'selective' order-taking and holding completed-works gross margin around 13%.",
        "**Capital efficiency:** ROE 10%+, DOE c.5%, JPY 100bn buyback programme, cross-holding reduction to 20% of net assets by March 2027.",
        "**Overseas and tech platform build-out:** MWH (water), GCON (data centres/semiconductors), Multiplex; real estate and data-centre development; wood and renewables.",
        "**Caution on the order environment from FY3/28** citing the Middle East situation and cost trends (FY3/26 Q4 Q&A†).",
    ], 8.8)
    h2(d, "9.2 Sentiment trajectory (qualitative, headline-based)")
    table(d, ["Period", "Tone", "Evidence"], [
        ["FY3/23 (Nov 2022)", "Defensive", "Forecast cut as materials inflation and delivery delays hit building margins"],
        ["FY3/24", "Cautious, then reform-minded", "Profit down 15%; March 2024 capital-policy pivot lifts sentiment"],
        ["FY3/25", "Confident", "Record profits; first buyback tranche; plan targets reached early"],
        ["Q3 FY3/26 (Feb 2026)", "Positive but not beating", "Ordinary +33% but below analyst consensus; stock hit ATH 27 Feb"],
        ["FY3/26 (13 May 2026)", "Prudent", "Beat forecasts but FY3/27 guided down; shares -7.8% intraday"],
        ["Q1 FY3/27 (7 Aug 2026)", "Measured", "OP +107%, guidance unchanged, orders -7.2%; progress 19.9% of ordinary guide"],
    ], widths=[3.6, 3.4, 10.0], size=7.8)
    para(d, "Shift: from defensive (2022) to confident (2024-25) to deliberately conservative (2026). The tone is consistent with a management that has learned to guide low and beat.", 8.5)
    h2(d, "9.3 Latest result: Q1 FY3/27 (April-June 2026, reported 7 August 2026)")
    table(d, ["JPY bn", "Q1 FY3/27", "Q1 FY3/26", "Change", "Comment"], [
        ["Net sales", "623.4", "c.523.8", "+19.0%", "Domestic building and civil progress on large backlog; GCON consolidated"],
        ["Operating income", "32.7", "c.15.8", "+107%", "OP margin 5.2% vs 3.0%; also property sales"],
        ["Ordinary income", "36.4", "c.18.4", "+98.2%", "19.9% of FY guide (JPY 183bn) vs 16.2% five-year average"],
        ["Net income", "39.0", "c.18.1", "+116%", "Exceeds OP: c.JPY 20bn securities gain; not a clean read"],
        ["Orders", "577.5", "c.622", "-7.2%", "Down despite higher sales; target FY JPY 3,100bn"],
    ], widths=[3.2, 2.2, 2.2, 2.0, 7.4], size=7.8)
    bullets(d, [
        "**Versus expectations:** consensus full-year ordinary profit stood at JPY 193.2bn vs company guidance JPY 183bn (kabuyoho†), i.e. the Street was already above guidance. A Q1-specific consensus and surprise percentage could not be found; the Q1 print itself was well ahead of the year-ago base, and guidance was left unchanged.",
        "**Segment drivers:** domestic building (profitable large jobs), domestic civil and overseas civil volumes, GCON in overseas building, and property sales in real estate.",
        "**Margins:** operating margin 5.2% vs 3.0%; full-year guide implies 6.1%, which looks beatable if Q1 is representative, though Q1 is seasonally light.",
        "**Guidance and tone:** unchanged guidance (sales JPY 2,945bn, OP JPY 180bn, NI JPY 157bn); DPS JPY 94 (47 interim). Tone cautious on orders.",
        "**Balance sheet flags:** FY3/26 operating cash flow JPY 253bn vs investing outflow JPY 84bn; net cash JPY 84bn†. Watch contract assets and receivables, the Multiplex purchase (about JPY 86bn cash) and goodwill build.",
        "**Market reaction:** the shares were around JPY 2,990 by 28 August and hit the YTD low of JPY 2,891 on 19 August, i.e. the market sold a strong print: it is discounting margin peaking and order weakness, not Q1 earnings.",
        "**Unusual versus history:** net income above operating income for two consecutive periods (gain-driven); sales +19% with orders -7%; consensus above guidance.",
    ], 8.5)


def eps_section(d):
    h1(d, "10. EPS estimates, FY3/27 to FY3/29")
    para(d, "Method: build ordinary income from operating income plus modest non-operating income, add an extraordinary-gain line for securities sales (the main swing factor), apply a 30% tax rate, and divide by a share count reduced by buybacks. Industry growth is modelled as low-single-digit nominal sales growth; no share gains assumed; price/mix held at a c.13% completed-works gross margin; operating leverage limited by labour and SG&A inflation; financing costs are immaterial given net cash.")
    rows = []
    for name, s in (("Bear", BEAR), ("Base", BASE), ("Bull", BULL)):
        for i, fy in enumerate(("FY3/27E", "FY3/28E", "FY3/29E")):
            x = s[i]
            rows.append([f"{name} {fy}", f"{x['sales']:,.0f}", f"{x['op']:.0f} ({x['opm']:.1f}%)", f"{x['ordi']:.0f}", f"{x['gain']:.0f}", f"{x['ni']:.0f}", f"{x['shares']}", f"{x['eps']:.0f}"])
    table(d, ["Scenario / year", "Sales (JPY bn)", "OP (margin)", "Ordinary", "Gains", "NI", "Avg shares (m)", "EPS (JPY)"], rows, widths=[3.0, 2.2, 2.6, 1.9, 1.5, 1.5, 2.3, 2.0], size=7.6, hl_rows=(3, 4, 5))
    bullets(d, [
        f"**Base case:** EPS JPY {BASE[0]['eps']:.0f} / {BASE[1]['eps']:.0f} / {BASE[2]['eps']:.0f}. FY3/27E OP of JPY 192bn is 7% above guidance (consensus c.JPY 193bn ordinary) with JPY 40bn of gains (Q1 JPY 20bn already booked). Gains fade and margin eases to c.6.5% as new, lower-margin work flows through, so EPS dips in FY3/28.",
        f"**Underlying EPS (ex-gains)** is c.JPY {(BASE[0]['ordi']*0.7)*1000/686:.0f} / {(BASE[1]['ordi']*0.7)*1000/680:.0f} / {(BASE[2]['ordi']*0.7)*1000/672:.0f}, which is the right base for multiple-setting; FY3/26's JPY 249 included an estimated JPY 30-35bn of net one-off gains.",
        "**Share count:** c.692m today (market cap / price), falling c.1% a year if the JPY 100bn programme and a successor policy continue; no dilution from options (executive stock awards are small).",
        "**Dividend:** DOE c.5% on equity of c.JPY 1.3tn implies c.JPY 94-100 per share; base DPS 94 / 98 / 102.",
        "**Where we differ from the company:** FY3/27 OP JPY 192bn vs guidance JPY 180bn; where we may be wrong: a Middle East-driven cost shock hitting the backlog.",
    ], 8.6)
