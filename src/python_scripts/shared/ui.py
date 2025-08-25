"""
UI helpers (CLI) for python_scripts.

Provides a spinner context using Halo that writes to stderr, keeping stdout
clean for JSON logs.

@see src/python_scripts/shared/logging.py
"""
from __future__ import annotations

import sys
from contextlib import contextmanager
from typing import Generator

from halo import Halo


@contextmanager
def spinner(text: str = "Working...", spinner_style: str = "dots") -> Generator[Halo, None, None]:
    """
    Context manager that yields a Halo spinner configured to write to stderr.

    @param text           Initial spinner text
    @param spinner_style  Halo spinner style name (e.g., "dots")
    @yields               The active Halo spinner instance
    @example
      with spinner("Processing") as sp:
          sp.text = "Step 1"
    """
    sp = Halo(text=text, spinner=spinner_style, stream=sys.stderr)
    sp.start()
    try:
        yield sp
        sp.succeed("Done")
    except Exception:
        sp.fail("Failed")
        raise
