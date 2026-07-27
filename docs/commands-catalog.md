# Commands catalog

Machine-readable catalog: [`data/commands.yaml`](../data/commands.yaml)
(schema: [`schema/commands.schema.json`](../schema/commands.schema.json)).

## Sections

| Key | Purpose |
|-----|---------|
| `builtin_commands` | cmd.exe internals and stock Windows utilities |
| `common_external_tools` | Third-party / language / package-manager CLIs commonly recognized by tooling |
| `deprecated_commands` | Still present or optionally available, but deprecated for new use |
| `removed_commands` | Historical commands no longer part of modern Windows cmd |
| `older_windows_commands` | DOS-era / legacy names retained for detection |
| `common_command_typos` | Frequent misspellings mapped to intended commands |
| `builtin_overlap_deprecated_notes` | Notes when a name is both detected as builtin and flagged deprecated |

## Guidance

- `builtin_commands` includes both cmd.exe internals (for example `set`, `call`, `break`) and stock Windows utilities resolved via PATH/`System32` (for example `curl`, `robocopy`, `choice`, `hostname`, `explorer`, `label`, `where`). For the machine name in scripts prefer `%COMPUTERNAME%`; `hostname` is the external `hostname.exe` printer, not a cmd internal. True internals are never overridden by a same-named file in the current directory, but external catalog entries can be shadowed by a CWD `.bat`/`.cmd`/`.exe` according to PATHEXT (see `command_resolution.cwd_shadows_externals` in [`data/expansion.yaml`](../data/expansion.yaml)).
- Prefer `builtin_commands` for "is this a Windows/cmd command?" checks
- Use `common_external_tools` for optional recognition of developer tooling without implying cmd builtins
- Stock utilities such as `curl`, `tar`, and `telnet` remain in `builtin_commands` for detection, but may be absent on older or Feature-on-Demand-stripped hosts (`builtin_overlap_deprecated_notes`)
- Read deprecation/removal strings carefully: some `removed_commands` entries are add-on Resource Kit / Sysinternals tools, or HELP-listed names whose binaries are no longer present on modern Windows (for example `graftabl`, or `edlin` on 64-bit hosts). Some `deprecated_commands` remain as cmd internals with no useful effect (for example `keys`).
- Captured help under [`audit/cmd-help/`](../audit/cmd-help/) is a language-relevant subset (internals and high-impact stock tools such as `find` / `findstr` / `robocopy` / `fc` / `comp` / `attrib` / `tree` / `reg` / `replace`), not a full dump of every `builtin_commands` name. Alias pairs share one help file (`cd`/`chdir`, `md`/`mkdir`, `rd`/`rmdir`, `del`/`erase`, `ren`/`rename`)
