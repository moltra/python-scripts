"""
Logging utilities for the python_scripts project.

Provides a single helper to configure Loguru to emit structured JSON to stdout
and to a rotating file sink under logs/<app_name>.log.

@see src/python_scripts/shared/ui.py
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from loguru import logger


def setup_loguru(app_name: str,
                 level: str = "INFO",
                 logs_dir: Optional[Path] = None) -> Path:
    """
    Configure Loguru with JSON sinks for stdout and file.

    @param app_name   Logical application name used for the file sink name
    @param level      Minimum log level (default: INFO)
    @param logs_dir   Override logs directory (default: <repo>/logs)
    @returns          Path to the log file used
    @example
      logfile = setup_loguru("org-file")
    """
    logger.remove()
    logger.add(sys.stdout, serialize=True, level=level)

    base_dir = logs_dir or Path(__file__).resolve().parents[4] / "logs"
    base_dir.mkdir(exist_ok=True)
    log_file = base_dir / f"{app_name}.log"

    logger.add(
        str(log_file),
        serialize=True,
        level=level,
        rotation="1 week",
        retention="4 weeks",
        enqueue=True,
        backtrace=False,
        diagnose=False,
    )
    return log_file
