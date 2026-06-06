# Security policy

This repository is intended to become public.

Do not commit:

- API keys, tokens, passwords, or credentials.
- `.env` files, private keys, certificates, or local config.
- Client names, private client material, or internal notes.
- Private A2X website source code.

Required checks:

- `gitleaks` secret scan.
- Private-file blocker script.
- GitHub Actions security workflow.

If a secret is committed, assume it is compromised. Rotate it before continuing.
