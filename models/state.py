#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel

import sqlalchemy
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    name = ""
