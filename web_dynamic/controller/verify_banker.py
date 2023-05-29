#!/usr/bin/python3
"""verify Banker credentials"""

from models import storage
from models.banker import Banker
from werkzeug.security import check_password_hash


def verify_credentials(username, password):

    bankers = storage.all(Banker)
    
    for banker in bankers.values():
        if banker.username == username:
            hashed_password = banker.password
            if check_password_hash(hashed_password, password):
                return banker
    return None
