<p align="center">
  <img src="assets/hero.svg" alt="Supply Chain Expert" width="100%" />
</p>

<p align="center">
  <a href="README.md">简体中文</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="README_EN.md">English</a>
</p>

<h3 align="center">Make procurement continuous, clear, and compounding.</h3>

<p align="center">
  One agent stays with the project from requirement intake to supplier evaluation.<br/>
  AI handles complexity. People own the decisions.
</p>

<br/>

## From list to outcome

<p align="center">
  <img src="assets/workflow.svg" alt="The complete intelligent procurement workflow" width="100%" />
</p>

Supply Chain Expert connects ten procurement stages into one project line. Every action retains its stage, evidence, state, and handoff. Four quality Gates place human confirmation exactly where it matters.

<table>
  <tr>
    <td width="25%"><strong>Gate 01</strong><br/><sub>List & classification</sub></td>
    <td width="25%"><strong>Gate 02</strong><br/><sub>Award & contract</sub></td>
    <td width="25%"><strong>Gate 03</strong><br/><sub>Delivery & acceptance</sub></td>
    <td width="25%"><strong>Gate 04</strong><br/><sub>Evaluation & closeout</sub></td>
  </tr>
</table>

## One core, four capabilities

<table>
  <tr>
    <td width="50%">
      <h3>01 · Workflow</h3>
      Ten-stage procurement orchestration with continuous project state and recoverable handoffs.
    </td>
    <td width="50%">
      <h3>02 · Intelligence</h3>
      Classification, standardization, cost analysis, supplier matching, and commercial guidance in one context.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>03 · Control</h3>
      Four Gates connect AI recommendations with accountable purchaser confirmation.
    </td>
    <td width="50%">
      <h3>04 · Memory</h3>
      Project facts, confirmed outcomes, and reusable lessons flow back into procurement knowledge.
    </td>
  </tr>
</table>

## Start now

```bash
git clone https://github.com/Hao-Miracle/supply-chain-expert.git
cd supply-chain-expert
python -m pip install -e .
```

Create your first procurement workflow:

```bash
supply-chain-expert \
  --project-id "DEMO-001" \
  --project-name "Campus network upgrade"
```

Or use Python:

```python
from supply_chain_expert import ProcurementWorkflow

flow = ProcurementWorkflow("DEMO-001", "Campus network upgrade")

flow.record("requirements", "import", "Requirement list imported")
flow.record(
    "classification_standardization",
    "classify",
    "Classification proposals prepared",
)

flow.approve_gate("gate1", reviewer="purchaser")
external_rfq = flow.prepare_external_rfq({
    "item": "24-port Gigabit Ethernet switch",
    "quantity": 2,
    "internal_cost": 100,
})
```

## The procurement intelligence foundation

| | Capability | Output |
|---:|---|---|
| 01 | Requirements | structured items, missing information, project context |
| 02 | Classification | category, code, normalized specification, confidence, evidence |
| 03 | Cost & market verification | cost analysis, price anomalies, verification evidence |
| 04 | Supplier & sourcing | supplier candidates, RFQ list, comparable quotations |
| 05 | Negotiation & award | negotiation points, consolidated analysis, award recommendation |
| 06 | Contract & delivery | contract/order draft, logistics state, delivery information |
| 07 | Acceptance & feedback | acceptance record, supplier evaluation, procurement knowledge |

Market prices enter the workflow as verification references with specification, brand, unit, tax, freight, region, source, and collection date. External RFQs retain only information intended for external sharing.

## Ready for agents

<table>
  <tr>
    <td width="50%">
      <a href="skills/supply-chain-expert/SKILL.md"><strong>supply-chain-expert</strong></a><br/>
      <sub>End-to-end procurement, quality Gates, commercial rules, and handoffs</sub>
    </td>
    <td width="50%">
      <a href="skills/procurement-device-classification/SKILL.md"><strong>procurement-device-classification</strong></a><br/>
      <sub>Explainable engineering-equipment classification and standardization</sub>
    </td>
  </tr>
</table>

The workflow contract lives in [`docs/WORKFLOW.md`](docs/WORKFLOW.md), with state defined in [`schemas/procurement-workflow.schema.json`](schemas/procurement-workflow.schema.json).

## Data boundary

The public repository is composed of generic code, public documentation, and synthetic examples. Organizational procurement data, runtime configuration, and private knowledge stay in the user's own environment. Privacy scanning is built in, together with commercial-field filtering for external RFQs.

```bash
python scripts/privacy_scan.py
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Build with us

Issues and pull requests are welcome across procurement workflows, industry taxonomies, data structures, and agent collaboration.

<p align="center">
  <sub>Apache-2.0 · Built for explainable procurement intelligence.</sub>
</p>
