import argparse
import json

from .audit import build_audit_record
from .engine import ClassificationEngine


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify a procurement equipment description")
    parser.add_argument("--name", required=True)
    parser.add_argument("--spec", default="")
    parser.add_argument("--remark", default="")
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    result = ClassificationEngine().classify(args.name, args.spec, args.remark)
    payload = build_audit_record(args.name, args.spec, result) if args.audit else result.to_dict()
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
