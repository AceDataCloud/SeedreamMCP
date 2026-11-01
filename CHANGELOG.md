# Changelog

## Unreleased

- Correct the image generation prompt-optimization guide for Seedream 5.0 Pro and Lite.

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-03-08

### Added

- Initial release
- Image generation tool (`seedream_generate_image`)
- Image editing tool (`seedream_edit_image`)
- Task query tools (`seedream_get_task`, `seedream_get_tasks_batch`)
- Info tools (`seedream_list_models`, `seedream_list_sizes`)
- Support for all Seedream models (4.5, 4.0, 3.0 T2I, SeedEdit 3.0 I2I)
- Multi-resolution support (1K, 2K, 4K, adaptive)
- Seed-based reproducibility (v3 models)
- Sequential image generation (v4.5/v4.0)
- Streaming support (v4.5/v4.0)
- Guidance scale control (v3 models)
- Watermark toggle
- Async callback support
- Stdio and HTTP transport modes
- Docker support with Kubernetes deployment configs
- CI/CD pipeline with GitHub Actions
- PyPI publishing with CalVer versioning
