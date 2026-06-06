# A2X Marketplace public-safety audit

Date: 2026-06-06

## Source located

- Public GitHub repo: `https://github.com/thamam/A2X-marketplace`
- GitHub metadata: `isPrivate: false`; default branch `main`; description: `Claude Code plugin marketplace - Maya AI development toolkit and custom plugins`.
- Local clone used for audit: temporary `/tmp/a2x-marketplace-audit.*` directory only; nothing copied into this repo.

## Current recommendation

Keep the workshop hub card as a **placeholder** for now. The repo is public and can be named internally, but the workshop hub should not add an active public link until the marketplace docs are cleaned up or a short sanitized landing page is written.

Safe path for first workshop:

1. Keep hub card unlinked.
2. If Tomer wants to mention it live, describe it verbally as a plugin marketplace for Claude Code workflows.
3. Before linking publicly from this hub, either:
   - clean the marketplace repo docs, then link `https://github.com/thamam/A2X-marketplace`, or
   - add a short public-safe overview page in this repo that avoids setup details, local paths, and plugin internals.

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

Create a sanitized marketplace overview card/page only after Tomer chooses one of these directions:

- link the existing public repo after cleanup, or
- keep the repo unlinked and publish only a short attendee-safe explanation of what a Claude Code marketplace is.
