#!/usr/bin/env python3
"""Generate ANTLR Python parser from grammar/*.g4 into generated/python/."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from _paths import GENERATED_DIR, GRAMMAR_DIR  # noqa: E402

_GRAMMAR_FILES = ("BatchLexer.g4", "BatchParser.g4")
_STAMP_NAME = ".grammar-stamp"


def _grammar_fingerprint() -> str:
    digest = hashlib.sha256()
    for name in _GRAMMAR_FILES:
        content = (GRAMMAR_DIR / name).read_bytes()
        content = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest.update(content)
    return digest.hexdigest()


def _run_antlr() -> None:
    grammar_paths = [str(GRAMMAR_DIR / name) for name in _GRAMMAR_FILES]
    cmd = [
        "antlr4",
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        "-o",
        str(GENERATED_DIR),
    ] + grammar_paths
    env = os.environ.copy()
    env.setdefault("ANTLR4_TOOLS_ANTLR_VERSION", "4.13.2")
    subprocess.run(cmd, check=True, cwd=GRAMMAR_DIR, env=env)


def generate_parser() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    _run_antlr()
    (GENERATED_DIR / "__init__.py").write_text(
        '"""ANTLR-generated batch parser (do not edit by hand)."""\n',
        encoding="utf-8",
    )
    (GENERATED_DIR / _STAMP_NAME).write_text(_grammar_fingerprint(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ANTLR Python parser")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    names = ["BatchLexer.py", "BatchParser.py", "BatchParserVisitor.py", "__init__.py", _STAMP_NAME]
    if args.check:
        missing = [GENERATED_DIR / name for name in names if not (GENERATED_DIR / name).is_file()]
        if missing:
            for path in missing:
                print(f"Missing {path}", file=sys.stderr)
            raise SystemExit(1)
        stamp = (GENERATED_DIR / _STAMP_NAME).read_text(encoding="utf-8").strip()
        if stamp != _grammar_fingerprint():
            print("Generated parser is stale", file=sys.stderr)
            raise SystemExit(1)
        print("Generated parser is up to date")
        return
    generate_parser()
    print(f"Wrote ANTLR output to {GENERATED_DIR}")


if __name__ == "__main__":
    main()
