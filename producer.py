from kafka import KafkaProducer
import time,json
from data import getdata

# creating an instance of producer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_message(num):
    """
    To send messages to a topic in Kafka
    @param num - Total number of messages to be send
    """
    for i in range(num):
        gen_message = getdata()
        producer.send('sms1',gen_message)
        print(gen_message)
        time.sleep(2)


if __name__=="__main__":
    with open('input.txt','r') as inputfile:
        line = inputfile.readlines()
        default_num = int(line[0])
    send_message(default_num)