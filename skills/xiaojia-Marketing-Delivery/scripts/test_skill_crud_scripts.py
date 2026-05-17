#!/usr/bin/env python3
import base64
import json
import os
from pathlib import Path
from types import SimpleNamespace
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

import _common
import create_skill
import list_skills
import update_skill


class SkillCrudScriptTests(unittest.TestCase):
    def test_resolve_prompt_content_reads_prompt_file(self):
        with TemporaryDirectory() as tmp_dir:
            prompt_path = Path(tmp_dir) / "prompt.md"
            prompt_path.write_text("# 测试 prompt\n", encoding="utf-8")

            content = _common.resolve_prompt_content(prompt_file=str(prompt_path), required=True)

        self.assertEqual(content, "# 测试 prompt\n")

    def test_resolve_prompt_content_rejects_two_prompt_sources(self):
        with self.assertRaises(SystemExit):
            _common.resolve_prompt_content(prompt_content="a", prompt_file="b")

    def test_create_skill_builds_payload(self):
        args = SimpleNamespace(
            name="自动化测试",
            description="desc",
            prompt_content="prompt",
            prompt_file="",
            thumbnail="",
            thumbnail_file="",
            category="note",
            keywords="测试,skill",
            market_status="off",
            market_prompt_visible="false",
            load_strategy="manual",
            applicable_stage=["free_chat"],
            priority=12,
            enabled="true",
            timeout=300,
        )

        payload = create_skill.build_payload(args)

        self.assertEqual(payload["name"], "自动化测试")
        self.assertEqual(payload["prompt_content"], "prompt")
        self.assertEqual(payload["category"], "note")
        self.assertEqual(payload["applicable_stages"], ["free_chat"])
        self.assertEqual(payload["priority"], 12)
        self.assertTrue(payload["enabled"])
        self.assertFalse(payload["market_prompt_visible"])

    def test_create_skill_builds_payload_with_thumbnail_file(self):
        args = SimpleNamespace(
            name="自动化测试",
            description="desc",
            prompt_content="prompt",
            prompt_file="",
            thumbnail="",
            thumbnail_file="./thumbnail.png",
            category="",
            keywords="",
            market_status="",
            market_prompt_visible="",
            load_strategy="",
            applicable_stage=[],
            priority=None,
            enabled="",
            timeout=123,
        )

        with patch.object(create_skill, "upload_skill_thumbnail_file", return_value="https://cos.example/thumb.png") as upload_mock:
            payload = create_skill.build_payload(args)

        upload_mock.assert_called_once_with("./thumbnail.png", timeout=123)
        self.assertEqual(payload["thumbnail"], "https://cos.example/thumb.png")

    def test_create_skill_rejects_two_thumbnail_sources(self):
        args = SimpleNamespace(
            name="自动化测试",
            description="desc",
            prompt_content="prompt",
            prompt_file="",
            thumbnail="https://example.com/thumb.png",
            thumbnail_file="./thumbnail.png",
            category="",
            keywords="",
            market_status="",
            market_prompt_visible="",
            load_strategy="",
            applicable_stage=[],
            priority=None,
            enabled="",
            timeout=123,
        )

        with self.assertRaises(SystemExit):
            create_skill.build_payload(args)

    def test_build_thumbnail_upload_payload_reads_local_file(self):
        with TemporaryDirectory() as tmp_dir:
            thumbnail_path = Path(tmp_dir) / "thumb.png"
            Image.new("RGB", (8, 8), color=(255, 0, 0)).save(thumbnail_path)

            payload = _common.build_thumbnail_upload_payload(str(thumbnail_path))

        self.assertEqual(payload["file_name"], "thumb.png")
        self.assertEqual(payload["content_type"], "image/png")
        decoded = base64.b64decode(payload["file_data"])
        self.assertLessEqual(len(decoded), _common.THUMBNAIL_MAX_BYTES)
        self.assertTrue(decoded.startswith(b"\x89PNG\r\n\x1a\n"))

    def test_update_skill_requires_a_field_besides_skill_id(self):
        args = SimpleNamespace(
            skill_id="skill_x",
            name="",
            description="",
            prompt_content="",
            prompt_file="",
            thumbnail="",
            category="",
            keywords="",
            market_status="",
            review_status="",
            load_strategy="",
            applicable_stage=[],
            priority=None,
            share_prompt_visible="",
            market_prompt_visible="",
        )

        with self.assertRaises(SystemExit):
            update_skill.build_payload(args)

    def test_list_skills_builds_full_internal_query_payload(self):
        args = SimpleNamespace(
            source="personal",
            enabled="all",
            keyword="自动化",
            category="note",
            sort_by="latest",
            page=2,
            page_size=10,
            include_details=True,
            is_featured="false",
        )

        payload = list_skills.build_payload(args)

        self.assertEqual(
            payload,
            {
                "source": "personal",
                "enabled": "all",
                "keyword": "自动化",
                "category": "note",
                "sort_by": "latest",
                "page": 2,
                "page_size": 10,
                "include_details": True,
                "is_featured": False,
            },
        )

    def test_openapi_skill_helpers_use_expected_endpoints(self):
        captured = []

        def fake_open_json(request, timeout):
            captured.append(
                {
                    "url": request.full_url,
                    "timeout": timeout,
                    "body": json.loads(request.data.decode("utf-8")),
                    "authorization": request.headers.get("Authorization"),
                }
            )
            return {"status": 0}

        with patch.dict(
            os.environ,
            {
                "JUSTAI_OPENAPI_BASE_URL": "https://example.com",
                "JUSTAI_OPENAPI_API_KEY": "demo-key",
            },
            clear=True,
        ), patch.object(_common, "open_json", side_effect=fake_open_json):
            _common.openapi_create_skill({"name": "n"}, timeout=11)
            _common.openapi_upload_skill_thumbnail({"file_name": "thumb.png"}, timeout=12)
            _common.openapi_update_skill({"skill_id": "skill_x"}, timeout=13)
            _common.openapi_get_skill("skill_x", timeout=14)
            _common.openapi_delete_skill("skill_x", timeout=15)

        self.assertEqual(
            [item["url"] for item in captured],
            [
                "https://example.com/openapi/skills/create",
                "https://example.com/openapi/skills/upload_thumbnail",
                "https://example.com/openapi/skills/update",
                "https://example.com/openapi/skills/detail",
                "https://example.com/openapi/skills/delete",
            ],
        )
        self.assertEqual(captured[0]["authorization"], "Bearer demo-key")
        self.assertEqual(captured[3]["body"], {"skill_id": "skill_x"})
        self.assertEqual([item["timeout"] for item in captured], [11, 12, 13, 14, 15])


if __name__ == "__main__":
    unittest.main()
