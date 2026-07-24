# Expansion catalog

Machine-readable rules live in [`data/expansion.yaml`](../data/expansion.yaml)

(schema: [`schema/expansion.schema.json`](../schema/expansion.schema.json)).

Primary reference text is captured under [`audit/cmd-help/`](../audit/cmd-help/) (`assoc-help.txt`, `break-help.txt`, `call-help.txt`, `cd-help.txt`, `choice-help.txt`, `cls-help.txt`, `cmd-help.txt`, `color-help.txt`, `copy-help.txt`, `date-help.txt`, `del-help.txt`, `dir-help.txt`, `echo-help.txt`, `endlocal-help.txt`, `exit-help.txt`, `find-help.txt`, `findstr-help.txt`, `for-help.txt`, `forfiles-help.txt`, `ftype-help.txt`, `goto-help.txt`, `if-help.txt`, `md-help.txt`, `mklink-help.txt`, `move-help.txt`, `path-help.txt`, `pause-help.txt`, `popd-help.txt`, `prompt-help.txt`, `pushd-help.txt`, `rd-help.txt`, `rem-help.txt`, `ren-help.txt`, `robocopy-help.txt`, `set-help.txt`, `setlocal-help.txt`, `setx-help.txt`, `shift-help.txt`, `start-help.txt`, `subst-help.txt`, `time-help.txt`, `timeout-help.txt`, `title-help.txt`, `type-help.txt`, `ver-help.txt`, `verify-help.txt`, `vol-help.txt`, `where-help.txt`, `xcopy-help.txt`, `chcp-help.txt`, `doskey-help.txt`, `help-help.txt`, `more-help.txt`, `sort-help.txt`).

## Topics covered

- **Percent-tilde (`%~`)** - requires Command Extensions; letter modifiers (order-independent, case-insensitive), path search (`%~$ENV:n`, empty on miss), bare quote-strip (`%~1`), attribute mask (`%~a`), short-name full paths (`%~sf`), locale timestamps (`%~t`), bare-vs-`f` qualification, and the multi-digit batveat (`%~10` is `%~1` plus literal `0`). With extensions off, `%~` forms are not expanded (literal `~...`). `%~*` is semantically invalid (CALL /?) even when the letter-regex does not match it.

- **Percent expansion** - in scripts, undefined `%name%` / `!name!` expand to empty; on the interactive prompt undefined `%name%` often remains literal; incomplete unclosed `%` forms are not successful expansions (leading `%` typically stripped, leaving trailing text as literals).

- **Delayed expansion (`!var!`)** - disabled by default; does *not* require SETLOCAL; enable via cmd `/V:ON`, SETLOCAL flags, or the Command Processor registry value. Independent of Command Extensions (plain `!var!` works with extensions off; substring/replace still need extensions). When disabled, `!var!` is literal. Supports substring/replace peers of the percent forms (case-insensitive search), FOR accumulate `!LIST!`, indirect `!%name%!` (percent then delayed); in-block `!prefix%name%!` still uses the pre-block percent value; values containing `!` can corrupt expansion; digit-leading names need bang forms; `!` escaping under delayed expansion is phase-sensitive. Disable via SETLOCAL DisableDelayedExpansion or `cmd /V:OFF`.

- **FOR variables / forms** - `%%i` in batch files, `%i` on the interactive command line; letter charset; `/D` `/R` `/L` `/F` forms (extensions); FOR `/R` with `(.)` includes the walk root; `/D /R` with `(*)` lists subdirs only; trailing `?` may match fewer characters; FOR `/R` without wildcards synthesizes `root\name` under each directory; FOR metavars expand in the DO body and share a session letter namespace (nested same-letter restores after inner); classic FOR non-wildcard set members are literals even when missing

- **FOR /F** - `eol` / `skip` / `delims` / `tokens` / `usebackq` (and live `useback` synonym), quote forms, consecutive-delimiter collapse, empty `delims=`, space-must-be-last in `delims`, case-sensitive delimiter chars, default first token, z/Z token ceiling; `eol=` skips lines whose first token starts with that character (mid-line occurrences stay data)

- **Caret escaping** - `2^n-1` for ordinary multilevel hops; CALL doubles carets on its tail (including inside quotes); line-continuation caret must be the last character of the physical line; caret does not escape `%` (percent expansion runs first; use `%%` for a literal percent in scripts)

- **Double percent** - batch `%%` literals; CALL also reduces `%%` pairs to `%` on its argument tail

- **String ops** - require Command Extensions; substring with negative offsets/lengths and omitted length; replace-all; empty replacement deletes; `*` prefix replace; case-insensitive `%var:old=new%` search; missing/empty substring batveat (`%NOSUCH:~-1%` / after `SET name=` yields literal `~-1`)

- **SET /A** - requires Command Extensions; operators with documented precedence, grouping, comma separator, hex/octal (`no_binary_literal`: not `0b` binary; `08`/`09` invalid), undefined-as-zero, bare names, 32-bit wrap on overflow, quoting rules; unary `!` interacts with delayed expansion; divide-by-zero leaves non-zero ERRORLEVEL; with extensions off, unquoted `set /A N=1+1` is a plain assignment whose name includes `/A` (quoted `set /A "..."` is a syntax error)

- **Plain SET assignment** - spaces around `=` become part of the name and/or value; prefix query (`SET P`, extensions); quoted `SET "name=value"` requires extensions; missing name/prefix sets ERRORLEVEL 1; `SET name=` unsets; `.bat` vs `.cmd` ERRORLEVEL matrix after successful SET/PATH/PROMPT/ASSOC/FTYPE (and SET /A / SET /P); APPEND is absent on modern hosts

- **SET /P** - requires extensions; optional prompt; EOF/NUL keeps prior value; a blank input line (Enter with no text) also keeps the prior value (does not assign empty); a spaces-only line assigns those spaces; `SET /P var=<file` reads the first line only; pipe-side SET /P updates only the child cmd environment

- **Environment variable names** - `=` forbidden in names; live cmd accepts `.`, `-`, `~`, spaces, and punctuation such as `@#$;[]` (prefer underscore-alnum for portability). Lexer `%name%` is a single PERCENT_VAR for any name chars other than `%`, `=`, or newlines.

- **ECHO** - blank-line forms (`ECHO.` `ECHO:` `ECHO/` `ECHO[` `ECHO]` and peers; `ECHO(` is WORD plus LPAREN); bare/whitespace-only ECHO prints on/off status; `ECHO ON`/`OFF` and `@` suppression

- **CMD processor switches** - `/V` delayed expansion; `/E` Command Extensions; `/Q` echo off; `/D` disable AutoRun; `/A` ANSI / `/U` Unicode pipe/file output; `/F:ON|OFF` completion (Ctrl-F / Ctrl-D and CompletionChar registry values); `/T:fg` colors; defaults (extensions on, delayed off); compatibility aliases `/X`=`/E:ON`, `/Y`=`/E:OFF`, `/R`=`/C`; `/C` `/K` `/S` quote-stripping; AutoRun registry unless `/D`

- **Command Extensions off** - disable via `cmd /E:OFF`, `/Y`, registry, or `SETLOCAL DisableExtensions`; base IF ERRORLEVEL/`==`/EXIST remain; compare-ops/`/I`/DEFINED/CMDEXTVERSION, GOTO `:EOF` special target, CALL `:label` jump/`%*`/`%~`, SET `/A`/`/P`, quoted SET, prefix query, string ops, FOR `/D`/`/R`/`/L`/`/F`, SHIFT `/n`, dynamic env names, CD `/D`, ASSOC/FTYPE/COLOR, and PROMPT `$+`/`$M` require extensions; delayed expansion remains independently switchable; under OFF, `set /A` and `set /P` become literal plain assignments whose names include the `/A` or `/P` token

- **SETLOCAL options** - four Enable/Disable Extensions and DelayedExpansion flags (precedence over CMD `/E`/`/V`; SETLOCAL /? still says "two valid arguments" while listing all four); nesting limit 32 per CALL level ("Maximum setlocal recursion level reached."); argument ERRORLEVEL probe; ENDLOCAL restores prior environment, Extensions/DelayedExpansion state, and current directory; `endlocal & set "out=%in%"` same-line (or paren-block) survive trick

- **ERRORLEVEL / CMDEXTVERSION** - `IF ERRORLEVEL n` means `>= n`; dynamic `%ERRORLEVEL%` env-var shadowing; CHOICE sets ERRORLEVEL to the 1-based choice ordinal (255 on tool error; CTRL+C/BREAK returns 0; /CS /T /D switches); CMDEXTVERSION starts at 1 and never true when extensions are off

- **Dynamic environment variables** - `%CD%`, `%DATE%`, `%TIME%`, `%RANDOM%`, `%ERRORLEVEL%`, `%CMDEXTVERSION%`, `%CMDCMDLINE%`, `%HIGHESTNUMANODENUMBER%` (SET /?; extensions required); `%TIME%` often space-pads hours 0-9; `%DATE%`/`%TIME%` follow locale-specific DATE/TIME formats (separators may include comma); `SET CD=...` shadows `%CD%` without changing process CWD

- **Keyword boundaries** - do not glue keywords to `%`, `!`, or quotes (`IF%1`, `SET%x%` are not IF/SET)

- **IF forms / parentheses** - base and extension predicates; EXIST (not EXISTS) for files and directories; quoted compare sides are string compares; string order is not raw ASCII; unquoted empty operands are a syntax error; classic `.%var%.` padding works only for simple values (breaks on spaces); no native `and`/`or` keywords inside IF; open `(` on the same line as the predicate (spaces allowed); ELSE same-line attachment

- **Command chaining** - `&`, `&&`, `||`, `|`, and parenthesized groups; on live cmd `&&` binds tighter than `||`; pipe sides run in concurrent child cmd contexts (delayed expansion and extensions default independently of parent SETLOCAL); `A && (B) || (C)` runs C when B fails even after successful A; ECHO/REM can succeed for chaining without clearing ERRORLEVEL; bare trailing `&` inside `( )` is a syntax error

- **Redirection** - `>`, `>>`, `<`, `n>`, `>&`, `<&` handle duplication, NUL suppress, group redirects, leading redirects, left-to-right handle order

- **Parenthesis-block expansion** - `%var%` expands when the block is parsed; `!var!` expands at execution when delayed expansion is on; nested blocks still expose only outermost-parse and current values; dual pre-block / in-block values enable swap patterns

- **Batch parameters** - `%*` and `%~` require Command Extensions (literal `*` / `~...` when off); base `%0`-`%9` work without extensions; `%10` is `%1` plus literal `0`; `%0` spelling mirrors CALL text; SHIFT `/n` and bare SHIFT; `%*` unaffected by SHIFT; unquoted args split on space/tab/comma/semicolon/equals

- **CALL / GOTO** - `CALL :label` return context; CALL requires colon for labels; missing CALL label continues with ERRORLEVEL 1; successful CALL without `EXIT /B` preserves prior ERRORLEVEL; bare script invoke does not return (CALL does); CALL context runs through later labels until EOF / `GOTO :EOF` / `EXIT /B`; `GOTO :EOF` vs `GOTO EOF`; case-insensitive user labels

- **Expanded GOTO/CALL targets** - `goto %name%` / `CALL :%name%` resolve after percent (or delayed) expansion; missing targets follow ordinary GOTO/CALL missing-label rules

- **Label charset** - label lines consume the rest of the physical line (spaces and punctuation allowed); ANTLR LABEL matches that form; CALL uses the first token after `:` as the label and the rest as arguments, while GOTO uses the remainder of the statement as the target (prefix-oriented matching)

- **EXIT** - bare `EXIT` ends the cmd process; `EXIT /B` ends the script/routine; omit exitCode to preserve ERRORLEVEL, or pass n to set it

- **Remarks** - `REM` vs `::` label-style remarks; REM consumes the rest of the physical line (including a trailing `&`); percent expansion still runs on REM lines (delayed `!` typically stays literal); a `::` line containing `)` inside `( )` can close the block early -- prefer REM in paren blocks

- **PROMPT `$` codes** - `$P$G`, `$T`, `$$`, and extensions `$+` / `$M` (PROMPT /?)

- **Command-line length** - cmd.exe accepts at most 8191 characters on a command line

- **Quoting** - double quotes suppress `&|<>^()` for command parsing but do not suppress percent or delayed `!` expansion; embedded `""` pairs inside a quoted arg are retained after `%~` outer-quote strip (`"a""b"` -> `a""b`)

- **Script encoding** - UTF-8/UTF-16 BOM prefixes the first token (breaking `@echo off`); prefer BOM-less ASCII/code-page text; CRLF preferred, LF usually works

- **Command resolution** - cwd then PATH with PATHEXT; bare missing external name sets ERRORLEVEL 9009; `CALL` of a missing external sets ERRORLEVEL 1

- **Directory commands** - CD `/D` changes drive; with extensions, CD normalizes case and accepts unquoted paths with spaces; PUSHD/POPD stack; UNC temp drives from Z: down (PUSHD /?)

- **MKDIR/MD** - with extensions, creates missing intermediate directories; without extensions parents must exist (MD /?)

- **RMDIR/RD** - `/S` removes a directory tree; `/Q` quiets `/S`; tree removal remains available with extensions off (RD /?)

- **COLOR** - two hex digits for background/foreground; same colors set ERRORLEVEL 1; unavailable when extensions are off (COLOR /?)

- **DEL/ERASE** - `/S` display shows only deleted files when extensions are on (DEL /?)

- **ASSOC/FTYPE** - extension associations and open-command strings; unavailable when extensions are off (ASSOC /?, FTYPE /?)

- **PATH command** - display/set path; `PATH ;` clears the search path

- **START** - quoted title, `/WAIT`, `/B`, `/I`; batch/internal often via new cmd; associations for non-executables

- **Expansion phases** - percent first, then caret/tokenize/execute; delayed `!` at execution; CALL reparses its tail

- **SET /A arithmetic details** -- integer `/` truncates toward zero; no `**` power operator (`^` is XOR); failed assignments leave the prior value; ERRORLEVEL codes for failures are implementation-defined

- **BREAK** -- DOS-compat internal; no-op for script control flow under Windows (does not break FOR/IF)

- **CHOICE defaults** -- omitted `/C` uses `YN`; `/C ABC` and `/C:ABC` both accepted

- **FOR /F unquoted options** -- caret-escaped `tokens^=...^ delims^=...` when quotes cannot wrap options

- **Label fallthrough** -- labels are not barriers; fence with `GOTO :EOF` / `EXIT /B`

- **@ prefix** -- suppresses echo of that one statement when ECHO is ON

- **SHIFT vacates** -- after SHIFT, vacated high `%n` slots expand empty

- **Remarks echo visibility** -- with ECHO ON, `REM` is echoed; `::` label-remarks typically are not

- **DIRCMD** -- ordinary env var supplying default `DIR` switches (DIR /?; `dir-help.txt`)

- **%PROMPT%** -- expands to the current prompt template

- **Special devices** -- `NUL`/`CON` reliable; `PRN`/`AUX`/`COM1`/`LPT1` redirects may fail on modern hosts

- **DATE / TIME / VERIFY** -- `/T` print-without-prompt (extensions); VERIFY ON/OFF; locale-tied formats for DATE/TIME

- **SETX / SUBST** -- persistent env (SETX space-delimited, not current session); SUBST virtual drives

- **COPY / MOVE / REN / DIR / TYPE** -- overwrite `/Y` defaults in batch; DIRCMD; REN in-place only; TYPE display

- **TITLE / PAUSE / CLS / VER / VOL / MKLINK** -- console/session builtins and link creation forms
- **CHCP / DOSKEY / HELP / MORE / SORT** -- code page, macros/history, help lookup, and common pipe filters

- **CHOICE** -- dedicated section: `/C` `/N` `/CS` `/T` `/D` `/M` and ERRORLEVEL ordinals

- **START** -- `/MIN` `/MAX` priority, `/NODE` `/AFFINITY`, `/D`, `/WAIT` `/B`

- **DEL/ERASE** -- `/P` `/F` `/S` `/Q` `/A` attributes; directory operand deletes files inside

- **External tool notes** -- FIND/FINDSTR ERRORLEVEL and `/C` OR-vs-literal; WHERE; FORFILES; ROBOCOPY bitmask vs `&&`; XCOPY; TIMEOUT `-1`..`99999`

## Parse vs catalog

The ANTLR grammar is intentionally permissive for parse-structure conformance.

Forms that are semantically invalid (for example an unknown `%~` letter such as

`%~q1`, or `%~*` which CALL /? forbids) may still `should_parse: true` in the

corpus so tools can document tokenizer acceptance. Treat this YAML as the

semantic companion: see `invalid_combinations` and related notes for rejection

guidance. Consumers (for example Blinter) should treat this YAML as the semantic

companion to the ANTLR grammar, not as a full cmd.exe simulator.

