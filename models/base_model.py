#!/usr/bin/python3
"""
Base Class Model
"""

from datetime import datetime, timezone
import uuid
timeFormat = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """ The BaseModel class from which future classes will be derived"""
    id = str(uuid.uuid4())
    created_at = datetime.now(tz=timezone.utc)
    updated_at = datetime.now(tz=timezone.utc)

    def __str__(self, cls):
        """ String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute ' updatd_at' with the current datetime """
        self.updated_at = datetime.now(tz=timezone.utc)

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        new = self.__dict__.copy()
        if "created_at" in new:
            new["created_at"] = new["created_at"].strftime(timeFormat)
        if "updated_at" in new:
            new["updated_at"] = new["updated_at"].strftime(timeFormat)
        new["__class__"] = self.__class__.__name__
        return new
