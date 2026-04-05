# MCP Seedream

<!-- mcp-name: io.github.AceDataCloud/mcp-seedream-pro -->

[![PyPI version](https://img.shields.io/pypi/v/mcp-seedream-pro.svg)](https://pypi.org/project/mcp-seedream-pro/)
[![PyPI downloads](https://img.shields.io/pypi/dm/mcp-seedream-pro.svg)](https://pypi.org/project/mcp-seedream-pro/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for AI image generation and editing using [ByteDance's Seedream](https://www.volcengine.com/product/doubao) models through the [AceDataCloud API](https://platform.acedata.cloud).

Generate and edit AI images directly from Claude, VS Code, or any MCP-compatible client.

## Features

- **Text-to-Image Generation** — Create high-quality images from text prompts (Chinese & English)
- **Image Editing** — Modify existing images with AI (style transfer, background change, virtual try-on)
- **Multiple Models** — Seedream v5.0 (flagship), v4.5, v4.0, v3.0 T2I, SeedEdit v3.0 I2I
- **Multi-Resolution** — 1K, 2K, 3K, 4K, adaptive, and custom dimensions
- **Seed Control** — Reproducible results with seed parameter (v3 models)
- **Sequential Generation** — Generate related images in sequence (v4.5/v4.0)
- **Streaming** — Progressive image delivery (v4.5/v4.0)
- **Task Tracking** — Monitor generation progress and retrieve results

## Tool Reference

| Tool | Description |
|------|-------------|
| `seedream_generate_image` | Generate an AI image from a text prompt using ByteDance's Seedream model. |
| `seedream_edit_image` | Edit or modify existing images using ByteDance's Seedream/SeedEdit model. |
| `seedream_get_task` | Query the status and result of a Seedream image generation or edit task. |
| `seedream_get_tasks_batch` | Query multiple Seedream image tasks at once. |
| `seedream_list_models` | List all available Seedream models with their capabilities and pricing. |
| `seedream_list_sizes` | List all available image sizes and resolution options for Seedream. |

## Quick Start

### 1. Get Your API Token

1. Sign up at [AceDataCloud Platform](https://platform.acedata.cloud)
2. Go to the [API documentation page](https://platform.acedata.cloud/documents/seedream-images)
3. Click **"Acquire"** to get your API token
4. Copy the token for use below

### 2. Use the Hosted Server (Recommended)

AceDataCloud hosts a managed MCP server — **no local installation required**.

**Endpoint:** `https://seedream.mcp.acedata.cloud/mcp`

All requests require a Bearer token. Use the API token from Step 1.

#### Claude.ai

Connect directly on [Claude.ai](https://claude.ai) with OAuth — **no API token needed**:

1. Go to Claude.ai **Settings → Integrations → Add More**
2. Enter the server URL: `https://seedream.mcp.acedata.cloud/mcp`
3. Complete the OAuth login flow
4. Start using the tools in your conversation

#### Claude Desktop

Add to your config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### Cursor / Windsurf

Add to your MCP config (`.cursor/mcp.json` or `.windsurf/mcp.json`):

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### VS Code (Copilot)

Add to your VS Code MCP config (`.vscode/mcp.json`):

```json
{
  "servers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

Or install the [Ace Data Cloud MCP extension](https://marketplace.visualstudio.com/items?itemName=acedatacloud.acedatacloud-mcp) for VS Code, which bundles all 11 MCP servers with one-click setup.

#### JetBrains IDEs

1. Go to **Settings → Tools → AI Assistant → Model Context Protocol (MCP)**
2. Click **Add** → **HTTP**
3. Paste:

```json
{
  "mcpServers": {
    "seedream": {
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```


#### Claude Code

Claude Code supports MCP servers natively:

```bash
claude mcp add seedream --transport http https://seedream.mcp.acedata.cloud/mcp \
  -h "Authorization: Bearer YOUR_API_TOKEN"
```

Or add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### Cline

Add to Cline's MCP settings (`.cline/mcp_settings.json`):

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### Amazon Q Developer

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### Roo Code

Add to Roo Code MCP settings:

```json
{
  "mcpServers": {
    "seedream": {
      "type": "streamable-http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

#### Continue.dev

Add to `.continue/config.yaml`:

```yaml
mcpServers:
  - name: seedream
    type: streamable-http
    url: https://seedream.mcp.acedata.cloud/mcp
    headers:
      Authorization: "Bearer YOUR_API_TOKEN"
```

#### Zed

Add to Zed's settings (`~/.config/zed/settings.json`):

```json
{
  "language_models": {
    "mcp_servers": {
      "seedream": {
        "url": "https://seedream.mcp.acedata.cloud/mcp",
        "headers": {
          "Authorization": "Bearer YOUR_API_TOKEN"
        }
      }
    }
  }
}
```

#### cURL Test

```bash
# Health check (no auth required)
curl https://seedream.mcp.acedata.cloud/health

# MCP initialize
curl -X POST https://seedream.mcp.acedata.cloud/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
```

### 3. Or Run Locally (Alternative)

If you prefer to run the server on your own machine:

```bash
# Install from PyPI
pip install mcp-seedream-pro
# or
uvx mcp-seedream-pro

# Set your API token
export ACEDATACLOUD_API_TOKEN="your_token_here"

# Run (stdio mode for Claude Desktop / local clients)
mcp-seedream-pro

# Run (HTTP mode for remote access)
mcp-seedream-pro --transport http --port 8000
```

#### Claude Desktop (Local)

```json
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": ["mcp-seedream-pro"],
      "env": {
        "ACEDATACLOUD_API_TOKEN": "your_token_here"
      }
    }
  }
}
```

#### Docker (Self-Hosting)

```bash
docker pull ghcr.io/acedatacloud/mcp-seedream-pro:latest
docker run -p 8000:8000 ghcr.io/acedatacloud/mcp-seedream-pro:latest
```

Clients connect with their own Bearer token — the server extracts the token from each request's `Authorization` header.

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
| `doubao-seedream-5-0-260128` | v5.0 | Text-to-Image | Best quality, latest flagship, web search | ~$0.040/image |
| `doubao-seedream-4-5-251128` | v4.5 | Text-to-Image | Previous flagship, great quality | ~$0.037/image |
| `doubao-seedream-4-0-250828` | v4.0 | Text-to-Image | Best value, most tasks | ~$0.030/image |
| `doubao-seedream-3-0-t2i-250415` | v3.0 | Text-to-Image | Reproducible results | ~$0.038/image |
| `doubao-seededit-3-0-i2i-250628` | v3.0 | Image-to-Image | Image editing | ~$0.046/image |

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

### Reproducible Generation

```
User: Generate a landscape and make sure I can recreate the exact same image later

Claude: I'll use the v3 model with a fixed seed.
[Calls seedream_generate_image with model=doubao-seedream-3-0-t2i-250415, seed=42]
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

This server wraps the [AceDataCloud Seedream API](https://platform.acedata.cloud/documents/seedream-images):

- [Seedream Images API](https://platform.acedata.cloud/documents/seedream-images) — Image generation and editing
- [Seedream Tasks API](https://platform.acedata.cloud/documents/seedream-tasks) — Task queries

## Use Cases

- **AI Art Creation** — Generate stunning artwork, illustrations, and digital art
- **Product Photography** — Create professional product scene compositions
- **Content Creation** — Generate images for blogs, social media, marketing
- **Virtual Try-On** — Visualize clothing on different models
- **Style Transfer** — Transform photos into different art styles
- **Game Design** — Concept art, character design, environment design
- **E-commerce** — Product mockups, lifestyle shots, banner images

## License

[MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Links

- [AceDataCloud Platform](https://platform.acedata.cloud)
- [Seedream API Documentation](https://platform.acedata.cloud/documents/seedream-images)
- [MCP Protocol](https://modelcontextprotocol.io)
- [GitHub Repository](https://github.com/AceDataCloud/SeedreamMCP)
- [PyPI Package](https://pypi.org/project/mcp-seedream-pro/)
