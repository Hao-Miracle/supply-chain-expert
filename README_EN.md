# Supply Chain Expert

[简体中文](README.md) | [English](README_EN.md)

An explainable procurement agent. It currently starts with equipment classification and standardization for engineering and IT integration procurement: it normalizes non-standard equipment names and returns the system category, detailed category, code, confidence, reasoning, and conflicting candidates. New or uncertain equipment is routed to human review instead of being silently forced into a category.

## Project scope

This public repository contains a general classification framework, baseline rules, an audit-data schema, and an Agent Skill example. It does not contain real procurement lists, suppliers, quotations, contracts, conversation logs, account configuration, or any organization-specific, human-confirmed knowledge base.

```text
Equipment name/specification/notes -> normalization -> rule candidates -> explainable classification proposal -> Gate-1 human confirmation -> private organizational knowledge base
```

## Quick start

```bash
python -m pip install -e .
procurement-classify --name "24-port Gigabit Ethernet switch" --spec "24GE+4SFP"
```

You can also run it without installing the package:

```bash
PYTHONPATH=src python -m procurement_classifier.cli --name "network video recorder" --spec "32-channel, 8-bay"
```

Rule-based results require human review by default. Only human-confirmed history explicitly imported by the user in a private environment may be treated as a stable reusable reference.

## Repository contents

- `src/procurement_classifier/`: generic classification and audit core.
- `skills/procurement-device-classification/`: Agent Skill.
- `schemas/ai-classification-audit.schema.json`: 24-field AI execution audit schema.
- `examples/`: fully synthetic demonstration records.
- `tests/`: tests for classification, human review, and audit hashing.
- `docs/SECURITY_AND_DATA.md`: privacy and publication boundaries.

## Accuracy statement

This project does not promise a fixed automatic accuracy rate for unknown equipment. Accuracy must be measured against an independent, human-confirmed test set that was not used to develop the rules. New equipment, conflicting candidates, and incomplete information should be routed to human review.

## Pre-release privacy checks

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

Passing the automated privacy scan is necessary but not sufficient for publication. The complete Git file and diff list must still be reviewed manually.

## License

The code is licensed under the Apache License 2.0. All example data is synthetic and provided solely for demonstration. Users are responsible for verifying the origin, authorization, privacy, and regulatory compliance of their own business data.
