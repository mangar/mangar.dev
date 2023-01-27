import os, sys
# import asyncio
# import time

# from confluent_kafka import Consumer


# KAFKA_SERVER = "localhost:9092"
# KAFKA_TOPIC = "welcome_emails_p5"
# KAFKA_GROUP_ID = "application_01"


# def consume(group:str):

#     consumer = Consumer({"bootstrap.servers":KAFKA_SERVER, "group.id": group})
#     consumer.subscribe([KAFKA_TOPIC])

#     count = 0
#     try:
#         # while count <= 5:
#         while True:
#             msg = consumer.poll(1.0)
#             if msg is None:
#                 print(f"Waiting... ({count})")
#                 count = 0
#             elif msg.error():
#                 print("ERROR: %s".format(msg.error()))
#             else:
#                 print(f">>[{count}] {msg.value().decode('utf-8')}")
                
#                 consumer.commit()

#                 # time.sleep(0.5)

#             count += 1

#     except KeyboardInterrupt:
#         pass
#     finally:
#         consumer.close()



if __name__ == '__main__':

    print('>> Send Email...')

    # group = sys.argv[1] if len(sys.argv) > 1 else KAFKA_GROUP_ID
    # print(f'>> {group}')
    # consume(group)
    


