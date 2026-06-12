# pdbe-bioskills

A curated collection of skills and agent profiles, developed by PDBe team, for developing analyses and workflows of PDBe/structure datasets.

> [!WARNING]  
> This repository is under active development and may change significantly. Please use it with caution.

## Available items

### Skills

#### Domain specific

| Name | Description |
|------|-------------|
| [`afdb-api-fetching`](skills/afdb-api-fetching/SKILL.md) | Retrieve structural and confidence data from the AFDB API, including mmCIF files, PAE matrices, and pLDDT scores |
| [`aggregated-interface-ingestion`](skills/aggregated-interface-ingestion/SKILL.md) | Build or validate the aggregated interface schema for a set of PDB complexes from chain correspondence data |
| [`homodimer-confidence-scoring`](skills/homodimer-confidence-scoring/SKILL.md) | Implement and review AlphaFold Database homodimer interface confidence scoring (PAE, ipTM, ipSAE, pDockQ, LIS) |
| [`ipsae-implementation`](skills/ipsae-implementation/SKILL.md) | Compute interface predicted TM-score (ipTM) and interface predicted aligned error (ipSAE) metrics |
| [`lis-implementation`](skills/lis-implementation/SKILL.md) | Compute the Local Interaction Score by averaging normalized low-PAE inter-chain interactions |
| [`molviewspec-rendering`](skills/molviewspec-rendering/SKILL.md) | Produce 3D structural views using MolViewSpec, including chain coloring, pLDDT overlays, and interface highlights |
| [`pae-visualization`](skills/pae-visualization/SKILL.md) | Create heatmaps and overlays for PAE matrices with annotations and color conventions |
| [`pdbe-llm-annotation-fetching`](skills/pdbe-llm-annotation-fetching/SKILL.md) | Fetch LLM-derived residue annotations from the PDBe LLM annotation REST API |
| [`pdockq-implementation`](skills/pdockq-implementation/SKILL.md) | Calculate pDockQ and pDockQ2 scores based on interface contacts and PAE-derived probabilities |
| [`sifts-sequence-mapping`](skills/sifts-sequence-mapping/SKILL.md) | Map PDBx/mmCIF structure sequences to UniProtKB or a custom FASTA using the SIFTS pipeline |
| [`validation-against-reference`](skills/validation-against-reference/SKILL.md) | Compare computed metrics against reference implementations, ensuring numerical accuracy within tolerance |

#### Development lifecycle

| Name | Description |
|------|-------------|
| [`concept-to-prd`](skills/concept-to-prd/SKILL.md) | Convert scoped InsightFold concepts or advisory-panel notes into a structured life-sciences PRD |
| [`fixture-selection`](skills/fixture-selection/SKILL.md) | Select and document pinned fixtures for InsightFold notebooks |
| [`idea-scoping-interview`](skills/idea-scoping-interview/SKILL.md) | Guide early concept discovery before PRD writing via a structured scoping interview |
| [`notebook-assembly`](skills/notebook-assembly/SKILL.md) | Compile modular sections into a cohesive Jupyter notebook with sequential execution and validation outputs |
| [`notebook-execution-validation`](skills/notebook-execution-validation/SKILL.md) | Validate InsightFold notebooks against their spec, fixtures, data contracts, and runtime constraints |
| [`notebook-from-spec`](skills/notebook-from-spec/SKILL.md) | Build an InsightFold Jupyter notebook from a reviewed spec pack |
| [`notebook-review`](skills/notebook-review/SKILL.md) | Perform final qualitative review of InsightFold notebooks for scientific correctness and reproducibility |
| [`notebook-spec-review`](skills/notebook-spec-review/SKILL.md) | Review InsightFold notebook spec packs before implementation starts |
| [`notebook-ux-contract`](skills/notebook-ux-contract/SKILL.md) | Define the first runnable user workflow for a notebook before fixture selection and implementation |
| [`prd-notebook-generation`](skills/prd-notebook-generation/SKILL.md) | Orchestrate the full InsightFold lifecycle from an approved PRD to a validated, reviewed notebook |
| [`prd-to-notebook-spec`](skills/prd-to-notebook-spec/SKILL.md) | Convert an approved InsightFold PRD into an implementation-ready notebook spec pack |
| [`scoping-decision-capture`](skills/scoping-decision-capture/SKILL.md) | Convert scoping conversations or advisory-panel discussions into a structured decision capture |

### Agent profiles

#### Domain specific

| Name | Description |
|------|-------------|
| [`3d-beacons-aggregator`](profiles/3d-beacons-aggregator/AGENTS.md) | Aggregate, compare, and rank structural models for a target protein from 3D-Beacons providers |
| [`afdb-model-reviewer`](profiles/afdb-model-reviewer/AGENTS.md) | Review AlphaFold Database model confidence, applicability, and suitability for downstream analysis |
| [`binding-site-analyser`](profiles/binding-site-analyser/AGENTS.md) | Identify, characterise, and annotate protein-ligand and protein-protein binding sites in PDB structures |
| [`coding`](profiles/coding/AGENTS.md) | Software engineering and technical research assistant |
| [`deposition-reviewer`](profiles/deposition-reviewer/AGENTS.md) | Review macromolecular structure depositions for metadata completeness and PDB archive compliance |
| [`homodimer-orchestrator`](profiles/homodimer-orchestrator/AGENTS.md) | Coordinate development of the AFDB homodimer diagnostic notebook across specialized agents |
| [`homodimer-reporter`](profiles/homodimer-reporter/AGENTS.md) | Briefing document and agent suite for recreating the AFDB homodimer diagnostic notebook |
| [`pdbekb-annotator`](profiles/pdbekb-annotator/AGENTS.md) | Aggregate and map PDBe-KB functional residue annotations onto PDB structures for notebook use |
| [`scientific-python-engineer`](profiles/scientific-python-engineer/AGENTS.md) | Implement scientific Python code for homodimer diagnostic notebooks |
| [`sifts-mapper`](profiles/sifts-mapper/AGENTS.md) | Map between UniProt sequence positions and PDB structure residue numbers using SIFTS |
| [`structural-biologist`](profiles/structural-biologist/AGENTS.md) | Interpret AlphaFold confidence metrics and provide structural biology guidance |
| [`structure-quality-assessor`](profiles/structure-quality-assessor/AGENTS.md) | Assess PDB/mmCIF structure quality using wwPDB validation metrics and flag issues for curation |
| [`visualization-engineer`](profiles/visualization-engineer/AGENTS.md) | Create educational scientific visualizations for homodimer notebooks |

#### Advisory roles

| Name | Description |
|------|-------------|
| [`bioinformatics-data-engineer`](profiles/bioinformatics-data-engineer/AGENTS.md) | Make data sources, identifiers, file contracts, provenance, caching, and reproducibility explicit |
| [`biophysical-assay-scientist`](profiles/biophysical-assay-scientist/AGENTS.md) | Review binding, stability, and oligomerization assumptions against assay evidence (SPR, ITC, DSF, MST, SEC-MALS) |
| [`computational-structural-biologist`](profiles/computational-structural-biologist/AGENTS.md) | Assess structural-biology assumptions, residue/chain logic, confidence interpretation, and biological overclaim risk |
| [`enzymologist`](profiles/enzymologist/AGENTS.md) | Review enzyme-specific notebooks for kinetics, active-site logic, substrate/product context, and catalysis |
| [`evaluation-benchmarking-specialist`](profiles/evaluation-benchmarking-specialist/AGENTS.md) | Stress-test metrics, baselines, tolerances, fixtures, leakage, and validation evidence |
| [`machine-learning-engineer`](profiles/machine-learning-engineer/AGENTS.md) | Assess ML method choice, baselines, embeddings, model limits, and reproducibility |
| [`molecular-visualization-specialist`](profiles/molecular-visualization-specialist/AGENTS.md) | Design and review MolViewSpec/Mol* 3D protein visualization for InsightFold notebooks |
| [`project-manager`](profiles/project-manager/AGENTS.md) | Plan delivery and post-notebook integration work once a notebook has a reviewed spec or graduation status |
| [`protein-biochemist`](profiles/protein-biochemist/AGENTS.md) | Evaluate biochemical realism around protein mechanism, stability, binding, and oligomerization |
| [`protein-design-scientist`](profiles/protein-design-scientist/AGENTS.md) | Evaluate whether a notebook is genuinely useful for protein design or engineering decisions |
| [`protein-purification-scientist`](profiles/protein-purification-scientist/AGENTS.md) | Assess construct, expression, purification, solubility, aggregation, and QC realism |
| [`scientific-product-manager`](profiles/scientific-product-manager/AGENTS.md) | Shape early concepts into scoped, user-grounded notebook products without premature implementation detail |
| [`scientific-software-engineer`](profiles/scientific-software-engineer/AGENTS.md) | Review notebook implementation quality, repository structure, execution reliability, and maintainability |
| [`technical-writer`](profiles/technical-writer/AGENTS.md) | Improve notebook pedagogy, README clarity, figure captions, limitations, and user-facing explanations |
| [`wet-lab-liaison`](profiles/wet-lab-liaison/AGENTS.md) | Check whether notebook claims and proposed outputs make sense to experimental scientists |

#### Development lifecycle

| Name | Description |
|------|-------------|
| [`advisory-orchestrator`](profiles/advisory-orchestrator/AGENTS.md) | Operating guide for assembling and running advisory agent panels |
| [`fixture-curator`](profiles/fixture-curator/AGENTS.md) | Select and document pinned fixtures for InsightFold notebooks |
| [`lifecycle-orchestrator`](profiles/lifecycle-orchestrator/AGENTS.md) | Support the project-wide notebook-driven development lifecycle across notebooks and biological domains |
| [`notebook-builder`](profiles/notebook-builder/AGENTS.md) | Build InsightFold notebooks from reviewed spec packs |
| [`notebook-reviewer`](profiles/notebook-reviewer/AGENTS.md) | Perform final qualitative review of InsightFold notebooks after execution validation |
| [`notebook-validator`](profiles/notebook-validator/AGENTS.md) | Validate that an InsightFold notebook executes and matches its spec, fixtures, and runtime constraints |
| [`spec-reviewer`](profiles/spec-reviewer/AGENTS.md) | Review InsightFold notebook spec packs before implementation starts |

## Installation

### skills (recommended)

Documentation for using the `skills` CLI can be found here: https://www.skills.sh/

```bash
# GitHub shorthand (owner/repo)
npx skills add vercel-labs/agent-skills

# Full GitHub URL
npx skills add https://github.com/vercel-labs/agent-skills

# Direct path to a skill in a repo
npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

# GitLab URL
npx skills add https://gitlab.com/org/repo

# Any git URL
npx skills add git@github.com:vercel-labs/agent-skills.git

# Local path
npx skills add ./my-local-skills
```

```bash
# Add a skill for Claude Code
npx skills add https://github.com/npechl/pdbe-bioskills/tree/main/skills/afdb-api-fetching -a claude-code

# Add a skill for Codex
npx skills add https://github.com/npechl/pdbe-bioskills/tree/main/skills/afdb-api-fetching -a codex

# Pull the latest skills and profiles from GitHub
npx skills update
```

### pip

```bash
pip install git+https://github.com/PDBeurope/pdbe-bioskills.git
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
pdbe-bioskills install --claude concept-to-prd coding

# Install globally (available in all projects, goes to $HOME)
pdbe-bioskills install --all --claude --global

# Pull the latest skills and profiles from GitHub
pdbe-bioskills update
```

> **First run:** if no local cache exists, the CLI fetches `skills/` and `profiles/` from GitHub automatically before listing or installing. Run `pdbe-bioskills update` at any time to refresh to the latest version.

### pipx (isolated global install)

```bash
pipx install git+https://github.com/npechl/pdbe-bioskills.git
pdbe-bioskills list
```

<!-- ## Where files are installed

| Flag | Destination |
|------|-------------|
| `--claude` | Skills → `.claude/commands/<name>.md` · Agents → `.claude/agents/<name>.md` |
| `--codex` | Skills → `.codex/skills/<name>/` · Agents → `.codex/AGENTS.md` |
| `--global` | Prepends `$HOME` to the paths above |
| `--dir PATH` | Uses a custom base directory | -->

## Contributing

1. Open an issue describing the skill or agent profile you plan to add or change.
2. Fork the repository and create a branch from `main`.
3. Add or update a skill or agent profile (see file conventions below).
4. Open a pull request — the CLI auto-discovers items, so no registry update is needed.

### Adding a skill

Create `skills/<name>/SKILL.md` with YAML frontmatter:

```markdown
---
name: your-skill-name
description: One-line description of what the skill does
---

Skill instructions here...
```

### Adding an agent profile

Create `profiles/<name>/AGENTS.md` with YAML frontmatter:

```markdown
---
name: your-agent-name
description: One-line description of the agent
---

Agent instructions here...
```

## License

MIT
