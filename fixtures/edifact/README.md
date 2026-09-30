# EDIFACT fixtures

Synthetic or properly anonymized messages used for parsing and validation tests belong here.

Rules:

- Never commit real customer or market-party data.
- State whether a fixture is valid or intentionally broken.
- Describe the expected result in a nearby test or matching metadata file.
- Do not treat a generated fixture as an authoritative Ediel example.
- New cases must state their profile, expected result and source edition before they become validator tests.

## Fixture sets

- `mock_mscons.edi` is an early synthetic research fixture and still needs domain validation.
- `utilts/candidate/` contains user-supplied realistic UTILTS candidate data. These raw files are preserved unchanged and are explicitly `UNVERIFIED`; see its README and manifest before using them in tests.

Downloaded publisher examples belong in the reference cache, not automatically in this fixture set. Start profile selection with the [research reading guide](../../docs/research/reading-guide.md).
