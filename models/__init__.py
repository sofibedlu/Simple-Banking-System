#!/usr/bin/python3
"""intialize the models package
"""

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
