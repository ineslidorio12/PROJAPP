import pygame
import cv2 as cv
import sys
from app.config import JANELA, IMAGEM_FUNDO, FONTE_TITULO, FONTE_BOTAO, BRANCO, CINZENTO, PRETO, LARGURA_JANELA, ALTURA_JANELA
from app.video import VideoCaptureThread
from app.hand_detector import HandDetector
from app.modos.aprender import ModoAprender
from app.modos.treinar import ModoTreinar
from app.modos.desafio import ModoDesafio
from body_detector import BodyGestureDetector

video = VideoCaptureThread()
hand_detector = HandDetector(min_detection_confidence=0.5, min_tracking_confidence=0.5)
body_detector = BodyGestureDetector()


# --------------------------------------------------------------
def mostrar_camera(frame):
    results = hand_detector.detect_hands(frame)
    hand_detector.draw_hands(frame, results)

    frame_resized = cv.resize(frame, (300, 225))
    frame_surface = pygame.image.frombuffer(frame_resized.tobytes(), frame_resized.shape[1::-1], "BGR")
    JANELA.blit(frame_surface, (LARGURA_JANELA - 320, ALTURA_JANELA - 250))

    return results

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
def menu_edit(opcoes, mostrar_video=False):
    while True:
        JANELA.blit(IMAGEM_FUNDO, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        eventos = pygame.event.get()

        for opcao in opcoes:
            texto, cor_default, posicao, callback = opcao
            cor = CINZENTO if desenhar_texto(JANELA, texto, FONTE_BOTAO, cor_default, posicao).collidepoint(mouse_pos) else cor_default
            desenhar_texto(JANELA, texto, FONTE_BOTAO, cor, posicao)
        
        if mostrar_video:
            ret, frame = video.cap.read()
            if ret:
                frame = cv.flip(frame, 1) 
                mostrar_camera(frame) 
                body_detector.detetar_gestos(frame) 

                if body_detector.ultimo_gesto == "braco_cruzado":
                    pagina_inicial()
                elif body_detector.ultimo_gesto == "braco_levantado":
                    iniciar_aprender()
                elif body_detector.ultimo_gesto == "inclinar_braco_direita":
                    iniciar_treinar()
                elif body_detector.ultimo_gesto == "inclinar_braco_esquerda":
                    iniciar_desafio()
                elif body_detector.ultimo_gesto == "saltar":
                    sair()
        
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
    ], mostrar_video=True)
        
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

