"""Information and reference tools for Seedream API."""

from core.server import mcp


@mcp.tool()
async def seedream_list_models() -> str:
    """List all available Seedream models with their capabilities and pricing.

    Use this when:
    - User asks what models are available
    - You need to help choose the right model for a task
    - You want to compare model capabilities

    Returns:
        Formatted table of all Seedream models with descriptions.
    """
    # Last updated: 2026-04-05
    return """# Available Seedream Models

| Model | Version | Type | Features | Price |
|-------|---------|------|----------|-------|
| `doubao-seedream-5-0-pro-260628` | v5.0 Pro | Text-to-Image | Flagship single image, highest quality. No sequential/streaming/web search | ~$0.044-0.088/image |
| `doubao-seedream-5-0-260128` | v5.0 Lite | Text-to-Image | Latest flagship, highest quality, sequential generation, streaming, web search | ~$0.040/image |
| `doubao-seedream-4-5-251128` | v4.5 | Text-to-Image | Previous flagship, great quality, sequential generation, streaming | ~$0.037/image |
| `doubao-seedream-4-0-250828` | v4.0 | Text-to-Image | Stable, cost-effective, sequential generation, streaming | ~$0.030/image |

## Model Selection Guide

### For Best Quality (single image)
→ **doubao-seedream-5-0-pro-260628** (v5.0 Pro)
- Flagship single-image model with highest quality
- Best for professional/commercial single images
- Note: does NOT support sequential generation, streaming, or web search

### For Sequential / Streaming (v5.0)
→ **doubao-seedream-5-0-260128** (v5.0 Lite)
- Latest flagship with sequential generation, streaming, web search
- Best when you need image sets or progressive output

### For Previous Flagship Quality
→ **doubao-seedream-4-5-251128** (v4.5)
- Great quality and detail
- Good for professional use

### For Best Value
→ **doubao-seedream-4-0-250828** (v4.0)
- Great balance of quality and cost
- Recommended for most use cases

### For Image Editing
→ **doubao-seedream-5-0-260128** (v5.0 Lite)
- Accepts one or more input images
- Best for style transfer, background changes, and multi-image composition

## Feature Comparison

| Feature | v5.0 Pro | v5.0 Lite | v4.5 | v4.0 |
|---------|----------|-----------|------|------|
| Text-to-Image | ✅ | ✅ | ✅ | ✅ |
| Image Editing | ✅ | ✅ | ✅ | ✅ |
| Sequential Gen | ❌ | ✅ | ✅ | ✅ |
| Streaming | ❌ | ✅ | ✅ | ✅ |
| Web Search | ❌ | ✅ | ❌ | ❌ |
| Output Format | ✅ | ✅ | ❌ | ❌ |
| Resolution | 1K/2K | 2K/3K/4K/Adaptive | 2K/4K/Adaptive | 1K/2K/4K/Adaptive |
"""


@mcp.tool()
async def seedream_list_sizes() -> str:
    """List all available image sizes and resolution options for Seedream.

    Use this when:
    - User asks about available image sizes
    - You need to help choose the right resolution
    - You want to understand size options

    Returns:
        Formatted list of all size options with descriptions.
    """
    # Last updated: 2026-04-05
    return """# Seedream Image Size Options

## Preset Sizes

| Size | Description | Best For |
|------|-------------|----------|
| `1K` | ~1024px (default) | General use, fast generation |
| `2K` | ~2048px | Higher detail, print-ready |
| `3K` | ~3072px | High detail, large prints |
| `4K` | ~4096px | Maximum quality, large prints |
| `adaptive` | Auto-selected based on content | Let the model choose optimal size |

## Custom Dimensions

You can also specify exact dimensions in `WIDTHxHEIGHT` format:
- `1024x1024` — Square (1:1)
- `1280x720` — Landscape (16:9)
- `720x1280` — Portrait (9:16)
- `1024x768` — Landscape (4:3)
- `768x1024` — Portrait (3:4)

## Tips
- **1K** is fastest and most cost-effective
- **4K** provides stunning detail but takes longer
- **adaptive** is great when you're unsure about the best size
- Custom dimensions give full control over aspect ratio
- Supported presets vary by model; use the model table above before choosing a size
"""
