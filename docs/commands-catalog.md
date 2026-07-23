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

- Prefer `builtin_commands` for "is this a Windows/cmd command?" checks
- Use `common_external_tools` for optional recognition of developer tooling without implying cmd builtins
- Read deprecation/removal strings carefully: some `removed_commands` entries are add-on Resource Kit / Sysinternals tools, or HELP-listed names whose binaries are no longer present on modern Windows (for example `graftabl`)
