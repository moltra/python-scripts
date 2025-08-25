"""
CLI: web_flask – run the Flask dev server.

Usage:
  poetry run web-flask --host 127.0.0.1 --port 5000
"""
from __future__ import annotations

import argparse
from typing import Optional

from python_scripts.modules.web_flask.service import create_app


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run Flask app")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args(argv)

    app = create_app()
    app.run(host=args.host, port=args.port, debug=True)


if __name__ == "__main__":
    main()
