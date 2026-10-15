"""Bottom status bar."""
import tkinter as tk

class StatusBar(tk.Frame):
    def __init__(self, master, theme):
        self.theme = theme
        super().__init__(master, bg=theme.color("surface"), highlightthickness=1,
                         highlightbackground=theme.color("border"))
        self.message = tk.Label(self, text="Ready", anchor="w", padx=12, pady=7,
                                bg=theme.color("surface"), fg=theme.color("muted"))
        self.message.pack(side="left", fill="x", expand=True)
        self.mode = tk.Label(self, text="●  Local", padx=12, pady=7,
                             bg=theme.color("surface"), fg=theme.color("success"))
        self.mode.pack(side="right")
        theme.register(self.refresh_theme)

    def set_message(self, text):
        self.message.configure(text=text)

    def refresh_theme(self):
        p = self.theme.palette
        self.configure(bg=p["surface"], highlightbackground=p["border"])
        self.message.configure(bg=p["surface"], fg=p["muted"])
        self.mode.configure(bg=p["surface"], fg=p["success"])
