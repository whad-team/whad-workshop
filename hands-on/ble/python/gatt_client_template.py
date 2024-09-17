"""
Script template of a GATT client.
"""
from whad.ble import Central
from whad.ble.profile import UUID
from whad.device import WhadDevice

INTERFACE = "hci0"
TARGET = "74:da:ea:91:47:e3"

# Create the Central connector based on our WHAD device
central = Central(WhadDevice.create(INTERFACE))

# Connect to a specific device
device = central.connect(TARGET, random=False)

# Discover and display the profile
# 
# use Central's `discover` method to perform services and characteristics
# enumeration and then enumerate services by calling `device.services()`
# enumerator and `service.characteristics()` to enumerate a service
# discovered characteristics.

# Make sure we are connected to a device
if device is not None:
    # Discover services and characteristics here
    # <Your code here>

    # Once done, we disconnect from the target device
    device.disconnect()

# Close central connector
central.close()
