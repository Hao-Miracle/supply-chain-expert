from __future__ import annotations

import argparse
import json

from .workflow import ProcurementWorkflow


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a safe synthetic procurement workflow snapshot")
    parser.add_argument("--project-id", default="DEMO-001")
    parser.add_argument("--project-name", default="Synthetic demonstration")
    args = parser.parse_args()

    workflow = ProcurementWorkflow(args.project_id, args.project_name)
    workflow.record("requirements", "import", "Synthetic requirement list imported")
    workflow.record("classification_standardization", "classify", "Classification proposals prepared")
    print(json.dumps(workflow.snapshot(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
