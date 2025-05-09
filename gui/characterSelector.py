import tkinter as tk
from tkinter import ttk
import os
from prompt import get_character_name
from game.map import GameMap  

class CharacterSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Eldoria - Selecció de Personatge")
        self.root.state("zoomed")
        self.root.configure(bg="#f5f5f5")

        self.color = "#FF6B35"
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Selecciona el teu personatge", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="#333").pack(pady=(40, 10))
        tk.Label(self.root, text="Tria un personatge per començar la teva aventura", font=("Arial", 12), bg="#f5f5f5", fg="#666").pack()

        center_frame = tk.Frame(self.root, bg="#f5f5f5")
        center_frame.pack(expand=True)

        characters = [
            ("Guerrer", self.select_guerrer),
            ("Mag", self.select_mag),
            ("Arquer", self.select_arquer),
            ("Lladre", self.select_lladre),
            ("Guaridor", self.select_guaridor)
        ]

        for text, cmd in characters:
            self.create_button(center_frame, text, cmd)

        tk.Label(self.root, text="Fet per Elías i Robert", font=("Arial", 10), bg="#f5f5f5", fg="#666").pack(side="bottom", pady=20)

    def create_button(self, parent, text, command):
        frame = tk.Frame(parent, bg=self.color)
        label = tk.Label(frame, text=text, font=("Arial", 12, "bold"), bg=self.color, fg="white", width=20, pady=12, cursor="hand2")
        label.pack()
        frame.pack(pady=10)

        frame.bind("<Button-1>", command)
        label.bind("<Button-1>", command)

        frame.bind("<Enter>", lambda e: self.root.config(cursor="hand2"))
        frame.bind("<Leave>", lambda e: self.root.config(cursor=""))
        label.bind("<Enter>", lambda e: self.root.config(cursor="hand2"))
        label.bind("<Leave>", lambda e: self.root.config(cursor=""))

    def select_guerrer(self, e=None):
        self.get_character_name("Guerrer")

    def select_mag(self, e=None):
        self.get_character_name("Mag")

    def select_arquer(self, e=None):
        self.get_character_name("Arquer")

    def select_lladre(self, e=None):
        self.get_character_name("Lladre")

    def select_guaridor(self, e=None):
        self.get_character_name("Guaridor")

    def get_character_name(self, character_type):
        name = get_character_name(self.root, character_type, self.color)
        if name:
            self.start_game(character_type, name)

    def start_game(self, character_type, character_name):
        self.root.withdraw()  # Oculta la ventana de selección de personaje
        game_window = tk.Toplevel()
        game_map = GameMap(game_window, character_type, character_name)
        game_window.protocol("WM_DELETE_WINDOW", self.on_game_close)
        game_window.mainloop()

    def on_game_close(self):
        self.root.destroy()  # Cierra la aplicación completamente cuando se cierra el juego

if __name__ == "__main__":
    root = tk.Tk()
    CharacterSelector(root)
    root.mainloop()