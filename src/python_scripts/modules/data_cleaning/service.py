"""
Service: data_cleaning – simple CSV cleaning/transformation with pandas.
"""
from __future__ import annotations

from pathlib import Path


def clean_sales_csv(csv_in: Path, csv_out: Path) -> Path:
    """
    Read a sales CSV with columns [Name, Units, Price] and write [Name, Units, Price, Revenue].
    Drops rows with missing values.
    """
    try:
        import pandas as pd  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("data_cleaning requires 'pandas' (poetry add pandas)") from exc

    df = pd.read_csv(csv_in)
    df["Revenue"] = df["Units"] * df["Price"]
    df.dropna(inplace=True)
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_out, index=False)
    return csv_out
