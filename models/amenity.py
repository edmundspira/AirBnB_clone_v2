#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy import Table, ForeignKey
from models.place import Place


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenity = Table(
                            "place_amenity", Base.metadata,
                            Column('place_id',
                                   String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True,
                                   nullable=False),
                            Column('amenity_id',
                                   String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True,
                                   nullable=False))
