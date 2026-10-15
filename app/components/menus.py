"""Theme-aware application menu helper."""
import tkinter as tk

def build_menu(root, theme, callbacks):
    menu = tk.Menu(root, tearoff=False)
    file_menu = tk.Menu(menu, tearoff=False)
    file_menu.add_command(label="Dashboard", command=lambda: callbacks["navigate"]("dashboard"))
    file_menu.add_command(label="Components", command=lambda: callbacks["navigate"]("components"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menu.add_cascade(label="File", menu=file_menu)
    view_menu = tk.Menu(menu, tearoff=False)
    view_menu.add_command(label="Toggle light/dark theme", command=theme.toggle)
    menu.add_cascade(label="View", menu=view_menu)
    root.configure(menu=menu)
    return menu
