#!/usr/bin/python3
"""contains Bank class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Bank(BaseModel, Base):
    __tablename__ = 'banks'

    name = Column(String(255), nullable=False)
    code = Column(String(10), nullable=False)
    address = Column(String(255), nullable=False)
    branches = relationship("Branch", backref="bank")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
