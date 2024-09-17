"""
This script is a basic GATT client based on WHAD that connects to a target
device with BD address 74:da:ea:91:47:e3 using WHAD device hci0.

Once connected to the target device, this script calls Central's `discover()`
method to perform a GATT services and characteristic enumeration and then
display the discovered services and characteristics.

Eventually, the script reads the *DeviceName* characteristic value from the
*Generic Device* service, if exposed by the target device.
"""
from whad.ble import Central
from whad.ble.profile import UUID
from whad.device import WhadDevice

INTERFACE = "hci0"
TARGET = "74:da:ea:91:47:e3"

# Create the Central connector & the WHAD device
central = Central(WhadDevice.create(INTERFACE))

# Connect to a specific device
device = central.connect(TARGET, random=False)

# Discover and display the profile
if device is not None:
    device.discover()
    print("[i] Discovered profile")
    for service in device.services():
        print(f"-- Service {service.uuid}")
        for charac in service.characteristics():
            print(f" + Characteristic {charac.uuid}")

    # Read the device name
    device_name = device.get_characteristic(UUID(0x1800), UUID(0x2A00))
    if device_name is not None:
        print("[i] Device name: ", device_name.value)

    # Disconnect
    device.disconnect()

# Close central connector
central.close()
