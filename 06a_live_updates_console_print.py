#!/usr/bin/env python3
# 06a_live_updates_console_print.py
example_info = {
    "title": "Rich Live Updates",
    "filename": "06a_live_updates_console_print.py",
    "description": "Displays live updates using the console.print function.",
    "explanation": "This script uses the console.print function to display live updates. It simulates a task by sleeping for three seconds, and then prints 'Done!' when the task is complete."
}
import time
from rich.console import Console

console = Console()

for i in range(10):
    console.print(f"[bold green]Update {i+1}/10[/bold green]", end="\r")
    time.sleep(0.5)
console.print("\nDone!")