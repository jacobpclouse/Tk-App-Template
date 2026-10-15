# Component reference

## Buttons — `app.components.buttons`

- `PrimaryButton(parent, text, command=...)`: main action.
- `SecondaryButton(parent, text, command=...)`: neutral action.
- `DangerButton(parent, text, command=...)`: destructive or high-impact action.

## Cards — `app.components.cards.Card`

`Card(parent, theme, title=None, subtitle=None, padding=18)` creates a bordered surface.
Add child widgets to `card.body`, not directly to the card.

## Inputs — `app.components.inputs`

- `LabeledEntry(parent, label, textvariable=None, placeholder=None, **entry_options)`.
- `LabeledCombobox(parent, label, values, textvariable=None, **combo_options)`.

`LabeledEntry.get()` returns the field's current value. Placeholder support is deliberately basic;
for validated forms, use a `StringVar` and perform validation in the owning screen.

## Sidebar — `app.components.sidebar.Sidebar`

A responsive navigation component with `set_active(key)` and `set_compact(bool)`. It accepts
a callback called with the destination key.

## Tables — `app.components.tables.DataTable`

Construct with a sequence of column IDs and optional heading labels. Use `insert(values)` and
`clear()`. The underlying `ttk.Treeview` is available as `.tree` for selection and events.

## Tabs — `app.components.tabs.Tabs`

A thin `ttk.Notebook` wrapper with `add_tab(child, title)`.

## Dialogs — `app.components.dialogs`

`confirm(parent, title, message)`, `info(parent, title, message)`, and
`error(parent, title, message)` wrap standard message boxes.

## Feedback — `app.components.feedback.InlineNotice`

`InlineNotice(parent, message, kind="info")`; supported kinds are `info`, `success`, `warning`,
and `error`. Call `.set(message, kind)` to update it.

## Toolbar and status bar

`Toolbar(parent, title, subtitle=None, actions=None)` provides a common page header.
`StatusBar(parent, theme)` has `.set_message(text)` for status updates.


## ButtonSelector

`ButtonSelector` is a button-style radio group for mutually exclusive choices. It is useful for
formats, modes, filters, or other small sets of options. The selected option is emphasized with
the theme accent, a check mark, bold text, and a thicker outline. It refreshes immediately when
the app's `ThemeManager` changes modes.

```python
from tkinter import StringVar
from app.components.selection import ButtonSelector

format_var = StringVar(value="video")
selector = ButtonSelector(
    parent, theme,
    [("video", "▶  Video · MP4"), ("audio", "♫  Audio only · MP3")],
    variable=format_var,
    command=lambda value: print("Selected:", value),
)
selector.pack(fill="x")
```

Read the current choice with `selector.get()` or `format_var.get()`. Use `selector.select(value)`
to change it programmatically.
