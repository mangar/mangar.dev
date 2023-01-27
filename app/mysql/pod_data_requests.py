import os, sys, time, json
import asyncio
from mysql.connector import connect, Error
from aiokafka import AIOKafkaConsumer



class DataRequests:
    """Data Requests"""
    def __init__(self, data:dict):
        self.data = data


    def factory(self):
        if self.data['action'] == 'data_requests_orders_by_user':
            return OrdersByUser(self.data).process()
        else:            
            return None



class OrdersByUser:
    """Action: Orders_by_User"""

    MY_HOST = "localhost"
    MY_USER = "root"
    MY_PWD = "pwd"
    MY_DATABASE = "py_mysql"

    def __init__(self, data:dict):
        self.data = data


    def _get_connect(self, database=MY_DATABASE):
        return connect(host=self.MY_HOST, user=self.MY_USER, password=self.MY_PWD, database=database)


    def process(self) -> list:
        res = {
            'request':self.data,
            'result':[]
        }

        connect = self._get_connect()
        cursor = connect.cursor()

        cursor.execute(f"""
        SELECT id, uuid, customer_id, date_order, payment_type, total_amount, status
        FROM orders
        WHERE customer_id = {self.data['params'][0]['value']}
        """)
        result = cursor.fetchall()

        for r in result:
            res['result'].append({
                'id':r[0],
                'uuid':r[1],
                'customer_id':r[2],
                'date_order':r[3],
                'payment_type':r[4],
                'total_amount':r[5],
                'status':r[6]
            })

        return res







KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "data_requests"
KAFKA_GROUP_ID = "app_00"


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
            mmsg = msg.value.decode("utf-8")

            print(f'Request:')
            print(f'{json.dumps( json.loads(mmsg), indent=4)}')
            print('-' * 20)

            result = DataRequests(  json.loads(mmsg) ).factory()
            print(f'Result:')
            print(f'{ json.dumps(result, indent=4, default=str) }')
            print('-' * 20)


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
    





