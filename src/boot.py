## Author: Adin De'Rosier adin.derosier@oit.edu
## In accordance with the requirements listed in the project documentation
## Please refer to LICENSE before modifying any code
## System Bootloader V1.0

import utils

print("System Bootloader V1.0")

# Connect to Wi-Fi network
utils.wlan_connect('Argus', 'ivetoldyoubefore')

# Check for updates in the source code
utils.check_for_update()

