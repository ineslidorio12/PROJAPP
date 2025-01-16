import cv2 as cv
import mediapipe as mp


class HandDetector:
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def detect_hands(self, frame):
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results

    def draw_hands(self, frame, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1),
                )
                
                if self.detect_gesto(results):
                    cv.putText(
                        frame,
                        "Mao aberta detectada!",
                        (10, 50),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                        cv.LINE_AA,
                    )

    def detect_gesto(self, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                dedos_levantados = self.contar_dedos(hand_landmarks)
                if dedos_levantados == 5:
                    return True
            
        return False
    
    def contar_dedos(self, hand_landmarks):
        dedos = [4, 8, 12, 16, 20]
        dedos_levantados = 0
        for dedo in dedos:
            if hand_landmarks.landmark[dedo].y < hand_landmarks.landmark[dedo - 2].y:
                dedos_levantados += 1
        return dedos_levantados
            
        
    def close(self):
        self.hands.close()
