"""
CLI: quotes_scraper – scrape quotes from a page and print as JSON lines.

Usage:
  poetry run quotes-scraper --url https://quotes.toscrape.com/ --limit 5

Outputs structured JSON via Loguru; rows are also printed to stdout as plain text for convenience.
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru
from python_scripts.shared.ui import spinner

from .service import scrape_quotes


def main(argv: Optional[list[str]] = None) -> None:
    """
    Parse flags, setup logging, and run the scraper.
    """
    setup_loguru("quotes-scraper", level="INFO")

    parser = argparse.ArgumentParser(description="Scrape quotes from a web page.")
    parser.add_argument("--url", required=True, help="Page URL to scrape")
    parser.add_argument("--limit", type=int, default=None, help="Max quotes to return")
    args = parser.parse_args(argv)

    with spinner("Fetching quotes..."):
        quotes = scrape_quotes(args.url, limit=args.limit)

    for q in quotes:
        print(f"{q.text} - {q.author}")
    logger.info("Scraped quotes", extra={"count": len(quotes), "requestId": None})


if __name__ == "__main__":
    main()
