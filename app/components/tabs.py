"""Notebook helper."""
from tkinter import ttk

class Tabs(ttk.Notebook):
    def add_tab(self, child, title):
        self.add(child, text=title)
