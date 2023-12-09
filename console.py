#!/usr/bin/python3
"""module defines and creates a console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_EOF(self, arg):
        """Exit the program"""
        sys.exit(0)

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
        pass

    def do_show(self, arg):
        """
        Prints the string repr of an instance based on class name and id
        Usage: $ show BaseModel 1234-1234-1234
        """
        pass

    def do_destroy():
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
         Usage: $ destroy BaseModel 1234-1234-1234
        """
        pass

    def do_all():
        """
        Prints all string representation of all instances based or
        not on the class name
        Usage: $ all BaseModel or $ all
        """
        pass

    def do_update():
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
