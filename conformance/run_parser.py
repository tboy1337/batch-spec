#!/usr/bin/env python3

"""Run parser conformance cases against a registered implementation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable, List

REPO_ROOT = Path(__file__).resolve().parent.parent

CORPUS_DIR = REPO_ROOT / "corpus" / "parse"

GENERATED_DIR = REPO_ROOT / "generated" / "python"


def _discover_cases() -> list[tuple[str, Path, dict[str, object]]]:

    cases: list[tuple[str, Path, dict[str, object]]] = []

    for expect_path in sorted(CORPUS_DIR.glob("**/expect.json")):

        case_dir = expect_path.parent

        input_path = case_dir / "input.cmd"

        if not input_path.is_file():

            continue

        expect = json.loads(expect_path.read_text(encoding="utf-8"))

        case_id = "/".join(case_dir.relative_to(CORPUS_DIR).parts)

        cases.append((case_id, input_path, expect))

    return cases


def _parse_antlr(lines: List[str]) -> tuple[object | None, list[str]]:

    if str(GENERATED_DIR) not in sys.path:

        sys.path.insert(0, str(GENERATED_DIR))

    from antlr4 import CommonTokenStream, InputStream  # isort: skip

    from antlr4.error.ErrorListener import ErrorListener  # isort: skip

    from BatchLexer import BatchLexer  # isort: skip

    from BatchParser import BatchParser  # isort: skip

    source = "\n".join(lines)

    lexer = BatchLexer(InputStream(source))

    token_stream = CommonTokenStream(lexer)

    parser = BatchParser(token_stream)

    errors: list[str] = []

    class _Listener(ErrorListener):  # type: ignore[misc]

        def syntaxError(  # pylint: disable=arguments-differ,too-many-positional-arguments
            self,
            recognizer: object,
            offendingSymbol: object,
            line: int,
            column: int,
            msg: str,
            e: BaseException | None,
        ) -> None:

            del recognizer, offendingSymbol, e

            errors.append(f"line {line}:{column} {msg}")

    lexer.removeErrorListeners()

    parser.removeErrorListeners()

    lexer.addErrorListener(_Listener())

    parser.addErrorListener(_Listener())

    tree = parser.script()

    return tree, errors


_IMPLEMENTATIONS: dict[str, Callable[[List[str]], tuple[object | None, list[str]]]] = {
    "antlr": _parse_antlr,
}


def _check_case(
    case_id: str,
    input_path: Path,
    expect: dict[str, object],
    impl: Callable[[List[str]], tuple[object | None, list[str]]],
) -> str | None:

    lines = input_path.read_text(encoding="utf-8").splitlines()

    tree, errors = impl(lines)

    parse_meta = expect.get("parse", {})

    if not isinstance(parse_meta, dict):

        parse_meta = {}

    if parse_meta.get("expect_syntax_errors"):

        if not errors:

            return f"{case_id}: expected syntax errors, got none"

        return None

    if parse_meta.get("should_parse") is False:

        if tree is not None and not errors:

            return f"{case_id}: expected parse failure"

        return None

    if tree is None:

        return f"{case_id}: parser returned no tree"

    return None


def main() -> int:

    parser = argparse.ArgumentParser(description="batch-spec parser conformance")

    parser.add_argument("--impl", default="antlr", choices=sorted(_IMPLEMENTATIONS))

    args = parser.parse_args()

    impl = _IMPLEMENTATIONS[args.impl]

    failures: list[str] = []

    for case_id, input_path, expect in _discover_cases():

        message = _check_case(case_id, input_path, expect, impl)

        if message:

            failures.append(message)

    if failures:

        for message in failures:

            print(message, file=sys.stderr)

        return 1

    print(f"All {len(_discover_cases())} parse cases passed ({args.impl})")

    return 0


if __name__ == "__main__":

    raise SystemExit(main())
