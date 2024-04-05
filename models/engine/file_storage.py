#!/usr/bin/python3
"""
Implement serailization deserialization using json file
"""

import json


class FileStorage:
    """
    File storage class for json serialization/desirilixation
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        return all objects
        """

        return self.__objects

    def new(self, obj):
        """
        Create a new object from key
        """

        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize objects to json format
        """

        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = globals()[class_name]
                    self.__objects[key] = obj_cls(**value)
        except FileNotFoundError:
            pass
