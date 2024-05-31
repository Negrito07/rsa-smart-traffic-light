import json
import os
from ultralytics import YOLO
import supervision as sv
import numpy as np
from typing import List,Tuple
import paho.mqtt.client as mqtt
import threading

class Yolo:
    MODEL = "yolov8x.pt"
    PEDAL_CLASSES = [0]
    VEHICLE_CLASSES = [1, 2, 3, 5, 7]
    COLORS = sv.ColorPalette.default()
    PEDAL_ZONES_POLYGONS = [
      np.array([[671,449],[817,495],[833,476],[767,460],[751,422],[705,411]]),
      np.array([[593,520],[562,548],[697,576],[718,552]])
  ]

    VEHICAL_ZONES_POLYGONS =[
        np.array([[834,499],[774,577],[1339,643],[1345,569]])
    ]


    def __init__(self, info):
        self.model = YOLO(Yolo.MODEL)
        self.class_names_dict = self.model.model.names
        self.frame_to_detect = None
        self.detections = None
        self.count = {"pessoas": 0, "veiculos":0}
        self.info = info
        self.pedal_polygon=self.initiate_polygon_zones(
            polygons=Yolo.PEDAL_ZONES_POLYGONS,
            frame_resolution_wh=info.resolution_wh,
            triggering_position=sv.Position.BOTTOM_CENTER
        )
        self.vehicle_polygon=self.initiate_polygon_zones(
            polygons=Yolo.VEHICAL_ZONES_POLYGONS,
            frame_resolution_wh=self.info.resolution_wh,
            triggering_position=sv.Position.BOTTOM_CENTER
        )

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]
        self.detections = sv.Detections.from_ultralytics(results)
        pedal_detections = sv.Detections.from_ultralytics(results)
        vehicle_detections = sv.Detections.from_ultralytics(results)

        detections_pedal_polygon = []
        for pedal_zone in self.pedal_polygon:
            pedal_detections = pedal_detections[np.isin(pedal_detections.class_id, Yolo.PEDAL_CLASSES)]
            pedal_detections = sv.ByteTrack(track_thresh=0.25, track_buffer=30, match_thresh=0.8, frame_rate=30).update_with_detections(pedal_detections)
            detection_pedal_polygon = pedal_detections[pedal_zone.trigger(pedal_detections)]
            detections_pedal_polygon.append(detection_pedal_polygon)
        


        detections_vehicle_polygon = []
        for vehicle_zone in self.vehicle_polygon:
            vehicle_detections = vehicle_detections[np.isin(vehicle_detections.class_id, Yolo.VEHICLE_CLASSES)]
            vehicle_detections = sv.ByteTrack(track_thresh=0.25, track_buffer=30, match_thresh=0.8, frame_rate=30).update_with_detections(vehicle_detections)
            detection_vehicle_polygon = vehicle_detections[vehicle_zone.trigger(vehicle_detections)]
            detections_vehicle_polygon.append( detection_vehicle_polygon)   


        # self.detections = self.detections[np.isin(self.detections.class_id, Yolo.SELECTED_CLASSES)]
        

        self.detections = self.detections[[valor > 0.5 for valor in self.detections.confidence]]
        self.detections = sv.ByteTrack(track_thresh=0.25, track_buffer=30, match_thresh=0.8, frame_rate=30).update_with_detections(self.detections)
        self.detections = sv.Detections.merge(detections_pedal_polygon + detections_vehicle_polygon)

       
        
        self.count["pessoas"] = self.detections.class_id.tolist().count(0)
        self.count["veiculos"] = len(self.detections.class_id) - self.detections.class_id.tolist().count(0)
        return self.count
    
    def draw(self, frame):
        labels = [
            f"#{tracker_id} {self.class_names_dict[class_id]} {confidence:0.2f}"
            for confidence, class_id, tracker_id in zip(self.detections.confidence, self.detections.class_id, self.detections.tracker_id)
        ]

        annotated_frame = sv.TraceAnnotator(thickness=4, trace_length=50).annotate(scene=frame.copy(),detections=self.detections)
        anotated_frame=sv.BoxAnnotator(thickness=1, text_thickness=1, text_scale=0.5).annotate(scene=annotated_frame, detections=self.detections, labels=labels)
        for pedal_zone in self.pedal_polygon:
            annotated_frame = sv.draw_polygon(
                scene = annotated_frame,
                polygon=pedal_zone.polygon,
                color = Yolo.COLORS.colors[0]
            )

        for vehicle_zone in self.vehicle_polygon:
            annotated_frame = sv.draw_polygon(
                scene = annotated_frame,
                polygon=vehicle_zone.polygon,
                color = Yolo.COLORS.colors[10]
            )

        return anotated_frame
        # sv.plot_image(anotated_frame, (16,16))

    def initiate_polygon_zones(
        self,
        polygons: List[np.ndarray],
        frame_resolution_wh: Tuple[int,int],
        triggering_position:sv.Position = sv.Position.BOTTOM_CENTER
    ) -> List[sv.PolygonZone]:
        return [
            sv.PolygonZone(
                polygon=polygon,
                frame_resolution_wh=frame_resolution_wh,
                triggering_position=triggering_position
            )
            for polygon in polygons
        ]

    def handle_connect(self, client, obj, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe('in/frames')

    def handle_message(self, client, obj, msg):
        message = msg.payload.decode('utf-8')
        topic = msg.topic
        print('Topic: ' + msg.topic)
        # print('Message: ' + message)
        obj = json.loads(message)
        self.frame_to_detect = np.array(obj.frame)

    def generate(self, client):
        while True:
            if self.frame_to_detect:
                count = self.detect(self.frame_to_detect)
                detection = self.draw(self.frame_to_detect)
                obj = {
                    'count': count,
                    'detection': detection
                }
                msg = json.dumps(obj)
                client.publish('in/detections', msg)

    # Simulate camera live feed from source video (sending frames through mqqt) 
    def start(self):
        client = mqtt.Client()
        client.on_connect = self.handle_connect
        client.on_message = self.handle_message
        client.connect('192.168.98.10', 1883, 60)     # connect to the rsu broker
        threading.Thread(target=self.client.loop_forever).start()
        self.generate(client)


        

