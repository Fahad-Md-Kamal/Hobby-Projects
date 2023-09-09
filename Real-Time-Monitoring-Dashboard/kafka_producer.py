from kafka import KafkaProducer
import json
import time
import random

# Define the Kafka topic to which you want to produce data
ORDER_KAFKA_TOPIC = "monitoring-data-topic"  # Make sure this matches the topic name in your Kafka setup

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers="localhost:29092")
def produce_sample_data():
    try:
        while True:
            # Generate sample monitoring data (e.g., CPU usage and memory usage)
            data = {
                "timestamp": int(time.time()),  # Unix timestamp
                "cpu_usage_percent": random.uniform(0.0, 100.0),
                "memory_usage_percent": random.uniform(0.0, 100.0),
            }

            # Produce the data to the Kafka topic as a JSON string
            producer.send(ORDER_KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))

            print(f"Produced: {data}")

            # Sleep for a while before producing the next data point
            time.sleep(5)  # Adjust the sleep interval as needed

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C to exit the script
        print("Producer interrupted. Exiting...")

if __name__ == "__main__":
    produce_sample_data()
