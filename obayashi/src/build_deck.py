from model import *
b=BASE; 
CSS="""
@page{size:13.333in 7.5in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Liberation Sans',Arial,sans-serif;color:#14243f}
.s{width:13.333in;height:7.5in;position:relative;page-break-after:always;overflow:hidden;background:#fff;padding:.42in .6in}
.s:last-child{page-break-after:auto}
.k{font-size:11.5pt;letter-spacing:.14em;font-weight:700;color:#2f6bd0;text-transform:uppercase}
.tag{position:absolute;right:.6in;top:.34in;background:#2d3a52;color:#fff;font-size:10pt;font-weight:700;letter-spacing:.1em;padding:.1in .25in;text-transform:uppercase}
.hd{border-bottom:2px solid #14243f;padding-bottom:.12in;margin-bottom:.2in;height:.5in}
h1{font-size:25pt;line-height:1.15;margin-bottom:.2in}
h3{font-size:13pt;border-bottom:1px solid #cfd5df;padding-bottom:.06in;margin:.1in 0 .1in}
ul{list-style:none} li{font-size:11pt;line-height:1.35;margin-bottom:.1in;padding-left:.2in;position:relative}
li:before{content:'';position:absolute;left:0;top:.08in;width:.1in;height:.1in;background:#2f6bd0}
.g li:before{background:#7a8497}
.tiles{display:flex;gap:4px;margin:.1in 0 .22in}.t{flex:1;background:#f1f3f8;padding:.16in .2in}
.t b{display:block;font-size:24pt}.t span{font-size:9.5pt;color:#555f70}
.cols{display:flex;gap:.45in}.cols>div{flex:1}
table{border-collapse:collapse;width:100%;font-size:9.5pt}th{background:#14243f;color:#fff;text-align:left;padding:.06in .09in}
td{padding:.055in .09in;border:1px solid #dde1ea}tr:nth-child(even) td{background:#f1f3f8}td.b{font-weight:700}tr.h td{background:#dce7fa}
.box{background:#f1f3f8;border-left:5px solid #14243f;padding:.14in .22in;font-size:11pt;line-height:1.35}
.dark{background:#2d3a52;color:#fff;border-left:5px solid #4f8ef0}
.note{font-size:8.5pt;color:#6b7587;font-style:italic;margin-top:.08in}
img{max-width:100%}
.cover{background:#13233f;color:#fff;padding:0}
.cover .l{position:absolute;left:.6in;top:1.2in;width:6.3in}
.cover .r{position:absolute;left:7.75in;top:1.5in;width:4.9in}
.cover .r div{border-bottom:1px solid #2c3d5c;padding:.18in 0}.cover .r b{font-size:30pt;display:block}.cover .r span{font-size:11pt;color:#c9d2e3}
.btn{display:inline-block;background:#2f6bd0;color:#fff;font-weight:700;padding:.14in .3in;font-size:13pt;margin-right:.1in}.btn2{display:inline-block;border:2px solid #4f8ef0;color:#fff;font-weight:700;padding:.12in .3in;font-size:13pt}
"""
def slide(kicker,tag,title,body): return f'<div class="s"><div class="hd"><span class="k">{kicker}</span><span class="tag">{tag}</span></div><h1>{title}</h1>{body}</div>'
S=[]
S.append(f'''<div class="s cover"><div class="l"><div class="k" style="color:#5b97ee;border-bottom:3px solid #2f6bd0;display:inline-block;padding-bottom:.08in">Equity research | Event &amp; special situations</div>
<div style="font-size:42pt;font-weight:700;line-height:1.1;margin:.35in 0 .25in">Obayashi Corporation</div>
<div style="font-size:16pt;color:#c9d2e3;margin-bottom:.4in">TSE: 1802 JT &mdash; Record margins, net cash, a stock 32% off its high</div>
<span class="btn">RATING: ACCUMULATE</span><span class="btn2">12-MO TARGET: &yen;3,500 (+16%)</span>
<div style="margin-top:.45in;font-size:11pt;color:#c9d2e3;line-height:1.7">Reference price &yen;3,008 (30 Sep 2026)&nbsp;&nbsp;|&nbsp;&nbsp;52-wk range &yen;2,891&ndash;4,439<br>Mkt cap &yen;{MCAP:,.0f}bn&nbsp;&nbsp;|&nbsp;&nbsp;Net cash &yen;{NETCASH:.0f}bn&nbsp;&nbsp;|&nbsp;&nbsp;EV &yen;{EV:,.0f}bn</div></div>
<div class="r"><div><b>{M["ev_ebitda"]:.1f}x</b><span>EV/EBITDA (c.{M["ev_ebitda_adj"]:.0f}x after cross-holdings) &mdash; regression implies c.23% EV/Sales discount</span></div>
<div><b>{M["fcfy"]:.0f}%</b><span>FCF yield proxy (CFO + investing CF), plus 6&ndash;7% shareholder-return yield</span></div>
<div><b style="color:#7fb0f5">&yen;{PW:,.0f}</b><span>Probability-weighted value (30/50/20 bear/base/bull)</span></div></div>
<div style="position:absolute;left:.6in;bottom:.4in;font-size:10pt;color:#8e9ab1">Prepared 3 October 2026 | Figures marked &dagger; are from search summaries, not primary filings</div></div>''')
S.append(slide("Executive summary","Recommendation","Accumulate: a conservative-guiding, net-cash contractor with a re-rating already partly given back",f'''
<div class="tiles"><div class="t"><b>7.5%</b><span>FY3/26 operating margin (2.1% in FY3/22)</span></div><div class="t"><b>&yen;84bn</b><span>Net cash&dagger; plus &yen;289bn cross-holdings</span></div><div class="t"><b>{M["pe_t"]:.0f}x</b><span>Trailing P/E; {M["pe_g"]:.1f}x on guidance</span></div><div class="t"><b>&yen;3,500</b><span>12-mo target (+16%)</span></div><div class="t"><b>30%</b><span>Bear-case probability (&yen;{SCV["Bear"][1]:,.0f})</span></div></div>
<div class="cols"><div><h3>Why now</h3><ul>
<li><b>Guidance is a sandbag:</b> FY3/26 net income guided to &yen;100bn, delivered &yen;174bn; FY3/27 OP guided &minus;7.5% with Q1 at 19.9% of the ordinary-profit guide vs 16.2% norm</li>
<li><b>Cheap vs peers:</b> 7-peer regression (R&sup2; 0.86) implies 0.95x EV/Sales vs 0.77x actual</li>
<li><b>Self-help:</b> DOE c.5%, &yen;100bn buyback programme, cross-holdings cut to 20% by Mar-2027</li>
<li><b>Stock down 35%</b> from Feb-26 peak on margin-peak and order worries</li></ul></div>
<div class="g"><h3>What has to go right</h3><ul>
<li>Completed-works gross margin holds near 13% as new, lower-margin jobs enter</li>
<li>No large fixed-price loss from Middle East-driven material disruption or Multiplex</li>
<li>Orders (Q1 &minus;7.2%) stabilise; developers do not defer on higher rates (BOJ 1.25%&dagger;)</li>
<li>Securities-gain-flattered EPS (FY3/26 &yen;249; underlying c.&yen;205&ndash;215) is read correctly</li></ul></div></div>
<div class="box" style="margin-top:.12in"><b>Sizing:</b> event-light, domestic-cyclical large-cap. Takeover is not the thesis (&lt;5% probability); the case rests on earnings beats, capital return and a modest re-rating.</div>'''))
S.append(slide("Business overview","Context","Obayashi at a glance: Japan's #2 super-contractor, c.86% of profit from Japan",'''
<div class="cols"><div><h3>What it does</h3><ul><li>Designs and builds offices, data centres, factories, hospitals, tunnels, dams and rail; fixed-price contracts paid on progress</li><li>Overseas c.33% of sales: US (Webcor, Kraemer, MWH, GCON), Asia; Multiplex (AU/UK/CA) pending</li><li>Property arm: development and leasing; lumpy, high margin</li></ul>
<h3>FY3/26 by division (&yen;bn)</h3><table><tr><th>Division</th><th>Sales</th><th>OP</th><th>Margin</th></tr><tr><td class="b">Domestic building</td><td>1,138.8</td><td>104.0</td><td>9.1%</td></tr><tr><td class="b">Domestic civil</td><td>426.6</td><td>40.9</td><td>9.6%</td></tr><tr><td class="b">Overseas building</td><td>508.0</td><td>11.9</td><td>2.3%</td></tr><tr><td class="b">Overseas civil</td><td>336.0</td><td>14.7&dagger;</td><td>4.4%</td></tr><tr><td class="b">Real estate/other (derived)</td><td>177.0</td><td>23.0</td><td>c.13%</td></tr><tr class="h"><td class="b">Group</td><td class="b">2,586.3</td><td class="b">194.7</td><td class="b">7.5%</td></tr></table></div>
<div><h3>Where the power sits</h3><ul><li><b>Upstream:</b> steel (Nippon Steel, JFE, Tokyo Steel), cement (Taiheiyo, UBE Mitsubishi), equipment (Mitsubishi Electric, Hitachi, Daikin, Kinden): price-taker, passes through with a lag</li><li><b>Midstream:</b> Obayashi design-build integration; capacity (labour) is the scarce asset</li><li><b>Downstream:</b> public clients (MLIT, NEXCO, JR Tokai) and developers (Mitsui Fudosan, Mitsubishi Estate, Mori Building)&dagger;</li></ul>
<div class="box dark" style="margin-top:.2in"><b>Most distinctive fact:</b> a four-firm oligopoly whose margin tripled on scarcity pricing, not product differentiation. The moat is cyclical.</div></div></div>'''))
S.append(slide("The setup","Context","Re-rated from &lt;1x book to c.2.3x, then 35% lower since February",'''
<div class="cols"><div style="flex:.9"><h3>Key levels&dagger;</h3><table><tr><th>Level</th><th>Price (&yen;)</th><th>Date</th></tr><tr><td class="b">All-time high</td><td>4,439</td><td>27 Feb 2026</td></tr><tr><td class="b">YTD low</td><td>2,891</td><td>19 Aug 2026</td></tr><tr><td class="b">Last close</td><td>3,008</td><td>30 Sep 2026</td></tr><tr><td class="b">~5 yrs ago</td><td>c.1,000 (approx.)</td><td>Late 2021</td></tr></table>
<p class="note">No daily series was retrievable; only one single-day move above 10% could be dated (5 Mar 2024, limit-up).</p>
<div class="box" style="margin-top:.2in">Net income exceeded ordinary income in FY3/26 (85%) &mdash; an estimated &yen;30&ndash;35bn of one-off gains. Underlying EPS &asymp; &yen;205&ndash;215.</div></div>
<div><h3>Key catalysts</h3><ul><li><b>Nov 2022:</b> FY3/23 forecast cut on building cost inflation</li><li><b>Jun 2023:</b> Silchester special-dividend proposal, 26.8% support</li><li><b>Mar 2024:</b> capital policy (DOE c.5%, ROE 10%+); limit-up</li><li><b>May 2025:</b> FY3/26 NI guided &minus;32%; shares c.&minus;9% intraday; outcome +74% vs guide</li><li><b>Feb 2026:</b> all-time high &yen;4,439</li><li><b>May 2026:</b> FY3/27 NI guided &minus;9.6%; &minus;7.8% intraday</li><li><b>Jun 2026:</b> Multiplex acquisition (US$540m)</li><li><b>Aug 2026:</b> Q1 OP +107%, orders &minus;7.2%; low &yen;2,891</li></ul></div></div>'''))
S.append(slide("Financials","Earnings","Operating income up 4.7x in four years; FY3/27 guided down but historically beaten",f'''
<div class="cols"><div><img src="assets/op_trend.png"></div><div><table><tr><th>&yen;bn</th><th>FY3/24</th><th>FY3/25</th><th>FY3/26</th><th>FY3/27E</th></tr><tr><td class="b">Sales</td><td>2,325</td><td>2,591</td><td>2,586</td><td>2,945</td></tr><tr><td class="b">Operating income</td><td>79.4</td><td>142.5</td><td>194.7</td><td>180.0</td></tr><tr><td class="b">Net income</td><td>75.1</td><td>145.4</td><td>173.8</td><td>157.0</td></tr><tr><td class="b">EPS (&yen;)</td><td>104.7</td><td>202.9</td><td>249.4</td><td>c.229</td></tr><tr><td class="b">DPS (&yen;)</td><td>75</td><td>81</td><td>88</td><td>94</td></tr></table>
<ul style="margin-top:.2in"><li>Margin drivers: change orders on large domestic jobs, selective bidding, fewer legacy losses</li><li>FY3/27: sales +13.9%, OP &minus;7.5% as new jobs start at lower progress margins; gross margin guided 13.0%</li><li>FY3/26: operating CF &yen;253bn, investing &minus;&yen;84bn&dagger;</li></ul></div></div>'''))
S.append(slide("Latest result","Earnings","Q1 FY3/27: profit doubled, but net income was gain-driven and orders fell",'''
<table style="width:62%;float:left"><tr><th>&yen;bn</th><th>Q1 FY3/27</th><th>Change</th><th>Comment</th></tr><tr><td class="b">Sales</td><td>623.4</td><td>+19.0%</td><td>Backlog burn; GCON</td></tr><tr><td class="b">Operating income</td><td>32.7</td><td>+107%</td><td>Margin 5.2% vs 3.0%</td></tr><tr><td class="b">Ordinary income</td><td>36.4</td><td>+98%</td><td>19.9% of FY guide (norm 16.2%)</td></tr><tr><td class="b">Net income</td><td>39.0</td><td>+116%</td><td>&gt; OP: c.&yen;20bn securities gain</td></tr><tr><td class="b">Orders</td><td>577.5</td><td>&minus;7.2%</td><td>Soft; FY target &yen;3.1tn</td></tr></table>
<div style="float:right;width:34%"><div class="box">Consensus FY ordinary profit &yen;193bn vs company guide &yen;183bn: the Street was already above guidance&dagger;. Guidance unchanged.</div></div><div style="clear:both"></div>
<div class="cols" style="margin-top:.25in"><div><h3>What is unusual</h3><ul><li>Net income above operating income twice running</li><li>Sales +19% with orders &minus;7%</li><li>Stock fell to its YTD low <i>after</i> a strong print</li></ul></div><div class="g"><h3>Read-through</h3><ul><li>Market is discounting margin peak and order slowdown, not Q1 earnings</li><li>Management tone: measured; cautious on orders from FY3/28 (Middle East)</li><li>Call transcripts not accessible: sentiment is headline-based</li></ul></div></div>'''))
S.append(slide("Question 1 &mdash; is Obayashi cheap?","Valuation","Cheaper than Japanese peers on EV/Sales, in line on P/E, expensive only on book",f'''
<table><tr><th>Metric</th><th>Obayashi</th><th>Kajima</th><th>Taisei</th><th>Shimizu</th><th>Vinci</th><th>Skanska</th><th>Balfour</th></tr>
<tr><td class="b">EV/Sales</td><td class="b" style="color:#2f6bd0">{M["ev_sales"]:.2f}x</td><td>1.03x</td><td>1.34x</td><td>0.63x</td><td>1.25x</td><td>0.52x</td><td>0.27x</td></tr>
<tr><td class="b">EV/EBITDA</td><td class="b" style="color:#2f6bd0">{M["ev_ebitda"]:.1f}x ({M["ev_ebitda_adj"]:.1f}x adj)</td><td>10.8&ndash;12.3x</td><td>10.3x</td><td>8.2&ndash;8.4x</td><td>7.7x</td><td>15.4x</td><td>6.8x</td></tr>
<tr><td class="b">EV/EBIT</td><td class="b" style="color:#2f6bd0">{M["ev_ebit"]:.1f}x</td><td>n/a</td><td>n/a</td><td>n/a</td><td>10.5x</td><td>14.7x</td><td>n/a</td></tr>
<tr><td class="b">P/E</td><td class="b" style="color:#2f6bd0">{M["pe_t"]:.1f}x / {M["pe_g"]:.1f}x fwd</td><td>15.3x fwd</td><td>n/a</td><td>12.9x fwd</td><td>14x</td><td>20x</td><td>12.9x</td></tr>
<tr><td class="b">EBIT margin</td><td class="b" style="color:#2f6bd0">7.5%</td><td>7.7%</td><td>9.0%</td><td>5.8%</td><td>11.9%</td><td>3.5%</td><td>2.1%</td></tr>
<tr><td class="b">Net debt/EBITDA</td><td class="b" style="color:#2f6bd0">{M["nd_ebitda"]:.1f}x (net cash)</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr></table>
<p class="note">Aggregator snippets, mixed dates; indicative. JGAAP (no IFRS 16) makes Obayashi's EV/EBITDA look cheaper than IFRS peers. Obayashi EV = market cap less net cash.</p>
<div class="cols" style="margin-top:.12in"><div><h3>What the comparison shows</h3><ul><li>Margin in line with Kajima, above Shimizu, yet P/E and EV/Sales trail Kajima and Taisei</li><li>FCF yield proxy c.8%; net cash vs. levered global peers</li></ul></div><div class="g"><h3>The honest counter-read</h3><ul><li>Book multiple 1.6x is high vs own history (c.0.6&ndash;1.0x for 2015&ndash;22&dagger;)</li><li>Peer data is mixed-source; own-history multiples were not retrievable</li></ul></div></div>'''))
S.append(slide("Question 1 &mdash; is Obayashi cheap?","Valuation","The regression says c.23% undervalued, a smaller outlier than a luxury-peer set would suggest",'''
<div class="cols"><div style="flex:1.25"><img src="assets/regression.png"></div><div><h3>Why this is useful, and its limits</h3><ul><li>R&sup2; 0.86, t = 5.5 across 7 listed peers: margin explains most of EV/Sales</li><li>Obayashi implied 0.95x vs 0.77x actual; implied value c.&yen;3,670/share (+22%)</li><li>n = 7; Vinci and Taisei carry the slope; IFRS/JGAAP and mixed-date EVs</li><li>Not a trade by itself: a margin-sustainability discount may be rational</li></ul></div></div>'''))
S.append(slide("Earnings and scenarios","Forecast",f"EPS of &yen;{b[0]['eps']:.0f} / {b[1]['eps']:.0f} / {b[2]['eps']:.0f} in FY3/27&ndash;29E; value range &yen;{SCV['Bear'][1]:,.0f}&ndash;{SCV['Bull'][1]:,.0f}",f'''
<div class="cols"><div><table><tr><th>Base case</th><th>FY3/27E</th><th>FY3/28E</th><th>FY3/29E</th></tr><tr><td class="b">Sales (&yen;bn)</td><td>{b[0]["sales"]:,.0f}</td><td>{b[1]["sales"]:,.0f}</td><td>{b[2]["sales"]:,.0f}</td></tr><tr><td class="b">Operating income</td><td>{b[0]["op"]:.0f}</td><td>{b[1]["op"]:.0f}</td><td>{b[2]["op"]:.0f}</td></tr><tr><td class="b">OP margin</td><td>{b[0]["opm"]:.1f}%</td><td>{b[1]["opm"]:.1f}%</td><td>{b[2]["opm"]:.1f}%</td></tr><tr><td class="b">Net income</td><td>{b[0]["ni"]:.0f}</td><td>{b[1]["ni"]:.0f}</td><td>{b[2]["ni"]:.0f}</td></tr><tr><td class="b">Avg shares (m)</td><td>{b[0]["shares"]}</td><td>{b[1]["shares"]}</td><td>{b[2]["shares"]}</td></tr><tr class="h"><td class="b">EPS (&yen;)</td><td class="b">{b[0]["eps"]:.0f}</td><td class="b">{b[1]["eps"]:.0f}</td><td class="b">{b[2]["eps"]:.0f}</td></tr><tr><td class="b">Bear / Bull EPS FY3/28E</td><td colspan="3">&yen;{BEAR[1]["eps"]:.0f} / &yen;{BULL[1]["eps"]:.0f}</td></tr></table>
<p class="note">30% tax; gains &yen;40bn / 20 / 15; buybacks cut shares c.1% a year; EBIT beats guidance by c.7% in FY3/27E.</p></div>
<div><table><tr><th>Scenario (FY3/28E)</th><th>Bear 30%</th><th>Base 50%</th><th>Bull 20%</th></tr><tr><td class="b">EBITDA (&yen;bn)</td><td>200</td><td>247</td><td>295</td></tr><tr><td class="b">EV/EBITDA</td><td>6.5x</td><td>8.5x</td><td>9.5x</td></tr><tr><td class="b">Value / share</td><td>&yen;{SCV["Bear"][1]:,.0f}</td><td>&yen;{SCV["Base"][1]:,.0f}</td><td>&yen;{SCV["Bull"][1]:,.0f}</td></tr><tr class="h"><td class="b">vs &yen;3,008</td><td class="b">{SCV["Bear"][1]/PRICE-1:+.0%}</td><td class="b">{SCV["Base"][1]/PRICE-1:+.0%}</td><td class="b">{SCV["Bull"][1]/PRICE-1:+.0%}</td></tr></table>
<div class="box" style="margin-top:.2in">Probability-weighted <b>&yen;{PW:,.0f}</b> (+{(PW/PRICE-1)*100:.0f}%). Equity = EBITDA x multiple + net cash + 75% of cross-held shares. Regression cross-check &yen;3,670.</div></div></div>'''))
S.append(slide("M&amp;A and takeover","Optionality","Takeover is not the thesis: a &yen;2tn target is 10x Japan's largest contractor deal",'''
<div class="cols"><div><h3>Comparable deals (EV/EBITDA)</h3><table><tr><th>Target / acquirer</th><th>Date</th><th>EV/EBITDA</th></tr><tr><td>Multiplex / Obayashi</td><td>Jun 2026</td><td>8.7&ndash;10.5x</td></tr><tr><td>Cupertino / Quanta</td><td>Jul 2024</td><td>c.9.1x</td></tr><tr><td>Miller Electric / EMCOR</td><td>Jan 2025</td><td>10.8x</td></tr><tr><td>CEC / Sterling</td><td>Jul 2025</td><td>9.6x</td></tr><tr><td>PayneCrest / Primoris</td><td>Mar 2026</td><td>c.10.5x</td></tr><tr><td>Superior / MasTec</td><td>Jul 2026</td><td>c.7.0x</td></tr><tr><td>TRC / WSP</td><td>Dec 2025</td><td>14.5x</td></tr><tr><td>Toyo / Taisei (premium 2.9%)</td><td>Aug 2025</td><td>n/a</td></tr></table><p class="note">US specialty median 9.6x; broader set median 10.1x. No Japanese deal disclosed EBITDA.</p></div>
<div><h3>If a bid came</h3><ul><li>25&ndash;40% premium = &yen;3,760&ndash;4,210; 10.3&ndash;11.6x EBITDA; 0.97&ndash;1.09x sales</li><li><b>Impediments:</b> size, licensing and client ties, JFTC, METI 2026 guidance on rejecting bids, no obvious financial buyer</li><li>Probability within 12 months: &lt;5%; no rumours found</li></ul><h3>Obayashi's own deals</h3><ul><li>MWH (90%, c.US$126m, Jan 2024); GCON (Dec 2025, undisclosed); Multiplex (US$540m, closing c.30 Sep 2026&dagger;)</li></ul>
<div class="box"><b>SK Telecom / Anthropic:</b> 3,860,330 shares at 30 Jun 2026; carrying value KRW 3.505tn; c.0.24% (0.3% per Hana Securities). Unrelated to Obayashi.</div></div></div>'''))
S.append(slide("Management and ownership","Governance","Finance-trained CEO, family chairman, no controlling holder, one activist (2023)",'''
<div class="cols"><div><h3>Leadership</h3><ul><li><b>Toshimi Sato</b> (66), CEO since Apr 2025; finance and planning career; first non-engineer, non-family president</li><li><b>Takeo Obayashi</b> (72), chairman; family; 2.46% (c.&yen;51bn)</li><li><b>Kenji Hasuwa</b> (72), vice chairman; president 2018&ndash;25 after the Linear scandal</li><li>Board: 6 of 10 outside and independent; 3 women; Tomita joined Jun 2026</li></ul><h3>Red flags</h3><ul><li>Linear bid-rigging: &yen;3.1bn surcharge, &yen;200m fine, 4-month Tokyo suspension</li><li>Oct 2024 tunnel injury; false statements to inspectors (&yen;200k fines, Mar 2026)</li><li>No related-party or restatement issue found</li></ul></div>
<div><h3>Top holders (31 Mar 2026)&dagger;</h3><table><tr><th>Holder</th><th>%</th></tr><tr><td>Japan Master Trust</td><td>15.51</td></tr><tr><td>Custody Bank of Japan</td><td>7.26</td></tr><tr><td>State Street 505001 / 505103</td><td>3.66 / 2.60</td></tr><tr><td>Takeo Obayashi (insider)</td><td>2.46</td></tr><tr><td>Nippon Life</td><td>2.13</td></tr><tr><td>Employee association</td><td>1.83</td></tr></table><p class="note">Foreign c.40%. Activism: Silchester 2023 (&yen;12 special dividend; 26.8% support). Short interest negligible (margin short 75k shares).</p></div></div>'''))
S.append(slide("Adversarial view","Risks","Bull, bear and the contrarian read",'''
<div class="cols"><div><h3>Bull</h3><ul><li>Oligopoly with labour-limited capacity: 13% gross margin defensible</li><li>Data centres, fabs, resilience (&yen;20tn+), Linear Shizuoka</li><li>6&ndash;7% shareholder yield; &yen;289bn cross-holding to monetise</li></ul><h3>Bear</h3><ul><li>Each 1pt of OP margin = &yen;29bn (c.13% of EPS)</li><li>Fixed-price cost shock; Multiplex legacy; compliance event</li><li>Underlying EPS &asymp; &yen;205&ndash;215, not &yen;249</li></ul></div>
<div class="g"><h3>Pre-mortem: &yen;2,000 by Oct 2027</h3><ul><li>Two or three large jobs take provisions; FY3/27 OP slides to &yen;150bn</li><li>Orders &minus;10%; peers discount; pricing discipline ends</li><li>Multiplex goodwill and provisions of &yen;20&ndash;30bn</li><li>New plan cuts payout ambition</li></ul>
<div class="box dark" style="margin-top:.15in"><b>Contrarian:</b> the market capitalises guided earnings as a normal downcycle. If guidance is again a sandbag and 13% is structural, the stock is c.10&ndash;11x underlying EPS, c.7x adjusted EV/EBITDA, with a 6&ndash;7% payout. The real risk is a few fixed-price jobs, not the margin level.</div></div></div>'''))
S.append(slide("Forensic view","Risks","Accounting and disclosure red flags",'''
<table><tr><th>Area</th><th>Observation</th><th>Risk</th></tr>
<tr><td class="b">Revenue recognition</td><td>Cost-to-cost estimates; change orders drove FY3/26 profit</td><td>High</td></tr>
<tr><td class="b">Earnings quality</td><td>Net income &gt; OP in FY3/26 and Q1; securities-gain dependence will fade</td><td>High</td></tr>
<tr><td class="b">Goodwill</td><td>GCON, MWH, Multiplex (c.&yen;86bn) add amortisation and impairment risk</td><td>Med-high</td></tr>
<tr><td class="b">Contingencies</td><td>Bid-rigging legacy, overseas disputes, defect warranties</td><td>Med-high</td></tr>
<tr><td class="b">Leases</td><td>JGAAP: off balance sheet; EV/EBITDA not comparable with IFRS peers</td><td>Medium</td></tr>
<tr><td class="b">Cash flow</td><td>Operating CF &yen;50bn&ndash;253bn over five years&dagger;: working-capital swings</td><td>Medium</td></tr>
<tr><td class="b">Related parties / SBC</td><td>None found; stock compensation immaterial</td><td>Low</td></tr></table>
<p class="note">Items marked &dagger; unverified against a primary filing. Check the yuho notes on contract losses, segments, related parties and investment securities.</p>'''))
S.append(slide("Catalysts","Calendar","What to watch, next 9 months",'''
<table><tr><th>Timing</th><th>Catalyst</th><th>What to watch</th></tr>
<tr><td class="b">By 30 Sep 2026</td><td>Multiplex closing (unconfirmed)</td><td>Final price, net debt, goodwill</td></tr>
<tr><td class="b">29&ndash;30 Oct</td><td>BOJ meeting</td><td>Rates and developer capex</td></tr>
<tr><td class="b">Early/mid Nov</td><td>Q2 / H1 FY3/27 results</td><td>Orders, gross margin, guidance raise; interim DPS &yen;47</td></tr>
<tr><td class="b">17&ndash;18 Dec</td><td>BOJ; FY2027 budget</td><td>Resilience and public-works budget</td></tr>
<tr><td class="b">c.9 Feb 2027</td><td>Q3 results</td><td>Guidance revision; gains</td></tr>
<tr><td class="b">Mar 2027</td><td>Cross-holding 20% deadline</td><td>Residual sales; buyback completion</td></tr>
<tr><td class="b">c.mid-May 2027</td><td>FY3/27 results; successor medium-term plan</td><td>ROE, payout, M&amp;A framework</td></tr>
<tr><td class="b">Late Jun 2027</td><td>123rd AGM</td><td>Board; proposals</td></tr></table>
<div class="box" style="margin-top:.25in"><b>Data caveat:</b> Obayashi IR, EDINET and finance sites were blocked in this environment. Verify flagged figures against the FY3/26 tanshin, the 2026 Integrated Report and the yuho before sizing. Dates are inferred from prior years.</div>'''))
html="<html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"+"".join(S)+"</body></html>"
open("deck.html","w").write(html); print(len(S))
