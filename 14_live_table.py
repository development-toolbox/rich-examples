#!/usr/bin/env python3
import time
from rich.live import Live
from rich.table import Table
from rich.console import Console

# Metadata for dynamic menu
example_info = {
    "title": "Live Updating Table",
    "filename": "14_live_table.py",
    "description": "Demonstrates a live-updating table that refreshes its data every second.",
    "explanation": "uses    with Live(generate_table(0), refresh_per_second=2) as live:\n    for i in range(1, 11):\n        live.update(generate_table(i))\n        time.sleep(1)"
}

console = Console()

def generate_table(iteration):
    table = Table(title=f"Live Data - Iteration {iteration}")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Value", style="magenta")
    for i in range(1, 6):
        table.add_row(str(i), f"Value: {iteration * i}")
    return table

with Live(generate_table(0), refresh_per_second=2) as live:
    for i in range(1, 11):
        live.update(generate_table(i))
        time.sleep(1)
