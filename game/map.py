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

        self.files = 10
        self.columnes = 10
        self.tamany = 60
        self.caselles = {}

        self.jugador = Jugador(character_type, character_name)
        self.enemics = Enemics(self.files, self.columnes)

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

        self.generar_caselles()
        self.dibuixar_mapa()
        self.dibuixar_jugador()
        self.dibuixar_enemics()

        self.root.bind("<w>", self.mover_arriba)
        self.root.bind("<s>", self.mover_abajo)
        self.root.bind("<a>", self.mover_izquierda)
        self.root.bind("<d>", self.mover_derecha)

    def generar_caselles(self):
        for fila in range(self.files):
            for col in range(self.columnes):
                self.caselles[(fila, col)] = ""

    def dibuixar_mapa(self):
        self.canvas.delete("all")
        for (fila, col), tipus in self.caselles.items():
            x1 = col * self.tamany
            y1 = fila * self.tamany
            x2 = x1 + self.tamany
            y2 = y1 + self.tamany
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#9c714e", outline="white")

    def dibuixar_jugador(self):
        self.canvas.delete("jugador")
        x1 = self.jugador.x_pos * self.tamany
        y1 = self.jugador.y_pos * self.tamany
        x2 = x1 + self.tamany
        y2 = y1 + self.tamany
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#4CAF50", outline="white", tags="jugador")

    def dibuixar_enemics(self):
        for x, y in self.enemics.obtenir_posicions():
            x1 = x * self.tamany
            y1 = y * self.tamany
            x2 = x1 + self.tamany
            y2 = y1 + self.tamany
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white", tags="enemic")

    def mover_jugador(self, dx, dy):
        new_x = self.jugador.x_pos + dx
        new_y = self.jugador.y_pos + dy

        if 0 <= new_x < self.columnes and 0 <= new_y < self.files:
            self.jugador.x_pos = new_x
            self.jugador.y_pos = new_y
            self.actualitzar_mapa()

            # Comprobar si hay un enemigo en la nueva posición
            if self.enemics.hay_enemigo(new_x, new_y):
                self.iniciar_combate()

    def eliminar_enemigo(self, x, y):
        if self.enemics.hay_enemigo(x, y):
            del self.enemics.enemigos[(x, y)]
            self.actualitzar_mapa()

    def iniciar_combate(self):
        enemigo = self.enemics.obtener_enemigo(self.jugador.x_pos, self.jugador.y_pos)
        ventana_combate = VentanaCombate(self.root, self.jugador, enemigo, self)
        combat = Combat(self.jugador, enemigo, ventana_combate)
        combat.iniciar_combate()

    def mover_arriba(self, event):
        self.mover_jugador(0, -1)

    def mover_abajo(self, event):
        self.mover_jugador(0, 1)

    def mover_izquierda(self, event):
        self.mover_jugador(-1, 0)

    def mover_derecha(self, event):
        self.mover_jugador(1, 0)

    def actualitzar_mapa(self):
        self.dibuixar_mapa()
        self.dibuixar_enemics()
        self.dibuixar_jugador()

if __name__ == "__main__":
    root = tk.Tk()
    mapa = GameMap(root, "Jugador", "Hero")
    root.mainloop()