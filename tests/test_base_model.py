#!/usr/bin/python3
"""
Base Model unittest module
"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4, UUID
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    mod = BaseModel()

    def test_default_attributes(self):
        self.assertTrue(hasattr(self.mod, "id"))
        self.assertTrue(hasattr(self.mod, "created_at"))
        self.assertTrue(hasattr(self.mod, "updated_at"))

    def test_id_is_UUID(self):
        mod = UUID(self.mod.id)
        self.assertIsInstance(mod, UUID)

    def test_created_is_datetime(self):
        mod = self.mod.created_at
        self.assertIsInstance(mod, datetime)

    def test_updated_is_datetime(self):
        mod = self.mod.updated_at
        self.assertIsInstance(mod, datetime)

    def test_class_methods(self):
        self.assertIn("save", dir(self.mod))
        self.assertIn("to_dict", dir(self.mod))

    def test_str_output(self):
        mod = self.mod
        output = f"[BaseModel] ({mod.id}) {mod.__dict__}"
        self.assertEqual(str(mod), output)

    def test_save_method(self):
        original = self.mod.updated_at
        self.mod.save()
        self.assertGreater(self.mod.updated_at, original)

    def test_to_dict_method(self):
        result = self.mod.to_dict()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["created_at"],
                         self.mod.created_at.isoformat())
        self.assertEqual(result["updated_at"],
                         self.mod.updated_at.isoformat())
        self.assertEqual(result["id"], self.mod.id)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertIsInstance(result["created_at"], str)
        self.assertIsInstance(result["updated_at"], str)
        self.assertIsInstance(result["id"], str)

    def test_valid_kwargs(self):
        kwargs = {"id": str(uuid4()),
                  "created_at": datetime.now().isoformat(),
                  "__class__": "BaseModel",
                  "my_number": 89,
                  "name": "My First Model",
                  "updated_at": datetime.now().isoformat()}
        mod = BaseModel(**kwargs)
        self.assertEqual(mod.to_dict(), kwargs)


if __name__ == "__main__":
    unittest.main()
