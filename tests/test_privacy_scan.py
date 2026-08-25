import unittest

from scripts.privacy_scan import APPROVED_PUBLIC_EMAILS, CONTENT_RULES


class PrivacyScanTests(unittest.TestCase):
    def test_only_declared_public_contact_email_is_allowlisted(self):
        text = "Contact miracle.hao2023@gmail.com or " + "private.person" + "@" + "example.org"
        for approved_email in APPROVED_PUBLIC_EMAILS:
            text = text.replace(approved_email, "[approved-public-email]")

        self.assertIsNotNone(CONTENT_RULES["email address"].search(text))

    def test_declared_public_contact_is_removed_from_email_scan(self):
        text = "Contact miracle.hao2023@gmail.com"
        for approved_email in APPROVED_PUBLIC_EMAILS:
            text = text.replace(approved_email, "[approved-public-email]")

        self.assertIsNone(CONTENT_RULES["email address"].search(text))


if __name__ == "__main__":
    unittest.main()
