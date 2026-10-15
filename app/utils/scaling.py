"""Helpers for basic responsive sizing."""

def compact_layout(width, breakpoint=940):
    """Return True when the sidebar should use its compact icon-rail layout."""
    return width < breakpoint

def columns_for_width(width, minimum_card_width=280, gap=16, maximum=4):
    """Estimate a sensible number of columns for a card grid."""
    if width <= 0:
        return 1
    return max(1, min(maximum, (width + gap) // (minimum_card_width + gap)))
