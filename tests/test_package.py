"""Smoke tests for the BioPilot package."""

import biopilot


def test_package_has_version() -> None:
    """The package should expose a version string."""
    assert isinstance(biopilot.__version__, str)
    assert biopilot.__version__
