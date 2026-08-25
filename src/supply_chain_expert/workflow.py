from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from .models import GateDecision, WorkflowEvent
from .policies import sanitize_external_payload, validate_market_reference


STAGES = (
    "requirements",
    "classification_standardization",
    "cost_estimation",
    "supplier_matching",
    "rfq_comparison",
    "negotiation_award",
    "contract_order",
    "logistics",
    "acceptance",
    "supplier_evaluation_feedback",
)

GATE_REQUIREMENTS = {
    "cost_estimation": "gate1",
    "supplier_matching": "gate1",
    "rfq_comparison": "gate1",
    "contract_order": "gate2",
    "logistics": "gate2",
    "supplier_evaluation_feedback": "gate3",
}

GATE_LABELS = {
    "gate1": "清单与分类确认 / list and classification review",
    "gate2": "定标与合同确认 / award and contract review",
    "gate3": "到货验收确认 / acceptance review",
    "gate4": "项目收尾确认 / closeout review",
}

GATE_MIN_STAGE = {
    "gate1": "classification_standardization",
    "gate2": "negotiation_award",
    "gate3": "acceptance",
    "gate4": "supplier_evaluation_feedback",
}


class WorkflowError(ValueError):
    pass


class ProcurementWorkflow:
    """A vendor-neutral, in-memory procurement workflow with explicit human gates."""

    def __init__(self, project_id: str, project_name: str = ""):
        if not project_id.strip():
            raise WorkflowError("project_id is required")
        self.project_id = project_id
        self.project_name = project_name
        self.current_stage = STAGES[0]
        self.gates = {gate: GateDecision(gate) for gate in GATE_LABELS}
        self.events: list[WorkflowEvent] = []
        self.market_references: list[dict[str, Any]] = []

    def record(self, stage: str, action: str, summary: str, data: Mapping[str, Any] | None = None, actor: str = "agent") -> WorkflowEvent:
        if stage not in STAGES:
            raise WorkflowError(f"unknown stage: {stage}")
        required_gate = GATE_REQUIREMENTS.get(stage)
        if required_gate and self.gates[required_gate].status != "approved":
            raise WorkflowError(f"{required_gate} approval required before {stage}")
        target_index = STAGES.index(stage)
        current_index = STAGES.index(self.current_stage)
        if target_index < current_index:
            raise WorkflowError("workflow cannot silently move backwards")
        if target_index > current_index + 1:
            raise WorkflowError("workflow cannot silently skip stages")
        event = WorkflowEvent(stage, action, actor, summary, dict(data or {}))
        self.events.append(event)
        self.current_stage = stage
        return event

    def approve_gate(self, gate: str, reviewer: str, note: str = "") -> GateDecision:
        if gate not in self.gates:
            raise WorkflowError(f"unknown gate: {gate}")
        if not reviewer.strip():
            raise WorkflowError("human reviewer is required")
        if STAGES.index(self.current_stage) < STAGES.index(GATE_MIN_STAGE[gate]):
            raise WorkflowError(f"{gate} cannot be approved before {GATE_MIN_STAGE[gate]}")
        decision = self.gates[gate]
        decision.status = "approved"
        decision.reviewer = reviewer
        decision.note = note
        decision.decided_at = datetime.now(timezone.utc).isoformat()
        return decision

    def prepare_external_rfq(self, payload: Mapping[str, Any]) -> dict[str, Any]:
        if self.gates["gate1"].status != "approved":
            raise WorkflowError("gate1 approval required before external RFQ")
        return sanitize_external_payload(payload)

    def add_market_reference(self, record: Mapping[str, Any]) -> dict[str, Any]:
        valid, missing = validate_market_reference(record)
        stored = dict(record)
        stored["usage"] = "verification_only"
        stored["decision_authority"] = False
        stored["status"] = "reference" if valid and record.get("stale") is not True else "manual_verification_required"
        stored["missing_fields"] = missing
        self.market_references.append(stored)
        return stored

    def snapshot(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "current_stage": self.current_stage,
            "stages": list(STAGES),
            "gates": {key: value.to_dict() for key, value in self.gates.items()},
            "events": [event.to_dict() for event in self.events],
            "market_references": list(self.market_references),
            "erp_in_scope": False,
        }
