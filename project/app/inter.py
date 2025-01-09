# pode ser considerado o main por enquanto
import pygame
import sys
import cv2 as cv
from config import JANELA, IMAGEM_FUNDO, FONTE_TITULO, FONTE_BOTAO, BRANCO, CINZENTO, PRETO, LARGURA_JANELA, ALTURA_JANELA
from video import VideoCaptureThread

# video_thread = VideoCaptureThread()

# --------------------------------------------------------------
def desenhar_texto(janela, texto, fonte, cor, posicao):
    texto_superficie = fonte.render(texto, True, cor)
    texto_retangulo = texto_superficie.get_rect(center=posicao)
    janela.blit(texto_superficie, texto_retangulo)
    return texto_retangulo

def texto_clicado(texto, fonte, posicao, event):
    texto_superficie = fonte.render(texto, True, BRANCO)
    texto_retangulo = texto_superficie.get_rect(center=posicao)
    
    if event.type == pygame.MOUSEBUTTONDOWN and texto_retangulo.collidepoint(event.pos):
        return True
    return False

def nova_janela(titulo):
    while True:
        JANELA.fill(PRETO)
        desenhar_texto(JANELA, titulo, FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        
        pygame.display.flip()
        
        
# pagina principal -------------------------------------------------------------------------------------------------------

def pagina_inicial():
    while True:
        JANELA.blit(IMAGEM_FUNDO, (0, 0))
        
        pos_jogar = (LARGURA_JANELA // 2, 370)
        pos_sair = (LARGURA_JANELA // 2, 420)
        
        mouse_pos = pygame.mouse.get_pos()
                
        cor_jogar = CINZENTO if desenhar_texto(JANELA, "JOGAR", FONTE_BOTAO, BRANCO, pos_jogar).collidepoint(mouse_pos) else BRANCO
        cor_sair = CINZENTO if desenhar_texto(JANELA, "SAIR", FONTE_BOTAO, BRANCO, pos_sair).collidepoint(mouse_pos) else BRANCO
        
        desenhar_texto(JANELA, "JOGAR", FONTE_BOTAO, cor_jogar, pos_jogar)
        desenhar_texto(JANELA, "SAIR", FONTE_BOTAO, cor_sair, pos_sair)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video_thread.stop()
                pygame.quit()
                sys.exit()
            
            if texto_clicado("SAIR", FONTE_BOTAO, pos_sair, event):
                video_thread.stop()
                pygame.quit()
                sys.exit()
            

        pygame.display.flip()
        
# menu inicial --------------------------------------------------------------------------------------------------------

def menu_principal():
    while True:
        JANELA.blit(IMAGEM_FUNDO, (0, 0))
        
        pos_aprender = (LARGURA_JANELA // 2, 300)
        pos_treino = (LARGURA_JANELA // 2, 350)
        pos_desafio = (LARGURA_JANELA // 2, 400)
        pos_inicial = (LARGURA_JANELA // 2, 450)
        pos_sair = (LARGURA_JANELA // 2, 500)
        
        mouse_pos = pygame.mouse.get_pos()
        
        cor_aprender = CINZENTO if desenhar_texto(JANELA, "APRENDER", FONTE_BOTAO, BRANCO, pos_aprender).collidepoint(mouse_pos) else BRANCO
        cor_treino = CINZENTO if desenhar_texto(JANELA, "TREINO", FONTE_BOTAO, BRANCO, pos_treino).collidepoint(mouse_pos) else BRANCO
        cor_desafio = CINZENTO if desenhar_texto(JANELA, "DESAFIO", FONTE_BOTAO, BRANCO, pos_desafio).collidepoint(mouse_pos) else BRANCO
        cor_inicial = CINZENTO if desenhar_texto(JANELA, "PAGINA INICIAL", FONTE_BOTAO, BRANCO, pos_inicial).collidepoint(mouse_pos) else BRANCO
        cor_sair = CINZENTO if desenhar_texto(JANELA, "SAIR", FONTE_BOTAO, BRANCO, pos_sair).collidepoint(mouse_pos) else BRANCO

        desenhar_texto(JANELA, "APRENDER", FONTE_BOTAO, cor_aprender, pos_aprender)
        desenhar_texto(JANELA, "TREINO", FONTE_BOTAO, cor_treino, pos_treino)
        desenhar_texto(JANELA, "DESAFIO", FONTE_BOTAO, cor_desafio, pos_desafio)
        desenhar_texto(JANELA, "PAGINA INICIAL", FONTE_BOTAO, cor_inicial, pos_inicial)
        desenhar_texto(JANELA, "SAIR", FONTE_BOTAO, cor_sair, pos_sair)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                video_thread.stop()
                pygame.quit()
                sys.exit()
            
            if texto_clicado("APRENDER", FONTE_BOTAO, pos_aprender, event):
                nova_janela("Modo Aprender")
            if texto_clicado("TREINO", FONTE_BOTAO, pos_treino, event):
                nova_janela("Modo Treino")
            if texto_clicado("DESAFIO", FONTE_BOTAO, pos_desafio, event):
                nova_janela("Modo Desafio")
            if texto_clicado("PAGINA INICIAL", FONTE_BOTAO, pos_inicial, event):
                return
            if texto_clicado("SAIR", FONTE_BOTAO, pos_sair, event):
                pygame.quit()
                sys.exit()
                    
        pygame.display.flip()
        
pagina_inicial()