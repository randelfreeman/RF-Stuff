const path=require('path'),fs=require('fs');
const order='s01_layman,s02_catalysts,s03_business,s04_macro,s05_moat,s06_supply,s07_financials,s08_earnings,s09_eps,s10_capital,s11_valuation,s12_mna,s13_management,s14_board,s15_shareholders,s16_strategy,s18_returns,s19_bullbear,s20_scenarios,s21_questions,s22_short,s23_timeline,s99_appendix'.split(',');
const h=['Investment summary'];
for(const s of order){const m=require(path.join(__dirname,'report',s+'.js'));for(const b of m) if(b.t==='h1') h.push(b.text);}
console.log(JSON.stringify(h,null,1));
