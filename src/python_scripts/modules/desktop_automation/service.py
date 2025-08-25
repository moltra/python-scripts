"""
Service: desktop_automation – small helpers around pyautogui.
"""
from __future__ import annotations

import time


def type_text(text: str, delay: float = 2.0, interval: float = 0.1) -> None:
    """
    After a short delay (to focus your target window), type text and press Enter.
    """
    try:
        import pyautogui  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "desktop_automation requires 'pyautogui' "
            "(poetry add pyautogui)"
        ) from exc

    time.sleep(delay)
    pyautogui.typewrite(text, interval=interval)
    pyautogui.press("enter")
