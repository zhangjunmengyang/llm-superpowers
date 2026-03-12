#!/usr/bin/env bash
set -euo pipefail

pick_python() {
  if command -v python3 >/dev/null 2>&1; then
    echo "python3"
    return
  fi
  if command -v python >/dev/null 2>&1; then
    echo "python"
    return
  fi
  echo "Python is required to install llm-superpowers." >&2
  exit 1
}

SCRIPT_DIR=""
if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

if [[ -n "$SCRIPT_DIR" && -f "$SCRIPT_DIR/install.py" && -d "$SCRIPT_DIR/../skills" ]]; then
  exec "$(pick_python)" "$SCRIPT_DIR/install.py" "$@"
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git is required for the remote installer." >&2
  exit 1
fi

TMP_DIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

git clone --depth=1 https://github.com/zhangjunmengyang/llm-superpowers.git "$TMP_DIR/repo" >/dev/null 2>&1
exec "$(pick_python)" "$TMP_DIR/repo/scripts/install.py" "$@"
