#
# Run:
# python producer.py
#

import sys, hashlib, json, random
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer

from faker import Faker


if __name__ == '__main__':

    KAFKA_SERVER = "localhost:9092"
    KAFKA_TOPIC = "welcome_emails"

    fake = Faker()

    # Kafka Producer
    producer = Producer({"bootstrap.servers":KAFKA_SERVER})

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


    count = 0
    for _ in range(1000):

        message = {'name': fake.name(), 'email':fake.email(), 'id': fake.ean13()}
        message_id = hashlib.sha256( str.encode(fake.ean13()) ).hexdigest()

        # Parametros: Tópico, Mensagem, Chave da Mensagem
        producer.produce(KAFKA_TOPIC, json.dumps(message), message_id, callback=delivery_callback)
        count += 1


    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()