# Rich Examples Tutorial

This tutorial will walk you through creating a collection of Python scripts that demonstrate various features of the [Rich](https://rich.readthedocs.io/) library. Each file showcases a different feature, and the main menu file lets you select and run any example. This is only an showcase what you can do with Rich. 

The Rich example project covers:
- Basic coloured text  
- Emojis and Markdown  
- Syntax highlighting  
- Tables  
- Progress bars  
- Live updates  
- Logging  
- Hierarchical trees  
- Custom layouts  
- Spinners

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Creating the Example Files](#creating-the-example-files)
   - [01_basic_colors.py](#01_basic_colorspy)
   - [02_emojis_markdown.py](#02_emojis_markdownpy)
   - [03_syntax_highlight.py](#03_syntax_highlightpy)
   - [04_tables.py](#04_tablespy)
   - [05_progress_bar.py](#05_progress_barpy)
   - [06a_live_updates_console_print.py](#06a_live_updates_console_printpy)
   - [06b_live_updates_text_object.py](#06b_live_updates_text_objectpy)
   - [07_logging.py](#07_loggingpy)
   - [08_tree.py](#08_treepy)
   - [09_layout.py](#09_layoutpy)
   - [10_spinner.py](#10_spinnerpy)
4. [Creating the Main Menu](#creating-the-main-menu)
   - [00_rich_examples.py](#00_rich_examplespy)
5. [Running the Project](#running-the-project)
6. [Customisation and Further Improvements](#customisation-and-further-improvements)

---

## Prerequisites

- **Python 3.x** installed on your system.
- **Rich Library** installed via pip:
  ```bash
  pip install rich
  ```
- A terminal emulator that supports ANSI escape codes.

---

## Project Setup

1. Create a new folder for the project, for example, `rich-examples`.
2. Inside this folder, create the following Python files:
   - `01_basic_colors.py`
   - `02_emojis_markdown.py`
   - `03_syntax_highlight.py`
   - `04_tables.py`
   - `05_progress_bar.py`
   - `06a_live_updates_console_print.py`
   - `06b_live_updates_text_object.py`
   - `07_logging.py`
   - `08_tree.py0`
   - `09_layout.py`
   - `10_spinner.py`
   - `00_rich_examples.py`

We will now code each file one by one.

---

## Creating the Example Files

### 01_basic_colors.py

This file demonstrates basic colour formatting and text styles with Rich.

```python
#!/usr/bin/env python3
from rich.console import Console

console = Console()

console.print("[bold red]This is bold red text[/bold red]")
console.print("[green]This is green text[/green]")
console.print("[underline cyan]This is underlined cyan text[/underline cyan]")
console.print("[bold italic magenta]This is bold italic magenta text[/bold italic magenta]")
console.print("[yellow on blue]Yellow text on a blue background[/yellow on blue]")
```

*Explanation:*  
A `Console` object is created from Rich. Its `print()` method uses Rich markup to display styled text.

---

### 02_emojis_markdown.py

This file shows how to render emojis and Markdown using Rich.

```python
#!/usr/bin/env python3
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

*Explanation:*  
The script prints emoji-supported text and then renders Markdown content.

---

### 03_syntax_highlight.py

This file demonstrates how to syntax-highlight JSON code.

```python
#!/usr/bin/env python3
from rich.console import Console
from rich.syntax import Syntax

console = Console()

json_data = '{"name": "Alice", "language": "Python"}'
syntax = Syntax(json_data, "json", theme="monokai", line_numbers=True)
console.print(syntax)
```

*Explanation:*  
A `Syntax` object is created with JSON data. The syntax-highlighting theme (Monokai) and line numbers are applied for clarity.

---

### 04_tables.py

This file shows how to create and display a formatted table.

```python
#!/usr/bin/env python3
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
```

*Explanation:*  
A table is constructed by creating a `Table` object, adding columns with styling options, and then adding rows of data.

---

### 05_progress_bar.py

This file displays an interactive progress bar.

```python
#!/usr/bin/env python3
import time
from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    for _ in range(100):
        time.sleep(0.05)  # Simulate work
        progress.update(task, advance=1)
```

*Explanation:*  
A progress bar is created using the `Progress` class. Work is simulated by a loop with a small delay, updating the progress each time.

---

### 06a_live_updates_console_print.py

This file provides an example of live updates using Rich’s console print method.

```python
#!/usr/bin/env python3
import time
from rich.console import Console

console = Console()

for i in range(10):
    console.print(f"[bold green]Update {i+1}/10[/bold green]", end="\r")
    time.sleep(0.5)
console.print("\nDone!")
```

*Explanation:*  
The terminal output is updated on the same line (using `\r`) to simulate live updates.

---

### 06b_live_updates_text_object.py

This file demonstrates live updates with a Rich `Text` object.

```python
#!/usr/bin/env python3
import time
from rich.console import Console
from rich.text import Text

console = Console()

for i in range(10):
    text = Text(f"Update {i+1}/10", style="bold green")
    console.print(text, end="\r")
    time.sleep(0.5)
console.print("\nDone!")
```

*Explanation:*  
This script uses the `Text` class to create a styled text object and updates it live on the same line.

---

### 07_logging.py

This file demonstrates how to use Rich for colour-coded logging.

```python
#!/usr/bin/env python3
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

*Explanation:*  
The script sets up Python’s logging with a Rich handler, ensuring that log messages are formatted colourfully in the terminal.

---


## 08_tree.py

This file demonstrates how to use the `Tree` class to display a hierarchical structure.

```python
#!/usr/bin/env python3
from rich.console import Console
from rich.tree import Tree

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

*Explanation:*  
This script builds a tree structure with a root and two child branches, each with its own grandchildren. It then prints the tree to the terminal.

---

## 09_layout.py

This file demonstrates how to create a terminal layout using the `Layout` class. It arranges several panels on the screen.

```python
#!/usr/bin/env python3
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

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

*Explanation:*  
The script defines a layout with an upper section and a lower section. The lower section is further divided into two columns, each containing its own panel.

---

## 10_spinner.py

This file demonstrates how to display a spinner using Rich’s status context manager. This is useful for showing an animated spinner while performing a task.

```python
#!/usr/bin/env python3
import time
from rich.console import Console

console = Console()

with console.status("[bold green]Processing...[/bold green]", spinner="dots"):
    # Simulate a task taking some time
    time.sleep(3)

console.print("[bold green]Done![/bold green]")
```

*Explanation:*  
This script uses `console.status()` to display a spinner with the text "Processing..." while it simulates a task by sleeping for three seconds. Once the task is complete, it prints "Done!".

---

## Creating the Main Menu

The main menu file ties all examples together. It displays a list of options and lets you choose which example to run.

### 00_rich_examples.py

```python
#!/usr/bin/env python3
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Dictionary of examples: key, title, filename, and description.
examples = {
    "1": ("Basic Colours", "01_basic_colors.py", "Demonstrates how to print coloured and styled text."),
    "2": ("Emojis and Markdown", "02_emojis_markdown.py", "Shows emoji support and Markdown rendering."),
    "3": ("Syntax Highlighting", "03_syntax_highlight.py", "Highlights JSON code with a colour theme."),
    "4": ("Tables", "04_tables.py", "Creates a formatted table with multiple columns."),
    "5": ("Progress Bar", "05_progress_bar.py", "Displays an interactive progress bar."),
    "6a": ("Live Updates (console print)", "06a_live_updates_console_print.py", "Updates terminal output live using console print."),
    "6b": ("Live Updates (Text object)", "06b_live_updates_text_object.py", "Updates terminal output live using a Text object."),
    "7": ("Rich Logging", "07_logging.py", "Demonstrates colour-coded logging with Rich."),
}

def clear_screen():
    """Clears the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")

def show_menu():
    """Displays the main menu."""
    clear_screen()
    
    console.print(Panel(
        "[bold cyan]Welcome to Rich Examples![/bold cyan] 🚀\n\n"
        "Enter the corresponding number to run an example.\n"
        "Type [bold magenta]'q'[/bold magenta] to quit.",
        title="[bold magenta]Rich Menu[/bold magenta]", expand=False))
    
    table = Table(title="Available Examples", header_style="bold magenta")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="green")
    
    for key, (title, _, _) in examples.items():
        table.add_row(f"[bold yellow]{key}[/bold yellow]", title)
    
    console.print(table)

def run_example(choice):
    """Runs the chosen script."""
    if choice in examples:
        script_title, script_filename, script_desc = examples[choice]
        
        if not os.path.exists(script_filename):
            console.print(f"[bold red]Error:[/bold red] File '{script_filename}' not found!")
            return
        
        clear_screen()
        console.print(Panel(
            f"[bold green]{script_title}[/bold green]\n\n"
            f"[italic]{script_desc}[/italic]\n\n"
            f"[bold cyan]File:[/bold cyan] {script_filename}",
            title="[bold green]Information[/bold green]", expand=False))
        
        # Run the chosen script immediately
        os.system(f"./{script_filename}")
        
        # Wait for user input before returning to the menu
        console.input("\n[bold magenta]Press Enter to return to the menu...[/bold magenta]")
    else:
        console.print("[bold red]Invalid choice![/bold red]")

def main():
    """Main function to run the menu loop."""
    while True:
        show_menu()
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", default="q").strip().lower()
        if choice == "q":
            console.print("\n[bold magenta]Exiting...[/bold magenta] 🚀\n")
            break
        run_example(choice)

if __name__ == "__main__":
    main()
```

*Explanation:*  
The main menu script clears the screen and displays a panel with a list of available examples. When the user selects an option, it clears the screen again, shows an information panel about the chosen script, and then runs that script. Finally, it waits for the user to press Enter before returning to the menu.

---

## Running the Project

1. Open your terminal and navigate to the project directory.
2. Make all the Python files executable (if needed):
   ```bash
   chmod +x 01_basic_colors.py 02_emojis_markdown.py 03_syntax_highlight.py 04_tables.py 05_progress_bar.py 06a_live_updates_console_print.py 06b_live_updates_text_object.py 07_logging.py 00_rich_examples.py
   ```
3. To run a specific example, execute its file directly, e.g.:
   ```bash
   ./01_basic_colors.py
   ```
4. To run the main menu and choose from the examples, execute:
   ```bash
   ./00_rich_examples.py
   ```

---

## Customisation and Further Improvements

- **Tweaking the Code:**  
  Feel free to adjust the Rich markup, add new examples, or modify the panel styles to suit your needs.

- **Extending the Menu:**  
  To add new examples, simply create a new Python script and add an entry to the `examples` dictionary in `00_rich_examples.py`.

- **Exploring Rich:**  
  For more features, refer to the [Rich documentation](https://rich.readthedocs.io/) and experiment with different components.

---

This concludes the full tutorial on how to build the **Rich Examples** project. Enjoy exploring the Rich library and enhancing your terminal programmes! If you have any questions or further ideas for improvement, feel free to ask. Happy coding!