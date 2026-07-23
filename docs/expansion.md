# Expansion catalog

Machine-readable rules live in [`data/expansion.yaml`](../data/expansion.yaml)
(schema: [`schema/expansion.schema.json`](../schema/expansion.schema.json)).

Primary reference text is captured under [`audit/cmd-help/`](../audit/cmd-help/)
(`call-help.txt`, `set-help.txt`, `for-help.txt`, `if-help.txt`, `setlocal-help.txt`).

## Topics covered

- **Percent-tilde (`%~`)** — letter modifiers, path search (`%~$ENV:n`), bare quote-strip (`%~1`), and the multi-digit batveat (`%~10` → `%~1` + literal `0`)
- **Delayed expansion (`!var!`)** — does **not** require `SETLOCAL`; can be enabled via `cmd /V:ON`, SETLOCAL flags, or the Command Processor registry value. Supports substring/replace peers of the percent forms. Digit-leading names need `!…!`
- **FOR variables** — `%%` in batch files, `%` on the interactive command line; letter charset includes digits and many punctuation characters
- **Caret escaping** — phase-driven; `CALL` doubles carets on its tail (including inside quotes)
- **String ops** — substring with negative offsets/lengths; `*prefix` replace; empty-defined substring batveat
- **SET /A** — operator inventory, hex/octal literals, `%%` modulo in batch files
- **SETLOCAL options** — Enable/Disable Extensions and DelayedExpansion; nesting limits
- **ERRORLEVEL / CMDEXTVERSION** — `IF ERRORLEVEL n` means ≥ n; CMDEXTVERSION never true when extensions are off
- **Remarks** — `REM` vs `::` label-style remarks

Consumers (for example Blinter) should treat this YAML as the semantic companion to the ANTLR grammar, not as a full cmd.exe simulator.
