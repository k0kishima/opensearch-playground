import asyncio
from sqlalchemy import select
from src.database import AsyncSessionLocal
from src.companies.models import Company, CompanySynonym
from opensearchpy import OpenSearch, helpers

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

INDEX_NAME = "companies"

async def fetch_companies():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Company))
        companies = result.scalars().all()

        data = []
        for company in companies:
            synonyms_result = await session.execute(
                select(CompanySynonym.synonym).where(CompanySynonym.company_id == company.id)
            )
            synonyms = [row[0] for row in synonyms_result.fetchall()]
            data.append({
                "id": company.id,
                "name": company.name,
                "description": company.description,
                "is_public": company.is_public,
                "synonym": synonyms
            })
        return data

async def index_companies():
    companies = await fetch_companies()

    actions = [
        {
            "_index": INDEX_NAME,
            "_id": company["id"],
            "_source": company
        }
        for company in companies
    ]

    helpers.bulk(client, actions)
    print(f"Indexed {len(actions)} companies.")

if __name__ == "__main__":
    asyncio.run(index_companies())
