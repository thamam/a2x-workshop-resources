# A2X Marketplace public-safety audit

Date: 2026-06-06

## Source located

- Public GitHub repo: `https://github.com/thamam/A2X-marketplace`
- GitHub metadata: `isPrivate: false`; default branch `main`; description: `Claude Code plugin marketplace - Maya AI development toolkit and custom plugins`.
- Local clone used for audit: temporary `/tmp/a2x-marketplace-audit.*` directory only; nothing copied into this repo.

## Current recommendation

2026-06-15 update: Tomer explicitly approved adding direct links from the placeholder folder to:

- `https://github.com/thamam/A2X-marketplace`
- `https://github.com/thamam/A2X-marketplace/blob/main/layout-designer.html`

Keep the sanitized overview/tutorial as the workshop-safe explanation. Treat the new links as direct source references, not as a fully curated install path.

Safe path for first workshop:

1. Point attendees to `A2X-public-marketplace/marketplace-links.md` only when Tomer wants to show the live marketplace source.
2. Use the sanitized overview/tutorial for the general concept and install mental model.
3. Before asking attendees to install or run real marketplace items, prepare a curated release path or facilitator-owned demo.

## Audit commands and findings

### Repository discovery

`gh repo list thamam --limit 200 --json nameWithOwner,isPrivate,url,description --jq ...` found:

```text
thamam/A2X-marketplace false https://github.com/thamam/A2X-marketplace Claude Code plugin marketplace - Maya AI development toolkit and custom plugins
```

`gh api repos/thamam/A2X-marketplace/contents --jq ...` showed top-level files:

```text
.claude-plugin/
.claude/
.gitignore
.octocode/
.serena/
INSTALLATION.md
README.md
plugins/
profiles.json
```

### Secret/local-path scan of a shallow clone

A temporary shallow clone contained 212 tracked files.

`gitleaks detect --no-banner --redact --source .` reported 5 `private-key` findings in:

```text
plugins/code-research/skills/octocode-research/scripts/server.js
```

Manual spot-check shows this file is a large bundled/minified server script and the matches appear around bundled dependency strings/functions rather than a straightforward checked-in PEM block, but this should still be treated as a release blocker until reviewed in the marketplace repo.

Pattern scan findings that matter for public hub linking:

- Absolute local home-directory paths appear in 5 files, including `profiles.json`, `INSTALLATION.md`, `plugins/mactools/README.md`, and `plugins/code-research/...` files.
- `LINEAR_API_KEY` appears in `README.md` and `INSTALLATION.md` as setup instructions.
- Maintainer email appears in README/installation/plugin metadata.
- Generic `api key`, `token`, `password`, and `secret` terms appear in docs and bundled code; these are not automatically leaks, but they make the repo noisy for a workshop handout.

## Public-safety notes

The repo is already public, so the approval issue is not repository exposure itself. The issue is whether the workshop hub should point attendees to it as a recommended resource.

Do not copy installation instructions wholesale yet because they include:

- absolute local development paths,
- environment-variable/API-key setup for Linear,
- plugin internals and bundled code that trigger secret-scanner noise,
- maintainer email and personal workflow details.

## Next action

If attendees will install or run real marketplace items, prepare a curated release path or facilitator-owned demo. The direct source links now exist in `A2X-public-marketplace/marketplace-links.md` by Tomer's request.
