# Design: Description Field + Provenance Log

**Date:** 2026-04-15
**Status:** Approved
**Inspiration:** Jibot/Switchboard architecture — `description` frontmatter for filter-before-read, append-only provenance log for chain-of-custody.

## Problem

1. **consult** reads full page content to determine relevance, burning tokens on pages that turn out to be irrelevant.
2. There is no structured record of what entered the wiki, from where, and what happened to it. The narrative log captures rationale well but is expensive to parse programmatically.

## Changes

### 1. Description field in frontmatter

Add `description:` (one sentence, ~120 chars max) to every page's YAML frontmatter.

**Field format:**
```yaml
description: "One-sentence summary useful for filtering without reading the full page"
```

**Rollout — no bulk migration:**
- **inscribe** adds `description` when creating source pages. Zero extra cost — it already summarizes the material.
- **bind** adds `description` when creating or updating concept/entity pages. No extra reads — it already touches these pages.
- Pages without the field continue to work. consult falls back to reading the full page.

### 2. Provenance log

**New file:** `scrolls/provenance.md`

Append-only structured table. One row per item entering the wiki.

```markdown
| date | item | origin | type | disposition | page |
|------|------|--------|------|-------------|------|
```

- **date** — ISO date (YYYY-MM-DD)
- **item** — original filename as it arrived in desk/
- **origin** — always `desk` for now (future-proofs for other inboxes)
- **type** — classification: `scroll-source`, `shelves-image`, `shelves-list`, `asset`
- **disposition** — what happened: `created`, `promoted`, `moved`
- **page** — wikilink to resulting page, or path for assets

**inscribe** appends rows after dispatching each item. **log.md** stays unchanged for narrative context that bind depends on.

### 3. Consult frontmatter-first filtering

New step between reading the index and reading full pages:

1. Read index, identify candidate pages (as today).
2. **New:** Read only the YAML frontmatter block of each candidate (first `---` to second `---`). Filter to pages whose `description` + `title` + `tags` match the query.
3. Read full content only for filtered matches.
4. For pages missing `description`, fall back to reading full content (graceful degradation).

## Skill changes

| Skill | Change |
|-------|--------|
| inscribe | Add `description:` to source page template; append row to `scrolls/provenance.md` after each dispatch |
| bind | Add `description:` when creating/updating concept/entity pages |
| consult | Add frontmatter-first filtering step; graceful fallback for pages without description |

## What doesn't change

- inscribe/bind separation and boundary rules
- log.md format, content, and bind's use of it
- Existing frontmatter fields (title, type, created, updated, sources, tags)
- Any other skill (divine, audit, illuminate)
