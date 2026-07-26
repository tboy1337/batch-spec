# Parse corpus contract

Each fixture lives under `corpus/parse/<case-id>/` and must contain both:

- `input.cmd` - UTF-8 batch source
- `expect.json` - expectations validated by `schema/parse-expect.schema.json`

`scripts/validate.py` fails if either file is missing for a case directory.

## expect.json fields

| Field | Required | Meaning |
|-------|----------|---------|
| description | yes | Human-readable case summary |
| parse | yes | Parse expectation object |
| tags | no | Free-form tags (`if`, `for`, `expansion`, `redirection`, `quoting`, ...) |

Prefer tag spelling `redirection` (not `redirect`) and `quoting` (not `quotes`)
for new fixtures.

### parse object

| Field | Meaning |
|-------|---------|
| should_parse | When true (or omitted with no error flags), require a clean parse tree and no syntax errors |
| should_parse: false | Pass only when the parse is not clean (errors and/or no usable tree) |
| expect_syntax_errors | Pass only when the implementation reports syntax errors |
| top_level_statement | Optional rule name of the **last script-level** statement (`ifStmt`, `forStmt`, `setStmt`, `genericCmd`, `detachedElseStmt`, ...). Nested statements inside IF/FOR/group blocks are ignored |

`should_parse: true` must not be combined with `expect_syntax_errors: true`.
`should_parse: false` must not be combined with `expect_syntax_errors: true`.
Prefer `expect_syntax_errors` for constructs that live `cmd.exe` rejects with a
syntax / "was unexpected at this time" style failure. Keep `should_parse: false`
available for implementations that fail without a clean tree.


## Scope

This corpus is **parse-structure** conformance aligned with live cmd syntax
rejection: when cmd reports a syntax error for the source as written, fixtures
should use `expect_syntax_errors: true` (for example empty unquoted IF operands
in `if-empty-unquoted-valid`, invalid `%~` letters in `e017-invalid-modifier`,
`%~*` in `percent-tilde-star-invalid`, or `IF EXISTS` misspelling).

Directory names containing `invalid` are not the same as
`expect_syntax_errors: true`. Some `*-invalid` fixtures still
`should_parse: true` and document semantic/runtime invalidity only (for example
sticky ERRORLEVEL, unknown external names, or a newline-detached ELSE that cmd
treats as an unknown command rather than an IF syntax abort — see
`else-newline-bare-invalid` / `else-unescaped-newline-invalid` and
`detachedElseStmt`). Runtime batveats that still parse cleanly (for example the
missing/empty substring batveat) stay `should_parse: true` with guidance in
[`data/expansion.yaml`](../data/expansion.yaml).

Semantic rejection guidance (valid `%~` letters, SET /A rules, remarks, and
related facts) lives in [`data/expansion.yaml`](../data/expansion.yaml). Parser
acceptance does not imply catalog validity for purely semantic batveats.

Authoritative command syntax snippets for authors live under `audit/cmd-help/`.
