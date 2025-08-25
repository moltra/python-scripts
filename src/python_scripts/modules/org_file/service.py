"""
Service layer for organizing files by extension.

Pure functions; no CLI/IO side-effects except logging via Loguru.

@see src/python_scripts/modules/org_file/cli.py
@see src/python_scripts/shared/logging.py
@see src/python_scripts/shared/ui.py
"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Callable, Optional

from loguru import logger


def _default_downloads_dir() -> Path:
    """
    Summary – Determine the current user's Downloads directory in a cross-platform way.

    Returns the best-effort path to the Downloads folder using the current user's home
    directory. This avoids hard-coding a Windows path string (which can break due to
    backslash escape sequences like "\\U").

    @returns        Path to the user's Downloads directory (not guaranteed to exist)
    @example
      downloads = _default_downloads_dir()
    """
    home = Path.home()
    return home / "Downloads"


def _move_to_extension_dir(file_path: Path, base_dir: Path, dry_run: bool) -> Path:
    """
    Summary – Compute destination and move a single file into a subfolder named by its extension.

    For example, "report.pdf" goes into "<Downloads>/pdf/". Files without an extension
    go into "<Downloads>/no_ext/". If a destination file already exists, a numeric suffix
    is appended (e.g., "report (1).pdf") to avoid overwriting.

    @param file_path  Absolute path to the source file
    @param base_dir   Base directory that contains the subfolders per extension
    @param dry_run    When True, only log the intended move without changing files
    @returns          Destination path (candidate)
    @throws           ValueError if file_path is not a file
    """
    if not file_path.is_file():
        raise ValueError(f"Expected a file path, got: {file_path}")

    # Normalize extension: ".PDF" -> "pdf". If there's no suffix, use "no_ext".
    ext = file_path.suffix.lower().lstrip(".") or "no_ext"
    dest_dir = base_dir / ext
    dest_dir.mkdir(exist_ok=True)

    # Compute destination path; if it exists, add a numeric suffix.
    candidate = dest_dir / file_path.name
    if candidate.exists():
        stem, suffix = file_path.stem, file_path.suffix
        i = 1
        while candidate.exists():
            candidate = dest_dir / f"{stem} ({i}){suffix}"
            i += 1

    if dry_run:
        logger.info(
            "Would move file",
            extra={
                "requestId": None,
                "src": str(file_path),
                "dst": str(candidate),
            },
        )
    else:
        shutil.move(str(file_path), str(candidate))
        logger.info(
            "Moved file",
            extra={
                "requestId": None,
                "src": str(file_path),
                "dst": str(candidate),
            },
        )

    return candidate


def organize_downloads(
    folder: Optional[str | Path] = None,
    dry_run: bool = False,
    progress: Optional[Callable[[Path], None]] = None,
) -> None:
    """
    Summary – Move each file in the downloads folder into a subfolder named by its file extension.

    Why – Keeps your Downloads tidy and makes it easier to scan by type (pdf, jpg, zip, etc.).
    Uses Loguru for structured logging and supports a dry-run mode for safety.

    @param folder     Directory to organize. If None, uses the user's Downloads folder.
    @param dry_run    When True, log intended actions but do not move files.
    @param progress   Optional callback invoked per file with the Path being processed.
    @returns          None
    @throws           FileNotFoundError if the folder does not exist
    @example
      organize_downloads()
    """
    base_dir = Path(folder) if folder is not None else _default_downloads_dir()

    if not base_dir.exists() or not base_dir.is_dir():
        raise FileNotFoundError(f"Downloads folder not found: {base_dir}")

    # Iterate only top-level entries; move regular files into their extension-named folders.
    for entry in base_dir.iterdir():
        if entry.is_file():
            if progress:
                progress(entry)
            _move_to_extension_dir(entry, base_dir, dry_run=dry_run)
