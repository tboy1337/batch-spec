#!/usr/bin/env python3
"""Validate batch-spec YAML files and corpus fixtures against JSON Schema."""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

import jsonschema
import yaml

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from _paths import (  # noqa: E402
    COMMANDS_YAML,
    CORPUS_DIR,
    DOCS_DIR,
    EXPANSION_YAML,
    REPO_ROOT,
    SCHEMA_DIR,
)

LOGGER = logging.getLogger(__name__)

# Allow tab/LF/CR only among C0 controls in consumer docs.
_ALLOWED_C0 = {9, 10, 13}


def _validate_yaml(path: Path, schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    LOGGER.info("OK %s", path.name)
    print(f"OK {path.name}")


def _validate_json(path: Path, schema: dict[str, object]) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    rel = path.relative_to(REPO_ROOT)
    LOGGER.info("OK %s", rel.as_posix())
    print(f"OK {rel.as_posix()}")


def _validate_docs_encoding() -> None:
    """Reject C0 control characters (except tab/LF/CR) in docs/*.md."""
    failures: list[str] = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        data = path.read_bytes()
        try:
            data.decode("utf-8")
        except UnicodeDecodeError as exc:
            failures.append(f"{path.relative_to(REPO_ROOT).as_posix()}: {exc}")
            continue
        bad = [
            f"0x{byte:02x}@{index}"
            for index, byte in enumerate(data)
            if byte < 32 and byte not in _ALLOWED_C0
        ]
        if bad:
            rel = path.relative_to(REPO_ROOT).as_posix()
            sample = ", ".join(bad[:5])
            failures.append(f"{rel}: disallowed C0 controls ({sample})")
    if failures:
        for message in failures:
            print(message, file=sys.stderr)
            LOGGER.error("%s", message)
        raise SystemExit(1)
    for path in sorted(DOCS_DIR.glob("*.md")):
        rel = path.relative_to(REPO_ROOT).as_posix()
        LOGGER.info("OK %s", rel)
        print(f"OK {rel}")


def _validate_corpus() -> None:
    schema_path = SCHEMA_DIR / "parse-expect.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    orphan_expects: list[Path] = []
    orphan_inputs: list[Path] = []
    for expect_path in sorted(CORPUS_DIR.glob("**/expect.json")):
        input_path = expect_path.parent / "input.cmd"
        if not input_path.is_file():
            orphan_expects.append(expect_path)
            continue
        _validate_json(expect_path, schema)
    for input_path in sorted(CORPUS_DIR.glob("**/input.cmd")):
        expect_path = input_path.parent / "expect.json"
        if not expect_path.is_file():
            orphan_inputs.append(input_path)
    if orphan_expects or orphan_inputs:
        for path in orphan_expects:
            rel = path.relative_to(REPO_ROOT)
            print(f"Missing input.cmd for {rel.as_posix()}", file=sys.stderr)
            LOGGER.error("Missing input.cmd for %s", rel.as_posix())
        for path in orphan_inputs:
            rel = path.relative_to(REPO_ROOT)
            print(f"Missing expect.json for {rel.as_posix()}", file=sys.stderr)
            LOGGER.error("Missing expect.json for %s", rel.as_posix())
        raise SystemExit(1)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    _validate_yaml(COMMANDS_YAML, SCHEMA_DIR / "commands.schema.json")
    _validate_yaml(EXPANSION_YAML, SCHEMA_DIR / "expansion.schema.json")
    _validate_docs_encoding()
    _validate_corpus()
    print("batch-spec validation passed")


if __name__ == "__main__":
    main()
