---
name: illuminate
description: Use when the user asks to localize images, pull images local, or roughly monthly — sweeps the corpus for remote image URLs that will rot, downloads them to raw/assets/, and rewrites the markdown references to local relative paths. The name is borrowed from illuminated manuscripts (images in pages).
---

# illuminate

> This skill is written from the CLAUDE.md spec, not from a real run. After the first real illuminate pass, rewrite this skill from what actually happened.

This is a maintenance operation. It does **not** create new wiki pages. Its only job is to harden the corpus against link rot (especially Web Clipper output and Twitter threads carrying `pbs.twimg.com` URLs).

## Steps

1. **Scan** `raw/processed/`, `desk/`, and `scrolls/` for markdown files containing remote image references — `![...](https://...)` and similar. Twitter image hosts (`pbs.twimg.com`) and Substack/Wordpress CDNs are the highest-priority targets.
2. **Download** each remote image to `raw/assets/`. Use a stable filename derived from the source page slug (e.g. `karpathy-method-img-01.jpg`). If the asset already exists at the target filename, skip the download.
3. **Rewrite** the markdown reference to point at the local copy via a relative path from the file being edited.
4. **Skip** YouTube thumbnails and other links that are not real images. **Skip** dead URLs (note them in the log so the user can decide what to do).
5. **Append a brief log entry** to `scrolls/log.md`:

```
## [YYYY-MM-DD] illuminate | <N> localized, <M> failed
```

Body: which source files were touched, how many images per file, and the dead URLs (with their containing files) for the user to triage.
