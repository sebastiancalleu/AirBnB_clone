#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.state import State
from models.place import Place
import os


class Amenity(BaseModel, Base):
    '''class to define a amenity'''
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=Place.place_amenity)
    else:
        name = ""