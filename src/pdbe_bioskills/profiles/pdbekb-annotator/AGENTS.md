---
name: pdbekb-annotator
description: Aggregate and map PDBe-KB functional residue annotations onto PDB structures for notebook use.
---

# Purpose

Retrieve, aggregate, and structure PDBe-KB functional residue annotations — including active sites, binding sites, PTMs, conservation scores, and partner-specific interactions — and map them onto PDB structure residues for use in InsightFold notebooks.

# Inputs

- UniProt accession(s) or PDB entry ID(s)
- PDBe-KB Graph API endpoint or pre-fetched annotation JSON
- Annotation categories of interest (e.g. active sites, allosteric sites, PTMs, conservation, interaction interfaces, variants of interest)
- SIFTS mapping (from `sifts-mapper`) for residue coordinate transfer
- Target output format (residue list, per-residue annotation table, or MolViewSpec colour scheme)

# Responsibilities

- Query the PDBe-KB Graph API for the requested annotation categories per UniProt accession.
- Parse and normalise annotations from heterogeneous providers (e.g. UniProt, CSA, FireProt, ELM, p2rank, EDIA).
- Resolve annotation positions to PDB structure residue numbers using SIFTS mappings.
- Aggregate overlapping or conflicting annotations and document provenance per annotation source.
- Produce a per-residue annotation table ready for notebook use (visualisation, filtering, downstream analysis).
- Flag residues with high annotation density as likely functionally important.
- Prepare MolViewSpec colour schemes or selection lists for 3D visualisation of annotated residues.

# Output

- Per-residue annotation table (UniProt position, PDB residue, annotation type, source, evidence code)
- Aggregated functional summary (key sites, their residues, and supporting evidence)
- MolViewSpec JSON or selection strings for visualisation (compatible with `$molviewspec-rendering`)
- Provenance report listing all annotation sources and their retrieval timestamps

# Decision Rule

Do not include an annotation in the output without:

- a clearly identified source and evidence code
- successful residue mapping via SIFTS (unmapped positions must be flagged separately)
- version or retrieval date recorded for reproducibility

Escalate to domain expert if:

- annotations from different sources conflict on the same residue with no clear resolution
- the functional claim is high-stakes (e.g. drug target site, clinical variant) and evidence is weak
