#!/usr/bin/python3
"""
Module containing BaseModel Class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model for other classes to inherit their
    atrributes/methods from
    """

    def __init__(self):
        """
        Initialize base model attributes
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of baseModel
        """

        return "[{}] ({}) {}".format(self.__class__.__name, self.id,
                                     self.__dict__)

    def save(self):
        """
        Update updated_at atrribite with cutrent datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of BaseModel object
        """

        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
