import render, content
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from docx.shared import RGBColor
T='TOTO Ltd (5332 JP)'; SUB='Equity Research | 4 October 2026'
def cover(S, W):
    st=lambda n,s,f='Lib',c='#16243D',l=None: ParagraphStyle(n,fontName=f,fontSize=s,leading=l or s*1.25,textColor=colors.HexColor(c))
    out=[Spacer(1,40),Paragraph('EQUITY RESEARCH  |  JAPAN  |  BUILDING PRODUCTS / SEMICONDUCTOR CERAMICS',st('k',8.5,'Lib-B','#2F6FD0')),Spacer(1,14),
         Paragraph('TOTO Ltd',st('t',34,'Lib-B')),Spacer(1,6),Paragraph('5332 JP — The toilet maker with a semiconductor engine',st('s',15,'Lib','#5E6878')),Spacer(1,22)]
    t=Table([[Paragraph('<b>RATING: BUY</b>',st('r',12,'Lib-B','#FFFFFF')),Paragraph('<b>12-MO TARGET: ¥7,200 (+18%)</b>',st('r2',12,'Lib-B','#16243D'))]],colWidths=[W*0.4,W*0.5])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),colors.HexColor('#2F6FD0')),('BOX',(1,0),(1,0),1.2,colors.HexColor('#2F6FD0')),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('LEFTPADDING',(0,0),(-1,-1),12)]))
    out+=[t,Spacer(1,22)]
    kp=[['Price (2 Oct 2026)','¥6,097'],['Market cap','~¥1.0tn / US$6.7bn'],['EV (e)','~¥937bn'],['52-week range','¥3,766 – ¥9,500'],['P/E FY3/27E / FY3/28E','21.8x / 17.3x'],['EV/EBITDA FY3/26A','10.6x'],['Dividend yield','2.0%'],['Ceramics share of FY3/26 segment OP','~51%'],['Probability-weighted value','~¥6,975 (+14%)']]
    k=Table(kp,colWidths=[W*0.45,W*0.35]); k.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Lib'),('FONTSIZE',(0,0),(-1,-1),9.5),('FONTNAME',(1,0),(1,-1),'Lib-B'),('LINEBELOW',(0,0),(-1,-1),0.4,colors.HexColor('#C9CED8')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    out+=[k,Spacer(1,24),Paragraph('Contents: investment summary; layman\'s guide; price catalysts; business model; macro; moats; supply chain; 5-year financials & KPIs; earnings & sentiment; EPS forecasts; capital structure; valuation & regression; M&A; management; board; shareholders & activism; strategy; stakes; capital returns; adversarial analysis; scenarios; questions for management; short-seller view; catalysts.',st('c',8.5,'Lib','#5E6878',12)),
          Spacer(1,30),Paragraph('Prepared for buy-side investment committee review. Figures marked (e)/~ are estimates — see Data Notes (Section 25).',st('d',7.5,'Lib-I','#5E6878'))]
    return out
render.build_pdf('TOTO_5332JP_Full_Report.pdf',T,SUB,cover,content.B)
W=RGBColor
cl=[('EQUITY RESEARCH | JAPAN | BUILDING PRODUCTS / SEMICONDUCTOR CERAMICS',8.5,True,W(0x2F,0x6F,0xD0)),('TOTO Ltd (5332 JP)',30,True,W(0x16,0x24,0x3D)),('The toilet maker with a semiconductor engine',15,False,W(0x5E,0x68,0x78)),
    ('RATING: BUY  |  12-month target ¥7,200 (+18%)  |  Probability-weighted ~¥6,975',12,True,W(0x2F,0x6F,0xD0)),
    ('Price ¥6,097 (2 Oct 2026) | Mkt cap ~¥1.0tn | EV ~¥937bn (e) | P/E 21.8x FY3/27E | EV/EBITDA 10.6x FY3/26A | Yield 2.0%',10,False,W(0x16,0x24,0x3D)),
    ('Equity Research | 4 October 2026. Figures marked (e)/~ are estimates — see Data Notes (Section 25).',8,False,W(0x5E,0x68,0x78))]
render.build_docx('TOTO_5332JP_Full_Report.docx',T,SUB,cl,content.B)
print('ok')
