#!/usr/bin/env python3

""" Importing the neccessary modules"""
from datetime import datetime
from uuid import uuid4

""" Defining the BaseModel class """
class BaseModel:
    
    """
    A constructor for the BaseModel class that
    - Assigns a new instance of the BaseModel class a unique identifier (UUID)
    - Registers the date a new instance of the BaseModel class is created and
    - Initializes updated timestamp to creation time
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    """
    A special method that returns a human-readable string representation of the object
    Format: "[<class name>] (<id>) <attributes>"
    """ 
    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    """ 
    A method that
    - updates the public instance attribute 'updated_at' with the current datetime
    """
    def save(self):
        self.updated_at = datetime.now()

    """
    A method that
    Converts the instance attributes to a dictionary and adds metadata.
    Returns a dictionary containing the instance attributes and metadata.
    """
    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)
