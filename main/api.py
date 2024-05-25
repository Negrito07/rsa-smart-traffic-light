import json
import paho.mqtt.client as mqtt
import threading

class Monitor:
    '''Helper class to listen to a given vanetza
    mqtt topic published by a given host.'''

    def __init__(self, host, topic):
        self.host = host
        self.topic = topic

    def on_connect(self, client, obj, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(f"vanetza/in/{self.topic}")

    def on_message(self, client, obj, msg):
        message = msg.payload.decode('utf-8')
        print('Topic: ' + msg.topic)
        print('Message: ' + message)
        obj = json.loads(message)


# hosts/topics to listen
monitors = [
    Monitor("192.168.98.10", "spatem"),     # rsu
    Monitor("192.168.98.20", "cam")         # obu
]

for monitor in monitors:
    client = mqtt.Client()
    client.on_connect = monitor.on_connect
    client.on_message = monitor.on_message
    client.connect(monitor.host, 1883, 60)
    threading.Thread(target=client.loop_forever).start()
    