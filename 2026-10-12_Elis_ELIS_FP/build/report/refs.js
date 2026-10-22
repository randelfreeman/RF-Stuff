// Shared citation helpers. All URLs come verbatim from raw MCP responses (S&P registry built from provenance/raw/*).
const path = require('path');
const SPL = require(path.join(__dirname, '..', '..', 'model', 'sp_source_links.json'));
function sp(item, period, display, cid = 'C_27989') {
  const r = SPL[`${cid}|${item}|${period}`];
  if (r && r.url) return `[${display}](${r.url})`;
  return `${display} {{sup:S&P, link n/a}}`;
}
const DOC = {
  H126: '[H1 2026 earnings call, 29-Jul-2026](https://gam.prontonlp.com/#/ref/$DOCID_T000003774119)',
  FY25: '[FY2025 earnings call, 11-Mar-2026](https://gam.prontonlp.com/#/ref/$DOCID_T000003676656)',
  CMD: '[Capital Markets Day, 27-May-2025](https://gam.prontonlp.com/#/ref/$DOCID_T000003468571)',
  H125: '[H1 2025 earnings call, 30-Jul-2025](https://gam.prontonlp.com/#/ref/$DOCID_T000003512646)',
  FY24: '[FY2024 earnings call, 6-Mar-2025](https://gam.prontonlp.com/#/ref/$DOCID_T000003394029)',
  URD25: '[FY2025 annual report/URD](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000259591248)',
  URD24: '[FY2024 annual report/URD](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000239166805)',
  SR26: '[H1 2026 semi-annual report](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000264324010)',
  SR26b: '[H1 2026 semi-annual report (2nd filing)](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000264346860)',
  FS25: '[FY2025 results release](https://gam.prontonlp.com/#/ref/$DOCID_NONSEC000256665099)',
  ELIS: '[Elis SA](https://gam.prontonlp.com/#/ref/$COMPANY_27989)',
};
const SPN = 'S&P Capital IQ (Elis SA, company id C_27989)';
module.exports = { sp, DOC, SPN };
