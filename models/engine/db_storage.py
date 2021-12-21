#!/usr/bin/python3
"""
[summary]
"""

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage():
    """connection with the database"""
    __engine = None
    __session = None

    classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

    def __init__(self):
        """
        __init__ [summary]
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.
                                            format(
                                                HBNB_MYSQL_USER,
                                                HBNB_MYSQL_PWD,
                                                HBNB_MYSQL_HOST,
                                                HBNB_MYSQL_DB
                                            ), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        NewDict = {}
        classes = DBStorage.classes
        for clss in classes:
            if clss is not None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    NewDict[key] = obj
        return NewDict

    def save(self):
        """Saves storage dictionary to file"""
        DBStorage.__session.commit()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        DBStorage.__session.add(obj)

    def delete(self, obj):
        """Deletes object from storage dictionary"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """sumary_line"""
        Base.metadata.create_all(self.__engine)
        sessFactory = sessionmaker(bind=self.__engine)
        Session = scoped_session(sessFactory)
        DBStorage.__session = Session(expire_on_commit=False)

    def close(self):
        self.__session.close()
