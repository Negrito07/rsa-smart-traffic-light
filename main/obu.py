import json
import paho.mqtt.client as mqtt
import threading
from time import sleep


def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("vanetza/out/spatem")
    

def on_message(client, obj, msg):
    message = msg.payload.decode('utf-8')
    
    print('Topic: ' + msg.topic)
    print('Message' + message)

    obj = json.loads(message)

    print('Object:' + obj)


def generate():
    f = open('./in_cam.json')
    m = json.load(f)
    m = json.dumps(m)
    client.publish("vanetza/in/cam",m)
    f.close()
    sleep(1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.98.10", 1883, 60)

threading.Thread(target=client.loop_forever).start()

while(True):
    generate()
