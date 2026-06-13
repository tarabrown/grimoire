# Apple Notes PARA Import

Use this when importing Apple Notes without losing PARA. The import is a preservation pass first, then a small-batch `inscribe` translation pass.

## Staging Shape

Import exported Apple Notes into `desk/apple-notes-import/` while preserving the original PARA folder:

```text
desk/apple-notes-import/
  1-projects/
  2-areas/
  3-resources/
  4-archives/
```

Actual imported notes stay untracked because `desk/` is an inbox. The tracked `.gitkeep` files only preserve the staging scaffold.

## Required Frontmatter

Every imported note should keep its Apple Notes origin and PARA meaning:

```yaml
---
source_app: apple_notes
source_folder: "1 Projects/Sit Spot Club"
para: project
status: staged
imported_at: 2026-06-12
---
```

Allowed `para` values are `project`, `area`, `resource`, and `archive`.

Keep `source_folder` as the original human-readable Apple Notes path, even after the note moves into `scrolls/`, `shelves/`, or `raw/`.

## Translation Rules

- Projects: active work notes. Route through `inscribe` into `scrolls/sources/`, `scrolls/concepts/`, or project-specific pages.
- Areas: ongoing responsibilities. Usually become durable pages in `scrolls/concepts/` or `scrolls/entities/`.
- Resources: reference material. Usually become `scrolls/sources/`, `shelves/` catalog material, or `raw/` attachments.
- Archives: historical context. Keep recoverable but out of default working context, usually under `raw/archive/` or a clearly marked archive page.

## Safe Import Rhythm

1. Preserve pass: export/import notes into the matching staging folder without cleanup.
2. Metadata pass: add or normalize the required frontmatter.
3. Sample pass: process one note from each PARA bucket and verify `source_folder` and `para` survive.
4. Batch pass: repeat in small batches with `inscribe`.

Do not deduplicate, delete, archive-clean, or bulk-rehome during the initial import.
