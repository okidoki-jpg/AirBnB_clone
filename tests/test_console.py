#!/usr/bim/python3
import unittest
from console import HBNBCommand
import os
from io import StringIO
from contextlib import redirect_stdout
from models import __all__ as clses


class TestHBNBCommand(unittest.TestCase):

    class_ = [f"{idx[0].upper()}{idx[1:]}" for idx in clses]
    ids = []

    @classmethod
    def setUpClass(cls):
        """ setting up process """
        cls.cli = HBNBCommand()

    def tearDownClass(cls):
        """ tear down """

        del cls.cli
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        """test create command """

        # Test create command with valid arguments
        for i in self.class_:
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{i}.create()")
                self.cli.onecmd(f"create {i}")
            self.ids += [out.getvalue()]
        print(self.ids)

        # Test create command with invalid arguments
        for i in self.class_:
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{i}Invalid.create()")
                self.cli.onecmd(f"{i}Invalid .create()")
                self.cli.onecmd(f"{i}Invalid.create(")
                self.cli.onecmd(f"{i} Invalid.create(")
                self.cli.onecmd(f"create Invalid")
            out.getvalue()
        print(self.ids)

    def test_all(self):
        """test all command """

        # Test all command with valid arguments
        out = StringIO()
        with redirect_stdout(out):
            self.cli.onecmd(f"all")

        for i in self.class_:
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{i}.all()")
                self.cli.onecmd(f"all {i}")

        # Test all command with invalid arguments
        for i in self.class_:
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{i} .all()")
                self.cli.onecmd(f"invalid.all()")

    def test_count(self):
        """test count command """

        # Test count command with valid arguments
        for i in self.class_:
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{i}.count()")
                self.cli.onecmd(f"count {i}")

        # Test count command with invalid arguments
        out = StringIO()
        with redirect_stdout(out):
            self.cli.onecmd(f"invalid.count()")

    def test_show(self):
        """test show command """

        # Test show command with valid arguments
        for i in range(len(self.class_)):
            out = StringIO()
            with redirect_stdout(out):
                self.cli.onecmd(f"{self.class_[i]}.show(self.ids[i])")
                self.cli.onecmd(f"show {self.class_[i]} {self.ids[i]}")

        # Test show command with invalid arguments
        out = StringIO()
        with redirect_stdout(out):
            self.cli.onecmd(f"{self.class_[1]}.show({self.ids[1]})")

        print("***", out.getvalue())

        with redirect_stdout(out):
            self.cli.onecmd(f"show {self.class_[3]} {self.ids[3]}")
        print(out.getvalue())
