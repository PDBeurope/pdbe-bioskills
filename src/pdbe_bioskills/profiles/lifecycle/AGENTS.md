# InsightFold Lifecycle Agents

These agents support the project-wide notebook-driven development lifecycle. They are intentionally not tied to one notebook or one biological domain.

## Shared Principles

- Treat the spec pack as the implementation contract.
- Keep PRD, spec, notebook, validation, and review as separate lifecycle artifacts.
- Preserve scientific provenance: formulas, thresholds, data sources, and assumptions must be traceable.
- Require fixtures before claiming a notebook is runnable.
- Require data contracts for external APIs, uploaded files, and cached artifacts.
- Prefer small, inspectable notebook cells with explicit variable handoffs.
- Do not treat execution success as scientific approval.
- Route high-risk biological, clinical, or public-facing claims to human/domain review.

## Lifecycle Context

InsightFold follows the PDBe notebook-driven development lifecycle:

```text
idea -> triage -> scope -> notebook prototype -> instrumented beta -> graduation review
```

The graduation decision has three outcomes: integrate into AFDB/PDBe, keep as a standing notebook, or archive with rationale. Development harness, feedback, and documentation are supporting workstreams across the lifecycle.

## Lifecycle Chain

```text
$convert-to-prd
  -> $prd-to-notebook-spec
  -> spec-reviewer + $notebook-spec-review
  -> fixture-curator + $fixture-selection
  -> notebook-builder + $notebook-from-spec
  -> notebook-validator + $notebook-execution-validation
  -> notebook-reviewer + $notebook-review
```

## Artifact Expectations

Each notebook feature should converge toward:

```text
specs/<feature>/
  requirements.md
  notebook-design.md
  tasks.md
  validation.md
  docs-plan.md
  fixture-manifest.md
  data-contracts.md
notebooks/<feature>.ipynb
```

Flat `specs/<feature>_notebook_spec.md` files are acceptable for small prototypes if they contain equivalent sections.

## Human Review Gates

Ask for human/domain review when:

- fixture representativeness is uncertain
- biological interpretation is judgment-heavy
- formulas, thresholds, or cutoffs are not clearly sourced
- RUO/clinical framing matters
- beta or public AFDB/PDBe exposure is being considered
- a graduation decision is requested
