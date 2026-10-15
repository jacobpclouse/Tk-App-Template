"""Reusable screen toolbar."""
from tkinter import ttk

class Toolbar(ttk.Frame):
    def __init__(self, master, title, subtitle=None, actions=None):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        text_frame = ttk.Frame(self)
        text_frame.grid(row=0, column=0, sticky="ew")
        ttk.Label(text_frame, text=title, style="Title.TLabel").pack(anchor="w")
        if subtitle:
            ttk.Label(text_frame, text=subtitle, style="Subtitle.TLabel").pack(anchor="w", pady=(4, 0))
        if actions:
            action_frame = ttk.Frame(self)
            action_frame.grid(row=0, column=1, sticky="e", padx=(16, 0))
            for widget in actions:
                widget.pack(side="left", padx=(8, 0))
