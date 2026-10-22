from docx_helpers import *
import report_part1 as p1, report_part2 as p2
d = new_doc()
p1.cover(d); p1.exec_summary(d); p1.laymans(d); p1.price_history(d); p1.business(d); p1.macro(d); p1.moat(d)
p1.supply_chain(d); p1.financials(d); p1.earnings(d); p1.eps_section(d)
p2.capital_structure(d); p2.valuation(d); p2.ma(d); p2.management(d); p2.board(d); p2.holders(d); p2.strategy(d)
p2.stakes(d); p2.returns(d); p2.bull_bear(d); p2.scenarios(d); p2.questions(d); p2.shortseller(d); p2.timeline(d); p2.appendix(d)
d.save("Obayashi_1802JT_Equity_Research_Report.docx"); print("saved")
