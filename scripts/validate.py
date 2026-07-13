from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_EXACT = {".env"}
FORBIDDEN_SUFFIXES = {".db", ".sqlite", ".sqlite3"}
SCAN_EXCLUSIONS = {"scripts/validate.py", ".env.example"}
SECRET_PATTERNS = {
    "OpenAI-style API key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def run(command: list[str]) -> bool:
    print(f"CHECK: {' '.join(command)}")
    completed = subprocess.run(command, cwd=ROOT, check=False)
    return completed.returncode == 0


def tracked_files() -> list[str]:
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [item.decode("utf-8") for item in completed.stdout.split(b"\0") if item]


def check_repository_safety(files: list[str]) -> list[str]:
    failures: list[str] = []

    for relative in files:
        path = Path(relative)
        if path.name in FORBIDDEN_EXACT or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            failures.append(f"forbidden tracked runtime file: {relative}")
            continue

        if relative in SCAN_EXCLUSIONS:
            continue

        absolute = ROOT / path
        try:
            text = absolute.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"possible {label} in tracked file: {relative}")

    return failures


def main() -> int:
    failures: list[str] = []

    try:
        failures.extend(check_repository_safety(tracked_files()))
    except (OSError, subprocess.CalledProcessError) as exc:
        failures.append(f"could not inspect tracked files: {exc}")

    if not run([sys.executable, "-m", "compileall", "-q", "app", "tests"]):
        failures.append("Python compilation failed")

    if not run([sys.executable, "-m", "pytest", "-q"]):
        failures.append("pytest failed")

    if failures:
        for failure in failures:
            print(f"VALIDATION_FAILURE: {failure}")
        print("VALIDATION_RESULT: FAIL")
        return 1

    print("VALIDATION_RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
