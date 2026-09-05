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
    # Last updated: 2026-09-05
    return """# Available Seedream Models

| Model | Version | Type | Features | Price |
|-------|---------|------|----------|-------|
| `doubao-seedream-5-0-pro-260628` | v5.0 Pro | Generate/Edit | Flagship single image, transparent background, layer decomposition | Tiered Credits |
| `doubao-seedream-5-0-260128` (alias: `doubao-seedream-5-0-lite-260128`) | v5.0 Lite | Generate/Edit | Sequential generation, streaming, web search | Per successful image |
| `doubao-seedream-4-5-251128` | v4.5 | Generate/Edit | Previous flagship, sequential generation, streaming | Credits |
| `doubao-seedream-4-0-250828` | v4.0 | Generate/Edit | Stable, sequential generation, streaming | Credits |

## Model Selection Guide

### For Best Quality (single image)
→ **doubao-seedream-5-0-pro-260628** (v5.0 Pro)
- Flagship single-image model with highest quality
- Best for professional/commercial single images, transparent edits, or layer decomposition
- Supports 1K/1.5K/2K and prompt optimization standard/fast
- Does NOT support sequential generation, streaming, or web search

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
| Layer Decomposition | ✅ | ❌ | ❌ | ❌ |
| Transparent Background | ✅ | ❌ | ❌ | ❌ |
| Resolution | 1K/1.5K/2K | 2K/3K/4K | 2K/4K | 1K/2K/4K |

See the live pricing page for current Credits: https://platform.acedata.cloud/services/seedream?tab=pricing
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
    # Last updated: 2026-09-05
    return """# Seedream Image Size Options

## Preset Sizes

| Size | Description | Best For |
|------|-------------|----------|
| `1K` | ~1024px | Pro and 4.0 |
| `1.5K` | ~1536px | Pro; same tier as 1K |
| `2K` | ~2048px | All current models |
| `3K` | ~3072px | High detail, large prints |
| `4K` | ~4096px | Maximum quality, large prints |

## Custom Dimensions

You can also specify exact dimensions in `WIDTHxHEIGHT` format:
- `2048x1024` — Wide (2:1)
- `2048x2048` — Square (1:1)
- `1536x3072` — Portrait (1:2)

## Tips
- **1.5K** gives Pro more detail at the same price tier as 1K
- **4K** provides stunning detail but takes longer
- Custom dimensions give full control over aspect ratio
- Supported presets vary by model; use the model table above before choosing a size
"""
