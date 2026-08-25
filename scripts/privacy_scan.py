from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_FILES = {Path(__file__).resolve(), ROOT / "docs" / "SECURITY_AND_DATA.md"}
FORBIDDEN_NAMES = {".env", "auth.json", "config.yaml", "state.db", "response_store.db"}
FORBIDDEN_DIRS = {"raw", "private", "logs", "sessions", "memories", "outputs"}
FORBIDDEN_SUFFIXES = {".doc", ".docx", ".pdf", ".xls", ".xlsx", ".db", ".wal"}
APPROVED_PUBLIC_EMAILS = {"miracle.hao2023@gmail.com"}
CONTENT_RULES = {
    "credential assignment": re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|passwd|secret)\s*[:=]\s*['\"][^'\"]{6,}"),
    "mainland mobile number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
}

private_markers = [value for value in os.getenv("PROCUREMENT_PRIVACY_MARKERS", "").split("||") if value]
if private_markers:
    CONTENT_RULES["private business marker"] = re.compile("|".join(map(re.escape, private_markers)))


def main() -> int:
    findings: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.resolve() in SKIP_FILES or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES or any(part in FORBIDDEN_DIRS for part in relative.parts) or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"forbidden path: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"unreviewed binary: {relative}")
            continue
        for label, pattern in CONTENT_RULES.items():
            scanned_text = text
            if label == "email address":
                for approved_email in APPROVED_PUBLIC_EMAILS:
                    scanned_text = scanned_text.replace(approved_email, "[approved-public-email]")
            if pattern.search(scanned_text):
                findings.append(f"{label}: {relative}")

    if findings:
        print("PRIVACY SCAN FAILED")
        print("\n".join(findings))
        return 1
    print("PRIVACY SCAN PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
