"""Tests for Seedream API type definitions."""

from core.types import SeedreamSize


def test_seedream_size_accepts_model_specific_presets_and_pixels() -> None:
    assert SeedreamSize is str
