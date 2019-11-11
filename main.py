from machine import Pin
import machine
import time
import urequests
import network

def do_connect():
    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        print('Connecting to network...')
        sta.active(True)
        sta.connect('H.W.','sherlock88*/')

        while not sta.isconnected():
            pass
        print('Network connected!')


def get_data():        
    num = 33.1
    return {'temperature':num}


def send_data(data):
    print('Sending data...')
    res = urequests.put('https://esp8266-97db2.firebaseio.com/data.json', json=data)
    print('Response: {}'.format(res.text))
    flash_led() 

def flash_led():
    led = machine.Pin(2, machine.Pin.OUT) 
    led.value(0) 
    time.sleep(0.5)
    led.value(1)

def main():
    do_connect()

    while True:
        send_data(get_data())
        time.sleep(1)

main()
