import json
import paho.mqtt.client as mqtt
import threading
from time import sleep

num_cars = 12
num_pedestrians = 5
green_light_duration = 20  # duration in seconds for green light
light_state = "RED"
countdown = green_light_duration
lock = threading.Lock()

def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("vanetza/out/cam")

def on_message(client, obj, msg):
    message = msg.payload.decode('utf-8')
    print('Topic: ' + msg.topic)
    print('Message: ' + message)
    obj = json.loads(message)

def generate():
    # Load the SPAT message model from the JSON file
    f = open('in_spatem.json')
    spat_message = json.load(f)
    f.close()

    # Simulate the number of cars and pedestrians (This comes from YOLO)
    global num_cars
    num_cars -= 1
    if num_cars < 0:
        num_cars = 4

    # Decide the traffic light color
    global light_state, countdown, green_light_duration
    light_state = decide_traffic_light(num_cars, num_pedestrians) 
    
    #--------------- Print dos valores ---------------- #
    print("Number of cars:", num_cars)
    #print("Number of pedestrians:", num_pedestrians)
    print("Current light state:", light_state)
    print("Countdown:", countdown)
    #--------------- Print dos valores ---------------- #


    # Update the eventState field based on the traffic light decision
    for state in spat_message["intersections"][0]["states"]:
        state["state-time-speed"][0]["eventState"] = 5 if light_state == "GREEN" else 3
        state["state-time-speed"][0]["timing"]["minEndTime"] = countdown

    # Convert the modified message to a JSON string
    spat_message_str = json.dumps(spat_message)

    # Publish the SPAT message
    client.publish("vanetza/in/spatem", spat_message_str)

def decide_traffic_light(num_cars, num_pedestrians):
    global light_state, countdown, lock
    with lock:


        if light_state == "GREEN":
            if num_pedestrians > num_cars and countdown == 12:
                countdown = 5 #leva reset. countdown das pessoas sao 5 segundos.
                return "RED"
            else:
                countdown -= 1
            if countdown == 0:
                countdown = 5 #leva reset. countdown das pessoas sao 5 segundos
                return "RED"   
            else:
                return "GREEN"    
        else:
            if num_cars > num_pedestrians and countdown == 1:
                countdown = 20 # leva reset. countdown dos carros sao 10s
                return "GREEN"
            else:
                countdown -= 1
            if countdown == 0:
                countdown = 20 # leva reset. countdown dos carros sao 10s
                return "GREEN"
            else:
                return "RED"    

            

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.98.10", 1883, 60)
threading.Thread(target=client.loop_forever).start()

while True:
    generate()
    sleep(1)
