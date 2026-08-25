---
name: procurement-device-classification
description: Classify engineering-procurement equipment descriptions into explainable system and subcategory suggestions, identify ambiguity, and prepare results for human Gate-1 review. Use for equipment-list normalization or classification; do not use it to select suppliers, set prices, or approve procurement decisions.
---

# Procurement Device Classification

Normalize the equipment name, specification and relevant remark, then call `scripts/classify_device.py` or an equivalent installed interface. The `procurement_classifier` package from the repository root must be installed or available on `PYTHONPATH`. Return the proposed system category, subcategory, code, confidence, evidence, alternatives and whether human review is required.

## Required behavior

- Treat rule output as a suggestion. New or ambiguous equipment must remain pending until a responsible person confirms it.
- Never describe “every row has a label” as classification accuracy.
- Do not infer a class only from supplier identity, price or brand.
- Do not silently choose the first candidate when equally strong rules conflict.
- Do not write a suggestion into a confirmed knowledge base without explicit Gate-1 approval.
- Keep supplier selection, pricing, contracting and acceptance outside this skill.

## Data safety

Operate on the minimum fields needed for classification. Do not expose customer names, supplier contacts, quotations, costs, credentials, runtime profiles, session logs or private correction histories.

For the public taxonomy and audit fields, read [references/classification-contract.md](references/classification-contract.md).
