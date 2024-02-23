#!/usr/bin/python3
"""Base Module"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True)
    name = Column(String(128), nullable=False)
