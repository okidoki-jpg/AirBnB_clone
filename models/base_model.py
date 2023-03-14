#!/usr/bin/python3
"""BaseModel Module Doc

Imports:
    uuid.uuid4 (module): Create Unique IDs
    datetime.datetime (module): Manage Time
    models.storage (module): Manage Objects Storage

Classes:
    BaseModel (cls): Project Base Class
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel Class Doc: Defines BaseModel Object
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel Object

        Attributes:
            id (str): Unique Instance id
            created_at (datetime): Assign datetime Values
            updated_at (datetime): Update datetime Values
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, str(key), value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns BaseModel object string representation
        """

        name = self.__class__.__name__
        attrs = self.__dict__

        return f"[{name}] ({self.id}) {attrs}"

    def save(self):
        """Updates the public instance attribute updated_at
        """

        self.updated_at = datetime.now()
        return storage.save()

    def to_dict(self):
        """Returns a dictionary of keys/values of instance
        """

        res = {}
        res.update(self.__dict__)
        res["__class__"] = self.__class__.__name__
        res["updated_at"] = self.updated_at.isoformat()
        res["created_at"] = self.created_at.isoformat()

        return res
