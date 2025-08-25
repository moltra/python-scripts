"""
CLI: chatbot – send one prompt and print the reply.

Usage:
  poetry run chatbot --prompt "Tell me a fun fact about space."
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import chat_once


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("chatbot", level="INFO")

    parser = argparse.ArgumentParser(description="Chat once and print the reply")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--model", default="gpt-4o-mini")
    args = parser.parse_args(argv)

    reply = chat_once(args.prompt, model=args.model)
    print(reply)
    logger.info("Chat completed", extra={"model": args.model, "requestId": None})


if __name__ == "__main__":
    main()
