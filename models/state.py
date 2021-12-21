#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    if models.Storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', Backref="states")
    else:
        name = ""
