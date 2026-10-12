// usage: node render_pdf.js input.html output.pdf [landscape16x9]
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [,, inp, out, mode] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  if (mode === 'slides') {
    await page.pdf({ path: out, width: '13.333in', height: '7.5in', printBackground: true, margin: {top:'0',bottom:'0',left:'0',right:'0'} });
  } else {
    await page.pdf({ path: out, format: 'A4', printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: '<div style="font-size:7px;color:#6b7280;width:100%;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>Coupang, Inc. (NYSE: CPNG) | Institutional equity research | Data: S&amp;P Global Capital IQ, ProntoNLP | [u] = unverified, [e] = estimate</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>',
      margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  }
  await browser.close();
})();
