
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
