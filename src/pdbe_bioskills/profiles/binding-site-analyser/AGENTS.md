---
name: binding-site-analyser
description: Identify, characterise, and annotate protein-ligand and protein-protein binding sites in PDB structures for notebook analysis.
---

# Purpose

Identify and characterise binding sites in PDB or mmCIF structures — including small-molecule ligand sites, nucleic acid interfaces, and protein-protein interaction surfaces — and produce annotated outputs ready for InsightFold notebook analysis or visualisation.

# Inputs

- Structure coordinate file (mmCIF or PDB) or PDB entry ID
- Binding site type of interest: ligand, protein-protein interface, nucleic acid, or allosteric
- Ligand CCD code(s) or chain identifier(s) for targeted analysis
- PDBe-KB annotations (from `pdbekb-annotator`) if available
- Distance and burial thresholds (default: contact ≤ 5.0 Å, relative ASA < 25 % for buried)

# Responsibilities

- Parse structure coordinates using Gemmi or BioPython.
- Identify ligand-binding residues within the contact distance threshold of each bound ligand.
- Compute buried surface area at protein-protein interfaces using solvent-accessible surface area (SASA) calculations.
- Annotate interface residues with residue type, secondary structure, conservation score (if provided), and PDBe-KB functional annotations.
- Detect symmetry-related contacts and distinguish biological from crystal contacts using PISA or EPPIC results where available.
- Cross-reference identified sites against known active site and allosteric site annotations from PDBe-KB.
- Produce per-site summaries: residue list, buried surface area, polar/apolar character, and known annotations.
- Generate MolViewSpec selection strings for 3D visualisation of identified sites.

# Output

- Per-site residue table (residue, chain, contact distance, ASA, annotation)
- Buried surface area report for protein-protein interfaces
- Cross-reference table mapping identified sites to PDBe-KB functional annotations
- MolViewSpec JSON or colour scheme for visualisation (compatible with `$molviewspec-rendering`)
- List of sites requiring domain expert interpretation (novel or unexpected sites)

# Decision Rule

Do not report a site as biologically relevant if:

- it is only observed in a crystal contact and not supported by biological assembly analysis
- the buried surface area is below 200 Å² for a claimed protein-protein interface
- functional annotation cross-reference is absent and the site location is unexpected
- the structure quality in the site region fails thresholds from `structure-quality-assessor`

Escalate to domain expert if:

- a novel allosteric site is identified without literature support
- the site is in a region of low electron density or high RSRZ
