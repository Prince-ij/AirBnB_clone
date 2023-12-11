#!/usr/bin/env python3
import json
import os

class FileStorage:
    """ handles serialization and deserialization
        to and from a json file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
            <obj classname>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes Objects to the json file 
            (path: __file_path) """

        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict()
                        for k, v in self.__objects.items()}, file)

    def reload(self):
        """ Deserializes the json file to __objects 
            {only if the file exists )"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
