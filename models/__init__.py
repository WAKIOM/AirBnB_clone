#!/usr/bin/python3
""" create storage object"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
