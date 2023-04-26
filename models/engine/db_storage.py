#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None
    __clsname = {"State": State,
                 "City": City,
                 "User": User,
                 "Place": Place,
                 "Review": Review,
                 "Amenity": Amenity}

    def __init__(self):
        """ init engine and session with mysqldb and sqlalchemy"""
        DBStorage.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ['HBNB_MYSQL_USER'],
                os.environ['HBNB_MYSQL_PWD'],
                os.environ['HBNB_MYSQL_HOST'],
                os.environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        self.reload()
        if 'HBNB_ENV' in os.environ.keys():
            if os.environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns a dictionary"""
        my_dict = {}
        if cls is None:
            for key, cls in self.__clsname.items():
                for obj in self.__session.query(cls):
                    my_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        else:
            for obj in self.__session.query(self.__clsname.get(cls)):
                my_dict["{}.{}".format(
                            self.__clsname.get(cls).__name__, obj.id)] = obj
        return my_dict

    def new(self, obj):
        """sets a given object in database"""
        DBStorage.__session.add(obj)

    def save(self):
        """saves changes to database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """delete a given object from database"""
        if obj is not None:
            DBStorage.__session.delete(obj)

    def reload(self):
        """create all tables in the db and create current session from engine
        """
        Base.metadata.create_all(DBStorage.__engine)
        Session = sessionmaker()
        Session.configure(bind=DBStorage.__engine)
        DBStorage.__session = Session()

    def close(self):
        """remove connections on private attribute or close() on session"""
        DBStorage.__session.close()
