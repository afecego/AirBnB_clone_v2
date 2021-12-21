#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel

import sqlalchemy
from sqlalchemy import Column, String

class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

