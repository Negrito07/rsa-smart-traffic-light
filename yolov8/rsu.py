import os
from camera import Camera
from yolo import Yolo
from time import sleep
import supervision as sv

HOME = os.getcwd()
SOURCE_VIDEO_PATH = f"{HOME}/WhatsApp Video 2024-05-24 at 19.20.04.mp4"
TARGET_VIDEO_PATH = f"{HOME}/vehicle-counting-result-with-counter.mp4"

class RSU:
  def __init__(self):
    self.camera = Camera(SOURCE_VIDEO_PATH)
    self.yolo = Yolo(self.camera.info)
    self.seconds = 0
    self.fps = self.camera.info.fps
    self.fps_des = 3
    self.frame_interval = int(self.fps/self.fps_des)

  def start(self):
    self.seconds = 1
    # while True:
    #   print(self.seconds)
    #   frame,pedal_zone,vehicle_zone = self.camera.read(self.seconds)
    #   count = self.yolo.detect(frame,pedal_zone,vehicle_zone)
    #   self.yolo.draw(frame,pedal_zone,vehicle_zone)
    sv.process_video(
        source_path = SOURCE_VIDEO_PATH,
        target_path = TARGET_VIDEO_PATH,
        callback=self.callback
    )


  def callback(self,frame,index):
    if index%self.frame_interval==0:
      count = self.yolo.detect(frame)
      print(index/self.fps, count)
    return self.yolo.draw(frame)