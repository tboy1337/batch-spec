#!/usr/bin/env python3
"""Validate batch-spec YAML files and corpus fixtures against JSON Schema."""

from __future__ import annotations

import json
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
    EXPANSION_YAML,
    REPO_ROOT,
    SCHEMA_DIR,
)


def _validate_yaml(path: Path, schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    print(f"OK {path.name}")


def _validate_json(path: Path, schema: dict[str, object]) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    rel = path.relative_to(REPO_ROOT)
    print(f"OK {rel.as_posix()}")


def _validate_corpus() -> None:
    schema_path = SCHEMA_DIR / "parse-expect.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    for expect_path in sorted(CORPUS_DIR.glob("**/expect.json")):
        _validate_json(expect_path, schema)


def main() -> None:
    _validate_yaml(COMMANDS_YAML, SCHEMA_DIR / "commands.schema.json")
    _validate_yaml(EXPANSION_YAML, SCHEMA_DIR / "expansion.schema.json")
    _validate_corpus()
    print("batch-spec validation passed")


if __name__ == "__main__":
    main()
