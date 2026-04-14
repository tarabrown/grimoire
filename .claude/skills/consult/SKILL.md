---
name: consult
description: Use when the user asks a substantive question the wiki should be the primary source for — reads the index, pulls relevant pages, synthesizes an answer with wikilinks back to sources, and offers to save reusable answers as reports.
---

# consult

> This skill is written from the CLAUDE.md spec, not from a real run. After the first real query, rewrite this skill from what actually happened.

## Steps

1. **Read `scrolls/index.md`** to find the relevant pages. The index is the entry point — don't grep blind across the whole wiki when the index is the catalog.
2. **Read those pages** in full. Follow the `## See also` links one hop if a page references something that looks load-bearing for the answer.
3. **Synthesize an answer.** Use `[[wikilinks]]` to point the user back to the pages and sources you drew on. Cite source filenames where a specific claim depends on a specific source.
4. **Flag uncertainty** explicitly. If two sources conflict, say so. If the answer rests on a single source, say so. Don't fill gaps with plausible-sounding content that isn't in the wiki.
5. **Offer to save reusable answers.** If the answer is substantive and the user is likely to want to refer back to it (or use it as future source material), offer to save it as a new page in `scrolls/reports/`. Reports are Q&A outputs — distinct from `scrolls/synthesis/`, which is reserved for cross-cutting essays drafted by `divine`.

## Logging

Consult logs only when it produces a report under `scrolls/reports/`. Plain Q&A answers in the conversation are not logged.

When a report is saved, append an entry to `scrolls/log.md` using the canonical header format:

```
## YYYY-MM-DD consult — report <slug> created
```

Body: the question asked, and a one-line summary of the answer.
