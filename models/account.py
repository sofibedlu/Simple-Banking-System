#!/usr/bin/python3
"""contains Account class"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base_model import BaseModel, Base

class Account(BaseModel, Base):
    __tablename__ = 'accounts'

    account_number = Column(String(20), nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    customer_id = Column(String(255), ForeignKey('customers.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
