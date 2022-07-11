## Author: Adin De'Rosier adin.derosier@oit.edu
## In accordance with the requirements listed in the project documentation
## Please refer to LICENSE before modifying any code
## System Utils V1.0

import network

def wlan_connect(ssid, passkey):

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, passkey)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
# end __wlan_connect