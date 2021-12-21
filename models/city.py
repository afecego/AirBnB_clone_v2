#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel

import sqlalchemy
from sqlalchemy import Column, String

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
