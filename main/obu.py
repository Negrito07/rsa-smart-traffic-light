import json
import paho.mqtt.client as mqtt
import threading
from time import sleep
from geographiclib.geodesic import Geodesic

def on_connect(client, obj, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("vanetza/out/spatem")

def on_message(client, obj, msg):
    message = msg.payload.decode('utf-8')

    # Descomentar estes dois prints para mostrar que spatem esta a receber a obu
    #print('Topic OBU: ' + msg.topic)
    #print('Message OBU: ' + message)

    spatem = json.loads(message)
    if msg.topic == "vanetza/out/spatem":
        # Check if the 'fields' and 'spat' keys exist
        # Extracting the eventstate field from json
        if "fields" in spatem and "spat" in spatem["fields"]:
            intersections = spatem["fields"]["spat"].get("intersections", [])
            for intersection in intersections:
                states = intersection.get("states", [])
                for state in states:
                    state_time_speed_list = state.get("state-time-speed", [])
                    for sts in state_time_speed_list:
                        event_state = sts.get("eventState")
                        if event_state == 3:
                            print('RED')
                        elif event_state == 5:
                            print('GREEN')
                        else:
                            print('Unknown eventState:', event_state)
        else:
            print("No SPAT data available in the message")

def generate():
    f = open('./in_spatem.json')
    m = json.load(f)
    m = json.dumps(m)
    client.publish("vanetza/in/spatem", m)
    f.close()
    sleep(1)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.98.20", 1883, 60)

threading.Thread(target=client.loop_forever).start()

while True:
    generate()
