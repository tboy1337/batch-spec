"""Tests for conformance/run_parser.py."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

CONFORMANCE_DIR = Path(__file__).resolve().parent.parent / "conformance"
if str(CONFORMANCE_DIR) not in sys.path:
    sys.path.insert(0, str(CONFORMANCE_DIR))

import run_parser  # noqa: E402


def _mock_impl(
    tree: object | None,
    errors: list[str],
) -> MagicMock:
    return MagicMock(return_value=(tree, errors))


def test_discover_cases_finds_repository_corpus() -> None:
    cases = run_parser._discover_cases()
    assert len(cases) == 107
    assert all(case_id for case_id, _, _ in cases)


def test_discover_cases_skips_missing_input(
    tmp_corpus: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    case_dir = tmp_corpus / "missing-input"
    case_dir.mkdir()
    (case_dir / "expect.json").write_text(
        json.dumps({"description": "missing input"}),
        encoding="utf-8",
    )
    monkeypatch.setattr(run_parser, "CORPUS_DIR", tmp_corpus)

    cases = run_parser._discover_cases()

    assert cases == []


def test_check_case_success(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=[])
    message = run_parser._check_case(
        "ok-case",
        input_path,
        {"parse": {"should_parse": True}},
        impl,
    )
    assert message is None


def test_check_case_expect_syntax_errors_passes_with_errors(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=["line 1:0 error"])

    message = run_parser._check_case(
        "syntax-error-case",
        input_path,
        {"parse": {"expect_syntax_errors": True}},
        impl,
    )

    assert message is None


def test_check_case_expect_syntax_errors_fails_without_errors(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=[])

    message = run_parser._check_case(
        "syntax-error-case",
        input_path,
        {"parse": {"expect_syntax_errors": True}},
        impl,
    )

    assert message == "syntax-error-case: expected syntax errors, got none"


def test_check_case_should_parse_false_passes_with_errors(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=["line 1:0 error"])

    message = run_parser._check_case(
        "parse-failure-case",
        input_path,
        {"parse": {"should_parse": False}},
        impl,
    )

    assert message is None


def test_check_case_should_parse_false_fails_when_tree_present(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=[])

    message = run_parser._check_case(
        "parse-failure-case",
        input_path,
        {"parse": {"should_parse": False}},
        impl,
    )

    assert message == "parse-failure-case: expected parse failure"


def test_check_case_should_parse_fails_with_hidden_errors(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(
        tree=object(), errors=["line 1:0 token recognition error at: '@'"]
    )

    message = run_parser._check_case(
        "hidden-error-case",
        input_path,
        {"parse": {"should_parse": True}},
        impl,
    )

    assert message is not None
    assert "expected clean parse" in message


def test_check_case_missing_tree_reports_error(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=None, errors=[])

    message = run_parser._check_case(
        "missing-tree-case",
        input_path,
        {"parse": {"should_parse": True}},
        impl,
    )

    assert message == "missing-tree-case: parser returned no tree"


def test_check_case_non_dict_parse_meta_is_treated_as_empty(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=[])

    message = run_parser._check_case(
        "non-dict-meta",
        input_path,
        {"parse": "invalid"},
        impl,
    )

    assert message is None


def test_check_case_should_parse_false_passes_with_no_tree(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=None, errors=["line 1:0 error"])

    message = run_parser._check_case(
        "parse-failure-case",
        input_path,
        {"parse": {"should_parse": False}},
        impl,
    )

    assert message is None


def test_check_case_top_level_statement_mismatch(tmp_path: Path) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")
    impl = _mock_impl(tree=object(), errors=[])

    message = run_parser._check_case(
        "stmt-case",
        input_path,
        {"parse": {"top_level_statement": "ifStmt"}},
        impl,
    )

    assert message == "stmt-case: expected top-level statement 'ifStmt', got None"


@pytest.mark.integration
def test_top_level_statement_helpers_with_real_tree(
    generated_parser: None,
) -> None:
    tree, errors = run_parser._parse_antlr(["if 1==1 echo yes"])
    assert tree is not None
    assert errors == []
    assert run_parser._top_level_statement_name(tree) == "ifStmt"


@pytest.mark.integration
def test_check_case_top_level_statement_mismatch_with_real_tree(
    generated_parser: None,
    tmp_path: Path,
) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("echo hi\n", encoding="utf-8")

    message = run_parser._check_case(
        "stmt-case",
        input_path,
        {"parse": {"top_level_statement": "ifStmt"}},
        run_parser._parse_antlr,
    )

    assert (
        message == "stmt-case: expected top-level statement 'ifStmt', got 'genericCmd'"
    )


@pytest.mark.integration
def test_check_case_top_level_statement_passes_with_real_tree(
    generated_parser: None,
    tmp_path: Path,
) -> None:
    input_path = tmp_path / "input.cmd"
    input_path.write_text("if 1==1 echo yes\n", encoding="utf-8")

    message = run_parser._check_case(
        "stmt-case",
        input_path,
        {"parse": {"top_level_statement": "ifStmt"}},
        run_parser._parse_antlr,
    )

    assert message is None


def test_statement_rule_name_returns_none_for_empty_children() -> None:
    class _EmptyStatement:
        children: list[object] | None = []

    assert run_parser._statement_rule_name(_EmptyStatement()) is None


@pytest.mark.integration
def test_parse_antlr_parses_simple_script(generated_parser: None) -> None:
    generated_dir = str(run_parser.GENERATED_DIR)
    if generated_dir in sys.path:
        sys.path.remove(generated_dir)

    tree, errors = run_parser._parse_antlr(["echo hello"])
    assert tree is not None
    assert errors == []
    assert generated_dir in sys.path

    tree_again, errors_again = run_parser._parse_antlr(["echo bye"])
    assert tree_again is not None
    assert errors_again == []


def test_main_returns_zero_when_all_cases_pass(monkeypatch: pytest.MonkeyPatch) -> None:
    sample_cases = [
        ("ok", Path("input.cmd"), {"parse": {"should_parse": True}}),
    ]
    monkeypatch.setattr(run_parser, "_discover_cases", lambda: sample_cases)
    monkeypatch.setattr(run_parser, "_check_case", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(sys, "argv", ["run_parser.py", "--impl", "antlr"])

    assert run_parser.main() == 0


def test_main_returns_one_when_case_fails(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    sample_cases = [
        ("bad", Path("input.cmd"), {"parse": {"should_parse": True}}),
    ]
    monkeypatch.setattr(run_parser, "_discover_cases", lambda: sample_cases)
    monkeypatch.setattr(
        run_parser,
        "_check_case",
        lambda *_args, **_kwargs: "bad: parser returned no tree",
    )
    monkeypatch.setattr(sys, "argv", ["run_parser.py", "--impl", "antlr"])

    assert run_parser.main() == 1
    captured = capsys.readouterr()
    assert "bad: parser returned no tree" in captured.err
