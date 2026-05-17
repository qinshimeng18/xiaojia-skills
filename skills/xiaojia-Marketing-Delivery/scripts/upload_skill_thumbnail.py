#!/usr/bin/env python3
import argparse
import json

from _common import (
    build_thumbnail_upload_payload,
    get_default_timeout,
    openapi_upload_skill_thumbnail,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Upload a local Skill thumbnail image through OpenAPI.")
    parser.add_argument("--file", required=True, help="Local image path. Converts to optimized PNG, max upload size 1MB.")
    parser.add_argument(
        "--timeout",
        type=int,
        default=get_default_timeout(),
        help="HTTP timeout in seconds. Defaults to env/local config or 300.",
    )
    args = parser.parse_args()

    result = openapi_upload_skill_thumbnail(
        build_thumbnail_upload_payload(args.file),
        timeout=args.timeout,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
