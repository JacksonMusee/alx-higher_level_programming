#!/usr/bin/python3

"""
Lessson 1 of ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    This class maps to the states tables in the database
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(124), nullable=False)
