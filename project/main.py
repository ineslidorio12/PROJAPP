import pygame
import sys
from screens.menu import menu
from screens.aprendizagem import aprendizagem
from screens.treino import treino
from screens.desafio import desafio

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Modos de Jogo")


WHITE = (255, 255, 255)

current_screen = "menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gerencia qual tela exibir
    if current_screen == "menu":
        current_screen = menu(screen, WHITE)
    elif current_screen == "aprendizagem":
        current_screen = aprendizagem(screen, WHITE)
    elif current_screen == "treino":
        current_screen = treino(screen, WHITE)
    elif current_screen == "desafio":
        current_screen = desafio(screen, WHITE)

    pygame.display.flip()