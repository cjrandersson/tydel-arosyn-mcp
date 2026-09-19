# Source permissions

Reviewed on 2026-09-19. This is a conservative project handling policy, not a legal
opinion or a grant of rights from any publisher.

## Decisions

| Source | Project handling | Reason |
| --- | --- | --- |
| MCP upstream specification/schema files | Original files in Git, with upstream license | Explicit licensing; pinned upstream commit and blob hashes |
| Swedish Ediel, Nordic guides and market handbook | Local reference cache only | Public download links; no blanket public-redistribution or model-use license established |
| eSett | Links only; automated document collection stopped | Published terms restrict automated collection, storage/reproduction and commercial use without permission |
| ENTSO-E | Links only | Published general terms limit downloads to personal non-commercial use, with further reuse requiring permission |
| Nordic ZIP schema bundles | Links only pending content/rights review | Bundles may include separately owned schemas; do not use a mirror to bypass publisher restrictions |
| ISO/IEC standards and other gated sources | Catalogue links only | Obtain the required edition with appropriate access and license |

Sources: [eSett terms](https://www.esett.com/terms-conditions/),
[ENTSO-E disclaimer, sections 2–3](https://www.entsoe.eu/about/legal-and-regulatory/disclaimer/),
[MCP upstream license](../../reference/vendor/mcp/LICENSE).

Different terms may apply to a specific document. We have not established that
every public Ediel reference is suitable for commercial redistribution. Local
reference storage does not settle that question. Stop and review any conflicting
notice found inside a document before further use.

## Reading, retrieval and training are different

This task creates a reference collection, not a training dataset. No embeddings,
fine-tuning, automated knowledge ingestion or uploads of these documents to an
external model were performed by the collection script.

Before any of those uses, record the intended purpose, publisher permission or
other documented basis, allowed recipients/providers and retention conditions.
Do not infer permission for model training from public availability, a successful
download or the presence of a file in this repository.

For parser tests, prefer new synthetic cases with explicit expected results.
Keep original publisher examples separate; they need their own applicability and
reuse review. Never use real customers' messages or credentials as training data.

## Unblocking a source

1. Identify the exact publisher, document/edition and intended use.
2. Obtain the required permission, or document an applicable file-specific license.
3. Record evidence and approved storage/model uses in a reviewed change.
4. Only then update the catalogue and downloader policy.

User approval alone cannot replace permission required from a publisher. Do not
work around restrictions via alternate hosts or by disguising automated requests.
