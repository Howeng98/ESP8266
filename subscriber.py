from umqtt.simple import MQTTClient
import time

SERVER = '192.168.2.95'
CLIENT_ID = 'ESP8266'
TOPIC = b'instruction'

def mqtt_callback(topic,msg):
    print('topic: {}'.format(topic))
    print('message: {}'.format(msg))

client = MQTTClient(CLIENT_ID,SERVER)
client.set_callback(mqtt_callback)
client.connect()
client.subscribe(TOPIC)

while True:
    client.check_msg()
    time.sleep(1)
