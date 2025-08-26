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

from .service import get_weather_line, get_weather_pretty


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("weather", level="INFO")

    parser = argparse.ArgumentParser(description="Print weather for a city")
    parser.add_argument("--city", required=True, help="City name")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Show a multi-line, human-readable summary",
    )
    parser.add_argument(
        "--units",
        choices=["f", "c"],
        default="f",
        help="Units for pretty output: 'f' (Fahrenheit/mph) or 'c' (Celsius/km/h)",
    )
    args = parser.parse_args(argv)

    output = (
        get_weather_pretty(args.city, units=args.units)
        if args.pretty
        else get_weather_line(args.city)
    )
    print(output)
    logger.info(
        "Weather fetched",
        extra={
            "city": args.city,
            "pretty": args.pretty,
            "units": args.units if args.pretty else None,
            "requestId": None,
        },
    )


if __name__ == "__main__":
    main()
