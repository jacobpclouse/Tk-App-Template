"""Example dashboard screen."""
import tkinter as tk
from tkinter import ttk
from app.components.cards import Card
from app.components.buttons import PrimaryButton, SecondaryButton
from app.components.tables import DataTable
from app.layouts.toolbar import Toolbar

class DashboardScreen(tk.Frame):
    def __init__(self, master, theme, notify):
        self.theme, self.notify = theme, notify
        super().__init__(master, bg=theme.color("background"))
        self.cards_frame = None
        self.middle_frame = None
        toolbar = Toolbar(self, "Good morning", "A clean starting point for your next desktop app.")
        toolbar.pack(fill="x", pady=(0, 22))
        cards = tk.Frame(self, bg=theme.color("background"))
        self.cards_frame = cards
        cards.pack(fill="x")
        for i, (title, value, note) in enumerate([
            ("Projects", "12", "3 recently updated"),
            ("Tasks completed", "84%", "Up 8% this week"),
            ("System status", "Healthy", "All services responding"),
        ]):
            card = Card(cards, theme, title=title, padding=16)
            card.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 10, 0))
            cards.columnconfigure(i, weight=1, uniform="metric")
            ttk.Label(card.body, text=value, style="Title.TLabel").pack(anchor="w", pady=(12, 5))
            ttk.Label(card.body, text=note, style="SurfaceMuted.TLabel").pack(anchor="w")
        middle = tk.Frame(self, bg=theme.color("background"))
        self.middle_frame = middle
        middle.pack(fill="both", expand=True, pady=(18, 0))
        activity = Card(middle, theme, title="Recent activity", subtitle="A sample data table you can replace with your own records.")
        activity.pack(side="left", fill="both", expand=True, padx=(0, 10))
        table = DataTable(activity.body, ("task", "status", "updated"),
                          ("Item", "Status", "Updated"), height=6)
        table.pack(fill="both", expand=True, pady=(8, 0))
        for row in [
            ("Refresh inventory report", "Completed", "Today, 9:42 AM"),
            ("Review data import", "In progress", "Today, 9:15 AM"),
            ("Update connection profile", "Queued", "Yesterday"),
            ("Archive old exports", "Completed", "Yesterday"),
        ]:
            table.insert(row)
        quick = Card(middle, theme, title="Quick actions", subtitle="Example actions for wiring into your app.")
        quick.pack(side="left", fill="y", padx=(10, 0))
        PrimaryButton(quick.body, text="Create new item",
                      command=lambda: notify("New-item action clicked (replace with your workflow).")).pack(fill="x", pady=(12, 8))
        SecondaryButton(quick.body, text="Open component gallery",
                        command=lambda: notify("Use the sidebar to open Components.")).pack(fill="x")
        ttk.Label(quick.body, text="Tip: keep callbacks short.\nMove slow work off the UI thread.",
                  style="SurfaceMuted.TLabel", justify="left").pack(anchor="w", pady=(18, 0))

        theme.register(self.refresh_theme)
        self.bind("<Destroy>", self._on_destroy, add="+")

    def refresh_theme(self):
        try:
            bg = self.theme.color("background")
            self.configure(bg=bg)
            self.cards_frame.configure(bg=bg)
            self.middle_frame.configure(bg=bg)
        except tk.TclError:
            pass

    def _on_destroy(self, event):
        if event.widget is self:
            self.theme.unregister(self.refresh_theme)
