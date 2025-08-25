"""
CLI entry point for the org_file module.

Loads settings from environment/.env (prefix ORG_FILE_), applies CLI overrides,
configures logging and shows a spinner while organizing files.

@see src/python_scripts/modules/org_file/service.py
@see src/python_scripts/shared/logging.py
@see src/python_scripts/shared/ui.py
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from python_scripts.shared.logging import setup_loguru
from python_scripts.shared.ui import spinner

from .service import organize_downloads


class AppSettings(BaseSettings):
    """
    App configuration loaded from environment variables (and .env).

    @env ORG_FILE_DOWNLOADS_DIR  Path to downloads directory
    @env ORG_FILE_DRY_RUN        Enable dry-run by default (true/false)
    """

    downloads_dir: Optional[Path] = None
    dry_run: bool = False

    model_config = SettingsConfigDict(
        env_prefix="ORG_FILE_",
        env_file=".env",
        env_file_encoding="utf-8",
    )


def main(argv: Optional[list[str]] = None) -> None:
    """
    Parse CLI flags, resolve settings, setup logging, and run the service.

    @param argv  Optional argument list (mainly for testing)
    @returns     None
    """
    # Logging
    setup_loguru(app_name="org-file", level="INFO")

    # CLI args override env/.env defaults
    parser = argparse.ArgumentParser(description="Organize files in Downloads by extension.")
    parser.add_argument(
        "--folder",
        "--downloads-dir",
        dest="folder",
        type=str,
        help="Folder to organize (default: ORG_FILE_DOWNLOADS_DIR or user's Downloads)",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Preview actions without moving files",
    )
    args = parser.parse_args(argv)

    settings = AppSettings()
    folder_arg: Optional[str] = args.folder
    resolved_folder: Optional[Path | str] = (
        folder_arg if folder_arg is not None else settings.downloads_dir
    )
    resolved_dry_run: bool = True if args.dry_run else settings.dry_run

    with spinner("Organizing files...") as sp:
        def on_progress(p: Path) -> None:
            sp.text = f"Processing: {p.name}"

        try:
            organize_downloads(
                folder=resolved_folder,
                dry_run=resolved_dry_run,
                progress=on_progress,
            )
            sp.succeed("Organization complete")
        except Exception as exc:
            sp.fail("Organization failed")
            logger.error(
                "Failure during organization",
                extra={
                    "requestId": None,
                    "stack": None,
                    "actor": "org-file",
                    "reason": str(exc),
                },
            )
            raise


if __name__ == "__main__":
    main()
