#!/usr/bin/python3
"""Banker authentication setup"""

from flask_login import LoginManager
from models.banker import Banker
from models import storage

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return storage.get(Banker, user_id)
