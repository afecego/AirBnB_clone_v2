#!/usr/bin/python3
""" State Module for HBNB project
This is the state class
holds class State"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            """Get a list of all linked Amenity.
            """

            cities_List = []

            for cities, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    cities_List.append(cities)
            return cities_List
