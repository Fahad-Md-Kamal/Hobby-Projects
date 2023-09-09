from elasticsearch import Elasticsearch
from fastapi import FastAPI


# Create a FastAPI instance
app = FastAPI()

# Elasticsearch configuration
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, "scheme": "http"}],
)


@app.get("/all-logs")
async def consume_data(index:str):
    resp = es.search(
        index = index,
        query={
            "match_all": {}
        },
        sort=[
            {
                "timestamp": {
                    "order": "desc"
                }
            }
        ]
    )
    data = [{"id": i["_id"], **i["_source"]} for i in resp.body["hits"]["hits"]]
    return {"total": resp.body["hits"]["total"]["value"], "data": data}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
