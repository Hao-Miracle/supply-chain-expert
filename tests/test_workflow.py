import unittest

from supply_chain_expert import ProcurementWorkflow, WorkflowError


class WorkflowTests(unittest.TestCase):
    def test_workflow_cannot_skip_stages(self):
        flow = ProcurementWorkflow("DEMO-000")
        with self.assertRaises(WorkflowError):
            flow.record("supplier_matching", "match", "candidates prepared")

    def test_full_flow_requires_human_gates(self):
        flow = ProcurementWorkflow("DEMO-001")
        flow.record("requirements", "import", "requirements imported")
        flow.record("classification_standardization", "classify", "suggestions prepared")
        with self.assertRaises(WorkflowError):
            flow.record("cost_estimation", "estimate", "estimate prepared")

        flow.approve_gate("gate1", "human-reviewer")
        flow.record("cost_estimation", "estimate", "estimate prepared")
        flow.record("supplier_matching", "match", "candidates prepared")
        flow.record("rfq_comparison", "compare", "quotes compared")
        flow.record("negotiation_award", "recommend", "award proposal prepared")
        with self.assertRaises(WorkflowError):
            flow.record("contract_order", "draft", "contract drafted")

        flow.approve_gate("gate2", "human-reviewer")
        flow.record("contract_order", "draft", "contract drafted")
        flow.record("logistics", "update", "manual logistics update")
        flow.record("acceptance", "assist", "acceptance evidence prepared")
        flow.approve_gate("gate3", "human-reviewer")
        flow.record("supplier_evaluation_feedback", "evaluate", "evaluation prepared")
        flow.approve_gate("gate4", "human-reviewer")

        snapshot = flow.snapshot()
        self.assertEqual(len(snapshot["stages"]), 10)
        self.assertFalse(snapshot["erp_in_scope"])

    def test_external_rfq_removes_internal_prices(self):
        flow = ProcurementWorkflow("DEMO-002")
        flow.record("classification_standardization", "classify", "suggestions prepared")
        flow.approve_gate("gate1", "human-reviewer")
        rfq = flow.prepare_external_rfq({
            "item": "synthetic switch",
            "quantity": 2,
            "internal_cost": 100,
            "target_price": 120,
            "other_supplier_quote": 130,
            "lines": [{"item": "synthetic cable", "内部成本价": 10}],
        })
        self.assertEqual(rfq, {
            "item": "synthetic switch",
            "quantity": 2,
            "lines": [{"item": "synthetic cable"}],
        })

    def test_market_price_is_reference_only(self):
        flow = ProcurementWorkflow("DEMO-003")
        reference = flow.add_market_reference({"source": "synthetic public catalog"})
        self.assertFalse(reference["decision_authority"])
        self.assertEqual(reference["status"], "manual_verification_required")
        self.assertIn("model_spec", reference["missing_fields"])


if __name__ == "__main__":
    unittest.main()
