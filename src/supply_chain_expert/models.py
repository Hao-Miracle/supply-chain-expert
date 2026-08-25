from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class WorkflowEvent:
    stage: str
    action: str
    actor: str
    summary: str
    data: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class GateDecision:
    gate: str
    status: str = "pending"
    reviewer: str = ""
    note: str = ""
    decided_at: str = ""

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
