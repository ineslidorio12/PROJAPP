# edicoes basicas -----------------------------------------
import pygame

pygame.init()

info = pygame.display.Info()
LARGURA_JANELA = info.current_w
ALTURA_JANELA = info.current_h
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), pygame.FULLSCREEN)

pygame.display.set_caption("Tradutor Gestual")

IMAGEM_FUNDO = pygame.image.load("project/assets/fundo.png")
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA_JANELA, ALTURA_JANELA))

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZENTO = (79, 79, 79) 

FONTE_TITULO = pygame.font.Font("project/utils/dogicapixel.ttf", 36)
FONTE_BOTAO = pygame.font.Font("project/utils/dogicapixel.ttf", 18)
