# Getting started

## 1. Verify Python and Tkinter

```bash
python --version
python -m tkinter
```

The second command should open a small Tk window. On Ubuntu/Debian, install `python3-tk` if
Tkinter is missing.

## 2. Launch

```bash
python run.py
```

The entry point creates one `Tk` root, initializes `ThemeManager`, and mounts `AppShell`.

## 3. Add a screen

Create `app/screens/reports.py` with a class that subclasses `tk.Frame` and accepts
`(master, theme, notify)`. Register it in the `screens` dictionary in `app/layouts/app_shell.py`
and add a navigation item in `app/components/sidebar.py`.

## 4. Keep UI and business logic separate

Screens should orchestrate widgets and user interaction. Put application services, persistence,
networking, and business rules in separate modules. Avoid long-running work in callbacks.
