#!/usr/bin/python3
"""
1-module
"""


def write_file(filename="", text=""):
    """
    writes a text file (UTF8) and prints it to stdout
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
