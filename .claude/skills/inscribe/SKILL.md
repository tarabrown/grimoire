---
name: inscribe
description: Use when the user asks to process the desk, ingest material, or words to that effect — classifies each item in desk/ and dispatches to the Shelves pipeline (catalog items) or the Scrolls pipeline (everything else). The only inbox entry point in Grimoire.
---

# Inscribe — the router

> Rewritten from real run (2026-04-15): 3 items — 2 scroll-sources (Salvaggio full body, Yuk Hui metadata-only clip) + 1 already-processed asset (AMI screenshot promoted to raw/assets/).

One desk, two pipelines. Inscribe classifies each item dropped into `desk/` and sends it where it belongs.

## When to invoke

Any of: "inscribe", "process the desk", "ingest this", "what's in my inbox", "run ingest". Also proactively if the user mentions dropping something new and `desk/` has contents.

## Classification rules

Look at each file in `desk/` (excluding `.gitkeep`) and classify:

1. **Shelves-image** — a photograph of a bookshelf spine, a record stack, a DVD case, or similar physical media. File extensions `.jpg`, `.jpeg`, `.heic`, `.png` are candidates. **Confirm by looking at the image** — not all PNGs are shelf photos. In the real run, a `.png` turned out to be a screenshot of an awards table, not physical media.
2. **Shelves-list** — a plain text or markdown file that is *primarily* a list of media titles (books, films, albums).
3. **Scroll-source** — everything else. Articles, clipped web pages, personal notes, essays, transcripts, research memos.
4. **Already-processed asset** — an image or file that belongs to an existing source page (e.g., a screenshot that was already transcribed into a source). Not a new source — promote to `raw/assets/` with a meaningful filename and update the existing source page's reference.

When uncertain between shelves-list and scroll-source, ask the user once.

## Dispatch

**For each shelves-image:**
- Move to `shelves/photos/inbox/`
- Report: "image moved to shelves inbox, ready for extraction"
- Do NOT run extraction automatically.

**For each shelves-list:**
- Leave in place, tell user which script: `python3 shelves/scripts/import_text.py desk/<filename>` (books) or `python3 shelves/scripts/import_media.py desk/<filename>` (films/music). Let the user decide.

**For each scroll-source:**
- Create a source page at `scrolls/sources/<kebab-slug>.md` with YAML frontmatter + markdown body.
- Move the original from `desk/` to `raw/processed/`.
- Flag overlaps with existing concept/entity pages but do NOT edit them — that's `bind`'s job.

**For each already-processed asset:**
- Move to `raw/assets/<descriptive-name>.<ext>` (use the related source page's slug).
- Update the existing source page's asset reference.
- Do NOT create a new source page.

## Source page structure

From the real run, a full-body source page includes:

```markdown
---
title: "<Title — Author (Year)>"
type: source
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "<original filename in desk>"
tags:
  - <topic tags>
---

# <Title — Author (Year)>

**Author:** ...
**Venue/Publication:** ...
**Source:** [url](url)

## Summary
<2-4 paragraph summary of the argument>

## <Core sections>
<Key claims, frameworks, or findings — use ### subheads>

## Where this lands in the wiki
<How it connects to existing concept/entity pages. Use [[wikilinks]]>

## Potential overlaps flagged for bind
<Entity/concept candidates, hub candidates, stance groupings>

## See also
<[[wikilinks]] to related pages>
```

### Metadata-only clips

When the web-clipper captures only title/URL/description (no body text), still create a source page but:
- Note prominently that body text is missing ("**Note:** metadata + footnotes only — needs re-clip")
- Infer what you can from available metadata/citations
- Flag for re-clip in the log entry

In the real run, the Yuk Hui piece arrived with footnotes but no essay body. The footnote apparatus was enough to sketch the argument's territory and flag useful connections.

## Boundary

Inscribe does NOT:
- Update concept/entity pages (that's `bind`)
- Draft synthesis (that's `divine`)
- Download remote images (that's `illuminate`)
- Run integrity checks (that's `audit`)

## After a run

Update `scrolls/index.md` with new source entries.

Append an entry to `scrolls/log.md`:

```
## YYYY-MM-DD inscribe — <summary>
```

The log entry should capture:
- Count + breakdown by classification
- Source pages created (with one-line descriptions)
- Asset promotions (what, where, why)
- Overlaps flagged for bind (bulleted list of concept/entity connections)
- Entity candidates held (with source count and hold rationale)
- Shelves neighborhood flags (deferred to bind)
- Files moved (desk → raw/processed, desk → raw/assets)
