import json
from elasticsearch import Elasticsearch
from fastapi import FastAPI
from kafka import KafkaConsumer

app = FastAPI()

es = Elasticsearch([{'host': 'localhost', 'port': 9200, "scheme": "http"}])

kafka_consumer_conf = {
    'bootstrap_servers': 'localhost:29092',
    'group_id': 'my-consumer-group',
    'auto_offset_reset': 'earliest',
}

consumer = KafkaConsumer(
    'monitoring-data-topic',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    **kafka_consumer_conf
)


@app.get("/es-data")
async def consume_data(index:str = "monitoring-data-topic", page: int = 1, page_size: int = 10):
    from_index = (page - 1) * page_size

    resp = es.search(index = index,
                    query={"match_all": {}},
                    sort=[{"timestamp": {"order": "asc"}}],
                    from_= from_index, size=page_size)
    data = [{"id": i["_id"], **i["_source"]} for i in resp.body["hits"]["hits"]]
    total_hits = resp.body["hits"]["total"]["value"]
    total_pages = -(-total_hits // page_size)
    next_page = page+1 if total_pages > page else None
    prev_page = page-1 if page > 1 else None
    return {
        "total": total_hits, 
        "pages": total_pages, 
        "next_page": next_page, 
        "prev_page": prev_page,  
        "data": data}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
