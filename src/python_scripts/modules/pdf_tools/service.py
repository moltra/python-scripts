"""
Service: pdf_tools – merge and split PDFs using PyPDF2.

Install if needed:
  poetry add PyPDF2
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable


def merge_pdfs(paths: Iterable[Path], out_path: Path) -> Path:
    """
    Merge multiple PDFs into one file.

    @param paths     Iterable of PDF paths in merge order
    @param out_path  Output PDF path
    @returns         Saved output path
    """
    try:
        from PyPDF2 import PdfMerger  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("pdf_tools requires 'PyPDF2' (poetry add PyPDF2)") from exc

    merger = PdfMerger()
    for p in paths:
        merger.append(str(p))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    merger.write(str(out_path))
    merger.close()
    return out_path
