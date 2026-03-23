#!/usr/bin/env python3
import argparse
import json
import os
from _common import DEFAULT_TIMEOUT, submit_and_poll


def main() -> int:
    parser = argparse.ArgumentParser(description="Call the JustAI openapi chat endpoint.")
    parser.add_argument("--message", required=True, help="User message to send.")
    parser.add_argument("--conversation-id", default="", help="Existing conversation id to continue.")
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("JUSTAI_OPENAPI_TIMEOUT", DEFAULT_TIMEOUT)),
        help="HTTP timeout in seconds. Defaults to JUSTAI_OPENAPI_TIMEOUT or 300.",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=2,
        help="Polling interval in seconds for chat_result. Defaults to 2.",
    )
    parser.add_argument(
        "--project-id",
        action="append",
        default=[],
        help="Optional project/folder id to scope RAG reference. Can be repeated.",
    )
    parser.add_argument(
        "--skill-id",
        action="append",
        default=[],
        help="Optional manual skill id to preload. Can be repeated.",
    )
    args = parser.parse_args()

    result = submit_and_poll(
        message=args.message,
        conversation_id=args.conversation_id,
        timeout=args.timeout,
        poll_interval=args.poll_interval,
        project_ids=args.project_id,
        skill_ids=args.skill_id,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
