#!/usr/bin/python3
"""srcript to define a DB class"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import os


class DBStorage():
    """class to define a DB storage for the project"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """return dictioary with all objects in DB"""
        from ..state import State, Base
        from ..city import City
        from ..user import User
        from ..place import Place
        from ..review import Review
        from ..amenity import Amenity

        if cls is not None:
            dct = {}
            objects = self.__session.query(eval(cls)).all()
            for row in objects:
                key = cls + "." + row.id
                dct[key] = row
            return (dct)
        else:
            Users = self.__session.query(User).all()
            States = self.__session.query(State).all()
            Cities = self.__session.query(City).all()
            # Amenities = self.__session.query(Amenity).all()
            Reviews = self.__session.query(Review).all()
            Places = self.__session.query(Place).all()
            dct1 = {}
            for row in States:
                key = "State" + "." + row.id
                dct1[key] = row
            for row in Cities:
                key = "City" + "." + row.id
                dct1[key] = row
            for row in Users:
                key = "User" + "." + row.id
                dct1[key] = row
            for row in Reviews:
                key = "Review" + "." + row.id
                dct1[key] = row
            for row in Places:
                key = "Place" + "." + row.id
                dct1[key] = row
            return(dct1)

    def new(self, obj):
        """add a new object to DB"""
        self.__session.add(obj)

    def save(self):
        """save changes in DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from DB"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """reload all objects in DB"""
        from ..state import State, Base
        from ..city import City
        from ..user import User
        from ..place import Place
        from ..review import Review
        from ..amenity import Amenity
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        session.configure(expire_on_commit=False)
        self.__session = scoped_session(session)
