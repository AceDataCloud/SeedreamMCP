"""Unit tests for utility functions."""

import json

from core.utils import format_image_result, format_task_result


class TestFormatImageResult:
    """Tests for format_image_result function."""

    def test_format_success(self, mock_image_response):
        """Test formatting successful image response."""
        result = format_image_result(mock_image_response)
        data = json.loads(result)
        assert data["success"] is True
        assert data["task_id"] == "test-task-123"
        assert data["trace_id"] == "test-trace-456"
        assert len(data["data"]) == 1
        assert "image_url" in data["data"][0]
        assert data["mcp_async_submission"]["poll_tool"] == "seedream_get_task"

    def test_format_edit_response(self, mock_edit_response):
        """Test formatting successful edit response."""
        result = format_image_result(mock_edit_response)
        data = json.loads(result)
        assert data["success"] is True
        assert data["task_id"] == "test-edit-789"
        assert len(data["data"]) == 1

    def test_format_preserves_all_image_elements(self):
        """Every image in the API data array should survive formatting unchanged."""
        images = [
            {
                "prompt": "first image",
                "image_url": "https://example.com/first.png",
                "size": "2048x2048",
                "metadata": {"index": 0},
            },
            {
                "prompt": "second image",
                "b64_json": "encoded-second-image",
                "size": "4096x4096",
                "metadata": {"index": 1},
            },
        ]
        response = {"success": True, "task_id": "multi-123", "data": images}

        data = json.loads(format_image_result(response))

        assert data["data"] == images

    def test_format_error(self, mock_error_response):
        """Test formatting error response."""
        result = format_image_result(mock_error_response)
        data = json.loads(result)
        assert data["success"] is False
        assert data["error"]["code"] == "invalid_request"

    def test_format_empty_data(self):
        """Test formatting response with no image data."""
        response = {"success": True, "task_id": "123", "data": []}
        result = format_image_result(response)
        data = json.loads(result)
        assert data["task_id"] == "123"
        assert data["data"] == []

    def test_format_chinese_prompt(self):
        """Test formatting response with Chinese content."""
        response = {
            "success": True,
            "task_id": "cn-123",
            "data": [{"prompt": "一只可爱的猫咪", "image_url": "https://example.com/cat.jpg"}],
        }
        result = format_image_result(response)
        data = json.loads(result)
        assert data["data"][0]["prompt"] == "一只可爱的猫咪"


class TestFormatTaskResult:
    """Tests for format_task_result function."""

    def test_format_success(self, mock_task_response):
        """Test formatting successful task response."""
        result = format_task_result(mock_task_response)
        data = json.loads(result)
        assert data["id"] == "task-123"
        assert data["request"]["model"] == "doubao-seedream-4-0-250828"
        assert data["response"]["success"] is True
        assert data["mcp_task_polling"]["poll_tool"] == "seedream_get_task"

    def test_format_error(self):
        """Test formatting error response."""
        error_response = {"error": {"code": "not_found", "message": "Task not found"}}
        result = format_task_result(error_response)
        data = json.loads(result)
        assert data["error"]["code"] == "not_found"

    def test_format_batch_result(self, mock_batch_task_response):
        """Test formatting batch task response."""
        result = format_task_result(mock_batch_task_response)
        data = json.loads(result)
        assert data["count"] == 2
        assert len(data["items"]) == 2
