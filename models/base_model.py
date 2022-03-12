#!/usr/bin/python3
"""
Base Class Model
"""

from datetime import datetime, timezone
from . import storage
import uuid
timeFormat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ The BaseModel class from which future classes will be derived"""
    id = str(uuid.uuid4())
    created_at = datetime.now(tz=timezone.utc)
    updated_at = datetime.now(tz=timezone.utc)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    timeFormat)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    timeFormat)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self, cls):
        """ String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute ' updatd_at' with the current datetime """
        self.updated_at = datetime.now(tz=timezone.utc)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        new = self.__dict__.copy()
        if "created_at" in new:
            new["created_at"] = new["created_at"].strftime(timeFormat)
        if "updated_at" in new:
            new["updated_at"] = new["updated_at"].strftime(timeFormat)
        new["__class__"] = self.__class__.__name__
        return new
