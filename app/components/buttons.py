"""Button helpers."""
from tkinter import ttk

class PrimaryButton(ttk.Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, style="Primary.TButton", **kwargs)

class SecondaryButton(ttk.Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

class DangerButton(ttk.Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, style="Danger.TButton", **kwargs)
