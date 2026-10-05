# User brief and comparison

## Intended user and painful task

Engineers exchanging JSONL fixtures and record references. Line positions become ambiguous after byte changes; a record reference should reject stale or tampered offset manifests rather than silently selecting another value.

Current alternatives: jq/jaq filters, Toolong interactive inspection and manual line selection.

Evidence and limits: Toolong and jq docs establish JSONL/JSON inspection workflows. Content-bound record references are an inferred workflow need; no user/adoption claim. No fabricated customers, requests, adoption, testimonials or growth promise.

## Smallest useful capability and acceptance criteria

Index exact UTF-8 bytes including CRLF/no final newline, retrieve zero-based records, reject malformed/oversize/nonfinite lines and stale or tampered indexes.

Runnable acceptance fixtures are `test_jsonl_seek.py` and `demo.py`. Invalid inputs must return an explicit failure, and diagnostics must preserve source files where the contract is read-only. See README for supported subsets and bounds. Plausible discovery path: jsonl and data-integrity topics; byte-offset receipt demo, with full revalidation cost disclosed.

## Live leader research on 5 October 2026

Queries `jsonl` were requested from live GitHub sorted by stars descending. Search receipts include exact query URLs, observation times and top-ten metadata in [research-evidence.json](research-evidence.json). Irrelevant broad matches were rejected: map fonts/geospatial tools are not JavaScript source-map comparables, browser redirect extensions are not site migration analysis, and unrelated notebook/diffusion matches are not notebook hygiene tools.

Highest-star relevant comparable found among the researched set: [jqlang/jq](https://github.com/jqlang/jq) with 35745 stars. Some established comparables were added outside the narrow search query. This is bounded search coverage, not an exhaustive global ranking. Stars are a discovery signal, not a performance/reliability result.

| Comparable | Stars | Last observed push UTC | License metadata | Workflow, install, docs and tradeoff |
| --- | ---: | --- | --- | --- |
| [jqlang/jq](https://github.com/jqlang/jq) | 35745 | 2026-10-01T06:39:24Z | unresolved metadata; inspect license before reuse | Portable C JSON filter with prebuilt binaries and extensive manual/examples. Much broader transformations; our index deliberately revalidates all bytes and is not faster. |
| [01mf02/jaq](https://github.com/01mf02/jaq) | 3787 | 2026-10-02T09:46:28Z | MIT | Rust jq-style processor, documented brew/cargo install and additional formats. Broader filtering; no throughput measurements conducted. |
| [Textualize/toolong](https://github.com/Textualize/toolong) | 3951 | 2024-08-05T19:29:28Z | MIT | Python terminal log/JSONL viewer, documented pip install, search/tail/merge UI. Last observed push is 2024; maintenance and support response unverified. |

Current READMEs and the returned recent issue/PR samples were inspected. Samples may be maintainer PRs, not genuine user requests. Support channels and examples are visible; support responsiveness, actual installation reliability and time to first useful result of comparables were not measured. License metadata marked unresolved/unavailable is not a permission to reuse. No competitor code or prose is incorporated.

## Distinctness and rejected directions

Compared with all 133 owned repository names, descriptions/READMEs for overlapping tools and yesterday's five launch briefs. The five new products handle saved notebook state, planned redirect graphs, exported LFS bytes, content-bound JSONL record references, and generated-code source positions respectively. They share packaging, not one subdivided product.

Existing json-differ/log-parser/traceweave analyze different JSON or agent-trace semantics; urlnorm normalizes URLs; syncplan plans filesystem synchronization; wheel-sentinel validates Python wheel archives; portable-tree audits names. This candidate's user contract is separate. Environment checking was rejected because envdiff/env-vault/dotenv-mini already cover it; another archive checker was rejected as overlapping Wheel Sentinel.

## Fairness and limitations

Safety-first lookup revalidates the whole source, including offsets; it is O(file size) and is not a speed claim. Offset storage is O(records). No compressed files, blank lines, JSON-LD or concurrent file replacement guarantee. One MiB per line / one million records. Index creation refuses existing output files.

There is no measured competitor benchmark or superiority claim. Local examples establish our behavior only. No claim is made that a competitor lacks this capability. Broader established tools can be better choices when their workflow/dependencies fit. Evidence dates, installed behavior and untested limits remain separate.
