#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity')

else:
    class Amenity(BaseModel):
        name = ""
