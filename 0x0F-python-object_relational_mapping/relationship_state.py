#!/usr/bin/python3
"""State Module
    Imporved by defining the relationship between State and City classes"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
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

    cities = relationship(
        "City", cascade="all, delete", back_populates="state")
