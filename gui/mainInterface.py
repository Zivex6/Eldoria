import tkinter as tk
import os
import sys

# Afegim el directori principal del projecte al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class mainInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Eldoria")
        self.root.state("zoomed")
        self.root.configure(bg="#f5f5f5")

        self.color = "#FF6B35"
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Benvingut!!", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="#333").pack(pady=(40, 10))
        tk.Label(self.root, text="Selecciona una opció per començar", font=("Arial", 12), bg="#f5f5f5", fg="#666").pack()

        center_frame = tk.Frame(self.root, bg="#f5f5f5")
        center_frame.pack(expand=True)

        options = [
            ("Nova Partida", self.nova_partida),
            ("Carregar Partida", self.carregar_partida),
            ("Veure Resultats", self.veure_resultats),
            ("Tutorial", self.tutorial)
        ]

        for text, cmd in options:
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

    def nova_partida(self, e=None):
        self.root.quit()
        self.root.destroy()
        os.system(f"python {os.path.join(os.path.dirname(__file__), 'characterSelector.py')}")

    def carregar_partida(self, e=None):
        print("Carregant partida guardada")

    def veure_resultats(self, e=None):
        print("Mostrant resultats")

    def tutorial(self, e=None):
        print("Mostrant tutorial")

if __name__ == "__main__":
    root = tk.Tk()
    mainInterface(root)
    root.mainloop()