import pygame

def draw_button(surface, text, x, y, width, height, color=(200, 200, 200), hover_color=(100, 149, 237)):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if click[0]:  # Clique detectado
            return True
    else:
        pygame.draw.rect(surface, color, (x, y, width, height))

    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surface, text_rect)
    return False
