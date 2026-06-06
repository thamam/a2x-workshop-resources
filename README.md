# A2X Workshop Resources

Public-facing resources for A2X Claude Code workshops.

This repository is designed to become public. Treat every commit as publishable.

## What belongs here

- Workshop resource hub content.
- Public setup guides.
- Public demos and examples.
- Links to public tools and references.

## What does not belong here

- Secrets, tokens, keys, or credentials.
- Private client material.
- Internal A2X website source code.
- Personal notes not intended for attendees.
- Local environment files such as `.env`.

## Security rule

Before this repository becomes public, every commit must pass secret scanning, private-file checks, and static local-link checks.

Local verification:

```bash
scripts/block-private-files.sh $(git ls-files)
python3 scripts/check-static-links.py
```

## Local preview

This is a no-build static hub. Preview it locally with:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/index.html`.

GitHub Pages readiness notes live in `docs/github-pages-readiness.md`. Do not enable Pages or make the repo public without Tomer approval.
