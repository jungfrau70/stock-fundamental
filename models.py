import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///fundamental1.db"

engine = create_engine(
    SQLALCHEMY_DB_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )

Base = declarative_base()

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
