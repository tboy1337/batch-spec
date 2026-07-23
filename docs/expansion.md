# Expansion catalog

Machine-readable rules live in [`data/expansion.yaml`](../data/expansion.yaml)
(schema: [`schema/expansion.schema.json`](../schema/expansion.schema.json)).

Primary reference text is captured under [`audit/cmd-help/`](../audit/cmd-help/)
(`call-help.txt`, `set-help.txt`, `for-help.txt`, `if-help.txt`, `setlocal-help.txt`,
`shift-help.txt`, `exit-help.txt`, `goto-help.txt`, `cmd-help.txt`, `echo-help.txt`).

## Topics covered

- **Percent-tilde (`%~`)** - letter modifiers (order-independent), path search (`%~$ENV:n`, empty on miss), bare quote-strip (`%~1`), and the multi-digit batveat (`%~10` is `%~1` plus literal `0`). `%~*` is semantically invalid (CALL /?) even when the letter-regex does not match it.
- **Percent expansion** - undefined `%name%` / `!name!` expand to empty; incomplete unclosed `%` forms are not successful expansions.
- **Delayed expansion (`!var!`)** - does *not* require SETLOCAL; can be enabled via cmd `/V:ON`, SETLOCAL flags, or the Command Processor registry value. Supports substring/replace peers of the percent forms (case-insensitive search). Digit-leading names need bang forms; `!` escaping under delayed expansion is phase-sensitive. Disable via SETLOCAL DisableDelayedExpansion or `cmd /V:OFF`.
- **FOR variables / forms** - `%%i` in batch files, `%i` on the interactive command line; letter charset; `/D` `/R` `/L` `/F` forms
- **FOR /F** - `eol` / `skip` / `delims` / `tokens` / `usebackq` (and live `useback` synonym), quote forms, consecutive-delimiter collapse, empty `delims=`
- **Caret escaping** - `2^n-1` for ordinary multilevel hops; CALL doubles carets on its tail (including inside quotes)
- **Double percent** - batch `%%` literals; CALL also reduces `%%` pairs to `%` on its argument tail
- **String ops** - substring with negative offsets/lengths and omitted length; `*` prefix replace; case-insensitive `%var:old=new%` search; missing/empty substring batveat (`%NOSUCH:~-1%` / after `SET name=` yields literal `~-1`)
- **SET /A** - operators, grouping, comma separator, hex/octal (not `0b` binary), undefined-as-zero, bare names, 32-bit range, quoting rules; unary `!` interacts with delayed expansion
- **Plain SET assignment** - spaces around `=` become part of the name and/or value; prefix query (`SET P`); missing name/prefix sets ERRORLEVEL 1; `SET name=` unsets
- **SET /P** - optional prompt; EOF/NUL keeps prior value; pipe-side SET /P updates only the child cmd environment
- **Environment variable names** - `=` forbidden in names; live cmd accepts `.`, `-`, `~`, and spaced names (prefer underscore-alnum for portability). Lexer single-token `%name%` covers `.`/`-`/`~`; spaced names are runtime-only (tokenizer note in YAML).
- **ECHO** - blank-line forms (`ECHO.` `ECHO:` `ECHO/` and peers); `ECHO ON`/`OFF` and `@` suppression
- **CMD processor switches** - `/V` delayed expansion; `/E` Command Extensions; `/C` `/K` `/S` quote-stripping rules
- **SETLOCAL options** - Enable/Disable Extensions and DelayedExpansion; nesting limits; argument ERRORLEVEL probe; `endlocal & set "out=%in%"` same-line survive trick
- **ERRORLEVEL / CMDEXTVERSION** - `IF ERRORLEVEL n` means `>= n`; dynamic `%ERRORLEVEL%` env-var shadowing; CMDEXTVERSION never true when extensions are off
- **Dynamic environment variables** - `%CD%`, `%DATE%`, `%TIME%`, `%RANDOM%`, `%ERRORLEVEL%`, `%CMDEXTVERSION%`, `%CMDCMDLINE%`, `%HIGHESTNUMANODENUMBER%` (SET /?; extensions required)
- **Keyword boundaries** - do not glue keywords to `%`, `!`, or quotes (`IF%1`, `SET%x%` are not IF/SET)
- **IF forms / parentheses** - base and extension predicates; open `(` on the same line as the predicate (spaces allowed); ELSE same-line attachment
- **Command chaining** - `&`, `&&`, `||`, `|`, and parenthesized groups; pipe sides run in child cmd contexts
- **Redirection** - `>`, `>>`, `<`, `n>`, `>&`, `<&` handle duplication, NUL suppress, group redirects, leading redirects, left-to-right handle order
- **Parenthesis-block expansion** - `%var%` expands when the block is parsed; `!var!` expands at execution when delayed expansion is on
- **Batch parameters** - `%*`, `%0`, SHIFT `/n`, `%*` unaffected by SHIFT
- **CALL / GOTO** - `CALL :label` return context; `GOTO :EOF` end-of-file target vs `GOTO EOF` ordinary label search
- **EXIT** - `EXIT /B` and optional exitCode
- **Remarks** - `REM` vs `::` label-style remarks; REM consumes the rest of the physical line (including a trailing `&`)

## Parse vs catalog

The ANTLR grammar is intentionally permissive for parse-structure conformance.

Forms that are semantically invalid (for example an unknown `%~` letter such as
`%~q1`, or `%~*` which CALL /? forbids) may still `should_parse: true` in the
corpus so tools can document tokenizer acceptance. Treat this YAML as the
semantic companion: see `invalid_combinations` and related notes for rejection
guidance. Consumers (for example Blinter) should treat this YAML as the semantic
companion to the ANTLR grammar, not as a full cmd.exe simulator.
