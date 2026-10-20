"""Centralized light/dark theme tokens and ttk styling."""
from tkinter import ttk

PALETTES = {
    "light": {
        "background": "#F1F5F2",
                # "background": "#02FAFA",
        "surface": "#FFFFFF",
        "surface_alt": "#E6EEE9",
        "border": "#D1DDD6",
        "text": "#1C2D26",
        "muted": "#62736A",
        "accent": "#177A5C",
        "accent_hover": "#12664C",
        "accent_soft": "#D5ECE1",
        "selection": "#D5ECE1",
        "danger": "#B42318",
        "warning": "#946200",
        "success": "#177A5C",
        "vscode": "#007ACC",
        "vscode_hover": "#005A9E",
        "input": "#FFFFFF",
        "disabled": "#AAB8B0",
    },
    "dark": {
        "background": "#151C19",
        "surface": "#202A25",
        "surface_alt": "#29362F",
        "border": "#3B4B42",
        "text": "#E8F0EB",
        "muted": "#A0B1A7",
        "accent": "#56C49A",
        "accent_hover": "#79D7B0",
        "accent_soft": "#294B3D",
        "selection": "#294B3D",
        "danger": "#FF8178",
        "warning": "#F0C36D",
        "success": "#56C49A",
        "vscode": "#2F9DE0",
        "vscode_hover": "#62B7EF",
        "input": "#1B2420",
        "disabled": "#65756B",
    },
}

class ThemeManager:
    """Applies palette tokens to ttk styles and notifies theme-aware widgets."""
    def __init__(self, root, mode="light"):
        self.root = root
        self.mode = mode if mode in PALETTES else "light"
        self.style = ttk.Style(root)
        try:
            self.style.theme_use("clam")
        except Exception:
            pass
        self._listeners = []
        self.apply()

    @property
    def palette(self):
        return PALETTES[self.mode]

    def color(self, token):
        return self.palette[token]

    def register(self, callback):
        if callback not in self._listeners:
            self._listeners.append(callback)

    def unregister(self, callback):
        if callback in self._listeners:
            self._listeners.remove(callback)

    def toggle(self):
        self.set_mode("dark" if self.mode == "light" else "light")

    def set_mode(self, mode):
        if mode not in PALETTES:
            raise ValueError(f"Unknown theme mode: {mode!r}")
        if mode == self.mode:
            return
        self.mode = mode
        self.apply()
        for callback in tuple(self._listeners):
            callback()

    def apply(self):
        p = self.palette
        self.root.configure(bg=p["background"])
        s = self.style
        s.configure(".", background=p["background"], foreground=p["text"],
                    font=("TkDefaultFont", 10), bordercolor=p["border"])
        s.configure("TFrame", background=p["background"])
        s.configure("Surface.TFrame", background=p["surface"])
        s.configure("Alt.TFrame", background=p["surface_alt"])
        s.configure("TLabel", background=p["background"], foreground=p["text"])
        s.configure("Muted.TLabel", background=p["background"], foreground=p["muted"])
        s.configure("Surface.TLabel", background=p["surface"], foreground=p["text"])
        s.configure("SurfaceMuted.TLabel", background=p["surface"], foreground=p["muted"])
        s.configure("Title.TLabel", background=p["background"], foreground=p["text"],
                    font=("TkDefaultFont", 21, "bold"))
        s.configure("Subtitle.TLabel", background=p["background"], foreground=p["muted"],
                    font=("TkDefaultFont", 10))
        s.configure("CardTitle.TLabel", background=p["surface"], foreground=p["text"],
                    font=("TkDefaultFont", 11, "bold"))
        s.configure("TButton", padding=(12, 8), background=p["surface_alt"],
                    foreground=p["text"], bordercolor=p["border"])
        s.map("TButton", background=[("active", p["selection"]), ("disabled", p["surface_alt"])],
              foreground=[("disabled", p["disabled"])])
        s.configure("Primary.TButton", padding=(13, 8), background=p["accent"],
                    foreground="#FFFFFF", bordercolor=p["accent"], font=("TkDefaultFont", 10, "bold"))
        s.map("Primary.TButton", background=[("active", p["accent_hover"])],
              foreground=[("disabled", p["disabled"])])
        s.configure("Accent.TButton", padding=(12, 8), background=p["accent_soft"],
                    foreground=p["accent"], bordercolor=p["accent_soft"])
        s.map("Accent.TButton", background=[("active", p["selection"])])
        s.configure("Danger.TButton", padding=(12, 8), background=p["surface"],
                    foreground=p["danger"], bordercolor=p["border"])
        s.configure("TEntry", padding=8, fieldbackground=p["input"], foreground=p["text"],
                    bordercolor=p["border"], insertcolor=p["text"])
        s.map("TEntry", fieldbackground=[("disabled", p["surface_alt"])])
        s.configure("TCombobox", padding=7, fieldbackground=p["input"], foreground=p["text"],
                    background=p["surface"], arrowcolor=p["muted"], bordercolor=p["border"])
        s.map("TCombobox", fieldbackground=[("readonly", p["input"])],
              foreground=[("readonly", p["text"])], selectbackground=[("readonly", p["selection"])])
        s.configure("TCheckbutton", background=p["background"], foreground=p["text"])
        s.map("TCheckbutton", background=[("active", p["background"])])
        s.configure("TRadiobutton", background=p["background"], foreground=p["text"])
        s.configure("TNotebook", background=p["background"], borderwidth=0, tabmargins=(0, 0, 0, 0))
        s.configure("TNotebook.Tab", padding=(14, 9), background=p["surface_alt"],
                    foreground=p["muted"], borderwidth=0)
        s.map("TNotebook.Tab", background=[("selected", p["surface"])],
              foreground=[("selected", p["accent"])])
        s.configure("Treeview", background=p["surface"], fieldbackground=p["surface"],
                    foreground=p["text"], bordercolor=p["border"], rowheight=31)
        s.configure("Treeview.Heading", background=p["surface_alt"], foreground=p["text"],
                    font=("TkDefaultFont", 9, "bold"), padding=8)
        s.map("Treeview", background=[("selected", p["selection"])],
              foreground=[("selected", p["text"])])
        s.configure("Horizontal.TProgressbar", troughcolor=p["surface_alt"],
                    background=p["accent"], bordercolor=p["border"])
        s.configure("Vertical.TScrollbar", background=p["surface_alt"], troughcolor=p["background"],
                    bordercolor=p["background"], arrowcolor=p["muted"])
        s.configure("Horizontal.TScrollbar", background=p["surface_alt"], troughcolor=p["background"],
                    bordercolor=p["background"], arrowcolor=p["muted"])
