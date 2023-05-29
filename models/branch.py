#!/usr/bin/python3
"""contains Branch class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Branch(BaseModel, Base):
    __tablename__ = 'branches'

    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    bank_id = Column(String(255), ForeignKey('banks.id'), nullable=False)
    bankers = relationship("Banker", backref="branch",
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
