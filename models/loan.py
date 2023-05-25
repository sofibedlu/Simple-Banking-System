#!/usr/bin/python3
"""contains Loan class"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base_model import BaseModel, Base

class Loan(BaseModel, Base):
    __tablename__ = 'loans'

    loan_number = Column(String(20), nullable=False)
    loan_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    customer_id = Column(String(255), ForeignKey('customers.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
