#!/usr/bin/python3
"""contains Banker class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base

class Banker(BaseModel, Base):
    __tablename__ = 'bankers'

    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    branch_id = Column(String(255), ForeignKey('branches.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
