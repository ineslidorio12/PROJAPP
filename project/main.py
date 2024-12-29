import pygame
import sys

pygame.init()

# janela -----------------------------------
LARGURA_JANELA = 800
ALTURA_JANELA = 800
JANELA = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Tradutor Gestual")


WHITE = (255, 255, 255)
current_screen = "menu"


def handle_screen_transition(screen_name):
    
    if screen_name == "menu":
        return menu(screen, WHITE)    
    elif screen_name == "aprendizagem":
        return aprendizagem(screen, WHITE) 
    elif screen_name == "treino":
        return treino(screen, WHITE) 
    elif screen_name == "desafio":
        return desafio(screen, WHITE) 
    elif screen_name == "quit":
        return "quit"
    return screen_name
 
running = True   
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            current_screen = "quit"
            
    current_screen = handle_screen_transition(current_screen)
    
    if current_screen == "quit":
        running = False
        
    pygame.display.flip()

pygame.quit()
sys.exit()