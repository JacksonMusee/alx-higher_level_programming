#!/usr/bin/python3

"""
Defines the blueprint of a city object which maps to
'cities' table in the database
"""

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    Define a city object
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    state = relationship('State', back_populates='cities')
