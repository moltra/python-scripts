"""
CLI: data_cleaning – clean a sales CSV and compute Revenue column.

Usage:
  poetry run data-clean --in sales.csv --out cleaned_sales.csv
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import clean_sales_csv


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("data-clean", level="INFO")

    parser = argparse.ArgumentParser(description="Clean a sales CSV and compute Revenue")
    parser.add_argument("--in", dest="inp", required=True)
    parser.add_argument("--out", dest="out", required=True)
    args = parser.parse_args(argv)

    out = clean_sales_csv(Path(args.inp), Path(args.out))
    logger.info("CSV cleaned", extra={"path": str(out), "requestId": None})


if __name__ == "__main__":
    main()
