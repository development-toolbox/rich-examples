#!/usr/bin/env python3
# 11_layout_demo.py
example_info = {
    "title": "Layout Demo",
    "filename": "11_layout_demo.py",
    "description": "Creates a layout with a header and a body."
}
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.box import ROUNDED

console = Console()

# Create a layout divided into a header and a body
layout = Layout()
layout.split_column(
    Layout(name="header", size=3),
    Layout(name="body")
)

# Header panel with red background, yellow text and rounded corners
header_panel = Panel(
    "This is the header",
    style="bold yellow on red",
    box=ROUNDED,
    padding=(0, 1)
)
layout["header"].update(header_panel)

# A simple body panel for demonstration (also with rounded corners)
body_panel = Panel(
    "This is the body of the layout",
    box=ROUNDED,
    padding=(1, 2)
)
layout["body"].update(body_panel)

console.print(layout)

