# A2X Workshop Resources

Public-facing resources for A2X Claude Code workshops.

## Start here

- **START-HERE:** [`START-HERE.md`](START-HERE.md)
- **Live resource hub:** https://thamam.github.io/a2x-workshop-resources/
- **A2X website:** https://a2xautonomy.com/
- **Website resources section:** https://a2xautonomy.com/#resources

If you arrived here from a workshop, start with [`START-HERE.md`](START-HERE.md). The older resource set is intentionally curated through [`Library/`](Library/) so the repo does not feel like a wall of handouts.

## Tomorrow's required material

- [`HowTo-OpenSpec.md`](HowTo-OpenSpec.md) — basic OpenSpec setup.
- [`llm-wiki/`](llm-wiki/) — LLM-Wiki guide, local copies, and raw source bundle.
- [`llm-wiki/HowTo-LLM-Wiki.md`](llm-wiki/HowTo-LLM-Wiki.md) — build a basic LLM Wiki with Claude Code.
- [`llm-wiki/raw-sources/`](llm-wiki/raw-sources/) — memory, dreaming, consolidation, and AI-agent memory source Markdown.
- [`llm-wiki/local-copies/karpathy-llm-wiki.md`](llm-wiki/local-copies/karpathy-llm-wiki.md) — local copy of Karpathy's LLM Wiki Markdown.
- [`Examples/OpenSpec/`](Examples/OpenSpec/) — empty OpenSpec tree for Tomer to fill later.
- [`A2X-public-marketplace/`](A2X-public-marketplace/) — placeholder while marketplace material is organized.
- [`Library/`](Library/) — curated index of existing artifacts.

## What belongs here

- Public workshop setup guides.
- Public-safe examples and demos.
- Curated links to public tools and references.
- Public-safe copies of referenced source material.

## What does not belong here

- Secrets, tokens, keys, or credentials.
- Private client material.
- Internal A2X website source code.
- Personal notes not intended for attendees.
- Local environment files such as `.env`.

## Root directory note

The root is intentionally small. The visible files are navigation, security/config, the static Pages entrypoint, and the project tracker. The large generated artifact set remains under `resources/` and is curated from `Library/`.


## Change workflow

All changes to `main` must go through a pull request. Do not push directly to `main`.

Default workflow:

```bash
git checkout main
git pull --ff-only origin main
git checkout -b <short-change-branch>
# make changes
git add <files>
git commit -m "<message>"
git push -u origin <short-change-branch>
gh pr create --base main
```

Before merge, the PR must pass the repository security/static checks.

## Security rule

Every commit must pass secret scanning, private-file checks, and static local-link checks.

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

GitHub Pages publishes from `main` branch `/` at `https://thamam.github.io/a2x-workshop-resources/`.
