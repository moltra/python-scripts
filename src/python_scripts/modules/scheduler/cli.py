"""
CLI: scheduler – demo daily job that prints to stdout.

Usage:
  poetry run scheduler-demo --at 10:00
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import run_daily


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("scheduler-demo", level="INFO")

    parser = argparse.ArgumentParser(description="Run a demo job daily at a time")
    parser.add_argument("--at", default="10:00")
    args = parser.parse_args(argv)

    def job() -> None:
        print("Daily task running...")

    logger.info("Starting scheduler", extra={"at": args.at, "requestId": None})
    run_daily(job, at=args.at)


if __name__ == "__main__":
    main()
