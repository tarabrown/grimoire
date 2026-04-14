---
name: bind
description: Use when the user asks for a weekly review, reflection, or deep pass — updates concept and entity pages with material inscribed since the last bind, creates hubs when warranted, runs the batched Shelves cross-check, and flags synthesis candidates for the user to draft with divine.
---

# bind — Stage 2 deep pass

> This skill is written from the CLAUDE.md spec, not from a real run. After the first real bind, rewrite this skill from what actually happened (per Isenberg: agents write better skills from real history than from theory).

Binding is where the heavy work happens. Inscribe only creates source pages and flags potential overlaps — it never touches concept or entity pages. Bind does ALL of that: reading concept pages, updating them with new source material, creating new hubs, promoting entities. This is where the wiki's graph actually deepens. Synthesis drafting is *not* part of bind — it lives in `divine`, invoked separately by the user.

## First-run note

Early ingests may have been done before the inscribe/bind split was enforced. They could have created concept pages, built deep cross-references, added Shelves library sections, and written multi-paragraph concept updates. The first bind pass is therefore a **reconciliation**, not a fresh build. Scan what exists, identify gaps or stale connections left by the old process, and focus new work on sources inscribed after the lean inscribe process took effect. Don't redo work that's already done.

## Scoping

Bind processes material since the last `bind` entry in the log. If the log has grown large, scan only from that marker forward — older material was handled by a previous bind (or by pre-split ingests on the first run).

**Per-session budget:** Propose a scope to the user at the start — e.g., "5 new sources to process, 3 concept pages to update, 2 entity promotions to consider." Get alignment before doing the work. This prevents runaway sessions.

## Steps

### 1. Scan the log
Read `scrolls/log.md` from the last `bind` entry forward. Identify:
- Every source inscribed since then.
- Every **Potential overlaps** list from those inscribe entries — these are the pointers inscribe left showing which sources connect to which existing pages. (Older entries may use **Candidates for Reflect** instead — same purpose, different label. Check for both.)
- Any **Shelves: neighborhood** lines queued for the batched Shelves pass in step 5.

### 2. Read the new material
Read every source page created since the last bind. Read the concept/entity pages flagged in the inscribe overlap lists. This is where you do the reading that inscribe deliberately skips.

### 3. Look for real overlaps
Four categories of move, in roughly this order of weight:

- **Concept/entity page updates.** This is where ALL concept and entity page editing happens — adding sources to frontmatter, writing new body content, adding See Also links, restructuring sections. Inscribe does not touch these pages; bind does all of it.
- **Concept hub candidates.** Multiple (4+) recent sources touching the same theme that isn't yet a concept page. Create the page.
- **Entity promotions.** Stubs or inline mentions that have crossed the multi-source threshold and now deserve real entity pages.
- **Orphans and non-obvious connections.** Pages linked from nothing; overlaps between older and recent material that inscribe missed.

### 4. Propose before doing (for substantial work)
For new concept pages or large restructurings: **propose to the user first**. For smaller cleanups (orphan hookups, cross-reference fixes, stub promotions from clearly-earned material), just do them.

### 5. Batched Shelves cross-check
Walk the queued **Shelves neighborhood** flags from step 1 and any newly created or substantially updated pages from this bind.

**Tier choice — default to the smallest tier that answers the question:**
- `shelves/CONTEXT_OVERVIEW.md` (smallest) — confirm or deny a neighborhood call.
- `shelves/CONTEXT_COMPACT.md` (mid) — **workhorse tier for bind.**
- `shelves/CONTEXT.md` (largest) — full synopses. Load once for the whole batch, not per page. Check file size first — grows as catalog grows.

**For each hit:** grep for author names (fuzzy/last-name OK), check topic slugs in `../shelves/wiki/`, and add or update `## In the library` on the Scrolls page with relative-path links. Match depth to hit count — thin hits get a note, not a full section on every page.

**Scope:** entity and concept pages by default. Skip source pages. **Direction:** Scrolls reads Shelves; never write to Shelves.

### 6. Update `scrolls/index.md`
Reflect any new pages and structural cleanup.

### 7. Append a bind entry to `scrolls/log.md`
Header: `## [YYYY-MM-DD] bind | <brief description>`

Body: bulleted list — what was updated, promoted, restructured, which Shelves connections were added, and any candidates *rejected* (with one-line reason). **Keep the entry concise** — same spirit as inscribe's 20-line limit, though bind entries can be longer since they cover more work. Aim for under 40 lines.

## Synthesis candidates (flag, don't write)

During the pass, watch for material that deserves a synthesis essay — a cross-cutting pattern, a convergence across sources, a thematic through-line. Do NOT draft. Instead, append a flag to `scrolls/log.md`:

```markdown
## YYYY-MM-DD bind

### Synthesis candidates

- **<working title>** — <2-3 sentence rationale>. Related pages: [[concept-a]], [[entity-b]], [[source-c]].
```

The user invokes `divine` separately to pick up a candidate and write the essay.

### 8. Archive old log entries
If `scrolls/log.md` exceeds ~200 lines after appending the new entry, move everything older than this bind entry to `scrolls/log-archive.md` (create if needed, append at top). The working log should only contain the most recent bind and any inscribes since.
