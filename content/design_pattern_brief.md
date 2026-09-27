# Phase 0 — Existing Web Ecosystem and the Pattern This Project Will Reuse

## What already exists

Five public sites live under `github.com/Ben-tenOever`, all served by GitHub Pages at `ben-tenoever.github.io/<repo>/`.

| Site | Repo | Character |
|---|---|---|
| Research Funding Opportunities | `grants` | Six pages, filterable proposal and fellowship data |
| Shared Equipment | `equipment` | Single page, filterable instrument directory |
| Microbiology Resources | `microbiology` | Landing page with resource cards and QR codes |
| Department podcast | `micro-podcast` | Listen and download page |
| Lab ATLAS | `tenoever-lab-atlas` | Private Next.js application, not part of the public family |

No Cloudflare project is in evidence. Everything public runs on GitHub Pages from `main` at root, with no build step. The decision for this project is GitHub Pages in a new repo, with all internal links written relative so a custom domain can be mapped later without breaking a single canonical URL.

## The design system, as measured from the live sites

The public family shares one design system, currently duplicated by copy and paste into each page's inline `<style>` block.

**Color tokens**, declared on `:root` and identical across all three sites.

```
--nyu-purple   #4F2C85     --bg-light      #f5f5f7
--nyu-deep     #2a1a49     --card-bg       #ffffff
--text-main    #222222     --border-subtle #e3e3ee
--text-soft    #56566a     --lav           #faf7ff
--amber-bg  #fdf6e3   --amber-line #e6d3a3   --amber-ink #7a5200
--red-bg    #fdeeeb   --red-line   #e6bcb1   --red-ink   #9a3520
```

**Typography** is the system stack, `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, at `line-height 1.55`. Monospace is `ui-monospace, SFMono-Regular, Menlo, monospace` and is reserved for identifiers, codes and dates. No web fonts are loaded anywhere.

**Header** is white with a 5px purple bottom rule, an NYU Langone logo at 52px that removes itself on error, and a title block separated by a hairline rule. Below 560px the logo drops to 40px and the title wraps full width.

**Navigation** is a sticky lavender bar of pill links in purple, with the current page filled solid purple and white.

**Main column** runs `max-width` 1060px to 1120px, centered, padded `2rem 2.25rem 3rem`, falling to `1.1rem 1rem 2.5rem` on narrow screens.

**Cards** are white, `border-radius .9rem`, one hairline border plus a 2px soft shadow, padded `1.3rem 1.5rem`.

**Filter chips** are pill buttons carrying `aria-pressed`, purple on white when off and solid purple when on, with a dimmed count suffix.

**Grids** use `repeat(auto-fill, minmax(300px, 1fr))` and collapse to one column at 400px.

**Stat tiles** sit on lavender with an uppercase letter-spaced label and a large purple value.

**Disclosure** uses native `details` and `summary` with a plus and minus glyph, so collapsed content is still in the DOM and still indexable.

**Accessibility** already present includes a `3px #b99be6` focus ring on every interactive element, semantic landmarks and `aria-label` on nav.

**Print styles** hide nav and filters, expand all disclosures and drop shadows.

**Data architecture** keeps content out of markup. The grants site carries `data/opportunities.json` and `data/teams.json`, the equipment site carries `equipment-data.js`, and the page renders from them at load.

**SEO today** is thin. Only the newer pages carry a meta description, only `microbiology` carries Open Graph tags, and no site has a sitemap, a canonical link or any structured data.

## What this project reuses unchanged

The color tokens, the type stack, the header treatment, the sticky pill nav, the card, the chip, the stat tile, the grid, the disclosure pattern, the focus ring, the footer, the print rules and the mobile breakpoints. A visitor moving from the grants site to this one should feel no seam.

## What this project must change, and why

**One stylesheet instead of inline duplication.** The existing sites each inline the whole system because each is one or six pages. This resource will have roughly eighty pages, one per publication plus the research, theme and index pages. Eighty copies of the same CSS is unmaintainable and wastes bandwidth. A single cached `assets/site.css` carries the identical tokens and rules.

**Real URLs instead of anchor navigation.** The existing sites navigate by `#anchor` inside one document. That cannot give a publication its own canonical URL, its own title and description, or its own structured data, all of which this project exists to provide. Every publication, research area and theme becomes a directory with an `index.html`, so the URL is clean and the trailing-slash form is canonical.

**Static generation instead of client-side rendering.** The equipment and grants pages build their card lists in JavaScript from a data file. That is fine for a directory a human scans. It is wrong here, because a search engine or a retrieval system must find the scientific text in the served HTML. A Python generator will read the knowledge base and write complete HTML to disk. The JSON data files still ship publicly for machine consumption, but nothing important depends on JavaScript to become visible. Filtering on the archive page remains client side, over content that is already in the DOM.

**A metadata layer the family currently lacks.** Per-page title and description, canonical link, Open Graph and Twitter tags, `sitemap.xml`, `robots.txt`, and Schema.org JSON-LD using `ScholarlyArticle` for papers and one consistent `Person` entity for Benjamin tenOever across every page.

**Density suited to a scholarly corpus.** The grants site is built to be skimmed. A publication page has to carry long-form prose, so the reading column narrows to roughly 72 to 78 characters while the page frame stays at the family width.

**One new accent.** The family has purple for structure and amber and red for warnings. A scholarly resource needs to mark evidence strength, distinguishing a demonstrated result from an author interpretation from a cross-paper synthesis. A muted teal, tokenised the same way as the existing amber and red triplets, carries that role without touching anything the other sites use.

## Repository proposal

A new public repo named `publications`, live at `ben-tenoever.github.io/publications/`, chosen to match the plain reusable naming already established by `grants` and `equipment`. None of the existing repos is a sensible home. The `grants` repo is about funding opportunities, `microbiology` is a departmental hub, and the ATLAS is private.

```
publications/
  index.html                     home
  research/<area>/index.html     broad research areas
  themes/<theme>/index.html      specific themes
  publications/index.html        filterable archive
  publications/<slug>/index.html one per paper, canonical
  discover/  timeline/  discoveries/
  assets/site.css  assets/nyulh-logo.png
  data/*.json                    public machine-readable corpus
  AI_CONTEXT.md  sitemap.xml  robots.txt
  build/                         generator and source knowledge base
```

Deployment follows the established workflow. Work happens in the cloud session, the repo is assembled and tested here, and the final push comes from macOS Terminal where the osxkeychain credential helper works. Published pages are verified by md5 against the locally tested build rather than by fetching the live site, because GitHub Pages serves a stale cache for several minutes after a push.

Nothing in any existing repo is modified.
