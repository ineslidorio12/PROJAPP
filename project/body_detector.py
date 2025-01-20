import cv2
import mediapipe as mp
import time

class BodyGestureDetector:
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

        self.drawing_spec_landmarks = self.mp_drawing.DrawingSpec(color=(80, 22, 255), thickness=1, circle_radius=3)
        self.drawing_spec_connections = self.mp_drawing.DrawingSpec(color=(80, 44, 255), thickness=1, circle_radius=1)

        # Número mínimo de frames para confirmar o gesto
        self.ultimo_gesto = None
        self.tempo_ultimo_gesto = 0
        self.intervalo_tempo = 3

    def detetar_gestos(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            
            gestos_atual = {
                "braco_cruzado": self.detetar_bracos_cruzados(landmarks),
                "braco_levantado": self.detetar_braco_levantado(landmarks),
                "inclinado_direita": self.detetar_inclinacao_direita(landmarks),
                "inclinado_esquerda": self.detetar_inclinacao_esquerda(landmarks),
                "saltar": self.detetar_salto(landmarks)
            }

            gesto_atual_detetado = None
            for gesto, detetado in gestos_atual.items():
                if detetado:
                    gesto_atual_detetado = gesto
                    break  # Apenas o primeiro gesto detetado é considerado

            tempo_atual = time.time()
            if gesto_atual_detetado and (tempo_atual - self.tempo_ultimo_gesto) > self.intervalo_tempo:
                self.ultimo_gesto = gesto_atual_detetado
                self.tempo_ultimo_gesto = tempo_atual  # Atualiza o tempo do último gesto detetado
                print(f"Gesto confirmado: {gesto_atual_detetado}")
            elif not gesto_atual_detetado:
                self.ultimo_gesto = None
                
            # Desenha landmarks na tela
            mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        # Retorna o frame e os gestos confirmados
        return frame

    def detetar_bracos_cruzados(self, landmarks):
        mao_esquerda_x = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST].x
        mao_direita_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST].x
        ombro_esquerdo_x = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER].x
        ombro_direito_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].x

        return mao_direita_x < ombro_esquerdo_x and mao_esquerda_x > ombro_direito_x

    def detetar_braco_levantado(self, landmarks):
        mao_esquerda_y = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST].y
        mao_direita_y = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST].y
        ombro_esquerdo_y = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER].y
        ombro_direito_y = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].y

        return mao_esquerda_y < ombro_esquerdo_y or mao_direita_y < ombro_direito_y

    def detetar_inclinacao_direita(self, landmarks):
        ombro_esquerdo_x = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER].x
        ombro_direito_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].x
        quadril_esquerdo_x = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP].x
        quadril_direito_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP].x

        return (ombro_esquerdo_x + quadril_esquerdo_x) / 2 < (ombro_direito_x + quadril_direito_x) / 2
        

    def detetar_inclinacao_esquerda(self, landmarks):
        ombro_esquerdo_x = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER].x
        ombro_direito_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].x
        quadril_esquerdo_x = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP].x
        quadril_direito_x = landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP].x

        return (ombro_esquerdo_x + quadril_esquerdo_x) / 2 > (ombro_direito_x + quadril_direito_x) / 2
        

    def detetar_salto(self, landmarks):
        quadril_y = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP].y
        pe_esquerdo_y = landmarks[self.mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y
        pe_direito_y = landmarks[self.mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y

        return quadril_y < (pe_esquerdo_y + pe_direito_y) / 2

    def close(self):
        self.pose.close()
