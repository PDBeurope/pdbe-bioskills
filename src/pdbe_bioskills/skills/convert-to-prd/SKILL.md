---
name: convert-to-prd
description: Convert raw summary and decisions capture content into a structured Life Sciences / Bioinformatics / Research Platforms Product Requirements Document (PRD) template by using the provided PRD structure template (assets/PRD-TEMPLATE.md) and mapping guidelines.
---

# PRD Conversion Skill

## Purpose
- Accept input text from summary templates like `Summary-Decisions_Capture-prompt_template bond type.txt`.
- Produce a full markdown PRD document using the exact PRD structure requested.
- Preserve key information while mapping it into the PRD sections.

## Instructions
1. Read the input summary and identify key details for each PRD section.
2. Use the provided PRD template structure exactly, including headings, tables, and numbered sections.
3. Populate fields with extracted values when available. If a field cannot be inferred, leave it blank or use a placeholder.
4. Convert bullets, statements, and decisions into concise PRD content.
5. Ensure the final output begins with `# Product Requirements Document (PRD)` and includes all sections from `1. Document Overview` through `Appendix`.

## Output Requirements
- Output must be valid markdown.
- Keep tables and section headers exactly as shown in the template.
- Maintain the Life Sciences / Bioinformatics context and use appropriate domain language.
- Do not omit any numbered section or core subsection.

## Mapping Guidelines
- `Document Overview`: fill fields like Product Name, Version, Date, Author(s), Stakeholders, Status, Related Documents, Regulatory Scope.
- `Executive Summary`: extract a problem statement, product vision, and success criteria.
- `Background & Context`: place scientific and business context details into the respective subsections.
- `Existing Solutions`: summarize known solutions, strengths, and weaknesses.
- `Goals & Objectives`: translate objectives into product goals and non-goals.
- `Target Users` and `User Personas`: identify primary and secondary users from the summary.
- `Product Scope`: determine in-scope and out-of-scope items.
- `Use Cases`, `User Stories`, `Functional Requirements`, `Non-Functional Requirements`, `Data Requirements`, `Architecture Overview`, `Workflow & UX`, `AI / ML Components`, `Risks & Mitigations`, `Dependencies`, `Milestones & Timeline`, `KPIs & Success Metrics`, and `Open Questions`: fill based on extracted summary details or leave placeholders.

## Example
Input: raw planning notes, decisions, and feature descriptions.

Output: a complete PRD markdown document following the requested template.
