import os
import asyncio
import supervision as sv
import numpy as np



class Camera:
  
  def __init__(self, src):
    self.info = sv.VideoInfo.from_video_path(src)        # informações do vídeo
    self.generator = sv.get_video_frames_generator(src)
    self.iterator = iter(self.generator)
    self.frame = next(self.iterator)
  

  # Simulate camera live feed from source video
  def read(self, seconds):
    for i in range(self.info.fps*seconds):
      self.frame = next(self.iterator)
    return (self.frame,self.pedal_zone,self.vehical_zone)



        