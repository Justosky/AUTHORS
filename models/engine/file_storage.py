#!/usr/bin/env python3

"""
Importing the neccessary modules
"""
import json
import os

"""
Defining FileStorage class
"""


class FileStorage:
    """
    Class private attributes
    """
    __file_path = 'file.json'
    __objects = {}

    """
    A method of the class that
    - Returns __objects which is a private dictionary that
        * Stores class instances with their class name and ID
    """
    def all(self):
        return (self.__objects)
    """

    """
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    """
    A method that
    - That serializes __objects private dictionary and
    - Stores it in a JSON file __file_path
    """
    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    """
    """
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
