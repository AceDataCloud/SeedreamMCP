"""Verify read/write permissions in the public MCP catalog."""

from unittest.mock import AsyncMock

import pytest

from core.client import client
from core.server import mcp
from tools import image_tools, info_tools, task_tools  # noqa: F401


@pytest.mark.asyncio
async def test_catalog_marks_credit_consuming_image_operations_as_writes():
    tools = await mcp.list_tools()
    assert len(tools) == 7
    writes = {"seedream_generate_image", "seedream_edit_image", "seedream_decompose_image"}
    for tool in tools:
        public = tool.model_dump(by_alias=True, exclude_none=True)
        assert public["title"]
        hints = public["annotations"]
        is_write = tool.name in writes
        assert hints["readOnlyHint"] is (not is_write)
        # Writes create paid tasks; conservative consent protects account Credits.
        assert hints["destructiveHint"] is is_write
        assert hints["idempotentHint"] is (not is_write)
        assert hints["openWorldHint"] is (not tool.name.startswith("seedream_list_"))


@pytest.mark.asyncio
async def test_reference_first_call_does_not_generate_or_query(monkeypatch):
    generate = AsyncMock(side_effect=AssertionError("Reference calls must stay local"))
    query = AsyncMock(side_effect=AssertionError("Reference calls must stay local"))
    monkeypatch.setattr(client, "generate_image", generate)
    monkeypatch.setattr(client, "query_task", query)
    result = await mcp.call_tool("seedream_list_models", {})
    assert result
    generate.assert_not_awaited()
    query.assert_not_awaited()
