from elasticsearch import Elasticsearch, ConnectionError
from app.config import settings

es = Elasticsearch(settings.ELASTICSEARCH_URL)

def search_in_elasticsearch(query: str, size: int = 10):
    try:
        response = es.search(
            index="your-index",
            body={"query": {"match": {"content": query}}},
            size=size,
        )
        return response["hits"]["hits"]
    except ConnectionError:
        raise Exception("Failed to connect to Elasticsearch")
