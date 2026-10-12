# Raw-file formats used by agent C_mna_capital

* `*.json` — verbatim tool response text.
* `*.jsonl` (format "C-compact-v1") — LOSSLESS re-encoding of a ProntoNLP searchSentences / getSentenceContext response, used to keep files compact (protocol section 3 allows lossless re-encoding):
  - Line 1 = header object: `_reencoding` note, `constant_fields` (fields whose value was identical in every result, e.g. companyId, companyName, sector), and `docs` = map transcriptId -> {title, documentType, date} (these three fields always depend only on the document).
  - Each following line = one result in the ORIGINAL order, holding `sentenceId`, `text` (verbatim, including its `[#N](url)` citation link), and `section` / `speakerType` only when present in the original result. The original `transcriptId` of a result = its `sentenceId` up to the last `-`; its `title`, `documentType`, `date` = `docs[transcriptId]`; plus all `constant_fields`.
  - If the original response carried `total` it is recorded in the header as `total`.
  - Reconstruction is exact: no values were altered, abbreviated or dropped.
