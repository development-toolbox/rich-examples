#!/usr/bin/env python3
import os
import ast

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

def get_example_code(filename):
    """
    Reads the entire content of the given file and returns it as a string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    return code

def remove_metadata_block(code):
    """
    Removes the metadata block (i.e. the top part of the file containing the
    `example_info` assignment) from the code, but preserves the shebang line if present.
    Assumes the metadata block starts after the shebang line (if it exists) and ends at the first blank line.
    """
    lines = code.splitlines()
    new_lines = []
    
    # If the first line is a shebang, preserve it.
    if lines and lines[0].startswith("#!"):
        new_lines.append(lines[0])
        lines = lines[1:]
    
    in_metadata = True
    for line in lines:
        # Once we hit a blank line, metadata is over.
        if in_metadata and line.strip() == "":
            in_metadata = False
            new_lines.append(line)  # Optionally, include the blank line.
            continue
        if not in_metadata:
            new_lines.append(line)
    return "\n".join(new_lines)

def generate_readme_content(examples):
    """
    Generates the Markdown content for README-Tutorials.md using the examples' metadata.
    Automatically inserts the full Python code (without metadata) of each example as a code block,
    and includes the explanation text if provided.
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
        if "explanation" in info:
            md += f"**Explanation:** {info['explanation']}\n\n"
        md += f"**File:** `{info['filename']}`\n\n"
        md += "#### Code\n\n"
        code = get_example_code(info["filename"])
        code_without_metadata = remove_metadata_block(code)
        md += "```python\n" + code_without_metadata + "\n```\n\n"
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
