"""Type definitions for Seedream MCP server."""

from typing import Literal

# Seedream model types
SeedreamModel = Literal[
    "doubao-seedream-5-5-261028",
    "doubao-seedream-5-0-flash-260915",
    "doubao-seedream-5-0-pro-260628",
    "doubao-seedream-5-0-lite-260128",
    "doubao-seedream-4-5-251128",
    "doubao-seedream-4-0-250828",
]
SeedreamLayerModel = Literal[
    "doubao-seedream-5-5-261028",
    "doubao-seedream-5-0-pro-260628",
    "doubao-seedream-5-0-flash-260915",
]

# Image size presets
SeedreamSize = str

# Output image format
OutputFormat = Literal["jpeg", "png"]

BackgroundMode = Literal["auto", "transparent", "opaque"]

# Sequential image generation mode
SequentialMode = Literal["auto", "disabled"]

# Response format
ResponseFormat = Literal["url", "b64_json"]

# Task action types
TaskAction = Literal["retrieve", "retrieve_batch"]

# Tool types for model tool use
WebSearchToolType = Literal["web_search"]
