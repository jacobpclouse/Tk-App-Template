# Layout guide

## Application shell

`AppShell` owns the sidebar, screen host, status bar, top-level menu, and navigation. Each screen
is a `Frame` mounted into the content area. Screens should not create another `Tk()` root.

## Geometry management

- Use `grid()` inside forms and small structured panels.
- Use `pack()` for simple vertical/horizontal composition.
- Do not mix `pack()` and `grid()` inside the same parent widget.
- Set row/column weights for areas that should expand.
- Use `sticky="nsew"` for widgets that should fill a grid cell.

## Responsive design

The shell uses `tk.PanedWindow` for a draggable divider. Drag the divider left or right to
change the navigation width. The ‹ / › control at the top of the sidebar collapses it to a compact
icon rail; pressing it again restores the previous width. Dashboard cards share available space
and the component gallery uses a scrollable canvas. For denser forms, consider moving fields into
a second column only above a width threshold.

## Accessibility and usability

- Keep keyboard focus visible and tab order logical.
- Give buttons specific action labels.
- Use text in addition to color to communicate state.
- Test at small window sizes and at common OS scaling settings.
- Avoid relying on Unicode symbols as final production icons; glyph appearance varies by font/OS.
