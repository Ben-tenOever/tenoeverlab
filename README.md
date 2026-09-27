# tenOever Laboratory scholarly website

Canonical public origin: **https://tenoeverlab.us**

A statically rendered scholarly resource built from the reviewed tenOever knowledge base: 63 publication records, six research areas, 34 themes, 14 discoveries, and 129 documented publication relationships. The curated corpus covers 2003–2025; it is not a complete or continuously updated bibliography.

## Build and preview

Python 3.11 or newer:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/validate.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Open http://127.0.0.1:8765 locally. Production HTML always uses the canonical public domain.

`content/` and `data/` are reviewed source material. `assets/` contains the shared stylesheet and progressively enhanced publication search. `scripts/build.py` generates **all of `docs/`**. Do not edit generated files directly: rebuilding replaces that directory. Source Markdown is preserved in full, including attribution, limitations, revisions, and source mappings. The supplied archive and root source copies are retained locally; the archive is excluded from Git because its extracted contents are tracked.

## Validation

The static validator checks every internal link and fragment, page headings, canonical origins, JSON-LD, all JSON data, sitemap coverage, robots.txt, CNAME, and publication completeness.

Optional browser checks use Playwright and the local Google Chrome installation:

```sh
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/browser_check.py
```

The local server must be running. Checks cover desktop and mobile widths, search/filter/reset behavior, URL state, and reading without JavaScript. `scripts/check_pdfs.py` performs read-only checks of the supplied external PDF URLs. Reports are under `reports/`.

## Deployment

Repository: https://github.com/Ben-tenOever/tenoeverlab

GitHub Pages serves `main:/docs`. All HTML is committed; there is no runtime application, database, client rendering dependency, or third-party font. `docs/.nojekyll` bypasses Jekyll and `docs/CNAME` declares `tenoeverlab.us`. The validation workflow rebuilds and checks that committed generated output is current. Publication identifiers and custom domain must remain stable.

## Editorial maintenance

Add or revise reviewed source records first, preserve attribution, then regenerate and validate. Keep original machine-readable inputs in `data/`; public enriched exports are generated into `docs/data/`. Do not infer authorship, external identifiers, PDFs, or scientific lineage from topic similarity. Cross-paper synthesis remains separate from individual experimental findings. Existing source PDFs were not included and publisher PDFs are not redistributed.

The institutional profile is an additional authoritative source for the About page only: https://med.nyu.edu/faculty/benjamin-tenoever (checked 2026-09-26). No source content license or publisher redistribution rights are implied.
