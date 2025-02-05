#!/usr/bin/env python3
# 01_basic_colors.py

# Metadata for dynamic menu
example_info = {
    "title": "Basic Colours",
    "filename": "01_basic_colors.py",
    "description": "Demonstrates basic colour formatting and text styles with Rich.",
    "explanation": "A `Console` object is created from Rich. Its `print()` method uses Rich markup to display styled text."
}
from rich.console import Console

console = Console()

console.print("[bold red]This is bold red text[/bold red]")
console.print("[green]This is green text[/green]")
console.print("[underline cyan]This is underlined cyan text[/underline cyan]")
console.print("[bold italic magenta]This is bold italic magenta text[/bold italic magenta]")
console.print("[yellow on blue]Yellow text on a blue background[/yellow on blue]")