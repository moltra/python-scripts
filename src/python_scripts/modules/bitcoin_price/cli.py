"""
CLI: bitcoin_price – print current BTC/USD rate.

Usage:
  poetry run bitcoin-price
"""
from __future__ import annotations

from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import get_btc_usd_rate


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("bitcoin-price", level="INFO")
    rate = get_btc_usd_rate()
    print("Bitcoin:", rate)
    logger.info("BTC rate fetched", extra={"rate": rate, "requestId": None})


if __name__ == "__main__":
    main()
