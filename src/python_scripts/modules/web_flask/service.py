"""
Service: web_flask – minimal Flask app factory.

Install when needed:
  poetry add flask
"""
from __future__ import annotations

from typing import Any


def create_app() -> Any:
    try:
        from flask import Flask  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("web_flask requires 'flask' (poetry add flask)") from exc

    app = Flask(__name__)

    @app.get("/")
    def home() -> dict[str, Any]:
        return {"message": "Hello Flask!"}

    return app
