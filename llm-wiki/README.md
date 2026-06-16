# LLM-Wiki Workshop Resources

This directory keeps the LLM-Wiki workshop material together.

## Start here

- [`HowTo-LLM-Wiki.md`](HowTo-LLM-Wiki.md) — basic Claude Code workflow for maintaining a Markdown wiki.
- [`raw-sources/`](raw-sources/) — source chooser for the live demos: `memory/` for agent-memory synthesis, `kids-books/` for simple ingestion practice.
- [`local-copies/karpathy-llm-wiki.md`](local-copies/karpathy-llm-wiki.md) — local copy of Andrej Karpathy's LLM-Wiki idea.
- [`resources/wiki-llm-tutorial.html`](resources/wiki-llm-tutorial.html) — legacy HTML tutorial page.
- [`resources/wiki-llm-overview.html`](resources/wiki-llm-overview.html) — legacy HTML overview page.

## Pick the right source path

- Use [`raw-sources/memory/`](raw-sources/memory/) when the room is ready for synthesis: human memory systems, dreaming, and AI-agent memory design.
- Choose [`raw-sources/kids-books/`](raw-sources/kids-books/) when you want a lighter ingestion demo: copyable public-domain stories with obvious characters and plot structure.
- Consult [`local-copies/karpathy-llm-wiki.md`](local-copies/karpathy-llm-wiki.md) when explaining the LLM-Wiki concept itself before creating a new wiki.

## Demo question

> What can AI-agent memory design learn from human memory systems, memory consolidation, and dreaming?

Suggested workflow:

1. Read [`raw-sources/README.md`](raw-sources/README.md).
2. Open Claude Code in a clean demo folder.
3. Create `raw/`, `wiki/`, and `OPERATING_CONTRACT.md` using the how-to.
4. Copy the Markdown files from the cloned repo’s [`llm-wiki/raw-sources/memory/`](raw-sources/memory/) folder into your clean demo folder’s `raw/` directory for the synthesis demo, or copy [`llm-wiki/raw-sources/kids-books/`](raw-sources/kids-books/) for a simpler ingestion walkthrough.
5. Ask Claude Code to build a small linked wiki from the sources.

## Boundaries

This directory is intentionally narrow. Do not add more public artifacts here unless the workshop actually needs them.
