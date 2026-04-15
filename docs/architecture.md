# Grimoire Architecture

## Two layers, one inbox

Grimoire unifies a library catalog (**Shelves**) and a research wiki (**Scrolls**) behind a single inbox (`desk/`) and a single config (`grimoire.json`). Each layer retains its distinct shape — Shelves is structured data with generated context tiers; Scrolls is prose pages with wikilinks — but the entry point is unified.

## Why unify?

Two independent systems force the user to think about routing: "is this a book I shelved or a concept I'm working on?" That's the LLM's job, not the user's. One inbox, `inscribe` classifies.

## The operation split

| Stage | Operation | What it does |
|---|---|---|
| Light pass (daily) | `inscribe` | Classify desk/ items, create source pages, move photos |
| Deep pass (weekly) | `bind` | Update concepts/entities, flag synthesis candidates |
| On demand | `consult` | Answer a question from the wiki |
| On demand | `divine` | Draft a synthesis essay |
| Maintenance | `audit` | Integrity check |
| Maintenance | `illuminate` | Localize remote images |

The deliberate split of `bind` (flag) and `divine` (draft) keeps each operation single-purpose. A weekly review that also drafts synthesis tends to over-draft; a synthesis writer that also does reflection tends to under-invest in either.

## Tiered context loading

Shelves exports three context tiers:
- `CONTEXT_OVERVIEW.md` — ~500 tokens, always-loadable
- `CONTEXT_COMPACT.md` — ~5K tokens, loaded for general work
- `CONTEXT.md` — ~40K tokens, loaded only when a question demands the full library

Scrolls skills load the smallest tier that serves the task. `inscribe` uses overview. `bind` uses compact. `divine` may load full for synthesis drafts that span the library.

## Data flow

```
desk/ (inbox)
  │
  ▼
inscribe ──── shelves-image ────► shelves/photos/inbox/   (then: import scripts)
  │
  ├──── shelves-list ─────► (user runs) shelves/scripts/import_text.py
  │
  └──── scroll-source ────► scrolls/sources/<slug>.md
                                │
                                ▼
                              bind (weekly)
                                │
                     ┌──────────┴──────────┐
                     ▼                     ▼
              scrolls/concepts/      scrolls/log.md
              scrolls/entities/      (synthesis candidates)
                                          │
                                          ▼
                                      divine (on demand)
                                          │
                                          ▼
                                scrolls/synthesis/<slug>.md
```
