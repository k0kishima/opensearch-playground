from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@localhost:5432/opensearch")

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
