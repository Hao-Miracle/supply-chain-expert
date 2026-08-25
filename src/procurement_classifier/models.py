from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Classification:
    system_category: str
    sub_category: str
    category_code: str
    confidence: float
    confidence_label: str
    source: str
    evidence: tuple[str, ...]
    alternatives: tuple[str, ...]
    needs_review: bool

    def to_dict(self) -> dict:
        result = asdict(self)
        result["evidence"] = list(self.evidence)
        result["alternatives"] = list(self.alternatives)
        return result
