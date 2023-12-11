#!/usr/bin/env python3
import uuid
from datetime import datetime


class BaseModel:
    """ Base class for other models with common
        attributes and methods """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance for BaseModel
            class """

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs):
            for k, v in kwargs.item():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, tform))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """ Returns a string representation
            of the object """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at with current datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of the
            objects attributes for serialization,
            converts created_at and updated_at
            into iso- format """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
