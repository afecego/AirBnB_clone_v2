#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
import uuid
from datetime import datetime

time = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, vale in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    vale = datetime.strptime(vale, time)
                if key != '__class__':
                    setattr(self, key, vale)
            now = datetime.now()
            if self.created_at is None:
                setattr(self, 'created_at', now)
            if self.updated_at is None:
                setattr(self, 'updated_at', now)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.strftime(time)
        dictionary["updated_at"] = self.updated_at.strftime(time)

        return dictionary
