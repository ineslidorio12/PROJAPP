import tkinter as tk
from tkinter import Label, Button, Frame
from PIL import Image, ImageTk

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()
        
# pagina de cada modo ----------------------------------
def start_aprendizagem(root, background_color):
    clear_window(root)
    label = Label(root, text="Modo Aprendizagem", font=("Arial", 24), bg=background_color)
    label.pack(pady=20)
    back_button = Button(root, text="Voltar", font=("Arial", 16), command=lambda: main_menu(root, background_color))
    back_button.pack(pady=10)    
        
def start_treino(root, background_color):
    clear_window(root)
    label = Label(root, text="Modo Treino", font=("Arial", 24), bg=background_color)
    label.pack(pady=20)
    back_button = Button(root, text="Voltar", font=("Arial", 16), command=lambda: main_menu(root, background_color))
    back_button.pack(pady=10)    
        
def start_desafio(root, background_color): 
    clear_window(root)
    label = Label(root, text="Modo Desafio", font=("Arial", 24), bg=background_color)
    label.pack(pady=20)
    back_button = Button(root, text="Voltar", font=("Arial", 16), command=lambda: main_menu(root, background_color))
    back_button.pack(pady=10)    
        
def sair(root):
    root.destroy()
    
# menu ------------------------------------

def main_menu(root, background_color):
    clear_window(root)

    # centro
    frame = Frame(root, bg=background_color, padx=0, pady=0)
    frame.pack(expand=True)

    label_title = Label(frame, text="Modos de Jogo", font=("Arial", 20, "bold"), bg=background_color)
    label_title.pack(pady=10)

    Button(frame, text="APRENDIZAGEM", font=("Arial", 14), 
           command=lambda: start_aprendizagem(root, background_color)).pack(pady=10, fill="both", padx=10)
    
    Button(frame, text="TREINO", font=("Arial", 14),
           command=lambda: start_treino(root, background_color)).pack(pady=10, fill="both", padx=10)
    
    Button(frame, text="DESAFIO", font=("Arial", 14),
           command=lambda: start_desafio(root, background_color)).pack(pady=10, fill="both", padx=10)
    
    Button(frame, text="Sair", font=("Arial", 14), 
           command=root.quit).pack(pady=10, fill="both", padx=10)

# main app ----------------------------------------

def main():
    root = tk.Tk()
    root.title("Modos de Jogo")

    background_color = "#FFFFFF"
    root.configure(bg=background_color)
    root.attributes("-fullscreen", True)

    main_menu(root, background_color)
    root.mainloop()

if __name__ == "__main__":
    main()