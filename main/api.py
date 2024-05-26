import json
import paho.mqtt.client as mqtt
import threading

class Monitor:
    '''Helper class to listen to a given
    mqtt topic published by a given host.'''

    def __init__(self, host, topic, on_message=lambda msg: msg):
        self.host = host
        self.topic = topic
        self.on_message = on_message

    def handle_connect(self, client, obj, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(self.topic)

    def handle_message(self, client, obj, msg):
        message = msg.payload.decode('utf-8')
        topic = msg.topic
        print('Topic: ' + msg.topic)
        print('Message: ' + message)
        self.on_message(topic, message)

    def start(self):
        client = mqtt.Client()
        client.on_connect = self.handle_connect
        client.on_message = self.handle_message
        client.connect(self.host, 1883, 60)
        threading.Thread(target=client.loop_forever).start()


# hosts/topics to listen
# monitors = [
#     Monitor("192.168.98.10", "spatem"),     # rsu
#     Monitor("192.168.98.20", "cam")         # obu
# ]

# for monitor in monitors:
#     client = mqtt.Client()
#     client.on_connect = monitor.on_connect
#     client.on_message = monitor.on_message
#     client.connect(monitor.host, 1883, 60)
#     threading.Thread(target=client.loop_forever).start()
    