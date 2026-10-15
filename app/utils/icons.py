"""Tiny standard-library icon helpers.

The template intentionally avoids external icon packages. Unicode symbols are placeholders;
for a production app, bundled SVG/PNG assets can be added here or drawn with Canvas.
"""

def symbol(name):
    return {
        "home": "⌂",
        "grid": "▦",
        "settings": "⚙",
        "folder": "▰",
        "refresh": "↻",
        "check": "✓",
        "close": "×",
        "plus": "+",
    }.get(name, "•")
