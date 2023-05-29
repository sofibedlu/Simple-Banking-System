#!/usr/bin/python3
"""contains Banker class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


class Banker(BaseModel, UserMixin, Base):
    __tablename__ = 'bankers'

    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    branch_id = Column(String(255), ForeignKey('branches.id'), nullable=False)
    
    def __init__(self, *args, **kwargs):
        password = kwargs['password']
        hashed_password = generate_password_hash(password)
        kwargs['password'] = hashed_password
        super().__init__(*args, **kwargs)
