# Seedream MCP — JetBrains Plugin

AI Image Generation with [ByteDance Seedream](https://www.volcengine.com) via [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) for JetBrains IDEs.

<!-- Plugin description -->
This plugin helps you set up the MCP ByteDance Seedream server with JetBrains AI Assistant.
Once configured, AI Assistant can generate and edit images
— all powered by [Ace Data Cloud](https://platform.acedata.cloud).

**6 AI Tools** — Generate and edit images.
<!-- Plugin description end -->

## Quick Start

1. Install this plugin from the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/com.acedatacloud.mcp.seedream)
2. Open **Settings → Tools → Seedream MCP**
3. Enter your [Ace Data Cloud](https://platform.acedata.cloud) API token
4. Click **Copy Config** (STDIO or HTTP)
5. Paste into **Settings → Tools → AI Assistant → Model Context Protocol (MCP)**

### STDIO Mode (Local)

Runs the MCP server locally. Requires [uv](https://github.com/astral-sh/uv) installed.

```json
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": ["mcp-seedream-pro"],
      "env": {
        "ACEDATACLOUD_API_TOKEN": "your-token"
      }
    }
  }
}
```

### HTTP Mode (Remote)

Connects to the hosted MCP server at `seedream.mcp.acedata.cloud`. No local install needed.

```json
{
  "mcpServers": {
    "seedream": {
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

## Links

- [Ace Data Cloud Platform](https://platform.acedata.cloud)
- [Documentation](https://platform.acedata.cloud/documents/seedream-mcp)
- [PyPI Package](https://pypi.org/project/mcp-seedream-pro/)
- [Source Code](https://github.com/AceDataCloud/SeedreamMCP)

## License

MIT
