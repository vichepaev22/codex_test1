# Orchestrator

## Input

- one open GitHub Issue;
- default-branch commit SHA;
- repository-level `AGENTS.md`.

## Procedure

1. Confirm the Issue has observable acceptance criteria.
2. Create an isolated Issue branch.
3. Run Maker with the smallest relevant context.
4. Record Maker's changed files and validation evidence.
5. Run Checker with a clean context: Issue, diff, and validation contract only.
6. If Checker returns FAIL, keep the Issue open and send findings back to Maker.
7. If Checker returns PASS, open a Draft Pull Request and wait for human review.

## Stop conditions

- PASS and a Draft Pull Request exists; or
- a permission, secret, ambiguous requirement, or repeated validation failure needs a human decision.
