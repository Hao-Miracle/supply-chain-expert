from __future__ import annotations

from typing import Any, Mapping


INTERNAL_PRICE_FIELDS = {
    "internal_cost",
    "cost_price",
    "target_price",
    "other_supplier_quote",
    "内部成本价",
    "目标价",
    "其他供应商报价",
}

MARKET_REFERENCE_REQUIRED_FIELDS = {
    "model_spec",
    "brand",
    "unit",
    "tax_rate",
    "freight",
    "region",
    "source",
    "collected_at",
}


def sanitize_external_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Recursively remove internal commercial fields before an RFQ leaves the organization."""
    def clean(value: Any) -> Any:
        if isinstance(value, Mapping):
            return {key: clean(item) for key, item in value.items() if str(key).lower() not in INTERNAL_PRICE_FIELDS}
        if isinstance(value, list):
            return [clean(item) for item in value]
        return value

    return clean(payload)


def validate_market_reference(record: Mapping[str, Any]) -> tuple[bool, list[str]]:
    """Validate a market-price reference without treating it as a decision price."""
    missing = sorted(field for field in MARKET_REFERENCE_REQUIRED_FIELDS if record.get(field) in (None, ""))
    return not missing, missing


def market_reference_notice() -> str:
    return "仅供核验参考 / For verification reference only"
