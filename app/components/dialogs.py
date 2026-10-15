"""Small dialog helpers."""
from tkinter import messagebox

def confirm(parent, title, message):
    return messagebox.askyesno(title, message, parent=parent)

def info(parent, title, message):
    messagebox.showinfo(title, message, parent=parent)

def error(parent, title, message):
    messagebox.showerror(title, message, parent=parent)
