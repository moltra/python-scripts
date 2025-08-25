"""
CLI: pdf_tools – merge PDFs.

Usage:
  poetry run pdf-merge --out merged.pdf one.pdf two.pdf three.pdf
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from loguru import logger

from python_scripts.shared.logging import setup_loguru

from .service import merge_pdfs


def main(argv: Optional[list[str]] = None) -> None:
    setup_loguru("pdf-tools", level="INFO")

    parser = argparse.ArgumentParser(description="Merge PDFs into a single file")
    parser.add_argument("--out", required=True, help="Output PDF path")
    parser.add_argument("inputs", nargs="+", help="Input PDF files in order")
    args = parser.parse_args(argv)

    out = merge_pdfs([Path(p) for p in args.inputs], Path(args.out))
    logger.info(
        "PDF merged",
        extra={
            "path": str(out),
            "count": len(args.inputs),
            "requestId": None,
        },
    )


if __name__ == "__main__":
    main()
