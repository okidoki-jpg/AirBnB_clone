#!/usr/bin/python3
""" testing amenity """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAT(unittest.TestCase):
	""" testing class """

	@classmethod
	def setUpClass(cls):
		""" setting up process """
		cls.amenity = Amenity()
		cls.amenity.name = "test"

	@classmethod
	def tearDownClass(cls):
		""" tear down """
		del cls.amenity


	def test_inheritance(self):
		""" testing for the inheritance """

		self.assertTrue(isinstance(self.amenity, BaseModel))
		self.assertTrue(hasattr(self.amenity, "id"))
		self.assertTrue(hasattr(self.amenity, "created_at"))
		self.assertTrue(hasattr(self.amenity, "updated_at"))


	def test_attrs(self):
		""" test for the attr or variables """
		self.assertTrue(hasattr(self.amenity, "name"))


if __name__ == "__main__":
	unittest.main()
