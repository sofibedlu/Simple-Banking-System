#!/usr/bin/python3
"""contains Customer class"""

from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Customer(BaseModel, Base):
    __tablename__ = 'customers'

    name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    street = Column(String(255), nullable=False)
    accounts = relationship("Account", backref="customer",
                            cascade="all, delete, delete-orphan")
    loans = relationship("Loan", backref="customer",
                         cascade="all, delete, delete-orphan")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
