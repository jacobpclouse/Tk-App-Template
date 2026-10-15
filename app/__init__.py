"""Tk App Template package."""
from tkinter import Tk
from app.config import APP_TITLE, WINDOW_GEOMETRY, MIN_WINDOW_SIZE
from app.layouts.app_shell import AppShell
from app.theme import ThemeManager

def run():
    root = Tk()
    root.title(APP_TITLE)
    root.geometry(WINDOW_GEOMETRY)
    root.minsize(*MIN_WINDOW_SIZE)
    theme = ThemeManager(root)
    AppShell(root, theme)
    root.mainloop()
