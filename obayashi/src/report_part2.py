from docx_helpers import _runs
from docx_helpers import *
from model import *

A = "assets/"
TK = MCAP * 1000 / PRICE  # shares m


def capital_structure(d):
    h1(d, "11. Capital structure")
    table(d, ["31 March 2026 (JPY bn)", "Amount", "Comment"], [
        ["Cash and equivalents", "430.9†", "Plus short-term investments JPY 9.8bn"],
        ["Total interest-bearing debt", "356.5† (another summary: 344.0)", "Mix of bonds, loans and commercial paper not retrieved"],
        ["Net cash", "84.2†", "Net cash position; net debt/EBITDA c.-0.3x (EBITDA est. JPY 245bn)"],
        ["Total assets / equity", "3,143.4 / 1,316.5", "Equity ratio 40.0%; equity target of JPY 1tn exceeded"],
        ["Investment securities (cross-holdings, market value)", "288.8", "21.9% of net assets; target 20% by Mar 2027; JPY 58.3bn agreed but not executed"],
        ["Operating / investing / financing cash flow", "252.9 / -84.4 / -141.4", "Financing outflow = dividends + buybacks net of debt"],
    ], widths=[5.4, 4.2, 7.4], size=7.8)
    bullets(d, [
        "**Debt maturities, covenants, interest cost:** not retrievable from search summaries. Japanese corporate bonds of this issuer type typically carry a negative-pledge clause rather than financial maintenance covenants (general market practice†, not confirmed for Obayashi's bonds). Obayashi's net interest burden is small given net cash; we recommend checking the yuho debt schedule.",
        "**Ratings:** a JCR long-term issuer rating of AA- (stable) appeared in one search summary but could not be tied definitively to Obayashi†. R&I and international ratings were not found.",
        "**Liquidity:** cash of JPY 431bn covers 1.2x gross debt. The Multiplex purchase (USD 540m, c.JPY 86bn) and a JPY 30bn remaining buyback are comfortably fundable; liquidity is not a concern.",
        "**What would change this:** a large fixed-price project loss, a working-capital reversal after the order-book expansion (operating CF has ranged from JPY 50bn to JPY 253bn in five years†), or a larger overseas acquisition.",
    ], 8.6)


def valuation(d):
    h1(d, "12. Valuation versus peers and history")
    para(d, f"At JPY 3,008, market cap is JPY {MCAP:,.0f}bn and EV (market cap less net cash) is JPY {EV:,.0f}bn. Deducting the full JPY 289bn of cross-held shares gives an adjusted EV of JPY {M['ev_adj']:,.0f}bn. Obayashi reports under JGAAP, which keeps operating leases off balance sheet; European peers report under IFRS 16, which lifts their EBITDA and EV. EV/EBITDA comparisons across the two are therefore biased in Obayashi's favour (looks cheaper), and EV/EBIT and P/E are cleaner.")
    table(d, ["Company (ticker)", "Listed", "EV/Sales", "EV/EBITDA", "EV/EBIT", "P/E", "EBIT margin", "Net debt/EBITDA"], [
        ["Obayashi (1802 JT)", "Yes", f"{M['ev_sales']:.2f}x", f"{M['ev_ebitda']:.1f}x ({M['ev_ebitda_adj']:.1f}x adj)", f"{M['ev_ebit']:.1f}x ({M['ev_ebit_adj']:.1f}x adj)", f"{M['pe_t']:.1f}x / {M['pe_g']:.1f}x fwd", "7.5%", f"{M['nd_ebitda']:.1f}x"],
        ["Kajima (1812 JT)", "Yes", "1.03x", "10.8-12.3x", "n/a", "15.3x fwd", "7.7%", "n/a"],
        ["Taisei (1801 JT)", "Yes", "1.34x", "10.3x", "n/a", "n/a (P/B 2.3x)", "9.0%", "n/a"],
        ["Shimizu (1803 JT)", "Yes", "0.63x", "8.2-8.4x", "n/a", "12.9x fwd", "5.8%", "n/a"],
        ["Vinci (DG FP)", "Yes", "1.25x", "7.7x TTM / 6.9x fwd", "10.5x", "14x", "11.9%", "n/a"],
        ["Skanska (SKA-B SS)", "Yes", "0.52x", "15.4x", "14.7x", "20x", "3.5%", "n/a"],
        ["Balfour Beatty (BBY LN)", "Yes", "0.27x", "6.8x", "n/a", "12.9x", "2.1%", "n/a"],
        ["Hochtief (HOT GR)", "Yes", "0.59x", "n/a", "22.9x", "n/a", "2.6%", "n/a"],
        ["Bouygues (EN FP)", "Yes", "0.48x", "4.9-9.9x", "9.6x", "16.8x", "3.3-5.0%", "n/a (conglomerate; excluded)"],
    ], widths=[3.6, 1.2, 1.5, 2.8, 2.3, 2.3, 1.7, 1.6], size=7.2, hl_rows=(0,))
    para(d, "Peer multiples are from aggregator search snippets (Marketscreener, TipRanks, Stockanalysis, Pitchbook), vary by date and source (e.g. Shimizu EV/EBITDA 8.2-13.5x in different sources, Kajima P/E 15.3x vs 17.4x), and EV figures are mixed-date. Treat them as indicative; a same-basis Bloomberg pull is needed before relying on them. Sales growth and FCF yield for peers were not retrieved; for Obayashi, FY3/26 sales growth -0.2%, FY3/27E +13.9%, and an FCF yield proxy of 8.1% (CFO JPY 253bn + investing CF -JPY 84bn = JPY 169bn, before financing).", 7.5, True, GREY)
    h2(d, "12.1 Versus peers and history")
    bullets(d, [
        f"**Versus Japanese Big-3:** EV/Sales of {M['ev_sales']:.2f}x compares with 0.63-1.34x; EV/EBITDA of {M['ev_ebitda']:.1f}x compares with c.8-12x; P/E of c.12-13x compares with 13-15x forward. Obayashi trades in the middle-to-lower half: cheaper than Taisei and Kajima, in line with Shimizu, despite a margin above Shimizu and in line with Kajima.",
        "**Versus global contractors:** at 8-10x EV/EBIT and 12-13x P/E, Obayashi is in line with Vinci/Balfour Beatty on P/E and cheaper than Skanska and Hochtief, but it has a much higher margin than Skanska/Balfour/Hochtief (2-4%), which argues for a premium.",
        "**Versus own history:** a historical series for P/E, P/B and EV/EBITDA could not be retrieved. From general knowledge, Obayashi traded at roughly 0.6-1.0x book and 8-12x earnings for much of 2015-2022† (approximate, unverified); at 1.6x book today the shares trade well above their own 10-year range on P/B, but below their February 2026 peak (c.2.3x book). **On earnings multiples (P/E c.12x) the stock sits within its historical range; on book multiple it is elevated.**",
        "**Conclusion: fair-to-modestly cheap.** Cheap on the regression and on a cross-holding-adjusted EV/EBITDA of c.7x; fair on P/E; not cheap on book. The discount is better explained by margin-sustainability doubts than by mispricing.",
    ], 8.6)
    h2(d, "12.2 Regression: TEV/Sales versus EBIT margin")
    image(d, A + "regression.png", 15.0)
    para(d, f"OLS across seven listed peers (Vinci, Skanska, Balfour Beatty, Hochtief, Kajima, Taisei, Shimizu): EV/Sales = 0.18 + 0.103 x EBIT margin (%), R² = 0.86, t-statistic 5.5, n = 7. At Obayashi's 7.5% margin the regression implies 0.95x EV/Sales versus 0.77x actual, a c.23% gap. Implied EV is JPY 2,455bn; adding net cash of JPY 84bn gives equity value of JPY 2,539bn, or c.JPY 3,670 per share (+22%). Caveats: n is small; the peer set mixes Japanese and global names, IFRS and JGAAP, and two points (Vinci, Taisei) carry much of the slope; margins are last-year and EVs are mixed-date aggregator figures. The earlier reference deck's regression (6 peers, EBITDA margin vs EV/Sales, implying a c.70% gap) reflects a different set that includes ultra-luxury and apparel names, and is not comparable.", 8.2)
    h2(d, "12.3 Competitor universe: listed and unlisted")
    table(d, ["Competitor", "Ticker", "Status", "Relevance"], [
        ["Kajima Corporation", "1812 JT", "Listed (TSE)", "Super-GC; largest by sales; civil and overseas strength"],
        ["Taisei Corporation", "1801 JT", "Listed (TSE)", "Super-GC; highest margin; acquiring Toyo Construction"],
        ["Shimizu Corporation", "1803 JT", "Listed (TSE)", "Super-GC; acquiring Nippon Road stake"],
        ["Takenaka Corporation", "none", "Unlisted (private)", "Fourth super-GC; design-build; no public valuation"],
        ["Daiwa House / Sekisui House", "1925 JT / 1928 JT", "Listed (TSE)", "Housing and light commercial; overlap in logistics and some commercial"],
        ["Toda / Haseko / Kumagai Gumi", "1860 / 1808 / 1861 JT", "Listed (TSE)", "Mid-tier general contractors"],
        ["Penta-Ocean / Okumura / Hazama Ando", "1893 / 1833 / 1719 JT", "Listed (TSE)", "Marine, building and civil mid-tier"],
        ["Mitsui Sumitomo Construction", "1821 JT", "Listed; being acquired by Infroneer (5076 JT)", "Mid-tier; consolidation example"],
        ["Hochtief / Turner", "HOT GR (ACS)", "Hochtief listed; Turner is its subsidiary", "US building competitor"],
        ["Skanska / Vinci / Balfour Beatty", "SKA-B SS / DG FP / BBY LN", "Listed", "US/European competitors and valuation comps"],
        ["Samsung C&T / Hyundai E&C", "028260 / 000720 KS", "Listed (KRX)", "Asia overseas competitors"],
        ["DPR / Gilbane / Kiewit / Bechtel", "none", "Private", "US data-centre, civil and industrial competitors"],
        ["Multiplex", "none", "Private (Brookfield-owned; being acquired by Obayashi)", "Australia/UK/Canada building"],
    ], widths=[4.6, 3.4, 4.2, 4.8], size=7.5)


def ma(d):
    h1(d, "13. M&A: industry transactions, takeover appeal, and Obayashi's own deals")
    h2(d, "13.1 Industry context")
    para(d, "Japanese contracting is consolidating at the mid-tier (Taisei-Toyo Construction, Infroneer-Mitsui Sumitomo Construction, Shimizu-Nippon Road, SMCC-road subsidiary) while the Big-4 buy overseas capability (Obayashi: MWH, GCON, Multiplex; Shimizu: Cross Management). In the US, specialty electrical and mechanical contractors are being bought at 7-11x EBITDA to capture data-centre demand. Japanese homebuilders (Sekisui House-MDC, Sumitomo Forestry-Tri Pointe, Daiwa House) are buying US housing. No priced 2024-26 deals for Kajima, Hochtief, Ferrovial or Skanska were found (not confirmed absent).", 9)
    h2(d, "13.2 Comparable transactions, October 2021 to October 2026")
    table(d, ["Target", "Acquirer", "Announced", "Size", "EV/EBITDA", "EV/Sales", "Note"], [
        ["Equans", "Bouygues", "Nov 2021", "EUR 7.1bn EV", "n/a", "c.0.59x", "11.4x 2026E operating profit (company)"],
        ["Cupertino Electric", "Quanta Services", "Jul 2024", "USD 1.5bn", "c.9.1x", "c.0.70x", "Calc from guided EBITDA"],
        ["Miller Electric", "EMCOR", "Jan 2025", "USD 865m", "10.8x", "1.07x", "Calc"],
        ["CEC Facilities", "Sterling Infrastructure", "Jul 2025", "USD 505m", "9.6x", "c.1.25x", "Company multiple"],
        ["Dynamic Systems", "Quanta Services", "Jul 2025", "USD 1.35bn", "c.8.4x", "c.1.3x", "Mechanical/process"],
        ["Feyen Zylstra + Meisner", "Comfort Systems", "Oct 2025", "c.USD 170m", "c.9.7x", "c.0.85x", "Calc"],
        ["PayneCrest Electric", "Primoris", "Mar 2026", "USD 422m", "c.10.5x", "c.1.17x", "Data-centre electrical"],
        ["The Superior Group (electrical)", "MasTec", "Jul 2026", "USD 1.65bn", "c.7.0x", "c.1.0x", "Cash plus stock"],
        ["Multiplex Global", "Obayashi", "18 Jun 2026", "USD 540m (headline USD 650m)", "8.7-10.5x", "0.14-0.17x", "Closest analogue: thin-margin building contractor; FY25 EBITDA c.USD 62m, revenue USD 3.8bn"],
        ["TRC Companies", "WSP", "Dec 2025", "USD 3.3bn", "14.5x fwd", "c.2.8x", "Engineering consulting"],
        ["IBI Group", "Arcadis", "Oct 2022", "CAD 873m", "11.5x", "n/a", "Design/engineering"],
        ["Toyo Construction", "Taisei", "Aug 2025", "c.JPY 130-160bn", "n/a", "n/a", "Premium 2.9% (6.4% to last close); P/B c.1.7-2.1x"],
        ["Mitsui Sumitomo Construction", "Infroneer", "2025", "JPY 600/share", "n/a", "n/a", "Premium 10.3%"],
        ["Nippon Road (remaining stake)", "Shimizu", "May 2025", "JPY 55.2bn", "n/a", "n/a", "Premium 16.2%"],
        ["MDC Holdings", "Sekisui House", "Jan 2024", "USD 4.9bn", "n/a", "n/a", "P/B 1.33x, P/E 12.8x, premium 19%"],
        ["Tri Pointe Homes", "Sumitomo Forestry", "Feb 2026", "USD 4.5bn", "unverified", "n/a", "Premium 28.5%"],
    ], widths=[3.2, 2.4, 1.8, 2.5, 1.7, 1.5, 4.0], size=7, hl_rows=(8,))
    para(d, "Statistics (our calculation): US specialty contractors (n=7) median EV/EBITDA 9.6x, mean 9.3x; EV/Sales median 1.07x. Broader set (n=12 including consulting) median 10.1x, range 7.0-14.5x. No Japanese contractor deal disclosed EV/EBITDA. Multiples marked 'calc' were computed from disclosed price and guided EBITDA, not company-stated. Japanese contractor deals show premiums of only 3-16% because most were friendly or parent-subsidiary unwinds.", 7.5, True, GREY)
    h2(d, "13.3 Is Obayashi a takeover target?")
    table(d, ["Pros (why a bid could happen)", "Impediments (why it probably will not)"], [
        ["Net cash JPY 84bn plus JPY 289bn of cross-held shares; cash-generative", "Size: c.JPY 2.1tn market cap is 10x the largest Japanese contractor deal (Toyo, c.JPY 130-160bn); EV near JPY 2tn+"],
        ["Valuation below peers on EV/Sales (c.23% regression gap); P/E c.12x", "No credible financial buyer for a JPY 2.5-3tn contractor; LBO leverage capacity limited by thin margins and working-capital swings"],
        ["Foreign ownership 40%; record 135 tender offers in Japan in 2025; METI 2023 guidelines legitimise bids", "May 2026 METI update says boards may reject unsolicited bids; Tokyo court upheld the Makino poison pill"],
        ["Strategic rationale for a foreign contractor (Vinci, ACS/Hochtief, Samsung C&T) seeking Japan scale", "Licensing and public-works eligibility, client relationships and subcontractor networks do not transfer; antitrust (JFTC) blocks a Big-4 merger"],
        ["Silchester precedent shows a shareholder base that responds to value arguments", "Shareholders are diffuse (top holder: trust bank 15.5%), but the founding-family chairman (2.46%) and cross-holders (Nippon Life 2.1%) lean friendly; Linear legacy makes buyers cautious"],
    ], widths=[8.5, 8.5], size=7.6, first_bold=False)
    callout(d, "**Our assessment:** probability of a bid for the whole company within 12 months is below 5%. We found no rumours of private-equity or strategic interest and no Big-4 merger talk. If a bid did happen, a 25-40% premium to JPY 3,008 gives JPY 3,760-4,210 per share, i.e. EV/EBITDA of 10.3-11.6x and EV/Sales of 0.97-1.09x, consistent with US specialty-contractor comps (9.6-10.1x) and about equal to the February 2026 peak.")
    h2(d, "13.4 Acquisitions by Obayashi, October 2016 to October 2026")
    table(d, ["Target", "Date", "Stake", "Cost", "Multiples", "Note"], [
        ["MWH Constructors (US water)", "Announced 11 Jan 2024", "90%", "c.USD 126m (c.JPY 19bn†; not officially disclosed)", "n/a", "Water-infrastructure builder; merged into US civil"],
        ["GCON Inc. + 2 affiliates (Arizona), via Webcor", "17 Oct 2025; closed 1 Dec 2025", "100%", "Undisclosed", "n/a", "Data-centre, semiconductor, healthcare construction management in 10 states; consolidated in FY3/26 H2"],
        ["Multiplex Global (AU/UK/CA) from Brookfield", "18 Jun 2026; closing targeted 30 Sep 2026 (unconfirmed)", "100%", "USD 540m (c.JPY 86bn); Bloomberg headline USD 650m incl. earn-out", "8.7-10.5x EBITDA; 0.14-0.17x sales (calc)", "Largest Obayashi deal of the decade; FY25 revenue USD 3.8bn, EBITDA c.USD 62m, net income USD 71m"],
        ["Cypress Sunadaya (wood)", "Consolidated FY2022", "n/a", "n/a", "n/a", "Timber construction"],
        ["Obayashi Road (minority buy-out)", "2017 TOB", "to 100%", "n/a", "n/a", "Delisted; wholly owned"],
    ], widths=[3.3, 2.8, 1.2, 3.4, 2.5, 3.8], size=7.2)
    para(d, "Earlier US platform (outside the ten-year window): James E. Roberts-Obayashi (1978), E.W. Howell (1989), Webcor (2007), Kraemer North America (2014-15), Kenaidan (2011). No other acquisitions were found for 2017-2022. Multiplex is a USD 3.8bn-revenue business bought at c.0.15x sales for a company that historically earned thin margins and has had fixed-price project disputes (general knowledge†); it carries more integration and execution risk than the sub-USD 200m deals, though at c.4% of Obayashi's market cap the financial exposure is modest.", 8)
    h2(d, "13.5 SK Telecom's holding in Anthropic")
    para(d, "**Nothing links SK Telecom (017670 KS) to Obayashi.** We include the data in case it was requested for a different context.", 9)
    table(d, ["Item", "Detail"], [
        ["Shares held (30 Jun 2026)", "3,860,330 Anthropic shares, per SKT's H1 2026 report (reported by Asia Today, Newspim, Edaily, Herald)"],
        ["Carrying value", "KRW 3.505tn at 30 Jun 2026, up from KRW 1.376tn at end-2025; c.KRW 908k per share"],
        ["H1 2026 purchase", "157,189 shares for KRW 139.9bn (c.KRW 890k per share)"],
        ["Original investment", "USD 100m in 2023 (instrument type not verified)"],
        ["Ownership percentage", "c.0.24% (our calc: Series H of 28 May 2026 at USD 965bn valuation and up to USD 589.01 a share implies c.1.64bn shares); Hana Securities cites 0.3%. Originally c.2%, diluted by later rounds"],
        ["Implied value", "c.USD 2.3bn at USD 589 a share (our calc); KRW 3.5tn carrying value (c.USD 2.5bn at KRW 1,380/USD, FX assumed)"],
        ["Discrepancies", "One Korean source says 0.5-0.7%, inconsistent with the share count; a Morningstar USD 17.6bn figure implies c.2% and looks stale. Anthropic has not published its share count (IPO filing confidential). Accounting classification (FVTPL/FVOCI) not found; the DART filing was not read directly"],
    ], widths=[3.6, 13.4], size=7.8)


def management(d):
    h1(d, "14. Management assessment")
    table(d, ["Executive", "Role / tenure", "Track record and holdings"], [
        ["Toshimi Sato (66)", "President and CEO since 1 Apr 2025; director since 2018", "Finance and planning career (head of Finance 2013, Corporate Planning 2015); first non-engineer, non-family president. Has presided over the best results in the group's recent history (OP JPY 195bn in FY3/26), a JPY 100bn buyback, GCON and Multiplex. Shareholding and pay not in the disclosed list (below JPY 100m threshold)"],
        ["Takeo Obayashi (72)", "Chairman; founding family; director since 1983", "Holds 16.9m shares (2.46%, c.JPY 51bn at JPY 3,008): meaningful skin in the game. Pay JPY 118m (FY3/25). Sources conflict on when he became chairman (2003, 2009 or Apr 2023)"],
        ["Kenji Hasuwa (72)", "Vice Chairman (non-representative) since Apr 2025; President Mar 2018-Mar 2025", "Civil engineer who took over after the Linear bid-rigging forced out his predecessor; delivered the recovery and MWH acquisition. Pay JPY 169m (FY3/25)"],
        ["Yasuo Morita; Yoshihito Sasaki; Atsushi Sasagawa", "Representative directors / vice chairman (changes Apr and Jun 2026)", "Details thin. The 6 Mar 2026 notice made Morita a representative director; Sasagawa gave up representation and moves to Vice Chairman, though one summary still lists him as a director. Verify against the AGM notice"],
        ["CFO / finance head; business-unit heads", "Not found", "Not retrievable; Sato himself ran Finance 2013-15, which is relevant for capital policy"],
    ], widths=[3.3, 4.4, 9.3], size=7.6)
    h3(d, "Assessment on the five tests")
    bullets(d, [
        "**1. Track record:** strongly positive since 2023. Profit up 4.7x, ROE c.14% vs a 10% target, ROIC 8.4% vs 5% target (company-stated†). Much of the improvement is cycle and pricing, but cost control and order selection are management's doing.",
        "**2. Tenure and ownership:** CEO new (18 months); chairman has real ownership; executive share-based pay is modest. No evidence of large insider selling was retrievable.",
        "**3. Capital allocation:** improving. Positives: DOE target, buybacks, a credible cross-holding exit, small, sensible bolt-ons (MWH, GCON). Negative: Multiplex is a bigger bet on a low-margin business; the past decade included an unproductive balance-sheet cash build.",
        "**4. Red flags:** the Linear bid-rigging (self-reported; JFTC surcharge c.JPY 3.1bn, JPY 200m court fine, 4-month Tokyo suspension, president resigned 2018); an October 2024 safety incident at a Chuo Shinkansen tunnel where employees gave false information to inspectors (JPY 200,000 summary fines, March 2026). We found no related-party issues, accounting restatements or promotional behaviour. Strategy has evolved consistently (MTP 2017, 2022, 2024 addendum), not erratically.",
        "**5. Founder vs professional:** hybrid. Salaried-manager presidents since 2011 with a family chairman and a 2.46% holding; no controlling holder. This suits a mature, process-driven contractor in a capital-discipline phase; the risk is slower decision-making and succession politics.",
    ], 8.5)


def board(d):
    h1(d, "15. Board of directors (after the 122nd AGM, 29 June 2026)")
    table(d, ["Director", "Status", "Appointed", "Background and affiliations"], [
        ["Takeo Obayashi", "Chairman, inside", "Director since 1983", "Founding family; 2.46% shareholder"],
        ["Toshimi Sato", "President and CEO, inside", "Jun 2018", "Waseda 1985; finance and planning; see Section 14"],
        ["Yoshihito Sasaki", "Representative director, inside†", "n/a", "Background not found"],
        ["Atsushi Sasagawa", "Inside (status conflicting)†", "n/a", "Notice says moves to Vice Chairman; one summary lists him re-elected"],
        ["Masako Orii (b. 1960)", "Outside, independent", "Jun 2020", "Ex-Suntory (joined 1983); exec officer Suntory Holdings 2012; MD Suntory Wellness 2016"],
        ["Hiroyuki Kato (b. 1956)", "Outside, independent", "n/a", "Ex-Mitsui & Co. (joined 1979), executive-level"],
        ["Yukiko Kuroda (b. 1963)", "Outside, independent", "Jun 2022", "Ex-Sony; founder of People Focus Consulting (1991); outside auditor Astellas, CAC†"],
        ["Hiroyuki 注連 (reading unverified)", "Outside, independent", "n/a", "Ex-Unitika management†"],
        ["Yoshihiro Ikegawa (b. 1960)", "Outside, independent", "n/a", "Ex-Mitsubishi Chemical (joined 1983); executive officer 2014"],
        ["Midori Tomita", "Outside, independent (new)", "Jun 2026", "Background not found"],
    ], widths=[3.8, 3.6, 2.6, 7.0], size=7.6)
    bullets(d, [
        "**Composition:** 6 of 10 directors outside and independent (60%); 3 women (30%). Board uses a company-with-audit-and-supervisory-board structure with voluntary nomination and compensation committees chaired by outside directors.",
        "**Audit & Supervisory Board:** three new members from June 2026: Yoshiaki Takada (full-time), Yohei Ueda and Sachiko Tsujino (outside).",
        "**Changes in five years (partial):** Orii 2020; Kuroda 2022; Tomita 2026; auditor turnover 2026; CEO change April 2025. Appointment years for several outside directors, 2021-25 turnover and AGM approval ratios could not be retrieved. Source documents: the 122nd AGM notice and extraordinary report on voting results.",
    ], 8.5)


def holders(d):
    h1(d, "16. Shareholders, activism and short interest")
    table(d, ["#", "Holder (31 Mar 2026)†", "Shares (m)", "%", "Type"], [
        ["1", "Japan Master Trust Bank (trust account)", "106.7", "15.51", "Institutional (passive/index trust-bank)"],
        ["2", "Custody Bank of Japan (trust account)", "50.0", "7.26", "Institutional (trust-bank)"],
        ["3", "State Street Bank & Trust 505001", "25.2", "3.66", "Foreign institutional custody"],
        ["4", "State Street Bank & Trust 505103", "17.9", "2.60", "Foreign institutional custody"],
        ["5", "Takeo Obayashi", "16.9", "2.46", "Insider / founding family"],
        ["6", "Nippon Life Insurance", "14.6", "2.13", "Strategic institutional (insurer, cross-holder)"],
        ["7", "Obayashi Group Employee Shareholding Assoc.", "12.6", "1.83", "Employees"],
        ["8", "JP Morgan Chase Bank 385781", "9.3", "1.35", "Foreign institutional custody"],
        ["9", "BNY Mellon 140042", "9.2", "1.33", "Foreign institutional custody"],
        ["10", "Goldman Sachs Securities (BNYM)", "9.0", "1.30", "Foreign broker/custody"],
    ], widths=[0.8, 6.6, 2.0, 1.2, 6.4], size=7.6)
    bullets(d, [
        "**Mix:** foreign investors c.40%, financial institutions c.31.5% (2026 shareholder data†). Trust-bank accounts show nominee holdings; beneficial owners (e.g. BlackRock, Vanguard) are not visible in this list. No controlling holder. Large-shareholding (5%) reports for 2024-26 were not found.",
        "**Activism:** one campaign found. **Silchester International Investors** (2023 AGM) proposed a special dividend of JPY 12 a share (payout of 100% of non-core and 50% of core income). The board opposed; the proposal failed with c.26.8% support. The company's May 2024 plan addendum (ROE 10%+, DOE c.5%, JPY 100bn buyback, cross-holding sales) delivered much of what such investors wanted, so the campaign was partially successful in effect, if not in vote. No other activist (Oasis, Effissimo, Elliott, 3D, Dalton, ValueAct) was found at Obayashi; peers have drawn activism (Oasis at Kumagai Gumi; an activist push at Toyo that preceded Taisei's bid).",
        "**Short interest:** minimal. JPX margin data for 25 Jun 2026†: margin short 75,300 shares versus margin long 854,100 (ratio 11.3x), i.e. negligible against c.690m shares. Stock-lending balance and FSA disclosures of short positions above 0.5% were not found, and no notable short sellers were identified.",
    ], 8.5)


def strategy(d):
    h1(d, "17. Strategic initiatives, last ten years")
    table(d, ["Initiative", "Period", "Outcome and status"], [
        ["Medium-Term Business Plan 2017", "2017-21", "Domestic profit rebuilding, overshadowed by the Linear scandal (2017-18) and civil/building margin problems. Partial"],
        ["Medium-Term Business Plan 2022 and May 2024 addendum", "2022-27", "Targets: OP JPY 100bn+, ROIC 5%+, later ROE 10%+, equity JPY 1tn. All exceeded (OP JPY 195bn, ROE c.14%). Success, helped by price pass-through and property gains. Successor plan due c.May 2027"],
        ["Capital-efficiency programme", "2024-27", "DOE c.5%, JPY 100bn buyback, cross-holdings to 20% of net assets. On track (21.9% at Mar 2026; 17.5% including agreed sales)"],
        ["US platform build-out", "2007-26", "Webcor, Kraemer, MWH, GCON now c.33% of sales overseas; margins still low (2-4%). Mixed but improving; data-centre exposure is the new leg"],
        ["Multiplex acquisition", "2026", "USD 540m, closing targeted 30 Sep 2026. Too early to judge; integration risk"],
        ["Obayashi Road take-private", "2017", "Simplified group; neutral"],
        ["Wood and sustainability (Cypress Sunadaya, wood high-rise, renewables, biomass)", "2018-26", "Small financially; strategic positioning on decarbonisation. Not quantified"],
        ["Construction technology (Smart Construction, robotics)", "ongoing", "Productivity response to labour shortage; benefits not separately disclosed. Space-elevator concept is R&D marketing"],
        ["Real estate and data-centre development", "ongoing", "c.JPY 100bn data-centre development investment mooted over a decade†; real estate gains boosted FY3/26"],
    ], widths=[5.0, 2.0, 10.0], size=7.6)


def stakes(d):
    h1(d, "18. Stakes in other companies")
    bullets(d, [
        "**Cross-shareholdings (listed):** JPY 288.8bn at market value (21.9% of net assets) at March 2026, being cut to 20%; c.JPY 285bn sold over five years†; JPY 58.3bn of further sales contracted. The number of issuers and top holdings could not be retrieved. Financial relevance: a source of cash (c.JPY 20bn gain in Q1 FY3/27) and dividend income, and a governance overhang that is shrinking. Strategic relevance: customer and bank relationships.",
        "**Subsidiaries:** Webcor (US, 100%), Kraemer North America (control; one source says 56%), MWH (90%), GCON (100%), E.W. Howell, James E. Roberts-Obayashi, Kenaidan (Canada), Obayashi Shinseiwa Real Estate (100%), Thai Obayashi, Obayashi Singapore, Taiwan and Indonesian units; Cypress Sunadaya; Multiplex (pending). Group size c.98 subsidiaries and 26 affiliates (March 2022 figure†).",
        "**Unlisted / venture / funds:** not found. Equity-method income was not retrieved.",
    ], 8.6)


def returns(d):
    h1(d, "19. Shareholder returns, treasury shares and cancellations")
    table(d, ["Fiscal year", "DPS (JPY)", "Payout (DPS/EPS)", "Buybacks and treasury-share events", "Share count / cancellation"], [
        ["FY3/22", "32", "59%", "No programme found", "c.718m issued†"],
        ["FY3/23", "42", "39%", "No programme found; Silchester special-dividend proposal rejected (Jun 2023)", "n/a"],
        ["FY3/24", "75", "72%", "Capital policy announced Mar 2024: DOE c.5% (from c.3%); ROE 10% target", "n/a"],
        ["FY3/25", "81", "40%", "10 Feb 2025: up to 20.0m shares (2.8%), 12 Feb-30 Jun 2025; one-third (c.JPY 33bn) of the JPY 100bn plan; all acquired shares to be cancelled", "c.721m shares at Mar 2025†"],
        ["FY3/26", "88 (41 interim + 47 final)", "35%", "Final tranche 1-23 Jun 2025: 1.94m shares, JPY 4.25bn (avg c.JPY 2,194); Aug 2025: cancellation plus JPY 40bn buyback†", "c.688-692m shares by 2026†"],
        ["FY3/27E", "94 (47 + 47)", "c.41%", "c.JPY 30bn of the JPY 100bn plan left† (through March 2027)", "Treasury-share balance not retrieved"],
    ], widths=[1.8, 2.6, 2.0, 7.6, 3.0], size=7.4)
    para(d, "Treasury-share balances at each year-end, individual buyback amounts for FY3/22-24 and the exact number of shares cancelled could not be retrieved; they are in the tanshin share-data notes and the 'Status of acquisition of treasury shares' in each yuho. Financing cash outflow in FY3/26 (JPY 141bn) implies a total shareholder-return proxy of c.6.8% of market cap. Shares in issue (c.718m) versus c.688-692m now implies roughly 26-30m shares retired or held as treasury†. Dividend policy: DOE c.5%, with special dividends and buybacks flexible.", 8, True, GREY)


def bull_bear(d):
    h1(d, "20. Adversarial analysis: bull, bear, pre-mortem, contrarian")
    h2(d, "20.1 Bull case")
    bullets(d, [
        "**Structural pricing power:** four-firm oligopoly, capacity-constrained by labour; selective bidding has held gross margin c.13%; Japanese building-cost inflation is increasingly passed through.",
        "**Secular tailwinds:** Tokyo redevelopment, data centres and semiconductor fabs, national-resilience spending (JPY 20tn+ over FY2026-30†), Linear Shizuoka start, US data-centre build-out via GCON/Webcor.",
        "**Capital-allocation upgrade:** DOE 5%, JPY 100bn buyback, JPY 289bn of cross-holdings to monetise, JPY 84bn net cash. A new plan in May 2027 could lift the payout further; total shareholder yield of c.6-7% is a floor.",
        "**Earnings-surprise machinery:** management guides low; FY3/26 net income came in 74% above the initial JPY 100bn guide; Q1 progress is ahead of the five-year average.",
        "**Valuation:** 23% regression discount; c.7x adjusted EV/EBITDA; P/E c.12x. At the February 2026 peak the shares traded at c.18x FY3/26 EPS, so re-rating headroom exists if margins hold.",
    ], 8.5)
    h2(d, "20.2 Bear case")
    bullets(d, [
        "**Margin mean reversion:** a 4.7x profit recovery driven by a few large domestic building jobs and change orders; lower-margin new work enters from FY3/27 (guide OP -7.5%). Each 1pt of OP margin on JPY 2.9tn sales is JPY 29bn, or c.13% of EPS.",
        "**Permanent-impairment risks:** (1) a cost shock in the fixed-price backlog (Middle East supply disruption, labour); (2) a large overseas project loss, particularly Multiplex's fixed-price legacy; (3) a bid-rigging or safety event that triggers public-works suspension.",
        "**Order deceleration:** Q1 orders -7.2%; management flags caution from FY3/28; higher rates and weaker developer returns could delay private capex.",
        "**Earnings quality:** FY3/26 EPS of JPY 249 included c.JPY 30-35bn of estimated net one-off gains; underlying EPS is closer to JPY 205-215. The cross-holding gain source will run dry as the 20% target is met.",
        "**Expectations:** the stock tripled; at 12-13x P/E on peak-margin earnings the market already assumes margin sustainability.",
    ], 8.5)
    h2(d, "20.3 Pre-mortem: it is October 2027 and the stock is at JPY 2,000. Why?")
    bullets(d, [
        "A November 2026-May 2027 sequence of project-cost write-downs (naphtha-material delays turn into loss provisions on two or three large jobs) cuts FY3/27 OP to JPY 150bn.",
        "Orders fall 10% as developers defer on higher rates; backlog cover shrinks and peers discount to fill capacity, ending pricing discipline.",
        "Multiplex reports a loss-making legacy project; goodwill and provisions of JPY 20-30bn offset the purchase price, and the market re-rates Obayashi's overseas arm as a risk, not a growth leg.",
        "The successor plan (May 2027) lowers the payout ambition because earnings fell, removing the capital-return support.",
    ], 8.5)
    h2(d, "20.4 Contrarian view: what the market may be refusing to see")
    callout(d, "**The market is capitalising FY3/27 guidance (OP -7.5%) as the start of a normal contractor downcycle. We think guidance is deliberately low and that the 13% gross-margin plateau is structurally supported by labour-driven capacity constraints, not a peak. In that case the stock trades at c.10-11x underlying EPS and c.7x adjusted EV/EBITDA, with a 6-7% shareholder yield and an unwound cross-holding book still ahead. The real risk is not margin; it is a handful of large fixed-price jobs and a Multiplex integration going wrong. A tilt to that nuance, rather than 'peak margin', is where we see the edge.**")


def scenarios(d):
    h1(d, "21. Scenario analysis")
    table(d, ["", "Bear (30%)", "Base (50%)", "Bull (20%)"], [
        ["Narrative", "Cost shock and order slump; margin back to c.5%; gains dry up", "Margin eases to 6.5%; orders flat; steady buybacks", "Margin holds above 7%; data-centre and overseas growth; payout upgrade"],
        ["Sales growth FY3/28E", "0% (JPY 2,900bn)", "+2.9% (JPY 3,030bn)", "+5.4% (JPY 3,150bn)"],
        ["Operating margin FY3/28E", "5.2%", "6.5%", "7.1%"],
        ["EBITDA FY3/28E (JPY bn)", "200", "247", "295"],
        ["EV/EBITDA multiple", "6.5x (trough contractor)", "8.5x (Japan Big-3 discount)", "9.5x (US specialty-contractor median)"],
        ["Equity value (JPY bn)", f"{SCV['Bear'][0]:,.0f}", f"{SCV['Base'][0]:,.0f}", f"{SCV['Bull'][0]:,.0f}"],
        ["Value per share (680m shares)", f"JPY {SCV['Bear'][1]:,.0f} ({SCV['Bear'][1]/PRICE-1:+.0%})", f"JPY {SCV['Base'][1]:,.0f} ({SCV['Base'][1]/PRICE-1:+.0%})", f"JPY {SCV['Bull'][1]:,.0f} ({SCV['Bull'][1]/PRICE-1:+.0%})"],
        ["Implied P/E on FY3/28E EPS", f"{SCV['Bear'][1]/BEAR[1]['eps']:.1f}x", f"{SCV['Base'][1]/BASE[1]['eps']:.1f}x", f"{SCV['Bull'][1]/BULL[1]['eps']:.1f}x"],
    ], widths=[4.2, 4.2, 4.2, 4.4], size=7.8)
    para(d, f"Equity value = EBITDA x multiple + net cash JPY 84bn + 75% of JPY 289bn cross-held shares (JPY 217bn). Probability-weighted value: JPY {PW:,.0f} (+{(PW/PRICE-1)*100:.0f}%). 12-month target JPY 3,500, set at the base case less a small execution haircut. Downside to bear case is -22%, upside to bull case +52%, a c.2.3:1 skew on the extremes with the weighted outcome positive. Regression cross-check: JPY 3,670.", 8.2)


def questions(d):
    h1(d, "22. Fifteen questions for the CEO and Chairman (ordered by information value)")
    qs = [
        "Your completed-works gross margin is guided at 13% 'and beyond': what share of that is contractual price escalation versus selective order-taking, and what does the margin look like on projects booked in the last 12 months?",
        "FY3/26 net income exceeded ordinary income by an unusually large margin: how much of FY3/26 and FY3/27 net income comes from securities sales and property gains, and what is the normalised earnings power without them?",
        "Why did you guide FY3/27 operating income down 7.5% when Q1 progress is ahead of average and consensus is already above guidance? What is the assumed margin on early-stage jobs?",
        "What loss provisions or cost overruns, if any, exist on fixed-price jobs from the Middle East supply disruption, and how many large projects have escalation clauses?",
        "Why did you pay USD 540m for Multiplex, and what is its standalone margin, backlog quality and legacy-dispute exposure? What goodwill and provisions do you expect on closing?",
        "What is the target gross margin and return on capital for the overseas business over the next plan, and when will overseas building clear a 5% operating margin?",
        "After the 20% cross-holding target is met in March 2027, will sales continue, and what will the recycled proceeds fund: buybacks, M&A or real estate?",
        "What payout, ROE and net-cash framework will the successor medium-term plan use? Is DOE 5% a floor?",
        "Orders fell 7.2% in Q1 and you flag caution from FY3/28: which client segments are slowing, and what is the order-to-sales ratio you need to protect margin?",
        "How are you managing labour capacity under the 2024 overtime cap, and how much of margin gain is productivity versus pricing?",
        "What are you doing about the Linear bid-rigging legacy, and what governance change ensures a repeat is impossible? How did the October 2024 safety incident and false statements to inspectors arise?",
        "How do you assess unsolicited-approach risk and your defence preparedness in light of METI's 2026 guidance, and would you engage with a bid at a 30%+ premium?",
        "Data centres and semiconductors: what is the share of backlog, expected margin versus conventional building, and customer concentration?",
        "How do you decide between building capacity organically and acquiring overseas, and what is the ceiling on overseas share of sales?",
        "Succession and governance: what is the role of the Chairman and Vice Chairmen alongside the new CEO, and how will the Board's skill mix change under the new plan?",
    ]
    for i, q in enumerate(qs, 1):
        p = d.add_paragraph()
        _runs(p, f"**{i}.** {q}", 8.8)
        p.paragraph_format.space_after = Pt(2)


def shortseller(d):
    h1(d, "23. Short-seller view and accounting red flags")
    h2(d, "23.1 Dismantling the bull case")
    bullets(d, [
        "**What structurally breaks the earnings model:** profit is a function of a few large domestic building jobs priced during a capacity shortage. Domestic building generates 53% of operating income. If order flow weakens and peers bid for volume, the 13% gross-margin plateau collapses; a mere 1pt margin loss is a JPY 29bn (c.15%) cut to OP.",
        "**Revenue concentration:** public clients (MLIT, JR Tokai) and a handful of developers; Linear schedule slippage (opening 2034-36†) defers civil volume. A shift in developer capex from higher rates is the most plausible trigger.",
        "**Why the moat is weaker than it looks:** a contractor's brand does not command a consumer premium; Kajima, Taisei and Shimizu are near-perfect substitutes; clients can run competitive tenders. The 2023-26 margin came from scarcity pricing and a legacy-loss roll-off, both cyclical.",
        "**Most dangerous underestimated competitor:** Taisei, with the highest operating margin (c.9%), a cleaner balance sheet narrative and the ability to buy mid-tier peers (Toyo), could out-execute in data centres and complex infrastructure. On the overseas side, Hochtief/Turner, which dominates US data-centre construction, is the competitor Webcor and GCON ultimately face.",
        "**Capital allocation concerns:** a decade of cash accumulation and cross-holdings (JPY 289bn) with ROIC only 8%; an acquisition of Multiplex (a business that has had losses and fixed-price disputes†) after the best earnings year ever; a JPY 40bn buyback programme whose execution prices we could not verify as the stock ran toward JPY 4,439.",
        "**What must hold for the price to be justified:** gross margin stays at c.13%, order backlog stays above 1x sales, gains continue, and no large fixed-price loss. If growth disappoints 20-30% (OP JPY 140-155bn), EPS falls to c.JPY 150-170 and at a 12x P/E the stock is JPY 1,800-2,040 (-32% to -40%).",
        "**The single permanently-impairing scenario:** a large fixed-price overseas or civil loss combined with a public-works suspension after a compliance breach, in a high-rate construction downturn. Plausibility: low but not negligible (10-15% over three years), given Linear history, the Multiplex legacy and the cost environment.",
    ], 8.5)
    h2(d, "23.2 Accounting and disclosure red flags")
    table(d, ["Area", "Observation", "Risk level"], [
        ["Revenue recognition", "Cost-to-cost percentage of completion relies on management's estimate of total costs; changes in estimates move profit materially (FY3/23-24 cost surprises). Large 'additional and change orders' were a key FY3/26 profit driver; check how much is recognised before client approval", "High"],
        ["Loss provisions / contingencies", "Provisions for construction-contract losses, defect warranties and the bid-rigging legacy (JFTC surcharge c.JPY 3.1bn, litigation by clients) require reading the yuho; overseas disputes (US, Multiplex) are the principal unknown", "Medium-high"],
        ["Segment reporting", "Company-defined segments; 'real estate and other' bundles property gains and group services (c.JPY 23bn derived OP). Segment D&A, assets and capex need the yuho notes; segment net income not disclosed", "Medium"],
        ["Earnings quality: non-operating and extraordinary items", "Net income above operating income in FY3/26 and Q1 FY3/27; securities sales gains (c.JPY 20bn in Q1) recur by policy but will run out; cash flow from sales is investing, not operating", "High"],
        ["Leases", "JGAAP: operating leases are off balance sheet; no IFRS 16 comparability with Vinci/Skanska/Hochtief. EV/EBITDA is flattered versus IFRS peers", "Medium"],
        ["Goodwill and intangibles", "GCON (undisclosed price), MWH (c.USD 126m), Multiplex (c.JPY 86bn) will add goodwill amortised over a fixed period under JGAAP (a drag), and impairment risk if overseas margins disappoint", "Medium-high"],
        ["Related parties", "None found in available summaries; Obayashi family chairman holds 2.46%; check yuho related-party note and any family-linked property transactions", "Low (unverified)"],
        ["Stock-based compensation", "Immaterial (restricted-share awards for directors); low dilution; not a concern", "Low"],
        ["Cash flow", "Operating cash flow volatile (JPY 50bn to JPY 253bn in five years†): driven by working capital on progress billings, retentions and advance payments; FCF yield of 8.1% overstates sustainable cash", "Medium"],
        ["Balance-sheet items", "Investment securities of JPY 289bn marked to market (equity gains in OCI); pension obligations (JGAAP); consolidated JV treatment (proportionate)", "Medium"],
    ], widths=[3.4, 11.4, 2.2], size=7.5)


def timeline(d):
    h1(d, "24. Timeline of past events and calendar of upcoming catalysts")
    h2(d, "24.1 Key past events")
    table(d, ["Date", "Event"], [
        ["1892", "Founded in Osaka by Yoshigoro Obayashi"],
        ["1978-2015", "US platform built: James E. Roberts-Obayashi (1978), E.W. Howell (1989), Webcor (2007), Kraemer (2014-15)"],
        ["2017", "Obayashi Road taken private by tender offer"],
        ["Dec 2017 - Mar 2018", "Linear Chuo Shinkansen bid-rigging probe; indictment; president Shiraishi resigns; Kenji Hasuwa becomes president"],
        ["Dec 2020 - 2021", "JFTC surcharge order (c.JPY 3.1bn); JPY 200m court fine; four-month Tokyo suspension"],
        ["Apr 2022", "Medium-Term Business Plan 2022 starts"],
        ["7 Nov 2022", "FY3/23 forecast cut on building cost inflation"],
        ["28 Jun 2023", "Silchester proposal; c.26.8% support"],
        ["Jan 2024", "MWH acquisition (90%)"],
        ["Mar - May 2024", "Capital policy: DOE c.5%, ROE 10%+; stock limit-up on 5 Mar 2024"],
        ["Oct 2024", "Chuo Shinkansen tunnel injury; later false-statement summary fines (Mar 2026)"],
        ["Feb - Jun 2025", "First buyback tranche (up to 20m shares)"],
        ["1 Apr 2025", "Toshimi Sato becomes President and CEO; Hasuwa to Vice Chairman"],
        ["13 May 2025", "FY3/26 guide: net income -32%; shares fall c.9% intraday"],
        ["Aug 2025", "Share cancellation and JPY 40bn buyback†"],
        ["Oct - Dec 2025", "GCON agreed (17 Oct) and closed (1 Dec)"],
        ["27 Feb 2026", "All-time high JPY 4,439"],
        ["13 May 2026", "FY3/26 results (OP JPY 194.7bn, +36.6%); FY3/27 guide OP -7.5%"],
        ["18 Jun 2026", "Multiplex acquisition announced (USD 540m)"],
        ["29 Jun 2026", "122nd AGM: board of 10, three women; Tomita joins"],
        ["7 Aug 2026", "Q1 FY3/27: OP +107%; orders -7.2%"],
        ["19 Aug 2026", "YTD low JPY 2,891"],
        ["18 Sep 2026", "BOJ policy rate reportedly raised to 1.25%†"],
    ], widths=[3.6, 13.4], size=7.6)
    h2(d, "24.2 Upcoming catalysts (dates inferred from prior years unless stated; confirm on the IR calendar)")
    table(d, ["Timing", "Catalyst", "What to watch"], [
        ["By 30 Sep 2026 (unconfirmed)", "Multiplex closing", "Closing date, final price, net debt assumed, goodwill"],
        ["29-30 Oct 2026", "BOJ meeting with outlook report", "Rate path; construction financing costs"],
        ["Early/mid Nov 2026 (prior-year: 5 Nov)", "Q2 / H1 FY3/27 results", "Orders, gross margin, whether guidance is raised, interim DPS (JPY 47)"],
        ["17-18 Dec 2026", "BOJ meeting; Japan FY2027 budget (resilience spending)", "Public-works budget size"],
        ["Late 2026 onward", "Linear Shizuoka section works start", "Contract awards and JV share"],
        ["c.9 Feb 2027", "Q3 FY3/27 results", "Full-year guidance revision; gain recognition"],
        ["Mar 2027", "Cross-holding 20% target date; fiscal year-end", "Residual sales; buyback completion"],
        ["c.mid-May 2027", "FY3/27 results and successor medium-term plan (likely)", "ROE, payout, net-cash and M&A frameworks"],
        ["Late Jun 2027", "123rd AGM", "Board changes; shareholder proposals"],
        ["Ongoing", "Large project awards (Tokyo redevelopments, data centres, rail), Middle East cost developments, JFTC/MLIT actions, M&A in the sector", "Pricing and order data from peers (Kajima, Taisei, Shimizu quarterly orders)"],
    ], widths=[4.2, 5.8, 7.0], size=7.6)


def appendix(d):
    h1(d, "Appendix: data confidence, conflicts and primary sources")
    table(d, ["Item", "Confidence", "Note"], [
        ["FY3/26 sales, OP, NI, DPS, FY3/27 guidance", "High", "Consistent across Nikkei, BUILT, japanir and company-linked headlines (NI 173.7-173.9bn rounding)"],
        ["Q1 FY3/27 sales 623.4bn, OP 32.7bn, NI 39.0bn, orders 577.5bn", "High", "Consistent across Jiji, Kabutan and Yahoo Japan; one summary's JPY 45.9bn / 131bn figures and another's JPY 523.8bn were garbled or are the prior-year base"],
        ["FY3/22-25 history", "Medium", "Single-table source; FY3/25 sales conflict (2,590.8bn vs 2,620.1bn)"],
        ["Segment data FY3/26", "Medium", "Overseas civil OP conflicts (14.7bn vs 8.3bn); orders/backlog from secondary summaries"],
        ["Net cash, debt, cash", "Medium-low", "Stockanalysis-type summary; another source shows debt JPY 344bn"],
        ["Share price, market cap, 52-week range", "Medium", "Kabutan/Nikkei-type snippets; undated EV figures (JPY 1.75tn) were not used"],
        ["Peer multiples", "Low-medium", "Mixed-date aggregator data; regression is indicative (n=7)"],
        ["Board, top-10 holders", "Medium", "From search summaries of the yuho and AGM notice; Sasagawa's status conflicts"],
        ["Buyback and treasury-share detail", "Low", "Programme outline found; amounts, balances and cancellations incomplete"],
        ["Earnings-call content", "Low", "Transcripts not accessible; sentiment is headline-based"],
        ["Price moves >10%", "Low", "Only one dated; no daily series"],
    ], widths=[5.4, 2.4, 9.2], size=7.5)
    para(d, "Primary documents to verify (not accessible here): FY3/26 tanshin (data.swcms.net .../140120260512524360.pdf); FY3/26 presentation and Q&A (ir.obayashi.co.jp, news202605131202en and news202605261500en); Q1 FY3/27 tanshin and presentation (auto_20260806512662, news202608071600en); 2025 and 2026 Integrated Reports (ir.obayashi.co.jp/en/ir/data/report/ ... ir2026en.pdf); Medium-Term Plan 2022 addendum (obayashi.co.jp/company/upload/file/mid_term_plan2022_add_J.pdf); AGM notice and voting results (March and June 2026 releases); yuho on EDINET.", 8)
    para(d, "This report is research, not investment advice. Figures marked † were not verified against a primary filing. Ticker for Obayashi is 1802 JT (Tokyo Stock Exchange); '1802 JY' in the request has been read as 1802 JT.", 7.5, True, GREY)
