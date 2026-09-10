"""Tests for Seedream API type definitions."""

from typing import get_args

from core.types import SeedreamModel, SeedreamSize


def test_seedream_size_accepts_model_specific_presets_and_pixels() -> None:
    assert SeedreamSize is str


def test_seedream_models_expose_only_the_canonical_lite_id() -> None:
    models = get_args(SeedreamModel)

    assert models.count("doubao-seedream-5-0-lite-260128") == 1
    assert "doubao-seedream-5-0-260128" not in models
