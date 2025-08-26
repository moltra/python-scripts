"""
Service: weather_notifier – fetch concise weather via wttr.in
"""
from __future__ import annotations

from typing import Any, Dict

import requests

# Constants
BASE_URL: str = "http://wttr.in"
DEFAULT_TIMEOUT_SECONDS: int = 10


def get_weather_line(city: str) -> str:
    """
    Return a single-line summary for the given city using wttr.in.
    """
    url = f"{BASE_URL}/{city}?format=3"
    resp = requests.get(url, timeout=DEFAULT_TIMEOUT_SECONDS)
    resp.raise_for_status()
    return resp.text.strip()


def get_weather_pretty(city: str, units: str = "f") -> str:
    """
    Return a more human-readable, multi-line summary using wttr.in JSON (j1).

    Includes city, conditions, temperature, feels-like, wind, and humidity.

    @param city     City name to query
    @param units    "f" for Fahrenheit/mph, "c" for Celsius/km/h (default: "f")
    @returns        Multi-line string formatted for humans
    @throws         requests.HTTPError on non-200 responses
    @see src/python_scripts/modules/weather_notifier/cli.py
    """
    url = f"{BASE_URL}/{city}?format=j1"
    resp = requests.get(url, timeout=DEFAULT_TIMEOUT_SECONDS)
    resp.raise_for_status()

    data: Dict[str, Any] = resp.json()
    current = (data.get("current_condition") or [{}])[0]
    nearest = (data.get("nearest_area") or [{}])[0]

    # Extract fields defensively
    name = (
        ((nearest.get("areaName") or [{}])[0].get("value"))
        or city
    )
    region = (
        ((nearest.get("region") or [{}])[0].get("value"))
        or ""
    )
    country = (
        ((nearest.get("country") or [{}])[0].get("value"))
        or ""
    )
    desc = (
        ((current.get("weatherDesc") or [{}])[0].get("value"))
        or ""
    )
    temp_c = current.get("temp_C")
    feels_c = current.get("FeelsLikeC")
    wind_kmph = current.get("windspeedKmph")
    temp_f = current.get("temp_F")
    feels_f = current.get("FeelsLikeF")
    wind_mph = current.get("windspeedMiles")
    wind_dir = current.get("winddir16Point")
    humidity = current.get("humidity")

    use_f = (units or "f").lower().startswith("f")
    if use_f:
        temp_line = f"Temperature: {temp_f}°F (feels like {feels_f}°F)"
        wind_line = f"Wind: {wind_mph} mph {wind_dir}"
    else:
        temp_line = f"Temperature: {temp_c}°C (feels like {feels_c}°C)"
        wind_line = f"Wind: {wind_kmph} km/h {wind_dir}"

    lines = [
        f"{name}{', ' + region if region else ''}{', ' + country if country else ''}",
        f"Conditions: {desc}",
        temp_line,
        wind_line,
        f"Humidity: {humidity}%",
    ]
    return "\n".join(lines)
