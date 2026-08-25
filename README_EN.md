# Supply Chain Expert

[简体中文](README.md) | [English](README_EN.md)

A privacy-conscious, explainable procurement agent with accountable human approval. It covers the complete procurement loop from requirement intake to supplier evaluation and procurement-data feedback. Equipment classification and standardization are one stage of the workflow, not the whole product.

```text
Requirement list -> Classification and standardization -> Cost estimation
-> Supplier matching -> RFQ and quote comparison -> Negotiation and award
-> Contract or purchase order -> Logistics tracking -> Delivery acceptance
-> Supplier evaluation and procurement-data feedback
```

Four human quality gates control the workflow: Gate-1 confirms the list and classification, Gate-2 confirms the award and contract, Gate-3 confirms acceptance, and Gate-4 confirms evaluation and closeout. AI prepares, checks, and recommends; accountable purchasers decide.

## Project scope

This public repository contains generic procurement orchestration, business safeguards, an equipment-classification component, audit schemas, synthetic examples, and Agent Skills. It does not contain real procurement lists, suppliers, quotations, contracts, conversation logs, account configuration, or any organization-specific, human-confirmed knowledge base.

```text
Public generic framework + private user data and configuration + human Gate approval = deployable procurement workflow
```

ERP integration, ERP receiving, sales-order matching, purchase-sales matching, and finance pre-posting are outside this project. Logistics integrations and image-based acceptance OCR are extension points and must not be described as automated until verified in a real deployment.

## Quick start

```bash
python -m pip install -e .
procurement-classify --name "24-port Gigabit Ethernet switch" --spec "24GE+4SFP"
supply-chain-expert --project-id "DEMO-001" --project-name "Synthetic demonstration"
```

You can also run it without installing the package:

```bash
PYTHONPATH=src python -m procurement_classifier.cli --name "network video recorder" --spec "32-channel, 8-bay"
```

Classification rules, supplier recommendations, award proposals, contract drafts, and acceptance assistance do not replace accountable human decisions. Only history explicitly confirmed by the user in a private environment may be treated as a stable reusable reference.

## Key safeguards

- External RFQs exclude internal cost, target price, and other suppliers' quotations.
- Market-price databases are for verification reference only; they do not directly determine cost, target, transaction price, or supplier selection.
- Market references must include specification, brand, unit, tax, freight, region, source, and collection date. Incomplete records require human verification.
- New classifications require Gate-1; award and contract require Gate-2; acceptance requires Gate-3; evaluation and feedback require Gate-4.

## Repository contents

- `src/supply_chain_expert/`: full workflow orchestration, Gates, and safeguards.
- `src/procurement_classifier/`: equipment-classification and audit component.
- `skills/supply-chain-expert/`: end-to-end procurement Agent Skill.
- `skills/procurement-device-classification/`: equipment-classification sub-skill.
- `docs/WORKFLOW.md`: workflow, Gates, and capability boundaries.
- `schemas/ai-classification-audit.schema.json`: 24-field AI execution audit schema.
- `schemas/procurement-workflow.schema.json`: full procurement-workflow snapshot schema.
- `examples/`: fully synthetic demonstration records.
- `tests/`: tests for classification, human review, and audit hashing.
- `docs/SECURITY_AND_DATA.md`: privacy and publication boundaries.

## Accuracy statement

This project does not promise a fixed automatic accuracy rate for unknown equipment, and workflow coverage does not imply that every real integration is production-ready. Classification accuracy must be measured against an independent, human-confirmed test set that was not used to develop the rules. New equipment, conflicting candidates, and incomplete information should be routed to human review.

## Pre-release privacy checks

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

Passing the automated privacy scan is necessary but not sufficient for publication. The complete Git file and diff list must still be reviewed manually.

## License

The code is licensed under the Apache License 2.0. All example data is synthetic and provided solely for demonstration. Users are responsible for verifying the origin, authorization, privacy, and regulatory compliance of their own business data.
