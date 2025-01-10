import pygame
import cv2 as cv
import time
from config import JANELA, IMAGEM_FUNDO, FONTE_TITULO, FONTE_BOTAO, BRANCO, CINZENTO, PRETO, LARGURA_JANELA, ALTURA_JANELA


class ModoAprender:
    def __init__(self, video, hand_detector):
        self.video = video
        self.hand_detector = hand_detector
        self.start_time = time.time()
        self.running = True
    
    
    def desenhar_texto(self, texto, fonte, cor, posicao):
        texto_superficie = fonte.render(texto, True, cor)
        texto_retangulo = texto_superficie.get_rect(center=posicao)
        JANELA.blit(texto_superficie, texto_retangulo)
        
        