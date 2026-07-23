"""Tests for scripts/ tooling modules."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock

import jsonschema
import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import _paths  # noqa: E402
import generate_parser  # noqa: E402
import validate  # noqa: E402


def test_paths_resolve_to_existing_targets() -> None:
    assert _paths.REPO_ROOT.is_dir()
    assert _paths.DATA_DIR.is_dir()
    assert _paths.SCHEMA_DIR.is_dir()
    assert _paths.GRAMMAR_DIR.is_dir()
    assert _paths.CORPUS_DIR.is_dir()
    assert _paths.GENERATED_DIR.is_dir()
    assert _paths.COMMANDS_YAML.is_file()
    assert _paths.EXPANSION_YAML.is_file()


def test_validate_accepts_real_commands_yaml() -> None:
    validate._validate_yaml(
        _paths.COMMANDS_YAML, _paths.SCHEMA_DIR / "commands.schema.json"
    )


def test_validate_accepts_real_expansion_yaml() -> None:
    validate._validate_yaml(
        _paths.EXPANSION_YAML, _paths.SCHEMA_DIR / "expansion.schema.json"
    )


def test_validate_rejects_invalid_yaml(tmp_path: Path) -> None:
    invalid_yaml = tmp_path / "invalid.yaml"
    invalid_yaml.write_text("builtin_commands: []\n", encoding="utf-8")
    schema_path = _paths.SCHEMA_DIR / "commands.schema.json"

    with pytest.raises(jsonschema.ValidationError):
        validate._validate_yaml(invalid_yaml, schema_path)


def test_validate_main_prints_success(capsys: pytest.CaptureFixture[str]) -> None:
    validate.main()
    captured = capsys.readouterr()
    assert "batch-spec validation passed" in captured.out


def test_validate_corpus_rejects_orphan_expect(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    corpus = tmp_path / "corpus" / "parse"
    orphan = corpus / "orphan-expect"
    orphan.mkdir(parents=True)
    (orphan / "expect.json").write_text(
        '{"description": "orphan", "parse": {"should_parse": true}}',
        encoding="utf-8",
    )
    monkeypatch.setattr(validate, "CORPUS_DIR", corpus)
    monkeypatch.setattr(validate, "REPO_ROOT", tmp_path)

    with pytest.raises(SystemExit) as exc_info:
        validate._validate_corpus()

    assert exc_info.value.code == 1


def test_validate_corpus_rejects_orphan_input(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    corpus = tmp_path / "corpus" / "parse"
    orphan = corpus / "orphan-input"
    orphan.mkdir(parents=True)
    (orphan / "input.cmd").write_text("@echo off\n", encoding="utf-8")
    monkeypatch.setattr(validate, "CORPUS_DIR", corpus)
    monkeypatch.setattr(validate, "REPO_ROOT", tmp_path)

    with pytest.raises(SystemExit) as exc_info:
        validate._validate_corpus()

    assert exc_info.value.code == 1


def test_grammar_fingerprint_is_deterministic() -> None:
    first = generate_parser._grammar_fingerprint()
    second = generate_parser._grammar_fingerprint()
    assert first == second
    assert len(first) == 64


def test_grammar_fingerprint_normalizes_crlf(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    grammar_dir = tmp_path / "grammar"
    grammar_dir.mkdir()
    (grammar_dir / "BatchLexer.g4").write_bytes(b"lexer grammar BatchLexer;\r\n")
    (grammar_dir / "BatchParser.g4").write_bytes(b"parser grammar BatchParser;\r\n")
    monkeypatch.setattr(generate_parser, "GRAMMAR_DIR", grammar_dir)

    crlf_fingerprint = generate_parser._grammar_fingerprint()

    (grammar_dir / "BatchLexer.g4").write_bytes(b"lexer grammar BatchLexer;\n")
    (grammar_dir / "BatchParser.g4").write_bytes(b"parser grammar BatchParser;\n")

    lf_fingerprint = generate_parser._grammar_fingerprint()
    assert crlf_fingerprint == lf_fingerprint


def test_generate_parser_check_reports_missing_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    generated_dir = tmp_path / "generated" / "python"
    generated_dir.mkdir(parents=True)
    monkeypatch.setattr(generate_parser, "GENERATED_DIR", generated_dir)
    monkeypatch.setattr(sys, "argv", ["generate_parser.py", "--check"])

    with pytest.raises(SystemExit) as exc_info:
        generate_parser.main()

    assert exc_info.value.code == 1


def test_generate_parser_check_reports_stale_stamp(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    generated_dir = tmp_path / "generated" / "python"
    generated_dir.mkdir(parents=True)
    for name in (
        "BatchLexer.py",
        "BatchParser.py",
        "BatchParserVisitor.py",
        "__init__.py",
        ".grammar-stamp",
    ):
        (generated_dir / name).write_text("placeholder", encoding="utf-8")
    (generated_dir / ".grammar-stamp").write_text("stale", encoding="utf-8")

    monkeypatch.setattr(generate_parser, "GENERATED_DIR", generated_dir)
    monkeypatch.setattr(sys, "argv", ["generate_parser.py", "--check"])

    with pytest.raises(SystemExit) as exc_info:
        generate_parser.main()

    assert exc_info.value.code == 1


def test_generate_parser_check_passes_when_up_to_date(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    generated_dir = tmp_path / "generated" / "python"
    generated_dir.mkdir(parents=True)
    fingerprint = generate_parser._grammar_fingerprint()
    init_text = '"""ANTLR-generated batch parser (do not edit by hand)."""\n'
    for name in ("BatchLexer.py", "BatchParser.py", "BatchParserVisitor.py"):
        (generated_dir / name).write_text("placeholder", encoding="utf-8")
    (generated_dir / "__init__.py").write_text(init_text, encoding="utf-8")
    (generated_dir / ".grammar-stamp").write_text(fingerprint, encoding="utf-8")

    def _fake_run_antlr(output_dir: Path) -> None:
        for name in ("BatchLexer.py", "BatchParser.py", "BatchParserVisitor.py"):
            (output_dir / name).write_text("placeholder", encoding="utf-8")

    monkeypatch.setattr(generate_parser, "GENERATED_DIR", generated_dir)
    monkeypatch.setattr(generate_parser, "_run_antlr", _fake_run_antlr)
    monkeypatch.setattr(sys, "argv", ["generate_parser.py", "--check"])

    generate_parser.main()


def test_generate_parser_writes_stamp_and_init(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    generated_dir = tmp_path / "generated" / "python"
    generated_dir.mkdir(parents=True)
    (generated_dir / "stale.txt").write_text("remove me", encoding="utf-8")
    grammar_dir = tmp_path / "grammar"
    grammar_dir.mkdir()
    (grammar_dir / "BatchLexer.g4").write_text(
        "lexer grammar BatchLexer;\n", encoding="utf-8"
    )
    (grammar_dir / "BatchParser.g4").write_text(
        "parser grammar BatchParser;\noptions { tokenVocab=BatchLexer; }\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(generate_parser, "GENERATED_DIR", generated_dir)
    monkeypatch.setattr(generate_parser, "GRAMMAR_DIR", grammar_dir)
    monkeypatch.setattr(
        generate_parser.subprocess,
        "run",
        MagicMock(return_value=MagicMock(returncode=0)),
    )

    generate_parser.generate_parser()

    assert not (generated_dir / "stale.txt").exists()
    assert (generated_dir / "__init__.py").is_file()
    stamp = (generated_dir / ".grammar-stamp").read_text(encoding="utf-8").strip()
    assert stamp == generate_parser._grammar_fingerprint()


def test_generate_parser_main_writes_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    generated_dir = tmp_path / "generated" / "python"
    monkeypatch.setattr(generate_parser, "GENERATED_DIR", generated_dir)
    monkeypatch.setattr(generate_parser, "generate_parser", MagicMock())
    monkeypatch.setattr(sys, "argv", ["generate_parser.py"])

    generate_parser.main()

    captured = capsys.readouterr()
    assert f"Wrote ANTLR output to {generated_dir}" in captured.out
