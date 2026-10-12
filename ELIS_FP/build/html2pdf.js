// Usage: node html2pdf.js in.html out.pdf [landscape16x9|a4]
const { chromium } = require('playwright');
(async () => {
  const [,, inp, out, mode] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  if (mode === 'a4') await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  else await page.pdf({ path: out, width: '13.333in', height: '7.5in', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('wrote', out);
})();
