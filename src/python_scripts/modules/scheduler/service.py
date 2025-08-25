"""
Service: scheduler – simple scheduled job runner using schedule.

Install when needed:
  poetry add schedule
"""
from __future__ import annotations

import time
from typing import Callable


def run_daily(job: Callable[[], None], at: str = "10:00") -> None:
    """
    Run a callable every day at the given time (HH:MM) until interrupted.
    """
    try:
        import schedule  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("scheduler requires 'schedule' (poetry add schedule)") from exc

    schedule.every().day.at(at).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
