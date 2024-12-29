from utils.buttons import draw_button
from utils.text import draw_text

def menu(screen, background_color):
    
    
    screen.fill(background_color)
    draw_text(screen, "Modos de Jogo", 400, 100, size=50)

    if draw_button(screen, "APRENDIZAGEM", 300, 200, 200, 50):
        return "aprendizagem"
    if draw_button(screen, "TREINO", 300, 300, 200, 50):
        return "treino"
    if draw_button(screen, "DESAFIO", 300, 400, 200, 50):
        return "desafio"
    if draw_button(screen, "SAIR", 300, 500, 200, 50):
        return "quit"

    return "menu"
