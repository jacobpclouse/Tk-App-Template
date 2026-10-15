"""Component gallery screen."""
import tkinter as tk
from tkinter import ttk
from app.components.cards import Card
from app.components.buttons import PrimaryButton, SecondaryButton, DangerButton
from app.components.inputs import LabeledEntry, LabeledCombobox
from app.components.feedback import InlineNotice
from app.components.selection import ButtonSelector
from app.components.tabs import Tabs
from app.layouts.toolbar import Toolbar

class ComponentsScreen(tk.Frame):
    def __init__(self, master, theme, notify):
        self.theme, self.notify = theme, notify
        super().__init__(master, bg=theme.color("background"))
        Toolbar(self, "Component gallery", "Reusable controls and surfaces included with the template.").pack(fill="x", pady=(0, 20))
        canvas = tk.Canvas(self, bg=theme.color("background"), highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.inner = tk.Frame(canvas, bg=theme.color("background"))
        self.inner.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.inner, anchor="nw", tags="inner")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure("inner", width=e.width))
        self._build()
        self._canvas = canvas
        theme.register(self._refresh_canvas)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def _build(self):
        p = self.theme.palette
        buttons = Card(self.inner, self.theme, title="Buttons", subtitle="Use styles to communicate primary, secondary, and destructive actions.")
        buttons.pack(fill="x", pady=(0, 14))
        row = ttk.Frame(buttons.body)
        row.pack(fill="x", pady=(8, 0))
        PrimaryButton(row, "Primary action", command=lambda: self.notify("Primary button clicked.")).pack(side="left", padx=(0, 8))
        SecondaryButton(row, "Secondary", command=lambda: self.notify("Secondary button clicked.")).pack(side="left", padx=(0, 8))
        DangerButton(row, "Destructive", command=lambda: self.notify("Destructive action demo.")).pack(side="left")
        selector_card = Card(self.inner, self.theme, title="Button-style radio selection", subtitle="Selected options use a check mark, accent fill, bold text, and a stronger outline.")
        selector_card.pack(fill="x", pady=(0, 14))
        demo_selector = ButtonSelector(
            selector_card.body, self.theme,
            [("video", "▶  Video · MP4"), ("audio", "♫  Audio only · MP3")],
            command=lambda value: self.notify(f"Selected: {value}"),
        )
        demo_selector.pack(fill="x", pady=(8, 0))

        form = Card(self.inner, self.theme, title="Form controls", subtitle="Labeled inputs keep forms aligned and consistent.")
        form.pack(fill="x", pady=(0, 14))
        formrow = ttk.Frame(form.body)
        formrow.pack(fill="x", pady=(8, 0))
        formrow.columnconfigure((0, 1), weight=1)
        LabeledEntry(formrow, "Project name", placeholder="e.g. Data pipeline").grid(row=0, column=0, sticky="ew", padx=(0, 8))
        LabeledCombobox(formrow, "Environment", ["Development", "Testing", "Production"], state="readonly").grid(row=0, column=1, sticky="ew", padx=(8, 0))
        notice = Card(self.inner, self.theme, title="Feedback", subtitle="Use concise notices to communicate the result of an action.")
        notice.pack(fill="x", pady=(0, 14))
        for kind, message in [("info", "Information: an operation is ready to start."),
                              ("success", "Success: the sample operation completed."),
                              ("warning", "Warning: check the selected configuration."),
                              ("error", "Error: an example failure message.")]:
            InlineNotice(notice.body, message, kind).pack(fill="x", pady=3)
        tabs_card = Card(self.inner, self.theme, title="Tabs", subtitle="The ttk Notebook is a useful pattern for related views.")
        tabs_card.pack(fill="x", pady=(0, 14))
        tabs = Tabs(tabs_card.body)
        tabs.pack(fill="x", pady=(8, 0))
        for name, desc in [("Overview", "Put a short summary here."), ("Details", "Put supporting details here.")]:
            panel = ttk.Frame(tabs, padding=18)
            ttk.Label(panel, text=desc).pack(anchor="w")
            tabs.add_tab(panel, name)

    def _refresh_canvas(self):
        try:
            bg = self.theme.color("background")
            self.configure(bg=bg)
            self.inner.configure(bg=bg)
            self._canvas.configure(bg=bg)
        except (AttributeError, tk.TclError):
            pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self._refresh_canvas)
