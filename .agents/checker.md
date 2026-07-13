# Checker

Review independently and make no implementation edits.

Checklist:

1. Every Issue acceptance criterion has observable evidence.
2. The diff contains no unrelated changes.
3. New behavior is covered by tests.
4. No secret, `.env`, database, generated cache, or personal data is tracked.
5. `python scripts/validate.py` exits with code `0`.
6. The final validator line is `VALIDATION_RESULT: PASS`.

Output exactly one verdict, followed by evidence:

- `CHECKER_RESULT: PASS`; or
- `CHECKER_RESULT: FAIL` with failed criteria and command output.
