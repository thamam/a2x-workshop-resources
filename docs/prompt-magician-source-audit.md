# Prompt Magician source/setup audit

Date: 2026-06-06

Scope: locate the likely Prompt Magician source/setup material and decide whether the workshop hub can link it publicly now. This audit does **not** publish or enable any public link from the hub.

## Finding

The likely source is the public GitHub repository `https://github.com/thamam/prompt-enhancer-extension`.

Why this appears to match Prompt Magician:

- `gh repo list thamam --limit 200 --json name,visibility,url` surfaced public repo `prompt-enhancer-extension` while searching for prompt/magic-related repositories.
- The repo describes itself as **Prompt Enhancer Pro**, a dual Chrome + VS Code prompt enhancement tool.
- It provides the workshop-relevant behavior expected from Prompt Magician: prompt rewrite modes, Claude/GPT optimization, anti-pattern fixes, prompt scoring, and optional LLM-backed enhancement.
- Setup docs exist in `README.md`, `INSTALL.md`, `QUICKSTART.md`, `chrome/README.md`, and `vscode/README.md`.

## Repository snapshot inspected

- Source: `https://github.com/thamam/prompt-enhancer-extension`
- Visibility from GitHub API/CLI: `PUBLIC`
- Shallow clone path used for audit: temporary local audit directory, now intentionally omitted.
- Commit inspected: `a6ff179`

## Public-safety notes

Status: **polish-first**.

The repo is already public and has useful setup docs, but the workshop hub should keep the Prompt Magician card unlinked until one of these happens:

1. A short public-safe overview/setup page is written in this repo, or
2. The source repo is cleaned/curated enough that linking it directly is intentional.

Reasons to avoid a direct first-release hub link today:

- The setup docs include remote API-key configuration examples and placeholder key formats. These are not leaked real secrets, but they can distract workshop attendees and need clear privacy framing.
- `gitleaks` flags the security-scanner regex strings for private-key detection as four `private-key` findings. Manual inspection shows these are scanner patterns, not actual private keys, but they would create noise in a release audit.
- The Chrome manifest requests broad content-script matching (`<all_urls>`) plus LLM provider host permissions. That may be appropriate for an extension, but it deserves a short safety explanation before sending attendees to install it.
- Keyboard shortcut defaults are documented as conflicting with browser shortcuts in `QUICKSTART.md`; attendees need a cleaned quick-start path.

## Checks run

From this repo:

- `gh auth status` — authenticated as `thamam`.
- `gh repo list thamam --limit 200 --json name,visibility,url` — located `prompt-enhancer-extension` as public.
- `git clone --depth 1 https://github.com/thamam/prompt-enhancer-extension.git <temporary-audit-dir>` — cloned successfully.
- `node --check` across root/core/chrome/vscode JavaScript files — passed.
- `gitleaks detect --source <temporary-audit-dir> --no-git --redact` — reported 4 findings, all scanner regex strings in `security-scanner.js` / `core/security-scanner.js` after manual line inspection.
- `scripts/block-private-files.sh $(git ls-files)` — passed for the workshop resource hub.
- `python3 scripts/check-static-links.py` — passed for 9 HTML files.

## Recommended next action

For the workshop hub, keep the homepage card as a placeholder and create a sanitized `resources/prompt-magician-setup.html` only if Tomer wants this in the first workshop wave. The sanitized page should:

- Position it as an optional advanced prompt-enhancement extension, not a required workshop dependency.
- Prefer local/offline modes and explain when remote LLM APIs send selected text to providers.
- Avoid showing fake secret-looking API keys inline unless necessary; use `[API_KEY]` placeholders instead.
- Tell attendees to load the Chrome extension from a curated `chrome/` folder or use the VS Code extension path, not to wander through all source docs during the workshop.
- Mention shortcut conflicts and suggest `Alt+Shift+E/Z/I/C` alternatives.
