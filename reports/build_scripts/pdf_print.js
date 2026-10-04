// Usage: node pdf_print.js in.html out.pdf [width] [height]
const { chromium } = require("playwright");
(async () => {
  const [, , inp, out, w = "13.333in", h = "7.5in"] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + require("path").resolve(inp), { waitUntil: "networkidle" });
  await page.pdf({ path: out, width: w, height: h, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
  console.log("pdf written", out);
})();
