---
name: 3d-beacons-aggregator
description: Aggregate, compare, and rank structural models for a target protein from 3D-Beacons providers.
---

# Purpose

Query the 3D-Beacons API to retrieve all available structural models for a target protein, compare their coverage and confidence, and produce a ranked summary suitable for model selection in notebook workflows.

# Inputs

- UniProt accession
- 3D-Beacons API endpoint
- Model categories of interest (experimental, computational, template-based, ab initio)
- Intended use case for model selection (e.g. binding site analysis, comparative modelling seed, visualisation)
- Optional: sequence range of interest to filter models by coverage

# Responsibilities

- Query the 3D-Beacons hub API for all available models for the target UniProt accession.
- Retrieve model metadata: provider, method, sequence coverage, resolution or confidence score, model URL, and creation date.
- Normalise confidence metrics across providers (e.g. pLDDT for AFDB, QMEANDisCo for SWISS-MODEL, MolProbity score for experimental structures).
- Filter models to the sequence range of interest where specified.
- Rank models by coverage, confidence, and method reliability for the stated use case.
- Identify coverage gaps where no model is available for a region.
- Flag deprecated or superseded models.

# Output

- Ranked model summary table (provider, method, coverage range, confidence metric, URL)
- Coverage map across the UniProt canonical sequence showing modelled and unmodelled regions
- Recommended model(s) for the stated use case with justification
- List of coverage gaps and providers that do not cover the region of interest

# Decision Rule

Do not recommend a model as primary if:

- its sequence coverage does not include the region of interest
- confidence metrics are absent or below acceptable thresholds for the use case
- the model is marked deprecated in the 3D-Beacons registry
- the retrieval timestamp is more than 90 days old for use cases where currency matters
