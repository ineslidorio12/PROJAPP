import pygame
import sys

pygame.init()

# janela -----------------------------------
LARGURA_JANELA = 800
ALTURA_JANELA = 800
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Tradutor Gestual")

IMAGEM_FUNDO = pygame.image.load("project/assets/fundo.png")
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA_JANELA, ALTURA_JANELA))

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 122, 255)
CINZENTO = (79, 79, 79) 
ROSA = (219, 112, 147)

FONTE_TITULO = pygame.font.Font(None, 74)
FONTE_BOTAO = pygame.font.Font("project/utils/dogicapixel.ttf", 18)

def desenhar_texto(janela, texto, fonte, cor, posicao):
    texto_superficie = fonte.render(texto, True, cor)
    texto_retangulo = texto_superficie.get_rect(center=posicao)
    janela.blit(texto_superficie, texto_retangulo)


def texto_clicado(texto, fonte, posicao, event):
    texto_superficie = fonte.render(texto, True, BRANCO)
    texto_retangulo = texto_superficie.get_rect(center=posicao)
    
    if event.type == pygame.MOUSEBUTTONDOWN and texto_retangulo.collidepoint(event.pos):
        return True
    return False

def nova_janela(titulo):
    while True:
        JANELA.fill(PRETO)
        desenhar_texto(JANELA, titulo, FONTE_TITULO, PRETO, (LARGURA_JANELA // 2, ALTURA_JANELA // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        
        pygame.display.flip()

# menu inicial ----------------------------------------------------------------
def menu_principal():
    while True:
        JANELA.blit(IMAGEM_FUNDO, (0, 0))
        
        # desenhar_texto(JANELA, "Tradutor Gestual", FONTE_TITULO, BRANCO, (LARGURA_JANELA // 2, 100))

        pos_aprender = (LARGURA_JANELA // 2, 350)
        pos_treino = (LARGURA_JANELA // 2, 400)
        pos_desafio = (LARGURA_JANELA // 2, 450)
        
        desenhar_texto(JANELA, "APRENDER", FONTE_BOTAO, BRANCO, pos_aprender)
        desenhar_texto(JANELA, "TREINO", FONTE_BOTAO, BRANCO, pos_treino)
        desenhar_texto(JANELA, "DESAFIO", FONTE_BOTAO, BRANCO, pos_desafio)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if texto_clicado("Aprender", FONTE_BOTAO, pos_aprender, event):
                    nova_janela("Modo Aprender")
                if texto_clicado("Treino", FONTE_BOTAO, pos_treino, event):
                    nova_janela("Modo Treino")
                if texto_clicado("Desafio", FONTE_BOTAO, pos_desafio, event):
                    nova_janela("Modo Desafio")
                    
        pygame.display.flip()

menu_principal()