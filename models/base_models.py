#!/usr/bin/env python3

""" Importing the neccessary modules"""
from uuid import uuid4
from datetime import datetime

""" Defining the BaseModel class """

class BaseModel:
    def __init__(self, created_at, updated_at):
        """ Converts the string values of "created_at" and "updated_at" to datetime objects """
        self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

        """ Create a new instance with id and current datetime """
 def __init__(self, **kwargs):
        if 'created_at' in kwargs and 'updated_at' in kwargs:
            """ Converts the string values of "created_at" and "updated_at" to datetime objects """
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%d %H:%M:%S")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%d %H:%M:%S")
        else:
            """ Generates a new UUID and assigns it to the id attribute of the instance """
            self.id = str(uuid.uuid4())

            """ Sets the created_at and updated_at attributes to the current datetime """
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        
    """ Convert instance attributes to dictionary representation """
    def to_dict(self):
        attribute_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                attribute_dict[key] = value.strftime("%Y-%m-%d %H:%M:%S")
            else:
                attribute_dict[key] = value
        return attribute_dict
