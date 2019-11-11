from umqtt.simple import MQTTClient
import time

SERVER = '192.168.2.95'
CLIENT_ID = 'ESP8266' # 客户端的ID
TOPIC = b'instruction' # TOPIC的ID

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


while True:
    client.publish(TOPIC, 'helloworld')
    time.sleep(1)
