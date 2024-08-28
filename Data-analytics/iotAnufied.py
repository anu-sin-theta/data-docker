import asyncio
import time

from azure.iot.device.aio import IoTHubDeviceClient
async def main():
    conn_str = "HostName=remotehub.azure-devices.net;DeviceId=laptop-test;SharedAccessKey=mykey"
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    while 1:
        await device_client.connect()
        print("Sending message...")
        await device_client.send_message("Hello, Cloud!")
        print("Message successfully sent!")
        #message from hub
        message = device_client.on_message_received
        if message:
            print("the data received from the hub is: ",message.data)
        else:
            print("No message received")
        #await device_client.disconnect()
        #time.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())