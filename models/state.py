#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """get the cities with state_id equal"""
        rtrn = []
        for key, value in storage.all().keys():
            if key.split(".")[0] == "City":
                if value.state_id == self.id:
                    rtrn.append(value)
        return rtrn
