---
name: prd-notebook-generation
description: Orchestrate the full InsightFold lifecycle from an approved PRD to a validated, reviewed notebook. Use when the user wants end-to-end guidance on moving from a PRD through spec, fixtures, UX contract, implementation, validation, and final review without losing track of stage dependencies or quality gates.
---

# PRD To Notebook Generation

## Purpose

Walk the InsightFold lifecycle from an approved PRD to a validated, reviewed notebook. This skill orchestrates the constituent skills in the correct order, enforces quality gates between stages, and surfaces blockers before they cause rework downstream.

Use this skill when:

- a PRD has been approved and the user wants to know what to do next
- a team wants a checklist for the full notebook development pipeline
- an agent needs to coordinate multiple lifecycle steps in a single session

Do not use this skill to skip or compress individual stages. Each stage has its own skill; this skill tells you when and how to invoke them.

## Pipeline Overview

```
PRD (approved)
  └─ 1. $prd-to-notebook-spec     → spec pack
       └─ 2. $notebook-spec-review → pass / fail
            └─ 3. $notebook-ux-contract  → UX contract
                 └─ 4. $fixture-selection     → fixture manifest
                      └─ 5. $notebook-from-spec    → notebook
                           └─ 6. $notebook-execution-validation → validation report
                                └─ 7. $notebook-review           → review report
```

## Stage Descriptions

### Stage 1 — Spec Pack (`$prd-to-notebook-spec`)

**Input**: approved PRD at `prd/<feature-slug>.md`

**Gate before starting**:
- PRD status is `Approved`
- All blocking open questions are resolved
- Advisory panel review is complete if required by the PRD

**Run**: invoke `$prd-to-notebook-spec` to produce the full spec pack directory.

**Gate before proceeding**: spec pack contains all required documents:
- `requirements.md`
- `notebook-design.md`
- `cell-blueprint.md`
- `traceability-matrix.md`
- `tasks.md`
- `data-contracts.md`
- `docs-plan.md`
- `validation.md`

---

### Stage 2 — Spec Review (`$notebook-spec-review`)

**Input**: spec pack directory

**Gate before starting**: spec pack is complete (all documents from Stage 1 present)

**Run**: invoke `$notebook-spec-review` in `readiness` mode first, then `scientific` and `implementation` if readiness passes.

**Gate before proceeding**: review verdict is `pass` or `pass-with-assumptions`. Record all assumptions.

**On `fail`**: return to Stage 1, revise the spec pack, and re-run the review. Do not proceed to implementation.

---

### Stage 3 — UX Contract (`$notebook-ux-contract`)

**Input**: approved PRD, spec pack

**Gate before starting**: spec review verdict is `pass` or `pass-with-assumptions`

**Run**: invoke `$notebook-ux-contract` to define the user entry point, section storyboard, parameter contract, and UX acceptance criteria.

**Gate before proceeding**: UX contract defines:
- first runnable input cell
- primary biological question
- target user and explanation level
- fixture/example separation from the user flow

---

### Stage 4 — Fixture Selection (`$fixture-selection`)

**Input**: reviewed spec pack, UX contract, biological object, API endpoints

**Gate before starting**: UX contract is complete

**Run**: invoke `$fixture-selection` to produce the fixture manifest covering happy-path, edge-case, negative, and reference fixtures.

**Gate before proceeding**: fixture manifest includes at least one happy-path fixture with expected outputs. Negative fixtures are included if the spec requires failure-mode handling.

---

### Stage 5 — Notebook Implementation (`$notebook-from-spec`)

**Input**: spec pack, UX contract, fixture manifest

**Gate before starting**:
- spec review is `pass` or `pass-with-assumptions`
- UX contract is complete
- fixture manifest exists
- data contracts exist
- validation plan exists

**Run**: invoke `$notebook-from-spec` to implement the notebook section by section.

**Gate before proceeding**:
- notebook runs top-to-bottom after kernel restart with the happy-path fixture
- all mandatory spec requirements are implemented
- no unexplained magic constants or hidden state

---

### Stage 6 — Execution Validation (`$notebook-execution-validation`)

**Input**: notebook, spec pack, fixture manifest, data contracts, validation plan

**Gate before starting**: notebook passes the manual smoke test from Stage 5

**Run**: invoke `$notebook-execution-validation` in `full` mode.

**Gate before proceeding**: validation report shows all happy-path checks pass. Edge-case and negative fixture results match expected outcomes from the fixture manifest.

**On failure**: identify whether the failure is in the notebook, the fixture, or the spec. Fix at the appropriate layer and re-run validation.

---

### Stage 7 — Final Review (`$notebook-review`)

**Input**: notebook, spec pack, execution validation report, PRD

**Gate before starting**: execution validation report exists and all blocking issues are resolved

**Run**: invoke `$notebook-review` covering scientific correctness, reproducibility, pedagogy, visualization, and lifecycle readiness.

**Gate before completion**: review report verdict is `pass` or `pass-with-minor-revisions`. Address all `must-fix` findings before marking the notebook ready.

---

## Failure Mode Handling

| Failure | Stage | Action |
|---|---|---|
| Spec is incomplete | 1 | Identify missing spec documents, re-run `$prd-to-notebook-spec` |
| Spec review fails | 2 | Fix blocking findings in spec pack, re-run review |
| UX contract is ambiguous | 3 | Clarify primary user and entry point with stakeholder, re-run |
| No valid happy-path fixture | 4 | Check API availability, re-run `$fixture-selection` with fallback accessions |
| Notebook fails smoke test | 5 | Debug section by section, fix implementation, re-run |
| Validation report has failures | 6 | Fix notebook or fixture mismatch, re-run validation |
| Review finds must-fix issues | 7 | Apply fixes, re-run `$notebook-execution-validation`, then re-run review |

## Output

At the end of a successful pipeline run, return:

- notebook path and filename
- spec pack directory
- fixture manifest path
- execution validation report path
- review report path
- list of accepted assumptions
- list of open items deferred to a follow-up lifecycle stage
