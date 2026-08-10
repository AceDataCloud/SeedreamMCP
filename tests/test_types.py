"""Tests for Seedream API type definitions."""

from typing import get_args

from core.types import SeedreamSize


def test_seedream_size_matches_api_contract() -> None:
    """Only the size presets accepted by the API are exposed."""
    assert get_args(SeedreamSize) == ("1K", "2K", "3K", "4K")
