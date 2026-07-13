#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

if [[ -x ".venv/bin/python" ]]; then
  exec .venv/bin/python scripts/validate.py
fi

exec python scripts/validate.py
