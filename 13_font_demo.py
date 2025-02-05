#!/usr/bin/env python3
# 13_font_demo.py
example_info = {
    "title": "Font Demo",
    "filename": "13_font_demo.py",
    "description": "Demonstrates different fonts."
}
from rich.console import Console
from rich.panel import Panel

console = Console()

def to_math_bold(text):
    """Konverterar A-Z och a-z till deras matematiskt feta Unicode-tecken."""
    result = []
    for c in text:
        if 'A' <= c <= 'Z':
            result.append(chr(ord(c) - ord('A') + 0x1D400))
        elif 'a' <= c <= 'z':
            result.append(chr(ord(c) - ord('a') + 0x1D41A))
        else:
            result.append(c)
    return ''.join(result)

def to_math_italic(text):
    """Konverterar A-Z och a-z till deras matematiskt kursiva Unicode-tecken."""
    result = []
    for c in text:
        if 'A' <= c <= 'Z':
            result.append(chr(ord(c) - ord('A') + 0x1D434))
        elif 'a' <= c <= 'z':
            result.append(chr(ord(c) - ord('a') + 0x1D44E))
        else:
            result.append(c)
    return ''.join(result)

# Testtext att demonstrera med
sample_text = "Rich Examples"

bold_text = to_math_bold(sample_text)
italic_text = to_math_italic(sample_text)

panel_bold = Panel(bold_text, title="Mathematical Bold", border_style="blue")
panel_italic = Panel(italic_text, title="Mathematical Italic", border_style="magenta")

console.print(panel_bold)
console.print(panel_italic)

