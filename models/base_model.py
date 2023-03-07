#!/usr/bin/python3
"""
Base Model Module Doc
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel Class Doc: Defines BaseModel Object
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel Object

        Attributes:
            id (str): Unique Instance id
            created_at (datetime): Assign datetime Values
            updated_at (datetime): Update datetime Values
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

    def __str__(self):
        """
        Returns BaseModel object string representation
        """

        name = type(self).__name__
        attrs = self.__dict__

        return f"[{name}] ({self.id}) {attrs}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary of keys/values of instance
        """

        res = {}
        res.update(self.__dict__)
        res["__class__"] = self.__class__.__name__
        res["updated_at"] = self.updated_at.isoformat()
        res["created_at"] = self.created_at.isoformat()

        return res
