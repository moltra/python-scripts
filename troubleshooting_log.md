# Troubleshooting Log

Purpose: track errors, exceptions, failed runs/tests, and their resolutions. Keep entries concise and actionable.

## Guidelines
- One entry per issue. Update the same entry as you learn more.
- Capture commands, environment, stack traces, and Loguru fields (`requestId`, `actor`).
- Record root cause and the concrete fix. Link PR/commit if applicable.
- Add follow-ups (tests, docs, monitoring) to avoid regressions.

## Template
```md
### [YYYY-MM-DD HH:MM] Short title
- Context: what you were doing
- Command: <exact command>
- Env: repo @ commit, Python, OS
- Expected: <what should happen>
- Actual: <what happened>
- Stack trace:
  ```
  <paste or link>
  ```
- Logs (redacted):
  ```json
  {"level":"ERROR","actor":"<module>","requestId":"...","stack":"..."}
  ```
- Root cause: <why it happened>
- Fix: <code/config change>
- Follow-ups: tests/docs/alerts
- Links: PR/commit/issue
```

## Entries
### [2025-08-25 07:50] Ruff E501 and import formatting in CLIs/services
- Context: Ran linter autofix across repo after scaffolding modules
- Command: `poetry run ruff check --fix`
- Env: repo @ WIP, Python 3.12, OS: Windows
- Expected: All issues auto-fixed
- Actual: 19 errors found (16 fixed, 3 remaining). Representative errors:
  - E501 Line too long in `desktop_automation/service.py` and `pdf_tools/cli.py`
  - Import formatting inside try-block in `web_fastapi/cli.py`
- Stack trace: N/A (linter output only)
- Logs: N/A
- Root cause: Long strings and dict literals >100 cols; import grouping violations in try
- Fix: Wrapped long strings/signatures; grouped imports (third-party before first-party) in try
  - Files changed:
    - `src/python_scripts/modules/desktop_automation/service.py`
    - `src/python_scripts/modules/pdf_tools/cli.py`
    - `src/python_scripts/modules/email_sender/service.py`
    - `src/python_scripts/modules/web_fastapi/cli.py`
- Follow-ups:
  - Add `ruff --fix` to pre-commit
  - Keep lines <=100 chars; group imports consistently (stdlib/third-party/first-party)
  - Expand tests to catch CLI regressions
- Links: README Troubleshooting section updated
