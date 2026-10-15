"""Settings screen demonstrating centralized theme controls."""
import tkinter as tk
from tkinter import ttk
from app.components.cards import Card
from app.components.buttons import PrimaryButton, SecondaryButton
from app.layouts.toolbar import Toolbar

class SettingsScreen(tk.Frame):
    def __init__(self, master, theme, notify):
        self.theme, self.notify = theme, notify
        super().__init__(master, bg=theme.color("background"))
        Toolbar(self, "Settings", "Customize the template's appearance and application defaults.").pack(fill="x", pady=(0, 20))
        card = Card(self, theme, title="Appearance", subtitle="The theme manager updates ttk styles and theme-aware custom widgets.")
        card.pack(fill="x")
        ttk.Label(card.body, text="Current theme").pack(anchor="w", pady=(10, 5))
        self.theme_value = tk.StringVar(value=theme.mode.title())
        ttk.Label(card.body, textvariable=self.theme_value, font=("TkDefaultFont", 13, "bold"),
                  style="Surface.TLabel").pack(anchor="w", pady=(0, 12))
        row = ttk.Frame(card.body)
        row.pack(anchor="w")
        PrimaryButton(row, "Toggle light / dark", command=self._toggle).pack(side="left", padx=(0, 8))
        SecondaryButton(row, "Use light", command=lambda: self._set("light")).pack(side="left", padx=(0, 8))
        SecondaryButton(row, "Use dark", command=lambda: self._set("dark")).pack(side="left")
        ttk.Separator(card.body).pack(fill="x", pady=18)
        ttk.Label(card.body, text="Brand colors", style="CardTitle.TLabel").pack(anchor="w", pady=(0, 10))
        swatches = tk.Frame(card.body, bg=theme.color("surface"))
        swatches.pack(fill="x")
        self.swatches = {}
        for token in ("background", "surface", "surface_alt", "accent", "selection", "border"):
            cell = tk.Frame(swatches, bg=theme.color("surface"))
            cell.pack(side="left", padx=(0, 12))
            swatch = tk.Frame(cell, width=58, height=34, bg=theme.color(token),
                              highlightthickness=1, highlightbackground=theme.color("border"))
            swatch.pack()
            swatch.pack_propagate(False)
            ttk.Label(cell, text=token, style="SurfaceMuted.TLabel").pack(anchor="w", pady=(5, 0))
            self.swatches[token] = swatch
        theme.register(self.refresh)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def _toggle(self):
        self.theme.toggle()
        self.notify(f"Theme changed to {self.theme.mode}.")

    def _set(self, mode):
        self.theme.set_mode(mode)
        self.notify(f"Theme changed to {mode}.")

    def refresh(self):
        self.configure(bg=self.theme.color("background"))
        self.theme_value.set(self.theme.mode.title())
        for token, swatch in self.swatches.items():
            try:
                swatch.configure(bg=self.theme.color(token),
                                 highlightbackground=self.theme.color("border"))
            except tk.TclError:
                pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self.refresh)
