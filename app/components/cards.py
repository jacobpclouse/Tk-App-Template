"""Surface card with a consistent background and padding."""
import tkinter as tk
from tkinter import ttk

class Card(tk.Frame):
    def __init__(self, master, theme, title=None, subtitle=None, padding=18, **kwargs):
        self.theme = theme
        super().__init__(master, bg=theme.color("surface"), highlightthickness=1,
                         highlightbackground=theme.color("border"), bd=0, **kwargs)
        self.body = tk.Frame(self, bg=theme.color("surface"))
        self.body.pack(fill="both", expand=True, padx=padding, pady=padding)
        if title:
            ttk.Label(self.body, text=title, style="CardTitle.TLabel").pack(anchor="w")
        if subtitle:
            ttk.Label(self.body, text=subtitle, style="SurfaceMuted.TLabel",
                      wraplength=440, justify="left").pack(anchor="w", pady=(4, 10))
        theme.register(self._on_theme)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def _on_theme(self):
        try:
            self.configure(bg=self.theme.color("surface"),
                           highlightbackground=self.theme.color("border"))
            self.body.configure(bg=self.theme.color("surface"))
        except tk.TclError:
            pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self._on_theme)
