#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
