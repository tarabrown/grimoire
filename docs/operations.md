# Operations Cheat Sheet

| Op | Trigger phrases | Reads | Writes | Runs when |
|---|---|---|---|---|
| **inscribe** | "process desk", "ingest this", "what's new" | `desk/`, `scrolls/index.md`, `shelves/CONTEXT_OVERVIEW.md` | `scrolls/sources/*`, moves to `shelves/photos/inbox/` or `raw/processed/`, `scrolls/log.md` | Whenever desk/ has items |
| **bind** | "weekly review", "reflect", "deep pass" | all new `scrolls/sources/*`, existing `concepts/` & `entities/`, `shelves/CONTEXT_COMPACT.md` | `scrolls/concepts/*`, `scrolls/entities/*`, `scrolls/log.md` (synthesis candidates) | Weekly, or when a batch of sources has accumulated |
| **consult** | "what do I have about X", "does my wiki say Y" | `scrolls/index.md`, relevant pages, optionally `shelves/CONTEXT_*` | optional `scrolls/reports/<slug>.md` | Any substantive question |
| **divine** | "draft a synthesis on X", "pick up the candidate from Apr 14" | named pages or candidates from `scrolls/log.md`, optionally `shelves/CONTEXT_*` | `scrolls/synthesis/<slug>.md`, `scrolls/log.md` | On demand only |
| **audit** | "lint the wiki", "audit", "check integrity" | all of `scrolls/` | report; minor typo/link fixes only | Periodic, or before publishing |
| **illuminate** | "localize images", "pull images local" | all `scrolls/` pages with remote image refs | `raw/assets/<file>`, in-place rewrites of image refs | Monthly |

## When in doubt

- A new article or note → inscribe
- A pattern you've noticed across material → flag it or ask bind to
- A question → consult
- An essay idea → divine (propose first)
- Something feels wrong → audit
- Tweet embeds going dead → illuminate
