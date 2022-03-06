#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)