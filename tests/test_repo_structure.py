import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ChatCmsRepositoryStructureTests(unittest.TestCase):
    def test_readme_exists_and_has_title(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.exists(), "README.md should exist")

        content = readme.read_text(encoding="utf-8")
        self.assertIn("# Chat CMS", content)
        self.assertIn("Apache License 2.0", content)

    def test_skill_file_exists_and_describes_core_contract(self):
        skill = ROOT / "SKILL.md"
        self.assertTrue(skill.exists(), "SKILL.md should exist")

        content = skill.read_text(encoding="utf-8")
        self.assertIn("# Chat CMS", content)
        self.assertIn("Core Contract", content)
        self.assertIn("Authorization Gate", content)

    def test_profile_template_exists_and_has_required_fields(self):
        template = ROOT / "profiles" / "template.yaml"
        self.assertTrue(template.exists(), "profiles/template.yaml should exist")

        content = template.read_text(encoding="utf-8")
        for expected in [
            "profile:",
            "site:",
            "github:",
            "authorization:",
            "deployment:",
            "forbidden:",
        ]:
            self.assertIn(expected, content, f"Missing required template section: {expected}")


if __name__ == "__main__":
    unittest.main()
