import unittest

from procurement_classifier import ClassificationEngine


class EngineTests(unittest.TestCase):
    def test_switch_is_explainable_and_requires_review(self):
        result = ClassificationEngine().classify("24口千兆交换机", "24GE+4SFP")
        self.assertEqual(result.sub_category, "交换机")
        self.assertEqual(result.category_code, "02-01")
        self.assertEqual(result.evidence, ("rule:network-switch",))
        self.assertTrue(result.needs_review)

    def test_non_item_is_not_forced_into_other(self):
        result = ClassificationEngine().classify("合计")
        self.assertEqual(result.sub_category, "")
        self.assertTrue(result.needs_review)

    def test_reviewed_history_can_be_reused(self):
        result = ClassificationEngine({"磁力锁|": "门禁控制"}).classify("磁力锁")
        self.assertEqual(result.source, "reviewed-history")
        self.assertEqual(result.confidence, 1.0)
        self.assertFalse(result.needs_review)


if __name__ == "__main__":
    unittest.main()
