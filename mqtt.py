import asyncio
import os
import signal
import time

from gmqtt import Client as MQTTClient

STOP = asyncio.Event()

TOPIC = 'ahlanBox/ahlanBox_Ahln_24_B0000001/liveStream'
def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/#', qos=0)


def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:', payload)


def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

def ask_exit(*args):
    STOP.set() 

client = MQTTClient('ali')

async def publish_message(message,client):
    client.publish(TOPIC, message, response_topic='RESPONSE/TOPIC')
