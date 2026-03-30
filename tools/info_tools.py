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
    return """# Available Seedream Models

| Model | Version | Type | Features | Price |
|-------|---------|------|----------|-------|
| `doubao-seedream-5-0-260128` | v5.0 | Text-to-Image | Latest flagship, highest quality, sequential generation, streaming, web search | ~$0.040/image |
| `doubao-seedream-4-5-251128` | v4.5 | Text-to-Image | Previous flagship, great quality, sequential generation, streaming | ~$0.037/image |
| `doubao-seedream-4-0-250828` | v4.0 | Text-to-Image | Stable, cost-effective, sequential generation, streaming | ~$0.030/image |
| `doubao-seedream-3-0-t2i-250415` | v3.0 | Text-to-Image | Seed control, guidance scale, reproducible results | ~$0.038/image |
| `doubao-seededit-3-0-i2i-250628` | v3.0 | Image-to-Image | Image editing, style transfer, seed control, guidance scale | ~$0.046/image |

## Model Selection Guide

### For Best Quality
→ **doubao-seedream-5-0-260128** (v5.0)
- Latest flagship model with highest quality
- Best for professional/commercial use

### For Previous Flagship Quality
→ **doubao-seedream-4-5-251128** (v4.5)
- Great quality and detail
- Good for professional use

### For Best Value
→ **doubao-seedream-4-0-250828** (v4.0)
- Great balance of quality and cost
- Recommended for most use cases

### For Reproducible Results
→ **doubao-seedream-3-0-t2i-250415** (v3.0 T2I)
- Supports seed parameter for exact reproducibility
- Supports guidance_scale for fine-tuning prompt adherence

### For Image Editing
→ **doubao-seededit-3-0-i2i-250628** (v3.0 I2I)
- Dedicated editing model
- Requires input image(s)
- Best for style transfer, background changes, virtual try-on

## Feature Comparison

| Feature | v5.0 | v4.5 | v4.0 | v3.0 T2I | v3.0 I2I (Edit) |
|---------|------|------|------|----------|-----------------|
| Text-to-Image | ✅ | ✅ | ✅ | ✅ | ❌ |
| Image Editing | ❌ | ❌ | ❌ | ❌ | ✅ |
| Seed Control | ❌ | ❌ | ❌ | ✅ | ✅ |
| Guidance Scale | ❌ | ❌ | ❌ | ✅ (default 2.5) | ✅ (default 5.5) |
| Sequential Gen | ✅ | ✅ | ✅ | ❌ | ❌ |
| Streaming | ✅ | ✅ | ✅ | ❌ | ❌ |
| Web Search | ✅ | ❌ | ❌ | ❌ | ❌ |
| Resolution | 1K/2K/3K/4K/Adaptive | 1K/2K/3K/4K/Adaptive | 1K/2K/3K/4K/Adaptive | 1K/2K/3K/4K/Adaptive | 1K/2K/3K/4K/Adaptive |
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
- All models support all size options
"""
