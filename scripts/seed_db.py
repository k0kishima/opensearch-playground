import asyncio
from src.database import AsyncSessionLocal
from src.companies.models import Company, CompanySynonym
from sqlalchemy import text

async def seed_db():
    async with AsyncSessionLocal() as session:
        await session.execute(text("DELETE FROM company_synonyms"))
        await session.execute(text("DELETE FROM companies"))

        companies = [
            {
                "name": "未来ロボティクス",
                "description": "AIをベースにした先進的なロボットを開発する会社です。",
                "is_public": True,
                "synonyms": ["Future Robotics", "Mirai Robotics", "MRX"]
            },
            {
                "name": "日本ソーラー",
                "description": "太陽光を活用したソリューションやインフラ整備などを主な事業としている会社です。",
                "is_public": True,
                "synonyms": ["Nippon Solar", "Japan Solar", "JS"]
            },
        ]

        for c in companies:
            company = Company(
                name=c["name"],
                description=c["description"],
                is_public=c["is_public"],
            )
            session.add(company)
            await session.flush()

            for synonym_text in c["synonyms"]:
                synonym = CompanySynonym(synonym=synonym_text, company_id=company.id)
                session.add(synonym)

        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed_db())
