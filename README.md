# python-scripts

A collection of productivity and learning Python scripts for Windows.

## Environment
- Managed with Poetry (in-project venv: `.venv/`).
- Python: 3.12 (per `pyproject.toml`).

## Quick start
```powershell
# from repo root
poetry install

# run any CLI (examples)
poetry run org-file --dry-run
poetry run quotes-scraper --url https://quotes.toscrape.com/ --limit 5
poetry run excel-report --out sales.xlsx
poetry run pdf-merge --out merged.pdf one.pdf two.pdf
poetry run weather --city Lahore
poetry run email-send --to you@mail.com --subject "Hi" --body "Done"
poetry run type-text --text "Hello" --delay 2
poetry run data-clean --in sales.csv --out cleaned.csv
poetry run chatbot --prompt "Tell me a fun fact"
poetry run bitcoin-price
poetry run scheduler-demo --at 10:00
poetry run web-flask --port 5000
poetry run web-fastapi --port 8000
```

## Available CLIs
- org-file – organize Downloads by extension
- quotes-scraper – scrape quotes as text output
- excel-report – write simple .xlsx from rows
- pdf-merge – merge PDFs
- weather – one-line weather via wttr.in
- email-send – send text email via SMTP
- type-text – type into active window (PyAutoGUI)
- data-clean – CSV cleaning + Revenue column (pandas)
- chatbot – one-shot OpenAI Chat Completion
- bitcoin-price – current BTC/USD rate (Coindesk)
- scheduler-demo – demo daily scheduler
- web-flask – run Flask dev server
- web-fastapi – run FastAPI with uvicorn

## Notes
- This repo is script-first. If you only want dependency management and not packaging, you can run:
  - `poetry install --no-root`
  - Or set in `pyproject.toml`:
    
    ```toml
    [tool.poetry]
    package-mode = false
    ```

## Optional dependencies
Install lazily as needed:
- quotes-scraper: `requests`, `beautifulsoup4`
- excel-report: `openpyxl`
- pdf-merge: `PyPDF2`
- weather: `requests`
- email-send: none (stdlib), but uses env config
- type-text: `pyautogui`
- data-clean: `pandas`
- chatbot: `openai`
- scheduler-demo: `schedule`
- web-flask: `flask`
- web-fastapi: `fastapi`, `uvicorn`

## Configuration
- `.env` at repo root is loaded via `pydantic-settings`.
- ORG_FILE_* variables:
  - `ORG_FILE_DOWNLOADS_DIR`, `ORG_FILE_DRY_RUN`
- EMAIL_* variables for SMTP (see `src/python_scripts/modules/email_sender/service.py`):
  - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`, `EMAIL_FROM`, `EMAIL_USE_TLS`

## Logging
- Structured JSON logs via Loguru, configured in `src/python_scripts/shared/logging.py`.
- Spinner output goes to stderr (`src/python_scripts/shared/ui.py`).

## Troubleshooting
- Log all failures, errors, and odd behaviors in `troubleshooting_log.md` at repo root.
- Use the template in that file to capture context, stack traces, logs, root cause, and fix.

## Development
- Pre-commit hooks run Ruff auto-fix and check via local hooks defined in `.pre-commit-config.yaml`.
- Setup (requires dev dependency install):

```powershell
poetry add --group dev pre-commit
poetry run pre-commit install
poetry run pre-commit run -a
```

- Ruff settings live in `pyproject.toml` under `[tool.ruff]`. Keep line-length and excludes in sync
  with the pre-commit config.
- To temporarily skip hooks (not recommended): `git commit -n`
