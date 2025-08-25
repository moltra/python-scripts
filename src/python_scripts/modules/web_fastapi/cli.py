"""
CLI: web_fastapi – run the FastAPI dev server with uvicorn.

Usage:
  poetry run web-fastapi --host 127.0.0.1 --port 8000
"""
from __future__ import annotations

import argparse
from typing import Optional


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run FastAPI app with uvicorn")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)

    try:
        import uvicorn  # type: ignore

        from python_scripts.modules.web_fastapi.service import create_app
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "web_fastapi requires 'fastapi' and 'uvicorn' "
            "(poetry add fastapi uvicorn)"
        ) from exc

    uvicorn.run(create_app(), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
