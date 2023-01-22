import sys, hashlib, json, random
import asyncio
import json

from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

from aiokafka import AIOKafkaProducer


from faker import Faker

app = FastAPI(title="Producer")

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "welcome_emails"


aio_producer = AIOKafkaProducer(client_id=f'{KAFKA_TOPIC}_01', bootstrap_servers=KAFKA_SERVER)

@app.on_event("startup")
async def startup_event():
    print(">>> ON_EVENT.startup")
    await aio_producer.start()    
    print("<<< ON_EVENT.startup")

@app.on_event("shutdown")
async def shutdown_event():
    print(">>> ON_EVENT.shutdown")
    await aio_producer.stop()
    print("<<< ON_EVENT.shutdown")




@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.post("/kafka_01/producer")
async def kafka_01_producer(count: int = 1000, topic_name: str = KAFKA_TOPIC):
    """Producer for Kafka messages"""

    responses = []
    fake = Faker()

    for _ in range(count):

        message_id = hashlib.sha256( str.encode(fake.ean13()) ).hexdigest()
        message = {'name': f'{fake.name()} FastAPI', 'email':f'fast_{fake.email()}', 'id': message_id}
        
        await aio_producer.send_and_wait(topic_name, json.dumps(message).encode("ascii"))

        responses.append(message)

    return JSONResponse(content=responses)

