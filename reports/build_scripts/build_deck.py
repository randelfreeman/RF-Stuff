import sys; sys.path.insert(0, ".")
from deckkit import *

FIG = "/home/user/RF-Stuff/reports/figures/"
S = []

# 1. Cover
S.append(f"""<div class='slide cover'>
<div class='kick'>INVESTMENT COMMITTEE MEMO</div>
<h1>Tokyo Tatemono<br/>Co., Ltd.</h1>
<div class='sub'>TSE: 8804 — Cheap equity, fair enterprise, hostage to rates</div>
<div><span class='btn fill'>RECOMMENDATION: HOLD</span><span class='btn line'>12-MO TARGET: ¥3,400 (+5.9%)</span></div>
<div class='facts'>
 <div>Reference price ¥3,211<br/>(2 Oct 2026 close)</div>
 <div>52-wk range<br/>≈¥2,994–¥4,374</div>
 <div>Mkt cap / EV<br/>¥668bn / ¥2.12tn</div>
 <div>Net debt<br/>¥1.44tn (12.0x)</div>
</div>
<div class='coverright'>
 <div class='big'>0.65x</div><div class='bigl'>P/NAV — NAV ≈¥4,937 per share; equity trades at a ~31% haircut to appraised values</div>
 <div class='big'>10.3x</div><div class='bigl'>FY2026 P/E vs 13.35x listed-developer median — but EV/Sales sits exactly on the peer regression line</div>
 <div class='big blue'>¥3,400</div><div class='bigl' style='border-bottom:none'>12-mo target = probability-weighted value (bear ¥2,300 / base ¥3,450 / bull ¥4,400)</div>
</div>
<div class='foot'>Prepared for Investment Committee review | 4 October 2026</div>
</div>""")

# 2. Executive summary
S.append(slide(header("Executive summary", "Recommendation", "Hold: cheap on equity multiples, fair on enterprise value — leverage explains the gap") +
 tiles([("10.3x", "FY2026 P/E (guidance EPS) — 23% below the 13.35x peer median"),
        ("0.65x", "P/NAV — NAV ≈¥4,937 (book ¥2,930 + after-tax unrealised gains ¥2,007)"),
        ("12.0x", "Net debt / EBITDA — the highest in the listed peer group (median 9.2x)"),
        ("¥3,400", "12-mo target (+5.9% vs ¥3,211); ≈+10% total return with dividends"),
        ("25%", "Bear-case probability we assign (¥2,300: exit channel stalls, cap rates +50bp)")]) +
 "<div class='cols'><div class='col'><h3>Why now — a decision point, not an entry point</h3>" +
 bullets([("Sector de-rating, not a company problem:", "−26.6% from the Feb-2026 high while guidance rose; Mitsui, Mitsubishi Estate and Sumitomo fell 34–42%"),
          ("Execution ahead of plan:", "record FY2025 OP ¥95.8bn; FY2026 guide raised to OP ¥105.5bn / NI ¥65.0bn / DPS ¥126; 2025–27 targets a year early"),
          ("Rates are the swing factor:", "BOJ 1.25% (18 Sep), 10-yr JGB ≈2.9–3.0%; ~54% of FY2024–26E OP growth is absorbed below the OP line"),
          ("Capital-policy optionality:", "plan met early → new capital policy likely with FY2026 results (mid-Feb 2027)")], tight=True) +
 "</div><div class='col'><h3>What has to go right</h3>" +
 bullets(["2H FY2026 operating profit of ≈¥65.7bn — the record, hotel-led investor-sale programme must close at margin",
          "10-yr JGB stays below ~3% and prime cap rates hold ≈3.2%, so J-REIT and private buyers keep bidding",
          "Office rent reversion (vacancy 1.87%, asking rents +12.5% YoY) keeps outrunning refinancing costs",
          "Year-end debt falls back toward ¥1.40tn and D/E toward the ≈2.4x guide (2.53x at June)"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("Position sizing:", "do not initiate at ¥3,211. Accumulate below ~¥3,000 (≈0.6x NAV, 9.3x FY2027E EPS) or on Q3 + year-end evidence. A levered, rate-sensitive developer — size as a rates-and-capital-policy position, not a core NAV compounder.") + "</div>"))

# 3. Business overview
S.append(slide(header("Business overview", "Context", "Tokyo Tatemono at a glance") +
 "<div class='cols'><div class='col'><h3>What it does</h3>" +
 bullets(["Japan's oldest listed developer (founded 1896, Yasuda/Fuyo lineage): a mid-sized Tokyo landlord-developer clustered around Tokyo Station — Otemachi Tower, Tokyo Square Garden, TOFROM YAESU (completed Feb 2026)",
          "Four profit engines: rent (stable), sales of stabilised buildings to investors (fast-growing, cyclical), Brillia condos (booked at handover), fees (brokerage, ~90,000 NPC24H parking spaces, resorts, asset management)",
          "J-GAAP, December year-end; ¥1.54tn of debt funds a ¥1.66tn (fair value) rental portfolio"], tight=True) +
 "<h3 style='margin-top:0.12in'>Segment mix — FY2025</h3>" +
 table(["Segment", "Revenue", "Op. profit", "Margin", "Comment"],
       [["Building", "¥220.2bn", "¥67.1bn", "30.5%", "Rent + record investor sales"],
        ["Residential", "¥165.1bn", "¥25.6bn", "15.5%", "Handover timing; 1H26 trough"],
        ["Asset Service", "¥63.5bn", "¥11.5bn", "18.1%", "Brokerage, resales, NPC24H"],
        ["Other", "≈¥25.8bn", "¥4.2bn", "16.2%", "Resorts, AM; overseas −¥6.9bn (equity method)"],
        ["Group", "¥474.6bn", "¥95.8bn", "20.2%", "After ≈−¥12.5bn corporate costs"]], small=True, col_widths=["17%", "15%", "15%", "11%", "42%"]) +
 "</div><div class='col'><h3>Where the power sits in the supply chain</h3>" +
 bullets([("Upstream:", "TT controls the scarce inputs — Yaesu/Kyobashi redevelopment rights and Tokyo approvals; construction is outsourced to Taisei, Obayashi and Kajima, which hold pricing power (+5.1% costs)"),
          ("Midstream:", "develop, lease and operate in-house (Tokyo Fudosan Kanri, Prime Place, NPC24H, Tokyo Tatemono Resort)"),
          ("Downstream:", "exit via its own platform — sole sponsor of Japan Prime Realty (TRIM 100%), a private REIT and funds — booking the gain and keeping the fees")], tight=True) +
 "<div style='margin-top:0.15in'>" + callout("The single most distinctive fact:", "TT owns both the scarce input (Tokyo Station redevelopment rights) and its own exit channel (JPR) — but funds the loop with the most levered balance sheet among listed peers (12x net debt/EBITDA).", dark=True) + "</div>" +
 "</div></div>"))

# 4. Setup
S.append(slide(header("The setup", "Context", "A 2.3x run to the February 2026 high, then a rate-driven 27% de-rating") +
 "<div class='cols'><div class='col w60'>" + img(FIG + "fig01_price_history.png") +
 "<div class='note'>Path joins reported year-end, monthly (2026) and event-day closes; shaded bands are annual high–low ranges.</div></div>" +
 "<div class='col w40'><h3>Key catalysts</h3>" +
 "".join(f"<div style='margin:0.07in 0 0.09in 0; padding-bottom:0.07in; border-bottom:1px solid #E3E6EB'><div style='color:#2F6FD0;font-weight:700;font-size:10.5pt'>{d}</div><div style='font-size:10.3pt;line-height:1.3'>{t}</div></div>" for d, t in [
   ("2020 – 2025", "Price +150.6% (TSR +197%, ~24%/yr) as EPS compounded 14%/yr and the stock re-rated in 2025."),
   ("14 NOV 2025", "Q3 guidance and dividend raised: +10.4% in one session — the only >10% single-day move."),
   ("27 FEB 2026", "All-time high ¥4,374 (+20.5% in February) after the FY2025 beat and FY2026 guidance above consensus."),
   ("MAR – MAY 2026", "JGB spike and a weak Q1 (NI −60%): two −21% drawdowns; 2026 low ¥3,083 on 28 May."),
   ("6 AUG 2026", "1H beat; FY2026 guidance raised (OP ¥105.5bn, NI ¥65.0bn, DPS ¥126) — muted reaction."),
   ("18 SEP 2026", "BOJ to 1.25%; shares break their rising-low support — ¥3,211 on 2 Oct (−26.6% from peak).")]) +
 "</div></div>"))

# 5. Peer table
S.append(slide(header("Question 1 — Is Tokyo Tatemono undervalued?", "Valuation", "Cheap on equity multiples — not on enterprise value") +
 table(["Metric", "Tokyo Tatemono", "Mitsui Fud.", "Mitsubishi Est.", "Sumitomo RE", "Tokyu Fud. HD", "Nomura RE", "Hulic", "Peer median (8)"],
       [["Forward P/E", "10.3x", "14.3x", "18.6x", "13.4x", "9.4x", "9.2x", "10.9x", "13.35x"],
        ["P/B", "1.10x", "1.25x", "1.61x", "1.16x", "1.03x", "0.99x", "1.39x", "1.25x"],
        ["EV/Sales", "4.47x", "3.15x", "4.36x", "6.39x", "2.10x", "2.66x", "4.68x", "4.52x"],
        ["EV/EBITDA", "17.7x", "15.9x", "17.4x", "18.1x", "11.2x", "15.8x", "16.7x", "17.0x"],
        ["EBIT margin", "20.2%", "14.7%", "18.9%", "28.3%", "13.4%", "14.7%", "25.7%", "22.3%"],
        ["Net debt / EBITDA", "12.0x", "8.3x", "7.4x", "10.0x", "7.1x", "10.4x", "10.1x", "9.2x"],
        ["Dividend yield", "3.9%", "2.45%", "1.35%", "1.61%", "3.81%", "4.75%", "3.86%", "3.25%"],
        ["ROE", "10.5%", "8.7%", "8.5%", "9.2%", "11.2%", "10.7%", "13.1%", "9.1%"]], hl_col=1, small=True) +
 "<div class='note'>Tokyo Tatemono at ¥3,211 (2 Oct 2026), EV on the 30 Jun 2026 balance sheet; peers priced 7 Aug–30 Sep 2026, last fiscal year (mostly FY3/2026). Median includes Heiwa RE and Keihanshin Bldg. Source: peer dataset (Shikiho, kabuyoho, company filings via search extracts).</div>" +
 "<div class='cols' style='margin-top:0.18in'><div class='col'><h3>What the comparison shows</h3>" +
 bullets(["Equity screens cheap: P/E 23% and P/B 12% below the peer median, with an above-median 3.9% yield and 10.5% ROE",
          "Enterprise screens fair: EV/Sales 4.47x vs 4.52x median; EV/EBITDA 17.7x vs 17.0x; EV/EBIT 22.2x vs 22.0x",
          "The gap is debt: 12.0x net debt/EBITDA after a ¥191bn 1H debt build — the highest in the group"], tight=True) +
 "</div><div class='col'><h3>The honest counter-read</h3>" +
 bullets(["On the Dec-2025 balance sheet (before the seasonal build) EV/EBITDA is 15.6x — some of the 'fair' read is timing",
          "Against its own history the stock is full: EV/Sales above its 3.53–4.09x FY2021–25 range; P/E above its 7.0–9.9x three-year band",
          "Hulic and Mitsubishi Estate earn their premia with lower leverage or higher margins — the multiple gap is partly earned"], grey=True, tight=True) +
 "</div></div>"))

# 6. Regression
S.append(slide(header("Question 1 — Is Tokyo Tatemono undervalued?", "Valuation", "The peer regression says fair on EV — the 'discount' is leverage, not mispricing") +
 "<div class='cols'><div class='col w60'><h3>EV/Sales vs EBIT margin — 8 listed developers</h3>" + img(FIG + "fig06_regression_ev_sales_ebit_margin.png", "max-height:4.05in; object-fit:contain") +
 "<div class='note'>OLS, Tokyo Tatemono excluded from the fit: EV/Sales = −1.974 + 0.3208 × EBIT margin (%); R² = 0.856, t = 5.97 (p ≈ 0.001), n = 8.</div></div>" +
 "<div class='col w40'><h3>Why this regression matters</h3>" +
 bullets(["A strong fit: margin (how much of a company is leasing vs develop-to-sell) explains ~86% of peers' EV/Sales",
          "Tokyo Tatemono sits on the line — actual 4.47x vs fitted 4.50x → implied ¥3,271 per share (+1.9%), close to our ¥3,400 target",
          "Very sensitive: equity is only ~31% of EV, so each 0.1x of EV/Sales = ¥228/share; variants span ¥2,376 (large caps only) to ¥4,477 (Dec-2025 balance sheet)",
          "Upside requires the June debt peak to unwind (→ ¥4,477) or above-peer growth to be capitalised (forward basis → ¥3,833) — exactly what 2H FY2026 will test"], tight=True) +
 "</div></div>"))

# 7. Value trap / EPS
S.append(slide(header("Question 2 — Value trap, or genuine opportunity?", "Value trap", "Not a classic trap — but growth after FY2026 is eaten by the cost of money") +
 "<div class='cols'><div class='col w60'>" +
 table(["¥bn unless per share", "FY2025A", "FY2026E", "FY2027E", "FY2028E"],
       [["Operating income", "95.8", "107.0", "113.0", "118.0"],
        ["Net non-operating cost", "17.6", "22.0", "24.0", "26.5"],
        ["Ordinary income", "78.2", "85.0", "89.0", "91.5"],
        ["Net income", "58.9", "65.4", "66.8", "67.9"],
        ["EPS (¥)", "283", "315", "323", "330"],
        ["EPS growth", "−10.3%", "+11.4%", "+2.6%", "+2.0%"],
        ["DPS at 40% payout (¥)", "105", "126", "129", "132"]], hl_col=2) +
 "<div class='note'>Our estimates (report Section 8). FY2026 guidance: OP ¥105.5bn, NI ¥65.0bn (EPS ≈¥313); consensus NI ¥66.5bn (≈¥320); Toyo Keizai FY2027 EPS ≈¥311. FY2027–28 consensus not available.</div></div>" +
 "<div class='col w40'><h3>Reading the earnings path</h3>" +
 bullets(["EPS compounded 14%/yr FY2021–25 and book value ~9%/yr — the earnings base is real and growing",
          "FY2026E growth is more than fully explained by a +¥14bn step-up in investor-sale profit; we assume −¥4bn in FY2027E as cap rates temper demand",
          "Financing costs rise from ¥17.6bn to ¥26.5bn: OP +¥11bn over FY2026–28E, but pre-tax only +¥3.5bn",
          "Unrealised gains grew only 3.9%/yr (¥515bn → ¥600bn): NAV is being harvested, not compounded"], tight=True) +
 "<div style='margin-top:0.12in'>" + callout("Verdict:", "a structural, leverage-linked discount rather than a trap. Closing it needs a capital-policy catalyst (buybacks funded by asset sales), not more earnings growth.") + "</div>" +
 "</div></div>"))

# 8. DuPont
S.append(slide(header("Diligence check", "Diligence", "DuPont: leverage, not margin, carries the 10% ROE") +
 tiles([("12.4%", "Net margin, FY2025 (NI ¥58.9bn ÷ revenue ¥474.6bn)"),
        ("0.22x", "Asset turnover (revenue ÷ average total assets of ~¥2.2tn)"),
        ("3.87x", "Equity multiplier (average assets ÷ average shareholders' equity)"),
        ("≈10.5%", "ROE FY2025 (FY2024 12.8% flattered by ≈¥20–25bn one-off gains)")]) +
 "<div class='cols'><div class='col'><h3>The DuPont decomposition</h3>" +
 bullets(["ROE ≈ 12.4% × 0.22x × 3.87x ≈ 10.5% — almost four times leverage turns a ~2.7% ROA into a double-digit ROE",
          "ROIC on book invested capital is only 3.1–3.7% (FY2021–25), barely above a rough weighted cost of capital",
          "Asset turnover is structurally low (asset-heavy landlord); margin is cyclical (sale gains); leverage is the lever being pulled"], tight=True) +
 "</div><div class='col'><h3>What this means for the equity</h3>" +
 bullets(["Every +100bp on fully repriced debt removes ≈¥15bn pre-tax (~16% of net income, ≈¥51/share)",
          "1.10x P/B with ≈10.7% ROE implies near-zero long-run growth at a 9–10% cost of equity — the market treats 10% ROE as the ceiling",
          "A re-rating needs better returns per unit of risk: recycling gains into buybacks at 0.65x NAV, not more balance-sheet growth"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("The cleanest diligence takeaway:", "Tokyo Tatemono's ROE is a leverage product. Track year-end debt/equity and the non-operating line, not the operating margin.", dark=True) + "</div>"))

# 9. NAV
S.append(slide(header("Diligence check", "Diligence", "0.65x NAV: the market haircuts appraised values by ~31% — the private market does not") +
 "<div class='cols'><div class='col w60'>" + img(FIG + "fig07_nav_bridge.png", "max-height:3.9in; object-fit:contain") + "</div>" +
 "<div class='col w40'><h3>What the NAV discount implies</h3>" +
 bullets(["NAV ≈¥4,937 = book ¥2,930 + after-tax unrealised gain ¥2,007 (rental property fair value ¥1,658bn vs book ¥1,058bn; 30.6% tax)",
          "At ¥3,211 the market credits only ≈¥58bn of the ¥416bn after-tax gain → a 31% haircut, ≈+136–181bp of cap-rate expansion",
          "Private marks disagree: JREI prime cap rate flat at 3.2% for seven surveys; Blackstone paid ≈¥400bn for Tokyo Garden Terrace (2025)",
          "Peers: Mitsubishi Estate and Mitsui ≈0.64x, Sumitomo ≈0.47–0.51x; TT's own 2026 range 0.62x (May) – 0.90x (Feb)",
          "Cushion: fair value would need to fall ~36% before reaching book; each ¥100bn of impairment ≈ ¥482/share"], tight=True) +
 "</div></div>"))

# 10. Activism
S.append(slide(header("Is there an activist in here?", "Catalyst", "No campaign yet — but Tokyo Tatemono fits the activist template") +
 "<div class='cols'><div class='col'><h3>What the register and newsflow show</h3>" +
 bullets([("No activist stake, letter or proposal", "found 2018–2026 (negative finding from limited searches)"),
          ("Passive register:", "Master Trust 18.02%, Custody Bank 12.01%; ≥5% filers are index/asset managers — BlackRock 6.42%, SMTAM 5.07%, Nomura AM"),
          ("Thin stable base:", "Fuyo-group insurers ≈4.3% and falling (Sompo 2.28% → 2.00%); Hulic cross-holding 1.22%; insiders 0.08%"),
          ("Short interest negligible:", "GS International peaked ~1.1% in 2025, below 0.5% since Apr 2025; margin ratio 2.82x on tiny balances")], tight=True) +
 "</div><div class='col'><h3>Direct answer to the activist question</h3>" +
 bullets(["Peers are already targets: Elliott holds 3.5% of Sumitomo Realty; Mitsui Fudosan conceded a ≥50% total payout in 2024; Oasis' Tokyo Dome campaign ended in a sale",
          "TT's gaps are the classic asks: 0.65x NAV, a 40% payout with only a token ¥3bn buyback, ≥¥130bn of cross-holding/asset sales still to come, an ex-banker non-independent chair and three representative directors",
          "Pre-emptive steps blunt the case: payout raised to 40% a year early, one-year director terms (2025), cross-shareholdings ≤10% of net assets by 2027"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("Bottom line:", "an activist minority stake is the most likely event path (our judgement: 20–30% over three years). The ask would be buybacks funded by asset sales and the ~¥35bn Hulic stake, a ≥50% total payout, and an independent chair.") + "</div>"))

# 11. Take-private candidate
S.append(slide(header("Question 3 — Activist target, or take-private candidate?", "Our assessment", "No blocking holder — but size and leverage make a bid unlikely") +
 tiles([("≈44%", "Top-10 holders — mostly trust-bank custody and foreign custodians"),
        ("≈4.3%", "Fuyo-group stable holders (Meiji Yasuda, Sompo) — and falling"),
        ("¥0.9–1.0tn", "Equity value at a 30–50% premium — 3–5x the largest recent Japanese RE take-private"),
        ("12.0x", "Net debt/EBITDA already — little room left for acquisition debt")]) +
 "<div class='cols'><div class='col'><h3>Why activism can work here</h3>" +
 bullets(["No controlling or strategic shareholder; Japan's pro-M&A governance climate (METI 2023 guidelines, TSE P/B push)",
          "A clear, monetisable value gap (0.65x NAV) and listed stakes worth ≈¥56–61bn (Hulic ≈¥35bn) to fund buybacks",
          "Passive holders support capital-return proposals at a fair price"], tight=True) +
 "</div><div class='col'><h3>Why a whole-company bid is unlikely</h3>" +
 bullets(["Size: no integrated Japanese developer has been bid for; Leopalace21 (≈¥270bn, Sep 2026) is the largest recent RE take-private",
          "Leverage: a buyer inherits ¥1.44tn of net debt; LBO returns of 7–11% sit below 15–20% hurdles",
          "Relationships: Mizuho/SMBC/MUFG lenders, change-of-control terms unknown; whole-company bid probability ≈5% over three years"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("Our assessment:", "the event angle is capital-return pressure (activist or self-help) rather than a takeover. A bid, if it came, would most plausibly be a friendly share-exchange with Hulic or a break-up-minded strategic/sovereign club.", dark=True) + "</div>"))

# 12. M&A precedents
S.append(slide(header("Question 4 — Who could buy, and at what price?", "M&A", "Japanese real-estate M&A is active — but mid-cap, at 21–45% premiums") +
 table(["Announced", "Target", "Acquirer", "Price / premium", "Value"],
       [["Nov 2020", "Tokyo Dome", "Mitsui Fudosan (+Yomiuri 20%)", "¥1,300; +44.9% (post-Oasis campaign)", "≈¥120bn"],
        ["Nov 2020", "Kenedix", "SMFL Mirai Partners + ARA/ESR", "¥750; +26.5%", "≈¥165bn"],
        ["Nov 2021", "Daibiru", "Mitsui O.S.K. Lines (owned 51.9%)", "¥2,200 per share", "¥121.3bn"],
        ["Feb 2022", "31 Prince hotels (asset deal)", "GIC (from Seibu HD)", "≈2.1x seller's book", "≈¥150bn"],
        ["Mar 2022", "Mitsubishi Corp.-UBS Realty (AM)", "KKR", "≈1.4% of ¥1.7tn AUM", "¥230bn"],
        ["Oct 2024", "Samty HD", "Hillhouse (Song Bidco)", "¥3,300 per share", "n/a"],
        ["2025", "Tokyo Garden Terrace Kioicho (asset)", "Blackstone (from Seibu HD)", "≈2.9x seller's book", "≈¥400bn"],
        ["Jan / Sep 2026", "Sankei Real Estate REIT", "Tosei/GIC funds; rival bid Sep 2026", "¥125,000/unit; +20.9% (failed May)", "n/a"],
        ["Feb 2026", "Sun Frontier Fudosan (20.05%)", "Itochu", "¥2,800 partial TOB + allotment", "≈¥13.4bn allotment"],
        ["Sep 2026", "Leopalace21", "Hikari Tsushin + MBK/NEC Capital", "¥1,000; ≈+45% (trading above offer)", "≈¥270bn"]], small=True, col_widths=["11%", "24%", "26%", "26%", "13%"]) +
 "<div class='cols' style='margin-top:0.16in'><div class='col'>" +
 bullets(["28 real-estate tender offers filed Nov 2022–Sep 2026 (EDINET scan) — all small/mid-cap; premiums cluster at +21% to +45%",
          "Asset deals clear at 2–3x sellers' book: private capital pays full prices for prime Tokyo assets"], tight=True) +
 "</div><div class='col'>" + callout("Status as of this note:", "no approach, stake-building or process is visible at Tokyo Tatemono. Transaction EV/EBITDA and P/NAV multiples were not retrievable for these deals; premiums and book multiples are the usable benchmarks.") + "</div></div>"))

# 13. Takeout / LBO
S.append(slide(header("Could this be taken private — at what price?", "M&A", "A bid would price at ¥4,170–4,820 — and a classic LBO does not work") +
 table(["Premium to ¥3,211", "Price / share", "Equity ¥bn", "EV ¥bn", "P/B", "P/NAV", "P/E FY26 (guide)", "EV/EBITDA FY26E"],
       [["0%", "¥3,211", "668", "2,123", "1.10x", "0.65x", "10.3x", "16.1x"],
        ["20%", "¥3,853", "801", "2,256", "1.32x", "0.78x", "12.3x", "17.2x"],
        ["30%", "¥4,174", "868", "2,323", "1.42x", "0.85x", "13.3x", "17.7x"],
        ["40%", "¥4,495", "935", "2,390", "1.53x", "0.91x", "14.4x", "18.2x"],
        ["50%", "¥4,816", "1,002", "2,456", "1.64x", "0.98x", "15.4x", "18.7x"]], hl_col=1, small=True) +
 "<div class='note'>FY2026E EBITDA = OP guidance ¥105.5bn + D&A ≈¥26bn (estimate). Illustrative framework, not a projection of any actual transaction.</div>" +
 "<div class='cols' style='margin-top:0.16in'><div class='col'><h3>What this framework tells us</h3>" +
 bullets(["Four anchors converge on ¥4,170–4,820: peer-median P/E (≈¥4,180), Mitsubishi Estate's P/B (≈¥4,720), NAV parity (≈¥4,940), the Feb-2026 high (¥4,374)",
          "LBO at a 40% premium: EV ≈¥2.39tn (18.2x EBITDA); 11x debt capacity is what TT already owes → ≈¥0.94tn equity cheque (39% of EV)",
          "Five-year exit at entry multiple with 3–5% EBITDA growth and no deleveraging → 1.4–1.7x MOIC, 7–11% IRR"], tight=True) +
 "</div><div class='col'>" + callout("Practical read:", "the market is not pricing takeout optionality — rightly. Only a strategic or break-up buyer makes sense; for public investors the same value gap is accessible through capital policy (buybacks at 0.65x NAV).", dark=True) + "</div></div>"))

# 14. Macro risk
S.append(slide(header("Question 5 — Rates vs rents: how much of the bear case is priced?", "Macro risk", "Two inflations are racing: the rents TT can reprice and the cost of its money") +
 tiles([("1.25%", "BOJ policy rate after the 18 Sep 2026 hike — the highest since 1995"),
        ("≈2.9–3.0%", "10-year JGB (2.945% intraday in Aug 2026) — passed 2% only in Dec 2025"),
        ("1.87%", "Central-5-ward office vacancy (Aug 2026); asking rents +12.5% YoY"),
        ("3.2%", "Prime Marunouchi/Otemachi cap rate — only ≈20–30bp over the 10-yr JGB")]) +
 "<div class='cols'><div class='col'><h3>Why rates and rents are different risks</h3>" +
 bullets([("Rents:", "short (2-year) Tokyo leases reprice fast — a tailwind now (+12.5%), a headwind just as fast if the cycle turns"),
          ("Rates:", "≈¥1.5tn of mostly fixed, long-dated debt reprices gradually but relentlessly; non-operating drag ¥7.9bn (FY24) → ¥22.0bn (FY26 guide)"),
          ("Cap rates:", "the exit channel — J-REIT equity raising and private bids — is where rates bite first; TSE REIT index hit 2026 lows in May–June")], tight=True) +
 "</div><div class='col'><h3>What would resolve each one</h3>" +
 bullets(["Rents: Miki Shoji monthly data — vacancy below 2% and rent growth above 10% sustains reversion",
          "Rates: BOJ path beyond 1.25% and whether the 10-yr JGB holds below ~3% (Sell trigger: above 3.25%)",
          "Cap rates: closing of the hotel-led 2H sale programme at margin, and JPR equity issuance"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("The structural risk unique to Tokyo Tatemono among the majors:", "the most levered balance sheet in the group, funding a growth model that depends on selling assets into a buyer pool whose cost of capital is rising.", dark=True) + "</div>"))

# 15. Net verdict on macro
S.append(slide(header("Net verdict on the macro risk", "Evidence", "Both outcomes are live — and both resolve within two prints") +
 "<div class='cols'><div class='col'><h3>The bear case</h3>" +
 bullets(["Hotel-led 2H FY2026 disposals slip into 2027 as J-REIT unit prices make offerings uneconomic; FY2026 OP lands near ¥98bn",
          "BOJ to 1.5–1.75%, 10-yr JGB > 3.25%; JREI finally shows cap-rate widening; NAV −≈¥600/share; market applies a 'Sumitomo discount' (0.5x NAV)",
          "Debt/equity > 2.6x; JCR outlook negative; condo contract rates < 60%; overseas losses recur → ¥2,300 (−28%)"], tight=True) +
 "</div><div class='col'><h3>The bull case</h3>" +
 bullets(["Rent reversion on short leases outpaces refinancing; TOFROM YAESU's first full year (FY2027) and retail lease-up add recurring income",
          "Private capital keeps clearing Tokyo assets at ≈3.2% (Blackstone, GIC, Leopalace21 bid at +45%): sale gains crystallise appraisal values",
          "New capital policy in Feb 2027 adds buybacks and an ROE target above 10% → 12.5x FY2027E EPS ≈ ¥4,400 (+37%)"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("Bottom line:", "both paths are falsifiable on a known timetable — Q3 (mid-November 2026) and FY2026 results with the capital policy (mid-February 2027). That argues for patience and explicit triggers rather than buying or selling aggressively at ¥3,211.") + "</div>"))

# 16. Technicals
S.append(slide(header("What does technical analysis say?", "Technicals", "Below every moving average, but the long-term uptrend is intact") +
 tiles([("¥3,211", "Last price (2 Oct 2026); first close below the May–Sep rising-low line"),
        ("¥4,374", "All-time high (27 Feb 2026); −26.6% from peak"),
        ("¥3,083", "2026 low (28 May 2026); next supports ¥3,135 / ¥3,083 / ¥3,000"),
        ("≈¥3,550", "200-day moving-average proxy (built from monthly bars)")]) +
 "<div class='cols'><div class='col'><h3>Moving-average picture</h3>" +
 table(["Average (proxy)", "Level", "Price vs average"],
       [["50-day", "≈¥3,360", "−4.5%"], ["100-day", "≈¥3,370", "−4.7%"], ["200-day", "≈¥3,550", "−9.5%"]]) +
 "<div class='note'>Proxies built from monthly bars (daily data unavailable): ±2–3% error.</div></div>" +
 "<div class='col'><h3>Reading the chart</h3>" +
 bullets(["Monthly highs have fallen every month since February (¥4,374 → ¥3,922 → ¥3,606 → ¥3,542 → ¥3,481); short averages below the long — a death-cross-type set-up",
          "Kabuyoho's trend signal: 'sell continuation'; retail margin positioning negligible, no reportable short",
          "Annual lows keep rising (¥1,484 → ¥2,029 → ¥2,238 → ¥3,083): a de-rating within a secular uptrend, not a breakdown",
          "Turn signal: hold ¥3,083 and reclaim the ¥3,245 floor; resistance ¥3,480 / ¥3,550 / ¥3,922"], tight=True) +
 "</div></div>"))

# 17. Balance sheet & capital allocation
S.append(slide(header("Balance sheet & capital allocation", "Capital", "Conservative in form, aggressive in quantity: debt at the guide ceiling") +
 tiles([("¥1,537bn", "Interest-bearing debt at 30 Jun 2026 (+¥191bn in six months)"),
        ("¥94bn", "Cash at 30 Jun 2026 (¥152bn at Dec 2025)"),
        ("2.53x", "Debt/equity vs the ≈2.4x guide (2.27x at Dec 2025)"),
        ("A (JCR)", "Issuer rating, upgraded from A−; hybrids rated BBB+")]) +
 "<div class='cols'><div class='col'><h3>Why this balance sheet matters</h3>" +
 bullets(["Mostly long-term, fixed-rate relationship-bank debt (Mizuho, SMBC, MUFG) plus bonds — repricing is gradual but one-directional",
          "Mid-year debt is seasonally inflated (for-sale inventory ahead of 2H disposals, Blackstone/Yellow Hat building purchases, Star Mica stake) — December is the real test",
          "Operating cash flow ¥19–32bn vs OP ¥80–96bn (FY2024–25); FY2024 free cash flow −¥123bn: dividends are effectively funded by sales and debt",
          "Maturity ladder and covenants not retrievable — verify in the FY2025 Yuho"], tight=True) +
 "</div><div class='col'><h3>Capital-allocation priorities, in order</h3>" +
 bullets(["1. Dividends: payout raised to 40% a year early; DPS ¥51 (FY21) → ¥126 (FY26E), 13 straight increases",
          "2. ≈¥200bn of redevelopment FY2025–27 (Kyobashi 3-chome East, FY2029)",
          "3. ≥¥130bn of cross-shareholding and fixed-asset sales; cross-holdings ≤10% of net assets by end-2027",
          "4. Buybacks: token — one ¥3bn programme (2025), shares cancelled; the obvious gap at 0.65x NAV"], grey=True, tight=True) +
 "</div></div>"))

# 18. Catalyst calendar
S.append(slide(header("Catalyst calendar", "Catalysts", "Two prints and the BOJ decide the case over the next five months") +
 cal_row("LATE OCT & DEC 2026", "BOJ policy meetings / 10-yr JGB", "Pace beyond 1.25%; JGB above or below 3% (Sell trigger: sustained above 3.25%).", "CRITICAL") +
 cal_row("~MID-NOV 2026 (est.)", "Q3 FY2026 results", "9M OP progress vs 52.8% last year; hotel-led sale closings; condo handovers; debt.", "CRITICAL") +
 cal_row("BY 30 OCT 2026", "Leopalace21 TOB close; Sankei REIT contest", "Sector take-private premiums and private-capital appetite — read-across for NAV support.", "MEDIUM") +
 cal_row("~MID-FEB 2027 (est.)", "FY2026 results, FY2027 guidance, capital policy", "Year-end debt (≈¥1.40tn = upgrade trigger); buyback; ROE target above 10% — the largest re-rating catalyst.", "CRITICAL") +
 cal_row("LATE MAR 2027", "209th AGM", "Support for CEO/chairman; any shareholder proposals; new ≥5% non-index filers.", "HIGH") +
 cal_row("JAN–FEB 2028 (OR EARLIER)", "Next medium-term plan", "Targets toward the 2030 vision (business profit ≈¥120bn); NAV-per-share objective.", "HIGH")))

# 19. Key risks
S.append(slide(header("Key risks", "Risks", "What would make this thesis wrong") +
 risk_grid([("Exit channel closes", "J-REIT and private buyers retreat as the 10-yr JGB passes 3%; the record sale programme slips; earnings fall 20–30% and value drops to ¥2,260–2,580."),
            ("Leverage ratchet", "Debt/equity stays above the ≈2.4x guide (2.53x at June); rating pressure raises the cost of capital and closes the asset-turnover spread."),
            ("Refinancing drag", "Every +100bp, once fully repriced on ¥1.54tn, removes ≈16% of net income (≈¥51 per share); non-operating cost already ¥22bn in FY2026 guidance."),
            ("New office supply", "Yaesu 2-chome Central (Jan 2029) and TT's own Kyobashi tower (FY2029) arrive as a +12% rent cycle matures; Mitsubishi Estate can outspend."),
            ("Condo affordability", "Initial contract rate 64.8%, rising inventory; 1H condo gross margin 27.8% (−2.6pt); construction costs +5.1% a year."),
            ("Overseas & governance", "FY2025 equity-method loss −¥6.9bn, a London office project; ex-banker chair, 0.08% insider ownership, bonus tied to profit not ROE/TSR.")])))

# 20. Agenda
S.append(slide(header("If we escalate: our own agenda", "Our agenda", "Push capital policy, not strategy") +
 "<div class='cols'><div class='col'><h3>What we would push for</h3>" +
 bullets(["Disclose the leasing vs sale-gain split inside Building, and a recurring run-rate that management would underwrite without a sale market",
          "A programmatic buyback funded by the ~¥35bn Hulic stake and mature-asset sales while the stock trades at ~0.65x NAV",
          "Next plan: ROE above 10%, a ≥50% total-payout commitment (Mitsui precedent) and an explicit NAV-per-share objective",
          "Governance: an independent chair, fewer representative directors, and pay tied to ROE/TSR rather than ordinary profit"], tight=True) +
 "</div><div class='col'><h3>Sizing & monitoring</h3>" +
 bullets(["Hold / do not initiate at ¥3,211; accumulate below ~¥3,000 (≈0.6x NAV, 9.3x FY2027E EPS)",
          "Upgrade trigger: Q3 9M OP progress ahead of 52.8%, and FY2026 year-end debt back near ¥1.40tn with a funded buyback",
          "Downgrade to Sell: 10-yr JGB above 3.25%, FY2026 sales slip into 2027, year-end D/E above 2.6x, or overseas losses at FY2025 scale",
          "Watch the AGM notice (≈8 weeks before late March) and EDINET for new ≥5% non-index filers"], grey=True, tight=True) +
 "</div></div>" +
 "<div class='bottom'>" + callout("Engagement path:", "there is no controlling shareholder to lobby — the register is passive and the board is plan-driven. The most effective route is a private letter to the CEO and board ahead of the February 2027 capital-policy update, backed by the 15 questions in the full report, with the 209th AGM (late March 2027) as the escalation point.", dark=True) + "</div>"))

# 21. IC decision
S.append(f"""<div class='slide dec' style='padding:0.35in 0.6in'>
<div class='kicker'>INVESTMENT COMMITTEE DECISION</div><div class='rule' style='border-color:#2B3A58'></div>
<h1 class='title'>Recommendation: HOLD</h1>
<div class='tiles' style='margin-top:0.1in'>
 <div class='tile'><div class='v'>¥3,400</div><div class='l'>12-mo target (+5.9%) = probability-weighted value</div></div>
 <div class='tile'><div class='v'>0.65x</div><div class='l'>P/NAV; 10.3x FY2026 P/E; 3.9% yield</div></div>
 <div class='tile'><div class='v'>12.0x</div><div class='l'>Net debt / EBITDA — highest among listed peers</div></div>
 <div class='tile hl'><div class='v'>¥3,000</div><div class='l'>Accumulation trigger (≈0.6x NAV)</div></div>
</div>
<div class='cols' style='margin-top:0.1in'><div class='col' style='flex:1.45'>
{bullets(["Cheap on equity multiples, fair on enterprise value: the peer EV/Sales–EBIT-margin regression (R² 0.86) implies ¥3,271 — the discount is leverage",
          "Execution is ahead of plan (FY2026 OP guide ¥105.5bn; targets a year early), but growth now comes from asset sales and borrowed money; EPS growth slows to 2–3% after FY2026",
          "Rates are the swing factor: BOJ 1.25%, 10-yr JGB ≈3%; ~54% of FY2024–26E OP growth is absorbed below the operating line",
          "Event optionality is capital policy and activism, not a takeover: buybacks at 0.65x NAV funded by the Hulic stake and asset sales would close the gap"], tight=True)}
</div><div class='col'><div class='panel' style='padding:0.2in 0.28in'><h3>Sizing &amp; monitoring</h3>
<p style='margin:0.12in 0 0.12in 0'>Do not initiate at ¥3,211. Accumulate below ~¥3,000 or on proof: Q3 9M progress above 52.8% and December debt back near ¥1.40tn.</p>
<p style='margin:0 0 0.12in 0'>Downgrade to Sell if the 10-yr JGB holds above 3.25%, the FY2026 sale programme slips, D/E exceeds 2.6x, or overseas losses recur.</p>
<p style='margin:0'>Decisive data point: mid-Feb 2027 FY2026 results, year-end debt and the new capital policy.</p>
</div></div></div>
<div class='foot'>Tokyo Tatemono Co., Ltd. | TSE: 8804 | Reference price ¥3,211 (2 Oct 2026) | 4 October 2026 | For professional investors only — figures largely from search extracts of primary filings</div>
</div>""")

open("/tmp/lotest/tt_deck.html", "w", encoding="utf-8").write(page(S))
print("slides:", len(S))
