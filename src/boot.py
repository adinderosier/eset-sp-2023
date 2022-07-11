## Author: Adin De'Rosier adin.derosier@oit.edu
## In accordance with the requirements listed in the project documentation
## Please refer to LICENSE before modifying any code
## System Boot V1.0

import utils
import senko
import machine

OTA = senko.Senko(
    user="adinderosier",
    repo="eset-sp-2023",
    branch="master",
    working_dir="src",
    files = ["boot.py", "main.py"]
)

# Connect to Wi-Fi network
utils.wlan_connect('Argus', 'ivetoldyoubefore')
    
if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()