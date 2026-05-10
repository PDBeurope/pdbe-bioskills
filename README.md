# pdbe-bioskills

A curated collection of skills and agent profiles, developed by PDBe team, for developing analyses and workflows of PDBe/structure datasets.

## Available items

### Skills

| Name | Description |
|------|-------------|
| `afdb-api-fetching` | Retrieve structural and confidence data for homodimers from the AFDB API, including mmCIF files, PAE matrices, and pLDDT scores |
| `aggregated-interface-ingestion` | Build or validate the aggregated interface schema for a set of PDB complexes from chain correspondence data |
| `convert-to-prd` | Convert rough InsightFold notebook ideas or planning notes into a structured life-sciences PRD |
| `fixture-selection` | Select and document pinned fixtures for InsightFold notebooks |
| `homodimer-confidence-scoring` | Implement and review AlphaFold Database homodimer interface confidence scoring (PAE, ipTM, ipSAE, pDockQ, LIS) |
| `ipsae-implementation` | Compute interface predicted TM-score (ipTM) and interface predicted aligned error (ipSAE) metrics |
| `lis-implementation` | Compute the Local Interaction Score by averaging normalized low-PAE inter-chain interactions |
| `molviewspec-rendering` | Produce 3D structural views using MolViewSpec, including chain coloring, pLDDT overlays, and interface highlights |
| `notebook-assembly` | Compile modular sections into a cohesive Jupyter notebook with sequential execution and validation outputs |
| `notebook-execution-validation` | Validate InsightFold notebooks against their spec, fixtures, data contracts, and runtime constraints |
| `notebook-from-spec` | Build an InsightFold Jupyter notebook from a reviewed spec pack |
| `notebook-review` | Perform final qualitative review of InsightFold notebooks for scientific correctness and reproducibility |
| `notebook-spec-review` | Review InsightFold notebook spec packs before implementation starts |
| `pae-visualization` | Create heatmaps and overlays for PAE matrices with annotations and color conventions |
| `pdbe-llm-annotation-fetching` | Fetch LLM-derived residue annotations from the PDBe LLM annotation REST API |
| `pdockq-implementation` | Calculate pDockQ and pDockQ2 scores based on interface contacts and PAE-derived probabilities |
| `prd-notebook-generation` | Generate the PRD homodimer confidence diagnostic notebook from the spec using agent workflows |
| `prd-to-notebook-spec` | Convert an approved InsightFold PRD into spec-driven notebook development documentation |
| `sifts-sequence-mapping` | Map PDBx/mmCIF structure sequences to UniProtKB or a custom FASTA using the SIFTS pipeline |
| `validation-against-reference` | Compare computed metrics against reference implementations, ensuring numerical accuracy within tolerance |

### Agent profiles

| Name | Description |
|------|-------------|
| `3d-beacons-aggregator` | Aggregate, compare, and rank structural models for a target protein from 3D-Beacons providers |
| `afdb-model-reviewer` | Review AlphaFold Database model confidence, applicability, and suitability for downstream analysis |
| `binding-site-analyser` | Identify, characterise, and annotate protein-ligand and protein-protein binding sites in PDB structures |
| `coding` | Software engineering and technical research assistant |
| `deposition-reviewer` | Review macromolecular structure depositions for metadata completeness and PDB archive compliance |
| `fixture-curator` | Select and document pinned fixtures for InsightFold notebooks |
| `lifecycle` | Support the project-wide notebook-driven development lifecycle across notebooks and biological domains |
| `notebook-builder` | Build InsightFold notebooks from reviewed spec packs |
| `notebook-reviewer` | Perform final qualitative review of InsightFold notebooks after execution validation |
| `notebook-validator` | Validate that an InsightFold notebook executes and matches its spec, fixtures, and runtime constraints |
| `pdbekb-annotator` | Aggregate and map PDBe-KB functional residue annotations onto PDB structures for notebook use |
| `sifts-mapper` | Map between UniProt sequence positions and PDB structure residue numbers using SIFTS |
| `spec-reviewer` | Review InsightFold notebook spec packs before implementation starts |
| `structure-quality-assessor` | Assess PDB/mmCIF structure quality using wwPDB validation metrics and flag issues for curation |

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
