import os, sys, time
import asyncio
from aiokafka import AIOKafkaConsumer


KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "welcome_emails_p5"
KAFKA_GROUP_ID = "application_a_01"


async def consume(group:str):
    print(f'''
    ----------------------------
    Sarting Kafka consumer
    Server: {KAFKA_SERVER}
    Topic: {KAFKA_TOPIC}
    GroupID: {KAFKA_GROUP_ID}
    ----------------------------
    ''')

    count = 0

    consumer = AIOKafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, group_id=group)
    await consumer.start()
    try:
        async for msg in consumer:
            print(msg.value)
            count += 1
            print(f'>> count: {count}')
    except KeyboardInterrupt:
        print("Bye bye!")            
    finally:
        await consumer.stop()
    


if __name__ == '__main__':

    group = sys.argv[1] if len(sys.argv) > 1 else KAFKA_GROUP_ID
    print(f'>> {group}')
    asyncio.run(consume(group=group))
    





