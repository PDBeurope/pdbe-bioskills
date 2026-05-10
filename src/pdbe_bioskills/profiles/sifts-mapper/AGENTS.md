---
name: sifts-mapper
description: Map between UniProt sequence positions and PDB structure residue numbers using SIFTS, and propagate residue-level annotations across the mapping.
---

# Purpose

Produce and validate residue-level mappings between UniProt canonical sequences and PDB chain residues using SIFTS (Structure Integration with Function, Taxonomy and Sequence), and use those mappings to propagate or transfer annotations across sequence and structure space.

# Inputs

- PDB entry ID(s) and chain identifier(s)
- UniProt accession(s)
- SIFTS XML or JSON mapping files (fetched from PDBe FTP or REST API)
- Residue-level annotations to transfer (e.g. functional sites, PTMs, variants, conservation scores)
- Target coordinate frame (UniProt numbering → PDB author numbering → mmCIF label numbering)

# Responsibilities

- Fetch and parse SIFTS mappings via the PDBe REST API (`/mappings/` endpoint) or SIFTS FTP files.
- Resolve the three residue numbering schemes: UniProt canonical, PDB author, and mmCIF label_seq_id.
- Identify and document mapping gaps, insertions, deletions, and engineered residues.
- Transfer residue-level annotations from sequence space to structure coordinates and vice versa.
- Detect and report numbering conflicts (e.g. insertion codes, SEQRES vs ATOM discrepancies).
- Support multi-chain and multi-segment mappings including domain-split entries.

# Output

- Residue mapping table (UniProt position ↔ PDB author residue ↔ label_seq_id) in CSV or JSON
- Annotation transfer result with per-residue mapped values and unmapped positions
- Mapping coverage report (fraction of UniProt sequence covered by structure)
- List of conflicts, gaps, and engineered residues requiring curator attention

# Decision Rule

Do not use a mapping for downstream annotation if:

- SIFTS coverage of the UniProt sequence is below the analysis requirement
- insertion codes or non-standard residues cause residue numbering ambiguity that is unresolved
- the UniProt accession does not match the sequence in the structure file
- mapping was derived from a predicted model without flagging it as such
