import pygame
import sys

pygame.init()

# janela -----------------------------------
LARGURA_JANELA = 800
ALTURA_JANELA = 800
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Tradutor Gestual")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 122, 255)
CINZENTO = (79, 79, 79)
ROSA = (219, 112, 147)

FONTE_TITULO = pygame.font.Font(None, 74)
FONTE_BOTAO = pygame.font.Font(None, 74)

def desenhar_texto(janela, texto, fonte, cor, posicao):
    texto_superficie = fonte.render(texto, True, cor)
    texto_retangulo = texto_superficie.get_rect(center=posicao)
    janela.blit(texto_superficie, texto_retangulo)


def menu_principal():
    while True:
        JANELA.fill(BRANCO)
        
        desenhar_texto(JANELA, "Tradutor Gestual", FONTE_TITULO, PRETO, (LARGURA_JANELA // 2, 100))

        espaco_vertical = 100
        botao_aprender = pygame.Rect(LARGURA_JANELA // 2 - 150, 200, 300, 60)
        botao_treino = pygame.Rect(LARGURA_JANELA // 2 - 150, 200 + espaco_vertical, 300, 60)
        botao_desafio = pygame.Rect(LARGURA_JANELA // 2 - 150, 200 + 2 * espaco_vertical, 300, 60)
 
        pygame.draw.rect(JANELA, AZUL, botao_aprender)
        pygame.draw.rect(JANELA, AZUL, botao_treino)
        pygame.draw.rect(JANELA, AZUL, botao_desafio)
        
        desenhar_texto(JANELA, "Aprender", FONTE_BOTAO, BRANCO, botao_aprender.center)
        desenhar_texto(JANELA, "Treino", FONTE_BOTAO, BRANCO, botao_treino.center)
        desenhar_texto(JANELA, "Desafio", FONTE_BOTAO, BRANCO, botao_desafio.center)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_aprender.collidepoint(event.pos):
                    print("Aprender Clicado")
                if botao_treino.collidepoint(event.pos):
                    print("Treino Clicado")
                if botao_desafio.collidepoint(event.pos):
                    print("Desafio Clicado")
                    
        pygame.display.flip()

menu_principal()