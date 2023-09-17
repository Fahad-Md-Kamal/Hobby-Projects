import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import asyncio

es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, "scheme": "http"}],
)

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


async def consume():

    while True:
        kafka_messages = consumer.poll(timeout_ms=1000)

        for _, messages in kafka_messages.items():
            for message in messages:
                res = es.index(
                    index=message.value["topic_group"], 
                    id=message.value["timestamp"], 
                    document=message.value
                )
                print("Consumed: ", message.value, end="\t")
                print("Stored : ", res["_shards"]["successful"])

def main():
    asyncio.run(consume())


if __name__ == "__main__":
    main()
