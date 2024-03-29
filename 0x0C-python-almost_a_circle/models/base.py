#!/usr/bin/python3

"""
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with
this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument
value - you can assume id is an integer and you don’t need to test the type of
it .
otherwise, increment __nb_objects and assign the new value to the public
instance attribute id
"""

import json


class Base:
    """
    Implementation as required above
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of a list of dictionaries
        """
        data = "[]"
        if list_dictionaries:
            data = json.dumps(list_dictionaries)

        return data

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        strings = []
        if list_objs is not None:
            for item in list_objs:
                strings.append(item.to_dictionary())

        data = cls.to_json_string(strings)
        with open(f"{cls.__name__}.json", "w") as jfile:
            jfile.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        jlist = []
        if json_string is not None:
            jlist = json.loads(json_string)

        return jlist
