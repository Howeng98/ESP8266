import paho.mqtt.client as mqtt
import time

HOST_IP = 'localhost' 
HOST_PORT = 1883 
TOPIC_ID = 'instruction' 

client = mqtt.Client()
client.connect(HOST_IP, HOST_PORT, 60)

count = 0
while True:
    count += 1    
    message = 'Instruction,{}'.format(count)       
    client.publish(TOPIC_ID, message)    
    print('SEND: {}'.format(message))
    time.sleep(1)
