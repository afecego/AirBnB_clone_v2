#!/usr/bin/python3
""" State Module for HBNB project
This is the state class
holds class State"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
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
            """
            this funtion add the city in the list
            """
            cities_list = []
            cities = models.storage.all(City).values()
            for city in cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
