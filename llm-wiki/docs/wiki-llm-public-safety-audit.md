# Wiki-LLM public-safety audit

Date: 2026-06-06  
Status: source path located; keep unlinked until Tomer chooses a public release path.

## Scope

This audit reviewed the local/private Wiki-LLM candidate material for workshop suitability without copying private knowledge-base content, local absolute paths, or private repository links into the public-ready hub.

Candidate material falls into three buckets:

1. A private knowledge vault that contains personal/research notes and raw source material.
2. A separate private plugin/software repo for Claude Code skills, commands, scripts, and operator docs.
3. Earlier private prototype vaults and a newer second-brain design/vault pair.

The exact private repository names and local checkout paths are intentionally withheld from this public-ready repo.

## Commands and checks run

- Listed candidate repositories with GitHub CLI filtered for wiki/LLM/knowledge/RAG terms.
- Shallow-cloned six private candidates into a temporary audit directory.
- Inspected top-level structure and README/contract files.
- Ran `gitleaks detect --no-banner --redact --exit-code 2` on each shallow clone.
- Ran a marker scan for local paths, API-key placeholders, secret/token terms, and provider-specific setup strings.

## Findings

### Useful public-safe concept

The workshop-safe concept is strong: a Markdown/Obsidian LLM wiki with a clear split between:

- **Vault/content:** private notes, raw sources, indexes, logs, and generated wiki pages.
- **Plugin/software:** reusable skills, slash commands, scripts, and operator docs that help an agent query or maintain the vault.

That split is exactly the right public-safety pattern for a workshop: teach the architecture and workflow without exposing the attendee to Tomer's private vault contents.

### Secret scan

`gitleaks` reported no findings in the six shallow-cloned candidates.

### Public-safety issues before direct linking

Do not link any Wiki-LLM candidate directly from the public hub yet.

Reasons:

- The active vaults are private knowledge stores by design and may include personal/research notes or raw source material.
- The software/plugin candidate is marked conceptually publishable, but the inspected docs still reference local checkout paths, private-vault wiring, and operator-specific setup details.
- Earlier prototypes include raw/wikilink examples that are useful as design history but not polished as attendee-facing setup material.
- The newer second-brain material includes detailed design docs and runbooks; some archived docs mention local paths and secret-handling setup patterns. They are not leaked real secrets, but they need redaction and framing before public release.
- Some docs use placeholder API-key examples for Obsidian/Local REST API wiring. These should be rewritten with `[TOKEN]` style placeholders and clear local-only privacy language before attendee use.

## Recommended public path

Best first workshop deliverable: create a sanitized overview page, not a direct repo link.

Suggested page: `llm-wiki/resources/wiki-llm-overview.html`.

Recommended framing:

- Explain the three-layer pattern: `raw/`, `wiki/`, and operating contract.
- Show a tiny synthetic vault example with public-safe fictional notes.
- Emphasize Markdown + git as source of truth; no vector DB or cloud store required for the basic pattern.
- Explain the safe split between private knowledge and reusable software.
- Keep all setup examples generic: `<vault-path>`, `[TOKEN]`, and `[plugin-path]`.
- Do not include Tomer's private vault names, raw note snippets, local paths, or private GitHub URLs.

## Inventory decision

Classification remains `polish-first`.

Wiki-LLM is workshop-relevant and worth showing if there is time, but the first public hub should only expose a sanitized overview or a cleaned software-only repo after Tomer explicitly approves that release path. Until then, the homepage card should remain an unlinked placeholder.
