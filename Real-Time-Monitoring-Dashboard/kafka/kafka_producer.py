from kafka import KafkaProducer
import json
import time
import random

ORDER_KAFKA_TOPIC = "monitoring-data-topic"  # Make sure this matches the topic name in your Kafka setup

producer = KafkaProducer(bootstrap_servers="localhost:29092")
def produce_sample_data(topic:str="os-usage"):
    try:
        while True:
            data = {
                "topic_group": topic,
                "timestamp": int(time.time()),  # Unix timestamp
                "cpu_usage_percent": random.uniform(0.0, 100.0),
                "memory_usage_percent": random.uniform(0.0, 100.0),
            }

            producer.send(ORDER_KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))

            print(f"Produced: {data}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Producer interrupted. Exiting...")

if __name__ == "__main__":
    produce_sample_data()
