#!/usr/bin/python3
"""
Create a unique FileStorage Instance
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
__all__ = ["amenity", "city", "place", "state", "review", "user", "storage"]
