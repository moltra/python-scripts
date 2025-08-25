"""
CLI: excel_report – write a simple Excel file with sample or provided data.

Usage:
  poetry run excel-report --out sales.xlsx
  poetry run excel-report --out path.xlsx --rows "Name,Sales" "Ali,1200" "Sara,900"
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import write_rows_to_xlsx


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("excel-report", level="INFO")

    parser = argparse.ArgumentParser(description="Create a simple Excel workbook")
    parser.add_argument("--out", required=True, help="Output .xlsx path")
    parser.add_argument(
        "--rows",
        nargs="*",
        help="Optional CSV-like rows, e.g., 'Name,Sales' 'Ali,1200'",
    )
    args = parser.parse_args(argv)

    if args.rows:
        rows = [r.split(",") for r in args.rows]
    else:
        rows = [("Name", "Sales"), ("Ali", 1200), ("Sara", 900), ("Hamza", 1400)]

    out = write_rows_to_xlsx(rows, Path(args.out))
    logger.info("Excel written", extra={"path": str(out), "requestId": None})


if __name__ == "__main__":
    main()
