## Author: Adin De'Rosier adin.derosier@oit.edu
## In accordance with the requirements listed in the project documentation
## Please refer to LICENSE before modifying any code
## System Utils V1.0

import senko
import network
import machine

def wlan_connect(ssid, passkey):
    """
    It connects the device to a given wireless network
    
    :param ssid: The name of the WiFi network you want to connect to
    :param passkey: The password for the WiFi network
    """
    
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, passkey)
        while not sta_if.isconnected():
            pass
        
    print('network config:', sta_if.ifconfig())
# end __wlan_connect

def check_for_update():
    """
    If there's an update, download it and reboot
    """
    
    OTA = senko.Senko(
        user="adinderosier",
        repo="eset-sp-2023",
        branch="master",
        working_dir="src",
        files = ["*.py"]
    )
    
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
# end __check_for_update