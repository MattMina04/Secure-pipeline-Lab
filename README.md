# Secure pipeline lab

A small lab for practising security checks in a CI pipeline.

On every push, GitHub Actions:
1. Runs the unit tests (pytest)
2. Scans the code with Semgrep (Python ruleset)
3. Scans dependencies with pip-audit

If any step fails, the build stops.

## What I tested
- Added `subprocess.run(cmd, shell=True)`. Semgrep flagged it as a command injection risk and failed the build. I fixed it with `shell=False`.
- Pinned `requests==2.19.1`. pip-audit found 37 known vulnerabilities across requests and its dependencies (idna and urllib3) and failed the build.
