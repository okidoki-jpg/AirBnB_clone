#!/usr/bin/python3
"""Commandline
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnB Command Interpreter

    Attributes:
        cmd.Cmd (class): Base clasd
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def emptyline(self):
        """Override emptyline
        """

        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel

        Usage: create <class name>
        """

        if not line:
            print("** class name missing **")
            return

        class_ = line.split()[0].strip()
        if not issubclass(globals().get(class_, str), BaseModel):
            print("** class doesn't exist **")
        else:
            model = eval(class_ + "()")
            storage.new(model)
            storage.save()
            print(model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id

        Usage: show <class name> <id>
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_, id = args[0], args[1]
        if not issubclass(globals().get(class_, str), BaseModel):
            print("** class doesn't exist **")
            return

        key = f"{class_}.{id}"
        model = storage.all().get(key)
        if not model:
            print("** no instance found **")
            return

        print(model)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_, id = args[0], args[1]
        if not issubclass(globals().get(class_, str), BaseModel):
            print("** class doesn't exist **")
            return

        key = f"{class_}.{id}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Usage: all <clasd name> | all
        """

        if not line:
            models = storage.all().values()
            print([str(mod) for mod in models])
        else:
            class_ = line.split()[0]
            if not issubclass(globals().get(class_, str), BaseModel):
                print("** class doesn't exist **")
                return
            models = storage.all().values()
            print([str(mod) for mod in models if type(mod).__name__ == class_])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        class_ = args[0]
        if not issubclass(globals().get(class_, str), BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        id = args[1]
        key = f"{class_}.{id}"
        model = storage.all().get(key)
        if not model:
            print("** no instance found **")
            return

        attr = args[2]
        if attr in ["id", "created_at", "updated_at"]:
            print("** attribute name forbidden **")
            return

        value = args[3].strip('"')
        if value.isdigit():
            value = int(value)
        elif value.isnumeric():
            value = float(value)

        setattr(model, attr, value)
        model.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
