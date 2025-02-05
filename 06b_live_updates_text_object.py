#!/usr/bin/env python3
# 06b_live_updates_text_object.py
example_info = {
    "title": "Rich Live Updates",
    "filename": "06b_live_updates_text_object.py",
    "description": "Displays live updates using the Text object."
}
import time
from rich.console import Console
from rich.text import Text

console = Console()

for i in range(10):
    text = Text(f"Update {i+1}/10", style="bold green")
    console.print(text, end="\r")
    time.sleep(0.5)
console.print("\nDone!")