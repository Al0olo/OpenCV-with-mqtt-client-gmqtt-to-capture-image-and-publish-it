# Import necessary modules and functions from the existing script
import asyncio
import os
import signal
import time
import base64

from cv2 import VideoCapture, destroyWindow, imshow, imwrite, waitKey
import gmqtt
from mqtt import *
from gmqtt import Client as MQTTClient
from cv2 import *

async def capture_image():
    cam_port = 0
    cam = VideoCapture(cam_port) 
    counter = 0
    result, image = cam.read()
    if result:
        imwrite("GeeksForGeeks.png", image)
        with open("GeeksForGeeks.png", "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_image
host = '83.110.196.13'
username = 'AHLN'
password = '123456'

# Instantiate the CustomMQTTClient globally
client = MQTTClient('ali')
async def run_main(message):
    host = '83.110.196.13'
    username = 'AHLN'
    password = '123456'
    client.on_message = on_message
    client.on_connect = on_connect
    client.set_auth_credentials(username=username,password=password)
    await client.connect(host, 1883, keepalive=65535)
    while True:
        image = await capture_image()
        await publish_message(image,client)
        await asyncio.sleep(2)
    # print(ali)
    await STOP.wait()
    await client.disconnect()

# async def publish(message,counter):
#     # host = '83.110.196.13'
#     # username = 'AHLN'
#     # password = '123456'
#     # client.on_message = on_message
#     # client.on_connect = on_connect
#     # client.set_auth_credentials(username=username,password=password)
#     # # if counter == 0:
#     # await client.connect(host, 1883, keepalive=65535)
#     # gmqtt.Message('TEST/WILL/42', "I'm dead finally", will_delay_interval=10)
#     # await publish_message(message,ali)
#     print(ali)
#     # await STOP.wait()
#     # await client.disconnect()

loop = asyncio.get_event_loop()

main_task = loop.create_task(run_main("start"))
# image_task = loop.create_task(capture_image())
# publish_task = loop.create_task(execute_publish())

combined_task = asyncio.gather(main_task)
loop.run_until_complete(combined_task)