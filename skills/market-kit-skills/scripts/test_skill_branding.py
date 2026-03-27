#!/usr/bin/env python3
from pathlib import Path
import unittest


class SkillBrandingTests(unittest.TestCase):
    def test_skill_metadata_uses_market_kit_branding(self):
        skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"

        skill_text = skill_md.read_text(encoding="utf-8")
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        self.assertIn("name: market-kit-skills", skill_text)
        self.assertIn("# Market Kit Skills", skill_text)
        self.assertIn('display_name: "Market Kit Skills"', yaml_text)
        self.assertIn("marketing", yaml_text.lower())

    def test_user_facing_docs_focus_on_marketing_capabilities(self):
        skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
        readme = Path(__file__).resolve().parents[1] / "README.md"
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"

        skill_text = skill_md.read_text(encoding="utf-8")
        readme_text = readme.read_text(encoding="utf-8")
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        self.assertIn("营销", skill_text)
        self.assertIn("营销", readme_text)
        self.assertIn("campaign", yaml_text.lower())
        self.assertIn("小红书", skill_text)
        self.assertIn("小红书", readme_text)

    def test_user_facing_docs_hide_login_and_payment_details(self):
        skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
        readme = Path(__file__).resolve().parents[1] / "README.md"
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"

        skill_text = skill_md.read_text(encoding="utf-8")
        readme_text = readme.read_text(encoding="utf-8")
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        for text in (skill_text, readme_text, yaml_text):
            self.assertNotIn("JUSTAI_OPENAPI_API_KEY", text)
            self.assertNotIn("login flow", text)
            self.assertNotIn("payment", text.lower())
            self.assertNotIn("营销页", text)

    def test_skill_docs_define_timeout_rules_for_slow_generation(self):
        skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
        readme = Path(__file__).resolve().parents[1] / "README.md"
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"

        skill_text = skill_md.read_text(encoding="utf-8")
        readme_text = readme.read_text(encoding="utf-8")
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        self.assertIn("300", skill_text)
        self.assertIn("300", readme_text)
        self.assertIn("running", skill_text)
        self.assertIn("running", yaml_text)
        self.assertIn("不要把轮询超时当成任务失败", skill_text)
        self.assertIn("不要把轮询超时当成任务失败", readme_text)
        self.assertIn("timeout", yaml_text.lower())

    def test_skill_docs_forbid_fabricating_results_and_require_web_url(self):
        skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
        readme = Path(__file__).resolve().parents[1] / "README.md"
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"

        skill_text = skill_md.read_text(encoding="utf-8")
        readme_text = readme.read_text(encoding="utf-8")
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        self.assertIn("不要自己擅自生成", skill_text)
        self.assertIn("不要自己擅自生成", readme_text)
        self.assertIn("still generating", yaml_text)
        self.assertIn("web_url", skill_text)
        self.assertIn("web_url", readme_text)
        self.assertIn("conversation_id", yaml_text)
        self.assertIn("https://justailab.com/marketing", skill_text)
        self.assertIn("https://justailab.com/marketing", readme_text)
        self.assertIn("https://justailab.com/marketing", yaml_text)

    def test_internal_prompt_uses_agent_market_not_agent_default(self):
        openai_yaml = Path(__file__).resolve().parents[1] / "agents" / "openai.yaml"
        yaml_text = openai_yaml.read_text(encoding="utf-8")

        self.assertIn("agent_market", yaml_text)
        self.assertNotIn("agent_default", yaml_text)


if __name__ == "__main__":
    unittest.main()
