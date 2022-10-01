import uuid

from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from db.config import Base

class BaseTable(Base):
    __abstract__ = True
    id          = uuid.uuid4()
    created_at  = Column(DateTime, default=datetime.now)
    updated_at  = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Fundamental(BaseTable):
    __tablename__ = 'fundamental'
    ticker      = Column(String(50), primary_key=True, index=True, nullable=False)
    category    = Column(String(100), primary_key=True, nullable=False)
    date        = Column(String, primary_key=True, nullable=False)
    value       = Column(Integer, nullable=False)
