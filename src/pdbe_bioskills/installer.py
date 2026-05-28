from __future__ import annotations

import shutil
from pathlib import Path

from pdbe_bioskills.discovery import Item


def install_skill_claude(item: Item, base: Path) -> Path:
    dest_dir = base / ".claude" / "commands"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{item.name}.md"
    shutil.copy2(item.source_dir / "SKILL.md", dest)
    return dest


def install_skill_codex(item: Item, base: Path) -> Path:
    dest_dir = base / ".codex" / "skills" / item.name
    shutil.copytree(
        item.source_dir,
        dest_dir,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("agents", "references", "assets", "scripts"),
    )
    return dest_dir


def install_agent_claude(item: Item, base: Path) -> Path:
    dest_dir = base / ".claude" / "agents"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{item.name}.md"
    shutil.copy2(item.source_dir / "AGENTS.md", dest)
    return dest


def install_agent_codex(item: Item, base: Path) -> Path:
    dest_dir = base / ".codex"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "AGENTS.md"
    src = item.source_dir / "AGENTS.md"
    content = src.read_text(encoding="utf-8")
    if dest.exists():
        existing = dest.read_text(encoding="utf-8")
        if content.strip() in existing:
            return dest
        with dest.open("a", encoding="utf-8") as f:
            f.write("\n\n---\n\n")
            f.write(content)
    else:
        dest.write_text(content, encoding="utf-8")
    return dest
