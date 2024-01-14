#!/usr/bin/python3

"""
Write a script that adds all arguments to a Python list, and then save them to
a file:

You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    Implementation of the requirements described above in modul's doc
    """
    my_list = []

    with open("add_item.json", "r") as my_file:
        content = my_file.read()

    if content:
        my_list = load_from_json_file("add_item.json")

    my_list += sys.argv[1:]
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_items()
