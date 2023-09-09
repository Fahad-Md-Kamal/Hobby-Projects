import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch


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

while True:
    kafka_messages = consumer.poll(timeout_ms=1000)

    data = []
    for _, messages in kafka_messages.items():
        for message in messages:
            res = es.index(
                index='monitoring-data-topic', 
                id=message.value["timestamp"], 
                document=message.value
            )
            print("Consumed : ", message.value, "\t", "Stored : ", res["_shards"]["successful"])
    
