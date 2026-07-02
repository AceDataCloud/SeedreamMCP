# Seedream MCP

Seedream by ByteDance — text-to-image and SeedEdit instruction-based editing.

[![VS Code Marketplace](https://img.shields.io/badge/VS%20Code-Marketplace-blue?logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=acedatacloud.mcp-seedream) [![PyPI](https://img.shields.io/pypi/v/mcp-seedream-pro.svg?label=PyPI)](https://pypi.org/project/mcp-seedream-pro/) [![Hosted MCP](https://img.shields.io/badge/hosted-mcp-blue)](https://seedream.mcp.acedata.cloud/mcp)

High-resolution image generation and edit-by-instruction with ByteDance Seedream (3.0 / 4.0 / 4.5 / 5.0) and SeedEdit 3.0.

This extension registers the **seedream** MCP server with VS Code so GitHub
Copilot and any other agent that speaks the [Model Context Protocol](https://modelcontextprotocol.io/)
can call it directly from chat.

---

## Quick Start

1. **Install this extension.** VS Code registers the `seedream` MCP server automatically.
2. **Get an API key** from [Ace Data Cloud](https://platform.acedata.cloud/console/applications) (Applications → API Key). New accounts include free trial credit.
3. **Open Copilot Chat** in agent mode and ask for a image task — the extension prompts for the API key the first time and stores it in the OS keychain via VS Code's `SecretStorage`.

You can rotate or remove the API key any time from the command palette:

- **Seedream MCP: Set Ace Data Cloud API Key**
- **Seedream MCP: Clear Ace Data Cloud API Key**

> The default config talks to the **hosted streamable-HTTP endpoint** at
> `https://seedream.mcp.acedata.cloud/mcp` — no Python, no `uvx`, no local install needed.

## VS Code Setup Guide

For screenshots, token setup, project-level and user-level `mcp.json`, and Copilot Agent Mode examples, see:

- [Seedream MCP VS Code guide](https://platform.acedata.cloud/documents/promotion_article_mcp_seedream_vscode)
- [All Ace Data Cloud MCP servers in VS Code](https://platform.acedata.cloud/documents/promotion_article_mcp_all_vscode)

### Example prompts

- "Generate a 2K cinematic poster of a samurai in neon Tokyo rain. Use seedream 5.0."
- "Edit https://example.com/cat.jpg — make the cat wear sunglasses."

---

## Tool Reference

**6 tools** available via this server.

| Tool | Description |
| --- | --- |
| `seedream_generate_image` | Generate an AI image from a text prompt using ByteDance's Seedream model. |
| `seedream_edit_image` | Edit or modify existing images using ByteDance's Seedream/SeedEdit model. |
| `seedream_get_task` | Query the status and result of a Seedream image generation or edit task. |
| `seedream_get_tasks_batch` | Query multiple Seedream image tasks at once. |
| `seedream_list_models` | List all available Seedream models with their capabilities and pricing. |
| `seedream_list_sizes` | List all available image sizes and resolution options for Seedream. |

## Supported Models

`seedream-3.0`, `seedream-4.0`, `seedream-4.5`, `seedream-5.0`, `seededit-3.0`

## Pricing

From $0.02 per image. Free trial credit on sign-up. See full pricing at [https://docs.acedata.cloud](https://docs.acedata.cloud).

---

## Configuration

This extension implements the `mcpServerDefinitionProviders` contribution point
and registers a single hosted server with VS Code:

```text
Provider id : acedatacloud.seedream
Server label: Seedream MCP
Server URL  : https://seedream.mcp.acedata.cloud/mcp
Transport   : Streamable HTTP
Auth        : Bearer API key from VS Code SecretStorage (or $ACEDATACLOUD_API_TOKEN)
```

You don't need to edit `mcp.json` — the extension handles registration and
token handling automatically. If you'd rather configure things by hand, the
sections below show equivalent `mcp.json` snippets you can use **instead of**
this extension.

### Alternative: manual `mcp.json` (hosted)

```jsonc
{
  "servers": {
    "seedream": {
      "type": "http",
      "url": "https://seedream.mcp.acedata.cloud/mcp",
      "headers": { "Authorization": "Bearer ${input:acedatacloud_api_token}" }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "acedatacloud_api_token",
      "description": "Ace Data Cloud API key",
      "password": true
    }
  ]
}
```

### Alternative: local stdio (no network roundtrip)

For offline dev, air-gapped environments, or pinning to a specific PyPI
version, install [`uv`](https://docs.astral.sh/uv/) and use:

```jsonc
{
  "servers": {
    "seedream": {
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-seedream-pro"],
      "env": { "ACEDATACLOUD_API_TOKEN": "${input:acedatacloud_api_token}" }
    }
  }
}
```

`uvx` will download and run the latest [`mcp-seedream-pro`](https://pypi.org/project/mcp-seedream-pro/) on demand.

---

## Links

- **Hosted endpoint:** https://seedream.mcp.acedata.cloud/mcp
- **PyPI package:** [`mcp-seedream-pro`](https://pypi.org/project/mcp-seedream-pro/)
- **Source repository:** https://github.com/AceDataCloud/SeedreamMCP
- **Ace Data Cloud platform:** https://platform.acedata.cloud
- **MCP documentation:** https://docs.acedata.cloud

## License

MIT — see [LICENSE](LICENSE).
