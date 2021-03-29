#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            cts = storage.all
            ltcts = []
            for objects in cts.values():
                if self.id == objects.state_id:
                    ltcts.append(objects)
            return ltcts
