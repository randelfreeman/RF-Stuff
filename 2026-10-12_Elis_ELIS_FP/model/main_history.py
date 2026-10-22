"""Lead-analyst model, part 1: historical metrics for Elis SA from S&P Capital IQ raw statements.
Inputs : provenance/raw/main/006..009 CSVs (EUR m, lossless re-encodings of S&P responses).
Outputs: model/main_history.csv (+ .json). All derived numbers are [calc]."""
import csv, json, os, io
BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, '..', 'provenance', 'raw', 'main')

def read_wide(fname, section=None):
    rows, cur, out, header = [], None, {}, None
    with open(os.path.join(RAW, fname)) as f:
        text = f.read()
    lines = [l for l in text.splitlines() if l and not l.startswith('# ')]
    # support '## SECTION' blocks
    blocks, name = {}, '_'
    for l in lines:
        if l.startswith('## '):
            name = l[3:].strip(); blocks[name] = []; continue
        blocks.setdefault(name, []).append(l)
    want = blocks[section] if section else blocks['_']
    rdr = list(csv.reader(io.StringIO('\n'.join(want))))
    header = rdr[0]
    for r in rdr[1:]:
        out[r[0]] = {h: (float(v) if v not in ('', None) else None) for h, v in zip(header[1:], r[1:])}
    return header[1:], out

yrs, IS = read_wide('006_spcapiq_income_statement_annual_2016_2025.csv')
_, BS = read_wide('007_spcapiq_balance_sheet_annual_2016_2025.csv')
_, CF = read_wide('008_spcapiq_cashflow_annual_2016_2025.csv')
icols, ISQ = read_wide('009_spcapiq_interim_ltm_statements.csv', 'INCOME STATEMENT')
bcols, BSQ = read_wide('009_spcapiq_interim_ltm_statements.csv', 'BALANCE SHEET (31-Mar-2026 and 30-Jun-2026 identical)')
ccols, CFQ = read_wide('009_spcapiq_interim_ltm_statements.csv', 'CASH FLOW LTM to 30-Jun-2026')

def g(d, item, col):
    v = d.get(item, {}).get(col)
    return 0.0 if v is None else v

rows = []
for y in yrs:
    rev = g(IS, 'Total Revenues', y); ebit = g(IS, 'Operating Income', y)
    amort = g(IS, 'Amortization of Goodwill and Intangible Assets - (IS)', y)
    da_cf = g(CF, 'Depreciation & Amortization, Total - CF', y)
    ebitda = ebit + da_cf
    ni = g(IS, 'Net Income - (IS)', y)
    ebt = g(IS, 'EBT, Incl. Unusual Items', y); tax = g(IS, 'Income Tax Expense', y)
    cfo = g(CF, 'Cash from Operations', y); capex = -g(CF, 'Capital Expenditure', y)
    sale_ppe = g(CF, 'Sale of Property, Plant, and Equipment', y); intang = -g(CF, 'Sale (Purchase) of Intangible assets', y)
    other_fin = g(CF, 'Other Financing Activities, Total', y)
    fcf_pre_lease = cfo - capex + sale_ppe - intang
    debt = g(BS, 'Short-term Borrowings', y) + g(BS, 'Current Portion of Long-Term Debt', y) + g(BS, 'Long-Term Debt', y)
    leases = g(BS, 'Current Portion of Leases', y) + g(BS, 'Long-Term Leases', y)
    cash = g(BS, 'Cash And Equivalents', y)
    equity = g(BS, 'Common Stock & APIC', y) + g(BS, 'Retained Earnings', y) + g(BS, 'Treasury Stock & Other', y)
    mi = g(BS, 'Minority Interest', y)
    rows.append(dict(period=y, revenue=rev, gross_profit=g(IS, 'Gross Profit', y), ebit_sp=ebit, amort_ppa=amort,
        ebita=ebit + amort, da_total_cf=da_cf, ebitda_calc=ebitda, net_interest=g(IS, 'Net Interest Expenses', y),
        unusual=g(IS, 'EBT, Incl. Unusual Items', y) - g(IS, 'EBT, Excl. Unusual Items', y), ebt=ebt, tax=tax,
        tax_rate=(tax / ebt if ebt else None), net_income=ni, cfo=cfo, capex=capex, capex_pct=capex / rev,
        sale_ppe=sale_ppe, intangibles_capex=intang, fcf_pre_lease=fcf_pre_lease, other_financing=other_fin,
        acquisitions=-g(CF, 'Cash Acquisitions', y), buybacks=-g(CF, 'Repurchase of Common Stock', y),
        dividends_paid=-(g(CF, 'Common Dividends Paid', y) + g(CF, 'Special Dividend Paid', y)),
        sbc=g(CF, 'Stock-Based Compensation (CF)', y), gross_debt_ex_leases=debt, lease_liabilities=leases,
        cash=cash, net_debt_ex_leases=debt - cash, net_debt_incl_leases=debt + leases - cash, equity=equity,
        minority=mi, goodwill=g(BS, 'Goodwill', y), other_intangibles=g(BS, 'Other Intangibles, Total', y),
        total_assets=g(BS, 'Total Assets', y), receivables=g(BS, 'Accounts Receivable, Total', y),
        inventory=g(BS, 'Inventory', y), payables=g(BS, 'Accounts Payable, Total', y),
        net_ppe=g(BS, 'Net Property Plant And Equipment', y), treasury_stock=g(BS, 'Treasury Stock', y)))

# LTM to 30-Jun-2026 (IS & CF LTM; BS at 30-Jun-2026)
L = 'LTM to 2026-06-30'; B = '2026-06-30'
rev = g(ISQ, 'Total Revenues', L); ebit = g(ISQ, 'Operating Income', L); amort = g(ISQ, 'Amortization of Goodwill and Intangible Assets - (IS)', L)
da_cf = g(CFQ, 'Depreciation & Amortization, Total - CF', L)
debt = g(BSQ, 'Short-term Borrowings', B) + g(BSQ, 'Current Portion of Long-Term Debt', B) + g(BSQ, 'Long-Term Debt', B)
leases = g(BSQ, 'Current Portion of Leases', B) + g(BSQ, 'Long-Term Leases', B); cash = g(BSQ, 'Cash And Equivalents', B)
equity = g(BSQ, 'Common Stock & APIC', B) + g(BSQ, 'Retained Earnings', B) + g(BSQ, 'Treasury Stock & Other', B)
cfo = g(CFQ, 'Cash from Operations', L); capex = -g(CFQ, 'Capital Expenditure', L)
rows.append(dict(period='LTM Jun-26', revenue=rev, gross_profit=g(ISQ, 'Gross Profit', L), ebit_sp=ebit, amort_ppa=amort,
    ebita=ebit + amort, da_total_cf=da_cf, ebitda_calc=ebit + da_cf, net_interest=g(ISQ, 'Net Interest Expenses', L),
    unusual=g(ISQ, 'EBT, Incl. Unusual Items', L) - g(ISQ, 'EBT, Excl. Unusual Items', L), ebt=g(ISQ, 'EBT, Incl. Unusual Items', L),
    tax=g(ISQ, 'Income Tax Expense', L), tax_rate=g(ISQ, 'Income Tax Expense', L) / g(ISQ, 'EBT, Incl. Unusual Items', L),
    net_income=g(ISQ, 'Net Income - (IS)', L), cfo=cfo, capex=capex, capex_pct=capex / rev,
    sale_ppe=g(CFQ, 'Sale of Property, Plant, and Equipment', L), intangibles_capex=-g(CFQ, 'Sale (Purchase) of Intangible assets', L),
    fcf_pre_lease=cfo - capex + g(CFQ, 'Sale of Property, Plant, and Equipment', L) + g(CFQ, 'Sale (Purchase) of Intangible assets', L),
    other_financing=g(CFQ, 'Other Financing Activities, Total', L), acquisitions=-g(CFQ, 'Cash Acquisitions', L),
    buybacks=-g(CFQ, 'Repurchase of Common Stock', L), dividends_paid=-g(CFQ, 'Common Dividends Paid', L),
    sbc=g(CFQ, 'Stock-Based Compensation (CF)', L), gross_debt_ex_leases=debt, lease_liabilities=leases, cash=cash,
    net_debt_ex_leases=debt - cash, net_debt_incl_leases=debt + leases - cash, equity=equity, minority=0.0,
    goodwill=g(BSQ, 'Goodwill', B), other_intangibles=g(BSQ, 'Other Intangibles, Total', B), total_assets=g(BSQ, 'Total Assets', B),
    receivables=g(BSQ, 'Accounts Receivable, Total', B), inventory=g(BSQ, 'Inventory', B), payables=g(BSQ, 'Accounts Payable, Total', B),
    net_ppe=g(BSQ, 'Net Property Plant And Equipment', B), treasury_stock=g(BSQ, 'Treasury Stock', B)))

# H1 figures (S&P semi-annual split evenly into quarters -> H1 = Q1+Q2)
h1 = {}
for lab, q1, q2 in [('H1 2025', 'FY2025Q1(3m to 2025-03-31)', 'FY2025Q2(3m to 2025-06-30)'), ('H2 2025', 'FY2025Q3(3m to 2025-09-30)', 'FY2025Q4(3m to 2025-12-31)'),
                    ('H1 2026', 'FY2026Q1(3m to 2026-03-31)', 'FY2026Q2(3m to 2026-06-30)')]:
    h1[lab] = {k: g(ISQ, k, q1) + g(ISQ, k, q2) for k in ['Total Revenues', 'Gross Profit', 'Operating Income', 'Amortization of Goodwill and Intangible Assets - (IS)', 'Net Interest Expenses', 'EBT, Incl. Unusual Items', 'Income Tax Expense', 'Net Income - (IS)']}

# derived ratios
prev = None
for r in rows:
    r['gross_margin'] = r['gross_profit'] / r['revenue']; r['ebit_margin_sp'] = r['ebit_sp'] / r['revenue']
    r['ebita_margin'] = r['ebita'] / r['revenue']; r['ebitda_margin_calc'] = r['ebitda_calc'] / r['revenue']
    r['net_margin'] = r['net_income'] / r['revenue']
    r['nd_ebitda_ex_leases'] = r['net_debt_ex_leases'] / r['ebitda_calc']; r['nd_ebitda_incl_leases'] = r['net_debt_incl_leases'] / r['ebitda_calc']
    r['dso_days'] = r['receivables'] / r['revenue'] * 365
    r['fcf_conversion_pre_lease'] = r['fcf_pre_lease'] / r['net_income'] if r['net_income'] else None
    r['goodwill_intang_pct_assets'] = (r['goodwill'] + r['other_intangibles']) / r['total_assets']
    r['interest_cover_ebit'] = -r['ebit_sp'] / r['net_interest'] if r['net_interest'] else None
    if prev and r['period'].startswith('FY'):
        r['revenue_growth'] = r['revenue'] / prev['revenue'] - 1
        avg_eq = (r['equity'] + prev['equity']) / 2
        ic, ic_prev = r['equity'] + r['net_debt_incl_leases'], prev['equity'] + prev['net_debt_incl_leases']
        r['roe'] = r['net_income'] / avg_eq
        r['roic_ebita'] = r['ebita'] * (1 - (r['tax_rate'] or 0)) / ((ic + ic_prev) / 2)
        r['roic_ebit'] = r['ebit_sp'] * (1 - (r['tax_rate'] or 0)) / ((ic + ic_prev) / 2)
    if r['period'].startswith('FY'):
        prev = r

out = os.path.join(BASE, 'main_history.csv')
keys = list(rows[-1].keys() | rows[0].keys())
order = ['period'] + [k for k in rows[0].keys() if k != 'period'] + [k for k in ['revenue_growth', 'roe', 'roic_ebita', 'roic_ebit'] if k not in rows[0]]
with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=order); w.writeheader()
    for r in rows: w.writerow({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items() if k in order})
json.dump({'annual_and_ltm': rows, 'half_years': h1}, open(os.path.join(BASE, 'main_history.json'), 'w'), indent=1)
# print a compact view
fmt = lambda v: '' if v is None else (f'{v*100:.1f}%' if abs(v) < 3 and not float(v).is_integer() else f'{v:,.1f}')
for k in ['revenue', 'revenue_growth', 'ebitda_calc', 'ebitda_margin_calc', 'ebita', 'ebita_margin', 'ebit_sp', 'ebit_margin_sp', 'net_income', 'tax_rate', 'cfo', 'capex', 'capex_pct', 'fcf_pre_lease', 'acquisitions', 'dividends_paid', 'buybacks', 'net_debt_ex_leases', 'lease_liabilities', 'nd_ebitda_ex_leases', 'nd_ebitda_incl_leases', 'equity', 'roe', 'roic_ebita', 'dso_days', 'goodwill', 'goodwill_intang_pct_assets', 'interest_cover_ebit']:
    print(f'{k:28s}', ' '.join(f'{fmt(r.get(k)):>9s}' for r in rows))
print('periods:', [r['period'] for r in rows])
for k, v in h1.items(): print(k, {kk: round(vv, 2) for kk, vv in v.items()})
