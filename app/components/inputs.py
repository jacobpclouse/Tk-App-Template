"""Labeled form controls."""
from tkinter import ttk

class LabeledEntry(ttk.Frame):
    def __init__(self, master, label, textvariable=None, placeholder=None, **kwargs):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        ttk.Label(self, text=label).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.entry = ttk.Entry(self, textvariable=textvariable, **kwargs)
        self.entry.grid(row=1, column=0, sticky="ew")
        self.placeholder = placeholder
        if placeholder and textvariable is None:
            self.entry.insert(0, placeholder)
            self.entry.configure(foreground="#718078")
            self.entry.bind("<FocusIn>", self._clear_placeholder)
            self.entry.bind("<FocusOut>", self._restore_placeholder)

    def _clear_placeholder(self, _event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, "end")
            self.entry.configure(foreground="")

    def _restore_placeholder(self, _event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.configure(foreground="#718078")

    def get(self):
        value = self.entry.get()
        return "" if value == self.placeholder else value

class LabeledCombobox(ttk.Frame):
    def __init__(self, master, label, values, textvariable=None, **kwargs):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        ttk.Label(self, text=label).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.combo = ttk.Combobox(self, values=values, textvariable=textvariable, **kwargs)
        self.combo.grid(row=1, column=0, sticky="ew")
