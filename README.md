# pdbe-bioskills

A curated collection of skills and agent profiles, developed by PDBe team, for developing analyses and workflows of PDBe/structure datasets.

## Available items

### Skills

#### Domain specific

Skills for fetching, computing, and visualising PDBe/AFDB structural data.

| Name | Description |
|------|-------------|
| [`afdb-api-fetching`](src/pdbe_bioskills/skills/afdb-api-fetching/SKILL.md) | Retrieve structural and confidence data from the AFDB API, including mmCIF files, PAE matrices, and pLDDT scores |
| [`aggregated-interface-ingestion`](src/pdbe_bioskills/skills/aggregated-interface-ingestion/SKILL.md) | Build or validate the aggregated interface schema for a set of PDB complexes from chain correspondence data |
| [`homodimer-confidence-scoring`](src/pdbe_bioskills/skills/homodimer-confidence-scoring/SKILL.md) | Implement and review AlphaFold Database homodimer interface confidence scoring (PAE, ipTM, ipSAE, pDockQ, LIS) |
| [`ipsae-implementation`](src/pdbe_bioskills/skills/ipsae-implementation/SKILL.md) | Compute interface predicted TM-score (ipTM) and interface predicted aligned error (ipSAE) metrics |
| [`lis-implementation`](src/pdbe_bioskills/skills/lis-implementation/SKILL.md) | Compute the Local Interaction Score by averaging normalized low-PAE inter-chain interactions |
| [`molviewspec-rendering`](src/pdbe_bioskills/skills/molviewspec-rendering/SKILL.md) | Produce 3D structural views using MolViewSpec, including chain coloring, pLDDT overlays, and interface highlights |
| [`pae-visualization`](src/pdbe_bioskills/skills/pae-visualization/SKILL.md) | Create heatmaps and overlays for PAE matrices with annotations and color conventions |
| [`pdbe-llm-annotation-fetching`](src/pdbe_bioskills/skills/pdbe-llm-annotation-fetching/SKILL.md) | Fetch LLM-derived residue annotations from the PDBe LLM annotation REST API |
| [`pdockq-implementation`](src/pdbe_bioskills/skills/pdockq-implementation/SKILL.md) | Calculate pDockQ and pDockQ2 scores based on interface contacts and PAE-derived probabilities |
| [`sifts-sequence-mapping`](src/pdbe_bioskills/skills/sifts-sequence-mapping/SKILL.md) | Map PDBx/mmCIF structure sequences to UniProtKB or a custom FASTA using the SIFTS pipeline |
| [`validation-against-reference`](src/pdbe_bioskills/skills/validation-against-reference/SKILL.md) | Compare computed metrics against reference implementations, ensuring numerical accuracy within tolerance |

#### Development lifecycle

Skills for planning, building, and reviewing LLM-assisted Jupyter notebook workflows.

| Name | Description |
|------|-------------|
| [`concept-to-prd`](src/pdbe_bioskills/skills/concept-to-prd/SKILL.md) | Convert scoped InsightFold concepts or advisory-panel notes into a structured life-sciences PRD |
| [`convert-to-prd`](src/pdbe_bioskills/skills/convert-to-prd/SKILL.md) | Convert rough notebook ideas or planning notes into a structured life-sciences PRD |
| [`fixture-selection`](src/pdbe_bioskills/skills/fixture-selection/SKILL.md) | Select and document pinned fixtures for InsightFold notebooks |
| [`idea-scoping-interview`](src/pdbe_bioskills/skills/idea-scoping-interview/SKILL.md) | Guide early concept discovery before PRD writing via a structured scoping interview |
| [`notebook-assembly`](src/pdbe_bioskills/skills/notebook-assembly/SKILL.md) | Compile modular sections into a cohesive Jupyter notebook with sequential execution and validation outputs |
| [`notebook-execution-validation`](src/pdbe_bioskills/skills/notebook-execution-validation/SKILL.md) | Validate InsightFold notebooks against their spec, fixtures, data contracts, and runtime constraints |
| [`notebook-from-spec`](src/pdbe_bioskills/skills/notebook-from-spec/SKILL.md) | Build an InsightFold Jupyter notebook from a reviewed spec pack |
| [`notebook-review`](src/pdbe_bioskills/skills/notebook-review/SKILL.md) | Perform final qualitative review of InsightFold notebooks for scientific correctness and reproducibility |
| [`notebook-spec-review`](src/pdbe_bioskills/skills/notebook-spec-review/SKILL.md) | Review InsightFold notebook spec packs before implementation starts |
| [`notebook-ux-contract`](src/pdbe_bioskills/skills/notebook-ux-contract/SKILL.md) | Define the first runnable user workflow for a notebook before fixture selection and implementation |
| [`prd-notebook-generation`](src/pdbe_bioskills/skills/prd-notebook-generation/SKILL.md) | Generate a notebook from the spec using agent workflows |
| [`prd-to-notebook-spec`](src/pdbe_bioskills/skills/prd-to-notebook-spec/SKILL.md) | Convert an approved InsightFold PRD into an implementation-ready notebook spec pack |
| [`scoping-decision-capture`](src/pdbe_bioskills/skills/scoping-decision-capture/SKILL.md) | Convert scoping conversations or advisory-panel discussions into a structured decision capture |

### Agent profiles

#### Domain specific

Agents for structural analysis, data retrieval, and scientific interpretation.

| Name | Description |
|------|-------------|
| [`3d-beacons-aggregator`](src/pdbe_bioskills/profiles/3d-beacons-aggregator/AGENTS.md) | Aggregate, compare, and rank structural models for a target protein from 3D-Beacons providers |
| [`afdb-model-reviewer`](src/pdbe_bioskills/profiles/afdb-model-reviewer/AGENTS.md) | Review AlphaFold Database model confidence, applicability, and suitability for downstream analysis |
| [`binding-site-analyser`](src/pdbe_bioskills/profiles/binding-site-analyser/AGENTS.md) | Identify, characterise, and annotate protein-ligand and protein-protein binding sites in PDB structures |
| [`coding`](src/pdbe_bioskills/profiles/coding/AGENTS.md) | Software engineering and technical research assistant |
| [`deposition-reviewer`](src/pdbe_bioskills/profiles/deposition-reviewer/AGENTS.md) | Review macromolecular structure depositions for metadata completeness and PDB archive compliance |
| [`homodimer-orchestrator`](src/pdbe_bioskills/profiles/homodimer-orchestrator/AGENTS.md) | Coordinate development of the AFDB homodimer diagnostic notebook across specialized agents |
| [`homodimer-reporter`](src/pdbe_bioskills/profiles/homodimer-reporter/AGENTS.md) | Briefing document and agent suite for recreating the AFDB homodimer diagnostic notebook |
| [`pdbekb-annotator`](src/pdbe_bioskills/profiles/pdbekb-annotator/AGENTS.md) | Aggregate and map PDBe-KB functional residue annotations onto PDB structures for notebook use |
| [`scientific-python-engineer`](src/pdbe_bioskills/profiles/scientific-python-engineer/AGENTS.md) | Implement scientific Python code for homodimer diagnostic notebooks |
| [`sifts-mapper`](src/pdbe_bioskills/profiles/sifts-mapper/AGENTS.md) | Map between UniProt sequence positions and PDB structure residue numbers using SIFTS |
| [`structural-biologist`](src/pdbe_bioskills/profiles/structural-biologist/AGENTS.md) | Interpret AlphaFold confidence metrics and provide structural biology guidance |
| [`structure-quality-assessor`](src/pdbe_bioskills/profiles/structure-quality-assessor/AGENTS.md) | Assess PDB/mmCIF structure quality using wwPDB validation metrics and flag issues for curation |
| [`visualization-engineer`](src/pdbe_bioskills/profiles/visualization-engineer/AGENTS.md) | Create educational scientific visualizations for homodimer notebooks |

#### Advisory roles

Specialist advisors that challenge decisions from a domain viewpoint. Pair with lifecycle skills.

| Name | Description |
|------|-------------|
| [`bioinformatics-data-engineer`](src/pdbe_bioskills/profiles/bioinformatics-data-engineer/AGENTS.md) | Make data sources, identifiers, file contracts, provenance, caching, and reproducibility explicit |
| [`biophysical-assay-scientist`](src/pdbe_bioskills/profiles/biophysical-assay-scientist/AGENTS.md) | Review binding, stability, and oligomerization assumptions against assay evidence (SPR, ITC, DSF, MST, SEC-MALS) |
| [`computational-structural-biologist`](src/pdbe_bioskills/profiles/computational-structural-biologist/AGENTS.md) | Assess structural-biology assumptions, residue/chain logic, confidence interpretation, and biological overclaim risk |
| [`enzymologist`](src/pdbe_bioskills/profiles/enzymologist/AGENTS.md) | Review enzyme-specific notebooks for kinetics, active-site logic, substrate/product context, and catalysis |
| [`evaluation-benchmarking-specialist`](src/pdbe_bioskills/profiles/evaluation-benchmarking-specialist/AGENTS.md) | Stress-test metrics, baselines, tolerances, fixtures, leakage, and validation evidence |
| [`machine-learning-engineer`](src/pdbe_bioskills/profiles/machine-learning-engineer/AGENTS.md) | Assess ML method choice, baselines, embeddings, model limits, and reproducibility |
| [`molecular-visualization-specialist`](src/pdbe_bioskills/profiles/molecular-visualization-specialist/AGENTS.md) | Design and review MolViewSpec/Mol* 3D protein visualization for InsightFold notebooks |
| [`project-manager`](src/pdbe_bioskills/profiles/project-manager/AGENTS.md) | Plan delivery and post-notebook integration work once a notebook has a reviewed spec or graduation status |
| [`protein-biochemist`](src/pdbe_bioskills/profiles/protein-biochemist/AGENTS.md) | Evaluate biochemical realism around protein mechanism, stability, binding, and oligomerization |
| [`protein-design-scientist`](src/pdbe_bioskills/profiles/protein-design-scientist/AGENTS.md) | Evaluate whether a notebook is genuinely useful for protein design or engineering decisions |
| [`protein-purification-scientist`](src/pdbe_bioskills/profiles/protein-purification-scientist/AGENTS.md) | Assess construct, expression, purification, solubility, aggregation, and QC realism |
| [`scientific-product-manager`](src/pdbe_bioskills/profiles/scientific-product-manager/AGENTS.md) | Shape early concepts into scoped, user-grounded notebook products without premature implementation detail |
| [`scientific-software-engineer`](src/pdbe_bioskills/profiles/scientific-software-engineer/AGENTS.md) | Review notebook implementation quality, repository structure, execution reliability, and maintainability |
| [`technical-writer`](src/pdbe_bioskills/profiles/technical-writer/AGENTS.md) | Improve notebook pedagogy, README clarity, figure captions, limitations, and user-facing explanations |
| [`wet-lab-liaison`](src/pdbe_bioskills/profiles/wet-lab-liaison/AGENTS.md) | Check whether notebook claims and proposed outputs make sense to experimental scientists |

#### Development lifecycle

Agents that own specific stages of the notebook-driven development workflow.

| Name | Description |
|------|-------------|
| [`advisory-orchestrator`](src/pdbe_bioskills/profiles/advisory-orchestrator/AGENTS.md) | Operating guide for assembling and running advisory agent panels |
| [`fixture-curator`](src/pdbe_bioskills/profiles/fixture-curator/AGENTS.md) | Select and document pinned fixtures for InsightFold notebooks |
| [`lifecycle-orchestrator`](src/pdbe_bioskills/profiles/lifecycle-orchestrator/AGENTS.md) | Support the project-wide notebook-driven development lifecycle across notebooks and biological domains |
| [`notebook-builder`](src/pdbe_bioskills/profiles/notebook-builder/AGENTS.md) | Build InsightFold notebooks from reviewed spec packs |
| [`notebook-reviewer`](src/pdbe_bioskills/profiles/notebook-reviewer/AGENTS.md) | Perform final qualitative review of InsightFold notebooks after execution validation |
| [`notebook-validator`](src/pdbe_bioskills/profiles/notebook-validator/AGENTS.md) | Validate that an InsightFold notebook executes and matches its spec, fixtures, and runtime constraints |
| [`spec-reviewer`](src/pdbe_bioskills/profiles/spec-reviewer/AGENTS.md) | Review InsightFold notebook spec packs before implementation starts |

## Installation

### pip (recommended)

```bash
pip install git+https://github.com/npechl/pdbe-bioskills.git
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
pipx install git+https://github.com/npechl/pdbe-bioskills.git
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
