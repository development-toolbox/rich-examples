# Rich Examples Tutorials

A collection of Python scripts demonstrating various features of the [Rich](https://rich.readthedocs.io/) library.

## Available Examples

| Option | Title | Description | File |
|--------|-------|-------------|------|
| 1 | Basic Colours | Demonstrates basic colour formatting and text styles with Rich. | `01_basic_colors.py` |
| 2 | Emojis and Markdown | Shows emoji support and Markdown rendering. | `02_emojis_markdown.py` |
| 3 | Syntax Highlighting | Highlights JSON code with a colour theme. | `03_syntax_highlight.py` |
| 4 | Tables | Creates a formatted table with multiple columns. | `04_tables.py` |
| 5 | Progress Bar | Displays an interactive progress bar. | `05_progress_bar.py` |
| 6 | Rich Live Updates | Displays live updates using the console.print function. | `06a_live_updates_console_print.py` |
| 7 | Rich Live Updates | Displays live updates using the Text object. | `06b_live_updates_text_object.py` |
| 8 | Rich Logging | Demonstrates colour-coded logging with Rich. | `07_logging.py` |
| 9 | Tree | Creates a tree structure using the Tree class. | `08_tree.py` |
| 10 | Layout | Creates a layout with multiple panels. | `09_layout.py` |
| 11 | Spinner | Displays a spinner while a task is being processed. | `10_spinner.py` |
| 12 | Layout Demo | Creates a layout with a header and a body. | `11_layout_demo.py` |
| 13 | Font Demo | Demonstrates different pyfiglet fonts. | `12_font_demo.py` |
| 14 | Font Demo | Demonstrates different fonts. | `13_font_demo.py` |
| 15 | Live Updating Table | Demonstrates a live-updating table that refreshes its data every second. | `14_live_table.py` |
| 16 | Custom Theme Demo | Demonstrates how to use a custom Rich theme to style output. | `15_custom_theme.py` |
| 17 | Rich Traceback Demo | Demonstrates enhanced traceback formatting with Rich. | `16_traceback_demo.py` |

## Tutorials

### 1. Basic Colours

**Description:** Demonstrates basic colour formatting and text styles with Rich.

**File:** `01_basic_colors.py`

#### Code

```python
#!/usr/bin/env python3

# Metadata for dynamic menu
example_info = {
    "title": "Basic Colours",
    "filename": "01_basic_colors.py",
    "description": "Demonstrates basic colour formatting and text styles with Rich.",
    "tutorial": """### 01_basic_colors.py

This file demonstrates basic colour formatting and text styles with Rich.


*Explanation:*  
A `Console` object is created from Rich. Its `print()` method uses Rich markup to display styled text.
"""
}
from rich.console import Console

console = Console()

console.print("[bold red]This is bold red text[/bold red]")
console.print("[green]This is green text[/green]")
console.print("[underline cyan]This is underlined cyan text[/underline cyan]")
console.print("[bold italic magenta]This is bold italic magenta text[/bold italic magenta]")
console.print("[yellow on blue]Yellow text on a blue background[/yellow on blue]")
```

---

### 2. Emojis and Markdown

**Description:** Shows emoji support and Markdown rendering.

**File:** `02_emojis_markdown.py`

#### Code

```python
#!/usr/bin/env python3

**Description:** Shows emoji support and Markdown rendering.    
        """
}
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Displaying emojis and styled text
console.print(":rocket: [bold cyan]Rich is brilliant![/bold cyan] :smile:")

# Rendering Markdown
md_content = """
# Markdown Title

**Bold text**

- Item 1
- Item 2
"""
md = Markdown(md_content)
console.print(md)
```

---

### 3. Syntax Highlighting

**Description:** Highlights JSON code with a colour theme.

**File:** `03_syntax_highlight.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

json_data = '{"name": "Alice", "language": "Python"}'
syntax = Syntax(json_data, "json", theme="monokai", line_numbers=True)
console.print(syntax)
```

---

### 4. Tables

**Description:** Creates a formatted table with multiple columns.

**File:** `04_tables.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

table = Table(title="Favourite Tools")

table.add_column("Tool", justify="left", style="cyan", no_wrap=True)
table.add_column("Category", style="magenta")
table.add_column("Rating", justify="right", style="green")

table.add_row("Rich", "Terminal Output", "5/5")
table.add_row("Click", "CLI Tool", "4/5")
table.add_row("MyPy", "Static Typing", "4.5/5")

console.print(table)
```

---

### 5. Progress Bar

**Description:** Displays an interactive progress bar.

**File:** `05_progress_bar.py`

#### Code

```python
#!/usr/bin/env python3

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    for _ in range(100):
        time.sleep(0.05)  # Simulate work
        progress.update(task, advance=1)
```

---

### 6. Rich Live Updates

**Description:** Displays live updates using the console.print function.

**File:** `06a_live_updates_console_print.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

for i in range(10):
    console.print(f"[bold green]Update {i+1}/10[/bold green]", end="\r")
    time.sleep(0.5)
console.print("\nDone!")
```

---

### 7. Rich Live Updates

**Description:** Displays live updates using the Text object.

**File:** `06b_live_updates_text_object.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

for i in range(10):
    text = Text(f"Update {i+1}/10", style="bold green")
    console.print(text, end="\r")
    time.sleep(0.5)
console.print("\nDone!")
```

---

### 8. Rich Logging

**Description:** Demonstrates colour-coded logging with Rich.

**File:** `07_logging.py`

#### Code

```python
#!/usr/bin/env python3

# 07_logging.py
example_info = {
    "title": "Rich Logging",
    "filename": "07_logging.py",
    "description": "Demonstrates colour-coded logging with Rich."
}

from rich.logging import RichHandler
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler()]
)

log = logging.getLogger("rich")

log.info("This is an info message")
log.warning("This is a warning")
log.error("This is an error")
```

---

### 9. Tree

**Description:** Creates a tree structure using the Tree class.

**File:** `08_tree.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

# Create a root node
tree = Tree("Root")

# Add child nodes
child1 = tree.add("Child 1")
child1.add("Grandchild 1.1")
child1.add("Grandchild 1.2")

child2 = tree.add("Child 2")
child2.add("Grandchild 2.1")
child2.add("Grandchild 2.2")

console.print(tree)
```

---

### 10. Layout

**Description:** Creates a layout with multiple panels.

**File:** `09_layout.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

# Create the main layout
layout = Layout()
layout.split(
    Layout(name="upper", size=3),
    Layout(name="lower")
)

# Update the upper panel
layout["upper"].update(Panel("This is the upper panel", title="Upper"))

# Split the lower layout into two columns
layout["lower"].split_row(
    Layout(Panel("Left lower panel", title="Left")),
    Layout(Panel("Right lower panel", title="Right"))
)

console.print(layout)
```

---

### 11. Spinner

**Description:** Displays a spinner while a task is being processed.

**File:** `10_spinner.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

with console.status("[bold green]Processing...[/bold green]", spinner="dots"):
    # Simulate a task taking some time
    time.sleep(3)

console.print("[bold green]Done![/bold green]")
```

---

### 12. Layout Demo

**Description:** Creates a layout with a header and a body.

**File:** `11_layout_demo.py`

#### Code

```python
#!/usr/bin/env python3

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

```

---

### 13. Font Demo

**Description:** Demonstrates different pyfiglet fonts.

**File:** `12_font_demo.py`

#### Code

```python
#!/usr/bin/env python3

console = Console()

# List of cool pyfiglet fonts to demo
fonts = ["slant", "3-d", "banner3-D", "digital"]

for font in fonts:
    ascii_art = pyfiglet.figlet_format("Rich", font=font)
    panel = Panel(ascii_art, title=f"[bold]{font}[/bold]", border_style="blue", expand=False)
    console.print(panel)

```

---

### 14. Font Demo

**Description:** Demonstrates different fonts.

**File:** `13_font_demo.py`

#### Code

```python
#!/usr/bin/env python3

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

```

---

### 15. Live Updating Table

**Description:** Demonstrates a live-updating table that refreshes its data every second.

**File:** `14_live_table.py`

#### Code

```python
#!/usr/bin/env python3

# Metadata for dynamic menu
example_info = {
    "title": "Live Updating Table",
    "filename": "14_live_table.py",
    "description": "Demonstrates a live-updating table that refreshes its data every second."
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
```

---

### 16. Custom Theme Demo

**Description:** Demonstrates how to use a custom Rich theme to style output.

**File:** `15_custom_theme.py`

#### Code

```python
#!/usr/bin/env python3

# Metadata for dynamic menu
example_info = {
    "title": "Custom Theme Demo",
    "filename": "15_custom_theme.py",
    "description": "Demonstrates how to use a custom Rich theme to style output."
}

# Define a custom theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

console = Console(theme=custom_theme)

console.print(Panel("This is an info message", style="info", title="Info"))
console.print(Panel("This is a warning message", style="warning", title="Warning"))
console.print(Panel("This is a danger message", style="danger", title="Danger"))
```

---

### 17. Rich Traceback Demo

**Description:** Demonstrates enhanced traceback formatting with Rich.

**File:** `16_traceback_demo.py`

#### Code

```python
#!/usr/bin/env python3

# Metadata for dynamic menu
example_info = {
    "title": "Rich Traceback Demo",
    "filename": "16_traceback_demo.py",
    "description": "Demonstrates enhanced traceback formatting with Rich."
}

# Install the Rich traceback handler
rich.traceback.install(show_locals=True)

def problematic_function():
    a = 1
    b = 0
    return a / b

# This will raise an exception and show a pretty traceback
problematic_function()
```

---

