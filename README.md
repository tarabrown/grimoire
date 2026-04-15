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
pip install -r requirements-dev.txt
python3 -m pytest tests/ -v
```

The tests verify structural invariants: skill metadata, depersonalization, and that the Shelves scripts run clean on an empty catalog.

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
