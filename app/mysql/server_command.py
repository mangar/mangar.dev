import sys, hashlib, json, random
import asyncio
import json

from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

from aiokafka import AIOKafkaProducer


from faker import Faker

app = FastAPI(title="Data Requests")

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "data_requests"

aio_producer = AIOKafkaProducer(client_id=f'{KAFKA_TOPIC}_01', bootstrap_servers=KAFKA_SERVER)

@app.on_event("startup")
async def startup_event():
    print(">>> ON_EVENT.startup")
    await aio_producer.start()    
    print("<<< ON_EVENT.startup")

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.post("/data/requests/orders_by_user")
async def data_requests(user_id:str):
    
    fake = Faker()
    request_id = hashlib.sha256( str.encode(fake.ean13()) ).hexdigest()

    request_data = {
        'request_id': request_id,
        'action':'data_requests_orders_by_user',
        'params': [
            {'name':'user_id', 'value':f'{user_id}'}
            ]        
    }
            
    await aio_producer.send_and_wait(KAFKA_TOPIC, json.dumps(request_data).encode("ascii"))
    return JSONResponse(content=request_data)

