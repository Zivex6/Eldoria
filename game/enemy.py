import random
from characters.character import Character

# Llista de possibles noms pels enemics
nombre_enemigos = ["Troll", "Orco", "Goblin", "Ogro"]

class Enemigo(Character):
    def __init__(self):
        # Constructor de la classe Enemigo
        nombre = random.choice(nombre_enemigos)  # Triem un nom aleatori de la llista
        super().__init__(nombre)  # Cridem al constructor de la classe pare (Character)
        # Vida aleatòria entre 50 i 100
        self.hp = self.hp_max = random.randint(50, 100)
        # Estadístiques aleatòries entre 5 i 15
        self.fortaleza = random.randint(5, 15)
        self.agilidad = random.randint(5, 15)
        self.bonuses = {}  # No tenen bonificadors especials

    def attack(self):
        # Atac de l'enemic, amb dany aleatori basat en la seva força
        damage = random.randint(self.fortaleza - 2, self.fortaleza + 2)
        # Retornem el dany i un número aleatori del 1 al 20 (com un d20 en jocs de rol)
        return damage, random.randint(1, 20)

    def defend(self):
        # Defensa de l'enemic basada només en la seva agilitat
        return self.agilidad

    @property
    def hp(self):
        # Getter de la propietat hp
        return self._hp

    @hp.setter
    def hp(self, value):
        # Setter de la propietat hp, assegurant que mai baixi de 0
        self._hp = max(0, value)

class Enemics:
    def __init__(self, files, columnes):
        # Constructor per gestionar tots els enemics del mapa
        self.enemigos = {}  # Diccionari que guardarà els enemics per posició (x,y)
        self.generar_enemigos(files, columnes)  # Generem enemics al crear l'objecte

    def generar_enemigos(self, files, columnes):
        # Generem enemics aleatòriament pel mapa
        num_enemigos = (files * columnes) // 10  # Aproximadament un 10% de les caselles tindran enemics
        for _ in range(num_enemigos):
            # Posició aleatòria
            x, y = random.randint(0, columnes - 1), random.randint(0, files - 1)
            # Ens assegurem que no hi hagi un enemic a la posició inicial del jugador (0,0)
            while x == 0 and y == 0:
                x, y = random.randint(0, columnes - 1), random.randint(0, files - 1)
            self.enemigos[(x, y)] = Enemigo()  # Creem un nou enemic en aquesta posició

    def hay_enemigo(self, x, y):
        # Comprova si hi ha un enemic en una posició determinada
        return (x, y) in self.enemigos

    def obtener_enemigo(self, x, y):
        # Obté l'enemic en una posició determinada (o None si no n'hi ha cap)
        return self.enemigos.get((x, y))

    def obtenir_posicions(self):
        # Retorna totes les posicions on hi ha enemics
        return self.enemigos.keys()

def determinar_iniciativa(jugador, enemigo):
    # Funció auxiliar per determinar qui comença en un combat
    # Retorna un número aleatori pel jugador i un altre per l'enemic
    return random.randint(1, 20), random.randint(1, 20)