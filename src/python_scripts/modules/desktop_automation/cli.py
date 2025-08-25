"""
CLI: desktop_automation – type text in the active window after a delay.

Usage:
  poetry run type-text --text "Hello World" --delay 2
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import type_text


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("type-text", level="INFO")

    parser = argparse.ArgumentParser(description="Type text in the active window")
    parser.add_argument("--text", required=True)
    parser.add_argument("--delay", type=float, default=2.0)
    parser.add_argument("--interval", type=float, default=0.1)
    args = parser.parse_args(argv)

    type_text(args.text, delay=args.delay, interval=args.interval)
    logger.info("Text typed", extra={"len": len(args.text), "requestId": None})


if __name__ == "__main__":
    main()
