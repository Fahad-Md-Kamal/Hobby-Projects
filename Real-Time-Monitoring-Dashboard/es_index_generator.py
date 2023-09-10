from elasticsearch import Elasticsearch

# Elasticsearch configuration
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, "scheme": "http"}],
)
# Define an Elasticsearch index and mapping
index_name = 'monitoring-data-topic'

# Check if the index already exists, and if not, create it with the mapping
mappings = {
    "properties": {
        "topic_group": {"type": "keyword"},
        "timestamp": {"type": "long"},
        "cpu_usage_percent": {"type": "float"},
        "memory_usage_percent": {"type": "float"}
    }
}

if es.indices.exists(index=index_name):
    es.indices.put_mapping(index=index_name, body=mappings)
    print(f"Update Index --- {index_name} --- successfully.")
else:
    es.indices.create(index=index_name, updated=mappings)
    print(f"Created Index --- {index_name} --- successfuly")
