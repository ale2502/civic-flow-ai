import unittest

from civicflow_ai import CivicAssistant


class CivicAssistantTest(unittest.TestCase):
    def test_triages_urgent_path_hazard(self) -> None:
        response = CivicAssistant().handle_request(
            "A fallen tree is blocking the footpath outside 12 King Street."
        )

        self.assertEqual(response.triage.category, "roads_and_paths")
        self.assertEqual(response.triage.priority, "high")
        self.assertTrue(response.triage.escalate)

    def test_triages_missed_recycling_bin(self) -> None:
        response = CivicAssistant().handle_request(
            "My recycling bin was missed yesterday even though it was out on time."
        )

        self.assertEqual(response.triage.category, "waste")
        self.assertEqual(response.triage.priority, "normal")
        self.assertFalse(response.triage.escalate)

    def test_rejects_empty_request(self) -> None:
        with self.assertRaises(ValueError):
            CivicAssistant().handle_request(" ")


if __name__ == "__main__":
    unittest.main()
