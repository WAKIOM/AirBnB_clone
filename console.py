#!/usr/bin/python3
"""module defines and creates a console"""
import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """emptyline"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: $ create BaseModel
        If the class name is missing, print ** class name missing **
        (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ create MyModel)
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string repr of an instance based on class name and id
        Usage: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all():
        """
        Prints all string representation of all instances based or
        not on the class name
        Usage: $ all BaseModel or $ all
        """
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] in storage.valid_classes():
            print([str(obj) for key, obj in all_objs.items()
                  if args[0] == key.split('.')[0]])
        else:
            print("** class doesn't exist **")

    def do_update():
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = all_objs[key]
        try:
            setattr(instance, attribute_name, eval(attribute_value))
        except ValueError:
            print("** invalid attribute value **")
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
