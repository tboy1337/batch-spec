# Expansion catalog

Machine-readable rules live in [`data/expansion.yaml`](../data/expansion.yaml)
(schema: [`schema/expansion.schema.json`](../schema/expansion.schema.json)).

Primary reference text is captured under [`audit/cmd-help/`](../audit/cmd-help/)
(`call-help.txt`, `set-help.txt`, `for-help.txt`, `if-help.txt`, `setlocal-help.txt`,
`shift-help.txt`, `exit-help.txt`, `goto-help.txt`, `cmd-help.txt`, `echo-help.txt`).

## Topics covered

- **Percent-tilde (`%~`)** - requires Command Extensions; letter modifiers (order-independent, case-insensitive), path search (`%~$ENV:n`, empty on miss), bare quote-strip (`%~1`), and the multi-digit batveat (`%~10` is `%~1` plus literal `0`). With extensions off, `%~` forms are not expanded (literal `~...`). `%~*` is semantically invalid (CALL /?) even when the letter-regex does not match it.
- **Percent expansion** - in scripts, undefined `%name%` / `!name!` expand to empty; on the interactive prompt undefined `%name%` often remains literal; incomplete unclosed `%` forms are not successful expansions (leading `%` typically stripped, leaving trailing text as literals).
- **Delayed expansion (`!var!`)** - does *not* require SETLOCAL; can be enabled via cmd `/V:ON`, SETLOCAL flags, or the Command Processor registry value. Supports substring/replace peers of the percent forms (case-insensitive search). Digit-leading names need bang forms; `!` escaping under delayed expansion is phase-sensitive. Disable via SETLOCAL DisableDelayedExpansion or `cmd /V:OFF`.
- **FOR variables / forms** - `%%i` in batch files, `%i` on the interactive command line; letter charset; `/D` `/R` `/L` `/F` forms (extensions); FOR `/R` without wildcards synthesizes `root\name` under each directory; FOR variables are global
- **FOR /F** - `eol` / `skip` / `delims` / `tokens` / `usebackq` (and live `useback` synonym), quote forms, consecutive-delimiter collapse, empty `delims=`, space-must-be-last in `delims`, case-sensitive delimiter chars, default first token, z/Z token ceiling
- **Caret escaping** - `2^n-1` for ordinary multilevel hops; CALL doubles carets on its tail (including inside quotes); line-continuation caret must be the last character of the physical line
- **Double percent** - batch `%%` literals; CALL also reduces `%%` pairs to `%` on its argument tail
- **String ops** - require Command Extensions; substring with negative offsets/lengths and omitted length; replace-all; empty replacement deletes; `*` prefix replace; case-insensitive `%var:old=new%` search; missing/empty substring batveat (`%NOSUCH:~-1%` / after `SET name=` yields literal `~-1`)
- **SET /A** - requires Command Extensions; operators with documented precedence, grouping, comma separator, hex/octal (not `0b` binary; `08`/`09` invalid), undefined-as-zero, bare names, 32-bit wrap on overflow, quoting rules; unary `!` interacts with delayed expansion; divide-by-zero leaves non-zero ERRORLEVEL
- **Plain SET assignment** - spaces around `=` become part of the name and/or value; prefix query (`SET P`); missing name/prefix sets ERRORLEVEL 1; `SET name=` unsets; `.bat` vs `.cmd` ERRORLEVEL after successful SET
- **SET /P** - optional prompt; EOF/NUL keeps prior value; pipe-side SET /P updates only the child cmd environment
- **Environment variable names** - `=` forbidden in names; live cmd accepts `.`, `-`, `~`, and spaced names (prefer underscore-alnum for portability). Lexer single-token `%name%` covers `.`/`-`/`~`; spaced names are runtime-only (tokenizer note in YAML).
- **ECHO** - blank-line forms (`ECHO.` `ECHO:` `ECHO/` and peers); bare/whitespace-only ECHO prints on/off status; `ECHO ON`/`OFF` and `@` suppression
- **CMD processor switches** - `/V` delayed expansion; `/E` Command Extensions; `/Q` echo off; `/D` disable AutoRun; `/A` ANSI / `/U` Unicode pipe/file output; `/F:ON|OFF` completion; `/T:fg` colors; defaults (extensions on, delayed off); compatibility aliases `/X`=`/E:ON`, `/Y`=`/E:OFF`, `/R`=`/C`; `/C` `/K` `/S` quote-stripping; AutoRun registry unless `/D`
- **Command Extensions off** - disable via `cmd /E:OFF`, `/Y`, registry, or `SETLOCAL DisableExtensions`; base IF ERRORLEVEL/`==`/EXIST remain; compare-ops/`/I`/DEFINED/CMDEXTVERSION, GOTO `:EOF` special target, CALL `:label`/`%*`/`%~`, SET `/A`, string ops, FOR `/D`/`/R`/`/L`/`/F`, SHIFT `/n`, and dynamic env names require extensions
- **SETLOCAL options** - Enable/Disable Extensions and DelayedExpansion (precedence over CMD `/E`/`/V`); nesting limit 32 ("Maximum setlocal recursion level reached."); argument ERRORLEVEL probe; ENDLOCAL restores prior state; `endlocal & set "out=%in%"` same-line survive trick
- **ERRORLEVEL / CMDEXTVERSION** - `IF ERRORLEVEL n` means `>= n`; dynamic `%ERRORLEVEL%` env-var shadowing; CMDEXTVERSION starts at 1 and never true when extensions are off
- **Dynamic environment variables** - `%CD%`, `%DATE%`, `%TIME%`, `%RANDOM%`, `%ERRORLEVEL%`, `%CMDEXTVERSION%`, `%CMDCMDLINE%`, `%HIGHESTNUMANODENUMBER%` (SET /?; extensions required)
- **Keyword boundaries** - do not glue keywords to `%`, `!`, or quotes (`IF%1`, `SET%x%` are not IF/SET)
- **IF forms / parentheses** - base and extension predicates; EXIST for files and directories; quoted compare sides are string compares; string order is not raw ASCII; unquoted empty operands are a syntax error; no native `and`/`or` keywords inside IF; open `(` on the same line as the predicate (spaces allowed); ELSE same-line attachment
- **Command chaining** - `&`, `&&`, `||`, `|`, and parenthesized groups; pipe sides run in child cmd contexts (delayed expansion defaults off in the child); `A && (B) || (C)` runs C when B fails even after successful A
- **Redirection** - `>`, `>>`, `<`, `n>`, `>&`, `<&` handle duplication, NUL suppress, group redirects, leading redirects, left-to-right handle order
- **Parenthesis-block expansion** - `%var%` expands when the block is parsed; `!var!` expands at execution when delayed expansion is on; dual pre-block / in-block values enable swap patterns
- **Batch parameters** - `%*` and `%~` require Command Extensions (literal `*` / `~...` when off); base `%0`-`%9` work without extensions; `%0` spelling mirrors CALL text; SHIFT `/n` and bare SHIFT; `%*` unaffected by SHIFT; unquoted args split on space/tab/comma/semicolon/equals
- **CALL / GOTO** - `CALL :label` return context; CALL requires colon for labels; missing CALL label continues with ERRORLEVEL 1; bare script invoke does not return (CALL does); `GOTO :EOF` vs `GOTO EOF`; case-insensitive user labels
- **EXIT** - bare `EXIT` ends the cmd process; `EXIT /B` ends the script/routine with optional exitCode
- **Remarks** - `REM` vs `::` label-style remarks; REM consumes the rest of the physical line (including a trailing `&`); a `::` line containing `)` inside `( )` can close the block early ? prefer REM in paren blocks

## Parse vs catalog

The ANTLR grammar is intentionally permissive for parse-structure conformance.

Forms that are semantically invalid (for example an unknown `%~` letter such as
`%~q1`, or `%~*` which CALL /? forbids) may still `should_parse: true` in the
corpus so tools can document tokenizer acceptance. Treat this YAML as the
semantic companion: see `invalid_combinations` and related notes for rejection
guidance. Consumers (for example Blinter) should treat this YAML as the semantic
companion to the ANTLR grammar, not as a full cmd.exe simulator.
