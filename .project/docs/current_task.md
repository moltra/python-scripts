# Current Task – 2025-08-25

Checklist of immediate actions. Check items as you complete them.

- [ ] Lint/format pass
  - [ ] poetry run ruff check --fix
  - [ ] poetry run ruff check
- [ ] Commit staged changes
  - [ ] git add -A
  - [ ] git commit -m "chore: fix lints; docs: README & task file; add module __init__"
- [ ] Configure environment
  - [ ] Create/update .env at repo root
  - [ ] ORG_FILE_ vars: ORG_FILE_DOWNLOADS_DIR, ORG_FILE_DRY_RUN
  - [ ] EMAIL_ vars: EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_FROM, EMAIL_USE_TLS
- [ ] Smoke-test core CLIs
  - [ ] poetry run org-file --help
  - [ ] poetry run email-send --help
  - [ ] poetry run pdf-merge --help
  - [ ] poetry run web-fastapi --help
- [ ] Optional dependency installs (as needed for specific CLIs)
  - [ ] quotes-scraper: requests, beautifulsoup4
  - [ ] excel-report: openpyxl
  - [ ] pdf-merge: PyPDF2
  - [ ] type-text: pyautogui
  - [ ] data-clean: pandas
  - [ ] chatbot: openai
  - [ ] scheduler-demo: schedule
  - [ ] web-flask: flask
  - [ ] web-fastapi: fastapi, uvicorn
- [ ] Add troubleshooting log
  - [ ] Create troubleshooting_log.md to track errors from running CLIs/tests
- [ ] Testing scaffold (next)
  - [ ] Create tests/ mirroring src/ structure
  - [ ] Add basic unit tests for modules (≥80% coverage target)

Refs:
- README: `README.md`
- Org service: `src/python_scripts/modules/org_file/service.py`
- Logging setup: `src/python_scripts/shared/logging.py`
