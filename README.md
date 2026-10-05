# jsonl-seek

Verified JSONL byte indexes with strict parsing and stale or tampered offset rejection.

## Install and first useful result

```bash
git clone https://github.com/nripankadas07/jsonl-seek
cd jsonl-seek
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python demo.py
.venv/bin/jsonl-seek --help
```

Python 3.10 or newer. The example creates synthetic inputs; it needs no account, service, token or downloaded dataset. Runtime uses only the standard library. Building requires setuptools from the package registry. POSIX commands above; Windows/macOS installation has not been tested.

## Useful contract

Index exact UTF-8 bytes including CRLF/no final newline, retrieve zero-based records, reject malformed/oversize/nonfinite lines and stale or tampered indexes.

Import `jsonl_seek` for the function used by `demo.py`, or use the installed CLI described by `--help`. JSON reports print to stdout. Exit 0 means the documented success condition, 1 means diagnostic findings or an unmapped source position where applicable, and 2 means invalid input or I/O failure. JSONL indexing uses 0/2 only; LFS returns 2 when no pointers were found.

## Limits

Safety-first lookup revalidates the whole source, including offsets; it is O(file size) and is not a speed claim. Offset storage is O(records). No compressed files, blank lines, JSON-LD or concurrent file replacement guarantee. One MiB per line / one million records. Index creation refuses existing output files.

No performance or superiority claim. Demand is inferred. See [research and acceptance criteria](RESEARCH.md), [validation](VALIDATION.md) and [support and security](SUPPORT.md). MIT license; implementation and synthetic fixtures are original. Comparables inform scope; no competitor code or prose is incorporated.

## Development

```bash
python -m unittest -v
python -m compileall -q jsonl_seek.py
python demo.py
```

## CLI input

`jsonl-seek index data.jsonl data.index.json` creates a new index and refuses an existing output path. `jsonl-seek get data.jsonl data.index.json 0` returns the first record after full revalidation. Floats outside Python's finite float range are rejected; ordinary floats use Python floating-point precision. This is not an exact-decimal data tool. Strict UTF-8; no BOM or blank lines.
