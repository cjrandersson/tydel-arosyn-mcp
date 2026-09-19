# Reference library

Official documents and format definitions to help us build Tydel correctly.
This is a research collection, not a complete or production-approved rule set.

Start with the [reading guide](../docs/research/reading-guide.md), then use the
[source index](INDEX.md) and [download inventory](INVENTORY.md).

## What goes where

| Path | Contents |
| --- | --- |
| [`catalogs/`](catalogs/) | Source URLs, publishers, edition hints and storage rules |
| [`sweden/`](sweden/) | Entry points for Swedish Ediel and market processes |
| [`nordic/`](nordic/) | Nordic EDIFACT, XML, NBS and eSett references |
| [`mcp/`](mcp/) | MCP reading order and version notes |
| [`vendor/mcp/`](vendor/mcp/) | Pinned upstream MCP specification and schema files, with their license |
| [`download-lock.json`](download-lock.json) | Download date, original URL, byte count and SHA-256 |
| `.cache/references/` | Local-only downloads, separated by collection, source ID and checksum |
| [`../docs/research/`](../docs/research/) | Our findings and questions, not copies of specifications |
| [`../fixtures/`](../fixtures/) | Our synthetic test messages, separate from source material |

## Download and verify

The helper needs Python 3.10+ and no third-party packages. It does not install or
run Tydel, send anything to an AI model, crawl websites or extract archives.

```bash
# Show the available source records.
python3 scripts/reference_library.py list

# Restore the openly licensed MCP files if needed.
python3 scripts/reference_library.py fetch

# Fetch permitted public references into the Git-ignored local cache.
python3 scripts/reference_library.py fetch --include-cache

# Also include historical Swedish instructions and natural-gas references.
python3 scripts/reference_library.py fetch --include-cache --include-archive

# Check files in Git, then optionally the entire downloaded collection.
python3 scripts/reference_library.py verify
python3 scripts/reference_library.py verify --include-cache --include-archive

# Refresh the human-readable index and inventory from local records.
python3 scripts/reference_library.py report
```

Use `--group ediel-se` or `--id se-ediel-3314` to work on a small subset. Fetching
an already verified file is a no-op. Changed upstream bytes cause an error; add
and review a new edition rather than silently replacing the locked original.

Only `vendor/` originals are included in a Git clone. A download entry in the lock
does not mean the local cache exists on another computer. The cache is not a
permanent backup; reconstruct it from the catalogue and locked checksums.

## Access and reuse

| Storage | What it means |
| --- | --- |
| `vendored` | Included in the public repository under the retained upstream license |
| `cache` | Public reference downloaded locally; public redistribution has not been cleared |
| `link-only` | Not downloaded; permission, bundle contents or format need review |

Read [source permissions](../docs/research/source-permissions.md) before sharing,
indexing or training on any material. `cache` is a storage policy, **not a license**.

The tool deliberately skips eSett and ENTSO-E downloads, including restricted
bundles. There is no flag to bypass that decision. Their source links remain in
the index so we know what needs permission.

## Read the metadata carefully

- `version_hint` may come from a filename. `verified_edition` and
  `version_evidence` record selected cover checks; MCP versions use pinned upstream
  paths. `version_verified` does not resolve conflicting publisher labels.
- `effective_from: null` means unknown, not "valid now".
- `listed-not-adopted` means present in the reviewed source index, not chosen for
  Tydel. Archive, draft and gas documents are explicitly separated.
- The lock checks downloaded bytes and basic containers, not Ediel compliance.
- An XSD may depend on other schemas. Downloading it alone does not prove that a
  complete, compatible validation set is available.
