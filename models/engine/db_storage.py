#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import os

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                                      (os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)


    def all(self, cls=None):
        from ..state import State, Base
        from ..city import City
        from ..user import User

        if cls != None:
            #self.__session = Session(self.__engine)
            dct = {}
            objects = self.__session.query(eval(cls)).all()
            for row in objects:
                key = cls + "." + row.id
                dct[key] = row
            return (dct)
        else:
            #Users = self.__session.query(User).all()
            States = self.__session.query(State).all()
            Cities = self.__session.query(City).all()
            #Amenities = self.__session.query(Amenity).all()
            #Reviews = self.__session.query(Review).all()
            #Places = self.__session.query(Place).all()
            dct1 = {}
            for row in States:
                key = "State" + "." + row.id
                dct1[key] = row
            for row in Cities:
                key = "City" + "." + row.id
                dct1[key] = row
            return(dct1)

    def new(self, obj):
        #self.__session = Session(self.__engine)
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        from ..state import State, Base
        from ..city import City
        from ..user import User
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        session.configure(expire_on_commit=False)
        self.__session = scoped_session(session)