---
name: audit
description: Use when the user asks to audit, lint, or check the wiki — surfaces contradictions, orphans, mentioned-but-missing concepts, stale claims, and weak cross-references. Reports only; does not write except for unambiguous typos and broken links.
---

# audit

> This skill is written from the CLAUDE.md spec, not from a real run. After the first real audit pass, rewrite this skill from what actually happened.

Audit is a *reporting* operation, not a writing operation. Its job is to surface issues for the user (or for the next bind pass) to act on. Don't fix things unilaterally unless they are unambiguous typos or broken-link cleanups.

## What to look for

- **Contradictions between pages.** Two pages making opposing claims, or a source page whose claim isn't reflected on the concept page that cites it.
- **Orphan pages.** Pages with no inbound links from anywhere (not from `scrolls/index.md`, not from any `## See also`, not from any frontmatter `sources:` reference). Orphans aren't necessarily wrong — sometimes a page is the seed of a future cluster — but they should be visible.
- **Concepts mentioned but not pages.** Recurring `[[wikilinks]]` (or recurring inline mentions) of a concept that has no page yet. These are concept-hub candidates for the next bind.
- **Stale claims.** A page making a claim a newer source has superseded or contradicted, where the page hasn't been updated.
- **Weak cross-references.** Pages that should be linked together (clear thematic overlap) but aren't.
- **Suggested topics.** Gaps where the existing material implies an investigation worth running.

## Output

Write the audit result as a structured report directly to the user in the conversation. If the report is substantive enough that the user will want to refer back to it, offer to save it to `scrolls/reports/`. Either way, append a short entry to `scrolls/log.md` using the canonical header format:

```
## YYYY-MM-DD audit — <one-line summary of what surfaced>
```

Body: how many issues in each category, plus any items that were unambiguous enough to fix in passing (broken links, obvious typos).
