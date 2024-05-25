import json
import paho.mqtt.client as mqtt
import threading
from time import sleep
from geopy.distance import geodesic
from geopy.point import Point
import math

# Global variable to store the current traffic light state
current_event_state = None

def on_connect(client, obj, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("vanetza/out/spatem")

def on_message(client, obj, msg):
    global current_event_state
    message = msg.payload.decode('utf-8')
    
    spatem = json.loads(message)
    if msg.topic == "vanetza/out/spatem":
        if "fields" in spatem and "spat" in spatem["fields"]:
            intersections = spatem["fields"]["spat"].get("intersections", [])
            for intersection in intersections:
                states = intersection.get("states", [])
                for state in states:
                    state_time_speed_list = state.get("state-time-speed", [])
                    for sts in state_time_speed_list:
                        event_state = sts.get("eventState")
                        current_event_state = event_state
                        if event_state == 3:
                            print('RED')
                        elif event_state == 5:
                            print('GREEN')
                        else:
                            print('Unknown eventState:', event_state)
        else:
            print("No SPATEM data available in the message")

def generate():
    f = open('./in_spatem.json')
    m = json.load(f)
    m = json.dumps(m)
    client.publish("vanetza/in/spatem", m)
    f.close()
    sleep(1)

def calculate_bearing(pointA, pointB):
    lat1 = math.radians(pointA.latitude)
    lat2 = math.radians(pointB.latitude)
    diffLong = math.radians(pointB.longitude - pointA.longitude)

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def simulate_movement(initial_coords, final_coords, stop_coords, duration, update_interval=1):
    global current_event_state

    start_point = Point(initial_coords)
    end_point = Point(final_coords)
    stop_point = Point(stop_coords)
    total_distance = geodesic(start_point, end_point).meters
    total_steps = int(duration / update_interval)
    bearing = calculate_bearing(start_point, end_point)

    for step in range(total_steps + 1):
        fraction = step / total_steps
        distance_moved = total_distance * fraction
        current_position = geodesic(meters=distance_moved).destination(point=start_point, bearing=bearing)
        
        print(f"Current Position: {current_position.latitude}, {current_position.longitude}")

        # Check if the current position is close to the stop coordinates
        if geodesic(current_position, stop_point).meters < 1:  # within 1 meters of stop point (Semaforo)
            print("Reached stop coordinates. Checking traffic light state...")
            while current_event_state != 5:  # Wait until the traffic light is green
                print("Traffic light is RED. Waiting...")
                sleep(1)
            print("Traffic light is GREEN. Proceeding...")

        # Here you can add code to publish the current position if needed
        sleep(update_interval)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.98.20", 1883, 60)

# Define initial, stop, and final coordinates (latitude, longitude)
initial_coords = (40.629994, -8.653797) #Passadeira do ISCA 40m antes
stop_coords = (40.630272896858486, -8.653951274842521) # Simulacao do Semaforo na Passadeira ISCA
final_coords = (40.630446, -8.654048) #  Rotunda do ISCA 

# Simulation parameters
duration = 60  # Total duration of the movement in seconds
update_interval = 1  # Interval to update the position in seconds

# Start MQTT loop in a separate thread
threading.Thread(target=client.loop_forever).start()

# Start the movement simulation
simulate_movement(initial_coords, final_coords, stop_coords, duration, update_interval)

while True:
    generate()
