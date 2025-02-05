#!/usr/bin/env python3
# 04_tables.py
example_info = {
    "title": "Tables",
    "filename": "04_tables.py",
    "description": "Creates a formatted table with multiple columns."
}
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Favourite Tools")

table.add_column("Tool", justify="left", style="cyan", no_wrap=True)
table.add_column("Category", style="magenta")
table.add_column("Rating", justify="right", style="green")

table.add_row("Rich", "Terminal Output", "5/5")
table.add_row("Click", "CLI Tool", "4/5")
table.add_row("MyPy", "Static Typing", "4.5/5")

console.print(table)