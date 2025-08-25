"""
Service: excel_report – generate or transform Excel workbooks using openpyxl.

Functions import openpyxl lazily to keep base environment light; install when needed:
  poetry add openpyxl
"""
from __future__ import annotations

from pathlib import Path
from typing import Sequence


def write_rows_to_xlsx(rows: Sequence[Sequence[object]], path: Path) -> Path:
    """
    Create a simple workbook with the provided rows and save to path.

    @param rows  2D sequence of cell values (e.g., [("Name","Sales"), ("Ali",1200)])
    @param path  Output .xlsx path
    @returns     The saved path
    """
    try:
        import openpyxl  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("excel_report requires 'openpyxl' (poetry add openpyxl)") from exc

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(list(row))
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(path))
    return path
