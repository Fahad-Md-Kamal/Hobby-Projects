from elasticsearch import Elasticsearch

# Elasticsearch configuration
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, "scheme": "http"}],
)
# Define an Elasticsearch index and mapping
index_name = 'monitoring-data-index'

# Check if the index already exists, and if not, create it with the mapping
if not es.indices.exists(index=index_name):
    mappings = {
        "properties": {
            "timestamp": {"type": "date"},
            "cpu_usage_percent": {"type": "float"},
            "memory_usage_percent": {"type": "float"}
        }
    }
    es.indices.create(index=index_name, mappings=mappings)
    print(f"Created Index {index_name} successfuly")
else:
    print(f"Index \"{index_name}\" exists.")
