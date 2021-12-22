#!/usr/bin/python3
""" State Module for HBNB project """
"""This is the state class"""
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', backref='state', cascade='delete')
    else:
        @property
        def cities(self):
            cities = models.storage.all(City)
            return {instans for instans in cities.values()
                    if self.id == instans.state_id}
