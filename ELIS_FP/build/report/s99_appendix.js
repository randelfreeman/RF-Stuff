module.exports = [
  { t: 'h1', text: 'Appendix: sources, methodology and data gaps' },
  { t: 'bullets', items: [
    '**Sources:** only S&P Global Capital IQ (S&P Deterministic Retrieval connector: financial statements and line items, company info) and ProntoNLP (S&P transcripts, Elis annual/semi-annual reports and releases, consensus, prices, peer graph, sentiment). No web browsing; the Financial Datasets connector was not used.',
    '**Hyperlinks:** ProntoNLP sentence markers [#n] and document links open the source in ProntoNLP; S&P figures link to the Capital IQ document viewer where the connector returned a link. Statement-level S&P pulls returned no links — such figures are marked "S&P, link n/a" or cited generally as S&P Capital IQ.',
    '**Conventions:** [calc] analyst calculation; [e] estimate; [u] unverified/background knowledge not found in permitted sources; [inferred] interpretation of garbled filing text. Fiscal year = calendar year for Elis; peers on their own fiscal years (LTM used).',
    '**Data gaps:** forward consensus (EPS/EBITDA) for Elis and peers; full top-10 shareholder register; short interest; euro amounts of executive pay and holdings; full-year € segment revenue (non-indexed tables); supplier names; Q3 2025 standalone revenue; ProntoNLP price history before 2019 (series partly dividend-adjusted).',
    '**Process note:** research was split across seven workers; four were stopped by an API rate limit after collecting and saving their raw data and structured files — the lead analyst completed their analysis (including the peer multiples and regression) from those saved files. Every connector call and raw response is listed in the separate data-provenance document.',
    '**Disclaimer:** prepared for institutional investors for discussion purposes; not investment advice; estimates are subject to change.',
  ] },
];
