from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from uuid import uuid4

from .models import Classification


def build_audit_record(device_name: str, specification: str, result: Classification, *, engine_version: str = "open-v1", session_id: str | None = None) -> dict:
    record = {
        "sample_record_id": f"AICL-{uuid4().hex[:12]}",
        "session_id": session_id or "local-demo",
        "task_id": uuid4().hex,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "run_channel": "local",
        "original_device_name": device_name,
        "original_specification": specification,
        "normalized_device_name": device_name.strip().lower(),
        "normalized_specification": specification.strip().lower(),
        "ai_system_category": result.system_category,
        "ai_sub_category": result.sub_category,
        "ai_category_code": result.category_code,
        "ai_confidence": result.confidence,
        "confidence_label": result.confidence_label,
        "evidence_summary": list(result.evidence),
        "alternative_categories": list(result.alternatives),
        "has_candidate_conflict": bool(result.alternatives),
        "needs_human_review": result.needs_review,
        "human_final_category": None,
        "human_corrected": None,
        "gate1_status": "pending",
        "knowledge_base_written": False,
        "engine_version": engine_version,
    }
    canonical = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    record["record_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return record
