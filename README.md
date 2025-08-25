# python-scripts

A collection of productivity and learning Python scripts for Windows.

## Environment
- Managed with Poetry (in-project venv: `.venv/`).
- Python: 3.12 (per `pyproject.toml`).

## Quick start
```powershell
# from repo root
poetry install
poetry run python org-file.py
```

## Notes
- This repo is script-first. If you only want dependency management and not packaging, you can run:
  - `poetry install --no-root`
  - Or set in `pyproject.toml`:
    
    ```toml
    [tool.poetry]
    package-mode = false
    ```

- Recommended deps:
  - Core: `loguru`, `pydantic-settings`, `python-dotenv`, `keyring`
  - Dev: `pytest`, `ruff`
