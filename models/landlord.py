#!/usr/bin/python3
""" holds class Landlord"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Landlord(BaseModel, Base):
    """Representation of a Landlord """
    if models.storage_t == 'db':
        __tablename__ = 'landlords'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="landlord")
        reviews = relationship("Review", backref="landlord")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes Landlord"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
