#!/usr/bin/env python3
# 05_progress_bar.py
example_info = {
    "title": "Progress Bar",
    "filename": "05_progress_bar.py",
    "description": "Displays an interactive progress bar."
}
import time
from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    for _ in range(100):
        time.sleep(0.05)  # Simulate work
        progress.update(task, advance=1)