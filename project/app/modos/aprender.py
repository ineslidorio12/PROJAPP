import pygame
import cv2 as cv
import time
from config import JANELA, FONTE_TITULO, FONTE_BOTAO, BRANCO, PRETO, LARGURA_JANELA, ALTURA_JANELA


class ModoAprender:
    def __init__(self, video, hand_detector):
        self.video = video
        self.hand_detector = hand_detector
        self.start_time = time.time()
        self.running = True
        self.mostrar_imagens_flag = False

        self.imagens = [
            pygame.image.load("project/assets/gesto/THUMBS.png"),
            pygame.image.load("project/assets/gesto/PEACE.png"),
            pygame.image.load("project/assets/gesto/PALM.png"),
            pygame.image.load("project/assets/gesto/FIST.png"),
            pygame.image.load("project/assets/gesto/3FINGERS.png")
        ]
        self.imagens = [pygame.transform.scale(img, (300, 300)) for img in self.imagens]
    
    def desenhar_texto(self, texto, fonte, cor, posicao):
        texto_superficie = fonte.render(texto, True, cor)
        texto_retangulo = texto_superficie.get_rect(center=posicao)
        JANELA.blit(texto_superficie, texto_retangulo)
        
    
    def mostrar_camera(self, frame):
        results = self.hand_detector.detect_hands(frame)
        self.hand_detector.draw_hands(frame, results)
        
        frame_resized = cv.resize(frame, (300, 225))
        frame_surface = pygame.image.frombuffer(frame_resized.tobytes(), frame_resized.shape[1::-1], "BGR")
        JANELA.blit(frame_surface, (LARGURA_JANELA - 320, ALTURA_JANELA - 250))

    def mostrar_imagens(self, gestos_detetados):
        posicoes = [
            (LARGURA_JANELA // 2 - 350, ALTURA_JANELA // 2 - 150),
            (LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 150),
            (LARGURA_JANELA // 2 + 350, ALTURA_JANELA // 2 - 150),
            (LARGURA_JANELA // 2 - 200, ALTURA_JANELA // 2 + 150),
            (LARGURA_JANELA // 2 + 200, ALTURA_JANELA // 2 + 150),
        ]
        
        for i, (img, pos) in enumerate(zip(self.imagens, posicoes)):
            JANELA.blit(img, img.get_rect(center=pos))
            
            if i == 2 and 'palm' in gestos_detetados:
                pygame.draw.circle(JANELA, (0, 255, 0), pos, 30)
            if i == 0 and 'thumbs_up' in gestos_detetados:
                pygame.draw.circle(JANELA, (0, 255, 0), pos, 30)
            if i == 3 and 'fist' in gestos_detetados:
                pygame.draw.circle(JANELA, (0, 255, 0), pos, 30)
            if i == 1 and 'peace' in gestos_detetados:  # Índice 1 -> PEACE.png (dois dedos levantados)
                pygame.draw.circle(JANELA, (0, 255, 0), pos, 30)   
         
            
    def executar(self):
        while self.running:
            JANELA.fill(PRETO)
            
            frame = self.video.get_frame()
            gestos_detetados = []
            if frame is not None:
                results = self.hand_detector.detect_hands(frame)
                self.hand_detector.draw_hands(frame, results)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        
                        if self.hand_detector.detect_gesto_mao_aberta(hand_landmarks):
                            gestos_detetados.append('palm')
                        if self.hand_detector.detect_gesto_thumbs_up(hand_landmarks):
                            gestos_detetados.append('thumbs_up')
                        if self.hand_detector.detect_gesto_mao_fechada(hand_landmarks):
                            gestos_detetados.append('fist')
                        if self.hand_detector.detect_gesto_peace_sign(hand_landmarks):
                            gestos_detetados.append('peace')
                            
                self.mostrar_camera(frame)
                
            current_time =time.time()
            tempo_passado = int(current_time - self.start_time)
            
            if tempo_passado < 5:
                self.desenhar_texto("Neste modo podes aprender uma linguagem gestual personalizada por nos.",
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2),
                )
            
            elif 5 <= tempo_passado < 11:
                self.desenhar_texto("OBJETIVO", FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 50))
                self.desenhar_texto("Replica os gestos e memoriza a palavra a que cada gesto esta associado.", 
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2),
                )
                
                tempo_restante = 11 - tempo_passado
                self.desenhar_texto(f"{tempo_restante} s",
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 + 50),
                )
                
            else:
                self.mostrar_imagens(gestos_detetados)
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            pygame.display.flip()