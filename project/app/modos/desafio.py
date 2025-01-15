import pygame
import cv2 as cv
import time
from config import JANELA, FONTE_TITULO, FONTE_BOTAO, BRANCO, PRETO, LARGURA_JANELA, ALTURA_JANELA


class ModoDesafio:
    def __init__(self, video, hand_detector):
        self.video = video
        self.hand_detector = hand_detector
        self.start_time = time.time()
        self.running = True
        
        self.palavra_atual = "Olá!"
        self.gesto_esperado = "mao_aberta"
        self.correto = False
        
        
    def desenhar_texto(self, texto, fonte, cor, posicao):
        texto_superficie = fonte.render(texto, True, cor)
        texto_retangulo = texto_superficie.get_rect(center=posicao)
        JANELA.blit(texto_superficie, texto_retangulo)
        
    
    def mostrar_camera(self, frame):
        results = self.hand_detector.detect_hands(frame)
        self.hand_detector.draw_hands(frame, results)
        
        gesto_detetado = self.hand_detector.detect_gesto(results)
        if gesto_detetado == self.gesto_esperado:
            self.correto == True
            
        frame_resized = cv.resize(frame, (300, 225))
        frame_surface = pygame.image.frombuffer(frame_resized.tobytes(), frame_resized.shape[1::-1], "BGR")
        JANELA.blit(frame_surface, (LARGURA_JANELA - 320, ALTURA_JANELA - 250))
            

    def executar(self):
        while self.running:
            JANELA.fill(PRETO)
            
            frame = self.video.get_frame()
            if frame is not None:
                self.mostrar_camera(frame)
                
            current_time =time.time()
            elapsed_time = current_time - self.start_time
            
            if elapsed_time < 5:
                self.desenhar_texto("Desafia-te e mostra o que sabes!",
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2),
                )
            
            elif elapsed_time < 11:
                self.desenhar_texto("OBJETIVO", FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2 - 50))
                self.desenhar_texto("Acerta o máximo de palavras que conseguires até o tempo acabar.", 
                                    FONTE_BOTAO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2),
                )
            
                tempo_restante = int(11 - elapsed_time)
                self.desenhar_texto(f"{tempo_restante} s", FONTE_BOTAO, BRANCO, (LARGURA_JANELA //2, ALTURA_JANELA // 2 + 50),
                )
            
            else:
                self.desenhar_texto(self.palavra_atual, FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2),
                )
                
                if self.correto:
                    self.desenhar_texto("✔️", FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2 + 200, ALTURA_JANELA // 2),
                    )
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            pygame.display.flip()