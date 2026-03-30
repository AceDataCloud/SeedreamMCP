"""Type definitions for Seedream MCP server."""

from typing import Literal

# Seedream model types
SeedreamModel = Literal[
    "doubao-seedream-5-0-260128",
    "doubao-seedream-4-5-251128",
    "doubao-seedream-4-0-250828",
    "doubao-seedream-3-0-t2i-250415",
    "doubao-seededit-3-0-i2i-250628",
]

# Image size presets
SeedreamSize = Literal["1K", "2K", "3K", "4K", "adaptive"]

# Output image format
OutputFormat = Literal["jpeg", "png"]

# Sequential image generation mode
SequentialMode = Literal["auto", "disabled"]

# Response format
ResponseFormat = Literal["url", "b64_json"]

# Task action types
TaskAction = Literal["retrieve", "retrieve_batch"]

# Tool types for model tool use
WebSearchToolType = Literal["web_search"]
