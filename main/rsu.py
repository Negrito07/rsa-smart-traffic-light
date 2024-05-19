import json
import paho.mqtt.client as mqtt
import threading
from time import sleep

num_cars = 10
num_pedestrians = 5


def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("vanetza/out/spatem")
    

def on_message(client, obj, msg):
    message = msg.payload.decode('utf-8')
    print('Topic: ' + msg.topic)
    print('Message: ' + message)
    obj = json.loads(message)

   


def generate():
    # Carregar o modelo da mensagem SPAT do arquivo JSON
    f = open('in_spatem.json')
    spat_message = json.load(f)

    # Simular o número de carros e pedestres (Isto vem do YOLO)
    global num_cars
    num_cars -= 1
    if num_cars < 0:
        num_cars = 10

    
    # Decidir a cor do semáforo
    light_state = decide_traffic_light(num_cars, num_pedestrians)

    # Atualizar o campo eventState com base na decisão do semáforo
    for state in spat_message["intersections"][0]["states"]:
        state["state-time-speed"][0]["eventState"] = 5 if light_state == "GREEN" else 3

    # Converter a mensagem modificada para uma string JSON
    spat_message_str = json.dumps(spat_message)

    # Publicar a mensagem SPAT
    client.publish("vanetza/in/spatem", spat_message_str)


def decide_traffic_light(num_cars, num_pedestrians):
    # Simular lógica de decisão
    print(num_cars)
    if num_cars > num_pedestrians:
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
    sleep(2)
    