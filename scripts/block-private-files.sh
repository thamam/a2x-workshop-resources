#!/usr/bin/env bash
set -euo pipefail

blocked=0
for file in "$@"; do
  case "$file" in
    *.pem|*.key|*.p12|*.pfx|*.kdbx|*.mobileprovision|*.env|.env|.env.*|*id_rsa*|*id_ed25519*)
      echo "Blocked private or credential-looking file: $file" >&2
      blocked=1
      ;;
  esac

  if [[ -f "$file" && "$file" != "scripts/block-private-files.sh" ]]; then
    if grep -I -nE 'BEGIN (RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY|PRIVATE CLIENT|CONFIDENTIAL|DO NOT SHARE' "$file" >/dev/null; then
      echo "Blocked private/confidential marker in: $file" >&2
      blocked=1
    fi
  fi
done

exit "$blocked"
