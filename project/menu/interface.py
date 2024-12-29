import tkinter as tk
from tkinter import Label, Button
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
    
    image = Image.open("project/assets/titulo.png")
    image = image.resize((300,52), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label_title = Label(root, image=photo, bg=background_color)
    label_title.image = photo
    label_title.pack(pady=20)

    Button(root, text="Aprendizagem", font=("Arial", 16), 
           command=lambda: start_aprendizagem(root, background_color)).pack(pady=10, fill="x", padx=20)
    
    Button(root, text="Treino", font=("Arial", 16),
           command=lambda: start_treino(root, background_color)).pack(pady=10, fill="x", padx=20)
    
    Button(root, text="Desafio", font=("Arial", 16),
           command=lambda: start_desafio(root, background_color)).pack(pady=10, fill="x", padx=20)
    
    Button(root, text="Sair", font=("Arial", 16), 
           command=lambda: sair(root)).pack(pady=10, fill="x", padx=20)

# main app ----------------------------------------

def main():
    root = tk.Tk()
    root.title("Modos de Jogo")

    background_color = "#FFFFFF"
    root.configure(bg=background_color)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(False, False)

    main_menu(root, background_color)

    root.mainloop()

if __name__ == "__main__":
    main()