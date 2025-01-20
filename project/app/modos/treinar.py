import pygame
import cv2 as cv
import time
import random
from config import JANELA, FONTE_TITULO, FONTE_BOTAO, BRANCO, PRETO, VERDE, VERMELHO, LARGURA_JANELA, ALTURA_JANELA


class ModoTreinar:
    def __init__(self, video, hand_detector):
        self.video = video
        self.hand_detector = hand_detector
        self.start_time = time.time()
        self.running = True
        self.palavras_gestos = {
            "OLA!": "palm",
            "ADEUS!":"fist",
            "OBRIGADA":"thumbs_up",
            "TUDO BEM?":"peace",
            "AJUDA":"3fingers"
        }
        
        self.palavra_atual, self.gesto_correto = random.choice(list(self.palavras_gestos.items()))
        self.feedback = None
        self.feedback_time = None
        self.feedback_delay = 2
    
    
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

        return results 
 
# ajustes dos gestos----------------------------------------------------------------------------------------------
   
    def verificar_gesto(self, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if self.gesto_correto == "palm" and self.hand_detector.detect_gesto_mao_aberta(hand_landmarks):
                    return True
                if self.gesto_correto == "thumbs_up" and self.hand_detector.detect_gesto_thumbs_up(hand_landmarks):
                    return True
                if self.gesto_correto == "peace" and self.hand_detector.detect_gesto_peace_sign(hand_landmarks):
                    return True
                if self.gesto_correto == "3fingers" and self.hand_detector.detect_gesto_tres_dedos(hand_landmarks):
                    return True
                if self.gesto_correto == "fist" and self.hand_detector.detect_gesto_mao_fechada(hand_landmarks):
                    return True
                
        return False

    def executar(self):
        while self.running:
            JANELA.fill(PRETO)
            
            frame = self.video.get_frame()
            if frame is not None:
                results = self.mostrar_camera(frame)
                
                if self.verificar_gesto(results):
                    self.feedback = "Correto!"
                    self.feedback_time = time.time()
                    
            if self.feedback and (time.time() - self.feedback_time > self.feedback_delay):
                self.palavra_atual, self.gesto_correto = random.choice(list(self.palavras_gestos.items()))
                self.feedback = None
                    
            current_time =time.time()
            tempo_passado = int(current_time - self.start_time)
  
# ajustes da interface/implementacao do modo ------------------------------------------------------------------------------------------
          
            if tempo_passado < 5:
                self.desenhar_texto("Esta na hora de treinar o que aprendes-te!",
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2))
            
            elif 5 <= tempo_passado < 11:
                self.desenhar_texto("OBJETIVO", FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 50))
                self.desenhar_texto("Faz os gestos que correspondem as palavras mostradas.", 
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2))
                
                tempo_restante = 11 - tempo_passado
                self.desenhar_texto(f"{tempo_restante} s",
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 + 50))
            
            else:
                self.desenhar_texto(f"{self.palavra_atual}",
                                    FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 50))
                
                if self.feedback:
                    self.desenhar_texto(self.feedback, 
                                        FONTE_BOTAO, VERDE, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 + 50))
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            pygame.display.flip()