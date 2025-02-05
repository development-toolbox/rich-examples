#!/usr/bin/env python3
# 03_syntax_highlight.py
example_info = {
    "title": "Syntax Highlighting",
    "filename": "03_syntax_highlight.py",
    "description": "Highlights JSON code with a colour theme."
}
from rich.console import Console
from rich.syntax import Syntax

console = Console()

json_data = '{"name": "Alice", "language": "Python"}'
syntax = Syntax(json_data, "json", theme="monokai", line_numbers=True)
console.print(syntax)