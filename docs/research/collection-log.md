# Reference collection — 2026-09-19

## Scope

Collect the important public specifications and formats for Tydel, organize them
for people and Codex, and keep source provenance. No application implementation,
production integration, embeddings or model training were added.

The collection covers Swedish Ediel instructions and code lists, Nordic EDIFACT
guides, NMEG/XML/NBS material, the Swedish market handbook and pinned MCP sources.
Relevant eSett, ENTSO-E, UNECE, regulatory and standards entry points are also
catalogued. It is not an exhaustive crawl of every linked website or standard.

The [inventory](../../reference/INVENTORY.md) gives exact downloaded, vendored,
local-cache and link-only counts. The [source index](../../reference/INDEX.md)
shows the individual records.

## Work completed

- Created source catalogues grouped by publisher and purpose.
- Downloaded permitted reference originals without altering their bytes.
- Recorded original/resolved URLs, timestamps, sizes, formats and SHA-256 hashes.
- Included a pinned MCP source snapshot and its complete upstream license in Git.
- Kept national specifications and other uncleared material in a Git-ignored
  local cache; documented how another checkout can reproduce it.
- Stopped eSett document collection after reviewing its usage restrictions.
  Kept ENTSO-E downloads and Nordic bundles pending permission/content review.
- Separated historical, natural-gas, draft and future-effective material from
  sources whose applicability still needs review.
- Read selected national guide covers and visually checked the general guide and
  UTILTS revision-4 cover. Recorded validity dates and a filename/footer conflict.
- Added Codex instructions, a reading guide, source-permission notes and a bounded
  download/verification tool with offline tests.
- Preserved the existing MSCONS fixture, package versions and application design.

## What the checks mean

Every recorded successful download passed a SHA-256 check and a basic content
check. MCP copies also matched their pinned upstream Git blob hashes. Direct XSD
files were parsed as XML and checked for the XML Schema root. ZIPs were inspected
for unsafe paths and size limits; they were not extracted or executed.

PDF signatures are not a full PDF integrity or content audit. Office container
checks do not certify spreadsheets or macros as safe. MDX was retained as source,
not executed. We have not semantically reviewed every page or validated all XSD
dependencies. Passing helper tests is not proof of Ediel or MCP conformance.

The script does not silently accept changes at a stable source URL. A changed
checksum requires a reviewed new edition. Downloaded versions and applicable
market versions are separate concepts.

## Next decisions, not actions taken

1. Confirm one Swedish operator use case and its exact message/profile edition.
2. Resolve the UTILTS filename/footer discrepancy with the publisher if needed
   for adoption, and account for the 2026-10-01 effective date.
3. Obtain necessary eSett/ENTSO-E and bundle permissions for the intended uses.
4. Review parser reliability and MCP SDK compatibility against the chosen versions.
5. Create a small, synthetic validator test set with source-linked expected results.

No claim is made that this collection is complete, licensed for model training or
ready to validate production electricity-market traffic.
