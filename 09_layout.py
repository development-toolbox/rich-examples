#!/usr/bin/env python3
# 09_layout.py
example_info = {
    "title": "Layout",
    "filename": "09_layout.py",
    "description": "Creates a layout with multiple panels.",
    "explanation": "This script demonstrates how to create a terminal layout using the `Layout` class. It arranges several panels on the screen."
}
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

# Create the main layout
layout = Layout()
layout.split(
    Layout(name="upper", size=3),
    Layout(name="lower")
)

# Update the upper panel
layout["upper"].update(Panel("This is the upper panel", title="Upper"))

# Split the lower layout into two columns
layout["lower"].split_row(
    Layout(Panel("Left lower panel", title="Left")),
    Layout(Panel("Right lower panel", title="Right"))
)

console.print(layout)
