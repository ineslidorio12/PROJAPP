import os
import cv2 as cv

class Objeto:
    def __init__(self):
        self.CLASS_FILE = "project/models/mobilenet_coco_classes.txt"
        self.NET_TRAINED = "project/models/frozen_inference_graph.pb"
        self.NET_CONFIG = "project/models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"

        self.CONFIDENCE_THRESHOLD = 0.7
        self.NMS_THRESHOLD = 0.3
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
        # Create DetectionModel instead of generic Net
        model = cv.dnn_DetectionModel(self.NET_TRAINED, self.NET_CONFIG)
        model.setInputParams(
            size=self.INPUT_SIZE,
            scale=self.SCALE_FACTOR,
            mean=self.MEAN_VALUES,
            swapRB=self.SWAP_RB,
        )
        return model

    
    def detetar_objetos(self, frame, confianca_minima=None):
        if confianca_minima is not None:
            self.CONFIDENCE_THRESHOLD = confianca_minima


        classes, scores, boxes = self.net.detect(
            frame,
            confThreshold=self.CONFIDENCE_THRESHOLD,
            nmsThreshold=self.NMS_THRESHOLD
        )

        results = []
        for class_id, score, box in zip(classes, scores, boxes):
            if score > self.CONFIDENCE_THRESHOLD:
                class_name = self.class_name[class_id] if class_id < len(self.class_name) else "Unknown"
                startX, startY, width, height = box
                endX = startX + width
                endY = startY + height
                results.append((class_name, float(score), (startX, startY, endX, endY)))
        return results