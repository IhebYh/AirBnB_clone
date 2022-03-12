#!/usr/bin/python3
"""Models to represent everything from users to cities."""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
