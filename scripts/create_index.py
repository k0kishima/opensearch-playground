from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

index_name = "companies"

# Delete the index if it exists (for dev use only)
if client.indices.exists(index=index_name):
    client.indices.delete(index=index_name)

# Create the index with kuromoji analyzer
client.indices.create(
    index=index_name,
    body={
        "settings": {
            "analysis": {
                "analyzer": {
                    "ja_kuromoji": {
                        "type": "custom",
                        "tokenizer": "kuromoji_tokenizer"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "name": {
                    "type": "text",
                    "analyzer": "ja_kuromoji"
                },
                "description": {
                    "type": "text",
                    "analyzer": "ja_kuromoji"
                },
                "synonym": {
                    "type": "text",
                    "analyzer": "ja_kuromoji"
                },
                "is_public": {
                    "type": "boolean"
                }
            }
        }
    }
)

print(f"Index '{index_name}' created with Kuromoji analyzer.")
