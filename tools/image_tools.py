"""Image generation and editing tools for Seedream API."""

from typing import Annotated

from pydantic import Field

from core.client import client
from core.server import mcp
from core.types import (
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
            "'doubao-seedream-5-0-260128' (v5.0, latest flagship, highest quality). "
            "'doubao-seedream-4-5-251128' (v4.5, previous flagship, great quality). "
            "'doubao-seedream-4-0-250828' (v4.0, stable, best value). "
            "'doubao-seedream-3-0-t2i-250415' (v3 text-to-image, supports seed and guidance_scale). "
            "'doubao-seededit-3-0-i2i-250628' is for image editing only — use seedream_edit_image "
            "instead."
        ),
    ] = "doubao-seedream-5-0-260128",
    size: Annotated[
        SeedreamSize | None,
        Field(
            description="Output image resolution. '1K' (default), '2K', '3K', '4K', or 'adaptive'. "
            "You can also specify custom dimensions like '1024x1024', '1280x720', etc."
        ),
    ] = None,
    seed: Annotated[
        int | None,
        Field(
            description="Random seed for reproducible results. Range: [-1, 2147483647]. "
            "Default is -1 (random). Only works with v3 models "
            "(doubao-seedream-3-0-t2i and doubao-seededit-3-0-i2i)."
        ),
    ] = None,
    sequential_image_generation: Annotated[
        SequentialMode | None,
        Field(
            description="Generate related images based on input. 'auto' enables it, 'disabled' "
            "(default) turns it off. Only supports v4.5 and v4.0 models."
        ),
    ] = None,
    stream: Annotated[
        bool | None,
        Field(
            description="Stream all pictures progressively. Default is false. "
            "Only supports v4.5 and v4.0 models."
        ),
    ] = None,
    guidance_scale: Annotated[
        float | None,
        Field(
            description="Prompt weight — higher values make the result more closely follow the "
            "prompt. Range: [1, 10]. Default is 2.5 for doubao-seedream-3-0-t2i. "
            "Only works with v3 models."
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
    - v3 T2I (doubao-seedream-3-0-t2i-250415): Supports seed for reproducibility

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
    if seed is not None:
        payload["seed"] = seed
    if sequential_image_generation is not None:
        payload["sequential_image_generation"] = sequential_image_generation
    if stream is not None:
        payload["stream"] = stream
    if guidance_scale is not None:
        payload["guidance_scale"] = guidance_scale
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
            description="Model to use for editing. "
            "'doubao-seededit-3-0-i2i-250628' (dedicated editing model, best for image "
            "modification). Other models can also be used for editing when images are provided."
        ),
    ] = "doubao-seededit-3-0-i2i-250628",
    size: Annotated[
        SeedreamSize | None,
        Field(description="Output image resolution. '1K' (default), '2K', '3K', '4K', or 'adaptive'."),
    ] = None,
    seed: Annotated[
        int | None,
        Field(
            description="Random seed for reproducible edits. Range: [-1, 2147483647]. "
            "Default is -1 (random). Only works with v3 models."
        ),
    ] = None,
    guidance_scale: Annotated[
        float | None,
        Field(
            description="Prompt weight — higher values make edits follow the prompt more closely. "
            "Range: [1, 10]. Default is 5.5 for doubao-seededit-3-0-i2i. "
            "Only works with v3 models."
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
    if seed is not None:
        payload["seed"] = seed
    if guidance_scale is not None:
        payload["guidance_scale"] = guidance_scale
    if response_format is not None:
        payload["response_format"] = response_format
    if watermark is not None:
        payload["watermark"] = watermark
    if output_format is not None:
        payload["output_format"] = output_format
    if callback_url:
        payload["callback_url"] = callback_url

    result = await client.edit_image(**payload)
    return format_image_result(result)
