#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from engine.file_storage import FileStorage


storage_t = getenv("HBNB_TYPE_STORAGE")
storage = FileStorage()
storage.reload()
