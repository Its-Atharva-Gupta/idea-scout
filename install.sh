#!/usr/bin/env bash
# 🔭 Idea Scout — 1-Command Universal Skill Installer
#
# One-line remote installation:
#   curl -fsSL https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.sh | bash -s -- --all
#
# Local clone installation:
#   bash install.sh [flags]

set -euo pipefail

REPO="Its-Atharva-Gupta/idea-scout"
BRANCH="main"

# Check for Node.js (>= 16) or Python 3
if ! command -v node >/dev/null 2>&1 && ! command -v python3 >/dev/null 2>&1; then
  echo "✖ Error: Either Node.js (≥16) or Python 3 is required to run the installer." >&2
  exit 1
fi

# Detect if running from within local repository clone
HERE=""
SOURCE_PATH="${BASH_SOURCE[0]:-}"
if [ -n "$SOURCE_PATH" ]; then
  HERE="$(cd "$(dirname "$SOURCE_PATH")" 2>/dev/null && pwd)" || HERE=""
fi

if [ -n "$HERE" ] && [ -f "$HERE/bin/install.js" ]; then
  exec node "$HERE/bin/install.js" "$@"
fi

# Remote curl | bash pipe: create ephemeral temp dir, fetch repo, and run
TMP_DIR="$(mktemp -d -t idea-scout-install-XXXXXX)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "→ Fetching latest Idea Scout skill from GitHub (${REPO})..."

if command -v git >/dev/null 2>&1; then
  git clone --depth 1 -b "$BRANCH" "https://github.com/${REPO}.git" "$TMP_DIR" >/dev/null 2>&1
else
  curl -fsSL "https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz" | tar -xz -C "$TMP_DIR" --strip-components=1
fi

if [ -f "$TMP_DIR/bin/install.js" ]; then
  exec node "$TMP_DIR/bin/install.js" "$@"
else
  echo "✖ Failed to fetch installer script." >&2
  exit 1
fi
