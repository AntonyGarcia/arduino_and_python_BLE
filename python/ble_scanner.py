import asyncio
from bleak import discover

# Asynchronous function to scan for BLE devices
async def scan():
    # Use the discover function from the bleak library to scan for devices
    devices = await discover()

    # Loop through the list of discovered devices
    for d in devices:
        # Print the information for each device
        print(d)

# Get the event loop
loop = asyncio.get_event_loop()

# Run the asynchronous function to scan for devices
loop.run_until_complete(scan())

