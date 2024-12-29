from utils.text import draw_text
from utils.buttons import draw_button

def desafio(screen, background_color):
    """Renderiza a tela do modo Desafio"""
    screen.fill(background_color)
    draw_text(screen, "Modo Desafio", 400, 300, size=50)

    # Botão para voltar ao menu
    if draw_button(screen, "VOLTAR", 300, 500, 200, 50):
        return "menu"

    return "desafio"
