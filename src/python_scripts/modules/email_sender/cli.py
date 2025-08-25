"""
CLI: email_sender – send a text email using SMTP settings from env.

Usage:
  poetry run email-send --to boss@mail.com --subject "Daily Report" --body "Done"
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import send_text_email


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("email-send", level="INFO")

    parser = argparse.ArgumentParser(description="Send a text email using SMTP")
    parser.add_argument("--to", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True)
    args = parser.parse_args(argv)

    send_text_email(args.to, args.subject, args.body)
    logger.info("Email sent", extra={"to": args.to, "requestId": None})


if __name__ == "__main__":
    main()
