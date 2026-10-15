"""Launch the main app at the component gallery."""
from tkinter import Tk
from app.config import APP_TITLE, WINDOW_GEOMETRY, MIN_WINDOW_SIZE
from app.theme import ThemeManager
from app.layouts.app_shell import AppShell

if __name__ == "__main__":
    root = Tk()
    root.title(f"{APP_TITLE} — Component Gallery")
    root.geometry(WINDOW_GEOMETRY)
    root.minsize(*MIN_WINDOW_SIZE)
    theme = ThemeManager(root)
    shell = AppShell(root, theme)
    shell.navigate("components")
    root.mainloop()
