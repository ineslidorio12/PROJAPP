import cv2 as cv
import mediapipe as mp


class HandDetector:
    def __init__(self, min_detection_confidence=0.7, min_tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
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

# detetcao dos gestos escolhidos ----------------------------------------------------------------------------------------
  
    def detect_gesto_mao_aberta(self, hand_landmarks):
        dedos_levantados = self.contar_dedos(hand_landmarks)
        return dedos_levantados == 5
    
    
    def detect_gesto_thumbs_up(self, hand_landmarks):
        polegar_levantado = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y < hand_landmarks.landmark[2].y
        
        outros_dedos_abaixados = (
            hand_landmarks.landmark[8].y > hand_landmarks.landmark[5].y and
            hand_landmarks.landmark[12].y > hand_landmarks.landmark[9].y and
            hand_landmarks.landmark[16].y > hand_landmarks.landmark[13].y and
            hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y
        )
        
        return polegar_levantado and outros_dedos_abaixados
    
    def detect_gesto_mao_fechada(self, hand_landmarks):
        dedos_levantados = self.contar_dedos(hand_landmarks)
        return dedos_levantados == 0
    
    def detect_gesto_peace_sign(self, hand_landmarks):
        dedos_levantados = self.contar_dedos(hand_landmarks)
        return dedos_levantados == 2
    
    def detect_gesto_tres_dedos(self, hand_landmarks):
        dedos_levantados = self.contar_dedos(hand_landmarks)
        return dedos_levantados == 3
    
  
    def contar_dedos(self, hand_landmarks):
        dedos = [8, 12, 16, 20]
        dedos_levantados = 0
        
        for dedo in dedos:
            if hand_landmarks.landmark[dedo].y < hand_landmarks.landmark[dedo - 2].y:
                dedos_levantados += 1
        
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:  # Para mão direita
            dedos_levantados += 1
        
        return dedos_levantados
            
        
    def close(self):
        self.hands.close()
