# Procurement workflow contract

| Stage | Public output | Human responsibility |
|---|---|---|
| Requirement list | normalized line-item draft and missing-field report | confirm project and source list |
| Classification and standardization | proposed category, code, normalized specification, confidence and conflicts | Gate-1 confirmation |
| Cost estimation | explainable estimate range and evidence status | approve internal planning use |
| Supplier matching | candidate list with reasons and constraints | confirm eligible suppliers |
| RFQ and comparison | sanitized RFQ and comparable quote table | confirm external issue and exceptions |
| Negotiation and award | negotiation points and award recommendation | Gate-2 final award |
| Contract or order | draft terms and consistency checks | Gate-2 signature/order approval |
| Logistics | manual or verified-integration status updates | handle delays and exceptions |
| Acceptance | checklist and optional AI-assisted evidence extraction | Gate-3 final acceptance |
| Evaluation and feedback | proposed score, lessons and reusable facts | Gate-4 closeout and knowledge approval |

Every event should retain the project identifier, stage, action, actor, timestamp, concise evidence summary, gate status, and whether the result is a suggestion or confirmed fact. Organization-specific storage and retention remain private deployment concerns.
