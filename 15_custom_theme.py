#!/usr/bin/env python3
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel

# Metadata for dynamic menu
example_info = {
    "title": "Custom Theme Demo",
    "filename": "15_custom_theme.py",
    "description": "Demonstrates how to use a custom Rich theme to style output.",
    "explanation": "The `Console` object is created from Rich with a custom theme. The `print()` method uses Rich markup to display styled text."
}

# Define a custom theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

console = Console(theme=custom_theme)

console.print(Panel("This is an info message", style="info", title="Info"))
console.print(Panel("This is a warning message", style="warning", title="Warning"))
console.print(Panel("This is a danger message", style="danger", title="Danger"))
