"""Convenience wrapper around ttk.Treeview."""
from tkinter import ttk

class DataTable(ttk.Frame):
    def __init__(self, master, columns, headings=None, height=6, **kwargs):
        super().__init__(master)
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=height, **kwargs)
        for i, col in enumerate(columns):
            self.tree.heading(col, text=(headings or columns)[i])
            self.tree.column(col, anchor="w", stretch=True, width=120)
        ybar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=ybar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        ybar.grid(row=0, column=1, sticky="ns")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def insert(self, values, parent="", index="end", tags=()):
        return self.tree.insert(parent, index, values=values, tags=tags)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
