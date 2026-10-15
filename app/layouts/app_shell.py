"""Main application shell with a draggable, collapsible sidebar."""
import tkinter as tk
from app.components.sidebar import Sidebar
from app.components.menus import build_menu
from app.layouts.status_bar import StatusBar
from app.screens.dashboard import DashboardScreen
from app.screens.components import ComponentsScreen
from app.screens.settings import SettingsScreen

class AppShell:
    def __init__(self, root, theme):
        self.root, self.theme = root, theme
        self.root.configure(bg=theme.color("background"))

        self.container = tk.Frame(root, bg=theme.color("background"))
        self.container.pack(fill="both", expand=True)

        # PanedWindow provides the draggable sash between navigation and content.
        self.panes = tk.PanedWindow(
            self.container, orient="horizontal", sashwidth=6, sashpad=1,
            sashrelief="flat", opaqueresize=True, showhandle=False,
            bg=theme.color("border"), bd=0, relief="flat"
        )
        self.panes.pack(fill="both", expand=True)

        self.sidebar = Sidebar(self.panes, theme, self.navigate, self.toggle_sidebar)
        self.main = tk.Frame(self.panes, bg=theme.color("background"))
        self.content = tk.Frame(self.main, bg=theme.color("background"))
        self.content.pack(fill="both", expand=True, padx=28, pady=24)
        self.status = StatusBar(self.main, theme)
        self.status.pack(fill="x", side="bottom")

        self.sidebar_width = 218
        self.sidebar_min_width = 72
        self.sidebar_max_width = 360
        self.sidebar_collapsed = False
        self.panes.add(self.sidebar, minsize=self.sidebar_min_width, width=self.sidebar_width, stretch="never")
        self.panes.add(self.main, minsize=420, stretch="always")

        self.screens = {
            "dashboard": DashboardScreen,
            "components": ComponentsScreen,
            "settings": SettingsScreen,
        }
        self.current_screen = None
        build_menu(root, theme, {"navigate": self.navigate})
        self.root.bind("<Configure>", self._on_resize)
        self.navigate("dashboard")

    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed
        if self.sidebar_collapsed:
            # Save the expanded width so the sidebar returns to its previous size.
            try:
                current = self.panes.sash_coord(0)[0]
                if current > self.sidebar_min_width + 10:
                    self.sidebar_width = max(self.sidebar_min_width, min(self.sidebar_max_width, current))
            except (tk.TclError, IndexError):
                pass
            self.sidebar.set_compact(True)
            self.panes.paneconfigure(self.sidebar, width=self.sidebar_min_width, minsize=self.sidebar_min_width)
        else:
            self.sidebar.set_compact(False)
            self.panes.paneconfigure(self.sidebar, width=self.sidebar_width, minsize=self.sidebar_min_width)
        self.status.set_message("Sidebar collapsed" if self.sidebar_collapsed else "Sidebar expanded")

    def navigate(self, key):
        if key not in self.screens:
            return
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.sidebar.set_active(key)
        self.current_screen = self.screens[key](self.content, self.theme, self.status.set_message)
        self.current_screen.pack(fill="both", expand=True)
        self.status.set_message(f"Viewing {key.title()}")

    def _on_resize(self, event):
        # Deliberately do not auto-collapse: users control the sidebar explicitly and can
        # resize it with the sash. The shell still remains responsive as the window changes.
        if event.widget is self.root:
            pass
