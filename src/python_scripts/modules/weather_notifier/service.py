"""
Service: weather_notifier – fetch concise weather via wttr.in
"""
from __future__ import annotations

import requests


def get_weather_line(city: str) -> str:
    """
    Return a single-line summary for the given city using wttr.in.
    """
    url = f"http://wttr.in/{city}?format=3"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text.strip()
