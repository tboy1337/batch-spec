# Expansion catalog

Machine-readable rules live in [`data/expansion.yaml`](../data/expansion.yaml)

(schema: [`schema/expansion.schema.json`](../schema/expansion.schema.json)).

Primary reference text is captured under [`audit/cmd-help/`](../audit/cmd-help/) (`assoc-help.txt`, `attrib-help.txt`, `break-help.txt`, `call-help.txt`, `cd-help.txt`, `choice-help.txt`, `cls-help.txt`, `cmd-help.txt`, `color-help.txt`, `comp-help.txt`, `copy-help.txt`, `date-help.txt`, `del-help.txt`, `dir-help.txt`, `echo-help.txt`, `endlocal-help.txt`, `exit-help.txt`, `fc-help.txt`, `find-help.txt`, `findstr-help.txt`, `for-help.txt`, `forfiles-help.txt`, `ftype-help.txt`, `goto-help.txt`, `if-help.txt`, `md-help.txt`, `mklink-help.txt`, `move-help.txt`, `path-help.txt`, `pause-help.txt`, `popd-help.txt`, `prompt-help.txt`, `pushd-help.txt`, `rd-help.txt`, `reg-help.txt`, `reg-query-help.txt`, `rem-help.txt`, `ren-help.txt`, `replace-help.txt`, `robocopy-help.txt`, `set-help.txt`, `setlocal-help.txt`, `setx-help.txt`, `shift-help.txt`, `start-help.txt`, `subst-help.txt`, `time-help.txt`, `timeout-help.txt`, `title-help.txt`, `tree-help.txt`, `type-help.txt`, `ver-help.txt`, `verify-help.txt`, `vol-help.txt`, `where-help.txt`, `xcopy-help.txt`, `chcp-help.txt`, `doskey-help.txt`, `help-help.txt`, `more-help.txt`, `sort-help.txt`).

## Topics covered

- **Percent-tilde (`%~`)** - requires Command Extensions; letter modifiers (order-independent, case-insensitive), path search (`%~$ENV:n`, empty on miss; letter+`$` combos such as `%~dp$PATH:1`), bare quote-strip (`%~1`), attribute mask (`%~a`), short-name full paths (`%~sf`), locale timestamps (`%~t`), bare-vs-`f` qualification, and the multi-digit batveat (`%~10` is `%~1` plus literal `0`). With extensions off, `%~` forms are not expanded (literal `~...`). Invalid forms (`%~*`, unknown letters such as `%~q1`, `%~name%` spellings) are live syntax errors and the grammar reports them as such. The `invalid_combinations` letter-regex lists both cases (`nxfpdstaz` / `NXFPDSTAZ`) so uppercase forms such as `%~DPNX0` are not false-positive rejects.

- **Percent expansion** - in scripts, undefined `%name%` / `!name!` expand to empty; on the interactive prompt undefined `%name%` often remains literal; incomplete unclosed `%` forms are not successful expansions (leading `%` typically stripped, leaving trailing text as literals).

- **Delayed expansion (`!var!`)** - disabled by default; does *not* require SETLOCAL; enable via cmd `/V:ON`, SETLOCAL flags, or the Command Processor registry value. Independent of Command Extensions (plain `!var!` works with extensions off; substring/replace still need extensions). When disabled, `!var!` is literal. Supports substring/replace peers of the percent forms (case-insensitive search), FOR accumulate `!LIST!`, indirect `!%name%!` (percent then delayed); in-block `!prefix%name%!` still uses the pre-block percent value (use FOR metavar / CALL reparse such as `call echo %%food!city!%%`); SET-time values containing `!` can corrupt under delayed-on assignment; intact bang-bearing values are mangled by `%var%` re-scan under delayed expansion while `!var!` keeps embedded `!`; digit-leading names need bang forms; `!` escaping under delayed expansion is phase-sensitive (`^^!` → `!`, `^^^^!` → `^`). CALL can force a second percent-expansion pass (`call set "out=%%%name%%%"`). Disable via SETLOCAL DisableDelayedExpansion or `cmd /V:OFF`.

- **FOR variables / forms** - `%%i` in batch files, `%i` on the interactive command line; letter charset (letters preferred; digits/punctuation accepted but easy to clash with `%0`-`%9`); adjacent literal text sticks after expansion (`%%n0` is metavariable `n` plus literal `0`); undeclared `%%letter` becomes literal `%letter`; `/D` `/R` `/L` `/F` forms (extensions); FOR `/R` with `(.)` includes the walk root; `/D /R` with `(*)` lists subdirs only; `*` matches the rest of a name component (including dots); trailing `?` may match fewer characters; short 8.3 names can satisfy masks the long name would not; FOR `/R` without wildcards synthesizes `root\name` under each directory; FOR metavars expand in the DO body and share a session letter namespace (nested same-letter restores after inner); classic FOR non-wildcard set members are literals even when missing; `GOTO` from a DO body exits the loop early (`BREAK` does not)

- **FOR /F** - `eol` / `skip` / `delims` / `tokens` / `usebackq` (and live `useback` synonym), quote forms, consecutive-delimiter collapse (empty fields are skipped / tokens shift; leading delimiters likewise), empty `delims=`, space-must-be-last in `delims`, case-sensitive delimiter chars, default first token; `tokens=` implies further metavars by ASCII succession from the declared letter (live continues past `z`/`Z`, e.g. 27th from `%%a` is `%%{`, despite FOR /? “26” wording); `eol=` takes exactly one comment character (extra characters in the same `eol=` value commonly break parsing); empty `eol=` does not reliably disable comments; repeated option keywords use the last occurrence; blank lines in file/command-output input are skipped (a quoted `("a" "" "b")` file-set is not a blank-line probe); with `usebackq`, parentheses inside single-quoted strings commonly need `^(`/`^)`

- **Caret escaping** - `2^n-1` for ordinary multilevel hops; CALL doubles carets on its tail (including inside quotes); line-continuation caret must be the last character of the physical line; caret does not escape `%` (percent expansion runs first; use `%%` for a literal percent in scripts)

- **Double percent** - batch `%%` literals; CALL also reduces `%%` pairs to `%` on its argument tail; when ECHO-writing a child `.bat`/`.cmd`, `%%` in the parent becomes `%` in the child (defer expansion), while a single `%name%` expands while writing; caret write-hops reduce one escape pass per generation (`^^^>` → `^>`); with delayed expansion on, `^^!var^^!` writes `!var!` for the child

- **String ops** - require Command Extensions; substring with negative offsets/lengths and omitted length; past-end on a populated string yields empty (distinct from undefined/empty → literal `~offset`); length past end returns the remainder; replace-all; empty replacement deletes; `*` prefix replace; case-insensitive `%var:old=new%` search; missing/empty substring batveat (`%NOSUCH:~-1%` / after `SET name=` yields literal `~-1`); missing/empty replace batveat (`%NOSUCH:a=b%` / after `SET name=` yields literal `a=b`, and `*` forms yield `*a=b`; delayed `!…!` peers match); with extensions off, substring/replace forms expand to empty

- **SET /A** - requires Command Extensions; operators with documented precedence, grouping, comma separator, hex/octal (`no_binary_literal`: not `0b` binary; `08`/`09` invalid as literals), undefined-as-zero, bare names (silent leading-integer truncation of non-integer env values; bare vs `%name%` diverge on decimals; bare `v=010` is octal `8` while bare `08`/`09` truncate to `0` with EL 0), 32-bit wrap on overflow, signed `<<`/`>>` arithmetic shifts (SET /? says "logical shift"; live cmd is signed/arithmetic), quoting rules; unary `!` interacts with delayed expansion; divide-by-zero / invalid literals leave non-zero ERRORLEVEL (host-specific codes); decimal literals can fail yet partial-assign; expression-only forms (`set /A 1+2`) are valid (print interactively, silent in scripts); with extensions off, unquoted `set /A N=1+1` is a plain assignment whose name includes `/A` (quoted `set /A "..."` is a syntax error)

- **Plain SET assignment** - spaces around `=` become part of the name and/or value; prefix query (`SET P`, extensions); quoted `SET "name=value"` requires extensions; missing name/prefix sets ERRORLEVEL 1; `SET name=` unsets; `.bat` vs `.cmd` ERRORLEVEL matrix after successful SET/PATH/PROMPT/ASSOC/FTYPE (and SET /A / SET /P); APPEND is absent on modern hosts

- **SET /P** - requires extensions; optional prompt (prompt text is display-only on stdout, never taken from a pipe/redirect or `%*`); EOF/NUL keeps prior value; a blank input line (Enter with no text) also keeps the prior value (does not assign empty / cannot clear via blank Enter); a spaces-only line assigns those spaces; `SET /P var=<file` reads the first line only; pipe-side SET /P (and plain SET / SETLOCAL) updates only the child cmd environment

- **Environment variable names** - `=` forbidden in names; live cmd accepts `.`, `-`, `~`, spaces, and punctuation such as `@#$;[]` (prefer underscore-alnum for portability). Lexer `%name%` is a single PERCENT_VAR for any name chars other than `%`, `=`, or newlines.

- **ECHO** - blank-line forms (`ECHO.` `ECHO:` `ECHO/` `ECHO[` `ECHO]` and peers; `ECHO(` is WORD plus LPAREN); bare/whitespace-only ECHO prints on/off status; `ECHO ON`/`OFF` and `@` suppression; `ECHO OFF` does not suppress stderr

- **CMD processor switches** - `/V` delayed expansion; `/E` Command Extensions; `/Q` echo off; `/D` disable AutoRun; `/A` ANSI / `/U` Unicode pipe/file output; `/F:ON|OFF` completion (Ctrl-F / Ctrl-D and CompletionChar registry values); `/T:fg` colors; defaults (extensions on, delayed off); compatibility aliases `/X`=`/E:ON`, `/Y`=`/E:OFF`, `/R`=`/C`; `/C` `/K` `/S` quote-stripping; AutoRun registry unless `/D`

- **Command Extensions off** - disable via `cmd /E:OFF`, `/Y`, registry, or `SETLOCAL DisableExtensions`; base IF ERRORLEVEL/`==`/EXIST remain; compare-ops/`/I`/DEFINED/CMDEXTVERSION, GOTO `:EOF` special target, CALL `:label` jump/`%*`/`%~`, SET `/A`/`/P`, quoted SET, prefix query, string ops, FOR `/D`/`/R`/`/L`/`/F`, SHIFT `/n`, dynamic env names, CD `/D`, ASSOC/FTYPE/COLOR, and PROMPT `$+`/`$M` require extensions; delayed expansion remains independently switchable; under OFF, `set /A` and `set /P` become literal plain assignments whose names include the `/A` or `/P` token

- **SETLOCAL options** - four Enable/Disable Extensions and DelayedExpansion flags (precedence over CMD `/E`/`/V`; SETLOCAL /? still says "two valid arguments" while listing all four); bare `SETLOCAL` inherits the current Enable/Disable state into a new nested scope; nesting limit 32 per CALL level ("Maximum setlocal recursion level reached."); argument ERRORLEVEL probe; ENDLOCAL restores prior environment, Extensions/DelayedExpansion state, and current directory; `endlocal & set "out=%in%"` same-line (or paren-block) survive trick

- **ERRORLEVEL / CMDEXTVERSION** - `IF ERRORLEVEL n` means `>= n`; dynamic `%ERRORLEVEL%` env-var shadowing; `cmd /C exit N` resets ERRORLEVEL without shadowing; bare `call` / `(call)` force ERRORLEVEL 1 and `call ` / `(call )` (trailing space) force 0; CHOICE sets ERRORLEVEL to the 1-based choice ordinal (255 on tool error; CTRL+C/BREAK returns 0; /CS /T /D switches); CMDEXTVERSION starts at 1 and never true when extensions are off; live Windows 10/11 reports `%CMDEXTVERSION%=2`

- **Dynamic environment variables** - `%CD%`, `%DATE%`, `%TIME%`, `%RANDOM%`, `%ERRORLEVEL%`, `%CMDEXTVERSION%`, `%CMDCMDLINE%`, `%HIGHESTNUMANODENUMBER%` (SET /?; extensions required); `%TIME%` often space-pads hours 0-9 (`%TIME: =0%` zero-pads); `%DATE%`/`%TIME%` follow locale-specific DATE/TIME formats (separators may include comma); `SET CD=...` shadows `%CD%` without changing process CWD; `%RANDOM% %% N` is biased unless N divides 32768; ordinary startup env (`COMPUTERNAME`, `USERNAME`, `TEMP`, …) appears in SET listings and is distinct from these dynamic names; `%CMDCMDLINE%` is process-original (Explorer-style launches often embed the script path; interactive consoles often show only comspec) and unchanged across in-process `CALL` of other scripts

- **Keyword boundaries** - do not glue keywords to `%`, `!`, quotes, or `)` (`IF%1`, `SET%x%`, `rem)`, `if)` are not IF/SET/REM)

- **IF forms / parentheses** - base and extension predicates; EXIST (not EXISTS) for files and directories; quoted compare sides are string compares; string order is not raw ASCII (digits before letters; letter-case chain `a` < `A` < `b` < `B`); letter-vs-digit unquoted compares are string compares (`A` GTR `9`); unquoted empty operands are a syntax error; classic `.%var%.` padding works only for simple values (breaks on spaces); no native `and`/`or` keywords inside IF; `else if` is same-line ELSE plus another IF (not a separate keyword); open `(` on the same line as the predicate (spaces allowed); ELSE same-line attachment (newline-detached ELSE is an unknown command; a following orphan `(block)` may still run); `IF %ERRORLEVEL% n` without a compare-op is a syntax error; the full predicate text may come from expansion (`set "b=a==a"` then `if %b%`)

- **Command chaining** - `&`, `&&`, `||`, `|`, and parenthesized groups; on live cmd `&&` binds tighter than `||`; `&&`/`||` are not the same as `IF %ERRORLEVEL% EQU 0` (ECHO/REM/`.bat` SET and CALLed scripts can succeed without clearing ERRORLEVEL); after a successful `||` alternative later alternatives are skipped (including a trailing `&&` grouped into a later alternative); pipe sides run in concurrent child cmd contexts (child delayed/extensions default independently of parent SETLOCAL); parent ERRORLEVEL after a pipe is the rightmost stage's exit code; with parent delayed expansion on, `!var!` in the pipeline text is still expanded by the parent; `A && (B) || (C)` runs C when B fails even after successful A; bare trailing `&` inside `( )` is a syntax error

- **Redirection** - `>`, `>>`, `<`, `n>`, `>&`, `<&` handle duplication, NUL suppress, group redirects, leading redirects, left-to-right handle order

- **Parenthesis-block expansion** - `%var%` expands when the block is parsed; `!var!` expands at execution when delayed expansion is on; nested blocks still expose only outermost-parse and current values; dual pre-block / in-block values enable swap patterns

- **Batch parameters** - `%*` and `%~` require Command Extensions (literal `*` / `~...` when off); base `%0`-`%9` work without extensions; `%10` is `%1` plus literal `0`; `%0` spelling mirrors CALL/invocation text (Explorer-style `cmd /c ""fullpath""` commonly yields a quoted full-path `%0`; relative CLI typing keeps the as-typed spelling); do not redirect into `%0` (can overwrite the running script); drag-and-drop / Open-with of multiple files typically delivers each path as its own quoted argument; SHIFT `/n` and bare SHIFT; `%*` is `%1 %2 ...` (never includes `%0`) and is unaffected by SHIFT; empty quoted `""` occupies a slot (`%1` is `""`, `%~1` empty); unquoted args split on space/tab/comma/semicolon/equals (`a=b` → two slots while `%*` keeps `a=b`)

- **CALL / GOTO** - `CALL :label` return context; CALL requires colon for labels; missing CALL label continues with ERRORLEVEL 1; successful CALL without `EXIT /B` preserves prior ERRORLEVEL; `EXIT /B` after `CALL :label` returns while `EXIT /B` after `GOTO :label` ends the script; bare `CALL` of a successful non-label non-script command (for example `call echo ok` / `call set ...`) clears ERRORLEVEL to 0; `CALL other.cmd` returns the child's final ERRORLEVEL (ECHO/REM often do not clear, so a child that only echoes can preserve the pre-CALL code; `EXIT /B n` sets it); bare script invoke does not return (CALL does); bare external `.exe` returns without CALL; CALL inherits the caller's CWD (cmd does not auto-cd to the script directory); CALL context runs through later labels until EOF / `GOTO :EOF` / `EXIT /B` (unfenced fallthrough to physical EOF returns; a later mainline EOF exits); deep recursive CALL aborts near stack limits ("BATCH RECURSION exceeds STACK limits"; host-dependent depth, separate from SETLOCAL's 32 cap); `GOTO :EOF` vs `GOTO EOF`; case-insensitive user labels

- **Expanded GOTO/CALL targets** - `goto %name%` / `CALL :%name%` resolve after percent (or delayed) expansion; missing targets follow ordinary GOTO/CALL missing-label rules

- **Label charset** - label lines consume the rest of the physical line (spaces and punctuation allowed); indented labels are accepted (prefer column 0); ANTLR LABEL matches that form; CALL uses the first token after `:` as the label and the rest as arguments, while GOTO uses the remainder of the statement as the target (prefix-oriented matching); `::` is the remark form; later colons in jump labels (for example `:ok:extra`) are allowed

- **EXIT** - bare `EXIT` ends the cmd process; `EXIT n` (no `/B`) ends the process with that exit code; `EXIT /B` ends the script/routine; omit exitCode on `/B` to preserve ERRORLEVEL on CALL return, or pass n to set it; top-level bare `EXIT /B` under `cmd /C` may still yield process exit 0

- **Remarks** - `REM` vs `::` label-style remarks; REM as the command verb (line-start or after `&` / `&&` / `||`) remarks out the rest of the physical line (including a trailing `&` and any `>` redirect on that line); glued forms such as `REMCASE` are not REM; punctuation-glued forms (`rem.` `rem/` `rem:` `rem]` `rem)` and peers) are also not REM on live cmd so a trailing `&` command still runs, while `rem(` without a space remains REM and absorbs the line; percent expansion still runs on REM lines (delayed `!` typically stays literal); a `::` line containing `)` inside `( )` can close the block early on some hosts -- prefer REM in paren blocks; real jump labels must not use `:` in the second character (`::` remark), but later colons (for example `:ok:extra`) are valid

- **PROMPT `$` codes** - `$P$G`, `$T`, `$$`, and extensions `$+` / `$M` (PROMPT /?); bare PROMPT restores displayed `$P$G` and clears the PROMPT env var

- **Command-line length** - cmd.exe accepts at most 8191 characters on a command line

- **Quoting** - double quotes suppress `&|<>^()` for command parsing but do not suppress percent or delayed `!` expansion; embedded `""` pairs inside a quoted arg are retained after `%~` outer-quote strip (`"a""b"` -> `a""b`)

- **Script encoding** - UTF-8 BOM prefixes the first token (breaking `@echo off`); UTF-16 BOM typically garbles the line worse; prefer BOM-less ASCII/code-page text; CRLF preferred, LF usually works

- **Command resolution** - cwd then PATH with PATHEXT; bare missing external name sets ERRORLEVEL 9009; `CALL` of a missing external sets ERRORLEVEL 1

- **Directory commands** - CD `/D` changes drive; with extensions, CD normalizes case and accepts unquoted paths with spaces; PUSHD/POPD stack; UNC temp drives from Z: down (PUSHD /?)

- **MKDIR/MD** - with extensions, creates missing intermediate directories; without extensions parents must exist (MD /?)

- **RMDIR/RD** - `/S` removes a directory tree; `/Q` quiets `/S`; tree removal remains available with extensions off (RD /?)

- **COLOR** - two hex digits for background/foreground (COLOR /?: background then foreground; some Learn pages invert that order in prose), or a single hex digit to set foreground only; COLOR /? documents ERRORLEVEL 1 for same fg/bg; Microsoft Learn/SS64 describe success as 0, but live Windows 10/11 cmd leaves ERRORLEVEL 1 after successful COLOR too (not &&-friendly); unavailable when extensions are off (COLOR /?)

- **DEL/ERASE** - `/P` `/F` `/S` `/Q` `/A` attributes; `/S` display shows only deleted files when extensions are on (DEL /?); directory operand deletes files inside; deleting a nonexistent file often leaves ERRORLEVEL 0 despite a stderr message

- **ASSOC/FTYPE** - extension associations and open-command strings; unavailable when extensions are off (ASSOC /?, FTYPE /?)

- **PATH command** - display/set path; `PATH ;` clears the search path

- **START** - quoted title, `/WAIT`, `/B`, `/I`, `/MIN` `/MAX` priority, `/NODE` `/AFFINITY`, `/D`; batch/internal often via new cmd; associations for non-executables; `/WAIT` propagates the child's exit code into ERRORLEVEL; without `/WAIT`, START typically returns promptly with ERRORLEVEL 0 while the child continues

- **Expansion phases** - percent first, then caret/tokenize/execute; delayed `!` at execution; CALL reparses its tail

- **SET /A arithmetic details** -- integer `/` truncates toward zero; no `**` power operator (`^` is XOR); Invalid number / divide-by-zero leave the prior value; decimal literals can fail yet partial-assign; bare names silently truncate non-integer env values (including bare octal `010` → `8` and bare `08`/`09` → `0`); ERRORLEVEL codes for failures are implementation-defined

- **BREAK** -- DOS-compat internal; no-op for script control flow under Windows (does not break FOR/IF)

- **CHOICE defaults** -- omitted `/C` uses `YN`; `/C ABC` and `/C:ABC` both accepted; without `/N` the prompt appends `[choices]?`; `/N` hides that entire trailing list including the auto-`?`; keys outside `/C` beep and wait for a listed key

- **FOR /F unquoted options** -- caret-escaped `tokens^=...^ delims^=...` when quotes cannot wrap options

- **Label fallthrough** -- labels are not barriers; fence with `GOTO :EOF` / `EXIT /B`

- **@ prefix** -- suppresses echo of that one statement when ECHO is ON

- **SHIFT vacates** -- after SHIFT, vacated high `%n` slots expand empty

- **Remarks echo visibility** -- with ECHO ON, `REM` is echoed; `::` label-remarks typically are not

- **DIRCMD** -- ordinary env var supplying default `DIR` switches (DIR /?; `dir-help.txt`)

- **%PROMPT%** -- expands to the current prompt template when set; empty after a bare PROMPT reset

- **Special devices** -- `NUL`/`CON` reliable; `PRN`/`AUX`/`COM1`/`LPT1` redirects may fail on modern hosts

- **DATE / TIME / VERIFY** -- `/T` print-without-prompt (extensions); VERIFY ON/OFF; locale-tied formats for DATE/TIME

- **SETX / SUBST** -- persistent env (SETX space-delimited, not current session); SUBST virtual drives

- **COPY / MOVE / REN / DIR / TYPE** -- overwrite `/Y` defaults in batch; `copy nul file` empty-file idiom; DIRCMD; REN in-place only; TYPE display (EL 0 success / 1 missing file); TYPE then `>>` append glues onto a final line that lacked CRLF

- **TITLE / PAUSE / CLS / VER / VOL / MKLINK** -- console/session builtins and link creation forms; TITLE keeps surrounding/embedded quotes as literal title-bar text
- **CHCP / DOSKEY / HELP / MORE / SORT** -- code page, macros/history, help lookup, and common pipe filters; SORT `/UNIQUE` (prefix `/UNIQ`) drops duplicate lines (Microsoft Learn; local SORT /? may omit it)

- **CHOICE** -- dedicated section: `/C` `/N` `/CS` `/T` `/D` `/M` and ERRORLEVEL ordinals

- **External tool notes** -- FIND/FINDSTR ERRORLEVEL (match 0 / no-match 1; FINDSTR missing file EL 1; FIND missing named file EL 1 on live Win10/11, EL 2 for invalid switch or empty wildcard mask), `/C` OR-vs-literal, default regex vs `/L`/`/R`, `/E`/`/X` trailing-newline quirk; WHERE (EL 0 hit / 1 miss); FORFILES (EL 0 hit / 1 no-match, `@file` placeholders); FC (EL 0/1/2/-1); COMP (EL 0/1/2, `/M` no-prompt); ATTRIB / TREE (missing path often EL 0); REG QUERY (EL 0 success / 1 fail including missing key); REPLACE (EL 0 including "No files replaced" / missing named source under existing path; EL 3 path not found; EL 11 bad syntax/switch; live often not EL 2 for missing named file); ROBOCOPY bitmask vs `&&`; ROBOCOPY `/MOV` (files) vs `/MOVE` (files and dirs); ROBOCOPY missing named file (existing source dir) often EL 0 vs missing source path often EL 16 vs XCOPY often EL 4; TIMEOUT `-1`..`99999`

- **SET /A integers only** -- no floating-point type; unary `!` conflicts with delayed expansion; bare-name truncation vs expanded decimals; expression-only forms silent in scripts

- **Delayed bang poison** -- with delayed expansion on, unescaped `!` in SET values can corrupt the stored value at assignment time

- **CALL reparse** -- each CALL halves `%%` on its argument tail before re-parsing; CALL can also drive a second percent-expansion pass for indirect assignment (`call set "out=%%%name%%%"`)

## Parse vs catalog

The ANTLR grammar reports syntax errors for forms that live `cmd.exe` rejects
as syntax (for example invalid `%~` modifiers / `%~*`, empty unquoted IF
operands, `IF EXISTS` misspelling, `IF %ERRORLEVEL% n` without a compare-op,
and multi-character `FOR /F eol=` values). Corpus fixtures for those forms use
`expect_syntax_errors: true`.

Forms that fail only at runtime with non-syntax behavior (wrong ERRORLEVEL,
"not recognized", sticky success codes, expansion batveats) may still
`should_parse: true`. Treat [`data/expansion.yaml`](../data/expansion.yaml) as
the semantic companion for those cases — see `invalid_combinations` and related
notes. Consumers (for example Blinter) should use the YAML alongside the
grammar, not as a full cmd.exe simulator.

