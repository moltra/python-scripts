"""
Service: web_fastapi – minimal FastAPI app factory.

Install when needed:
  poetry add fastapi uvicorn
"""
from __future__ import annotations

from typing import Any


def create_app() -> Any:
    try:
        from fastapi import FastAPI  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("web_fastapi requires 'fastapi' (poetry add fastapi uvicorn)") from exc

    app = FastAPI()

    @app.get("/")
    def home() -> dict[str, Any]:
        return {"message": "Hello from FastAPI"}

    return app
