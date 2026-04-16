---
name: consult
description: Use when the user asks a substantive question the wiki should be the primary source for — reads the index, pulls relevant pages, synthesizes an answer with wikilinks back to sources, and offers to save reusable answers as reports.
---

# consult

> Rewritten from real run (2026-04-15): "what do I have about CryptoPunks?" — pulled entity + concept + verified cross-layer links.

## Steps

### 1. Start from the index
Read `scrolls/index.md`. Scan for pages relevant to the question — entity pages, concept pages, and source pages that match the topic. The index is organized by category (Art > Digital Art, Art > NFT Provenance, Entities, Concepts, Sources, Synthesis) — use the structure to narrow quickly.

### 2. Read the hub page(s)
Read the most relevant entity or concept page in full. These are the load-bearing pages — they aggregate multiple sources and carry cross-references to both Scrolls pages (via `[[wikilinks]]`) and Shelves catalog entries (via `../../shelves/wiki/books/<slug>.md` relative links).

### 3. Follow one hop where load-bearing
If the hub page's `## See also` or body links reference a concept or entity that looks essential to the answer, read that page too. In the real run, `[[cryptopunks]]` (entity) led to `[[nft-provenance-and-value]]` (concept) — the concept page carried additional framing the entity didn't duplicate.

One hop is usually enough. Don't spider the whole wiki.

### 4. Verify cross-layer links
If the answer cites Shelves books via `../../shelves/wiki/books/` paths, spot-check that the targets exist (`ls shelves/wiki/books/ | grep <slug>`). Broken cross-layer links undermine the answer's credibility.

### 5. Synthesize the answer
Structure the answer around what the wiki actually contains:
- **Hub summary** — what the entity/concept page says
- **Source inventory** — list the source pages with dates and one-line descriptions, using `[[wikilinks]]`
- **Shelves cross-layer** — any books in the library that connect, with resolution status
- **Gaps** — what the wiki doesn't cover yet, if relevant to the question

Use `[[wikilinks]]` throughout so the user can click through in Obsidian. Cite specific source filenames where a claim depends on a single source.

### 6. Flag uncertainty
If two sources conflict, say so. If the answer rests on a single source, say so. If a source page is metadata-only (clipper captured no body text), note that limitation. Don't fill gaps with plausible-sounding content.

### 7. Offer to save (only if substantive)
If the answer is genuinely reusable — not a one-off lookup — offer to save as `scrolls/reports/<slug>.md`. Reports are Q&A outputs, distinct from `scrolls/synthesis/` (cross-cutting essays drafted by `divine`). Most consult answers stay in the conversation and don't need saving.

## Logging

Consult logs only when it produces a report under `scrolls/reports/`. Plain Q&A answers in the conversation are not logged.

When a report is saved, append an entry to `scrolls/log.md`:

```
## YYYY-MM-DD consult — report <slug> created
```

Body: the question asked, and a one-line summary of the answer.
