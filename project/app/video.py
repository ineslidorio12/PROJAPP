import cv2
import threading

class VideoCaptureThread:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise ValueError("ERRO CAMERA")
        self.frame = None
        self.running = True
        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()
        
    def _update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = cv2.flip(frame, 1)
                
    def get_frame(self):
        return self.frame
    
    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()