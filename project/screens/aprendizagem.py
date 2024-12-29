from utils.text import draw_text
from utils.buttons import draw_button

def aprendizagem(screen, background_color):
    """Renderiza a tela do modo Aprendizagem"""
    screen.fill(background_color)
    draw_text(screen, "Modo Aprendizagem", 400, 300, size=50)

    # Botão para voltar ao menu
    if draw_button(screen, "VOLTAR", 300, 500, 200, 50):
        return "menu"

    return "aprendizagem"
