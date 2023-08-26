#!/usr/bin/python3
"""
module contains the City class that represents a city linked to a state.
"""

from sqlalchemy import Column, Integer, String, ForeignKe
from sqlalchemy.ext.declarative import declarative_basey
from relationship_state import Base


class City(Base):
    """
    base city represents a city linked to a state
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and cant be null
    class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
