#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel

import sqlalchemy
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
