"""
Service: quotes_scraper – fetch and parse quotes from a website.

This module keeps core logic separated from CLI concerns (argument parsing, spinners),
which improves testability and reuse. BeautifulSoup is imported lazily so the
package remains runnable without optional dependencies until this feature is used.

@see src/python_scripts/modules/quotes_scraper/cli.py
@see src/python_scripts/shared/logging.py
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Quote:
    """
    Represents a single quote scraped from the page.

    Attributes
    -----------
    text: str
        The quote text (without surrounding quotes characters).
    author: str
        The author's name as displayed on the page.
    """

    text: str
    author: str


def scrape_quotes(url: str, limit: int | None = None) -> List[Quote]:
    """
    Scrape quotes from the given URL using BeautifulSoup.

    Why – Avoid manual copy-paste; collect structured data for research.

    Parameters
    ----------
    url: str
        Page URL to scrape (e.g., https://quotes.toscrape.com/)
    limit: int | None
        Optional maximum number of quotes to return.

    Returns
    -------
    list[Quote]
        Parsed quotes in the order found on the page.

    Raises
    ------
    RuntimeError
        If BeautifulSoup (bs4) or requests are not installed.
    """
    try:
        import requests
        from bs4 import BeautifulSoup  # type: ignore
    except Exception as exc:  # pragma: no cover - dependency guard
        raise RuntimeError(
            "quotes_scraper requires 'requests' and 'beautifulsoup4'.\n"
            "Install with: poetry add requests beautifulsoup4"
        ) from exc

    html = requests.get(url, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")

    quotes: list[Quote] = []
    for q in soup.select(".quote"):
        text_el = q.select_one(".text")
        author_el = q.select_one(".author")
        if not text_el or not author_el:
            continue
        text = text_el.get_text(strip=True).strip("\u201c\u201d\"")
        author = author_el.get_text(strip=True)
        quotes.append(Quote(text=text, author=author))
        if limit is not None and len(quotes) >= limit:
            break
    return quotes
