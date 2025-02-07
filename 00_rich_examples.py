#!/usr/bin/env python3
import os
import ast
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def load_example_info(filepath):
    """
    Reads the file and uses the AST module to check for a top-level
    assignment to `example_info`. Returns the evaluated data if found,
    or None if not.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
        tree = ast.parse(file_content, filename=filepath)
    except Exception:
        return None

    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "example_info"
            for target in node.targets
        ):
            try:
                return ast.literal_eval(node.value)
            except Exception:
                return None
    return None

def scan_examples(directory="."):
    """
    Scans the specified directory for Python files whose names start with a digit
    (excluding the main menu file) and checks if they contain `example_info`.
    Returns a sorted list of metadata dictionaries.
    """
    examples = []
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename[0].isdigit() and filename != "00_rich_examples.py":
            info = load_example_info(filename)
            if info:
                examples.append(info)
    # Sort the examples by filename for a consistent order.
    examples.sort(key=lambda x: x["filename"])
    return examples

def show_menu(examples):
    """
    Displays a numbered menu using the loaded metadata.
    """
    console.clear()
    console.print(Panel(
        "[bold cyan]Welcome to Rich Examples![/bold cyan] 🚀\n\n"
        "Enter the number corresponding to the example to run.\n"
        "Type [bold magenta]'q'[/bold magenta] to quit.",
        title="[bold magenta]Rich Menu[/bold magenta]", expand=False))
    
    table = Table(title="Available Examples", header_style="bold magenta")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="green")
    table.add_column("Description", style="yellow")
    
    for idx, info in enumerate(examples, start=1):
        table.add_row(f"[bold yellow]{idx}[/bold yellow]", info["title"], info["description"])
    
    console.print(table)

def run_example(example_filename):
    """
    Runs the chosen example file.
    """
    os.system(f"./{example_filename}")

def main():
    examples = scan_examples(".")
    while True:
        show_menu(examples)
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]", default="q").strip().lower()
        if choice == "q":
            console.print("\n[bold magenta]Exiting...[/bold magenta] 🚀\n")
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(examples):
                example = examples[index]
                console.clear()
                console.print(Panel(
                    f"[bold green]{example['title']}[/bold green]\n\n"
                    f"[italic]{example['description']}[/italic]\n\n"
                    f"[bold cyan]File:[/bold cyan] {example['filename']}",
                    title="[bold green]Information[/bold green]", expand=False))
                # Immediately run the example without waiting for an extra prompt.
                run_example(example["filename"])
                # Wait after running to allow the user to return to the menu.
                Prompt.ask("\n[bold magenta]Press Enter to return to the menu...[/bold magenta]")
            else:
                console.print("[bold red]Invalid choice![/bold red]")
        except ValueError:
            console.print("[bold red]Invalid input! Please enter a number.[/bold red]")

if __name__ == "__main__":
    main()
