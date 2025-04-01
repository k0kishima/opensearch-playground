from opensearchpy import OpenSearch
from src.companies.schemas import CompanyResponse

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

INDEX_NAME = "companies"

async def search_companies(keyword: str) -> list[CompanyResponse]:
    query = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["name", "description", "synonym"]
            }
        }
    }

    response = client.search(index=INDEX_NAME, body=query)

    results = []
    for hit in response["hits"]["hits"]:
        source = hit["_source"]
        results.append(CompanyResponse(**source))
    return results
