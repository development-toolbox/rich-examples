#!/usr/bin/env python3
import os
import ast

def load_example_info(filepath):
    """
    Reads the file and uses the AST module to check for a top-level
    assignment to `example_info`. Returns the evaluated data if found,
    or None if not.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
    try:
        tree = ast.parse(file_content, filename=filepath)
    except Exception:
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "example_info":
                    try:
                        # Safely evaluate the value
                        value = ast.literal_eval(node.value)
                        return value
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

def get_example_code(filename):
    """
    Reads the entire content of the given file and returns it as a string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    return code

def generate_readme_content(examples):
    """
    Generates the Markdown content for README-Tutorials.md using the examples' metadata.
    Automatically inserts the full Python code of each example as a code block.
    """
    md = "# Rich Examples Tutorials\n\n"
    md += "A collection of Python scripts demonstrating various features of the [Rich](https://rich.readthedocs.io/) library.\n\n"
    md += "## Available Examples\n\n"
    md += "| Option | Title | Description | File |\n"
    md += "|--------|-------|-------------|------|\n"
    for idx, info in enumerate(examples, start=1):
        md += f"| {idx} | {info['title']} | {info['description']} | `{info['filename']}` |\n"
    md += "\n"
    md += "## Tutorials\n\n"
    for idx, info in enumerate(examples, start=1):
        md += f"### {idx}. {info['title']}\n\n"
        md += f"**Description:** {info['description']}\n\n"
        md += f"**File:** `{info['filename']}`\n\n"
        md += "#### Code\n\n"
        code = get_example_code(info["filename"])
        md += "```python\n" + code + "\n```\n\n"
        md += "---\n\n"
    return md

def update_readme():
    examples = scan_examples(".")
    readme_content = generate_readme_content(examples)
    with open("README-Tutorials.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README-Tutorials.md has been updated with the latest examples.")

if __name__ == "__main__":
    update_readme()
