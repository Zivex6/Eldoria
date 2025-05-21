import tkinter as tk
from game.gameplay import Jugador
from game.enemy import Enemics
from gui.attack import VentanaCombate
from game.combat import Combat

from characters.guerrer import Guerrer
from characters.mag import Mag
from characters.arquer import Arquer
from characters.lladre import Lladre
from characters.guaridor import Guaridor

class GameMap:
    def __init__(self, root, character_type, character_name):
        self.root = root
        self.root.title(f"Eldoria - {character_name} el {character_type}")
        self.root.state("zoomed")
        self.root.config(bg="#ffb375")

        # Configuración del mapa
        self.files = self.columnes = 10
        self.tamany = 60
        self.caselles = {}

        # Inicialización de personajes
        self.jugador = Jugador(character_type, character_name)
        self.enemics = Enemics(self.files, self.columnes)

        # Configuración del canvas
        self.marc_principal = tk.Frame(self.root, bg="#ffb375")
        self.marc_principal.place(relx=0.5, rely=0.5, anchor="center")
        self.canvas = tk.Canvas(
            self.marc_principal,
            width=self.columnes * self.tamany,
            height=self.files * self.tamany,
            bg="#ffb375",
            highlightthickness=0,
        )
        self.canvas.pack()

        # Inicializar y dibujar elementos
        self.generar_caselles()
        self.actualitzar_mapa()

        # Mapeo de teclas de movimiento
        movimientos = {
            "<w>": lambda e: self.mover_jugador(0, -1),
            "<s>": lambda e: self.mover_jugador(0, 1),
            "<a>": lambda e: self.mover_jugador(-1, 0),
            "<d>": lambda e: self.mover_jugador(1, 0)
        }
        
        # Registrar eventos de teclado
        for tecla, funcion in movimientos.items():
            self.root.bind(tecla, funcion)

    def generar_caselles(self):
        self.caselles = {(fila, col): "" for fila in range(self.files) for col in range(self.columnes)}

    def dibuixar_mapa(self):
        self.canvas.delete("all")
        for (fila, col) in self.caselles:
            x1 = col * self.tamany
            y1 = fila * self.tamany
            x2, y2 = x1 + self.tamany, y1 + self.tamany
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#9c714e", outline="white")

    def dibuixar_jugador(self):
        self.canvas.delete("jugador")   
        x1 = self.jugador.x_pos * self.tamany
        y1 = self.jugador.y_pos * self.tamany
        x2, y2 = x1 + self.tamany, y1 + self.tamany
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#4CAF50", outline="white", tags="jugador")

    def dibuixar_enemics(self):
        for x, y in self.enemics.obtenir_posicions():
            x1 = x * self.tamany
            y1 = y * self.tamany
            x2, y2 = x1 + self.tamany, y1 + self.tamany
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white", tags="enemic")

    def mover_jugador(self, dx, dy):
        new_x = self.jugador.x_pos + dx
        new_y = self.jugador.y_pos + dy

        if 0 <= new_x < self.columnes and 0 <= new_y < self.files:
            self.jugador.x_pos, self.jugador.y_pos = new_x, new_y
            self.actualitzar_mapa()

            if self.enemics.hay_enemigo(new_x, new_y):
                self.iniciar_combate()

    def eliminar_enemigo(self, x, y):
        if self.enemics.hay_enemigo(x, y):
            del self.enemics.enemigos[(x, y)]
            self.actualitzar_mapa()

    def iniciar_combate(self):
        enemigo = self.enemics.obtener_enemigo(self.jugador.x_pos, self.jugador.y_pos)
        ventana_combate = VentanaCombate(self.root, self.jugador, enemigo, self)
        # Iniciar el combate después de crear la ventana
        ventana_combate.combat.iniciar_combate()

    def actualitzar_mapa(self):
        self.dibuixar_mapa()
        self.dibuixar_enemics()
        self.dibuixar_jugador()

if __name__ == "__main__":
    root = tk.Tk()
    GameMap(root)
    root.mainloop()