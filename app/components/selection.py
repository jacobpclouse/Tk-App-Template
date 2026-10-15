"""Theme-aware button-style radio/segmented selector."""
import tkinter as tk


class ButtonSelector(tk.Frame):
    """A reusable group of mutually exclusive options styled as active buttons.

    Args:
        master: Parent widget.
        theme: The app's ThemeManager.
        options: Sequence of (value, label) pairs.
        variable: Optional tkinter StringVar shared with application state.
        command: Optional callback receiving the newly selected value.

    The active option uses the theme accent, bold text, a check mark, and a thicker
    outline. It updates immediately when the theme changes.
    """
    def __init__(self, master, theme, options, variable=None, command=None, **kwargs):
        self.theme = theme
        self.options = list(options)
        self.variable = variable or tk.StringVar(master=master, value=self.options[0][0] if self.options else "")
        self.command = command
        self._buttons = {}
        super().__init__(master, bg=theme.color("surface"), bd=0, highlightthickness=0, **kwargs)
        for index, (value, label) in enumerate(self.options):
            button = tk.Button(
                self, command=lambda selected=value: self.select(selected),
                cursor="hand2", takefocus=True, relief="flat", bd=0,
                font=("TkDefaultFont", 10), padx=14, pady=12, anchor="center",
            )
            button.grid(row=0, column=index, sticky="ew", padx=(0 if index == 0 else 4, 0))
            self.columnconfigure(index, weight=1, uniform="selector")
            self._buttons[value] = (button, label)
        self._refresh()
        theme.register(self._refresh)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def get(self):
        """Return the selected option value."""
        return self.variable.get()

    def select(self, value):
        """Select an option and invoke the optional callback."""
        if value not in self._buttons:
            raise ValueError(f"Unknown selector value: {value!r}")
        changed = self.variable.get() != value
        self.variable.set(value)
        self._refresh()
        if changed and self.command:
            self.command(value)

    def _refresh(self):
        p = self.theme.palette
        active_fg = "#FFFFFF" if self.theme.mode == "light" else "#10251B"
        try:
            self.configure(bg=p["surface"])
            for value, (button, label) in self._buttons.items():
                active = self.variable.get() == value
                icon = "✓  " if active else "○  "
                button.configure(
                    text=icon + label,
                    bg=p["accent"] if active else p["surface_alt"],
                    fg=active_fg if active else p["text"],
                    activebackground=p["accent_hover"] if active else p["selection"],
                    activeforeground=active_fg if active else p["text"],
                    highlightthickness=3 if active else 1,
                    highlightbackground=p["accent"] if active else p["border"],
                    highlightcolor=p["accent"] if active else p["border"],
                    font=("TkDefaultFont", 10, "bold" if active else "normal"),
                )
        except tk.TclError:
            pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self._refresh)
