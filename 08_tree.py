#!/usr/bin/env python3
# 08_tree.py
example_info = {
    "title": "Tree",
    "filename": "08_tree.py",
    "description": "Creates a tree structure using the Tree class.",
    "explanation": "This script demonstrates how to use the Tree class to display a hierarchical structure."
}
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
