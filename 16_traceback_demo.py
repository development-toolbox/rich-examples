#!/usr/bin/env python3
import rich.traceback

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
