"""Responsive navigation sidebar with manual collapse and theme support."""
import tkinter as tk

NAV_ITEMS = [
    ("⌂", "Dashboard", "dashboard"),
    ("▦", "Components", "components"),
    ("⚙", "Settings", "settings"),
]

class Sidebar(tk.Frame):
    """Navigation rail. The parent shell controls the pane width; this widget controls its labels."""
    def __init__(self, master, theme, on_navigate, on_toggle=None):
        self.theme = theme
        self.on_navigate = on_navigate
        self.on_toggle = on_toggle
        self.compact = False
        super().__init__(master, bg=theme.color("surface"), width=218,
                         highlightthickness=0, bd=0)
        self.pack_propagate(False)

        self.brand = tk.Frame(self, bg=theme.color("surface"))
        self.brand.pack(fill="x", padx=12, pady=(14, 20))
        self.brand_icon = tk.Label(self.brand, text="N", bg=theme.color("accent"),
                                   fg="#FFFFFF", font=("TkDefaultFont", 13, "bold"),
                                   width=2, pady=5)
        self.brand_icon.pack(side="left")
        self.brand_text = tk.Label(self.brand, text="  Northstar", bg=theme.color("surface"),
                                   fg=theme.color("text"), font=("TkDefaultFont", 12, "bold"))
        self.brand_text.pack(side="left")
        self.toggle_button = tk.Button(
            self.brand, text="‹", width=2, relief="flat", bd=0, cursor="hand2",
            font=("TkDefaultFont", 14), command=self._toggle,
            bg=theme.color("surface"), fg=theme.color("muted"),
            activebackground=theme.color("selection"), activeforeground=theme.color("accent")
        )
        self.toggle_button.pack(side="right", padx=(4, 0))

        self.nav_frame = tk.Frame(self, bg=theme.color("surface"))
        self.nav_frame.pack(fill="x", padx=8)
        self.buttons = {}
        for icon, label, key in NAV_ITEMS:
            btn = tk.Button(self.nav_frame, text=f"  {icon}     {label}", anchor="w",
                            relief="flat", bd=0, padx=12, pady=10, cursor="hand2",
                            command=lambda k=key: on_navigate(k))
            btn.pack(fill="x", pady=2)
            self.buttons[key] = (btn, icon, label)

        self.bottom = tk.Frame(self, bg=theme.color("surface"))
        self.bottom.pack(side="bottom", fill="x", padx=8, pady=12)
        self.help_label = tk.Label(self.bottom, text="Built with Tkinter · stdlib",
                                   bg=theme.color("surface"), fg=theme.color("muted"),
                                   font=("TkDefaultFont", 8))
        self.help_label.pack(anchor="w", padx=8)
        self.active_key = "dashboard"
        self.set_active(self.active_key)
        theme.register(self.refresh_theme)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def _toggle(self):
        if self.on_toggle:
            self.on_toggle()
        else:
            self.set_compact(not self.compact)

    def set_active(self, key):
        self.active_key = key
        self.refresh_theme()

    def set_compact(self, compact):
        compact = bool(compact)
        if self.compact == compact:
            return
        self.compact = compact
        if compact:
            self.brand_text.pack_forget()
            self.brand.pack_configure(padx=8)
            self.toggle_button.configure(text="›")
            self.help_label.pack_forget()
            for btn, icon, _label in self.buttons.values():
                btn.configure(text=f" {icon} ", anchor="center", padx=4)
        else:
            self.brand_text.pack(side="left")
            self.brand.pack_configure(padx=12)
            self.toggle_button.configure(text="‹")
            self.help_label.pack(anchor="w", padx=8)
            for btn, icon, label in self.buttons.values():
                btn.configure(text=f"  {icon}     {label}", anchor="w", padx=12)
        self.refresh_theme()

    def refresh_theme(self):
        try:
            p = self.theme.palette
            self.configure(bg=p["surface"])
            self.brand.configure(bg=p["surface"])
            self.brand_icon.configure(bg=p["accent"])
            self.brand_text.configure(bg=p["surface"], fg=p["text"])
            self.toggle_button.configure(bg=p["surface"], fg=p["muted"],
                                         activebackground=p["selection"],
                                         activeforeground=p["accent"])
            self.nav_frame.configure(bg=p["surface"])
            self.bottom.configure(bg=p["surface"])
            self.help_label.configure(bg=p["surface"], fg=p["muted"])
            for key, (btn, _icon, _label) in self.buttons.items():
                active = key == self.active_key
                btn.configure(bg=p["selection"] if active else p["surface"],
                              fg=p["accent"] if active else p["text"],
                              activebackground=p["selection"], activeforeground=p["accent"])
        except tk.TclError:
            pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self.refresh_theme)
