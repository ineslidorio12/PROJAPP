import pygame
import sys
from config import JANELA, IMAGEM_FUNDO, FONTE_TITULO, FONTE_BOTAO, BRANCO, CINZENTO, PRETO, LARGURA_JANELA, ALTURA_JANELA
from video import VideoCaptureThread
from hand_detector import HandDetector
from modos.aprender import ModoAprender
from modos.treinar import ModoTreinar
from modos.desafio import ModoDesafio

video = VideoCaptureThread()
hand_detector = HandDetector(min_detection_confidence=0.5, min_tracking_confidence=0.5)
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
        
# menu_edit -------------------------------------------------------------------------------------------------------------
def menu_edit(opcoes):
    while True:
        JANELA.blit(IMAGEM_FUNDO, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        eventos = pygame.event.get()

        for opcao in opcoes:
            texto, cor_default, posicao, callback = opcao
            cor = CINZENTO if desenhar_texto(JANELA, texto, FONTE_BOTAO, cor_default, posicao).collidepoint(mouse_pos) else cor_default
            desenhar_texto(JANELA, texto, FONTE_BOTAO, cor, posicao)

        for event in eventos:
            if event.type == pygame.QUIT:
                sair()

            for opcao in opcoes:
                texto, _, posicao, callback = opcao
                if texto_clicado(texto, FONTE_BOTAO, posicao, event):
                    callback()

        pygame.display.flip()


# pagina principal -------------------------------------------------------------------------------------------------------

def pagina_inicial():
    menu_edit([
        ("JOGAR", BRANCO, (LARGURA_JANELA // 2, 370), menu_principal),
        ("SAIR", BRANCO, (LARGURA_JANELA // 2, 420), sair),
        
    ])
            
# menu inicial --------------------------------------------------------------------------------------------------------

def menu_principal():
    menu_edit([
        ("APRENDER", BRANCO, (LARGURA_JANELA // 2, 300), iniciar_aprender),
        ("TREINO", BRANCO, (LARGURA_JANELA // 2, 350), iniciar_treinar),
        ("DESAFIO", BRANCO, (LARGURA_JANELA // 2, 400), iniciar_desafio),
        ("PAGINA INICIAL", BRANCO, (LARGURA_JANELA // 2, 450), pagina_inicial),
        ("SAIR", BRANCO, (LARGURA_JANELA // 2, 500), sair),
    ])
        
# opcoes menu -----------------------------------------------------------------------------------------------------------

def iniciar_aprender():
    aprender = ModoAprender(video, hand_detector)
    aprender.executar()


def iniciar_treinar():
    treinar = ModoTreinar(video, hand_detector)
    treinar.executar()


def iniciar_desafio():
    desafio = ModoDesafio(video, hand_detector)
    desafio.executar()

def sair():
    pygame.quit()
    sys.exit()    
        
        
pagina_inicial()

