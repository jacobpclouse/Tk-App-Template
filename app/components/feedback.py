"""Inline status / notice widget."""
import tkinter as tk

class InlineNotice(tk.Frame):
    COLORS = {
        "info": ("#E7F2FC", "#175A8C"),
        "success": ("#E3F5EA", "#176B42"),
        "warning": ("#FFF2D6", "#805900"),
        "error": ("#FCE8E6", "#A12A22"),
    }
    def __init__(self, master, message="", kind="info", **kwargs):
        super().__init__(master, bd=0, **kwargs)
        self.label = tk.Label(self, text=message, anchor="w", padx=10, pady=8,
                              font=("TkDefaultFont", 9))
        self.label.pack(fill="x")
        self.set(message, kind)

    def set(self, message, kind="info"):
        bg, fg = self.COLORS.get(kind, self.COLORS["info"])
        self.configure(bg=bg)
        self.label.configure(text=message, bg=bg, fg=fg)
