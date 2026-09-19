# Reading guide

Research snapshot: **2026-09-19**. Start here before picking a parser or writing
validation rules. This collection does not choose Tydel's first message profile.

## Start with these

| Order | Read | Why |
| --- | --- | --- |
| 1 | [General Swedish Ediel rules](https://www.ediel.se/Portal/Document/3314), source `se-ediel-3314` | Message envelopes, acknowledgements, addressing and transport boundaries |
| 2 | [Swedish market handbook](https://www.elmarknadshandboken.se/handbok.html) | Processes, actors and responsibilities |
| 3 | [National implementation guides](https://www.ediel.se/Info/EdielAnvisningar) | Select the exact process, message and validity period |
| 4 | [Nordic EDIFACT guides](https://ediel.org/guides/) | Base message structure; not a replacement for Swedish rules |
| 5 | [Nordic XML rules](https://ediel.org/common-ediel-documents/) and [NBS sources](https://ediel.org/nordic-balance-settlement-nbs/) | XML-based settlement, code lists and schema dependencies |
| 6 | [MCP reading order](../../reference/mcp/README.md) | How our tools and references can be exposed to an assistant |

Use [`reference/catalogs/`](../../reference/catalogs/) to find source IDs and
[`download-lock.json`](../../reference/download-lock.json) to locate downloaded
files. A source link is not proof that we have downloaded or may redistribute it.

## Keep the layers separate

| Layer | Examples | What it establishes |
| --- | --- | --- |
| Syntax | EDIFACT separators, XML, JSON | Whether content can be parsed |
| Message/profile | UTILTS, PRODAT, APERAK, a particular XML namespace/XSD | The structure for one named release |
| Business rules | Swedish Ediel instructions, national settlement rules | What values and relationships are acceptable for that process |
| Transport | SMTP, ECP or a customer's export adapter | How messages arrive, not whether their business content is valid |
| AI interface | MCP tools/resources | Controlled access to validation and evidence, not market-message validity |

For XML, syntactic well-formedness and XSD validation are separate checks. Neither
alone proves that a message meets business rules or will be accepted by a partner.

## Findings that affect the first version

### Start the meter-data research with UTILTS

The [Swedish Ediel index](https://www.ediel.se/Info/EdielAnvisningar) places
electricity meter-value guidance under **UTILTS–APERAK**. MSCONS also appears in
natural-gas and historical material. The existing `mock_mscons.edi` remains useful
as an unverified parser experiment, but is not evidence for choosing MSCONS as the
first current Swedish electricity profile.

**Recommendation, not an implemented decision:** choose a narrow UTILTS test case
with its matching acknowledgement/profile after a domain review. PRODAT is a
separate candidate for master-data and supplier-change workflows.

### Publication date is not the effective date

The covers of `se-ediel-3364` and `se-ediel-3365` identify UTILTS **D.02B**, profile
**E5SE5A**, guide revision **4**, effective **2026-10-01**. At this review date that
is a future effective date. The previous Swedish/English guides, `se-ediel-3333`
and `se-ediel-3334`, show revision **3**, effective **2025-06-01**.

Evidence: [Swedish revision 4, cover p. 1](https://www.ediel.se/Portal/Document/3364),
[English revision 4, cover p. 1](https://www.ediel.se/Portal/Document/3365),
[Swedish revision 3, cover p. 1](https://www.ediel.se/Portal/Document/3333).
The exact downloaded editions are pinned by SHA-256 in the lock file.

There is also a source inconsistency: the portal filename for the Swedish
revision-4 PDF ends in `25-A-4`, while its page footer says `25-A-5`. The cover
states revision 4. We preserve these observations; we do not guess which label
the publisher intended. Confirm with the publisher before production adoption.

The [general guide](https://www.ediel.se/Portal/Document/3314) is **24.A revision 6**,
dated **2026-02-20**, with two cover validity dates. The
[PRODAT/APERAK guide](https://www.ediel.se/Portal/Document/3338) combines versions
**26.A/16.B**, revision **3**, with different cover validity dates for its profiles.
Never derive one global "current Ediel version" from either filename.

### Acknowledgements need their own context

Do not treat standalone APERAK, UTILTS-associated APERAK and PRODAT-associated
APERAK as interchangeable. Keep the original message reference, profile and error
location when explaining a rejection. Distinguish transport failure, parsing
failure, structural validation and a business-level rejection.

### NBS/XML is a separate research track

The Nordic catalogue includes business requirements, code lists, XSDs and bundle
links. Some documents are drafts or describe future changes. Not every schema
listed by NMEG is accepted by eSett for every process and country. Bundle rights,
schema imports, namespaces and partner-supported editions remain to be checked.

### MCP is not the inference engine

An MCP server exposes capabilities to an MCP client in a host application. The
host/model can use those results to explain errors. Downloading a specification
does not create an agent, parser, validator, inference service or training set.

## From a source to a testable rule

For each proposed rule, record:

1. Country, process, message/profile and applicable reporting dates.
2. Source ID, verified edition, page/section and file SHA-256.
3. The exact field/relationship checked and its exceptions.
4. A synthetic passing case and a synthetic failing case with expected results.
5. Open questions and a review outcome before marking the rule implemented.

This is a proposed workflow. No production rules or new validated fixtures were
created during reference collection.

## Gaps to resolve

- eSett and ENTSO-E permissions for the intended project and model uses.
- Contents, licensing and dependency closure of Nordic schema bundles.
- Full ISO/IEC standards where a licensed edition is needed.
- The correct effective profile and first real operator use case.
- A complete review of all collected documents; only selected covers and source
  classifications have been inspected in depth.
- Ei's linked PDF was not captured; the regulatory catalogue retains the official
  publication page. Check amendments and reporting-period applicability before
  turning regulation into a rule.
- MCP SDK/protocol compatibility and the proposed EDIFACT parser. Neither was
  installed, changed or endorsed by collecting these references.
