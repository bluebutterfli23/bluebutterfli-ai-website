from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class FoundingBetaSiteContractTests(unittest.TestCase):
    def test_positioning_is_behavioral_assurance(self) -> None:
        self.assertIn("Independent Behavioral Assurance for AI Agents", HTML)
        self.assertIn("Evidence, not just a score", HTML)
        self.assertIn("Agent Journal", HTML)

    def test_intake_fields_and_required_confirmations_remain_present(self) -> None:
        self.assertIn('id="beta-intake-form"', HTML)
        for field in ("requester", "email", "agent_name", "agent_type", "purpose"):
            self.assertRegex(HTML, rf'name="{field}"[^>]*required')
        self.assertRegex(HTML, r'name="authorized"[^>]*required')
        self.assertRegex(HTML, r'name="safe_contact"[^>]*required')

    def test_intake_still_opens_the_existing_gmail_draft(self) -> None:
        self.assertIn("https://mail.google.com/mail/?view=cm&fs=1&to=", HTML)
        self.assertIn("info@bluebutterfliai.com", HTML)
        self.assertIn("if (!this.reportValidity()) return;", HTML)
        self.assertIn('id="intake-status"', HTML)
        self.assertIn('href="#intake"', HTML)
        self.assertIn('id="beta"', HTML)

    def test_public_copy_states_confidentiality_and_ownership_boundaries(self) -> None:
        self.assertIn("protects confidential evaluation methods", HTML)
        self.assertIn("Confidential methods withheld", HTML)
        self.assertIn("© 2026 Bluebutterfli AI · All rights reserved", HTML)

    def test_mobile_layout_contract_remains_present(self) -> None:
        self.assertIn("@media(max-width:720px)", CSS)
        self.assertIn(".grid,form", CSS)


if __name__ == "__main__":
    unittest.main()
