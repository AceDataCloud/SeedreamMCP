# SeedreamMCP

<!-- mcp-name: io.github.AceDataCloud/mcp-seedream-pro -->

[![PyPI version](https://img.shields.io/pypi/v/mcp-seedream-pro.svg)](https://pypi.org/project/mcp-seedream-pro/)
[![PyPI downloads](https://img.shields.io/pypi/dm/mcp-seedream-pro.svg)](https://pypi.org/project/mcp-seedream-pro/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for AI image generation and editing using [ByteDance's Seedream](https://www.volcengine.com/product/doubao) models through the [AceDataCloud API](https://platform.acedata.cloud?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_platform).

Generate and edit AI images directly from Claude, VS Code, or any MCP-compatible client.

## Features

- **Text-to-Image Generation** — Create high-quality images from text prompts (Chinese & English)
- **Image Editing** — Modify existing images, including transparent-background Pro edits
- **Multiple Models** — Seedream v5.0 (flagship), v4.5, and v4.0
- **Layer Decomposition** — Split one image into a base plus up to 16 editable transparent PNG layers
- **Multi-Resolution** — Pro 1K/1.5K/2K; Lite 2K/3K/4K; custom dimensions
- **Sequential Generation** — Generate related images in sequence (5.0 Lite/4.5/4.0)
- **Web Search** — Let 5.0 Lite use current web information when needed
- **Task Tracking** — Monitor generation progress and retrieve results

## Tool Reference

| Tool | Description |
|------|-------------|
| `seedream_generate_image` | Generate an AI image from a text prompt using ByteDance's Seedream model. |
| `seedream_edit_image` | Edit images, including Seedream 5.0 Pro transparent-background mode. |
| `seedream_decompose_image` | Split one image into a base and up to 16 positioned transparent layers. |
| `seedream_get_task` | Query the status and result of a Seedream image generation or edit task. |
| `seedream_get_tasks_batch` | Query multiple Seedream image tasks at once. |
| `seedream_list_models` | List all available Seedream models with their capabilities and pricing. |
| `seedream_list_sizes` | List all available image sizes and resolution options for Seedream. |

## Seedream 5.0 capability matrix

| Capability | 5.0 Pro | 5.0 Lite |
|---|---:|---:|
| Single image generation/editing | Yes | Yes |
| Layer decomposition / transparent background | Yes | No |
| Sequential images / web search | No | Yes |
| Prompt optimization | standard, fast | standard |
| Preset sizes | 1K, 1.5K, 2K | 2K, 3K, 4K |

MCP image tools submit asynchronously and return a task id. Use `seedream_get_task` until completion. For real-time NDJSON streaming, call the REST API or CLI rather than combining `stream` with MCP async submission.

## Connect: hosted OAuth, API token, or local stdio

The hosted endpoint is `https://seedream.mcp.acedata.cloud/mcp`. Choose one route for the MCP client:

| Route | When to use it | Credential setup |
|---|---|---|
| Hosted OAuth | The client supports remote MCP OAuth | Add only the URL, then sign in to AceDataCloud and approve access. No token needs to be pasted into client configuration. |
| Hosted API token | The client cannot finish OAuth, or you need an explicit integration credential | Send an AceDataCloud API token in the `Authorization: Bearer …` header. Keep it in a local secret store or environment variable. |
| Local stdio | The client runs a local MCP process | Install `mcp-seedream-pro` and pass `ACEDATACLOUD_API_TOKEN` to that process. It still calls the AceDataCloud API. |

The hosted service advertises OAuth metadata and Dynamic Client Registration (DCR). **DCR registers the client application; it is not an API key.** OAuth signs you in and the client sends the resulting Bearer token; it may reuse or create an API credential for the account. Browser sign-in still requires an AceDataCloud account. The hosted service can be metered: review [current service documentation](https://platform.acedata.cloud/documents/seedream-mcp?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_quick_start) and displayed pricing before a real operation. Do not configure both an OAuth login and a fixed `Authorization` header for the same server.

### Hosted OAuth examples

- **Claude and Claude Desktop chat:** Add a remote custom connector in `Customize → Connectors → Add custom connector`, enter `https://seedream.mcp.acedata.cloud/mcp`, select sign-in, and choose **Register automatically** if Claude asks how to register its OAuth client. Complete consent. Claude Desktop's local `claude_desktop_config.json` is a separate setup. [Claude connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).
- **Claude Code:** `claude mcp add --transport http --scope user seedream https://seedream.mcp.acedata.cloud/mcp`, then `claude mcp login seedream`. Check `/mcp`. [Claude Code MCP guide](https://code.claude.com/docs/en/mcp).
- **Cursor:** Add a remote server with only `https://seedream.mcp.acedata.cloud/mcp`. For a project, merge the entry below into `<project>/.cursor/mcp.json`; for personal use, use `~/.cursor/mcp.json`. [Cursor MCP guide](https://cursor.com/docs/mcp).
- **VS Code / Copilot:** Run **MCP: Add Server**, select HTTP, enter `https://seedream.mcp.acedata.cloud/mcp`, then finish the browser sign-in. New portable workspace configs use `<project>/.mcp.json`; the VS Code-specific format below uses `<project>/.vscode/mcp.json` or the user profile. Check **MCP: List Servers**. [VS Code MCP setup](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- **Codex:** `codex mcp add seedream --url https://seedream.mcp.acedata.cloud/mcp`, then `codex mcp login seedream`. Its user settings are in `~/.codex/config.toml`. [Official Codex MCP guide](https://developers.openai.com/codex/mcp/).

Cursor project config (OAuth):

```json
{
  "mcpServers": {
    "seedream": {"url": "https://seedream.mcp.acedata.cloud/mcp"}
  }
}
```

VS Code-specific workspace config (OAuth):

```json
{
  "servers": {
    "seedream": {"type": "http", "url": "https://seedream.mcp.acedata.cloud/mcp"}
  }
}
```

### Hosted API token

Sign in at [AceDataCloud Platform](https://platform.acedata.cloud?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_platform), open the [service page](https://platform.acedata.cloud/documents/seedream-mcp?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_quick_start), and obtain an API credential. A fixed Bearer header is useful when your client lacks OAuth; an invalid header does not fall back to OAuth in Claude Code. The header value is sensitive, so keep it out of committed files and screenshots.

For Claude Code, the shell expands the token when you add the server; treat the saved user MCP config as a secret:

```bash
export ACEDATACLOUD_API_TOKEN='YOUR_API_TOKEN'
claude mcp add --transport http --scope user seedream https://seedream.mcp.acedata.cloud/mcp \
  --header "Authorization: Bearer $ACEDATACLOUD_API_TOKEN"
```

For a Claude Code project config, put a variable reference in `<project>/.mcp.json` and set that variable in the environment that launches Claude Code:

```json
{
  "mcpServers": {
    "seedream": {
      "type": "http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {"Authorization": "Bearer ${ACEDATACLOUD_API_TOKEN}"}
    }
  }
}
```

Cursor uses a different environment-variable syntax in `~/.cursor/mcp.json` or an uncommitted project config:

```json
{
  "mcpServers": {
    "seedream": {
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {"Authorization": "Bearer ${env:ACEDATACLOUD_API_TOKEN}"}
    }
  }
}
```

In VS Code, run **MCP: Open User Configuration** and merge this server plus its masked input; `${input:...}` is for VS Code's user/workspace format and is not portable to the Agent Host `.mcp.json` format:

```json
{
  "inputs": [
    {"id": "acedata-seedream-token", "type": "promptString", "description": "AceDataCloud API token", "password": true}
  ],
  "servers": {
    "seedream": {
      "type": "http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {"Authorization": "Bearer ${input:acedata-seedream-token}"}
    }
  }
}
```

For **Cline**, use its MCP configuration UI or CLI file `~/.cline/data/settings/cline_mcp_settings.json`; its remote transport value is `streamableHttp`. For **JetBrains AI Assistant**, add a remote URL from **Settings → Tools → AI Assistant → Model Context Protocol (MCP)**. For **Zed**, use a `context_servers` entry with the URL only for OAuth or add a local Bearer header. These clients have different configuration schemas; follow their current UI rather than copying another client's JSON. [Cline](https://docs.cline.bot/mcp/mcp-overview) · [JetBrains](https://www.jetbrains.com/help/ai-assistant/mcp.html) · [Zed](https://zed.dev/docs/ai/mcp).

### Local stdio

Install the package and give the local process an API token:

```bash
python -m pip install mcp-seedream-pro
export ACEDATACLOUD_API_TOKEN='YOUR_API_TOKEN'
mcp-seedream-pro
```

For Claude Desktop local MCP, merge this entry into the file opened by its developer settings (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS). `uvx` requires [uv](https://docs.astral.sh/uv/) on `PATH`:

```json
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": ["mcp-seedream-pro"],
      "env": {"ACEDATACLOUD_API_TOKEN": "YOUR_API_TOKEN"}
    }
  }
}
```

Keep this user-level file private. Self-hosted HTTP uses `mcp-seedream-pro --transport http --port 8000`; expose it only with suitable network and TLS controls. Local execution still calls the AceDataCloud API.

### Check before using the service

1. `https://seedream.mcp.acedata.cloud/health` returning `{"status":"ok"}` checks endpoint reachability only.
2. Confirm that the MCP client loads tools. `seedream_list_models` is a reference tool; it does not verify downstream API access or balance.
3. If you need a full API check, call `seedream_generate_image` with your own valid input after reviewing [current service documentation](https://platform.acedata.cloud/documents/seedream-mcp?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_quick_start) and displayed pricing. If the result contains a task ID, call `seedream_get_task` on that same ID until terminal success or failure. Do not resubmit the operation just to check progress.

For **401**, check which auth route the client used and whether the token or OAuth session is valid. A **403** may mean an account permission or content moderation failure; read the returned error. Insufficient balance and downstream service failures need their own diagnosis. A listed tool or submitted task does not prove a successful result.

## Available Tools

### Image Generation & Editing

| Tool                       | Description                                   |
| -------------------------- | --------------------------------------------- |
| `seedream_generate_image`  | Generate an image from a text prompt           |
| `seedream_edit_image`      | Edit or modify existing images with AI         |

### Task Management

| Tool                       | Description                                   |
| -------------------------- | --------------------------------------------- |
| `seedream_get_task`        | Query a single task status and result          |
| `seedream_get_tasks_batch` | Query multiple tasks at once                   |

### Information

| Tool                       | Description                                   |
| -------------------------- | --------------------------------------------- |
| `seedream_list_models`     | List available models with capabilities        |
| `seedream_list_sizes`      | List available image size options               |

## Available Models

| Model | Version | Type | Best For | Price |
|-------|---------|------|----------|-------|
| `doubao-seedream-5-0-pro-260628` | v5.0 Pro | Generate/Edit | Single image, transparent background, layer decomposition | Tiered Credits |
| `doubao-seedream-5-0-lite-260128` | v5.0 Lite | Text-to-Image | Sequential generation, streaming, web search | See live pricing |
| `doubao-seedream-4-5-251128` | v4.5 | Text-to-Image | Previous flagship, great quality | See live pricing |
| `doubao-seedream-4-0-250828` | v4.0 | Text-to-Image | Best value, most tasks | See live pricing |

## Usage Examples

### Generate Image from Prompt

```
User: Create a photorealistic image of a cat in a garden

Claude: I'll generate that image for you.
[Calls seedream_generate_image with detailed prompt]
→ Returns task_id and image URL
```

### Image Editing

```
User: Change the background of this photo to a beach
[Provides image URL]

Claude: I'll edit that image for you.
[Calls seedream_edit_image with image URL and edit description]
```

### Chinese Prompt Support

```
User: 生成一幅中国山水画，有远山、流水和古松

Claude: 好的，我来为您生成这幅山水画。
[Calls seedream_generate_image with Chinese prompt]
```

## Configuration

### Environment Variables

| Variable                    | Description                   | Default                     |
| --------------------------- | ----------------------------- | --------------------------- |
| `ACEDATACLOUD_API_TOKEN`    | API token from AceDataCloud   | **Required**                |
| `ACEDATACLOUD_API_BASE_URL` | API base URL                  | `https://api.acedata.cloud` |
| `ACEDATACLOUD_OAUTH_CLIENT_ID`  | OAuth client ID (hosted mode) | —                           |
| `ACEDATACLOUD_PLATFORM_BASE_URL` | Platform base URL            | `https://platform.acedata.cloud` |
| `SEEDREAM_REQUEST_TIMEOUT`  | Request timeout in seconds    | `1800`                      |
| `LOG_LEVEL`                 | Logging level                 | `INFO`                      |

### Command Line Options

```bash
mcp-seedream-pro --help

Options:
  --version          Show version
  --transport        Transport mode: stdio (default) or http
  --port             Port for HTTP transport (default: 8000)
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/AceDataCloud/SeedreamMCP.git
cd SeedreamMCP

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows

# Install with dev dependencies
pip install -e ".[dev,test]"
```

### Run Tests

```bash
# Run unit tests
pytest

# Run with coverage
pytest --cov=core --cov=tools

# Run integration tests (requires API token)
pytest -m integration
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type check
mypy core tools main.py
```

### Build & Publish

```bash
# Install build dependencies
pip install -e ".[release]"

# Build package
python -m build

# Upload to PyPI
twine upload dist/*
```

## Project Structure

```
SeedreamMCP/
├── core/                   # Core modules
│   ├── __init__.py
│   ├── client.py          # HTTP client for Seedream API
│   ├── config.py          # Configuration management
│   ├── exceptions.py      # Custom exceptions
│   ├── server.py          # MCP server initialization
│   ├── types.py           # Type definitions
│   └── utils.py           # Utility functions
├── tools/                  # MCP tool definitions
│   ├── __init__.py
│   ├── image_tools.py     # Image generation/editing tools
│   ├── task_tools.py      # Task query tools
│   └── info_tools.py      # Model & size info tools
├── prompts/                # MCP prompt templates
│   └── __init__.py
├── tests/                  # Test suite
│   ├── conftest.py
│   ├── test_config.py
│   └── test_utils.py
├── deploy/                 # Deployment configs
│   ├── run.sh
│   └── production/
│       ├── deployment.yaml
│       ├── ingress.yaml
│       └── service.yaml
├── .github/                # GitHub Actions workflows
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yaml
│       ├── claude.yml
│       ├── deploy.yaml
│       └── publish.yml
├── .env.example           # Environment template
├── .gitignore
├── .ruff.toml             # Ruff linter config
├── CHANGELOG.md
├── Dockerfile             # Docker image for HTTP mode
├── docker-compose.yaml    # Docker Compose config
├── LICENSE
├── main.py                # Entry point
├── pyproject.toml         # Project configuration
└── README.md
```

## API Reference

This server wraps the [AceDataCloud Seedream API](https://platform.acedata.cloud/documents/seedream-images?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_documents_seedream-images):

- [Seedream Images API](https://platform.acedata.cloud/documents/seedream-images?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_documents_seedream-images) — Image generation and editing
- [Seedream Tasks API](https://platform.acedata.cloud/documents/seedream-tasks?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_documents_seedream-tasks) — Task queries

## Use Cases

- **AI Art Creation** — Generate stunning artwork, illustrations, and digital art
- **Product Photography** — Create professional product scene compositions
- **Content Creation** — Generate images for blogs, social media, marketing
- **Virtual Try-On** — Visualize clothing on different models
- **Style Transfer** — Transform photos into different art styles
- **Game Design** — Concept art, character design, environment design
- **E-commerce** — Product mockups, lifestyle shots, banner images

## Documentation

<!-- canonical-documentation -->
[Documentation](https://platform.acedata.cloud/documents/seedream-mcp?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_quick_start)

## License

[MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Links

- [AceDataCloud Platform](https://platform.acedata.cloud?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_platform)
- [Seedream API Documentation](https://platform.acedata.cloud/documents/seedream-images?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=seedream_mcp_readme_documents_seedream-images)
- [MCP Protocol](https://modelcontextprotocol.io)
- [GitHub Repository](https://github.com/AceDataCloud/SeedreamMCP)
- [PyPI Package](https://pypi.org/project/mcp-seedream-pro/)
