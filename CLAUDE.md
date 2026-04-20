# Grimoire — Unified Knowledge System

A book of instructions for summoning and directing entities. This repository is a personal knowledge system with two layers — **Shelves** (archival library catalog) and **Scrolls** (active research wiki) — unified behind one inbox (`desk/`), one config (`grimoire.json`), and six named operations.

## The two layers

- **Shelves** — what has been consumed. Books, films, music. Structured `catalog.json`, generated `CONTEXT_*` tiers for loading into LLM context, generated `shelves/wiki/` for browsing. Source of truth: `shelves/catalog.json`.
- **Scrolls** — what is being thought about. Daily ingested articles, living concept/entity pages, synthesis essays. Source of truth: the pages themselves under `scrolls/`.

**Flow:** material arrives in `desk/` → becomes either a shelves catalog entry or a scrolls source page → over time, scrolls pages mature into concept/entity hubs → concepts may reference shelves catalog entries; shelves entries may be cited from scrolls pages.

## The six operations

Each operation is a Claude Code skill in `.claude/skills/`. Invoke by asking the LLM to perform the operation by name.

| Operation | Purpose | Output |
|-----------|---------|--------|
| **inscribe** | Route items from `desk/` to the right pipeline | Source pages, catalog updates, moves files to `raw/processed/` or `shelves/photos/processed/` |
| **bind** | Weekly deep pass over scrolls — update concepts/entities, create hubs, flag synthesis candidates | Updated `scrolls/concepts/`, `scrolls/entities/`; candidate flags in `scrolls/log.md` |
| **consult** | Quick question the wiki can answer — lookup and correlation | Conversational reply; optional `scrolls/reports/` entry |
| **divine** | Draft a synthesis essay on request (or on a flagged candidate) | `scrolls/synthesis/<slug>.md` |
| **audit** | Integrity check — contradictions, orphans, stale claims | Report (no writes beyond typos/broken links) |
| **illuminate** | Localize remote images into `raw/assets/` and rewrite references | Updated image refs across scrolls |

## Config

Personal settings live in `grimoire.json` (gitignored). Copy `grimoire.example.json` → `grimoire.json` on fork and fill in owner details.

## Key conventions

- `shelves/catalog.json` is the source of truth for Shelves. Never hand-edit `CONTEXT_*.md` or `shelves/wiki/*.md` — they regenerate.
- `scrolls/` pages use YAML frontmatter + markdown with `[[wikilinks]]`, no inline `#tags`. Kebab-case filenames.
- Cross-layer links: scrolls → shelves use relative markdown links (e.g., `../shelves/wiki/books/<slug>.md`), not wikilinks.
- `desk/` is the only inbox. `inscribe` dispatches from there; nothing else should be dropped directly into `shelves/photos/inbox/` or `raw/` by hand.

## Operations documentation

See `docs/operations.md` for a cheat sheet of what each operation does and when to invoke it. See `docs/architecture.md` for the rationale behind the two-layer design.

## Agent permissions

This repo is read by both local Claude Code (full agent) and external agents (e.g., OpenClaw on a separate machine, via the GitHub skill). Permissions are enforced by convention here and by token scope on the external side.

**Local Claude Code (this machine):**
- `scrolls/`, `shelves/`: read + write
- `desk/`: read + write; treat as ephemeral inbox, never commit contents
- `raw/`: read only; never commit, never echo large blobs back to chat
- `grimoire.json`: read only; never commit, never paste contents into chat or external tools
- `.claude/skills/`: do not modify without an explicit request from the owner

**External agents (OpenClaw and any other remote agent):**
- Read-only access to `scrolls/**` and `shelves/**` only
- No access to `desk/`, `raw/`, `.claude/`, `grimoire.json`, `tests/fixtures/`, or any dotfile
- No write, no PR, no issue creation unless explicitly authorized per session
- Identity must be a distinct GitHub user or app with a fine-grained PAT scoped to the two paths above

## Credits

- **Shelves** is a fork of [mccoyspace/llmbrary](https://github.com/mccoyspace/llmbrary).
- **Scrolls** evolved from [Karpathy's LLM-wiki gist](https://gist.github.com/karpathy).
- **Grimoire** is the unification — inbox routing, tiered context loading between layers, split ingest/reflect/synthesis cycle — released under the same spirit: fork it, make it yours.
