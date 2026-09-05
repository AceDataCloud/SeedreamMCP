"""Contract tests for Seedream image tools."""

import tools.image_tools  # noqa: F401
from core.server import mcp


def test_image_tool_size_schemas_describe_model_specific_sizes() -> None:
    """Generate and edit tools accept presets plus explicit pixel dimensions."""
    for tool_name in ("seedream_generate_image", "seedream_edit_image"):
        tool = mcp._tool_manager._tools[tool_name]
        size_schema = tool.parameters["properties"]["size"]
        description = size_schema["description"]

        assert "1.5K" in description
        assert "2K/3K/4K" in description
        assert "dimensions" in description
        assert "adaptive" not in description.lower()


def test_decomposition_tool_exposes_pro_contract() -> None:
    tool = mcp._tool_manager._tools["seedream_decompose_image"]
    properties = tool.parameters["properties"]

    assert properties["image"]["type"] == "string"
    assert properties["size"]["default"] == "auto"
    assert properties["output_format"]["default"] == "jpeg"
    assert "stream" not in properties


def test_async_image_tools_do_not_advertise_stream() -> None:
    for tool_name in ("seedream_generate_image", "seedream_edit_image", "seedream_decompose_image"):
        assert "stream" not in mcp._tool_manager._tools[tool_name].parameters["properties"]


async def test_decomposition_tool_builds_official_payload(monkeypatch) -> None:
    from unittest.mock import AsyncMock

    from tools.image_tools import seedream_decompose_image

    request = AsyncMock(return_value={"task_id": "layer-task"})
    monkeypatch.setattr("tools.image_tools.client.edit_image", request)

    await seedream_decompose_image(image="https://cdn.example/poster.png")

    request.assert_awaited_once_with(
        model="doubao-seedream-5-0-pro-260628",
        image="https://cdn.example/poster.png",
        layer_decomposition=True,
        size="auto",
        output_format="jpeg",
        watermark=True,
    )
