#!/usr/bin/python3
"""File Storage Module Doc

Imports:
    json (module): Manage Serializatiin & Deserialization
"""
import json


class FileStorage:
    """FileStorage Class Doc: Serializes Instances to JSON
        and deserializes JSON to instances:

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): database objects local storage
            by {<class name>.id: obj}
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize FileStorage Instance
        """
        pass

    def all(self):
        """Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """Populates __objects in {<obj class name>.id: obj}
            format.
        """

        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """

        with open(self.__file_path, "w") as f:
            export = {}
            for key, value in self.__objects.items():
                export[key] = value.to_dict()
            json.dump(export, f)

    def reload(self):
        """Deserializes the JSON file to __objects

        Imports:
            models.base_model.BaseModel (cls): Base Class
            models.user.User (cls): User Class
            models.amenity.Amenity (cls): Amenity Class
            models.city.City (cls): City Class
            models.place.Place (cls): Place Class
            models.review.Review (cls): Reviee Class
            models.state.State (cls): State Class
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        try:
            with open(self.__file_path) as f:
                chunk = json.load(f)
                for key, value in chunk.items():
                    class_ = key.split(".")[0]
                    self.__objects[key] = eval(class_)(**value)
        except FileNotFoundError:
            pass
