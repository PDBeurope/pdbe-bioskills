---
name: afdb-api-fetching
description: This skill handles retrieving structural and confidence data for homodimers from the AFDB API, including mmCIF files, PAE matrices, and pLDDT scores, ensuring data integrity and chain ordering.
---

# Goal

Fetch homodimer data from the AlphaFold Database API.

# Inputs

AFDB accession ID.

# Workflow

1. Call:
https://alphafold.ebi.ac.uk/api/prediction/{accession_id}

2. Parse returned JSON.

3. Extract:
- cifUrl
- paeDocUrl
- plddtDocUrl
- sequence
- UniProt accession

4. Download:
- mmCIF
- PAE JSON
- confidence JSON

5. Validate response structure.

# Requirements

- use requests
- handle HTTP failures
- validate JSON schema
- preserve chain ordering

# Dependencies

- requests library for HTTP calls

# Outputs

- parsed metadata
- structure content
- PAE matrix
- pLDDT arrays