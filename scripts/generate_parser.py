#!/usr/bin/env python3
"""Generate ANTLR Python parser from grammar/*.g4 into generated/python/."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from _paths import GENERATED_DIR, GRAMMAR_DIR  # noqa: E402

_GRAMMAR_FILES = ("BatchLexer.g4", "BatchParser.g4")
_STAMP_NAME = ".grammar-stamp"
_GENERATED_NAMES = (
    "BatchLexer.py",
    "BatchParser.py",
    "BatchParserVisitor.py",
    "__init__.py",
)


def _grammar_fingerprint() -> str:
    digest = hashlib.sha256()
    for name in _GRAMMAR_FILES:
        content = (GRAMMAR_DIR / name).read_bytes()
        content = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest.update(content)
    return digest.hexdigest()


def _file_fingerprint(path: Path) -> str:
    content = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(content).hexdigest()


def _run_antlr(output_dir: Path) -> None:
    grammar_paths = [str(GRAMMAR_DIR / name) for name in _GRAMMAR_FILES]
    cmd = [
        "antlr4",
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        "-o",
        str(output_dir),
    ] + grammar_paths
    env = os.environ.copy()
    env.setdefault("ANTLR4_TOOLS_ANTLR_VERSION", "4.13.2")
    _ = subprocess.run(cmd, check=True, cwd=GRAMMAR_DIR, env=env)


def _write_init(output_dir: Path) -> None:
    (output_dir / "__init__.py").write_text(
        '"""ANTLR-generated batch parser (do not edit by hand)."""\n',
        encoding="utf-8",
    )


def generate_parser() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    _run_antlr(GENERATED_DIR)
    _write_init(GENERATED_DIR)
    (GENERATED_DIR / _STAMP_NAME).write_text(_grammar_fingerprint(), encoding="utf-8")


def _check_generated() -> None:
    names = list(_GENERATED_NAMES) + [_STAMP_NAME]
    missing = [
        GENERATED_DIR / name for name in names if not (GENERATED_DIR / name).is_file()
    ]
    if missing:
        for path in missing:
            print(f"Missing {path}", file=sys.stderr)
        raise SystemExit(1)
    stamp = (GENERATED_DIR / _STAMP_NAME).read_text(encoding="utf-8").strip()
    if stamp != _grammar_fingerprint():
        print(
            "Generated parser is stale (grammar fingerprint mismatch)",
            file=sys.stderr,
        )
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="batch-spec-antlr-") as tmp:
        tmp_dir = Path(tmp)
        _run_antlr(tmp_dir)
        _write_init(tmp_dir)
        for name in _GENERATED_NAMES:
            committed = GENERATED_DIR / name
            fresh = tmp_dir / name
            if not fresh.is_file():
                print(f"ANTLR did not produce {name}", file=sys.stderr)
                raise SystemExit(1)
            if _file_fingerprint(committed) != _file_fingerprint(fresh):
                print(
                    f"Generated file drift: {name} does not match fresh ANTLR output",
                    file=sys.stderr,
                )
                raise SystemExit(1)
    print("Generated parser is up to date")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ANTLR Python parser")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        _check_generated()
        return
    generate_parser()
    print(f"Wrote ANTLR output to {GENERATED_DIR}")


if __name__ == "__main__":
    main()
