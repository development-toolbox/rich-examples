#!/usr/bin/env python3
# 12_font_demo.py
example_info = {
    "title": "Font Demo",
    "filename": "12_font_demo.py",
    "description": "Demonstrates different pyfiglet fonts."
}
import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()

# List of cool pyfiglet fonts to demo
fonts = ["slant", "3-d", "banner3-D", "digital"]

for font in fonts:
    ascii_art = pyfiglet.figlet_format("Rich", font=font)
    panel = Panel(ascii_art, title=f"[bold]{font}[/bold]", border_style="blue", expand=False)
    console.print(panel)

