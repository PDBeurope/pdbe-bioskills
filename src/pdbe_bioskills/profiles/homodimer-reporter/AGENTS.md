---
name: homodimer
description: Briefing document for the agent suite that recreates the AFDB homodimer diagnostic notebook.
---

# Agent Suite: Homodimer Diagnostic Notebook Recreation

**Briefing document for running the agent suite that recreates `notebooks/homodimer_diagnostic.ipynb`.**

---

## Overview

| Item | Detail |
|---|---|
| Target notebook | `notebooks/homodimer_diagnostic.ipynb` |
| Spec | `specs/homodimer_diagnostic_notebook_spec.md` |
| Primary reference | `$homodimer-confidence-scoring` in `.agents/skills/homodimer-confidence-scoring/SKILL.md` |
| Input | Single AFDB accession ID (e.g. `AF-0000000065889468`) |
| Output | Interactive Jupyter notebook with 7 sections, self-contained, Colab-compatible |

### Notebook sections

| # | Title | Key output |
|---|---|---|
| 1 | Setup and Data Loading | AFDB API fetch, mmCIF + PAE + pLDDT parsed into numpy arrays |
| 2 | Interface Detection | CB-CB contact mask, contact map plot, interface coverage bar |
| 3 | PAE Matrix Decomposition | Full heatmap + 4-panel quadrant overlay (one panel per score's PAE mask) |
| 4 | Score Computation and Decomposition | All 5 scores with intermediates, per-residue profile plots |
| 5 | Per-Residue pLDDT at Interface | pLDDT distribution (interface vs non-interface), annotated pLDDT profile |
| 6 | 3D Structure Visualisation | 4 MolViewSpec views (overview, pLDDT, ipSAE interface, disagreement) |
| 7 | Diagnostic Summary | Traffic-light HTML table, pairwise agreement matrix, plain-text diagnostic |

---

## Phase 1 — Exploration

**Agent:** `feature-dev:code-explorer`

| File | Why |
|---|---|
| `specs/homodimer_diagnostic_notebook_spec.md` | Full requirements, score formulas, acceptance criteria, API schemas |
| `.agents/skills/homodimer-confidence-scoring/SKILL.md` | Canonical formula implementations, PAE quadrant extraction pattern, AFDB API field names, edge-case table |
| `src/insightfold/interface.py` | CB-CB distance implementation the notebook mirrors (GLY→CA fallback, 8.0 Å cutoff) |
| `notebooks/analysis_template.ipynb` | Scaffold pattern: cell structure, import block, colour constants |

**Goal:** Produce a findings summary confirming which variables, constants, and patterns must be inherited verbatim from existing code vs. reimplemented in the notebook.

---

## Phase 2 — Architecture

**Agent:** `feature-dev:code-architect`

Produces a cell-by-cell blueprint covering:

- **Dependency graph** — the strict execution order that all downstream agents must respect:

  ```
  AFDB API fetch
    └── mmCIF parse → ch_coords, ch_resids, ch_resnames, ch_plddt (per chain)
    └── PAE JSON parse → pae_matrix, pae_AB, pae_BA, nA, nB
    └── pLDDT JSON parse → plddt_A, plddt_B
          └── dist_matrix (nA × nB) → contact_mask, interface_A, interface_B
                └── compute_pdockq, compute_pdockq2 (use dist_matrix + plddt)
                └── compute_iptm, compute_ipsae, compute_lis (use PAE quadrants)
                      └── scores dict → Section 7 summary
  ```

- **Variable namespace table** — which cell produces each variable, which cells consume it. Prevents handoff breaks when cells are implemented by separate agents.

- **MolViewSpec block flagged as optional** — Section 6 is wrapped in `try/except ImportError`. If `molviewspec` is unavailable the notebook degrades gracefully; Sections 1–5 and 7 must never depend on Section 6 state.

- **`COLORING_MODE` and `STRUCTURE_SOURCE` variables** set in Section 1, read by Section 6. Required for PDB model support (see [PDB Model Extension](#pdb-model-extension)).

---

## Phase 3 — Implementation

Three agents run in parallel once the architecture blueprint is finalised. All three are governed by `$homodimer-confidence-scoring`; formulas must not be inferred from training data.

### Agent A — Data + Parsing (Sections 1–2)

**Scope:** AFDB API call, mmCIF manual parser, PAE/pLDDT JSON parsing, interface detection, contact map plot, interface coverage bar.

Key constraints:
- No BioPython. mmCIF parsed by scanning `_atom_site` loop manually.
- Only `group_PDB == 'ATOM'`, only `label_atom_id in ('CA', 'CB')`, skip `label_seq_id` of `'.'`/`'?'`.
- PAE quadrant extraction must follow `$homodimer-confidence-scoring` (sort `chains` by `label_asym_id`, use `sequenceStart`/`sequenceEnd`).
- `ipywidgets` file-upload path for local files (offline mode) alongside the AFDB download path.

### Agent B — Scoring + Analysis (Sections 3–4–5)

**Scope:** Full PAE heatmap, 4-panel quadrant overlay, all 5 score functions (`compute_pdockq`, `compute_pdockq2`, `compute_lis`, `compute_iptm`, `compute_ipsae`), per-residue profile plots, pLDDT distribution and annotated profile.

Key constraints:
- All `compute_*` functions must return flat dicts including intermediates (masks, counts, per-residue arrays) — callers reuse them without recomputation.
- Numerical agreement with `ipsae.py` (DunbrackLab, v4 Jan 2026): tolerance ±0.001.
- pLDDT source for pDockQ/pDockQ2: B-factor column from mmCIF, sliced from `plddt_A`/`plddt_B` arrays produced in Section 1.
- Use `$homodimer-confidence-scoring` sigmoid constants verbatim; do not derive from spec prose.

**Supporting tool lookups:**
- `mcp__plugin_context7_context7__query-docs` — seaborn/matplotlib heatmap with masked overlays.
- `mcp__claude_ai_PubMed__get_article_metadata` — verify pDockQ2 sigmoid constants against Zhu et al. 2023 (Bioinformatics btad424).

### Agent C — Viz + Summary (Sections 6–7)

**Scope:** MolViewSpec 4 views, traffic-light HTML summary table, pairwise score agreement matrix, plain-text diagnostic heuristics.

**Primary skill for Section 6:** `$molviewspec-rendering` from `.agents/skills/molviewspec-rendering/SKILL.md`.

Key constraints:
- Section 6 entirely inside `try/except ImportError`.
- Traffic-light thresholds from `$homodimer-confidence-scoring` `THRESHOLDS` dict; do not use spec prose values.
- Diagnostic heuristic logic must cover all five cases from spec §7 (all-high, ipSAE-high/pDockQ-low, pDockQ-high/ipSAE-low, pDockQ2 diverges, LIS-high/ipSAE-low).

**Supporting tool lookup:**
- `mcp__plugin_context7_context7__query-docs` — MolViewSpec builder API (see [MolViewSpec Deep Dive](#molviewspec-skill--deep-dive)).

---

## Phase 4 — Review

**Agents:** `feature-dev:code-reviewer` then `simplify` skill

### `code-reviewer` checks

| Check | Detail |
|---|---|
| Formula correctness | Cross-reference every `compute_*` function against `$homodimer-confidence-scoring` primitives (`d0_func`, `ptm_func`, PAE cutoffs, sigmoid coefficients) |
| Variable handoff | Confirm each cell's inputs exist as outputs of a prior cell; no undefined references |
| Edge-case coverage | Verify the edge-case table in `$homodimer-confidence-scoring` is handled (zero contacts -> floor values, GLY -> CA, multi-model filter, etc.) |
| pDockQ2 sigmoid | Notebook uses `1.31 / (1 + exp(-0.075 * (x - 84.733)))` — verify against spec §5.7 and PubMed source |
| Section 6 isolation | Confirm no cell in Sections 1–5 or 7 imports from Section 6 scope |

### `simplify` skill

Final pass: remove redundant intermediate variables, tighten cell boundaries, ensure no cell exceeds a single logical operation.

---

## MolViewSpec Skill — Deep Dive

Use `$molviewspec-rendering` from `.agents/skills/molviewspec-rendering/SKILL.md` as the canonical MolViewSpec procedure. The notes below are historical homodimer-specific constraints and additional checks.

Section 6 is the highest-risk section: the `molviewspec` Python API is version-sensitive, sparsely documented in training data, and the per-residue coloring pattern has a performance cliff.

### Step 1 — Resolve library version

```
mcp__plugin_context7_context7__resolve-library-id(libraryName="molviewspec")
```

Identify the Context7 library ID and the version covered by docs. Cross-check against `pip show molviewspec` in the target environment. Flag any version delta before proceeding.

### Step 2 — Query builder API surface

```
mcp__plugin_context7_context7__query-docs(
  query="builder create_builder download parse model_structure component
         representation color ComponentExpression per-residue coloring"
)
```

Specific calls to verify:

| API call in current notebook | What to confirm |
|---|---|
| `mvs.create_builder()` | Still the correct entry point |
| `.parse(format='bcif')` | Accepted format strings (`'bcif'`, `'mmcif'`, `'cif'`) |
| `mvs.ComponentExpression(label_asym_id='A', beg_label_seq_id=r, end_label_seq_id=r)` | Field names — `beg_label_seq_id`/`end_label_seq_id` vs `seq_id`/`auth_seq_id` |
| `.representation(type='cartoon')` | Accepted `type` strings |
| `.color(color='#009688')` | Kwarg name — `color=` vs `hex=` |
| `builder.get_state().molstar_html()` | Method exists, returns embeddable HTML |

### Step 3 — Verify per-residue coloring strategy

Current notebook loops over each interface/chain residue and calls `.component()` once per residue. For View 2 (pLDDT, all residues in both chains) this is up to 344+ calls; for larger structures it becomes a performance and state-tree problem.

Query:
```
mcp__plugin_context7_context7__query-docs(
  query="annotation file per-residue color gradient ComponentAnnotation continuous coloring"
)
```

If annotation-file coloring is supported, use it for Views 2 and 3 (it collapses N calls into one JSON attachment). If not, keep the per-residue loop but add a size guard:

```python
if nA + nB > 500:
    print('Structure too large for per-residue coloring — using chain-level colors.')
    # fall back to chain-level View 1 style
```

### Step 4 — Verify inline display path

Preferred path (current notebook):
```python
html = state.molstar_html()
encoded = base64.b64encode(html.encode()).decode()
display(IFrame(src=f'data:text/html;base64,{encoded}', width=950, height=600))
```

If `molstar_html()` is absent or broken in the installed version, fall back to:
```python
mvsj = state.to_dict()  # or state.dumps()
url = f'https://molstar.org/viewer/?mvs-url=data:application/json;base64,{base64.b64encode(json.dumps(mvsj).encode()).decode()}'
display(HTML(f'<a href="{url}" target="_blank">Open in Mol* viewer</a>'))
```

The fallback always works but requires a browser and internet access — acceptable for Colab.

### Step 5 — Produce verified cell

The final cell must:
- Use confirmed field names and format strings from Steps 2–3
- Choose annotation-file or per-residue loop based on Step 3 finding, with size guard
- Use `molstar_html()` with fallback from Step 4
- Wrap the entire section in `try/except ImportError` (already present in current notebook — preserve it)

### Out of scope for the MolViewSpec skill

Score formula correctness, PAE array indexing, and pLDDT array slicing are verified by the `code-reviewer` in Phase 4. The MolViewSpec skill only owns the visualization layer: correct API calls, display method, and coloring strategy.

---

## PDB Model Extension

The notebook is currently AFDB-only. Supporting PDB experimental structures requires branching in the visualization layer and disabling PAE-dependent views.

### AFDB vs PDB comparison

| Aspect | AFDB homodimer | PDB structure |
|---|---|---|
| Per-residue confidence | pLDDT 0–100 (higher = better) | B-factor Å² (lower = more ordered; scale varies, typically 0–200+) |
| PAE matrix | Always present | Never present |
| Chain IDs | Always A and B | Arbitrary author-assigned labels |
| Multiple models | Filtered to model 1 | NMR ensembles: 10–100 models |
| Source URL | `bcifUrl` from AFDB API | `https://files.rcsb.org/download/{PDB_ID}.cif` |
| Homodimer guarantee | Enforced by AFDB filter | Not guaranteed — symmetric chains must be detected |

### Three coloring modes

| Mode | When to use | Normalization | Colormap |
|---|---|---|---|
| `plddt` | AFDB source, pLDDT in B-factor column | Fixed 4-band: >90 / 70–90 / 50–70 / <50 | Dark blue → light blue → yellow → orange |
| `bfactor` | PDB crystal structure | Percentile-robust: `np.percentile(b, [5, 95])` → 0–1; low B = ordered = blue | `coolwarm` or `viridis` (inverted relative to pLDDT) |
| `neutral` | NMR structure, or no confidence signal available | N/A | Chain A = `#009688` teal, chain B = `#FF7043` coral, interface = `#FFC107` amber |

B-factor percentile normalization:
```python
b_min, b_max = np.percentile(b_factors, [5, 95])  # robust to HETATM outliers
norm_b = np.clip((b_val - b_min) / (b_max - b_min), 0, 1)  # 0=ordered, 1=flexible
```

### Source detection

```python
def detect_structure_source(meta: dict, accession: str) -> str:
    if meta.get('paeDocUrl'):
        return 'afdb'
    if accession.upper().startswith('AF-'):
        return 'afdb'
    return 'pdb'

def detect_pdb_experiment_type(meta: dict) -> str:
    """Returns 'xray', 'nmr', or 'unknown'."""
    method = meta.get('experimentalMethod', '').lower()
    if 'nmr' in method:
        return 'nmr'
    if any(k in method for k in ('x-ray', 'electron', 'neutron')):
        return 'xray'
    return 'unknown'
```

### View availability by source

| View | AFDB | PDB (crystal) | PDB (NMR) |
|---|---|---|---|
| View 1: Chain overview (neutral) | Yes | Yes | Yes |
| View 2: Confidence mapping | pLDDT | B-factor | Skip (B-factors meaningless in NMR) |
| View 3: Interface ipSAE gradient | Yes | Skip — requires PAE | Skip |
| View 4: PAE/contact disagreement | Yes | Skip — requires PAE | Skip |

Views 3 and 4 skipped for PDB inputs with a printed notice, not an error.

### Blueprint changes required

In the architecture blueprint (Phase 2), the `code-architect` agent adds two variables set in Section 1 and read downstream:

```python
STRUCTURE_SOURCE = detect_structure_source(meta, ACCESSION_ID)
COLORING_MODE = (
    'plddt'   if STRUCTURE_SOURCE == 'afdb' else
    'bfactor' if detect_pdb_experiment_type(meta) == 'xray' else
    'neutral'
)
```

All Section 6 visualization cells branch on `COLORING_MODE`. The pLDDT parsing cell (currently unconditional) becomes:

```python
if STRUCTURE_SOURCE == 'afdb':
    plddt_A, plddt_B = ...  # parse from plddtDocUrl
else:
    plddt_A = ch_plddt[cA_id]  # B-factors already parsed from mmCIF
    plddt_B = ch_plddt[cB_id]
```

### Additional MolViewSpec agent query for PDB mode

```
mcp__plugin_context7_context7__query-docs(
  query="continuous gradient per-residue color normalization float annotation custom value"
)
```

Verifies whether MolViewSpec accepts a pre-normalized float to drive color interpolation natively, or whether the agent must pre-compute hex strings from the colormap for every residue — which is the current approach and works for both `plddt` and `bfactor` modes.
