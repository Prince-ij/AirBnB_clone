#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        self.deserialize(kwargs)  # Use a helper method for deserialization

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.strftime(self.DATE_FORMAT),
            "updated_at": self.updated_at.strftime(self.DATE_FORMAT),
            "__class__": self.__class__.__name__,
        }

    def deserialize(self, kwargs):
        """Deserialize key/value pairs in kwargs and set attributes."""
        for key, value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.strptime(value, self.DATE_FORMAT))
            else:
                setattr(self, key, value)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
