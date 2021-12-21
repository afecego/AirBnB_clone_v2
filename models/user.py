#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel

import sqlalchemy
from sqlalchemy import Column, String

class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__()
