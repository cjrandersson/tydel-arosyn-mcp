# MCP sources

The [catalogue](../catalogs/mcp.json) pins originals to upstream commit
`24efd6e7cbd7a074e6b3b781eb370891df40afad`.

Included:

- specification source documents for `2026-07-28`;
- JSON and TypeScript protocol schemas for `2026-07-28`;
- `2025-11-25` schemas for comparison;
- the complete upstream [LICENSE](../vendor/mcp/LICENSE).

These are research references. **We have not selected or implemented a production
protocol version, changed the SDK dependency or asserted compatibility.** A
protocol date and an npm package version are different things.

## Reading order

1. [Architecture](../vendor/mcp/docs/specification/2026-07-28/architecture/index.mdx): host, client and server responsibilities.
2. [Tools](../vendor/mcp/docs/specification/2026-07-28/server/tools.mdx) and [resources](../vendor/mcp/docs/specification/2026-07-28/server/resources.mdx): how to expose deterministic validation and approved references.
3. [Transports](../vendor/mcp/docs/specification/2026-07-28/basic/transports/index.mdx) and [versioning](../vendor/mcp/docs/specification/2026-07-28/basic/versioning.mdx).
4. [Authorization](../vendor/mcp/docs/specification/2026-07-28/basic/authorization/index.mdx) and [security considerations](../vendor/mcp/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx).
5. The selected [schema](../vendor/mcp/schema/2026-07-28/schema.json), then compatibility tests before implementation.

The MDX files are unmodified upstream source, not a standalone rendered website.
Some links and images rely on the upstream documentation site. Read them as text;
do not execute MDX as part of this library.

The upstream license explains its Apache-2.0/MIT transition and separate licensing
for non-specification documentation. Do not simplify this to "everything is MIT".
Original author notices and files have been retained; no Tydel edits were made to
the upstream content.
