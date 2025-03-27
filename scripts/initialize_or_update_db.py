import asyncio
from src.database import engine
from src.companies.models import Base

async def initialize_or_update_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(initialize_or_update_db())
