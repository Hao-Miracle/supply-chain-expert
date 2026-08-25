import argparse
import json

from procurement_classifier import ClassificationEngine


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--spec", default="")
    parser.add_argument("--remark", default="")
    args = parser.parse_args()
    result = ClassificationEngine().classify(args.name, args.spec, args.remark)
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
