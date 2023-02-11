import asyncio, time, json
from bleak import BleakClient

# Function to handle accelerometer data received as a notification
def handle_accel_notification(sender, data):
    # Split the data into separate x, y, z values
    x, y, z = data.decode().split(',')
    acX = float(x)
    acY = float(y)
    acZ = float(z)

    # Get the current time
    timestamp = time.time()

    # Create a dictionary with the accelerometer data
    accel_data = {"acc_x": acX, "acc_y": acY, "acc_z": acZ, "Timestamp": timestamp}

    # Write the accelerometer data to a JSON file
    with open("data.json", "a") as json_file:
        json.dump(accel_data, json_file)
        json_file.write(',\n')

# Function to handle gyroscope data received as a notification
def handle_gyro_notification(sender, data):
    # Split the data into separate x, y, z values
    gx, gy, gz = data.decode().split(',')
    gX = float(gx)
    gY = float(gy)
    gZ = float(gz)

    # Get the current time
    timestamp = time.time()

    # Create a dictionary with the gyroscope data
    gyro_data = {"gy_x": gX, "gy_y": gY, "gy_z": gZ, "Timestamp": timestamp}

    # Write the gyroscope data to a JSON file
    with open("data.json", "a") as json_file:
        json.dump(gyro_data, json_file)
        json_file.write(',\n')

# Asynchronous function to connect to the BLE peripheral
async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        # Start receiving notifications for the accelerometer data
        await client.start_notify("00002001-0000-1000-8000-00805f9b34fb", handle_accel_notification)

        # Start receiving notifications for the gyroscope data
        await client.start_notify("00002011-0000-1000-8000-00805f9b34fb", handle_gyro_notification)

        # Continuously run the loop
        while True:
            await asyncio.sleep(0.001)

# Address of the BLE peripheral to connect to
address = "00:00:00:00:00:00"

# Get the event loop
loop = asyncio.get_event_loop()

# Run the asynchronous function
loop.run_until_complete(run(address, loop))
