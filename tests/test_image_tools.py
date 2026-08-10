"""Contract tests for Seedream image tools."""

import tools.image_tools  # noqa: F401
from core.server import mcp


def test_image_tool_size_schemas_match_supported_presets() -> None:
    """Generate and edit tools should expose only supported size presets."""
    expected_sizes = ["1K", "2K", "3K", "4K"]

    for tool_name in ("seedream_generate_image", "seedream_edit_image"):
        tool = mcp._tool_manager._tools[tool_name]
        size_schema = tool.parameters["properties"]["size"]
        preset_schema = next(option for option in size_schema["anyOf"] if "enum" in option)

        assert preset_schema["enum"] == expected_sizes
        assert "adaptive" not in size_schema["description"].lower()
