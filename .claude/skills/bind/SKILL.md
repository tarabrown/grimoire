---
name: bind
description: Use when the user asks for a weekly review, reflection, or deep pass — updates concept and entity pages with material inscribed since the last bind, creates hubs when warranted, runs the batched Shelves cross-check, and flags synthesis candidates for the user to draft with divine.
---

# bind — Stage 2 deep pass

> Rewritten from real run (2026-04-15): reconciliation pass over 5 pre-split sources. Promoted Hertzmann entity, batched Shelves cross-check (no new hits), rejected 4 candidates with rationale, flagged 1 synthesis candidate, archived log.

Bind is where the wiki's graph deepens. Inscribe only creates source pages and flags overlaps — it never touches concept or entity pages. Bind does ALL of that: reading concept pages, updating them with new material, creating hubs, promoting entities. Synthesis drafting is NOT part of bind — it lives in `divine`.

## Reconciliation mode

If the last log entries are pre-split ingests (labeled "ingest" rather than "inscribe") that already updated concept pages, this bind is a **reconciliation**, not a fresh build. Focus on the "Candidates for Reflect" (or "Potential overlaps") list at the bottom of those entries rather than re-reading all sources and redoing concept work.

## Steps

### 1. Scan the log
Read `scrolls/log.md` from the last `bind` entry forward. Identify:
- Every source inscribed since then (check for both "inscribe" and older "ingest" labels).
- Every **Potential overlaps** / **Candidates for Reflect** list — these are the pointers inscribe left.
- Any **Shelves: neighborhood** lines queued for the batched cross-check.

### 2. Read the new material
Read every source page created since the last bind. Read the concept/entity pages flagged in the overlap lists. This is where the reading happens that inscribe deliberately skips.

### 3. Propose scope to the user
Before doing work, propose a budget: "N sources to process, N concept pages to update, N entity promotions to consider, N rejections." Get alignment. This prevents runaway sessions.

In the real run, the proposal was: "1 entity promotion (Hertzmann, 2 sources — threshold met), 1 batched Shelves cross-check, 4 rejections (Casey Reas, Art Blocks, two concept hubs — thresholds not met)." User said "sure, whatever is needed."

### 4. Execute the work
Four categories, roughly in order of weight:

- **Concept/entity page updates.** Add sources to frontmatter, write new body sections, add See Also links. Add a `description:` field to frontmatter if missing (one sentence, ~120 chars, summarizing what the page is about — enables cheap filtering by consult). In the real run: added `[[aaron-hertzmann]]` to See Also on 3 concept pages (autonomous-ai-artists, technology-disruption-in-art, generative-art).
- **Entity promotions.** Multi-source threshold (2+ substantive sources citing the same figure). Include `description:` in frontmatter when creating new entity pages. In the real run: created `scrolls/entities/aaron-hertzmann.md` — two sources (Gotlieb Lecture + Le Random interview).
- **Concept hub candidates.** 4+ recent sources touching the same theme without a concept page. Create the page. Propose first for substantial new pages.
- **Orphans and non-obvious connections.** Pages linked from nothing; cross-refs that inscribe missed.

### 5. Batched Shelves cross-check
Walk the queued Shelves neighborhood flags and any newly created/updated pages.

**Tier choice:** Check file sizes first, then pick the smallest tier that answers the question:
- `shelves/CONTEXT_OVERVIEW.md` — confirm/deny a neighborhood call
- `shelves/CONTEXT_COMPACT.md` — workhorse tier
- `shelves/CONTEXT.md` — full synopses; grep once for the whole batch

In the real run: checked COMPACT size (475 lines), then grepped full CONTEXT.md for a batch of 10 entity/author names. Result: no new biographical hits beyond the topical cluster already cited on relevant pages. Conclusion recorded in the log entry.

**For each hit:** add or update `## In the library` on the Scrolls page with relative-path links (`../../shelves/wiki/books/<slug>.md`). Match depth to hit count.

**Scope:** entity and concept pages by default. Skip source pages. **Direction:** Scrolls reads Shelves; never write to Shelves.

### 6. Record rejections
Explicitly log candidates considered and rejected, with one-line reasons. This prevents re-evaluating the same candidates next bind. In the real run: 4 rejections (Casey Reas — two thin mentions; Art Blocks — single source; two concept hubs — single source each).

### 7. Update `scrolls/index.md`
Add any new pages. Update the `updated:` date in frontmatter.

### 8. Append a bind entry to `scrolls/log.md`
Canonical header format:

```
## YYYY-MM-DD bind — <brief description>
```

Body sections:
- **Promoted:** what was created/updated
- **Shelves cross-check:** method, results, conclusion
- **Rejected:** candidates not acted on, with reasons
- **Still open:** items punted (e.g., re-clip needed)
- **Synthesis candidates** (sub-section): cross-cutting patterns noticed during the pass. Format:

```markdown
### Synthesis candidates

- **<working title>** — <2-3 sentence rationale>. Related pages: [[concept-a]], [[entity-b]], [[source-c]].
```

Aim for under 40 lines total.

### 9. Archive old log entries
If `scrolls/log.md` exceeds ~200 lines after appending, move everything older than this bind entry to `scrolls/log-archive.md` (create if needed, append at top with frontmatter). The working log should only contain the most recent bind and any inscribes since.
