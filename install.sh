#!/usr/bin/env bash

set -e

MODE="project"

if [[ "$1" == "--global" ]]; then
  TARGET="$HOME/.codex"
else
  TARGET="."
fi

mkdir -p "$TARGET/.codex/skills"

cp profiles/default/AGENTS.md "$TARGET/AGENTS.md"

cp -r skills/* "$TARGET/.codex/skills/"

echo "Installation complete."