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
        # Inicialitzem la finestra principal del joc
        self.root = root
        self.root.title(f"Eldoria - {character_name} el {character_type}")  # Títol de la finestra
        self.root.state("zoomed")  # La finestra es mostrarà a pantalla completa
        self.root.config(bg="#ffb375")  # Color de fons

        # Configuració del mapa
        self.files = self.columnes = 10  # Mida del mapa, 10x10
        self.tamany = 60  # Tamany de cada casella
        self.caselles = {}  # Diccionari per emmagatzemar les caselles del mapa

        # Inicialització dels personatges i enemics
        self.jugador = Jugador(character_type, character_name)  # Creem el jugador
        self.enemics = Enemics(self.files, self.columnes)  # Generem els enemics aleatòriament

        # Configuració del frame i canvas per mostrar el mapa
        self.marc_principal = tk.Frame(self.root, bg="#ffb375")
        self.marc_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centrem el frame
        self.canvas = tk.Canvas(
            self.marc_principal,
            width=self.columnes * self.tamany,  # Amplada segons el nombre de columnes
            height=self.files * self.tamany,  # Alçada segons el nombre de files
            bg="#ffb375",  # Color de fons del canvas
            highlightthickness=0,  # Sense línia de contorn
        )
        self.canvas.pack()  # Afegeix el canvas a la finestra

        # Inicialitzem i dibuixem els elements al mapa
        self.generar_caselles()
        self.actualitzar_mapa()

        # Mapeig de tecles per moure el jugador
        movimientos = {
            "<w>": lambda e: self.mover_jugador(0, -1),  # Moure amunt
            "<s>": lambda e: self.mover_jugador(0, 1),   # Moure avall
            "<a>": lambda e: self.mover_jugador(-1, 0),  # Moure a l'esquerra
            "<d>": lambda e: self.mover_jugador(1, 0)    # Moure a la dreta
        }
        
        # Registra els esdeveniments de teclat per als moviments
        for tecla, funcion in movimientos.items():
            self.root.bind(tecla, funcion)

    def generar_caselles(self):
        # Genera un diccionari de caselles buides
        self.caselles = {(fila, col): "" for fila in range(self.files) for col in range(self.columnes)}

    def dibuixar_mapa(self):
        # Dibuixa el mapa al canvas
        self.canvas.delete("all")  # Elimina qualsevol element preexistent
        for (fila, col) in self.caselles:
            x1 = col * self.tamany  # Coordenada X de la casella
            y1 = fila * self.tamany  # Coordenada Y de la casella
            x2, y2 = x1 + self.tamany, y1 + self.tamany  # Calcula les cantonades de la casella
            # Dibuixa el rectangle per a cada casella
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#9c714e", outline="white")

    def dibuixar_jugador(self):
        # Dibuixa el jugador al mapa
        self.canvas.delete("jugador")  # Elimina el jugador anterior si n'hi ha
        x1 = self.jugador.x_pos * self.tamany  # Coordenada X del jugador
        y1 = self.jugador.y_pos * self.tamany  # Coordenada Y del jugador
        x2, y2 = x1 + self.tamany, y1 + self.tamany  # Calcula les cantonades del rectangle
        # Dibuixa el rectangle que representa el jugador (en color verd)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#4CAF50", outline="white", tags="jugador")

    def dibuixar_enemics(self):
        # Dibuixa els enemics al mapa
        for x, y in self.enemics.obtenir_posicions():  # Obtenim totes les posicions dels enemics
            x1 = x * self.tamany  # Coordenada X de l'enemic
            y1 = y * self.tamany  # Coordenada Y de l'enemic
            x2, y2 = x1 + self.tamany, y1 + self.tamany  # Calcula les cantonades
            # Dibuixa el rectangle per a cada enemic (en color vermell)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="white", tags="enemic")

    def mover_jugador(self, dx, dy):
        # Mou el jugador en funció de les tecles premudes
        new_x = self.jugador.x_pos + dx  # Nova coordenada X
        new_y = self.jugador.y_pos + dy  # Nova coordenada Y

        # Comprovem que la nova posició sigui dins dels límits del mapa
        if 0 <= new_x < self.columnes and 0 <= new_y < self.files:
            self.jugador.x_pos, self.jugador.y_pos = new_x, new_y  # Actualitzem la posició del jugador
            self.actualitzar_mapa()  # Actualitzem el mapa després de moure el jugador

            # Comprovem si el jugador ha arribat a una casella amb enemic
            if self.enemics.hay_enemigo(new_x, new_y):
                self.iniciar_combate()  # Si hi ha enemic, iniciem el combat

    def eliminar_enemigo(self, x, y):
        # Elimina un enemic de la posició (x, y)
        if self.enemics.hay_enemigo(x, y):
            del self.enemics.enemigos[(x, y)]  # Elimina l'enemic del diccionari
            self.actualitzar_mapa()  # Actualitza el mapa després de l'eliminació

    def iniciar_combate(self):
        # Inicia un combat amb l'enemic a la posició del jugador
        enemigo = self.enemics.obtener_enemigo(self.jugador.x_pos, self.jugador.y_pos)  # Obtenim l'enemic
        ventana_combate = VentanaCombate(self.root, self.jugador, enemigo, self)  # Creem la finestra de combat
        # Iniciem el combat després de crear la finestra de combat
        ventana_combate.combat.iniciar_combate()

    def actualitzar_mapa(self):
        # Actualitza el mapa dibuixant els elements
        self.dibuixar_mapa()  # Dibuixa el fons del mapa
        self.dibuixar_enemics()  # Dibuixa els enemics
        self.dibuixar_jugador()  # Dibuixa el jugador