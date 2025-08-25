"""
CLI: weather_notifier – print one-line weather for a city.

Usage:
  poetry run weather --city Lahore
"""
from __future__ import annotations

import argparse
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import get_weather_line


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("weather", level="INFO")

    parser = argparse.ArgumentParser(description="Print concise weather for a city")
    parser.add_argument("--city", required=True, help="City name")
    args = parser.parse_args(argv)

    line = get_weather_line(args.city)
    print(line)
    logger.info("Weather fetched", extra={"city": args.city, "requestId": None})


if __name__ == "__main__":
    main()
