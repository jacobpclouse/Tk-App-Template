# Theme system

The palette lives in `app/theme.py` as `PALETTES["light"]` and `PALETTES["dark"]`.
Both modes expose the same tokens: `background`, `surface`, `surface_alt`, `border`, `text`,
`muted`, `accent`, `accent_hover`, `accent_soft`, `selection`, `danger`, `warning`, `success`,
`vscode`, `vscode_hover`, `input`, and `disabled`.

Use `theme.color("surface")` for custom `tk.Frame`, `tk.Canvas`, or `tk.Label` colors. Prefer ttk
styles for ordinary controls. Do not scatter hex values through screens.

## Theme-aware custom widgets

Register a callback with `theme.register(callback)` when a custom widget needs to update colors.
Unregister it when the widget is destroyed. `Card` and `Sidebar` demonstrate this pattern.
`ThemeManager.set_mode("dark")` changes the palette and refreshes ttk styles; `theme.toggle()`
switches between modes.

## Notes

- ttk controls follow the centralized ttk style configuration.
- Custom `tk` widgets need explicit palette updates.
- `InlineNotice` uses semantic colors with high contrast. If you need strict dark-mode semantic
  colors, move its notice palette into `PALETTES` and update it from a theme callback.
