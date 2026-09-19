# EDIFACT fixtures

Synthetic or properly anonymized messages used for parsing and validation tests belong here.

Rules:

- Never commit real customer or market-party data.
- State whether a fixture is valid or intentionally broken.
- Describe the expected result in a nearby test or matching metadata file.
- Do not treat a generated fixture as an authoritative Ediel example.

The current `mock_mscons.edi` file is an early research fixture and still needs domain validation.

It is not an authoritative example of today's Swedish electricity meter-value
exchange. Start profile selection with the [research reading guide](../../docs/research/reading-guide.md).
Downloaded publisher examples belong in the reference cache, not automatically
in this fixture set. New cases must state their profile, expected result and
source edition before they become validator tests.
