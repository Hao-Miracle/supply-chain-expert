import unittest

from procurement_classifier import ClassificationEngine
from procurement_classifier.audit import build_audit_record


class AuditTests(unittest.TestCase):
    def test_audit_record_has_24_fields_and_hash(self):
        result = ClassificationEngine().classify("网络硬盘录像机", "32路 8盘位")
        record = build_audit_record("网络硬盘录像机", "32路 8盘位", result)
        self.assertEqual(len(record), 24)
        self.assertEqual(len(record["record_sha256"]), 64)
        self.assertEqual(record["gate1_status"], "pending")
        self.assertFalse(record["knowledge_base_written"])


if __name__ == "__main__":
    unittest.main()
