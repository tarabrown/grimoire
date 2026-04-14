---
name: divine
description: Use when the user asks for a synthesis, deeper analysis, or picks up a candidate flagged by bind — drafts a synthesis essay under scrolls/synthesis/ that connects concepts, entities, and sources into a single cross-cutting argument. Propose-before-doing.
---

# Divine — synthesis on request

Divine writes synthesis essays. It is the only operation that drafts pages under `scrolls/synthesis/`. It runs on demand, never automatically.

## When to invoke

- User asks: "draft a synthesis on X", "write up the pattern between Y and Z", "can you divine a synthesis from the Apr 14 bind candidates".
- Bind flagged a candidate and the user wants to act on it.

## Inputs

1. A topic, working title, or candidate flag reference.
2. The concept/entity/source pages the synthesis should draw from (either specified by the user or identified by divine from the wiki index).
3. Shelves context via `shelves/CONTEXT_COMPACT.md` (loaded lazily, only if the topic plausibly touches the library).

## Procedure

### 1. Propose first

Before drafting, tell the user:
- The working title
- The 3–8 pages you plan to pull from
- A one-paragraph sketch of the argument shape
- Whether you'll load Shelves context (and which tier)

Wait for approval. If the user redirects, adjust and re-propose. Synthesis drafts are the most expensive operation; propose-before-doing is non-negotiable.

### 2. Draft

Write to `scrolls/synthesis/<kebab-slug>.md`:

```markdown
---
title: <full title>
created: YYYY-MM-DD
kind: synthesis
drawn_from:
  - concepts/<name>
  - entities/<name>
  - sources/<name>
tags: []
---

# <title>

<body with [[wikilinks]] into the drawn_from pages, relative markdown links to ../shelves/wiki/books/<slug>.md where Shelves is cited>

## What this synthesis does NOT claim

<brief honesty section: limits of the argument, what it doesn't address, what would falsify it>

## See also

- [[page-a]]
- [[page-b]]
```

### 3. Log

Append to `scrolls/log.md` under a dated `## YYYY-MM-DD divine` section: the title, the drawn-from list, a one-line summary.

## Boundary

Divine does NOT:
- Update concept/entity pages (that's `bind`)
- Answer quick questions (that's `consult`)
- Invent sources. Every citation must correspond to a real page in scrolls or a real catalog entry in shelves.

## Tone

Synthesis essays should read like a serious argument, not like a summary. Include disagreements and tensions within the drawn-from material, not just agreements. The user's `intellectual_profile` from `grimoire.json` is the frame — match it.
