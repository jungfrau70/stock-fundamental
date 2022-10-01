from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLALCHEMY_DB_URL = "sqlite:///fundamental1.db"
SQLALCHEMY_DB_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DB_URL,
    future=True,
    echo=True
    )

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
    )

Base = declarative_base()