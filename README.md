# Tk App Template

A reusable starter project for polished desktop apps built with **Python's Tkinter and ttk**.
It is a template project to copy and customize—not a separately installed UI framework.

The visual language is based on the supplied Tkinter file-transfer app: soft green-gray surfaces,
deep green accents, restrained borders, a clear header, cards, sidebar navigation, tables, and a
status bar. It includes a light/dark theme switch and a component gallery.

## Features

- Python standard library only; no runtime `pip install` required.
- Light and dark themes, applied centrally with immediate theme-aware component refresh.
- Reusable buttons, cards, labeled inputs, sidebar, toolbar, status bar, tables, tabs, dialogs,
  and feedback/toast-style status messages.
- Resizable sidebar: drag the vertical divider between navigation and content.
- Collapsible sidebar: use the ‹ / › control at the top of the sidebar to switch between full labels and a compact icon rail.
- Responsive layouts that continue to adapt as the window size changes.
- Dashboard, component gallery, and settings screens.
- Component gallery example.
- Unit tests for theme and component configuration.
- Documentation for getting started, theming, components, and layouts.

## Requirements

- Python 3.10 or newer.
- Tkinter must be included with your Python installation.
  - Windows: use the standard python.org installer and ensure Tcl/Tk is installed.
  - Ubuntu/Debian: if needed, install the OS package `python3-tk`.

No third-party Python packages are required.

## Run it

From this directory:

```bash
python run.py
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Customize it

1. Change the app name and initial window size in `app/config.py`.
2. Adjust the palette in `app/theme.py`.
3. Add screens in `app/screens/`.
4. Register each screen in `app/layouts/app_shell.py`.
5. Add reusable widgets under `app/components/`.
6. Read the `docs/` guides before introducing app-specific behavior.

## Project structure

```text
tk-app-template/
├── app/
│   ├── components/       # Reusable widgets
│   ├── layouts/          # App shell, toolbar, status bar
│   ├── screens/          # Dashboard, component gallery, settings
│   ├── utils/            # Scaling and icon helpers
│   ├── config.py
│   ├── styles.py
│   └── theme.py
├── docs/
├── tests/
├── run.py
└── README.md
```

## Design notes

- The palette is intentionally centralized. Avoid hard-coded colors inside new components; use
  `ThemeManager.color("token")` instead.
- Prefer `ttk` widgets for controls and `tk` frames/canvases only where custom drawing or a
  specific background is useful.
- The app shell owns navigation and screen switching. Screens should not create their own root.
- Keep long-running work off the UI thread. Tkinter callbacks should return quickly; use a worker
  thread and a thread-safe queue for background tasks, then poll the queue with `after()`.

## License

Use, modify, and redistribute this starter in your own projects.
