---
name: supply-chain-expert
description: Use when running an engineering-procurement project from requirement intake through classification, costing, supplier work, sourcing, contracting, logistics, acceptance, evaluation, and feedback with human approval gates and durable handoffs.
version: 1.0.0
author: Supply Chain Expert
license: Apache-2.0
metadata:
  hermes:
    tags: [procurement, workflow, sourcing, supply-chain, human-in-the-loop]
    related_skills: [procurement-device-classification]
---

# Supply Chain Expert

Identify the current project and stage, restore the latest approved state, then advance only the requested part of the procurement workflow. Keep recommendations separate from human decisions and record a concise handoff after material work.

## Workflow

1. Requirement list
2. Classification and standardization
3. Cost estimation
4. Supplier matching
5. RFQ and quote comparison
6. Negotiation and award recommendation
7. Contract or purchase order
8. Logistics tracking
9. Delivery acceptance
10. Supplier evaluation and procurement-data feedback

ERP integration, ERP receiving, sales-order matching, purchase-sales matching, and finance pre-posting are outside this workflow.

## Human gates

- Gate-1: confirm item name, category, specification, quantity, and external RFQ list.
- Gate-2: confirm supplier, price, tax, delivery date, award decision, and contract or order.
- Gate-3: confirm model, quantity, condition, and acceptance exceptions.
- Gate-4: confirm supplier evaluation, final transaction facts, open items, and project closeout.

Do not represent an AI recommendation as an approved decision. Do not write unconfirmed suggestions into a confirmed knowledge base.

## Commercial and privacy rules

- Never include internal cost, target price, or another supplier's quotation in an external RFQ.
- Treat market-price data as verification reference only. Check specification, brand, unit, tax, freight, region, source, and collection date; mark incomplete or stale records for human verification.
- Prefer approved transaction history, valid formal supplier quotations, and purchaser confirmation for key decisions.
- Use the minimum business data needed. Do not expose credentials, runtime profiles, logs, conversations, real contacts, contracts, bank data, private knowledge, or registration evidence.
- Describe logistics automation and image OCR as assisted or unverified unless their real integrations have been validated.

When the full repository is available, read [references/workflow-contract.md](references/workflow-contract.md) for its extended output contract. Use the repository's device-classification component for the classification stage when installed.
