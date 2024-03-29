#!/usr/bin/python3

"""
Write a function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object:

Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string,
integer and boolean
You are not allowed to import any module
"""


def class_to_json(obj):
    """
    Implementaton of the requirements outlined above
    """

    data = {}

    for key, value in obj.__dict__.items():
        data[key] = value

    return (data)
