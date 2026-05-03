import os
import re
import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("DaisyUI-Expert-Python")

# Path to the big component documentation file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_FILE = os.path.join(SCRIPT_DIR, "component_content.md")

def load_components():
    """Parses the component_content.md and returns a dictionary of components."""
    if not os.path.exists(DOCS_FILE):
        return {}
    
    with open(DOCS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split content by the separator we added
    sections = content.split("\n---\n")
    components = {}
    
    for section in sections:
        # Look for the ## Heading which is our component title
        match = re.search(r"##\s*(.*)", section)
        if match:
            title = match.group(1).strip()
            # Clean title (remove trailing daisyUI etc)
            clean_title = re.sub(r" [-–] daisyUI.*", "", title).lower()
            components[clean_title] = section.strip()
            
    return components

# Global cache for components
COMPONENTS_CACHE = load_components()

@mcp.tool()
def list_components() -> str:
    """Lists all available DaisyUI components in the library."""
    titles = sorted([name.capitalize() for name in COMPONENTS_CACHE.keys()])
    return "\n".join([f"- {t}" for t in titles if t])

@mcp.tool()
def get_component(name: str) -> str:
    """
    Retrieves full documentation and code examples for a specific DaisyUI component.
    Args:
        name: The name of the component (e.g., 'button', 'card', 'modal')
    """
    name = name.lower().strip()
    
    # Try fuzzy matching
    found_key = None
    if name in COMPONENTS_CACHE:
        found_key = name
    else:
        for key in COMPONENTS_CACHE.keys():
            if name in key:
                found_key = key
                break
    
    if not found_key:
        return f"Error: Component '{name}' not found. Use list_components to see available components."
    
    doc = COMPONENTS_CACHE[found_key]
    
    # Extract only the relevant component section if it's within a larger block (like llms.txt)
    if "### " + name in doc:
        # Simple extraction logic: find the ### name and take until the next ### or end
        parts = re.split(r"(### .*)", doc)
        for i, p in enumerate(parts):
            if p.lower().startswith(f"### {name}"):
                doc = p + (parts[i+1] if i+1 < len(parts) else "")
                break

    # Add Antigravity Design Tips automatically
    tips = "\n\n--- \n✨ **ANTIGRAVITY DESIGN TIPS FOR " + found_key.upper() + "** ✨\n"
    tips += "- **Aesthetics**: Always use semantic colors (primary, secondary, accent) instead of raw hex values.\n"
    tips += "- **Interaction**: Use `transition-all duration-300` for smooth hover states.\n"
    tips += "- **Premium Feel**: Combine with subtle shadows (`shadow-sm` or `shadow-xl`) for depth.\n"
    tips += "- **Responsiveness**: Use DaisyUI responsive classes (e.g., `btn-sm md:btn-md`) for all viewports.\n"
    
    return doc + tips

@mcp.tool()
def search_docs(query: str) -> str:
    """
    Search across all DaisyUI component documentation for a specific term or feature.
    """
    query = query.lower()
    results = []
    
    for name, content in COMPONENTS_CACHE.items():
        if query in name or query in content.lower():
            results.append(f"### {name.capitalize()}\n{content[:500]}...\n")
            
    if not results:
        return f"No results found for '{query}'."
    
    return "\n\n".join(results[:5]) # Limit to top 5 results

@mcp.tool()
def get_boilerplate() -> str:
    """
    Returns the standard HTML5 boilerplate with DaisyUI v5 and Tailwind CSS v4 CDN links.
    Use this as the starting point for any new UI design.
    """
    return """
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DaisyUI v5 Design</title>
    <!-- DaisyUI v5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <!-- All DaisyUI Themes (Optional but recommended) -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
    <!-- Tailwind CSS v4 Browser Script -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="min-h-screen bg-base-200">
    <!-- Your content here -->
</body>
</html>
"""

@mcp.resource("daisyui://design-guide")
def get_design_guide() -> str:
    """Returns the internal Antigravity design philosophy for premium UI generation."""
    return """
# Antigravity DaisyUI Design Philosophy

## 1. Fast Setup (CDN)
Always use these latest links for DaisyUI v5 and Tailwind v4:
- CSS: https://cdn.jsdelivr.net/npm/daisyui@5
- Themes: https://cdn.jsdelivr.net/npm/daisyui@5/themes.css
- Tailwind JS: https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4

## 2. Aesthetics
- Use `data-theme` on the `<html>` tag to switch themes (e.g., cupcake, night, luxury).
- Use `bg-base-200` or `bg-base-300` for page backgrounds to make components "pop".
- Combine DaisyUI components with standard Tailwind spacing (`p-4`, `m-2`, `gap-4`).

## 3. Premium Touches
- Add `transition-all duration-300` to buttons.
- Use `mask` classes for creative image shapes.
- Leverage the Popover API for dropdowns and tooltips where possible.
"""

@mcp.prompt()
def expert_instruction() -> str:
    """Instruction for the AI to proactively use DaisyUI tools."""
    return """You are a DaisyUI Expert. 
Whenever the user mentions keywords like 'daisyui', 'daisy ui', or 'daisy mcp', you MUST proactively trigger the DaisyUI MCP tools. 
- Use 'list_components' if the user is looking for inspiration.
- Use 'get_component' if a specific component is mentioned.
- Use 'search_docs' for general design questions.
Always prioritize premium, modern, and high-performance UI generation using DaisyUI v5 and Tailwind v4. Do not guess; use the provided context."""

if __name__ == "__main__":
    mcp.run()
