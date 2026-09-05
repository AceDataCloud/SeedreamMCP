"""Image generation and editing tools for Seedream API."""

from typing import Annotated

from pydantic import Field

from core.client import client
from core.server import mcp
from core.types import (
    BackgroundMode,
    OutputFormat,
    ResponseFormat,
    SeedreamModel,
    SeedreamSize,
    SequentialMode,
    WebSearchToolType,
)
from core.utils import format_image_result


@mcp.tool()
async def seedream_generate_image(
    prompt: Annotated[
        str,
        Field(
            description="Description of the image to generate. Be descriptive about subject, "
            "style, atmosphere, lighting, and composition. Supports both Chinese and English. "
            "Example: 'A photorealistic portrait of an astronaut on Mars, golden hour lighting, "
            "cinematic composition, ultra-detailed'"
        ),
    ],
    model: Annotated[
        SeedreamModel,
        Field(
            description="Model to use for generation. "
            "'doubao-seedream-5-0-pro-260628' (v5.0 Pro, flagship single image, highest quality; "
            "no sequential generation, streaming, or web search). "
            "'doubao-seedream-5-0-260128' (v5.0 Lite, latest flagship, sequential generation, streaming, web search). "
            "'doubao-seedream-4-5-251128' (v4.5, previous flagship, great quality). "
            "'doubao-seedream-4-0-250828' (v4.0, stable, best value)."
        ),
    ] = "doubao-seedream-5-0-260128",
    size: Annotated[
        SeedreamSize | None,
        Field(
            description="Model-specific output size: Pro supports 1K/1.5K/2K (and auto for decomposition); Lite supports 2K/3K/4K. Explicit dimensions such as 2048x1024 are also accepted."
        ),
    ] = None,
    sequential_image_generation: Annotated[
        SequentialMode | None,
        Field(
            description="Generate related images based on input. 'auto' enables it, 'disabled' "
            "(default) turns it off. Supported by Seedream 5.0 Lite, 4.5, and 4.0; not Pro."
        ),
    ] = None,
    sequential_image_generation_options: Annotated[
        dict | None,
        Field(
            description="Tunable options for grouped image generation. Only honored when "
            "`sequential_image_generation=auto`. Supports `max_images` (int, range [1, 15]). "
            "Supported by Seedream 5.0 Lite, 4.5, and 4.0; not Pro."
        ),
    ] = None,
    response_format: Annotated[
        ResponseFormat | None,
        Field(
            description="Response format for the generated image. 'url' (default) returns a "
            "public image URL. 'b64_json' returns base64-encoded image data."
        ),
    ] = None,
    watermark: Annotated[
        bool | None,
        Field(description="Whether to add an AI-generated watermark. Default is true."),
    ] = None,
    output_format: Annotated[
        OutputFormat | None,
        Field(description="Output image format. 'jpeg' (default) or 'png'."),
    ] = None,
    callback_url: Annotated[
        str,
        Field(
            description="Optional webhook URL to receive the result asynchronously. "
            "The API will POST the result to this URL when complete. "
            "Must be publicly accessible."
        ),
    ] = "",
    tools: Annotated[
        list[WebSearchToolType] | None,
        Field(
            description="Optional list of tool types for the model to use during generation. "
            "Currently only 'web_search' is supported. "
            "Only supported by doubao-seedream-5-0-260128 (v5.0)."
        ),
    ] = None,
    optimize_prompt_options: Annotated[
        dict | None,
        Field(
            description="Optional prompt optimization configuration. Supports `mode` with values "
            "'standard' (higher quality, slower) or 'fast' (quicker, lower quality). "
            "Only supported on doubao-seedream-4.5 (standard mode only) and doubao-seedream-4.0."
        ),
    ] = None,
) -> str:
    """Generate an AI image from a text prompt using ByteDance's Seedream model.

    This tool creates high-quality images from text descriptions using ByteDance's
    Seedream models (powered by Doubao). Supports multiple model versions with different
    capabilities and quality levels.

    Use this when:
    - You want to generate a new image from scratch based on a text description
    - You need high-quality AI-generated images (photos, illustrations, art)
    - You want to create images with specific styles, compositions, or themes

    Do NOT use this when:
    - You want to edit or modify an existing image (use seedream_edit_image instead)
    - You need to combine multiple images (use seedream_edit_image instead)

    Model selection guide:
    - v5.0 (doubao-seedream-5-0-260128): Latest flagship, highest quality
    - v4.5 (doubao-seedream-4-5-251128): Previous flagship, great quality and detail
    - v4.0 (doubao-seedream-4-0-250828): Stable and cost-effective, great for most tasks
    Returns:
        JSON with task_id, trace_id, success status, and generated image data
        including image URLs.
    """
    payload: dict = {
        "prompt": prompt,
        "model": model,
    }

    if size is not None:
        payload["size"] = size
    if sequential_image_generation is not None:
        payload["sequential_image_generation"] = sequential_image_generation
    if sequential_image_generation_options is not None:
        payload["sequential_image_generation_options"] = sequential_image_generation_options
    if response_format is not None:
        payload["response_format"] = response_format
    if watermark is not None:
        payload["watermark"] = watermark
    if output_format is not None:
        payload["output_format"] = output_format
    if callback_url:
        payload["callback_url"] = callback_url
    if tools is not None:
        payload["tools"] = [{"type": t} for t in tools]
    if optimize_prompt_options is not None:
        payload["optimize_prompt_options"] = optimize_prompt_options

    result = await client.generate_image(**payload)
    return format_image_result(result)


@mcp.tool()
async def seedream_edit_image(
    prompt: Annotated[
        str,
        Field(
            description="Description of the edit to perform on the image(s). Describe what "
            "changes you want. Example: 'Change the background to a beach scene', "
            "'Make the person wear a red dress', 'Convert to watercolor painting style'"
        ),
    ],
    image: Annotated[
        list[str],
        Field(
            description="List of image URLs or base64-encoded images to edit. "
            "Supports HTTP/HTTPS URLs (publicly accessible) or base64 format "
            "(data:image/png;base64,...). Each image must be under 10MB."
        ),
    ],
    model: Annotated[
        SeedreamModel,
        Field(
            description="Model to use for editing. Seedream 5.0 Pro, 5.0 Lite, 4.5, and 4.0 "
            "all support image editing when images are provided."
        ),
    ] = "doubao-seedream-5-0-260128",
    size: Annotated[
        SeedreamSize | None,
        Field(
            description="Model-specific output size or explicit dimensions. Pro supports 1K/1.5K/2K; Lite supports 2K/3K/4K."
        ),
    ] = None,
    response_format: Annotated[
        ResponseFormat | None,
        Field(description="Response format. 'url' (default) or 'b64_json'."),
    ] = None,
    watermark: Annotated[
        bool | None,
        Field(description="Whether to add an AI-generated watermark. Default is true."),
    ] = None,
    output_format: Annotated[
        OutputFormat | None,
        Field(description="Output image format. 'jpeg' (default) or 'png'."),
    ] = None,
    sequential_image_generation: Annotated[
        SequentialMode | None,
        Field(description="Generate related images based on input. 'auto' enables it."),
    ] = None,
    sequential_image_generation_options: Annotated[
        dict | None,
        Field(description="Tunable options for grouped image generation."),
    ] = None,
    tools: Annotated[
        list[WebSearchToolType] | None,
        Field(description="Optional list of tool types for the model to use during editing."),
    ] = None,
    optimize_prompt_options: Annotated[
        dict | None,
        Field(
            description="Prompt optimization. Pro supports standard/fast; Lite supports standard."
        ),
    ] = None,
    background: Annotated[
        BackgroundMode | None,
        Field(
            description="Seedream 5.0 Pro background mode. transparent requires one PNG input and PNG output."
        ),
    ] = None,
    callback_url: Annotated[
        str,
        Field(description="Optional webhook URL for async result notification."),
    ] = "",
) -> str:
    """Edit or modify existing images using ByteDance's Seedream/SeedEdit model.

    This tool modifies existing images based on text instructions. It can change
    styles, backgrounds, attributes, clothing, and more. Supports single or
    multiple image inputs.

    Use this when:
    - You want to modify or transform an existing image
    - You need to change style, background, colors, or attributes
    - You want to apply artistic transformations (watercolor, oil painting, etc.)
    - You need virtual try-on (clothing on person)
    - You want to place objects in different scenes

    Common use cases:
    - Style transfer: "Convert to anime style", "Make it look like a pencil sketch"
    - Background change: "Replace background with a sunset beach"
    - Attribute edit: "Change hair color to blonde", "Add sunglasses"
    - Virtual try-on: Provide person image + clothing image
    - Scene composition: Place products in realistic environments

    Returns:
        JSON with task_id, trace_id, success status, and edited image data
        including image URLs.
    """
    payload: dict = {
        "prompt": prompt,
        "image": image,
        "model": model,
    }

    if size is not None:
        payload["size"] = size
    if response_format is not None:
        payload["response_format"] = response_format
    if watermark is not None:
        payload["watermark"] = watermark
    if output_format is not None:
        payload["output_format"] = output_format
    if sequential_image_generation is not None:
        payload["sequential_image_generation"] = sequential_image_generation
    if sequential_image_generation_options is not None:
        payload["sequential_image_generation_options"] = sequential_image_generation_options
    if tools is not None:
        payload["tools"] = [{"type": t} for t in tools]
    if optimize_prompt_options is not None:
        payload["optimize_prompt_options"] = optimize_prompt_options
    if background is not None:
        payload["background"] = background
    if callback_url:
        payload["callback_url"] = callback_url

    result = await client.edit_image(**payload)
    return format_image_result(result)


@mcp.tool()
async def seedream_decompose_image(
    image: Annotated[str, Field(description="One PNG or JPEG URL/base64 image to decompose.")],
    prompt: Annotated[
        str,
        Field(
            description="Optional elements to decompose; omit for automatic decomposition. Supports <bbox> coordinates."
        ),
    ] = "",
    size: Annotated[str, Field(description="Output size: auto, 1K, 1.5K, or 2K.")] = "auto",
    output_format: Annotated[
        OutputFormat, Field(description="Base image format; layers are always PNG.")
    ] = "jpeg",
    watermark: Annotated[
        bool, Field(description="Whether to add an AI-generated watermark.")
    ] = True,
    callback_url: Annotated[
        str, Field(description="Optional webhook URL for async delivery.")
    ] = "",
) -> str:
    """Decompose one image into a base image and up to 16 editable transparent layers."""
    payload: dict = {
        "model": "doubao-seedream-5-0-pro-260628",
        "image": image,
        "layer_decomposition": True,
        "size": size,
        "output_format": output_format,
        "watermark": watermark,
    }
    if prompt:
        payload["prompt"] = prompt
    if callback_url:
        payload["callback_url"] = callback_url
    result = await client.edit_image(**payload)
    return format_image_result(result)
