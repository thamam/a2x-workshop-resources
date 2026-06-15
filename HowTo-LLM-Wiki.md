# HowTo-LLM-Wiki — Build a Basic LLM Wiki with Claude Code

This is the workshop-safe version of Andrej Karpathy's LLM Wiki idea: keep raw material in Markdown, ask Claude Code to synthesize linked wiki pages, and make the agent cite what it used.

## Source inspiration

- Karpathy gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Local raw Markdown copy: [`LocalCopies/karpathy-llm-wiki.md`](LocalCopies/karpathy-llm-wiki.md)

## Goal

Build a tiny local Markdown wiki that Claude Code can maintain.

The important pattern:

```text
raw notes -> synthesized wiki pages -> reviewed updates over time
```

No database is needed for the first version.

## Minimal folder tree

Create this inside a private project folder or vault:

```text
llm-wiki/
  raw/
    inbox.md
  wiki/
    index.md
  OPERATING_CONTRACT.md
```

## Setup steps

1. Create the folders:

   ```bash
   mkdir -p llm-wiki/raw llm-wiki/wiki
   touch llm-wiki/raw/inbox.md
   touch llm-wiki/wiki/index.md
   ```

2. Add a few raw notes to `llm-wiki/raw/inbox.md`.

   Use fictional, public, or sanitized notes for workshops. Do not paste customer data, credentials, private repo contents, production logs, employee records, account screenshots, contracts, or confidential strategy.

3. Create `llm-wiki/OPERATING_CONTRACT.md`:

   ```markdown
   # LLM Wiki operating contract

   You are maintaining this Markdown wiki.

   Rules:
   - Read `raw/` before editing `wiki/`.
   - Every wiki page must list source notes used.
   - Link related pages with Markdown links.
   - If a fact is not supported by raw notes, mark it as unknown.
   - Do not include private names, credentials, local paths, or raw secrets in public pages.
   - Prefer small edits over full rewrites.
   - End with a changelog of files changed and claims that need human review.
   ```

4. Open Claude Code in the folder that contains `llm-wiki/`.

5. Ask Claude Code to build or update the wiki.

## Claude Code prompt

```text
Read llm-wiki/OPERATING_CONTRACT.md.
Use the notes in llm-wiki/raw/.
Update llm-wiki/wiki/ so it becomes a small linked Markdown wiki.

For each changed page, include:
1. What changed
2. Source notes used
3. Related pages
4. Open questions
5. Unsupported claims to verify

Do not invent facts. Keep private material private.
```

## First useful wiki pages

Start with only a few pages:

```text
llm-wiki/wiki/index.md
llm-wiki/wiki/projects.md
llm-wiki/wiki/people-and-roles.md
llm-wiki/wiki/open-questions.md
```

Add more pages only when the notes justify them.

## Good review questions

- Did every claim come from raw notes?
- Did Claude Code link related pages?
- Did it mark unknowns instead of guessing?
- Did it preserve private/sensitive boundaries?
- Are the pages useful to read later, or just polished noise?

## Related local material

- HTML tutorial: [`resources/wiki-llm-tutorial.html`](resources/wiki-llm-tutorial.html)
- Local Karpathy Markdown copy: [`LocalCopies/karpathy-llm-wiki.md`](LocalCopies/karpathy-llm-wiki.md)
