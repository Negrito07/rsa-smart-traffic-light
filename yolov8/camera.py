import json
import os
import asyncio
import supervision as sv
import numpy as np
from time import sleep
import threading
import paho.mqtt.client as mqtt

class Camera:
  
  def __init__(self, src):
    self.info = sv.VideoInfo.from_video_path(src)        # informações do vídeo
    self.generator = sv.get_video_frames_generator(src)
    self.frame = None
    self.period = 1/self.info.fps

  def handle_connect(self, client, obj, flags, rc):
        print("Connected with result code "+str(rc))
  
  # Simulate camera live feed from source video
  def read(self, seconds):
    for i in range(self.info.fps*seconds):
      self.frame = next(self.iterator)
    return (self.frame,self.pedal_zone,self.vehical_zone)
  
  # Simulate camera live feed from source video (sending frames through mqqt) 
  def start(self):
    client = mqtt.Client()
    client.on_connect = self.handle_connect
    client.connect('192.168.98.10', 1883, 60)     # connect to the rsu broker
    threading.Thread(target=client.loop_forever).start()
    for frame in self.generator:
      obj = {'frame': frame.tolist()}
      msg = json.dumps(obj)
      client.publish("in/frames", msg)
      sleep(self.period)


def main():
    camera = Camera("./poland-5fps.mp4")
    camera.start()

main()

        