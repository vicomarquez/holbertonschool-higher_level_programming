#!/usr/bin/python3
"""
7-module
"""


import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []

try:
    new_list = load_from_json_file("add_item.json")
except Exception:
    new_list = []

new_list = new_list + argv[1:]
save_to_json_file(new_list, "add_item.json")
