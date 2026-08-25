# Intelligent procurement workflow

```text
Requirement list
  -> Classification and standardization
  -> Cost estimation
  -> Supplier matching
  -> RFQ and quote comparison
  -> Negotiation and award
  -> Contract or purchase order
  -> Logistics tracking
  -> Delivery acceptance
  -> Supplier evaluation and procurement-data feedback
```

The public project provides a workflow state model, policy safeguards, an explainable classification component, schemas, synthetic examples, and Agent Skills. It does not claim that every business integration is production-ready.

## Decision gates

| Gate | Required confirmation |
|---|---|
| Gate-1 | item name, category, specification, quantity, and RFQ list |
| Gate-2 | supplier, price, tax, delivery date, award, contract or order |
| Gate-3 | delivered model, quantity, condition, and exceptions |
| Gate-4 | supplier evaluation, final facts, open items, and closeout |

## Safety invariants

- AI prepares and recommends; accountable purchasers approve.
- External RFQs exclude internal cost, target price, and competing quotations.
- Market-price records are verification references, never automatic decision prices.
- ERP and finance-posting processes are not part of this project.
- Logistics integrations and acceptance OCR must be described according to verified deployment status.
