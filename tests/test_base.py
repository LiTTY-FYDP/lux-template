"""Tests for lux_template.base."""

from __future__ import annotations

from typing import TYPE_CHECKING

from lux_template.base import NAME
from lux_template.cli import main

if TYPE_CHECKING:
    import pytest

EXPECTED_NAME = "lux_template"
EXPECTED_OUTPUT = "This will do something\n"


def test_base_name() -> None:
    """Expose the package name constant."""
    assert NAME == EXPECTED_NAME


def test_main_writes_default_message(capsys: pytest.CaptureFixture[str]) -> None:
    """Write the default CLI message."""
    main()

    assert capsys.readouterr().out == EXPECTED_OUTPUT
