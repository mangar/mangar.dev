import os
import asyncio
# ---
from fastapi import FastAPI
from starlette.responses import RedirectResponse
# ---
from aiokafka import AIOKafkaConsumer
# ---
from confluent_kafka import Consumer




app = FastAPI(title="Consumer")


KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "welcome_emails"
KAFKA_GROUP_ID = "welcome_emails_group_02"



@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.on_event("startup")
async def startup_event():
    print(f'''
    ----------------------------
    Sarting Kafka consumer
    Server: {KAFKA_SERVER}
    Topic: {KAFKA_TOPIC}
    GroupID: {KAFKA_GROUP_ID}
    Server as a service: {os.environ["SERVER_AS_CONSUMER"]}
    ----------------------------
    ''')

    if os.environ["SERVER_AS_CONSUMER"] == "1":
        consumer = AIOKafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, group_id=KAFKA_GROUP_ID)
        await consumer.start()
        try:
            async for msg in consumer:
                print(msg.value)
        finally:
            await consumer.stop()
    


@app.get("/kafka_01/consume")
def kafka_01_consume():

    consumer = Consumer({"bootstrap.servers":KAFKA_SERVER, "group.id": KAFKA_GROUP_ID})
    consumer.subscribe([KAFKA_TOPIC])

    count = 1
    try:
        while count <= 5:
            msg = consumer.poll(1.0)
            if msg is None:
                print(f"Waiting... ({count})")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                print(f">> {msg.value().decode('utf-8')}")
                count = 0

            count += 1

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()



    


