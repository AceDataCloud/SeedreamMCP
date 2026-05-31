# Seedream MCP

Seedream by ByteDance — text-to-image and SeedEdit instruction-based editing.

[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/acedatacloud.mcp-seedream-pro?label=VS%20Code)](https://marketplace.visualstudio.com/items?itemName=acedatacloud.mcp-seedream-pro) [![PyPI](https://img.shields.io/pypi/v/mcp-seedream-pro.svg?label=PyPI)](https://pypi.org/project/mcp-seedream-pro/) [![Hosted MCP](https://img.shields.io/badge/hosted-mcp-blue)](https://seedream.mcp.acedata.cloud/mcp)

High-resolution image generation and edit-by-instruction with ByteDance Seedream (3.0 / 4.0 / 4.5 / 5.0) and SeedEdit 3.0.

This extension registers the **seedream** MCP server with VS Code so GitHub
Copilot and any other agent that speaks the [Model Context Protocol](https://modelcontextprotocol.io/)
can call it directly from chat.

---

## Quick Start

1. **Install this extension.** VS Code registers the `seedream` MCP server automatically.
2. **Get an API token** from [Ace Data Cloud](https://platform.acedata.cloud) → *API Keys*. New accounts include free trial credit.
3. **Open Copilot Chat** in agent mode and ask for a image task — VS Code will prompt for the token the first time and store it securely.

> The default config talks to the **hosted streamable-HTTP endpoint** at
> `https://seedream.mcp.acedata.cloud/mcp` — no Python, no `uvx`, no local install needed.

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

This extension contributes the following entry to your VS Code MCP config:

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
      "description": "Ace Data Cloud API token",
      "password": true
    }
  ]
}
```

VS Code will prompt for the token on first use and persist it in the OS
secret store (Keychain / Credential Manager / libsecret).

### Alternative: local stdio (no network roundtrip)

If you prefer running the server locally — for offline dev, air-gapped
environments, or to pin to a specific PyPI version — install
[`uv`](https://docs.astral.sh/uv/) and replace your `mcp.json` entry with:

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

### Alternative: OAuth via Dynamic Client Registration

The hosted endpoint also accepts OAuth 2.1 with [DCR](https://datatracker.ietf.org/doc/html/rfc7591).
Drop the `headers` and `inputs` blocks and VS Code will run the auth flow on
first use (redirect URL `http://127.0.0.1:33418` or `https://vscode.dev/redirect`).

---

## Links

- **Hosted endpoint:** https://seedream.mcp.acedata.cloud/mcp
- **PyPI package:** [`mcp-seedream-pro`](https://pypi.org/project/mcp-seedream-pro/)
- **Source repository:** https://github.com/AceDataCloud/SeedreamMCP
- **Ace Data Cloud platform:** https://platform.acedata.cloud
- **MCP documentation:** https://docs.acedata.cloud

## License

MIT — see [LICENSE](LICENSE).
