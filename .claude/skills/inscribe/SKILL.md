---
name: inscribe
description: Use when the user asks to process the desk, ingest material, or words to that effect — classifies each item in desk/ and dispatches to the Shelves pipeline (catalog items) or the Scrolls pipeline (everything else). The only inbox entry point in Grimoire.
---

# Inscribe — the router

One desk, two pipelines. Inscribe classifies each item dropped into `desk/` and sends it where it belongs.

## When to invoke

Any of: "inscribe", "process the desk", "ingest this", "what's in my inbox", "run ingest". Also proactively if the user mentions dropping something new and `desk/` has contents.

## Classification rules

Look at each file in `desk/` (excluding `.gitkeep`) and classify:

1. **Shelves-image** — a photograph of a bookshelf spine, a record stack, a DVD case, or similar physical media. File extensions in `grimoire.json → inscribe.shelves_image_extensions` (default `.jpg`, `.jpeg`, `.heic`, `.png`) are candidates. Confirm by looking at the image: if it shows physical media with titles visible, it's shelves-image.
2. **Shelves-list** — a plain text file or markdown document that is *primarily* a list of media titles (books, films, albums). Heuristics: each line looks like a title (possibly with author/year), density of known media names, or filename/content matching patterns in `grimoire.json → inscribe.shelves_text_patterns`.
3. **Scroll-source** — everything else. Articles, clipped web pages, personal notes, essays, transcripts, research memos.

When uncertain between shelves-list and scroll-source, ask the user once, then remember the answer for similar-looking items in this run.

## Dispatch

**For each shelves-image:**
- Move to `shelves/photos/inbox/`
- Report to user: "image moved to shelves inbox, ready for extraction"
- Do NOT run the extraction pipeline automatically — spine extraction is vision-heavy and should be a deliberate step.

**For each shelves-list:**
- Leave the file in place and tell the user which script to run: `python3 shelves/scripts/import_text.py desk/<filename>` (books) or `python3 shelves/scripts/import_media.py desk/<filename>` (films/music). Let the user decide which — don't guess.

**For each scroll-source:**
- Create a source page at `scrolls/sources/<kebab-slug>.md` following the CLAUDE.md page format (YAML frontmatter + markdown body with wikilinks).
- After the source page is written, move the original from `desk/` to `raw/processed/`.
- Scan the new source page for entity/concept names that already exist in `scrolls/concepts/` or `scrolls/entities/`. Flag overlaps to the user but do NOT edit concept/entity pages — that's `bind`'s job.

## Boundary

Inscribe does the Stage 1 light pass. It does NOT:
- Draft synthesis (that's `divine`)
- Update concept/entity pages (that's `bind`)
- Download remote images (that's `illuminate`)
- Run integrity checks (that's `audit`)

## After a run

Write a one-line entry to `scrolls/log.md` under a dated `## YYYY-MM-DD inscribe` section summarizing: count of items processed, breakdown by classification, overlaps flagged.
