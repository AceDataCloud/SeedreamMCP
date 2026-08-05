"""Prompt templates for Seedream MCP server.

MCP Prompts provide guidance to LLMs on when and how to use the available tools.
These are exposed via the MCP protocol and help LLMs make better decisions.
"""

from core.server import mcp


@mcp.prompt()
def seedream_image_generation_guide() -> str:
    """Guide for choosing the right Seedream tool for image tasks."""
    return """# Seedream Image Generation Guide

When the user wants to generate or edit images, choose the appropriate tool based on their needs:

## Text-to-Image Generation
**Tool:** `seedream_generate_image`
**Use when:**
- User wants to create a new image from a text description
- No existing images are involved
- User describes a scene, object, person, concept, or artwork

**Model selection:**
- v5.0 Pro (`doubao-seedream-5-0-pro-260628`): Best single-image quality
- v5.0 Lite (`doubao-seedream-5-0-260128`): Best for image sets, streaming, or web search
- v4.5 (`doubao-seedream-4-5-251128`): Best quality, latest flagship
- v4.0 (`doubao-seedream-4-0-250828`): Best value, stable and reliable (recommended default)

**Example:** "Create an image of a futuristic cityscape at sunset"
→ Call `seedream_generate_image` with a detailed prompt

## Image Editing
**Tool:** `seedream_edit_image`
**Use when:**
- User has existing image(s) to modify
- User wants to change style, background, attributes, or details
- User needs virtual try-on or product placement
- User wants to combine or transform images

**Model selection:**
- `doubao-seedream-5-0-260128`: Recommended for most edits
- 5.0 Pro, 4.5, and 4.0 also accept image input

**Example:** "Change the background of this photo to a beach"
→ Call `seedream_edit_image` with image URL and edit description

## Checking Task Results
**Tool:** `seedream_get_task`
**Use when:**
- User wants to check if generation is complete
- User asks "is my image ready?"
- Need to retrieve image URLs from a previous request

## Batch Status Check
**Tool:** `seedream_get_tasks_batch`
**Use when:**
- Multiple images were generated and need status updates
- User wants to check several tasks at once

## Model Information
**Tool:** `seedream_list_models`
**Use when:**
- User asks what models are available
- Need to compare capabilities or pricing

## Size Information
**Tool:** `seedream_list_sizes`
**Use when:**
- User asks about available image sizes or resolutions

## Important Notes:
1. Image generation is async in MCP — generation tools should return quickly with a task_id
2. After generate/edit submission, poll with `seedream_get_task` until the final image URLs are available
2. Detailed prompts produce significantly better results
3. Supports both Chinese and English prompts
4. The v4.5 model produces the highest quality but costs slightly more
5. For editing, ensure image URLs are publicly accessible or use base64
"""


@mcp.prompt()
def seedream_prompt_writing_guide() -> str:
    """Guide for writing effective Seedream image generation prompts."""
    return """# Seedream Prompt Writing Guide

## Effective Prompt Structure

A good prompt includes these elements:
- **Main Subject:** What is the primary focus of the image?
- **Style:** What artistic or photographic style? (photorealistic, anime, watercolor, etc.)
- **Atmosphere/Mood:** What feeling should the image convey? (serene, dramatic, playful)
- **Lighting:** How is the scene illuminated? (golden hour, soft studio, neon, etc.)
- **Composition:** Camera angle, lens type, framing (close-up, wide-angle, aerial)
- **Quality Keywords:** Technical quality descriptors (ultra-detailed, 8K, HDR)

## Example Prompts by Category

### Portrait Photography
"A photorealistic close-up portrait of a young woman with flowing auburn hair,
soft studio lighting with rim light, 85mm portrait lens, shallow depth of field,
warm skin tones, professional headshot quality"

### Landscape / Nature
"Breathtaking aerial view of a turquoise mountain lake surrounded by autumn
forests, dramatic clouds, golden hour lighting, landscape photography,
ultra-wide angle lens, HDR, 4K resolution"

### Product Photography
"A sleek smartphone floating at an angle, dark gradient background with
subtle reflections, professional product photography, studio lighting,
clean and minimal aesthetic, high contrast"

### Illustration / Art
"A whimsical watercolor illustration of a cozy bookshop on a rainy evening,
warm yellow light spilling from windows, cats sitting on stacks of books,
soft pastel colors, storybook style, hand-painted texture"

### Chinese Traditional Art
"一幅中国山水画，远处是云雾缭绕的青山，近处有古松和小桥流水，
一位白衣文人独坐松下抚琴，水墨风格，留白意境，宋代画风"

## Tips for Better Results

1. **Be Specific:** "elderly Japanese ceramicist" > "old man"
2. **Describe Lighting:** "soft golden hour side light" > "good lighting"
3. **Include Style:** "photorealistic", "watercolor", "3D render", "anime"
4. **Set the Mood:** "serene", "dramatic", "whimsical", "mysterious"
5. **Quality Keywords:** "ultra-detailed", "professional", "8K", "HDR"
6. **Bilingual Support:** Seedream excels at both Chinese and English prompts

## Image Editing Prompts

### Style Transfer
Prompt: "Transform this photo into a Studio Ghibli anime style"
Image: [original photo URL]

### Background Change
Prompt: "Replace the background with a tropical sunset beach"
Image: [person photo URL]

### Virtual Try-On
Prompt: "Let this person naturally wear this clothing"
Images: [person photo URL, clothing photo URL]

### Enhancement
Prompt: "Enhance this photo with vibrant colors and sharper details"
Image: [original photo URL]
"""


@mcp.prompt()
def seedream_workflow_examples() -> str:
    """Common workflow examples for Seedream image generation."""
    return """# Seedream Workflow Examples

## Workflow 1: Simple Image Generation
1. User: "Create an image of a sunset over mountains"
2. Call `seedream_generate_image(
     prompt="Breathtaking sunset over mountain range, dramatic orange and purple sky,
     alpine peaks silhouetted, landscape photography, wide-angle lens, HDR",
     model="doubao-seedream-4-0-250828"
   )`
3. Return the task_id from the submission response
4. Poll with `seedream_get_task(task_id)` until the final image URLs are available

## Workflow 2: High-Quality Generation with v4.5
1. User: "I need the highest quality image of a luxury watch"
2. Call `seedream_generate_image(
     prompt="Luxury chronograph watch, polished steel case, dark dial, leather strap,
     studio product photography, dark background with subtle reflections, 4K",
     model="doubao-seedream-4-5-251128",
     size="4K"
   )`

## Workflow 3: Image Editing
1. User provides an image URL and says "Change the background to space"
2. Call `seedream_edit_image(
     prompt="Change the background to outer space with stars and nebulae,
     keep the subject unchanged",
     image=["https://example.com/photo.jpg"],
    model="doubao-seedream-5-0-260128"
   )`

  ## Workflow 4: Sequential Image Generation
1. User: "Generate a series of related images about space exploration"
2. Call `seedream_generate_image(
     prompt="Space exploration series: astronaut on Mars surface, red landscape,
     Earth visible in sky, photorealistic",
     model="doubao-seedream-4-0-250828",
     sequential_image_generation="auto"
   )`

## Workflow 5: Batch Status Check
1. After generating multiple images, collect all task_ids
2. Call `seedream_get_tasks_batch(task_ids=["task-1", "task-2", "task-3"])`
3. Get status of all images at once

## Workflow 6: Async with Callback
1. User has a webhook endpoint
2. Call `seedream_generate_image(
     prompt="...",
     callback_url="https://example.com/webhook"
   )`
3. API returns task_id immediately
4. Result will be POSTed to callback URL when ready

## Tips:
- Always use detailed, descriptive prompts
- Start with v4.0 for best value, upgrade to v4.5 for premium quality
- For editing, image URLs must be publicly accessible
- Store task_ids for later status checking
- Seedream excels at both Chinese and English prompts
"""
