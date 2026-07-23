"""Shared paths for batch-spec tooling."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = REPO_ROOT / "schema"
GRAMMAR_DIR = REPO_ROOT / "grammar"
DOCS_DIR = REPO_ROOT / "docs"
CORPUS_DIR = REPO_ROOT / "corpus" / "parse"
GENERATED_DIR = REPO_ROOT / "generated" / "python"
COMMANDS_YAML = DATA_DIR / "commands.yaml"
EXPANSION_YAML = DATA_DIR / "expansion.yaml"
