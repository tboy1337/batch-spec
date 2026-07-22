#!/usr/bin/env python3
"""Validate batch-spec YAML files against JSON Schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from _paths import COMMANDS_YAML, EXPANSION_YAML, SCHEMA_DIR  # noqa: E402


def _validate(path: Path, schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    print(f"OK {path.name}")


def main() -> None:
    _validate(COMMANDS_YAML, SCHEMA_DIR / "commands.schema.json")
    _validate(EXPANSION_YAML, SCHEMA_DIR / "expansion.schema.json")
    print("batch-spec validation passed")


if __name__ == "__main__":
    main()
