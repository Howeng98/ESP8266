import network

def do_connect():
    sta_if = network.WLAN(netowrk.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('H.W.','sherlock88*/')
    while not sta_if.isconnected():
        pass
    print('network config:', sta_if.ifconfig())

do_connect()

