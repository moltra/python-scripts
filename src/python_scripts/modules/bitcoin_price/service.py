"""
Service: bitcoin_price – fetch BTC price from Coindesk.
"""
from __future__ import annotations

import requests


def get_btc_usd_rate() -> str:
    """
    Return the BTC USD rate string from the Coindesk API.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    data = requests.get(url, timeout=10).json()
    return data["bpi"]["USD"]["rate"]
