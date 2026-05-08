# pdbe-bioskills

A curated collection of Claude Code skills (slash commands) and agent profiles for life sciences and bioinformatics workflows.

## Available items

| Type | Name | Description |
|------|------|-------------|
| Skill | `convert-to-prd` | Convert raw planning notes into a structured Life Sciences PRD |
| Agent | `coding` | Software engineering and technical research assistant |

## Installation

### pip (recommended)

```bash
pip install pdbe-bioskills
```

Then from any project directory:

```bash
# See what's available
pdbe-bioskills list

# Interactive install (pick what you want)
pdbe-bioskills install

# Install everything for Claude Code
pdbe-bioskills install --all --claude

# Install everything for Codex
pdbe-bioskills install --all --codex

# Install both targets
pdbe-bioskills install --all --claude --codex

# Install specific items by name
pdbe-bioskills install --claude convert-to-prd coding

# Install globally (available in all projects, goes to $HOME)
pdbe-bioskills install --all --claude --global
```

### pipx (isolated global install)

```bash
pipx install pdbe-bioskills
pdbe-bioskills list
```

## Where files are installed

| Flag | Destination |
|------|-------------|
| `--claude` | Skills → `.claude/commands/<name>.md` · Agents → `.claude/agents/<name>.md` |
| `--codex` | Skills → `.codex/skills/<name>/` · Agents → `.codex/AGENTS.md` |
| `--global` | Prepends `$HOME` to the paths above |
| `--dir PATH` | Uses a custom base directory |

## Contributing

**Add a skill** — create `src/pdbe_bioskills/skills/<name>/SKILL.md` with YAML frontmatter:

```markdown
---
name: your-skill-name
description: One-line description of what the skill does
---

Skill instructions here...
```

**Add an agent profile** — create `src/pdbe_bioskills/profiles/<name>/AGENTS.md` with YAML frontmatter:

```markdown
---
name: your-agent-name
description: One-line description of the agent
---

Agent instructions here...
```

The CLI discovers items automatically — no registry to update.

## License

MIT
