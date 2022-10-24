import random,time, json
from kafka import KafkaConsumer



# making error1, time1,N as global variables
error1 = 0
time1 = 0
N=0


def consume_message():
        """
        Receiving messages published in Kafka topic. Along with keeping track of progress monitor.
        Using 2 global variables 
        Progress monitor is printing after every N seconds.
        """
        global error1, time1, N
        msgsend = 0
        ierror = 0
        consumer = KafkaConsumer('sms1',bootstrap_servers='localhost:9092', auto_offset_reset = 'earliest',group_id = 'groupA')
        print('starting consumer')
        curr = time.time()
        for msg in consumer:
            randerr = random.uniform(0,1)
            if randerr <= error1:
                ierror += 1
            else:
                msgsend += 1

            if int(time.time()-curr)>=N:
                print('Number send till now',msgsend)
                print('Number of messages encountered error',ierror)
                print('Average messages send till now',float(msgsend)/float(ierror+msgsend))
                ierror,msgsend = 0,0
                curr = time.time()
            print(json.loads(msg.value))
            time.sleep(time1)
                
            

if __name__=="__main__":
    with open('input.txt','r') as inputfile:
        lines = inputfile.readlines()
        lines = [line.rstrip('\n') for line in lines]
        default_num = lines[0]
        time1, error1 = int(lines[2]), float(lines[3])
        N = int(lines[4])
    consume_message()