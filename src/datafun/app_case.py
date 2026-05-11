"""src/datafun/app_case.py - Project script (example).

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - imports
    - logging
    - pathlib for cross-platform file paths
    - type hints
    - global constants with Final
    - functions
    - repetition patterns:
        - for loop over a numeric range
        - for loop over a list
        - list comprehension
        - while loop with a counter
    - main function
    - conditional execution guard

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.app_case

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P02", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"

FIRST_QUARTER: Final[int] = 1
LAST_QUARTER: Final[int] = 4

PET_LIST: Final[list[str]] = ["dog", "cat", "fish"]

WAIT_SECONDS: Final[int] = 1
FILE_COUNT: Final[int] = 3


# === DECLARE A HELPER FUNCTION TO WRITE A FILE ===


def write_text_file(*, path: Path, content: str) -> None:
    """Write content to a text file, creating parent directories as needed.

    Arguments:
        path: Full path to the file to create or overwrite.
        content: Text content to write.

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path.name}")


# === DECLARE REPETITION FUNCTION 1: FOR LOOP OVER A NUMERIC RANGE ===


def create_files_from_numeric_range() -> None:
    """Create one text file per quarter using a for loop over a range.

    WHY: Use range() when repeating logic a known number of times.
    range(start, stop + 1) produces start, start+1, ..., stop (inclusive).

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 1: for loop over a numeric range")
    LOG.info("========================")

    LOG.info(f"First quarter: {FIRST_QUARTER}")
    LOG.info(f"Last quarter:  {LAST_QUARTER}")

    for quarter_number in range(FIRST_QUARTER, LAST_QUARTER + 1):
        filename: str = f"case_quarter_{quarter_number}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Report for quarter number: {quarter_number}\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 2: FOR LOOP OVER A LIST ===


def create_files_from_list() -> None:
    """Create one text file per item in a list using a for loop.

    WHY: Use a for loop over a list when repeating logic for each item.
    The loop variable takes on each value in the list, one at a time.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 2: for loop over a list")
    LOG.info("========================")

    LOG.info(f"Pet list: {PET_LIST}")

    for pet_name in PET_LIST:
        filename: str = f"case_{pet_name}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Pet data for: '{pet_name}'\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 3: LIST COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """Create one text file per item in a transformed list.

    WHY: Use a list comprehension to transform one list into another.
    Read it as: <expression> FOR each <item> IN <list>.
    List comprehensions are more concise than a for loop building a new list.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 3: list comprehension")
    LOG.info("========================")

    prefix: str = "favorite_"

    LOG.info(f"Original list: {PET_LIST}")
    favorite_list: list[str] = [f"{prefix}{name}" for name in PET_LIST]
    LOG.info(f"Transformed list: {favorite_list}")

    for favorite in favorite_list:
        filename: str = f"case_{favorite}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Special data about: '{favorite}'\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 4: WHILE LOOP ===


def create_files_periodically() -> None:
    """Create a fixed number of files with a brief delay between each.

    WHY: Use a while loop when repeating logic until a condition becomes false.
    Always increment the counter variable to avoid an infinite loop.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 4: while loop with counter")
    LOG.info("========================")

    LOG.info(f"Files to create: {FILE_COUNT}")
    LOG.info(f"Seconds between files: {WAIT_SECONDS}")

    i: int = 1

    while i <= FILE_COUNT:
        filename: str = f"case_{i:02d}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Periodic file number: {i}\n"
        write_text_file(path=path, content=content)
        LOG.info(f"Waiting {WAIT_SECONDS} second(s)...")
        time.sleep(WAIT_SECONDS)
        i += 1  # WHY: increment to avoid an infinite loop


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None
    Returns: None
    """
    log_header(LOG, "P02")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    create_files_from_numeric_range()
    create_files_from_list()
    create_files_using_list_comprehension()
    create_files_periodically()

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: Only call main() when running this file directly as a script.
# This is standard Python boilerplate.

if __name__ == "__main__":
    main()
