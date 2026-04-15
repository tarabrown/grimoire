![Grimoire](grimoire.jpg)

# Grimoire

A personal knowledge system with two layers: a **library catalog** of things you've consumed (books, films, music) and a **research wiki** of things you're thinking about. Unified behind one inbox and six named operations.

> A book of instructions for summoning and directing entities. Which, if you squint, is what any knowledge system is — and more specifically, it is what this one is: instructions an LLM follows to route your material into the right place and help you think through it.

## Why two layers?

The library tells you what you've read; the wiki tells you what you're working through. Neither is complete on its own. The useful part is their intersection — when a concept you're drafting in the wiki resonates with a book you shelved three years ago, or when a pattern in your reading history suggests a synthesis you hadn't named yet. Grimoire makes that intersection cheap.

## The six operations

| Operation | You ask | It does |
|---|---|---|
| **inscribe** | "process my desk" / "ingest this" | Routes each item in `desk/` to the right pipeline |
| **bind** | "let's do a weekly review" | Deep pass over recent scrolls, updates concepts, flags synthesis candidates |
| **consult** | "what do I have about X?" | Answers from the wiki with citations |
| **divine** | "draft a synthesis on X" | Writes a synthesis essay |
| **audit** | "lint the wiki" | Surfaces contradictions, orphans, stale claims |
| **illuminate** | "localize images" | Downloads remote images, rewrites refs |

## How to use your Grimoire

Grimoire is conversational — every operation is you asking an LLM to run it. The files are plain markdown, so [Obsidian](https://obsidian.md) works well as the reading and editing layer — point a vault at your grimoire folder and you get scrolls and shelves with backlinks, graph view, and search. The [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension sends articles straight into `desk/`, ready for the next inscribe pass.

A typical rhythm:

**Daily-ish:** drop new material (articles, bookshelf photos, notes) into `desk/`. When it's time to process, ask your LLM:

> "Inscribe the desk."

Inscribe classifies each item and routes it: book/record/film photos to the Shelves import pipeline, clipped articles and other prose to a new Scrolls source page, anything else into the scroll-source bucket. Nothing sits stale.

**Importing a whole shelf at once:** take a photo of your bookshelf, film shelf, or record stack and drop it in `desk/`. Inscribe moves it to the Shelves photo inbox; ask for the extraction pass and vision reads every visible spine, creating a catalog entry for each — title, author (or director, or artist), year, themes, a short synopsis. Hundreds of books in minutes, no typing.

**Any time a question comes up:**

> "Consult: what do I have about X?"

You get an answer synthesized from your wiki, with links back to the source pages and any relevant entries in your library.

**Weekly, or when a batch of sources has accumulated:**

> "Let's do a bind pass."

Bind updates concept and entity pages with recent material, creates topic hubs when warranted, and flags synthesis candidates for you to consider later.

**When an essay wants writing:**

> "Divine a synthesis on X."

Divine proposes the shape first (title, pages to draw from, argument sketch), waits for your approval, then drafts the essay under `scrolls/synthesis/`.

**Maintenance, roughly monthly:**

> "Audit the wiki." / "Illuminate — pull remote images local."

Audit surfaces contradictions, orphans, and stale claims. Illuminate downloads remote images into `raw/assets/` before the URLs rot, rewriting references to the local copies.

Grimoire doesn't watch your files — nothing runs until you ask.

## Setup

```bash
git clone <this-repo> grimoire
cd grimoire
cp grimoire.example.json grimoire.json
# edit grimoire.json — fill in owner_name, intellectual_profile, etc.
```

The Shelves scripts use only Python standard library — no `pip install` step. Requires Python 3.9 or later.

Grimoire is primarily an LLM-driven system — most day-to-day interaction is asking an LLM to run an operation. Claude Code with the skills in `.claude/skills/` is the reference implementation.

## Running the tests

```bash
pip install pytest
python3 -m pytest tests/ -v
```

The tests verify structural invariants: skill metadata, depersonalization, and that the Shelves scripts run clean on an empty catalog.

The depersonalization audit scans system files for strings that shouldn't leak into a public repo. It reads its patterns from `tests/fixtures/audit_patterns.json` (gitignored) if present, otherwise from `tests/fixtures/audit_patterns.example.json` (whose placeholders don't match anything real). To make the audit catch _your_ personal data, copy the example to the gitignored file and fill in your name, handles, and system paths:

```bash
cp tests/fixtures/audit_patterns.example.json tests/fixtures/audit_patterns.json
# edit tests/fixtures/audit_patterns.json
```

## Directory shape

```
desk/                # drop new material here
shelves/             # library catalog + generated context
scrolls/             # wiki pages you and the LLM co-maintain
raw/                 # ingested source material
.claude/skills/      # the six operations as Claude Code skills
grimoire.json        # your personal config (gitignored)
```

## Credits

- **Shelves** is a fork of [mccoyspace/llmbrary](https://github.com/mccoyspace/llmbrary).
- **Scrolls** was inspired by Andrej Karpathy's LLM-wiki [gist](https://gist.github.com/karpathy).
- Operation names (inscribe, bind, consult, divine, audit, illuminate) borrow the grimoire metaphor. If you fork this and rename them, go wild.

## License

MIT (see `LICENSE`). Fork freely; replace the example content with your own.
