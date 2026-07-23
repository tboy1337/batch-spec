# Parse corpus contract

Each fixture lives under corpus/parse/<case-id>/ and must contain both:

- input.cmd — UTF-8 batch source
- expect.json — expectations validated by schema/parse-expect.schema.json

scripts/validate.py fails if either file is missing for a case directory.

## expect.json fields

| Field | Required | Meaning |
|-------|----------|---------|
| description | yes | Human-readable case summary |
| parse | yes | Parse expectation object |
| 	ags | no | Free-form tags (if, or, expansion, ...) |

### parse object

| Field | Meaning |
|-------|---------|
| should_parse | When 	rue (or omitted with no error flags), require a clean parse tree and no syntax errors |
| should_parse: false | Pass only when the parse is not clean (errors and/or no usable tree) |
| expect_syntax_errors | Pass only when the implementation reports syntax errors |
| 	op_level_statement | Optional rule name of the **last script-level** statement (ifStmt, orStmt, setStmt, genericCmd, ...). Nested statements inside IF/FOR/group blocks are ignored |

should_parse: true must not be combined with expect_syntax_errors: true.
should_parse: false must not be combined with expect_syntax_errors: true.

## Scope

This corpus is **parse-structure** conformance. A case may still should_parse: true
for semantically dubious input (for example invalid %~ modifiers) when the goal is
to document tokenizer/parser acceptance rather than runtime validity.

Authoritative command syntax snippets for authors live under udit/cmd-help/.
