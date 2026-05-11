"""tests/test_app_case.py

Minimal tests for app_case.py.

OBS:
- Simple tests may only verify that expected callables exist.

Assumptions:
- module is importable
- pytest running from project root

Run:
  uv run python -m pytest
"""

from datafun_02_automation import app_case


def test_write_text_file_exists() -> None:
    assert callable(app_case.write_text_file)


def test_create_files_from_numeric_range_exists() -> None:
    assert callable(app_case.create_files_from_numeric_range)


def test_create_files_from_list_exists() -> None:
    assert callable(app_case.create_files_from_list)


def test_create_files_using_list_comprehension_exists() -> None:
    assert callable(app_case.create_files_using_list_comprehension)


def test_create_files_periodically_exists() -> None:
    assert callable(app_case.create_files_periodically)


def test_main_exists() -> None:
    assert callable(app_case.main)
