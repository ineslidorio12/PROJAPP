import os
import cv2 as cv

class Objeto:
    def __init__(self):
        self.CLASS_FILE = "project/models/mobilenet_coco_classes.txt"
        self.NET_TRAINED = "project/models/frozen_inference_graph.pb"
        self.NET_CONFIG = "project/models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"

        self.CONFIDENCE_THRESHOLD = 0.6
        self.INPUT_SIZE = (320, 320)
        self.SCALE_FACTOR = 1.0 / 127.5
        self.MEAN_VALUES = (127.5, 127.5, 127.5)
        self.SWAP_RB = True

        self.class_name = self.carregar_class()
        self.net = self.carregar_modelo()
        
        
    def carregar_class(self):
        if not os.path.exists(self.CLASS_FILE):
            raise FileNotFoundError("Class não encontrada: {self.CLASS_FILE}")
        with open(self.CLASS_FILE, "rt") as f:
            return f.read(). rstrip("\n").split("\n")
        
        
    def carregar_modelo(self):
        if not os.path.exists(self.NET_TRAINED) or not os.path.exists(self.NET_CONFIG):
            raise FileNotFoundError("Arquivos do modelo SSD não encontrados.")
        return cv.dnn.readNetFromTensorflow(self.NET_TRAINED, self.NET_CONFIG)
    
    
    def detetar_objetos(self, frame, confianca_minima=None):
        if confianca_minima is not None:
            self.CONFIDENCE_THRESHOLD = confianca_minima
        (h, w) = frame.shape[:2]
        blob = cv.dnn.blobFromImage(
            frame,
            scalefactor=self.SCALE_FACTOR,
            size=self.INPUT_SIZE,
            mean=self.MEAN_VALUES,
            swapRB=self.SWAP_RB,
            crop=False,
        )
        self.net.setInput(blob)
        detections = self.net.forward()

        results = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.CONFIDENCE_THRESHOLD:
                idx = int(detections[0, 0, i, 1])
                class_name = self.class_name[idx] if idx < len(self.class_name) else "Unknown"
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")
                results.append((class_name, confidence, (startX, startY, endX, endY)))
        return results