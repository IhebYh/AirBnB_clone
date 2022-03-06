#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Representation of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
