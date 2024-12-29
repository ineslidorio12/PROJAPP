import pygame

def draw_text(surface, text, x, y, size=30, color=(0, 0, 0)):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)
